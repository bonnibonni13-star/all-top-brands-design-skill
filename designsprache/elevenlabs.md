---
slug: elevenlabs
marke: ElevenLabs
website: https://elevenlabs.io
ansatz: minimal
ansatz2: editorial
modus: hell
aufbau: Off-White-Fläche #f5f5f5, weiße Karten mit Haarlinie; Pastell-Verlaufskugeln als einzige Farbe, sonst Tinte
navigation: App-Muster (Empfehlung): schwebende weiße Pillenleiste unten, 4 Ziele, aktives Ziel als tintenschwarze Pille mit Text
komponenten: Verlaufskugel-Karte (r 24), Wellenform-Karte, Stimmzeilen mit 32-px-Kreisplatte, Pillen-Chips, Tinten-Pille
icons: Empfehlung: Lucide-Linien 1.5 px, 20 px, runde Enden, nie gefüllt, nie farbig – Tinte oder Muted
bewegung: Empfehlung: ruhig, 180/280 ms, cubic-bezier(.22,1,.36,1); Kugeln driften langsam, Pille wächst beim Wechsel
schrift: Leichte Serife 300 mit negativer Laufweite für Displays + Inter 400/500 mit +0,16 px Laufweite
---
# ElevenLabs – Designsprache

**Kurz:** Eine ruhige Zeitschriftenfläche in Off-White, in der die einzige Farbe aus weichen Pastell-Verlaufskugeln kommt, die wie Atmosphäre hinter dem Inhalt liegen. Displays laufen in einer leichten Serife mit Gewicht 300 und enger Laufweite, alles andere in Inter mit leicht geöffneter Laufweite. Aktionen sind tintenschwarze Pillen – es gibt keine Signalfarbe.

## Wirkung
- Charakter: leise, gebildet, atmosphärisch; Produkt tritt hinter Typografie und Luft zurück. Wirkt teuer, nie laut.
- Passt zu: Audio-, Sprach-, Lese-, Medien- und Portfolio-Apps; allem, was Ruhe und Qualität ausstrahlen soll.
- Passt weniger zu: Spiel- und Kinder-Apps, dichten Dashboards, Marken mit Signalfarbe oder Dunkel-Ästhetik.
- Abgrenzung zu Claude (ebenfalls hell + Serife): hier neutral-grauweiß statt creme, Pastellkugeln statt Farbblöcken, Pillen statt 8-px-Rechtecken, runde Bildplatten statt Cremekarten, Serife 300 statt 400.

## Aufbau und Raster
- Seitenaufbau: einspaltige Bänder auf #f5f5f5; weiße Karten (#ffffff, 1 px #e7e5e4) tragen den Inhalt, dazwischen nur Luft und Haarlinien.
- Ausrichtung: Web-Hero zentriert, Produkt- und Listenflächen linksbündig; Zahlen rechts in der Zeile.
- Raster: 4-px-Basis, Abstände 4/8/12/16/20/24/32/48 px, Bandabstand 96 px (Web); max. 1200 px, 12 Spalten, Karten 3-up → 2-up → 1-up.
- Dichte und Weißraum: großzügig; Karten innen 24–32 px, in der App 16–20 px, Seitenrand 20 px, Bandabstand 28–32 px.
- Rhythmus: Fläche → Karte → Fläche; eine Verlaufskugel pro Screen als Atempause, nie zwei nebeneinander.

## Navigation
- Website: 64-px-Kopfzeile auf Canvas, Wortmarke links, Textmenü mittig (15 px/500), rechts Anmelden + Tinten-Pille; unter 768 px Hamburger.
- App (Empfehlung, aus der Pillen-Geometrie abgeleitet): schwebende Leiste 56 px über dem Rand, weiß, Radius 9999 px, 1 px Haarlinie, Schatten `0 4px 16px rgba(0,0,0,.06)`, 4 Ziele (Start, Bibliothek, Suche, Profil). Inaktiv nur Linien-Icon 20 px in #777169, aktiv eine tintenschwarze Pille mit Icon **und** Text in Weiß – Aktivität also über Form, Fläche und Beschriftung, nicht über Farbe. Beim Scrollen bleibt die Leiste stehen; auf Detailseiten entfällt sie zugunsten des Zurück-Knopfes oben links.
- TV: horizontale Textreihe oben, Fokus als Tintenpille um den Eintrag, kein Rahmen um Kacheln außer einer 2-px-Tintenlinie.

## Startscreen
- Kopfzeile nur mit neutralem Zeichen links und Avatar rechts; darunter eine Serifen-Begrüßung 34–36 px/300 und eine Zahlenzeile in Inter 15 px/#777169.
- Danach die Verlaufskugel-Karte (Radius 24 px) als einziger hervorgehobener Inhalt, mit Pillen-Label, Serifentitel, Bildplatte und Tinten-Pille.
- Darunter eine Reihe weißer Bildkarten und ein ruhiges Quellen-Band mit Haarlinie und Fortschrittsbalken.

## Komponenten
- Buttons: primär Tinten-Pille #292524, Weiß, 15 px/500, 40 px hoch, Radius 9999 px, Druck #0c0a09; sekundär transparente Pille mit 1 px #d6d3d1; tertiär reiner Textlink in Tinte. Nie eine Signalfarbe.
- Karten und Kacheln: weiß, Radius 16 px, 1 px #e7e5e4, Innenabstand 24 px (App 16–20 px), höchstens ein Schattenniveau `0 4px 16px rgba(0,0,0,.04)`; Verlaufskugel-Karte auf #fafafa mit Radius 24 px.
- Listen: Zeilen ohne Kartenrahmen, nur 1 px Haarlinie dazwischen, links eine runde 44-px-Bildplatte (Stimmen-Icon-Prinzip, `rounded.full`), rechts Angabe plus 28-px-Kreisknopf.
- Suche und Eingabefelder: weiß, Radius 8 px, 44 px hoch, 1 px #d6d3d1, Text 16 px; Fokus = 2 px Tintenrahmen, kein farbiger Ring.
- Chips, Tabs, Filter: Pillen in `caption`-Größe; aktiv gefüllt in Tinte mit weißer Schrift, inaktiv transparent mit Haarlinie – nie nur eingefärbt.
- Dialoge und Sheets: weißes Blatt, Radius 24 px oben, Haarlinie, 24 px Innenabstand, Aktion als Tinten-Pille über die volle Breite.
- Signatur-Komponenten: Verlaufskugel-Karte (Pastellbloom hinter dem Text), Wellenform-Karte (Play-Kreis + Balken-Wellenform + Angaben), Versalien-Mikrolabel 12 px/600/+0,96 px als Abschnittsmarke.

## Icons
- Stil: Empfehlung – gleichmäßige Linien-Icons ohne Füllung, runde Enden, geometrisch-ruhig (Lucide). Nie zwei Stärken mischen, nie farbig.
- Größe und Strich: 20 px in Zeilen und Navigation, 18 px in Knöpfen, 24 px in Kreisplatten; Strich 1,5 px.
- Einsatz: sparsam – Navigation, Zeilenende, Play, Quellen. Überschriften und Chips bleiben ohne Icon.
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Rounded, Gewicht 300, Füllung 0; iOS SF Symbols Light/Regular, ungefüllt; Web Lucide stroke-width 1.5 oder Phosphor Light.

## Bildsprache
- Atmosphärische, weiche Fotografie ist der Markenträger; Bilder laufen natürlich, höchstens `saturate(.96)`, kein Duplex, kein Graufilter.
- Formate: Bildplatte im Band 16 px Radius, Seitenverhältnis 16:10 oder 4:3; Listenbilder **rund** (44 px) wie die Stimmenkreise; Avatare rund.
- Kein Vollbild-Hero mit Text darauf: Das Bild sitzt als Platte in der Karte, Text steht darüber oder darunter auf der Fläche.
- Pastell-Verlaufskugeln (Mint #a7e5d3, Pfirsich #f4c5a8, Lavendel #c8b8e0, Himmel #a8c8e8, Rosé #e8b8c4) liegen als weiche Radialverläufe hinter Inhalten – nie als Flächenfarbe, Knopffüllung oder Textfarbe.

## Typografie-Stimme
- Größenkontrast groß, Gewichtskontrast klein: Display 32–48 px in Gewicht 300 mit −0,3 bis −1 px Laufweite, Fließtext 16 px/400 mit +0,16 px, Zeilenhöhe 1,5.
- Zwei Stimmen: leichte Serife nur für Titel und Zahlen-Displays, Inter für alles Funktionale; Versalien-Mikrolabel 12 px/600/+0,96 px markieren Abschnitte.
- Displays werden nie fett; Fließtext fällt nie auf 300.
- Freier Ersatz: EB Garamond 300 oder Cormorant Garamond 300 für die Serife, Inter für Text (Google Fonts).

## Form, Tiefe und Material
- Radien: 4 / 6 / 8 / 12 / 16 / 24 px, Pille 9999 px für alle Knöpfe, Chips und Badges; 0 px kommt nicht vor.
- Linien und Rahmen: 1 px #e7e5e4 als Standardtrennung, #d6d3d1 für Eingaben und Umrisspillen, #f0efed für leise Trennungen.
- Schatten und Ebenen: genau eine Stufe, `0 4px 16px rgba(0,0,0,.04)`, nur für schwebende Elemente (Navigationspille, Sheet). Tiefe entsteht sonst aus Weiß auf Off-White.
- Besondere Oberflächen: Verlaufskugeln als `radial-gradient` mit 60–70 % Transparenz, weich auslaufend; dunkle Inversion (#0c0a09) nur für einen einzelnen hervorgehobenen Block.

## Bewegung
- Laut Datei: keine Angaben (Animationszeiten ausdrücklich außerhalb des Umfangs).
- Empfehlung: klein 180 ms / Screenwechsel 280 ms, Easing `cubic-bezier(.22, 1, .36, 1)`; Druck = Pille auf 0,98 skaliert und auf #0c0a09; Einblenden = 8 px Aufwärtsbewegung mit 60 ms Versatz je Band; Screenwechsel = weiches Überblenden, keine Seitwärtsschübe; Verlaufskugeln driften 12–20 s lang um wenige Prozent; Wellenform-Balken pulsieren nur beim Abspielen; Fokus (TV) = Pille wächst von 0,96 auf 1.
- Compose: `tween(180, easing = CubicBezierEasing(.22f, 1f, .36f, 1f))`, Pillenwechsel über `animateDpAsState` der Breite, Listen mit `animateItem()`, Screenwechsel `fadeIn() + slideInVertically { it / 24 }`.

## Signatur-Elemente
1. Pastell-Verlaufskugel als weiche Atmosphäre hinter Titel oder Karte – die einzige Farbe im Bild.
2. Leichte Serife in Gewicht 300 mit enger Laufweite neben Inter – großer Größen-, kleiner Gewichtskontrast.
3. Tintenschwarze Pille als einzige Aktion, dazu Umrisspillen und Pillen-Chips.
4. Runde Bildplatten in Listen (Stimmenkreis-Prinzip) mit Haarlinien statt Kartenrahmen.
5. Wellenform-Karte mit Play-Kreis und Balkengrafik als Produktzeichen.

## Übertragung auf eine App
- Startscreen: Serifen-Begrüßung, eine Verlaufskugel-Karte als Rückblick, eine Reihe weißer Bildkarten, Quellen-Band mit Fortschrittslinie; Navigation als schwebende Pille.
- Liste und Übersicht: Suchfeld, Pillen-Filter, danach Gruppen mit Versalien-Mikrolabel und Zeilen mit runder Bildplatte, Haarlinie dazwischen; keine Kacheln, kein Raster.
- Detail: Versalien-Label, großer Serifentitel, Bildplatte mit Kugel dahinter, eine Tinten-Pille plus drei Umrisskreise, Wellenform-Karte für die Musik, Pillen-Umschalter und ein Foto-Mosaik.
- Formulare und Einstellungen: 44-px-Felder, Beschriftung in Versalien-Mikrolabel darüber, Schalter in Tinte, Abschnitte durch Haarlinien getrennt.
- Leere Zustände und Laden: Verlaufskugel plus ein Satz in Serife 300 und eine Umrisspille; Laden als ruhiges Aufblenden weißer Karten, keine Spinner-Farbe.
- TV: dieselbe Fläche in dunkler Inversion (#0c0a09), Kugeln bleiben, Fokus als Tintenpille mit weißer Beschriftung invertiert.
- Musterscreens: Start mit Kugel-Rückblick und Kartenreihe, Bibliothek als Haarlinien-Liste mit runden Bildplatten, Detail mit Serifentitel, Wellenform-Karte und Foto-Mosaik.

## Vermeiden
- Keine Signalfarbe für Aktionen; Pastelltöne nie als Knopf-, Chip- oder Textfarbe.
- Displays nie fett setzen und Fließtext nie auf 300 ziehen.
- Keine eckigen Knöpfe (0 px) und keine zweite Schattenstufe.
- Keine dunkle Entwickler-Oberfläche, kein Neon, keine Glas- oder Leuchteffekte.
- Nicht mit Karten zupflastern: Weiß auf Off-White wirkt nur mit viel Luft.
