"""Extract a compact visual profile (surfaces, text, button, swatches, font) per brand for the catalog page.

Usage: python3 -I extract_tokens.py <skill_dir> <out_json>
"""
import json
import pathlib
import re
import sys

import yaml

skill = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])

# The ten files without a YAML header, read by hand from their sections 2-4.
LEGACY = {
    "kraken": dict(light="#ffffff", inkLight="#101114", primary="#7132f5", onPrimary="#ffffff", radius=12,
                   swatches=["#ffffff", "#101114", "#7132f5", "#5741d8", "#686b82", "#149e61"],
                   font="Kraken-Brand", weight=700, tracking=-0.02),
    "lamborghini": dict(dark="#000000", inkDark="#ffffff", primary="#ffc000", onPrimary="#000000", radius=0,
                        swatches=["#000000", "#ffffff", "#ffc000", "#917300", "#202020", "#29abe2"],
                        font="LamboType", weight=400, tracking=0),
    "lovable": dict(light="#f7f4ed", inkLight="#1c1c1c", primary="#1c1c1c", onPrimary="#fcfbf8", radius=6,
                    swatches=["#f7f4ed", "#1c1c1c", "#fcfbf8", "#5f5f5d", "#eceae4", "#3b82f6"],
                    font="Camera Plain Variable", weight=600, tracking=-0.025),
    "mastercard": dict(light="#f3f0ee", inkLight="#141413", primary="#141413", onPrimary="#ffffff", radius=20,
                       swatches=["#f3f0ee", "#141413", "#cf4500", "#f37338", "#9a3a0a", "#fcfbfa"],
                       font="MarkForMC", weight=500, tracking=-0.02),
    "runwayml": dict(dark="#000000", inkDark="#ffffff", light="#e9ecf2", inkLight="#000000", primary="#ffffff",
                     onPrimary="#000000", radius=4,
                     swatches=["#000000", "#ffffff", "#1a1a1a", "#e9ecf2", "#767d88", "#c9ccd1"],
                     font="abcNormal", weight=400, tracking=-0.025),
    "sanity": dict(dark="#0b0b0b", inkDark="#ffffff", primary="#f36458", onPrimary="#ffffff", radius=9999,
                   swatches=["#0b0b0b", "#ffffff", "#f36458", "#0052ef", "#55beff", "#212121"],
                   font="waldenburgNormal", weight=400, tracking=-0.04),
    "spotify": dict(dark="#121212", inkDark="#ffffff", primary="#1ed760", onPrimary="#000000", radius=9999,
                    swatches=["#121212", "#ffffff", "#1ed760", "#181818", "#b3b3b3", "#539df5"],
                    font="SpotifyMixUI", weight=700, tracking=-0.01),
    "starbucks": dict(light="#f2f0eb", inkLight="#1e3932", primary="#00754a", onPrimary="#ffffff", radius=9999,
                      swatches=["#f2f0eb", "#1e3932", "#006241", "#00754a", "#d4e9e2", "#cba258"],
                      font="SoDoSans", weight=600, tracking=0),
    "tesla": dict(light="#ffffff", inkLight="#171a20", primary="#3e6ae1", onPrimary="#ffffff", radius=4,
                  swatches=["#ffffff", "#171a20", "#3e6ae1", "#393c41", "#5c5e62", "#f4f4f4"],
                  font="Universal Sans Display", weight=500, tracking=0),
    "theverge": dict(dark="#131313", inkDark="#ffffff", primary="#3cffd0", onPrimary="#000000", radius=9999,
                     swatches=["#131313", "#ffffff", "#3cffd0", "#5200ff", "#2d2d2d", "#949494"],
                     font="Manuka", weight=900, tracking=0.01),
}
MODE_OVERRIDE = {"apple": "gemischt"}
# Hero surface named in the file's description but not picked up by the key heuristics.
SURFACE_OVERRIDE = {"superhuman": {"dark": "#1b1938"}}
UPPER = {"bugatti", "spacex", "bmw-m", "vodafone", "lamborghini", "nike"}
SERIF_NAMES = re.compile(r"serif|editorial|domaine|tiempos|copernicus|garamond|times|georgia|wired", re.I)
HEX = re.compile(r"#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?|#[0-9a-fA-F]{3}")
LIGHT_KEYS = ["canvas", "canvas-light", "surface-canvas-light", "background", "surface", "canvas-soft", "canvas-cream"]
DARK_KEYS = ["canvas-dark", "canvas-night", "surface-canvas-dark", "surface-dark", "surface-night", "canvas",
             "inverse-canvas", "surface-card-dark", "charcoal", "ink"]
INK_LIGHT_KEYS = ["ink", "ink-deep", "text", "body-on-light", "on-light", "body-strong", "body"]
INK_DARK_KEYS = ["on-dark", "inverse-ink", "ink", "body", "text", "on-primary"]


def norm_hex(v):
    if not isinstance(v, str) or not HEX.fullmatch(v.strip()):
        return None
    v = v.strip().lower()
    if len(v) == 4:
        v = "#" + "".join(c * 2 for c in v[1:])
    return v[:7]


def rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def lum(h):
    def ch(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def close(a, b, tol=28):
    return sum((x - y) ** 2 for x, y in zip(rgb(a), rgb(b))) ** 0.5 < tol


def resolve(v, fm, depth=0):
    if isinstance(v, str) and depth < 5:
        m = re.fullmatch(r"\{(\w+)\.([\w.-]+)\}", v.strip())
        if m:
            grp, key = m.groups()
            return resolve((fm.get(grp) or {}).get(key), fm, depth + 1)
    return v


def px(v):
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        m = re.match(r"\s*(-?[\d.]+)\s*(px|rem|em)?", v)
        if m:
            n = float(m.group(1))
            return n * 16 if m.group(2) in ("rem", "em") else n
    return None


def index_entries(text):
    entries, cat, on = [], None, False
    for line in text.splitlines():
        if line.startswith("## Index"):
            on = True
            continue
        if not on:
            continue
        m = re.match(r"^### (.+)$", line)
        if m:
            cat = m.group(1)
            continue
        m = re.match(r"^- `([^`]+)` — \*\*([^*]+)\*\*: (.+)$", line)
        if m:
            # Ansatz und Aufbau stehen im Katalog in eigenen Feldern (aus dem Profil),
            # darum hier nur die Kurzbeschreibung bis zum Zusatz "Ansatz: …".
            blurb = re.split(r"\s+Ansatz:\s", m.group(3))[0].rstrip(" ;,")
            entries.append(dict(slug=m.group(1), name=m.group(2), cat=cat, blurb=blurb))
    return entries


def mode_of(slug, blurb):
    if slug in MODE_OVERRIDE:
        return MODE_OVERRIDE[slug]
    b = blurb.lower()
    if b.startswith("retro"):
        return "retro"
    if b.startswith("hell"):
        return "hell"
    if b.startswith("dunkel,") or b.startswith("dunkel "):
        return "dunkel"
    return "gemischt"


def first(colors, keys, test):
    for k in keys:
        c = colors.get(k)
        if c and test(c):
            return c
    return None


def from_yaml(fm):
    colors = {k: norm_hex(v) for k, v in (fm.get("colors") or {}).items()}
    colors = {k: v for k, v in colors.items() if v}
    comps = fm.get("components") or {}
    btn_key = next((k for k in comps if "button" in k and "primary" in k), None) \
        or next((k for k in comps if "button" in k), None)
    btn = comps.get(btn_key) or {}

    light = first(colors, LIGHT_KEYS, lambda c: lum(c) > 0.45)
    dark = first(colors, DARK_KEYS, lambda c: lum(c) < 0.06)
    ink_light = first(colors, INK_LIGHT_KEYS, lambda c: light and contrast(c, light) >= 4.5) if light else None
    ink_dark = first(colors, INK_DARK_KEYS, lambda c: dark and contrast(c, dark) >= 4.5) if dark else None

    bg_raw = resolve(btn.get("backgroundColor"), fm)
    primary = norm_hex(bg_raw)
    ghost = isinstance(bg_raw, str) and bg_raw.strip().lower() == "transparent"
    if not primary and not ghost:
        primary = colors.get("primary")
    on_primary = norm_hex(resolve(btn.get("textColor"), fm)) or colors.get("on-primary")
    radius = px(resolve(btn.get("rounded"), fm))
    if radius is None:
        radius = px((fm.get("rounded") or {}).get("md"))

    typo = fm.get("typography") or {}
    tkey = next((k for k in typo if re.search(r"display|hero|headline|h1", k)), next(iter(typo), None))
    t = typo.get(tkey) or {}
    fam = str(t.get("fontFamily", ""))
    font = fam.split(",")[0].strip().strip("'\"") if fam else ""
    try:
        weight = int(re.match(r"\s*(\d+)", str(t.get("fontWeight", 400))).group(1))
    except (AttributeError, ValueError):
        weight = 400
    ls, size = t.get("letterSpacing"), px(t.get("fontSize"))
    tracking = 0.0
    if isinstance(ls, str) and ls.strip().endswith("em"):
        tracking = float(re.match(r"\s*(-?[\d.]+)", ls).group(1))
    elif px(ls) is not None and size:
        tracking = px(ls) / size

    sw = []
    for c in (light, dark, ink_light, primary):
        if c and not any(close(c, s) for s in sw):
            sw.append(c)
    prio = sorted(colors, key=lambda k: (
        0 if re.match(r"(accent|brand|secondary|tertiary|link)", k) else
        1 if re.match(r"(primary-deep|primary-soft|surface-dark|canvas-dark|inverse)", k) else
        2 if re.match(r"(surface|canvas)", k) else 3))
    for k in prio:
        if len(sw) >= 6:
            break
        c = colors[k]
        if not any(close(c, s) for s in sw):
            sw.append(c)
    return dict(light=light, dark=dark, inkLight=ink_light, inkDark=ink_dark, primary=primary,
                onPrimary=on_primary, ghost=ghost, radius=radius, swatches=sw, font=font, fontStack=fam,
                weight=weight, tracking=tracking)


text = (skill / "SKILL.md").read_text(encoding="utf-8")
result, problems = [], []
for e in index_entries(text):
    slug = e["slug"]
    body = (skill / "references" / f"{slug}.md").read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", body, re.S)
    if slug in LEGACY:
        prof = {"ghost": False, "fontStack": LEGACY[slug]["font"], **LEGACY[slug]}
    elif m:
        # Drop free-text keys: unquoted colons inside them break YAML (and raycast has a stray "属于:" line).
        fm_text = re.sub(r"^(description|属于):.*\n(?:[ \t]+.*\n)*", "", m.group(1) + "\n", flags=re.M)
        try:
            prof = from_yaml(yaml.safe_load(fm_text))
        except yaml.YAMLError as exc:
            problems.append(f"{slug}: YAML error {exc}")
            continue
    else:
        problems.append(f"{slug}: no YAML and no manual entry")
        continue

    mode = mode_of(slug, e["blurb"])
    light, dark = prof.get("light"), prof.get("dark")
    if mode == "retro" and m:
        canvas = norm_hex((yaml.safe_load(fm_text).get("colors") or {}).get("canvas"))
        light = canvas or light
    light, dark = SURFACE_OVERRIDE.get(slug, {}).get("light", light), SURFACE_OVERRIDE.get(slug, {}).get("dark", dark)
    if mode in ("hell", "retro") and not light:
        light = "#ffffff"
    if mode == "dunkel" and not dark:
        dark = "#000000"
    if mode == "gemischt":
        light, dark = light or "#ffffff", dark or "#0a0a0a"
    ink_light = prof.get("inkLight") or ("#111111" if light else None)
    ink_dark = prof.get("inkDark") or ("#ffffff" if dark else None)
    if mode in ("hell", "retro"):
        dark, ink_dark = None, None
    if mode == "dunkel":
        light, ink_light = None, None

    primary, on_primary, ghost = prof.get("primary"), prof.get("onPrimary"), prof.get("ghost", False)
    base = dark if mode == "dunkel" else light
    if primary and on_primary and contrast(primary, on_primary) < 2:
        ghost = True
    if ghost:
        primary = None
        on_primary = ink_dark if mode == "dunkel" else (ink_light or ink_dark)
    if not ghost and not on_primary:
        on_primary = "#ffffff" if lum(primary) < 0.4 else "#000000"
    radius = prof.get("radius")
    radius = 8 if radius is None else min(9999, radius)

    stack = prof.get("fontStack", "")
    generic = "mono" if re.search(r"mono", stack, re.I) else (
        "serif" if re.search(r"(?<!sans-)serif", stack) or SERIF_NAMES.search(prof.get("font", "")) else "sans")
    result.append({
        **e, "mode": mode, "light": light, "dark": dark, "inkLight": ink_light, "inkDark": ink_dark,
        "primary": primary, "onPrimary": on_primary, "ghost": ghost, "radius": radius,
        "swatches": prof["swatches"][:6], "font": prof.get("font", ""), "generic": generic,
        "weight": max(100, min(900, prof.get("weight", 400))),
        "tracking": round(max(-0.06, min(0.12, prof.get("tracking", 0))), 3),
        "upper": slug in UPPER,
    })

out.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"profiles: {len(result)}")
for p in problems:
    print("PROBLEM", p)
for r in result:
    btn = "ghost" if r["ghost"] else f"{r['primary']}/{r['onPrimary']}"
    print(f"{r['slug']:14} {r['mode']:8} light={r['light']} ink={r['inkLight']} dark={r['dark']} "
          f"inkD={r['inkDark']} btn={btn:17} r={r['radius']:<6} {r['generic']:5} w={r['weight']} "
          f"up={int(r['upper'])} font={r['font'][:20]}")
