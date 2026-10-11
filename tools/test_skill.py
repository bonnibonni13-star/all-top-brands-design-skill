"""Prüft den gebauten Skill-Ordner auf Vollständigkeit und Stimmigkeit.

Aufruf: python3 -I test_skill.py <skill_dir> <repo_dir>
  <repo_dir> ist ein Klon von VoltAgent/awesome-design-md (Quelle der DESIGN.md-Dateien).
"""
import hashlib
import pathlib
import re
import sys

ANSAETZE = {"buehne", "regale", "galerie", "werkzeug", "editorial", "daten",
            "verspielt", "plakativ", "minimal", "leuchten", "retro"}
KOPF_PFLICHT = ("slug", "marke", "website", "ansatz", "modus", "aufbau",
                "navigation", "komponenten", "icons", "bewegung", "schrift")
TOOL_FILES = ("SKILL.template.md", "build_skill.py", "extract_tokens.py", "build_catalog.py",
              "katalog.template.html", "render_screens.py", "live_screens.py", "build_vorschau.py",
              "screens/ANLEITUNG.md", "screens/base.css", "vorschau/vorlage.html", "vorschau/icons.js",
              "test_skill.py")
ERWARTET = 74

skill = pathlib.Path(sys.argv[1])
repo = pathlib.Path(sys.argv[2])
text = (skill / "SKILL.md").read_text(encoding="utf-8")
fails = []


def kopfdaten(path):
    m = re.match(r"---\n(.*?)\n---", path.read_text(encoding="utf-8"), re.S)
    data = {}
    if m:
        for line in m.group(1).splitlines():
            k, sep, v = line.partition(":")
            if sep:
                data[k.strip()] = v.strip()
    return data


# --- Kopf der SKILL.md -------------------------------------------------------
m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
if not m:
    fails.append("kein Frontmatter")
else:
    fm = dict(line.split(": ", 1) for line in m.group(1).splitlines())
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        fails.append(f"name nicht kebab-case: {name!r}")
    if re.search(r"claude|anthropic", name):
        fails.append("name enthält ein reserviertes Wort")
    if not desc or len(desc) > 1024 or "<" in desc or ">" in desc:
        fails.append(f"description ungültig (Länge {len(desc)})")
    print(f"name={name} description_len={len(desc)}")

if "<!-- INDEX -->" in text:
    fails.append("Index-Markierung in SKILL.md übrig")

# --- Index gegen references/ -------------------------------------------------
indexed = re.findall(r"^- `([^`]+)` — \*\*", text, re.M)
files = sorted(p.stem for p in (skill / "references").glob("*.md"))
if sorted(indexed) != files:
    fails.append(f"Index/Dateien weichen ab: {sorted(set(indexed) ^ set(files))}")
if len(indexed) != len(set(indexed)):
    fails.append("doppelte Slugs im Index")
if len(indexed) != ERWARTET or not re.search(rf"Designsprachen von {ERWARTET} bekannten Marken", text):
    fails.append(f"Markenzahl im Text passt nicht zum Index ({len(indexed)})")
ohne_ansatz = [s for s, line in
               ((s, l) for s in indexed for l in text.splitlines() if l.startswith(f"- `{s}` — "))
               if "Ansatz: " not in line or "Aufbau: " not in line]
if ohne_ansatz:
    fails.append(f"Index ohne Ansatz/Aufbau: {ohne_ansatz[:5]}")

# --- references/ identisch zur Quelle ---------------------------------------
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


for slug in indexed:
    ref = skill / "references" / f"{slug}.md"
    src = repo / "design-md" / slug / "DESIGN.md"
    if ref.stat().st_size == 0 or sha(ref) != sha(src):
        fails.append(f"reference weicht von der Quelle ab: {slug}")

# --- Profile -----------------------------------------------------------------
profile = sorted(p.stem for p in (skill / "designsprache").glob("*.md"))
if profile != files:
    fails.append(f"designsprache/ unvollständig: {sorted(set(files) ^ set(profile))}")
for slug in profile:
    d = kopfdaten(skill / "designsprache" / f"{slug}.md")
    fehlt = [k for k in KOPF_PFLICHT if not d.get(k)]
    if fehlt:
        fails.append(f"{slug}: Kopfdaten fehlen: {fehlt}")
    if d.get("slug") != slug:
        fails.append(f"{slug}: slug im Kopf ist {d.get('slug')!r}")
    for k in ("ansatz", "ansatz2"):
        if d.get(k) and d[k] not in ANSAETZE:
            fails.append(f"{slug}: unbekannter {k}: {d[k]!r}")
    if d.get("modus") not in ("hell", "dunkel", "gemischt", None):
        fails.append(f"{slug}: modus {d.get('modus')!r}")

# --- Musterscreens -----------------------------------------------------------
for endung, ordner in (("png", "screens"), ("html", "screens")):
    da = sorted(p.stem for p in (skill / ordner).glob(f"*.{endung}"))
    if da != files:
        fails.append(f"{ordner}/*.{endung} unvollständig: {sorted(set(files) ^ set(da))}")
klein = sorted(p.stem for p in (skill / "screens" / "klein").glob("*.webp"))
if klein != files:
    fails.append(f"screens/klein/ unvollständig: {sorted(set(files) ^ set(klein))}")
for slug in files:
    h = (skill / "screens" / f"{slug}.html").read_text(encoding="utf-8")
    if h.count('<section class="phone') != 3:
        fails.append(f"{slug}.html: nicht genau drei Phones")
    if re.search(r'(?:src|href)\s*=\s*["\']?(?:https?:)?//', h) or "<script" in h.lower():
        fails.append(f"{slug}.html: externe Adresse oder <script>")
    if (skill / "screens" / f"{slug}.png").stat().st_size < 20_000:
        fails.append(f"{slug}.png zu klein")

# --- Animations-Katalog ---
for f in ("KATALOG.md", "animationen.html", "LIZENZEN.md"):
    if not (skill / "animationen" / f).exists():
        fails.append(f"animationen/{f} fehlt")
akat = skill / "animationen" / "KATALOG.md"
if akat.exists():
    effekte = len(re.findall(r"^### ", akat.read_text(encoding="utf-8"), re.M))
    if effekte < 40:
        fails.append(f"animationen/KATALOG.md hat nur {effekte} Effekte")
ahtml = skill / "animationen" / "animationen.html"
if ahtml.exists():
    h = ahtml.read_text(encoding="utf-8")
    if re.search(r'(?:src|href)\s*=\s*["\']?(?:https?:)?//', h):
        fails.append("animationen.html lädt etwas aus dem Netz")
    if h.count('<article class="kachel"') < 28:
        fails.append("animationen.html hat zu wenige Beispiele")
    if "prefers-reduced-motion" not in h:
        fails.append("animationen.html beachtet reduzierte Bewegung nicht")

# --- Werkzeuge, Katalog, Lizenz ---------------------------------------------
for f in TOOL_FILES:
    if not (skill / "tools" / f).exists():
        fails.append(f"tools/{f} fehlt")
if not (skill / "tools" / "screens" / "scenes").is_dir():
    fails.append("tools/screens/scenes/ fehlt")
kat = skill / "katalog.html"
if not kat.exists() or kat.stat().st_size < 50_000:
    fails.append("katalog.html fehlt oder ist zu klein")
elif f"{ERWARTET} Designs" not in kat.read_text(encoding="utf-8"):
    fails.append(f"katalog.html nennt nicht {ERWARTET} Designs")
if not (skill / "LICENSE").read_text(encoding="utf-8").startswith("MIT License"):
    fails.append("LICENSE fehlt")

# --- im SKILL.md genannte Pfade ---------------------------------------------
for pfad in sorted(set(re.findall(r"`((?:tools|animationen)/[\w./-]+)`", text))):
    if not (skill / pfad).exists():
        fails.append(f"SKILL.md nennt {pfad}, Datei fehlt")

gesamt = sum(f.stat().st_size for f in skill.rglob("*") if f.is_file())
print(f"Marken={len(indexed)} Profile={len(profile)} Musterscreens={len(klein)} "
      f"SKILL.md={len(text.encode()) // 1024} KB Ordner={gesamt / 1e6:.1f} MB")
print("FEHLER:\n  " + "\n  ".join(fails) if fails else "ALLE PRÜFUNGEN BESTANDEN")
sys.exit(1 if fails else 0)
