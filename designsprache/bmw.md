---
slug: bmw
marke: BMW
website: https://www.bmw.de
ansatz: galerie
ansatz2: daten
modus: hell
aufbau: Helle Bahnen mit 80px Rhythmus, Foto-Karten im 2er-Raster, dazwischen genau eine dunkle Navy-Bahn.
navigation: Untere Leiste, 4 Ziele, Linien-Icon + Versal-Label, aktiv mit 3px blauem Balken an der Oberkante.
komponenten: Modellkarte (Foto auf #fafafa + Titel + „DETAILS ›“), Spec-Zellen mit Haarlinien, eckige Filter-Chips
icons: Lucide-Linie, 1.5px, eckige Enden und Gehrung, 20–22px, nie gefüllt
bewegung: Sachlich, kein Überschwingen; 120ms klein, 240ms Screen, cubic-bezier(.2,0,.2,1), Druck = Farbvertiefung
schrift: Inter als Ersatz für BMW Type Next Latin; 700 Display gegen 300 Light im Fließtext, Laufweite 0
---
# BMW – Designsprache

**Kurz:** Eine korporativ-automobile Oberfläche: helle Fläche, rechteckige Kanten ohne jeden Radius, ein einziges Blau für alle Hauptaktionen. Tiefe entsteht nie durch Schatten, sondern durch Farbblöcke (helle Bahn gegen dunkle Navy-Bahn) und durch Fotografie. Die Stimme ist der Gewichtskontrast 700 gegen 300.

## Wirkung
- Charakter: gemessen, technisch, erwachsen; Präzision statt Wärme, Ordnung statt Überraschung.
- Passt zu: Produktkatalogen, Konfiguratoren, Fahrzeug- und Geräte-Apps, Bestands- und Preislisten, Mediatheken mit Sachton.
- Passt weniger zu: verspielten Communities, Kinder-Apps, Content-Feeds, die Nähe und Rundung brauchen.

## Aufbau und Raster
- Seitenaufbau: Bahnen von Rand zu Rand, die den Flächenmodus wechseln: hell → dunkel (Hero) → hell → hell (Feature) → dunkel (CTA) → hell. Zwei gleiche Modi hintereinander sind verboten.
- Ausrichtung: links; Fotos laufen randlos in ihre Bahn, Text sitzt in 24px Seitenrand.
- Raster: Web 12 Spalten, max. 1440px; Modellkarten 4- bis 5-spaltig, Tablet 2, Handy 1–2.
- Dichte und Weißraum: Bahnabstand 80px (enger als BMW M mit 96px), Kartenpolster 24px, Basiseinheit 8px (4/8/12/16/24/32/48).
- Rhythmus: Überschrift → Fließtext Light → Versal-Textlink. Jede Bahn hat genau eine Hauptaktion.

## Navigation
- Website: weiße, 64px hohe Leiste oben, Menüpunkte 14px/400 mit 0.3px Laufweite, unter 768px Hamburger als Vollbild-Sheet.
- App: untere Leiste, 4 Ziele (Start, Bibliothek, Suche, Profil), Höhe 74px, weiß, 1px Haarlinie oben, kein Radius. Icon 21px Linie + Label 9px/700 in Versalien mit 1px Laufweite. Aktiv: 3px blauer Balken an der Oberkante des Ziels, Icon und Label in `#262626`, inaktiv `#9a9a9a` – nie nur über Farbe. Leiste bleibt beim Scrollen stehen, Detailseiten behalten sie. (App-Muster abgeleitet, Empfehlung.)
- TV: horizontale Reiter oben in Versalien, Fokus als 3px blaue Unterlinie plus Aufhellung der Kachel auf `#f7f7f7`.

## Startscreen
- Kopfzeile 54px: neutrales Zeichen links, Glocke und Avatar (28px Kreis, 1px Haarlinienring) rechts, darunter Haarlinie.
- Begrüßung: Versal-Augenbraue 10px/700/1.5px in `#6b6b6b`, darunter „Guten Abend, Lena“ 28px/700, darunter die Zahlen in 13px/300.
- Darunter genau eine dunkle Bahn `#1a2129` mit randlosem Foto, Versal-Augenbraue, 24px/700-Titel, Light-Meta und einem blauen Rechteck-Knopf.
- Dann helle Bahnen: Abschnittskopf (18px/700 + „ALLE ›“) über einem 2er-Kartenraster, zuletzt die Quellen als haarlinien-getrennte Zellen mit Speicherbalken.

## Komponenten
- Buttons: primär `#1c69d4`, weiße Schrift, 14px/700/0.5px, 48px hoch, Polster 14/32, Radius 0, Druck `#0653b6`. Sekundär weiß mit 1px `#cccccc`. Auf dunkel: transparent mit 1px weißem Rand. Versalien sind den Textlinks vorbehalten, Knopflabels bleiben gemischt – das trennt BMW von BMW M.
- Karten und Kacheln: Modellkarte = Fotoplatte auf `#fafafa` (16:10, randlos, Radius 0), darunter 24px Polster mit Titel 16–18px/700, Zeile 13px/300 und Versal-Textlink. Kein Rahmen, kein Schatten.
- Listen: Zeilen durch 1px `#e6e6e6` getrennt, Wert links 700, Zusatz rechts 300 in `#6b6b6b`; Spec-Zellen nebeneinander mit senkrechten Haarlinien, Wert 20–24px/700 über Versal-Label 10px/700.
- Suche und Eingabefelder: 48px hoch, weiß, 1px `#e6e6e6`, Radius 0, Text 15px/300, Platzhalter `#9a9a9a`; Fokus verdickt den Rand auf Tinte.
- Chips, Tabs, Filter: Filter-Chip rechteckig, 1px `#cccccc`, 12px/400, Polster 8/14; aktiv Fläche `#262626` mit weißer Schrift. Kategorie-Reiter rein typografisch in Versalien 11px/700/1.5px, aktiv `#262626` plus 2px Unterlinie, inaktiv `#6b6b6b`.
- Dialoge und Sheets: weiße Fläche, Radius 0 (höchstens 12px auf Mobil), 24px Polster, Haarlinie als Kopftrenner, Aktionen rechtsbündig.
- Signatur-Komponenten: Spec-Zellen-Reihe, die dunkle Navy-Bahn, der Versal-Textlink „DETAILS ›“, runde 48px-Icon-Knöpfe als einzige runde Form.

## Icons
- Stil: geometrische Linien-Icons, nie gefüllt, eckige Enden (`stroke-linecap:square`) und Gehrung (`stroke-linejoin:miter`) – passend zum Radius 0. (Empfehlung, die Datei beschreibt keine Icon-Familie.)
- Größe und Strich: 20–22px in der Navigation, 18px inline, 16px in Zellen; Strich konstant 1.5px, keine Stärkewechsel.
- Einsatz: sparsam und funktional (Navigation, Quellenstatus, Teilen/Favorit/Mehr). Icons ersetzen nie ein Label, sie begleiten es.
- Umsetzung: Compose `Icons.Sharp` bzw. Material Symbols Sharp, Weight 300, Fill 0, Grade 0; iOS SF Symbols Regular, ungefüllt; Web Lucide mit `stroke-width:1.5`, `stroke-linecap:square`.

## Bildsprache
- Fahrzeug- bzw. Motivfotos randlos, Radius 0, 16:9 oder 21:9 im Hero, 16:10 in Karten; auf der Karte liegt das Foto auf `#fafafa`, damit das Motiv freigestellt wirkt.
- Kein Schatten, kein Rahmen, keine abgerundete Maske; Verläufe nur als dunkler Fuß über Fotos, auf denen weißer Text liegt.
- Bildraster in der Detailansicht sitzt randlos mit 2px Fuge – die Fuge ist Linie, nicht Luft.
- Keine Filter oder Tönungen; Farbigkeit bleibt dokumentarisch.

## Typografie-Stimme
- Zwei Gewichte tragen alles: 700 für Display, Titel, Knopf und Navigation, 300 (Light) für jeden Fließtext. Gewicht 500 ist im System nicht vorgesehen, 400 nur für Caption und Menüpunkt.
- Größenkontrast groß (28–32px Titel gegen 13–14px Light), Laufweite 0 – kein negatives Tracking.
- Versalien mit 1.5px Laufweite nur für Textlinks, Kategoriereiter und Mikro-Labels; Zeilenhöhe 1.05–1.25 im Display, 1.55 im Fließtext.
- Freier Ersatz: Inter 700/300 (von der Datei als Ersatz genannt), alternativ Saira Condensed für Überschriften.

## Form, Tiefe und Material
- Radien: 0px für Knöpfe, Karten, Felder, Chips, Fotos; 9999px ausschließlich für runde Icon-Knöpfe und Avatare. Dazwischen nichts – die Binarität ist Teil der Marke.
- Linien und Rahmen: 1px `#e6e6e6` als Standardtrenner, 1px `#cccccc` für betonte Umrisse, 2px `#1c69d4` für Auswahlzustände, 3px für den Navigations-Aktivbalken.
- Schatten und Ebenen: keine. Tiefe kommt aus Farbblock-Kontrast (hell gegen `#1a2129`) und aus dem Foto; verschachtelte Flächen auf Dunkel nutzen `#262e38`.
- Besondere Oberflächen: keine Verläufe, kein Glas, keine Körnung. Der M-Tricolor-Streifen gehört ausdrücklich nicht in die Konzernsprache – er bleibt BMW M vorbehalten.

## Bewegung
- Laut Datei: keine Angaben (Animation ausdrücklich außerhalb des Umfangs); dokumentiert sind nur Default und Aktiv/Druck, keine Hover-Zustände.
- Empfehlung: klein 120ms, Screenwechsel 240ms, Easing `cubic-bezier(.2,.0,.2,1)`; Druck = Farbvertiefung auf `#0653b6` plus `scale(.985)`, kein Federn, kein Überschwingen. Einblenden: 8px nach oben plus Opazität, Karten 40ms gestaffelt. Screenwechsel: horizontales Schieben ohne Skalierung. Fokus (TV): 3px blaue Linie wächst von links.
- Compose: `tween(240, easing = CubicBezierEasing(.2f,0f,.2f,1f))`, Druck über `animateFloatAsState(.985f, tween(120))`, Listen mit `animateItem()`, Screens mit `slideInHorizontally` + `fadeIn`.

## Signatur-Elemente
1. Radius 0 überall – und als einzige Ausnahme kreisrunde Icon-Knöpfe.
2. Genau eine dunkle Navy-Bahn `#1a2129` in einer sonst weißen Seite.
3. Modellkarte: Foto auf `#fafafa`, Titel darunter, Versal-Textlink „DETAILS ›“, kein Rahmen, kein Schatten.
4. Spec-Zellen-Reihe mit senkrechten Haarlinien: Wert 700 über Versal-Label.
5. Gewichtssprung 700 gegen 300 ohne jedes Zwischengewicht.

## Übertragung auf eine App
- Startscreen: Begrüßung mit Zahlenzeile, darunter eine dunkle Bahn als hervorgehobener Inhalt, danach helle Abschnitte mit 2er-Kartenraster und Quellenzellen.
- Liste und Übersicht: rechteckiges Suchfeld, Filter-Chips ohne Radius, 2-spaltiges Kartenraster mit Fotoplatte; Sortierzeile als Light-Text mit Versal-Label.
- Detail: randloses Foto über die volle Breite, runder Zurück-Knopf darauf, darunter Titel 32px/700, Spec-Zellen, blauer Hauptknopf neben runden Icon-Knöpfen, Versal-Reiter mit Unterlinie, randloses Fotoraster mit 2px Fuge.
- Formulare und Einstellungen: ein Feld je Zeile, Label 10px/700 Versalien darüber, 48px Feldhöhe, Haarlinien statt Karten, primärer Knopf unten links ausgerichtet.
- Leere Zustände und Laden: Linien-Icon 32px, Satz in 300, ein blauer Knopf. Laden als graue `#ebebeb`-Rechtecke in Karten- und Zeilenform, kein Spinner, kein Schimmern.
- TV: Bahnen bleiben, Karten wachsen auf 4er-Reihen, Fokus als blaue Unterlinie plus Aufhellung – Skalierung nur minimal (1.02).
- Musterscreens: Start mit Zahlenzeile, dunkler Rückblick-Bahn und 2er-Kartenraster; Bibliothek mit eckigem Suchfeld, Chips und sechs Karten; Detail mit randlosem Foto, Spec-Zellen, blauem Hauptknopf und fugenloser Fotomatrix.

## Vermeiden
- Keine runden Knöpfe oder Pillen – Rechteck ist die Marke; Rundung ist nur für Icon-Knöpfe erlaubt.
- Keine Schlagschatten auf Karten, keine Verläufe hinter Überschriften.
- Kein zweites Akzentblau, kein Rot, kein Grün als Aktionsfarbe – `#1c69d4` ist allein zuständig.
- Fließtext nie fett setzen: Light 300 ist die Stimme; Display nie auf 500 absenken.
- Nicht zwei Bahnen desselben Flächenmodus hintereinander stellen.
- Den M-Tricolor-Streifen nicht als Füllung, Knopf oder Dekor der Konzernsprache verwenden.
- Keine negative Laufweite im Display – das liest sich sofort nach einer anderen Marke.
