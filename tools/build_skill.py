"""Build the design-md skill folder from a clone of VoltAgent/awesome-design-md.

Usage: python3 -I build_skill.py <repo_dir> <template> <out_dir>
"""
import pathlib
import re
import shutil
import sys

repo = pathlib.Path(sys.argv[1])
template = pathlib.Path(sys.argv[2])
out = pathlib.Path(sys.argv[3])

CAT_DE = {
    "AI & LLM Platforms": "KI & LLM-Plattformen",
    "Developer Tools & IDEs": "Entwickler-Tools & IDEs",
    "Backend, Database & DevOps": "Backend, Datenbanken & DevOps",
    "Productivity & SaaS": "Produktivität & SaaS",
    "Design & Creative Tools": "Design- & Kreativ-Tools",
    "Fintech & Crypto": "Fintech & Krypto",
    "E-commerce & Retail": "E-Commerce & Handel",
    "Media & Consumer Tech": "Medien & Consumer-Tech",
    "Automotive": "Automobil",
    "Retro Web · DESIGN.md Nostalgia": "Retro-Web (1996–2001)",
}

# In the repo folder but missing from the README list.
EXTRA = [dict(cat="Productivity & SaaS", name="Slack", slug="slack")]

# German one-liners written from each file's own description (the README blurbs are partly outdated).
# Format: Grundton; Akzent; Besonderheit.
BLURB_DE = {
    "claude": "hell, Creme-Fläche; Korallen-Buttons; Serifen-Überschriften, dunkle Produktkarten",
    "cohere": "hell, viel Weiß; dunkelgrüne Produktbänder; Mono-artige Überschriften, runde Medienkarten",
    "elevenlabs": "hell, Off-White; Pastell-Verlaufskugeln als einzige Farbe; leichte Display-Schrift, magazinartig",
    "minimax": "hell, reines Weiß; schwarze Pill-Buttons; bunte Verlaufs-Produktkarten, riesige Hero-Headline",
    "mistral.ai": "hell, Cremegelb; orange Buttons; Sonnenuntergangs-Verläufe über Bergfotos",
    "ollama": "hell, papierweiß, extrem minimal; nur Schwarz, Weiß, Grau; Pill-Buttons, wirkt wie eine README",
    "opencode.ai": "hell, warme Creme; alles in Monospace; Terminal-Look mit einer dunklen Hero-Karte",
    "replicate": "hell, Creme; heißes Orange sparsam; sehr große Display-Schrift, „Labor-Notizbuch“",
    "runwayml": "dunkel, filmisch, helle Lesebänder; Fotos und Videos als UI; eine Schrift, schwarze Pill-Buttons",
    "together.ai": "dunkle und helle Bänder im Wechsel; Orange-Magenta-Periwinkle-Verlauf; Mono-Versal-Labels",
    "voltagent": "dunkel, fast schwarz; ein elektrisches Grün; Code-Editor-Mockups, dunkle Feature-Karten",
    "x.ai": "dunkel, fast schwarz; weiße Pill-Umrisse, vereinzelt Abendrot-Verläufe; Mono-Versal-Labels",
    "cursor": "hell, warme Creme; Orange nur für Buttons; leichte Display-Schrift, Pastell-Timeline",
    "expo": "hell, Weiß mit himmelblauem Hauch; schwarze Buttons; Inter plus Mono",
    "lovable": "hell, Pergament-Creme; fast schwarze Schrift; warm, analog, wie ein Notizbuch",
    "raycast": "dunkel, fast schwarz; weiße Pill-Buttons, Haarlinien; bunte Kategorie-Akzente",
    "superhuman": "dunkler Indigo-Hero, heller Inhalt; dunkles Petrol als Abschluss; schwere, enge Display-Schrift",
    "vercel": "hell, fast weiß, Schwarz-Weiß; bunter Mesh-Verlauf im Hero; geometrische Sans plus Mono",
    "warp": "dunkel, warmes Anthrazit; Inter mit Serifen-Kursiv-Akzenten; dichte Terminal-Mockups",
    "clickhouse": "dunkel, fast schwarz; elektrisches Gelb für Buttons und Kennzahlen; Code in dunklen Karten",
    "composio": "dunkel, fast schwarz; tiefes Elektroblau mit Spotlight-Glow; Terminal-Raster als Hero",
    "hashicorp": "dunkel, schwarz; eine Akzentfarbe je Produkt; Anthrazit-Karten mit Haarlinien",
    "mongodb": "dunkle Petrol-Heros, weiße Doku-Flächen; leuchtend grüne Pill-Buttons",
    "posthog": "hell, warme Creme; gelb-orange Buttons; handgezeichnete Igel, verspielt",
    "sanity": "dunkel, fast schwarz, streng strukturiert; Korallenrot für Buttons; Neon-Grün und Blau als Akzente",
    "sentry": "dunkel, violette Mitternacht; Limetten-Akzente; verspielte Display-Schrift, Sticker-Maskottchen",
    "supabase": "hell mit Schwarz, fast monochrom; Smaragdgrün nur für Buttons; dichte Produkt-Mockups",
    "cal": "hell, Weiß; schwarze Buttons; eigene geometrische Display-Schrift, dunkelblauer Footer",
    "intercom": "hell, Creme-Weiß; Orange nur für die KI-Marke; schlicht, redaktionell, viele Screenshots",
    "linear.app": "dunkel, tiefstes Schwarz; ein Lavendelblau; dicht, technisch, Karten mit Haarlinien",
    "mintlify": "hell mit Himmelsverläufen, dunkle Bänder; Grün als Akzent; schwarze Pill-Buttons",
    "notion": "hell, dunkelblaues Hero-Band; lila Pill-Buttons; pastellige Feature-Karten, Illustrationen",
    "resend": "dunkel, fast schwarz; große Serifen-Headlines; zarte Glows, Haarlinien",
    "slack": "hell, Creme-Lavendel-Verläufe; Aubergine als Hauptfarbe; Pill-Buttons, blaue Links",
    "zapier": "hell, warme Creme; kräftiges Orange; kaffeebraune Schrift, warm statt kühl",
    "airtable": "hell, Weiß; schwarze Pill-Buttons; Farbkarten in Koralle, Dunkelgrün, Pfirsich, Navy",
    "clay": "hell, Creme; dunkelblaue Buttons; Knet-3D-Illustrationen, bunte Feature-Karten",
    "figma": "hell, Schwarz-Weiß; große Pastell-Farbblöcke; Pill-Buttons, technisch und fröhlich",
    "framer": "dunkel, schwarz; Blau nur für Links; leuchtende Verlaufs-Panels, weiße Pill-Buttons",
    "miro": "hell, Weiß; Kanariengelb; Pastell-Tönungen, schwarze Pill-Buttons",
    "webflow": "hell, Weiß mit Fast-Schwarz; fünf Akzentfarben je Produktbereich; enge Laufweite",
    "binance": "dunkel, fast schwarz (Transaktionen hell); Binance-Gelb für alle Buttons",
    "coinbase": "hell, reines Weiß; Blau sparsam; leichte Display-Schrift, ruhig und seriös",
    "kraken": "hell, Weiß; Lila als Hauptfarbe; fette Überschriften, seriös",
    "mastercard": "hell, Kitt-Creme; Signal-Orange; sehr große Radien, Pillen und Kreise",
    "revolut": "Schwarz und Weiß; Kobalt-Violett plus kräftige Produktfarben; riesige Headlines, Produkt-Mockups",
    "stripe": "hell, fast weiß, Navy-Schrift; Indigo; Verlaufs-Mesh oben, dünne Display-Schrift",
    "wise": "hell, blassgrüne Fläche; Limettengrün; extrem fette Display-Schrift",
    "airbnb": "hell, Weiß; Pink-Rot für Buttons; fotolastig, großzügig, moderate Schriftgewichte",
    "meta": "hell, Weiß; Kobaltblau für Kaufaktionen; Produktfotos, Pill-Buttons, große Kartenradien",
    "nike": "hell, Schwarz-Weiß; schwarze Pill-Buttons; riesige Versal-Headlines über Kampagnenfotos",
    "shopify": "dunkel im Marketing, Creme-Mint bei Preisen und Anmeldung; dünne, große Display-Schrift",
    "starbucks": "hell, warme Creme; vier Grüntöne; warm, wie im Laden",
    "apple": "helle und dunkle Flächen im Wechsel; ein Aktionsblau; Produktfotos, keine Deko",
    "hp": "hell, Weiß; Elektroblau für Buttons; Chevron-Deko, dunkelblaue Abschlussbänder",
    "ibm": "hell, Weiß; IBM-Blau; eckig, leichte Display-Schrift, Carbon-Stil",
    "nvidia": "Schwarz und Weiß im Wechsel; grelles Grün; kantig (2 px Radius)",
    "pinterest": "hell, warme Creme; Pinterest-Rot; Masonry-Raster, bildzentriert",
    "playstation": "Schwarz, Weiß und Blau im Kapitelwechsel; blaue Pill-Buttons; Konsolen-Renderings",
    "spacex": "dunkel, schwarz; Vollbild-Fotos; Versal-Display, Umriss-Pill-Buttons, sehr karg",
    "spotify": "dunkel, Anthrazit; Spotify-Grün; die Inhalte (Cover) liefern die Farbe",
    "theverge": "dunkel, fast schwarz; Säure-Mint und Ultraviolett; extrem fette Headlines, bunte Kacheln",
    "uber": "hell, Schwarz-Weiß; Pill-Form überall; geometrische Display-Schrift, Illustrationen",
    "vodafone": "hell mit Foto-Heros; Scharlachrot; riesige, fette Versal-Headlines",
    "wired": "hell, Weiß; schwarze Typo, schmale Display-Serif; wie ein gedrucktes Magazin",
    "bmw": "hell, Cremeweiß; BMW-Blau für Buttons; dunkelblaue Hero-Bänder, Karten-Raster",
    "bmw-m": "dunkel, fast schwarz; weiße Versal-Headlines; M-Farbstreifen sparsam",
    "bugatti": "dunkel, schwarz; kein Akzent; Versal-Display mit weiter Laufweite, nur Fotos",
    "ferrari": "dunkel, fast schwarz; Rennrot sehr sparsam; filmisch-redaktionell",
    "lamborghini": "dunkel, reines Schwarz; Gold-Akzent; eigene Neo-Grotesk",
    "renault": "hell, Schwarz-Weiß; Sonnengelb-Akzent; eckige Container, Konfigurator",
    "tesla": "hell, Weiß; ein Blau für Buttons; Vollbild-Fotos, radikal reduziert",
    "dell-1996": "Retro 1996; schwarzer Seitenrahmen; flache Farbblock-Karten, GIF-Sticker",
    "nintendo-2001": "Retro 2001; Periwinkle-Metall-Look; bernsteinfarbene Navigation, Platinen-Optik",
}

readme = (repo / "README.md").read_text(encoding="utf-8")
collection = readme.split("## Collection", 1)[1].split("## What's Inside", 1)[0]

entries, cat = [], None
for line in collection.splitlines():
    m = re.match(r"^### (.+)$", line)
    if m:
        cat = m.group(1).strip()
        continue
    m = re.match(r"^- \[\*\*(.+?)\*\*\]\(https://getdesign\.md/([^/]+)/design-md\) - (.+)$", line)
    if m:
        name, slug, _ = m.groups()
        entries.append(dict(cat=cat, name=name, slug=slug))
entries += EXTRA

folders = {p.name for p in (repo / "design-md").iterdir() if p.is_dir()}
slugs = [e["slug"] for e in entries]
problems = dict(
    missing_files=sorted(set(slugs) - folders),
    unindexed=sorted(folders - set(slugs)),
    dupes=sorted({s for s in slugs if slugs.count(s) > 1}),
    unknown_cats=sorted({e["cat"] for e in entries} - set(CAT_DE)),
    missing_blurbs=sorted(set(slugs) - set(BLURB_DE)),
    stale_blurbs=sorted(set(BLURB_DE) - set(slugs)),
)
if any(problems.values()):
    sys.exit(f"mismatch: {problems}")

# Index grouped by category in README order, brands sorted by name.
order = []
for e in entries:
    if e["cat"] not in order:
        order.append(e["cat"])
lines = []
for c in order:
    lines.append(f"### {CAT_DE[c]}")
    for e in sorted((e for e in entries if e["cat"] == c), key=lambda e: e["name"].lower()):
        lines.append(f"- `{e['slug']}` — **{e['name']}**: {BLURB_DE[e['slug']]}")
    lines.append("")
index = "\n".join(lines).rstrip() + "\n"

# Rebuild in place: only SKILL.md, LICENSE and references/ are replaced; other files (tools/, README, katalog) stay.
out.mkdir(parents=True, exist_ok=True)
if (out / "references").exists():
    shutil.rmtree(out / "references")
(out / "references").mkdir()
for e in entries:
    shutil.copyfile(repo / "design-md" / e["slug"] / "DESIGN.md", out / "references" / f"{e['slug']}.md")
shutil.copyfile(repo / "LICENSE", out / "LICENSE")

tpl = template.read_text(encoding="utf-8")
assert tpl.count("<!-- INDEX -->") == 1
(out / "SKILL.md").write_text(tpl.replace("<!-- INDEX -->", index), encoding="utf-8")

print(f"brands: {len(entries)}, categories: {len(order)}, reference files: {len(list((out / 'references').iterdir()))}")
