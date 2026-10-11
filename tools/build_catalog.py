"""Render the catalog page from the extracted brand profiles.

Usage: python3 -I build_catalog.py <profiles_json> <template_html> <out_html> <skill_name>
                                   [standalone_html] [--skill-dir DIR]

<skill_dir> defaults to the folder of <standalone_html> (the skill root, where GitHub Pages
serves katalog.html from) and otherwise to the folder of <out_html>. It is read for
`designsprache/<slug>.md` (the design-language profile) and `screens/<slug>.png` / `.html`
(the sample screens); thumbnails are written to `screens/klein/<slug>.webp`.
"""
import json
import pathlib
import re
import sys

THUMB_W = 680
THUMB_QUALITY = 78
# The render is 1346x988: stage padding, a caption row, the three 844 px phones, a footnote.
# For the small card the captions and the footnote are unreadable noise, so the thumbnail keeps
# only the phone band (the catalog CSS uses the resulting 1346:862 ratio).
CROP_BOX = (0, 66, 1346, 928)
CROP_REF = (1346, 988)
# Front-matter keys taken over into the catalog. Values may carry '#', ':' and quotes,
# so the header is parsed line by line instead of with a YAML parser.
FM_KEYS = ("marke", "website", "ansatz", "ansatz2", "modus", "aufbau", "navigation",
           "komponenten", "icons", "bewegung", "schrift")
KEY_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*)\s*:\s*(.*)$")


def parse_front_matter(text):
    """Read a YAML-ish header robustly: first `---` block, one `key: value` per line."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fm, key = {}, None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith((" ", "\t")) and key:          # continuation of the line before
            fm[key] = (fm[key] + " " + line.strip()).strip()
            continue
        m = KEY_RE.match(line)
        if not m:
            key = None
            continue
        key, val = m.group(1).lower(), m.group(2).strip()
        if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
            val = val[1:-1]
        fm[key] = val.strip()
    return fm


def make_thumb(png, thumb):
    """Scale the screens PNG down to a small WebP; skip when the thumbnail is current."""
    if thumb.exists() and thumb.stat().st_mtime >= png.stat().st_mtime:
        return "ok"
    try:
        from PIL import Image
    except ImportError:
        return "no-pillow"
    try:
        with Image.open(png) as im:
            im = im.convert("RGB")
            ratio = im.width / im.height
            if 1.30 <= ratio <= 1.45:                      # the expected three-phone render
                k = im.height / CROP_REF[1]
                im = im.crop(tuple(round(v * k) for v in CROP_BOX))
            h = max(1, round(im.height * THUMB_W / im.width))
            small = im.resize((THUMB_W, h), Image.LANCZOS)
        thumb.parent.mkdir(parents=True, exist_ok=True)
        small.save(thumb, "WEBP", quality=THUMB_QUALITY, method=6)
        return "neu"
    except OSError as exc:
        print(f"PROBLEM thumbnail {png.name}: {exc}")
        return "fehler"


args = [a for a in sys.argv[1:]]
skill_dir = None
if "--skill-dir" in args:
    i = args.index("--skill-dir")
    if i + 1 >= len(args):
        sys.exit("--skill-dir braucht einen Ordner")
    skill_dir = pathlib.Path(args[i + 1])
    del args[i:i + 2]
for a in args:
    if a.startswith("--skill-dir="):
        skill_dir = pathlib.Path(a.split("=", 1)[1])
args = [a for a in args if not a.startswith("--")]
if len(args) < 4:
    sys.exit(__doc__)

profiles = json.loads(pathlib.Path(args[0]).read_text(encoding="utf-8"))
tpl = pathlib.Path(args[1]).read_text(encoding="utf-8")
out = pathlib.Path(args[2])
name = args[3]
standalone = pathlib.Path(args[4]) if len(args) > 4 else None
if skill_dir is None:
    skill_dir = (standalone or out).resolve().parent

sprache_dir = skill_dir / "designsprache"
screens_dir = skill_dir / "screens"
thumb_dir = screens_dir / "klein"

keys = ["slug", "name", "cat", "blurb", "mode", "light", "dark", "inkLight", "inkDark", "primary",
        "onPrimary", "ghost", "radius", "swatches", "font", "generic", "weight", "tracking", "upper"]
data, stats = [], dict(profil=0, shot=0, live=0, neu=0)
for p in profiles:
    slug = p["slug"]
    d = {k: p[k] for k in keys}

    fm = {}
    prof = sprache_dir / f"{slug}.md"
    if prof.is_file():
        fm = parse_front_matter(prof.read_text(encoding="utf-8"))
        if fm:
            stats["profil"] += 1
            d["profil"] = 1
    for k in FM_KEYS:
        v = fm.get(k, "")
        if v:
            d[k] = v

    png = screens_dir / f"{slug}.png"
    if png.is_file():
        d["shot"] = 1
        stats["shot"] += 1
        res = make_thumb(png, thumb_dir / f"{slug}.webp")
        if res == "neu":
            stats["neu"] += 1
        if res in ("ok", "neu"):
            d["thumb"] = 1
    if (screens_dir / f"{slug}.html").is_file():
        d["live"] = 1
        stats["live"] += 1
    data.append(d)

payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

assert tpl.count("/*DATA*/[]") == 1
html = tpl.replace("/*DATA*/[]", payload).replace("__CMD__", name)
out.write_text(html, encoding="utf-8")
print(f"{out}: {len(data)} designs, {len(html.encode()) // 1024} KB")
print(f"skill-dir {skill_dir}: {stats['profil']} Profile, {stats['shot']} Musterscreens, "
      f"{stats['live']} live, {stats['neu']} Vorschaubilder neu")
missing = [d["slug"] for d in data if not d.get("shot")]
if missing:
    print(f"ohne Musterscreens ({len(missing)}): {' '.join(missing)}")

# Standalone copy for opening locally (the artifact host adds this skeleton itself).
if standalone:
    standalone.write_text(
        '<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<style>:root{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
        '</head>\n<body>\n' + html + '\n</body>\n</html>\n', encoding="utf-8")
    print(f"{standalone}: standalone copy")
