# All Top Brands Design Skill

Ein Skill für Claude (Claude Code und die Claude-App), der Apps und Websites die **ganze Designsprache** bekannter Marken gibt – Aufbau, Navigation, Komponenten, Icons, Bildsprache, Typografie, Abstände und Animation, nicht nur die Farben. Er kennt 74 Marken, von Apple über Spotify bis Tesla.

**Katalog mit Musterscreens aller 74 Designs:** https://bonnibonni13-star.github.io/all-top-brands-design-skill/katalog.html

## Was er kann

- **„design md“** oder `/all-top-brands-design-skill` in einem Projekt: Er fragt, wie viele Designvorschläge du sehen willst, sieht sich dein Projekt an und baut eine **Vorschau-Seite mit deinem eigenen Hauptscreen** in mehreren Designsprachen – jeweils mit drei umschaltbaren Farbvarianten.
- **Auswahl im Gespräch:** Du wählst ein Design und eine Farbvariante, oder lässt dir eine neue Runde zeigen (andere Marken, Abwandlungen, Mischungen oder nach deiner Beschreibung).
- **Erst der Hauptscreen,** damit du die Richtung im echten Projekt siehst, bevor viel Arbeit hineinfließt.
- **Danach Bereich für Bereich:** Farben, Schrift, Icons, Navigationsleiste, Karten und Listen, Animationen, Abstände, Bildsprache – jeweils mit drei konkreten Vorschlägen aus anderen Marken und einer Vorschau nebeneinander.
- **Animations-Katalog:** 60 benannte Effekte mit Werten und Umsetzung für Web, React (Magic UI) und Jetpack Compose; 40 davon laufen live in `animationen/animationen.html`.
- **„Zeig mir alle Designs“:** der Katalog mit Musterscreens, Filter nach Ansatz (Große Bühne, Medien-Regale, Bild-Karten, Präzises Werkzeug, Editorial, Daten und Zahlen, Verspielt, Plakativ, Stilles Minimal, Verlauf und Leuchten, Retro).
- **„Mach es wie Stripe“** oder `/all-top-brands-design-skill stripe`: Er legt `DESIGN.md` und `DESIGNSPRACHE.md` ins Projekt und überträgt die Designsprache – auch auf Jetpack Compose, Android TV, iOS und Flutter.

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
| `SKILL.md` | Anleitung für Claude mit Index aller Marken (Ansatz und Aufbau je Marke) |
| `references/` | 74 DESIGN.md-Dateien: Farben, Schrift, Abstände, Radien, Schatten, Komponenten |
| `designsprache/` | 74 Profile: Aufbau, Navigation, Komponenten, Icons, Bildsprache, Bewegung, Signatur-Elemente, Übertragung auf eine App |
| `screens/` | 74 Musterscreens: dieselbe Beispiel-App in jeder Designsprache, als Bild und als HTML mit Animationen |
| `animationen/` | Animations-Katalog: 60 Effekte mit Werten, dazu eine Seite mit 40 laufenden Beispielen |
| `katalog.html` | Katalog zum Durchklicken, im Browser öffnen |
| `tools/` | Skripte für Vorschau-Seite, echte Website-Screens, Musterscreens, Katalog und Aktualisierung (siehe `SKILL.md`, Abschnitt „Aktualisieren“) |

## Quelle und Lizenz

Die DESIGN.md-Dateien stammen aus [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) (MIT-Lizenz, siehe `LICENSE`). Es sind inoffizielle Nachbildungen aus öffentlich sichtbarem CSS, keine offiziellen Designsysteme. Marken- und Schriftrechte liegen bei den jeweiligen Inhabern.

Die Profile in `designsprache/` und die Musterscreens in `screens/` sind eigene Arbeiten mit erfundenen Beispielinhalten – **keine Originalscreens der Marken**. Die darin verwendeten Icons stammen aus [Lucide](https://lucide.dev) (ISC) und [Phosphor](https://phosphoricons.com) (MIT).

Der Animations-Katalog verweist für React-Projekte auf [Magic UI](https://github.com/magicuidesign/magicui) (MIT); die Umsetzungen und Compose-Hinweise darin sind eigene Arbeit, es wird kein Magic-UI-Quelltext mitgeliefert (siehe `animationen/LIZENZEN.md`).
