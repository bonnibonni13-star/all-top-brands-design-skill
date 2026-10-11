---
slug: warp
marke: Warp
website: https://warp.dev
ansatz: werkzeug
ansatz2: editorial
modus: dunkel
aufbau: Warm-dunkle Bahn ohne Bruch: Terminal-Reiter oben, ruhige leichte Überschriften, vollbreite Linienzeilen und Mockup-Karten, Eingabe unten.
navigation: Terminal-Reiter oben über die volle Breite (vier Ziele, Mono, aktiv mit Füllung und 2-px-Marke); Eingabezeile unten statt Tab-Leiste.
komponenten: Mockup-Karte mit Kopfzeile, Datentabelle mit Mono-Köpfen, Linienzeilen, 3-up-Kacheln, Eingabezeile mit ❯
icons: Phosphor Light, 17–18 px, 1 px Strich, nur Elfenbein/Beige – keine Buntfarbe
bewegung: ruhig und knapp; 150/240 ms, cubic-bezier(.4,0,.2,1), kein Federn, Cursor blinkt 1 s
schrift: Inter 400 mit negativer Laufweite (−0,4 bis −1,2 px), Mono für alles Technische, Serif-Kursiv als seltener Akzent
---
# Warp – Designsprache

**Kurz:** Eine einzige warm-dunkle Bahn in Braun-Anthrazit (#2b2622), nicht Schwarz – die Wärme ist die Marke. Überschriften sind groß, aber im Gewicht 400 mit negativer Laufweite, also betont leise. Alles Technische steht in Monospace, Struktur entsteht aus 1-px-Linien und fast rechteckigen Formen (3–4 px); es gibt keine einzige Buntfarbe.

## Wirkung
- Charakter: ruhig, warm, technisch, erwachsen; „Lesemodus eines Entwicklers“ statt Marketingseite.
- Passt zu: Entwickler- und Profi-Werkzeuge, Archive, Dateiverwaltung, Terminal- und Konsolen-Apps, Lese- und Rechercheapps.
- Passt weniger zu: bunte Consumer-Apps, verspielte Marken, alles, was von gesättigten Akzentfarben lebt.

## Aufbau und Raster
- Seitenaufbau: Reiterleiste oben → Kopfblock (Mono-Zeile + leise Überschrift) → Abschnitte durch Linien getrennt → feste Eingabezeile unten.
- Ausrichtung: linksbündiger Textblock, technische Angaben rechtsbündig in Mono – jede Zeile ist zweispaltig gelesen.
- Raster: 4-px-Basis (2/4/8/10/16/24/32/48/64/96 px). Abschnittsabstand 96 px auf Web, 24–32 px in der App; Kartenpolsterung 24 px (App 14–16 px).
- Dichte und Weißraum: mittel. Zeilen 48–62 px hoch, Seitenrand 16 px, Tabellenzellen 8/10 px.
- Rhythmus: Mono-Augenbraue (11–12 px, viel Laufweite) → Inhalt → 1-px-Linie → nächster Abschnitt. Linien ersetzen Abstände.

## Navigation
- Website: schlanke Kopfleiste (10/24 px), Textlinks mit 3-px-Radius, rechts Ghost-Knopf + heller CTA; mobil Hamburger.
- App (Empfehlung, aus Terminal-Reitern und `ex-app-shell-row` abgeleitet): oben eine Reiterleiste über die volle Breite mit vier gleich breiten Zielen (start · bibliothek · suche · profil) in Mono 12,5 px, klein geschrieben. Aktiv = Fläche #383330 + 2-px-Marke in #f7f5f0 an der Oberkante + Elfenbein-Text; inaktiv = transparent, #aea69c. Darunter eine durchgehende 1-px-Linie. Unten keine Tab-Leiste, sondern die Eingabezeile: `❯` + Feld (#383330, 1 px #3f3a36, Radius 3 px) + runder Icon-Knopf – sie ist zugleich Suche und Befehlszeile und bleibt auf allen Screens stehen.
- TV: Reiter oben bleiben, Fokus = Fläche #383330 + 2-px-Marke links, Mono-Beschriftung.

## Startscreen
- Mono-Pfadzeile (`~/medien · 1.248 fotos · 96 videos · 312 titel`), darunter die Begrüßung in 34 px/400 mit −1,2 px Laufweite.
- Hervorgehobener Inhalt als **Befehl-und-Ausgabe-Karte**: Kopfzeile mit `❯ rückblick --jahr 1`, darunter Bild, Serif-Kursiv-Zeile („Vor einem Jahr“), Titel, Mono-Angaben und ein heller Knopf.
- Danach „quellen“ als drei gleich breite Kacheln mit dünnem Speicherbalken und „zuletzt hinzugefügt“ als vollbreite Linienzeilen ohne Flächen.

## Komponenten
- Buttons: primär Elfenbein #f7f5f0 auf Braun, Text #2b2622, 14/500, **Radius 3 px**, Polsterung 8/16 px, Höhe 36 px. Sekundär: Ghost, nur Text, gleicher Radius. Icon-Knöpfe als **Kreis** (28–34 px, 1 px #3f3a36) – der einzige runde Ort im System.
- Karten und Kacheln: Fläche #383330, 1 px #3f3a36, Radius 4 px (größer 6 px), Polsterung 16–24 px, keine Schatten. Mockup-Karte zusätzlich mit Kopfzeile (Mono links, Mono rechts, 1-px-Linie darunter).
- Listen: vollbreite Zeilen **ohne Füllung**, nur 1-px-Unterlinie (`press-row`/`job-row`); Titel 15–16/500 links, technische Angaben 12 px Mono rechts. Ausgewählte Zeile: Fläche #383330 + 2-px-Marke links.
- Suche und Eingabefelder: Fläche #383330, 1 px #3f3a36, Radius 3 px, 8/10 px Polsterung, Text 14 px; Fokus hellt den Rahmen auf. Eingabezeile zusätzlich mit `❯` in Elfenbein und blinkendem Block-Cursor.
- Chips, Tabs, Filter: keine Pillen – kleine Textschalter mit 3-px-Radius; aktiv = Fläche #383330 + Elfenbein + 500. Status-Pillen (`rounded.pill`) nur für Zustände wie „abgleich“.
- Dialoge und Sheets: Karte mit Radius 6 px, 24 px Polsterung, Kopfzeile in Mono, Aktionen rechts unten (primär + Ghost).
- Signatur-Komponenten: Terminal-Reiterleiste, Mockup-Karte mit Mono-Kopfzeile, Datentabelle mit Mono-Spaltenköpfen (`ex-data-table-cell`), 3-up-Kacheln, Eingabezeile mit `❯`.

## Icons
- Stil: dünne, ruhige Linien, geometrisch, ohne Fülle (Phosphor Light als Entsprechung – Empfehlung; die Datei dokumentiert kein Icon-System).
- Größe und Strich: 17–18 px in Zeilen und Knöpfen, 20 px in Kacheln, Strichstärke 1 px; nie gefüllt, nie farbig.
- Einsatz: sparsam – Rückweg, Quellenkacheln, Nebenaktionen. Statt Icons trägt meist Mono-Text die Information.
- Umsetzung: Compose `Icons.Outlined`/Material Symbols Rounded Fill 0 Gewicht 200, 20 dp; iOS SF Symbols ultraLight/thin; Web Phosphor `light` (oder Lucide mit stroke-width 1,25).

## Bildsprache
- Bilder werden in die warme Palette gezogen: `filter: sepia(.5) saturate(.62) contrast(1.03) brightness(.93)` – kein Bild bringt eine Fremdfarbe in die Seite.
- Große Bilder stehen in einer Mockup-Karte mit Mono-Kopfzeile, Seitenverhältnis ~3:2, Radius 4 px, 1 px Haarlinie.
- Kleine Bilder: Quadrate 26–40 px, Radius 3–4 px, in Tabellenzeilen vor dem Namen.
- Raster: 3 Spalten, 6 px Abstand, Radius 4 px. Keine Verläufe, keine Textauflagen, keine abgerundeten Fotokarten.

## Typografie-Stimme
- Drei Stimmen: Inter (Fließtext, Überschriften), Mono (alles Technische: Pfade, Zahlen, Dauer, Spaltenköpfe, Reiter), Serif-Kursiv (ein einziger editorialer Moment pro Screen).
- Überschriften im Gewicht **400** mit negativer Laufweite: 34 px/−1,2, 28 px/−0,8, 22 px/−0,4; Text 15–16 px/1,5; Angaben 12 px Mono; Augenbrauen 11 px Mono, 0,12 em, klein geschrieben.
- Rollentrennung im Mono: **Werte** (Pfade, Zahlen, Dauer, Reiter) klein geschrieben, **Beschriftungen** (Spaltenköpfe, Augenbrauen) in Versalien mit 0,14 em – so steht die Datei es für `ex-data-table-cell` fest.
- Freier Ersatz: Inter + DM Mono + Instrument Serif (alle Google Fonts); Ersatz hier: Inter, DejaVu Sans Mono, TeX Gyre Termes kursiv.

## Form, Tiefe und Material
- Radien: 1 px Marke, 2 px Mini-Chip, **3 px Knopf und Eingabe**, 4 px Karte und Bild, 6 px große Karte, 9999 px nur Icon-Kreise und Status-Pillen.
- Linien und Rahmen: 1 px #3f3a36 – als Kartenkante, als Zeilenunterlinie über die volle Breite und als Abschnittstrenner. Linien sind das Hauptgestaltungsmittel.
- Schatten und Ebenen: keine. Nur zwei Flächen: #2b2622 und #383330.
- Besondere Oberflächen: keine Verläufe, kein Glas. Erlaubt: feine Körnung (`--grain: .08`) und der warme Bildfilter.

## Bewegung
- Laut Datei: keine Angaben.
- Empfehlung: klein 150 ms / Screenwechsel 240 ms, Easing `cubic-bezier(.4,0,.2,1)`; Druck = Fläche #383330 + `opacity:.9`, kein Skalieren; Einblenden = nur Deckkraft (kein Verschieben), Zeilen um 30 ms gestaffelt; Reiterwechsel = Marke gleitet 180 ms; Cursor blinkt im 1-s-Takt; Fokus (TV) 150 ms.
- Compose: `tween(150, easing = CubicBezierEasing(.4f,0f,.2f,1f))`, `fadeIn()` ohne `slideIn`, `AnimatedContent` mit `SizeTransform(clip=false)`, Reitermarke über `animateDpAsState`.

## Signatur-Elemente
1. Terminal-Reiter oben über die volle Breite, klein geschriebene Mono-Beschriftung, aktiv mit 2-px-Marke.
2. Eingabezeile mit `❯` und Block-Cursor unten – Suche und Befehl in einem.
3. Mockup-Karte: Mono-Kopfzeile mit Pfad links und Angaben rechts, Inhalt darunter.
4. Vollbreite Linienzeilen und Tabellen mit Mono-Spaltenköpfen statt Karten mit Schatten.
5. Warme Braun-Fläche plus Sepia-getönte Bilder – keine einzige Buntfarbe, dazu ein Serif-Kursiv-Moment.

## Übertragung auf eine App
- Startscreen: Mono-Pfadzeile, leise Begrüßung, Befehl-und-Ausgabe-Karte als Rückblick, drei Quellenkacheln mit Speicherbalken, darunter Linienzeilen „zuletzt hinzugefügt“.
- Liste und Übersicht: Titel plus Mono-Zählzeile, Filter als eckige Textschalter, dann eine **Tabelle**: Kopfzeile mit Mono-Spaltennamen auf #383330, Zeilen mit 26-px-Bild, Name, Mono-Art und rechtsbündigen Mono-Angaben, 1-px-Linien, gewählte Zeile mit Marke links; Fußzeile in Mono.
- Detail: runder Zurück-Knopf plus Mono-Pfad, Bild in der Mockup-Karte, Titel 28 px/400 mit Serif-Kursiv-Datum, heller Knopf „Diashow starten“ und runde Icon-Knöpfe, Umschalter als Textschalter, enges 3er-Raster, dazwischen eine Befehlszeile für die Musik.
- Formulare und Einstellungen: Zeilen mit Beschriftung links, Wert rechts in Mono, 1-px-Linien, Eingaben mit 3-px-Radius; Hilfetext 12 px #aea69c.
- Leere Zustände und Laden: Mono-Zeile wie eine Ausgabe (`0 einträge`), darunter ein Satz in Inter; Laden als Linienzeilen mit pulsierender Deckkraft, kein Spinner.
- TV: gleiche warme Bahn, Tabelle auf 72-px-Zeilen, Fokus = Fläche + 2-px-Marke links, Angaben bleiben in Mono.
- Musterscreens: Start mit Befehlskarte und Quellenkacheln, Bibliothek als Mono-Tabelle mit acht Einträgen, Detail „Lissabon“ mit Mockup-Karte und Musik-Befehlszeile – alle drei mit Reiterleiste oben und Eingabezeile unten.

## Vermeiden
- Keine Buntfarbe als Akzent, kein Schwarz oder neutrales Grau statt des warmen Brauns, keine Schatten.
- Keine Pillen-Knöpfe und keine Radien über 6 px (außer Icon-Kreisen), keine schweren Überschriften (700+).
- Mono nicht für Fließtext, Serif nicht für Beschriftungen – die Rollentrennung ist Teil der Stimme.
- Bilder nicht ungefiltert und nicht randlos einsetzen; sie gehören in eine Karte mit Haarlinie.
- Nicht mit anderen dunklen Werkzeug-Marken verwechseln: Warp ist **warm-braun, Mono-getrieben, fast rechteckig (3–4 px), mit vollbreiten Linien und Tabellen**; Raycast ist reinschwarz, zeilen- und keycap-getrieben mit 6–16-px-Radien und Icon-Kacheln; Linear arbeitet mit Tab-Leiste unten und großen Titeln.
