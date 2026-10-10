# All Top Brands Design Skill

Ein Skill für Claude (Claude Code und die Claude-App), der Apps und Websites den Look bekannter Marken gibt. Er kennt die Designsysteme von 74 Marken, von Apple über Spotify bis Tesla, im DESIGN.md-Format.

**Katalog aller Designs:** https://bonnibonni13-star.github.io/all-top-brands-design-skill/katalog.html

## Was er kann

- **„design md“** oder `/all-top-brands-design-skill` in einem Projekt: Er sieht sich das Projekt an und schlägt 3–5 passende Designs vor.
- **„Gib mir Designideen“**: Ideen mit eigenem Namen, darunter jeweils „Inspiriert von: Marke“.
- **„Zeig mir alle Designs“**: der Katalog mit allen 74 Designs (Farben, Schriftprobe, Button-Form) zum Auswählen.
- **„Mach es wie Stripe“** oder `/all-top-brands-design-skill stripe`: Er legt die DESIGN.md ins Projekt und überträgt Farben, Schrift und Formen, auch auf Jetpack Compose, Android TV, iOS und Flutter.

## Installieren

**Claude Code**, mit einem Befehl:

```bash
npx skills add bonnibonni13-star/all-top-brands-design-skill -g -a claude-code
```

Oder per Git:

```bash
git clone https://github.com/bonnibonni13-star/all-top-brands-design-skill ~/.claude/skills/all-top-brands-design-skill
```

Aktualisieren: `git -C ~/.claude/skills/all-top-brands-design-skill pull`

**Claude-App:** Auf dieser Seite „Code → Download ZIP“ wählen und die Datei in Claude unter Einstellungen → Capabilities → Skills hochladen. Dafür braucht es mindestens den Pro-Plan und eingeschaltete Code-Ausführung.

## Inhalt

| Pfad | Inhalt |
| --- | --- |
| `SKILL.md` | Anleitung für Claude mit Index aller Marken |
| `references/` | 74 DESIGN.md-Dateien, eine pro Marke |
| `katalog.html` | Katalog zum Durchklicken, im Browser öffnen |
| `tools/` | Skripte zum Aktualisieren der Sammlung und des Katalogs (siehe `SKILL.md`, Abschnitt „Aktualisieren“) |

## Quelle und Lizenz

Die Designdateien stammen aus [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) (MIT-Lizenz, siehe `LICENSE`). Es sind inoffizielle Nachbildungen aus öffentlich sichtbarem CSS, keine offiziellen Designsysteme. Marken- und Schriftrechte liegen bei den jeweiligen Inhabern.
