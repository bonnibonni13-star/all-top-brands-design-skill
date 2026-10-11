# Am Skill arbeiten

Dieser Ordner ist zugleich das Git-Repo des Skills (`origin` zeigt auf GitHub) und der Arbeitsordner einer Claude-Code-Sitzung. `SKILL.md` ist die Anleitung für Claude; diese Datei hier ist die Anleitung für die Arbeit **am** Skill.

## Was wo liegt

| Pfad | Inhalt |
| --- | --- |
| `SKILL.md` | wird gebaut – nicht von Hand ändern, sondern `tools/SKILL.template.md` |
| `references/` | 74 DESIGN.md, unverändert aus der Quellsammlung übernommen |
| `designsprache/` | 74 Profile – hier wird von Hand geschrieben |
| `screens/` | je Marke `<slug>.html` (Quelle, von Hand) und `<slug>.png` (gerendert), dazu `klein/` für den Katalog |
| `animationen/` | Effekt-Katalog und die Seite mit den laufenden Beispielen |
| `tools/` | alle Skripte; `tools/screens/ANLEITUNG.md` beschreibt, wie Profil und Musterscreens entstehen |
| `icons/` | Lucide und Phosphor, von Git ausgenommen (siehe unten) |

## Einmal einrichten

```bash
python3 -m pip install --user playwright pillow pyyaml
python3 -m playwright install chromium
git clone --depth 1 https://github.com/lucide-icons/lucide icons/lucide
git clone --depth 1 https://github.com/phosphor-icons/core icons/phosphor
git clone --depth 1 https://github.com/VoltAgent/awesome-design-md /tmp/adm
```

`icons/` steht in `.gitignore` – die beiden Sammlungen gehören den jeweiligen Projekten (Lucide ISC, Phosphor MIT) und werden nicht mitversioniert.

## Eine Marke ändern oder ergänzen

1. `designsprache/<slug>.md` und `screens/<slug>.html` bearbeiten – der Maßstab steht in `tools/screens/ANLEITUNG.md`.
2. Rendern und ansehen:
   ```bash
   python3 -I tools/render_screens.py <slug> --src screens --profiles designsprache --out screens --icons icons --qa
   ```
   Der Renderer meldet fehlende Icons, abgeschnittene Texte und Schriftrückfälle. `--qa` legt zusätzlich ein Graustufenbild und 2x-Ausschnitte unter `screens/qa/` ab.
3. Bei einer neuen Marke zusätzlich in `tools/build_skill.py` unter `BLURB_DE` eine Kurzbeschreibung ergänzen.

## Alles neu bauen

```bash
python3 -I tools/build_skill.py /tmp/adm tools/SKILL.template.md . \
  --sprache designsprache --screens screens --tools tools --animationen animationen
python3 -I tools/extract_tokens.py . /tmp/profiles.json
python3 -I tools/build_catalog.py /tmp/profiles.json tools/katalog.template.html \
  /tmp/katalog-online.html all-top-brands-design-skill katalog.html
python3 -I tools/test_skill.py . /tmp/adm
```

Der Test muss „ALLE PRÜFUNGEN BESTANDEN“ melden. Kommt eine Marke dazu, vorher `ERWARTET` in `tools/test_skill.py` hochsetzen.

## Vorschau-Vorlage und Icon-Satz erneuern

```bash
python3 -I tools/build_vorschau.py --screens screens --icons icons --out tools/vorschau
```

Das Skript erzwingt, dass **jedes** Icon, das die Musterscreens benutzen, auch in `tools/vorschau/icons.js` steht – sonst zeigt die Vorschau rot gestrichelte Kästchen.

## Veröffentlichen

Committen wie gewohnt, dann `git push` beziehungsweise „Push origin“ in GitHub Desktop. GitHub Pages baut danach den Katalog neu:
https://bonnibonni13-star.github.io/all-top-brands-design-skill/katalog.html

Die Fassung unter `~/.claude/skills/all-top-brands-design-skill` ist ein eigener Klon und wird mit `git -C ~/.claude/skills/all-top-brands-design-skill pull` nachgezogen.
