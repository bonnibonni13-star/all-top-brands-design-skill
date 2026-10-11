# Designsprache-Profile und Musterscreens – Anleitung

Für jede Marke entstehen zwei Dateien:

1. **Profil** `work/sprache/<slug>.md`: die Designsprache der Marke über die Farben hinaus (Aufbau, Navigation, Komponenten, Icons, Bildsprache, Typografie-Stimme, Form, Bewegung) und ihre Übertragung auf eine App.
2. **Musterscreens** `work/mock/<slug>.html`: drei Handy-Screens derselben Beispiel-App in dieser Designsprache.

Der Skill nutzt beides, damit eine App beim Anwenden eines Designs wirklich anders aufgebaut wird – nicht nur umgefärbt. Maßstab: Zwei Marken mit verschiedenem Ansatz müssen schon in Graustufen unterschiedlich aussehen (andere Anordnung, Navigation, Kartenform, Icon-Stil, Dichte, Typografie). Die Screens sollen wie veröffentlichte, sorgfältig gestaltete App-Screens wirken (Mobbin-/Dribbble-Niveau), nicht wie Wireframes und nicht wie Material-Standard.

## Ablauf pro Marke

1. Die Markendatei **vollständig** lesen: `/home/claude/build/all-top-brands-design-skill/references/<slug>.md` (alle Abschnitte, besonders Layout, Components, Shapes, Elevation, Do's and Don'ts, Responsive Behavior, Iteration Guide bzw. Agent Prompt Guide). Die Kurzbeschreibung der Marke steht im Index am Ende von `/home/claude/build/all-top-brands-design-skill/SKILL.md`.
2. Profil schreiben (Vorlage unten). Werte aus der Datei übernehmen (Hex, px, Radien, Schatten, Abstände). Was die Datei nicht hergibt – oft Bewegung und Icons –, aus Charakter und Komponenten der Marke ableiten und als **Empfehlung** kennzeichnen. Nichts erfinden, was als Tatsache über die Marke ausgegeben wird.
3. Musterscreens nach dem Abschnitt „Übertragung auf eine App“ des Profils bauen (Regeln unten).
4. Rendern und ansehen:
   `cd /home/claude && python3 -I tools/render_screens.py <slug>` → `work/out/<slug>.png` mit dem Read-Werkzeug ansehen. Der Renderer meldet fehlende Icons, falsche Struktur, externe Adressen, seitlich herausragende Elemente, abgeschnittene Texte (HINWEIS-Zeilen) und welche Schriften tatsächlich gerendert wurden (fällt eine Schrift auf DejaVu/Liberation zurück, stimmt der Name nicht; „Inter SemiBold“ stammt von der Statusleiste).
   Mit `--qa` entstehen zusätzlich `work/out/qa/<slug>-grau.png` (Graustufen-Test) und je Phone eine 2x-Aufnahme `<slug>-1@2x.png` … `-3@2x.png` für Details. Keine eigenen Playwright-Skripte schreiben; Renderer, `base.css` und Motive nicht ändern.
5. Kritisch prüfen und verbessern, bis es überzeugt: Überlappungen, abgeschnittene oder zu lange Texte, falsche Abstände, zu leer oder überladen, unklare Hierarchie, Icon-Stil uneinheitlich, wirkt generisch. Frage: Erkennt man die Designsprache auch ohne Farben (Graustufenbild)? Sind mindestens drei Signatur-Elemente sichtbar? Meist reichen zwei bis drei Render-Runden; die letzte mit `--qa`.

## Qualitätsmaßstab und Referenzen

Drei fertige Beispiele zeigen das erwartete Niveau: `work/out/spotify.png`, `work/out/airbnb.png`, `work/out/linear.app.png` (Quelltexte in `work/mock/`, Profile in `work/sprache/`). Sie sind Maßstab für Sorgfalt und Detailtiefe, **keine Vorlage zum Abwandeln**: Jede Marke bekommt ihren eigenen Aufbau aus ihrer eigenen Datei. Wer eine dunkle Marke baut, kopiert nicht Spotify; wer helle Karten baut, kopiert nicht Airbnb.

## Klarstellungen

- **App-Muster:** Die Markendateien beschreiben meist Websites. Für die App-Übertragung sind gut bekannte, öffentlich sichtbare App-Muster der Marke erlaubt (Kennzeichnung: „App-Muster der Marke (nicht in der Datei)“), sonst eigene Ableitungen als „Empfehlung“. Inspiration, keine 1:1-Kopie eines Produkt-Screens.
- **Widersprüche in der Markendatei:** Tokens und Komponenten-Abschnitt vor Fließtext; die Entscheidung im Profil kurz vermerken.
- **Navigation:** Das Ziel „Profil“ darf über einen Avatar oben erreichbar sein statt in der Leiste; Detail darf eigene Leisten (Mini-Player, Aktionsleiste) oder die Navigation behalten, wenn die Marke das so macht. Eine Hauptaktion nur als Icon (z. B. runder Play-Knopf) ist erlaubt, wenn die Marke es so macht.
- **Texte:** Inhalte aus der Beispiel-App; übliche UI-Texte (Sortierung, Zustände wie „Aktuell“, Fortschritt, „Alle“, „Neu“, Begrüßung) sind erlaubt. Verboten sind Slogans, Werbetexte und Eigennamen der Marke.
- **Aktiv-Zustände** nie nur über Farbe zeigen (zusätzlich Füllung, Strich, Fläche, Unterstrich oder Gewicht).
- **Ornamente:** Kleine eigene Inline-SVG-Formen (z. B. Lorbeer, Illustrations-Icons, Wellenform) sind erlaubt, wenn sie zur Marke gehören. Keine Logos.
- **Statusleiste** ist von der Regel „ein Icon-Stil“ ausgenommen.
- **Horizontale Reihen** passen entweder ganz hinein oder sind deutlich angeschnitten (nicht wenige Pixel vor dem Rand enden).
- **CSS:** Eigene Resets nur mit `:where()` (die Basis setzt bereits Abstände von Überschriften, Absätzen, Listen und Buttons auf null), sonst überschreiben sie Komponenten-Klassen.
- **Website-Feld:** Hauptadresse der Marke; beschreibt die Datei ein Produkt (z. B. Web-Player), dessen Adresse.

## Beispiel-App (für alle Marken gleich)

Eine Medien-Bibliothek für Fotos, Videos, Musik und Alben. Sprache Deutsch. Die App hat keinen Markennamen; ein neutrales Zeichen (Kreis, Quadrat, Welle) ist erlaubt. Nutzerin: Lena (Initialen LB, Bild `.scene-person`).

Navigationsziele (Muster je nach Marke): **Start, Bibliothek, Suche, Profil**. Quellen: **Google Fotos, NAS, USB-Stick**.

| Titel | Art | Angaben | Bild |
| --- | --- | --- | --- |
| Lissabon | Album | 342 Fotos · 18 Videos · Mai 2025 | `.scene-lissabon` |
| Sommer am See | Album | 128 Fotos · Aug. 2025 | `.scene-see` |
| Herbstwald | Album | 86 Fotos · Okt. 2024 | `.scene-herbst` |
| Winter in Wien | Album | 203 Fotos · Jan. 2025 | `.scene-wien` |
| Konzert im Park | Videos | 12 Videos · 1:04 Std. | `.scene-konzert` |
| Kurzfilme 2024 | Videos | 7 Videos · 38 Min. | `.scene-film` |
| Nachtfahrt | Playlist | 24 Titel · 1 Std. 32 Min. | `.scene-nacht` |
| Studio-Sessions | Album (Musik) | 11 Titel · 48 Min. | `.scene-studio` |

Titel aus „Nachtfahrt“: Neonlichter 3:42 · Autobahn bei Nacht 4:05 · Spiegelung 3:18 · Letzte Ausfahrt 5:11 · Morgengrauen 4:27.
Zahlen: 1.248 Fotos · 96 Videos · 312 Titel · Speicher 412 GB von 600 GB (69 %). Rückblick: „Vor einem Jahr: Herbstwald“.

### Die drei Screens

1. **Start** – Einstieg der App: Begrüßung oder Titel (bei Marken, die mit der Suche beginnen, darf die Suche den Titel ersetzen), ein hervorgehobener Inhalt (z. B. Rückblick „Vor einem Jahr: Herbstwald“, „Sommer am See“ oder „Weiter ansehen: Konzert im Park“), mindestens ein, besser zwei weitere Bereiche (z. B. „Zuletzt hinzugefügt“, „Musik“, Speicher/Zahlen, Quellen) und die Navigation. Lieber weniger Bereiche, dafür in der richtigen Größe und Luft der Marke.
2. **Bibliothek** – Übersicht: Suche, Filter (Alle · Fotos · Videos · Musik · Alben, als Chips, Tabs, Segment o. Ä.), mindestens sechs Einträge als Liste, Raster, Regal oder Tabelle mit Angaben (die letzten dürfen angeschnitten sein), Navigation.
3. **Detail** – Album „Lissabon“: großes Bild, Titel mit Angaben, Hauptaktion „Diashow starten“, Nebenaktionen (Teilen, Favorit, Mehr), Umschalter (Fotos · Videos · Orte), Inhalt (Fotoraster aus Bildausschnitten, gern zusätzlich „Musik zur Diashow: Nachtfahrt“), Zurück-Navigation.

Wie diese Inhalte angeordnet und dargestellt werden, entscheidet die Designsprache: Navigation unten, oben, als schwebende Pille oder Menü; Inhalte als Regale, Karten, Raster, dichte Liste, Tabelle, Bühne mit Vollbild, Magazin-Spalte, Kennzahlen-Kacheln usw. Nicht jede Marke bekommt eine Leiste unten und Karten mit Schatten.

## Regeln für die HTML-Datei

```html
<!doctype html>
<html lang="de"><head><meta charset="utf-8"><title>Musterscreens <Marke></title>
<style>
:root { /* Tokens der Marke aus der Datei: Farben, Schriften, Radien, Abstände, Schatten, Bewegung */ }
/* eigene Regeln */
</style></head>
<body>
<main class="stage">
  <figure class="shot"><figcaption>Start</figcaption><section class="phone" id="start">…</section></figure>
  <figure class="shot"><figcaption>Bibliothek</figcaption><section class="phone" id="bibliothek">…</section></figure>
  <figure class="shot"><figcaption>Detail</figcaption><section class="phone" id="detail">…</section></figure>
</main>
</body></html>
```

- Der Renderer setzt Basis-Stile davor (`tools/screens/base.css`): Bühne, Phone 390×844 px mit runden Ecken und `overflow:hidden`, Statusleiste `.sb`, Gestenleiste `.hi`, Bilder `.scene-*`, Körnung `.grain`, Icons `.ic`, `.row-x` (horizontale Reihe, rechts angeschnitten). Eigene Regeln dürfen alles außer der Phone-Größe überschreiben. Hintergrund des Phones selbst setzen.
- Jeder Screen beginnt mit der Statusleiste (Farbe per `color`):
  `<div class="sb"><span>9:41</span><span class="sb-icons"><i data-icon="ph-fill:cell-signal-full"></i><i data-icon="ph-fill:wifi-high"></i><i data-icon="ph-fill:battery-full"></i></span></div>`
  Sie darf über einem Vollbild liegen. Unten optional die Gestenleiste `<div class="hi"></div>` (Farbe per `color`).
- Inhalt darf unten abgeschnitten sein (Scrollen andeuten). Feste Leisten (Navigation, Mini-Player, Aktionsleiste) mit `position:absolute` am Phone ausrichten.
- Nur lokale Inhalte: keine URLs, kein `<img>`, kein `<script>`, keine Webfonts. Eigene Inline-SVGs für Diagramme, Wellenformen, Fortschritt oder Formen sind erlaubt.
- Keine Markennamen, Logos, Slogans, Maskottchen oder Originaltexte der Marke. Texte nur aus der Beispiel-App.
- Saubere, lesbare CSS mit Variablen, damit die Datei als Vorlage taugt. Klassennamen sprechend (z. B. `.nav-bar`, `.shelf`, `.cover`, `.chip`).

### Schriften (nur diese sind installiert und werden gerendert)

| Charakter in der Markendatei | Verwenden |
| --- | --- |
| Neo-Grotesk, SF Pro, Helvetica, Circular, Söhne, GT America | `Inter` (Text), `Inter Display` (große Titel), `TeX Gyre Heros` (Helvetica), `Liberation Sans` (Arial) |
| Geometrisch: Futura, Avenir, Product Sans, Gilroy, Circular Display | `Poppins`, `TeX Gyre Adventor` |
| Schmal (condensed) | `TeX Gyre Heros Cn` |
| Humanistisch: Segoe, Frutiger, Calibri | `Carlito`, `DejaVu Sans` |
| Serif/Editorial: Tiempos, GT Super, Lyon, Times, Garamond | `Lora`, `TeX Gyre Pagella`, `Caladea`, `TeX Gyre Termes`, `TeX Gyre Bonum`, `TeX Gyre Schola`, `DejaVu Serif` |
| Mono: SF Mono, Berkeley Mono, JetBrains Mono, Courier | `DejaVu Sans Mono`, `Liberation Mono`, `TeX Gyre Cursor`, `FreeMono` |
| Retro-Web (90er/00er) | `Liberation Serif` (Times), `Liberation Sans` (Arial), `DejaVu Sans` (Verdana-artig) |

Nicht verfügbar: Utopia, Bitstream Charter, Courier 10 Pitch. Gewichte, Laufweite (`letter-spacing`), Versalien und Zeilenhöhe aus der Datei übernehmen – sie prägen die Stimme oft stärker als die Schriftart.

### Icons

Nur als Platzhalter `<i data-icon="SATZ:NAME"></i>` (zusätzlich `class` und `style` erlaubt; Größe per `font-size`). Der Renderer setzt das SVG ein.

- `lucide:NAME` – Linien-Icons, Strichstärke per CSS (z. B. `.ic-l{stroke-width:1.5}`), eckig per `stroke-linecap:square; stroke-linejoin:miter`. Namen: `ls /home/claude/src/icons/lucide/icons | grep -i <wort>`.
- Phosphor in sechs Stärken: `ph-thin:`, `ph-light:`, `ph-regular:`, `ph-bold:`, `ph-fill:`, `ph-duotone:` + NAME (z. B. `ph-bold:house`). Namen: `ls /home/claude/src/icons/phosphor/assets/regular | grep -i <wort>`.

Pro Marke **ein** Icon-Stil, passend zum Profil (z. B. dünne Linien, kräftig gefüllt, Duoton, eckig). Wechsel zwischen Linie (inaktiv) und gefüllt (aktiv) nur, wenn er zur Marke passt. Nützliche Namen: house, library / books, search / magnifying-glass, user, play, pause, heart, share-2 / share-network, ellipsis / dots-three, chevron-left / caret-left, arrow-left, plus, image, video / film-strip, music / music-notes, shuffle, sliders-horizontal, layout-grid / squares-four, list, clock, map-pin, hard-drive / hard-drives, usb, cloud, star, bookmark, download, settings / gear, bell, x.

### Bilder

Nur die Motive aus der Basis (Hintergrundbilder): `.scene-lissabon`, `.scene-see`, `.scene-herbst`, `.scene-wien`, `.scene-konzert`, `.scene-film`, `.scene-nacht`, `.scene-studio`, `.scene-person` – laut Tabelle den Einträgen zugeordnet. Weitere „Fotos“ (z. B. im Raster der Detailseite) als Ausschnitte desselben Motivs: die erprobten Klassen `.crop-1` … `.crop-12` (z. B. `class="photo scene-lissabon crop-4"`) oder eigene Werte für `background-size`/`background-position`. Auf wichtige Bildteile achten (Sonne, Straßenbahn nicht hinter Knöpfen verstecken). Die Bildbehandlung gehört zur Designsprache: Radius, Seitenverhältnis, Vollbild, Verlauf darüber, Duplex-, Tönungs- oder Graustufenfilter (`filter`, z. B. für Marken mit gedämpfter Palette), Maske, Rahmen, Körnung (`.grain`).

### Bewegung

Die Bewegung der Marke als CSS zeigen: Einblenden und Staffeln beim Laden, Druck-/Hover-Zustände, Fokus. Dauer und Easing als Variablen (`--dur-s`, `--dur-m`, `--ease`). Alles mit `@keyframes`/`animation` gehört in `@media (prefers-reduced-motion: no-preference) { … }`; `transition` darf überall stehen. Gerendert wird mit reduzierter Bewegung – ohne Animation muss alles im Endzustand sichtbar sein.

## Profil-Vorlage

Kopfdaten (kurz, je höchstens etwa 110 Zeichen; sie erscheinen im Index, im Katalog und dienen dem Skill als Schnellauswahl bei Mischungen):

```markdown
---
slug: <slug>
marke: <Markenname, wie im Index>
website: <Hauptadresse, z. B. https://stripe.com>
ansatz: <Schlüssel aus der Liste unten>
ansatz2: <zweiter Schlüssel oder leer>
modus: <hell | dunkel | gemischt>
aufbau: <ein Satz: Anordnung und Grundprinzip>
navigation: <App-Navigationsmuster>
komponenten: <prägende Komponenten>
icons: <Stil, Stärke, Größe>
bewegung: <Charakter, Dauer, Easing, typischer Effekt>
schrift: <Typografie-Stimme>
---
# <Marke> – Designsprache

**Kurz:** 2–3 Sätze, was diese Designsprache über die Farben hinaus ausmacht.

## Wirkung
- Charakter: …
- Passt zu: … (App-Arten)
- Passt weniger zu: …

## Aufbau und Raster
- Seitenaufbau: …
- Ausrichtung: …
- Raster: … (Werte aus der Datei)
- Dichte und Weißraum: … (Abstände in px)
- Rhythmus: …

## Navigation
- Website: …
- App: … (konkretes Muster mit Zahl der Ziele, Icon/Beschriftung, Aktiv-Zustand, Verhalten beim Scrollen)
- TV: …

## Startscreen
- …

## Komponenten
- Buttons: …
- Karten und Kacheln: …
- Listen: …
- Suche und Eingabefelder: …
- Chips, Tabs, Filter: …
- Dialoge und Sheets: …
- Signatur-Komponenten: …

## Icons
- Stil: …
- Größe und Strich: …
- Einsatz: …
- Umsetzung: Compose `Icons.Outlined|Rounded|Sharp|Filled|TwoTone` bzw. Material Symbols (Variante, Gewicht, Füllung); iOS SF Symbols (Gewicht, Füllung); Web Lucide/Phosphor (Stärke)

## Bildsprache
- …

## Typografie-Stimme
- … (Größenkontrast, Gewichte, Laufweite, Versalien, Zeilenhöhe)
- Freier Ersatz: … (Google Fonts)

## Form, Tiefe und Material
- Radien: …
- Linien und Rahmen: …
- Schatten und Ebenen: …
- Besondere Oberflächen: … (Verläufe, Glas, Körnung, Muster)

## Bewegung
- Laut Datei: … (genannte Effekte; sonst „keine Angaben“)
- Empfehlung: Dauer klein … ms / Screenwechsel … ms, Easing `cubic-bezier(…)`, Druck-Effekt …, Einblenden …, Screenwechsel …, Fokus (TV) …
- Compose: … (z. B. `tween(220, easing = CubicBezierEasing(…))`, `spring(…)`, `AnimatedVisibility`, `animateItem()`, Shared-Element-Übergänge)

## Signatur-Elemente
1. …
2. …
3. …
(3–5 Dinge, an denen man den Stil sofort erkennt)

## Übertragung auf eine App
- Startscreen: …
- Liste und Übersicht: …
- Detail: …
- Formulare und Einstellungen: …
- Leere Zustände und Laden: …
- TV: …
- Musterscreens: … (ein Satz, was die drei Screens zeigen)

## Vermeiden
- … (aus Do's and Don'ts und typische Fehler beim Übertragen)
```

Jeder Abschnitt muss für sich verständlich sein: Der Skill kombiniert einzelne Abschnitte verschiedener Marken (z. B. Navigation von A, Icons von B). Deutsch, knapp, konkret, mit Werten. Etwa 70–110 Zeilen. In den Kopfdaten sind Hex-Werte erlaubt; Kennzeichnung „Empfehlung:“ auch dort, wo nötig.

## Ansätze (Schlüssel für `ansatz` und `ansatz2`)

| Schlüssel | Name | Kennzeichen |
| --- | --- | --- |
| `buehne` | Große Bühne | vollflächige Bilder oder Produkte, wenig UI, große ruhige Überschriften |
| `regale` | Medien-Regale | Inhalte in Reihen aus Covern/Kacheln, oft dunkel, Medien im Vordergrund |
| `galerie` | Bild-Karten | Fotokarten im Raster, runde Ecken, hell und freundlich |
| `werkzeug` | Präzises Werkzeug | dichte Listen, feine Linien, Tastatur-/Befehlsdenken, kleine Schrift |
| `editorial` | Editorial | Typografie im Mittelpunkt, Lesetexte, Magazin-Rhythmus |
| `daten` | Daten und Zahlen | Kennzahlen, Diagramme, Tabellen, nüchtern und vertrauenswürdig |
| `verspielt` | Verspielt | kräftige Farben, Illustrationen, runde dicke Formen, Persönlichkeit |
| `plakativ` | Plakativ | riesige Schrift, harte Kontraste, Blöcke, Versalien |
| `minimal` | Stilles Minimal | viel Weißraum, monochrom, zurückhaltende Details |
| `leuchten` | Verlauf und Leuchten | Verläufe, Glühen, dunkle Flächen mit Lichtakzenten |
| `retro` | Retro | Web der 90er/00er: Systemschriften, Rahmen, Reliefs, Tabellenlayout |

## Abschlussbericht

Pro Marke eine Zeile: `slug` – Ansatz – App-Navigation – ein Satz zu den Musterscreens – „Render OK“ oder offene Probleme.
