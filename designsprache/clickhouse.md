---
slug: clickhouse
marke: ClickHouse
website: https://clickhouse.com
ansatz: daten
ansatz2: werkzeug
modus: dunkel
aufbau: Fast schwarze Fläche in Bändern; Kennzahlen, Tabellen und Code-Fenster tragen den Inhalt, eine gelbe Fläche pro Screen setzt den Akzent.
navigation: Oben: 56-px-Kopfleiste plus waagerechte Kategorie-Tabs, aktiv als dunkel gefülltes Feld
komponenten: Datentabelle mit Versal-Spaltenköpfen, Code-Fenster-Karte mit Statuszeile, gelbe CTA-Karte, Kennzahl-Block, Badge-Pills
icons: Lucide, Linie 1.75 px, eckige Enden, 16–18 px, nie gefüllt
bewegung: Empfehlung – sachlich und kurz, 120/200 ms, cubic-bezier(.4,0,.2,1), kein Federn, Zahlen zählen hoch
schrift: Inter – 700 mit negativer Laufweite (−1 bis −2.5 px) für Titel und Kennzahlen, 400/500 für Text, Mono für Werte
---
# ClickHouse – Designsprache

**Kurz:** Die kontrastreichste Oberfläche im Datenbank-Umfeld: fast schwarze Fläche (`#0a0a0a`), weiße Inter-Titel mit eng gezogener Laufweite und ein einziges elektrisches Gelb (`#faff69`), das Hauptknöpfe, Kennzahlen und ganze CTA-Flächen trägt. Tiefe entsteht nicht durch Schatten, sondern durch den minimalen Helligkeitssprung von Fläche zu Karte (`#1a1a1a`) und durch Haarlinien. Inhalte werden gezeigt wie Abfrageergebnisse: Spaltenköpfe in Versalien, Werte in Mono, Statuszeile darunter.

## Wirkung
- Charakter: technisch, präzise, hochkontrastig; Leistung statt Atmosphäre, Messwert statt Stimmung.
- Passt zu: Datenbanken, Analyse, Monitoring, Entwicklerwerkzeugen, allem mit Tabellen und Kennzahlen.
- Passt weniger zu: Kinder- und Lifestyle-Apps, weichen Marken, allem, was warm oder beruhigend wirken soll.

## Aufbau und Raster
- Seitenaufbau: Bänder im 96-px-Rhythmus, nie zwei gleiche Flächenarten hintereinander – schwarz, dunkle Karte, gelbe Karte, schwarz, Code-Fenster.
- Ausrichtung: linksbündig; Hero als 7/5-Teilung (Titel links, Code-Fenster rechts), auf dem Handy gestapelt.
- Raster: Basis 4 px. Abstände 4 · 8 · 12 · 16 · 24 · 32 · 48 px, Band 96 px. Inhalt max. 1280 px.
- Dichte und Weißraum: dicht genug, um „engineering-grade“ zu wirken – Kartenpolster 32 px (Feature) bzw. 24 px (Code, Events), Tabellenzeilen 48–56 px, Spaltenabstand 12–16 px.
- Rhythmus: Titel → Kennzahlen → Beleg (Tabelle oder Code) → gelbe Aktion.

## Navigation
- Website: schwarze Kopfleiste, 64 px hoch, Wortmarke links, Menü in 14 px/500, rechts „Sign in“ als Textknopf plus gelber Hauptknopf; unter 768 px Hamburger.
- App (Empfehlung, aus `category-tab` abgeleitet): oben bleiben – 56-px-Kopfleiste (Zeichen links, runde Icon-Knöpfe rechts) und darunter eine waagerechte Tab-Reihe mit 4 Zielen. Inaktiv transparent mit `#888888`, aktiv Fläche `#1a1a1a` + Haarlinie + weiße Schrift in 600. Keine untere Leiste; der Inhalt scrollt frei unter den Tabs.
- TV: Empfehlung – linke Spalte mit Versal-Labels, Fokus als `#242424`-Fläche mit 2 px gelber Kante.

## Startscreen
- Kurzer Titel in 30–32 px/700/−1 px, keine Begrüßungsfloskel über zwei Zeilen.
- Direkt darunter der Kennzahl-Block: drei Zahlen in Gelb (34–56 px/700/−1.5 px) mit Versal-Labels (12 px/600/1.5 px), getrennt durch 1-px-Haarlinien.
- Genau eine gelbe Fläche als Aktion (Rückblick-Karte, schwarzer Knopf darin).
- Danach ein Beleg-Block: Quellen als Monitor-Tabelle mit Statuspunkten (`#22c55e`, `#f59e0b`, `#ef4444`), Mono-Werten und gelber Fortschrittszeile.

## Komponenten
- Buttons: Hauptknopf gelb `#faff69`, Schrift schwarz 14 px/600, Radius 8 px, Polster 12/20 px, Höhe 40 px; gedrückt `#e6eb52`. Zweitknopf `#1a1a1a` mit weißer Schrift, gleiche Form. Runder Icon-Knopf 36 px auf `#1a1a1a`. Textlink in Gelb mit Unterstrich.
- Karten und Kacheln: `#1a1a1a` mit 1 px `#2a2a2a`, Radius 12 px, kein Schatten; verschachtelte Karten `#242424`. Gelbe Karte `#faff69` mit schwarzem Text als einziger Farbblock.
- Listen: als **Tabelle** denken – Spaltenkopf in 11–12 px/600 Versalien mit 1.5 px Laufweite in `#888888`, Zeilen 48–56 px mit 1-px-Trenner `#2a2a2a`, Werte rechtsbündig in Mono 12–14 px, Vorschaubild 32–40 px mit Radius 4 px.
- Suche und Eingabefelder: `#1a1a1a`, Radius 8 px, Höhe 40 px, Polster 10/14 px, Text weiß, Platzhalter `#888888`; Fokus = 1 px gelber Rahmen.
- Chips, Tabs, Filter: Kategorie-Tabs mit Radius 8 px, Polster 7/11 px – inaktiv transparent/`#888888`, aktiv `#1a1a1a` + weiß + Haarlinie. Badge-Pills `#1a1a1a` (Radius 9999 px) für Metadaten, gelbe Pille nur für „Neu“.
- Dialoge und Sheets: `#1a1a1a`, Radius 12 px, 1 px Haarlinie, kein Schatten, Titel 18 px/600.
- Signatur-Komponenten: Kennzahl-Block in Gelb; Code-Fenster-Karte mit Zeilennummern, Mono-Inhalt und Statuszeile am Fuß; gelbe CTA-Karte; Ergebnis-Fußzeile unter Tabellen (Mono, 11 px, gelber Punkt).

## Icons
- Stil: Lucide, reine Linie, nie gefüllt, eckige Enden (`stroke-linecap: square; stroke-linejoin: miter`) – gezeichnet wie ein Schaltplan.
- Größe und Strich: 16 px in Zeilen und Tabs, 18 px in Knöpfen, Strichstärke 1.75 px; Icons bleiben `#888888`, außer im aktiven Tab (weiß).
- Einsatz: funktional, nie dekorativ; Status lieber als 6-px-Punkt in Semantikfarbe als als Icon.
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Outlined, Gewicht 400, Grad 0, Füllung 0; iOS SF Symbols `regular`; Web Lucide mit `stroke-width: 1.75`.

## Bildsprache
- Die Marke zeigt Code und Produkt-UI statt Fotos. Bilder deshalb wie Datenobjekte behandeln: in `#1a1a1a`-Karten mit 1 px Haarlinie, Radius 12 px, ohne Verlauf und ohne Schatten.
- Raster dicht: 3–4 Spalten, 4 px Abstand, Radius 4 px – die Fläche zählt, nicht das einzelne Bild.
- Leichte Kühlung empfohlen (`saturate(.92) contrast(1.05)`), damit Fotos neben dem Gelb nicht bunt wirken; nie Farbverlauf, nie Weichzeichner.
- Ein einziges Bild pro Screen darf groß sein (Detail-Kopf, 16:9); alles andere bleibt klein und zählbar.

## Typografie-Stimme
- Eine Familie für alles: Inter. 700 für Titel und Kennzahlen mit −1 bis −2.5 px Laufweite (ohne die negative Laufweite wirkt es zu breit), 600 für Zwischentitel und Knöpfe, 400 für Text.
- Größenkontrast ist das Hierarchiemittel: 72/56/40/32/24/18/16 – kein zweiter Schriftcharakter, keine Serife.
- Versalien nur in Mikro-Labels: 12 px/600 mit 1.5 px Laufweite. Zahlen und Werte in Mono (JetBrains Mono) 12–14 px.
- Freier Ersatz: Inter (Original), Geist oder Söhne; Mono: JetBrains Mono. Hier gerendert: Inter, Inter Display, DejaVu Sans Mono.

## Form, Tiefe und Material
- Radien: 4 px Rasterbilder und Badges · 6 px kleine Knöpfe · 8 px Knöpfe, Eingaben, Tabs · 12 px Karten und Code-Fenster · 9999 px nur für Pillen und Avatare.
- Linien und Rahmen: 1 px `#2a2a2a` für Karten und Tabellenzeilen, `#3a3a3a` für betonte Trenner. Linien ersetzen Schatten vollständig.
- Schatten und Ebenen: keine. Tiefe = Flächenstufen `#0a0a0a` → `#121212` → `#1a1a1a` → `#242424`, jeder Schritt sehr klein.
- Besondere Oberflächen: gelbe Vollfläche als eigene Ebene; Code-Fenster mit eigenem Innenchrom (Zeilennummern, Statuszeile) statt Schatten.

## Bewegung
- Laut Datei: keine Angaben – Animationszeiten sind ausdrücklich außerhalb des Umfangs („Known Gaps“).
- Empfehlung: klein 120 ms / Screenwechsel 200 ms, Easing `cubic-bezier(.4,0,.2,1)`, kein Überschwingen; Druck = Gelb auf `#e6eb52` und `scale(.99)`; Einblenden nur als Deckkraft über 120 ms; Kennzahlen zählen beim Erscheinen in 600 ms hoch; Tabellenzeilen erscheinen ohne Versatz.
- Compose: `tween(120, easing = CubicBezierEasing(.4f,0f,.2f,1f))`, Kennzahl über `animateIntAsState`, Tabs mit `Crossfade`, keine `spring`-Federung.

## Signatur-Elemente
1. Kennzahlen in Gelb, riesig und eng gesetzt, mit winzigen Versal-Labels darunter.
2. Genau eine gelbe Vollfläche pro Screen – Karte oder Knopf, nie beides groß.
3. Tabelle mit Versal-Spaltenköpfen, Mono-Werten und Ergebnis-Fußzeile.
4. Code-Fenster-Karte mit Zeilennummern und Statuszeile.
5. Oben liegende Tabs mit gefülltem Aktiv-Feld; keine untere Leiste.

## Übertragung auf eine App
- Startscreen: Kopfleiste + Tabs, kurzer Titel, Kennzahl-Block in Gelb, eine gelbe Rückblick-Karte mit schwarzem Knopf, darunter die Quellen als Monitor-Tabelle mit Statuspunkten und gelber Speicherzeile.
- Liste und Übersicht: echte Tabelle – Suchfeld, Kategorie-Tabs, Spaltenkopf, 8 Zeilen mit 32-px-Vorschau, Mono-Zahlen rechts, unten eine Ergebnis-Fußzeile mit Summen.
- Detail: Bild in einer Karte mit Haarlinie, Titel 32 px/700/−1 px, Badge-Pills, gelber Hauptknopf neben zwei dunklen Icon-Knöpfen, dichtes 3-Spalten-Raster mit 4 px Abstand, darunter die Titelliste als Code-Fenster mit Zeilennummern und Statuszeile.
- Formulare und Einstellungen: dunkle Felder mit 8 px Radius, Label 12 px/600 Versalien, ein gelber Knopf unten rechts, Hilfetext in `#888888`.
- Leere Zustände und Laden: Tabellenkopf stehen lassen und darunter eine Mono-Zeile „0 Einträge“; Ladeplatzhalter als `#1a1a1a`-Blöcke ohne Schimmer.
- TV: schwarze Fläche, große Kennzahlen, Fokus als `#242424`-Feld mit gelber Kante; Tabellen auf 4 Spalten reduzieren.
- Musterscreens: Start mit gelbem Kennzahl-Block und gelber Rückblick-Karte, Bibliothek als Tabelle mit Spaltenköpfen und Ergebnis-Fußzeile, Detail mit dichtem Raster und Titelliste im Code-Fenster.

## Unterschied zu Sentry (beides Entwickler-Infrastruktur)
ClickHouse misst, Sentry erzählt. Hier: fast schwarze Fläche, eine Schriftfamilie in 700 mit negativer Laufweite, Spaltenköpfe und Mono-Werte, dünne eckige Linien-Icons, Radien 4–12 px, Navigation oben, Gelb als Fläche. Sentry dagegen: violette Mitternacht, Schmal-Display plus geometrische UI-Schrift, Illustration und Sticker, fette gefüllte Icons, Radien 12–18 px, schwebende Leiste unten und ein harter Wechsel zu weißer Fläche für Listen. ClickHouse bleibt durchgehend dunkel und zählbar.

## Vermeiden
- Eine zweite Markenfarbe einführen – Schwarz, Weiß und Gelb reichen; Semantikfarben nur als Punkt.
- Gelb für Fließtext, große Hintergrundflächen ohne Grund oder zwei gelbe Blöcke in einem Screen.
- Gewicht 500 für Titel oder Fettungen über 700; Hierarchie kommt aus Größe.
- Pillenförmige Knöpfe – Standardradius ist 8 px, rund nur für Badges und Avatare.
- Schlagschatten, Verläufe, Glühen oder Glas.
- Zwei gleiche Flächenarten direkt hintereinander.
- Abstrakte Illustrationen statt echter Daten – der Wert selbst ist das Bild.
