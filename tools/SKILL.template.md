---
name: all-top-brands-design-skill
description: All Top Brands Design Skill – wenn eine App oder Website wie eine bekannte Marke (Apple, Stripe, Spotify …) aussehen soll, Designideen, alle Designs oder eine DESIGN.md gewünscht sind oder jemand nur „design md“ sagt.
---

# All Top Brands Design Skill

74 Designsysteme bekannter Marken im DESIGN.md-Format, aus deren öffentlichen Websites herausgelesen (Quelle: VoltAgent/awesome-design-md, MIT-Lizenz). Jede Datei legt Farben, Schrift, Abstände, Radien, Schatten, Komponenten, Do's & Don'ts und Responsive-Verhalten fest.

Katalog zum Durchklicken: https://bonnibonni13-star.github.io/all-top-brands-design-skill/katalog.html (liegt der Skill lokal vor, auch als `katalog.html` in seinem Ordner).

## Ablauf

### 1. Einstieg: Was ist gewünscht?
- **Marke genannt** (z. B. `/all-top-brands-design-skill stripe`, „mach es wie Airbnb“): Slug im Index nachschlagen, weiter mit Schritt 2.
- **„Zeig mir alle Designs“** (auch „alle Designarten“, „was hast du alles“):
  1. Auf den Katalog verweisen. Er zeigt alle 74 Designs mit Farben, Schriftprobe und Button-Form; „Auswählen“ kopiert den Befehl `/all-top-brands-design-skill <slug>`. Online: Link oben. Lokal in Claude Code (macOS): `open <Ordner dieses Skills>/katalog.html`.
  2. Darunter den ganzen Index ausgeben, nach Kategorien gruppiert, je Marke eine Zeile mit Kurzbeschreibung.
  3. Fragen, welches Design es sein soll. Nach der Wahl weiter mit Schritt 2.
- **„Gib mir Designideen“** (auch „Vorschläge“, „was würde passen“): 3–5 Ideen im Ideen-Format. In einem Projekt die Suche a–d, ohne Projekt Punkt e.
- **Nur „design md“ oder der Skill-Name ohne weitere Angaben:** in einem Projekt die Suche a–d, ohne Projekt Punkt e.
- **Stil beschrieben** („dunkel und edel“, „seriös wie eine Bank“): Suche ab c, mit dem Stilwunsch statt der Projektanalyse.
- **Marke nicht im Index:** siehe „Marke fehlt“.

#### Suche
- **a.** Liegt im Projekt schon eine `DESIGN.md`, nicht neu suchen: Theme-Dateien und ein bis zwei Haupt-Screens damit abgleichen, Abweichungen auflisten (Farben, Schriften, Radien, Abstände) und die Korrektur anbieten. Neue Vorschläge nur auf Wunsch.
- **b.** Projekt gezielt ansehen: README, App-Name, Theme-Dateien (z. B. `Color.kt`, `Theme.kt`, `tailwind.config`, CSS-Variablen) und ein bis zwei Haupt-Screens. Daraus ableiten: Plattform, Zweck, Zielgruppe und bisherigen Grundton. Standardfarben aus Vorlagen (Android-Studio-Lila, Material- oder Tailwind-Standard) zählen nicht als Designentscheidung; dann nur nach Zweck und Zielgruppe wählen.
- **c.** Alle 74 Marken im Index dagegen abgleichen (Grundton, Akzent, Besonderheit; die Branche muss nicht passen) und 6–8 Kandidaten wählen. Von jedem die ersten rund 60 Zeilen der Datei lesen (Beschreibung und Farben). Fehlt `references/`, vorher die Sammlung wie in Schritt 2 holen.
- **d.** 3–5 Ideen im Ideen-Format zeigen, die sich spürbar unterscheiden, und eine davon empfehlen.
- **e.** Ohne Projekt (z. B. im Chat): 5 Ideen mit unterschiedlicher Stimmung aus verschiedenen Kategorien zeigen – dunkel und edel, hell und minimal, warm mit Creme-Tönen, bunt und verspielt, kräftig und plakativ. Vorher von jeder gewählten Marke die ersten rund 60 Zeilen lesen wie in c, damit Schrift und Formen stimmen. Dazu fragen, wofür das Design ist (Website, Android, iOS …).

#### Ideen-Format
Jede Idee bekommt einen eigenen Namen, der ihre Stimmung beschreibt, und darunter die Quelle:

> **1. <Ideen-Name>** – ein bis zwei Sätze, wie die App damit aussähe (Grundton, Akzentfarbe, Schrift, Formen).
> Inspiriert von: <Marke> · https://getdesign.md/<slug>/design-md

Höchstens eine Idee pro Auswahl darf zwei Marken mischen („Inspiriert von: Linear (Farben) + Notion (Schrift)“). Zum Schluss: eine Empfehlung mit einem Satz Begründung, der Hinweis auf den Katalog und die Frage „Welche soll es sein? Nummer oder Name genügt.“ Bei „mach einfach“ die Empfehlung nehmen. Nach der Wahl weiter mit Schritt 2.

### 2. Datei vollständig laden
- Lokal: `references/<slug>.md` im Ordner dieses Skills.
- Fehlt der Ordner `references/`: `curl -fsSL https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md/<slug>/DESIGN.md`. Ist das blockiert: `git clone --depth 1 https://github.com/VoltAgent/awesome-design-md` in einen temporären Ordner und dort `design-md/<slug>/DESIGN.md` lesen.
- Immer den ganzen Text verwenden, keine Zusammenfassung: Zusammenfassungen verlieren Hex-Werte und Maße.

### 3. Ins Projekt legen
- Die Datei als `DESIGN.md` ins Hauptverzeichnis des Projekts kopieren (`cp`, ohne `references/` per `curl -o`), nicht abtippen: Abtippen ist langsam und verfälscht Werte. Danach nur Hinweiszeile und Anpassungen per Bearbeitung ergänzen. Gibt es schon eine `DESIGN.md`, vorher fragen: ersetzen, zusammenführen oder unter anderem Namen ablegen.
- Hinweiszeile einfügen – bei YAML-Kopf direkt nach dem schließenden `---`, sonst als erste Zeile: `> Basis: <Marke>-Stil aus awesome-design-md (inoffizielle Nachbildung). Vorrang haben die „Projektspezifischen Anpassungen“ am Ende.`
- Am Ende den Abschnitt `## Projektspezifische Anpassungen` anlegen. Dort landen Schrift-Ersatz, Plattform-Übersetzung, Mischungen und Entscheidungen bei Widersprüchen. Dieser Abschnitt hat Vorrang vor dem Rest der Datei.
- Gibt es eine `CLAUDE.md`, dort eine Zeile ergänzen: `UI-Arbeit: zuerst DESIGN.md lesen und nur deren Tokens verwenden; die „Projektspezifischen Anpassungen“ am Ende haben Vorrang.` So halten sich auch künftige Sitzungen daran. Gibt es keine, das Anlegen anbieten.
- Ohne Projekt (z. B. im Chat): die angepasste DESIGN.md als Datei ausgeben.
- Danach anbieten, das Design gleich anzuwenden (Schritte 4 und 5), falls das nicht schon verlangt war.

### 4. Anwenden
Vor dem ersten UI-Code die Datei lesen. Es gibt zwei Formate:
- **Mit YAML-Kopf** (`colors`, `typography`, `rounded`, `spacing`, `components`): Die Werte im Kopf sind verbindlich. Die Abschnitte darunter (Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts, Responsive Behavior, Iteration Guide) erklären, wo und wie sie eingesetzt werden.
- **Ohne YAML-Kopf** (9 nummerierte Abschnitte): Die Werte stehen in den Abschnitten 2–6. Abschnitt 9 „Agent Prompt Guide“ enthält eine Kurzreferenz und fertige Prompts.

Dann:
1. Tokens zentral anlegen (Theme-Datei bzw. CSS-Variablen). Token-Namen übernehmen, Markennamen darin aber neutralisieren (z. B. `spotify-green` → `accent-green`).
2. Komponenten bauen, die nur diese Tokens verwenden – keine verstreuten Hex-Werte oder Maße.
3. Spannen (z. B. Gewicht 600–700): einen Wert daraus wählen. Widersprüche innerhalb der Datei: YAML-Kopf vor Fließtext, konkreter Abschnitt (Components) vor Zusammenfassung (Agent Prompt Guide). Die Entscheidung in den Anpassungen vermerken.
4. Weicht der Wunsch von der Datei ab (z. B. hell statt dunkel), gilt der Wunsch: die Variante ableiten (Flächen- und Textstufen umkehren, Akzent beibehalten, Kontrast prüfen) und in den Anpassungen festhalten. Do's and Don'ts, die dem Wunsch widersprechen, entfallen.
5. Zum Schluss die übrigen Do's and Don'ts als Prüfliste durchgehen und Verstöße beheben.

### 5. Auf die Plattform übertragen
Die Dateien beschreiben Websites. Für andere Plattformen sinngemäß übersetzen und das Ergebnis in den Anpassungen festhalten:
- **Web:** Tokens als CSS-Variablen in `:root` oder im Tailwind-Theme, Breakpoints aus „Responsive Behavior“.
- **Android / Jetpack Compose:**
  - Farben als `Color(0xFFRRGGBB)` in ein Material-3-`ColorScheme`. Alle Rollen belegen – neben primary, onPrimary, secondary, tertiary, background, surface, surfaceVariant, outline und error ausdrücklich auch surfaceContainerLowest bis surfaceContainerHighest, surfaceBright, surfaceDim und die inverse-Rollen (Karten, Navigationsleisten, Dialoge und Menüs nutzen sie) –, sonst scheinen die lila Standardfarben durch; Dynamic Color abschalten. Bietet die Marke nur hell oder nur dunkel, diesen Modus fest verwenden oder die zweite Variante wie in Schritt 4 ableiten.
  - Übrige Markenfarben, Abstände, zusätzliche Radien und Schatten in eigene Token-Klassen per `CompositionLocal`.
  - px → dp, Schriftgrößen px → sp. letter-spacing in px → sp, in em → `.em`. line-height als Faktor → Schriftgröße × Faktor. Versalschreibung (text-transform) im Composable umsetzen.
  - Radien → `Shapes`, Box-Shadows → `Modifier.shadow` bzw. Elevation (Annäherung genügt; Schattenfarben wirken erst ab Android 9). Übergänge → `tween(…, easing = CubicBezierEasing(…))`, Breakpoints → WindowSizeClass. Hover-Zustände als Pressed-Zustände umsetzen.
  - Freie Schriften per Downloadable Fonts (`androidx.compose.ui:ui-text-google-fonts`) oder als Datei in `res/font`.
- **Android TV:** Das Theme über `androidx.tv.material3.MaterialTheme` setzen, denn die TV-Komponenten lesen nur dieses (sein `ColorScheme` hat `border`/`borderVariant` statt `outline`). Dunkles Schema als Basis, helle Markenflächen sparsam. Hover-Zustände als deutliche Fokus-Zustände umsetzen (Skalierung, Rahmen oder Leuchten; fehlt eine Fokusfarbe, die Kontrastfarbe der Fläche nehmen). Text größer als auf dem Handy, Overscan-Ränder von 48 dp seitlich und 27 dp oben/unten.
- **iOS / SwiftUI, Flutter:** entsprechend über Color-Assets bzw. `ThemeData`, pt statt px.

### 6. Schriften und Marke
- Viele Dateien nennen proprietäre Schriften (z. B. SF Pro, SoDoSans, LamboType). Für eigene Produkte eine freie Schrift mit ähnlichem Charakter wählen (z. B. von Google Fonts) und die Wahl in den Anpassungen vermerken.
- Farb- und Maßwerte dürfen übernommen werden. Die markentypische Signaturfarbe (z. B. Spotify-Grün, Ferrari-Rot) für eigene Produkte leicht abwandeln, besonders in derselben Branche.
- Logos, Markennamen, Slogans, Maskottchen und Markenfotos nie übernehmen. Das Ergebnis soll vom Stil inspiriert sein, nicht wie die Marke selbst aussehen.

### 7. Mischen
Kombinationen sind erlaubt, z. B. Farben von Linear mit Typografie von Notion. Dann in den Anpassungen festhalten, was woher stammt, und Widersprüche (Radien, Schatten, Abstände) zugunsten einer Quelle auflösen.

## Marke fehlt
Die gewünschte Website abrufen (HTML und CSS) und eine eigene DESIGN.md im gleichen Aufbau schreiben: YAML-Kopf mit `colors`, `typography`, `rounded`, `spacing`, `components`, danach die Abschnitte Overview bis Responsive Behavior. Eine Datei aus dem Index als Muster lesen. Nur beobachtbare Werte übernehmen und Geschätztes als geschätzt kennzeichnen.

## Aktualisieren
Die Sammlung wächst. Auf Wunsch mit den Skripten in `tools/` (brauchen Python 3 und `pyyaml`):
1. `git clone --depth 1 https://github.com/VoltAgent/awesome-design-md /tmp/adm`
2. Für neue Marken (Ordner in `/tmp/adm/design-md/` ohne Eintrag im Index) die Datei lesen und in `tools/build_skill.py` unter `BLURB_DE` eine deutsche Kurzbeschreibung ergänzen (Grundton; Akzent; Besonderheit).
3. Im Ordner dieses Skills: `python3 tools/build_skill.py /tmp/adm tools/SKILL.template.md .` – erneuert `SKILL.md` und `references/`.
4. `python3 tools/extract_tokens.py . /tmp/profiles.json && python3 tools/build_catalog.py /tmp/profiles.json tools/katalog.template.html /tmp/katalog-online.html all-top-brands-design-skill katalog.html` – erneuert den Katalog. `/tmp/katalog-online.html` ist die Fassung für die Online-Seite.

## Hinweise
- Inoffizielle Nachbildungen aus öffentlich sichtbarem CSS, keine offiziellen Designsysteme. Marken- und Schriftrechte liegen bei den Inhabern. Lizenz der Sammlung: MIT (`LICENSE` bzw. https://github.com/VoltAgent/awesome-design-md).
- Manche Dateien verfremden den Markennamen absichtlich (z. B. „Stripi“, „Slacc“); gemeint ist die jeweilige Marke.
- Erfasst sind Marketing-Websites, keine eingeloggten App-Bereiche. Für dichte Dashboards die Werte sinngemäß übertragen.

## Index
Format: `slug` — **Marke**: Grundton; Akzent; Besonderheit.

<!-- INDEX -->
