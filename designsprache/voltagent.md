---
slug: voltagent
marke: VoltAgent
website: https://voltagent.dev
ansatz: werkzeug
ansatz2: daten
modus: dunkel
aufbau: Dokumentations-Rhythmus: Versal-Eyebrow, ruhige 400er-Überschrift, alles in 1-px-Haarlinienrahmen
navigation: Durchgehende Leiste unten mit Haarlinie oben; aktiv = 2 px grüner Balken über dem Ziel
komponenten: Haarlinien-Karten ohne Füllung, Editor-Fenster mit Kopfzeile, Datentabelle, gestrichelte Trenner
icons: Lucide, 1.5 px Strich, eckige Enden und Gehrung, 18-20 px
bewegung: Empfehlung - knapp und technisch, 120/200 ms, cubic-bezier(.4,0,.2,1), Rahmen leuchtet statt Schatten
schrift: Inter, Display im Gewicht 400; Versal-Eyebrow 600 mit +2.52 px; Mono für alle Werte
---
# VoltAgent – Designsprache

**Kurz:** Eine einzige fast schwarze Fläche, auf der jede Einheit durch eine 1 px dünne Haarlinie begrenzt wird – keine Füllungen, keine Schatten. Ein elektrisches Grün trägt ausschließlich Hauptaktion und Live-Status. Die Seite liest sich wie gepflegte Dokumentation: Versal-Eyebrow, ruhige Überschrift im Gewicht 400, Werte in Mono.

## Wirkung
- Charakter: technisch, präzise, unaufgeregt; „technische Zeichnung“ statt Schaufenster.
- Passt zu: Entwickler-Werkzeuge, Verwaltungs- und Monitoring-Apps, Medien-Bibliotheken mit vielen Metadaten, Dokumentation.
- Passt weniger zu: emotionale Bildmarken, Kinder- und Lifestyle-Apps, alles mit weichen Schatten und Pastell.

## Aufbau und Raster
- Seitenaufbau: gleichmäßige Bahnen auf einer durchgehenden Fläche; jede Bahn beginnt mit einem Versal-Eyebrow, darunter Überschrift, darunter Haarlinien-Einheiten.
- Ausrichtung: konsequent links; Zahlen und Dauern rechtsbündig in Mono – daraus entsteht eine Tabellenoptik.
- Raster: Web-Container 1200–1400 px, Außenabstand 32 px; Feature-Karten 3-up Desktop, 2-up Tablet, 1-up Handy. App: Seitenrand 20 px.
- Dichte und Weißraum: Basiseinheit 4 px (2/4/8/12/16/20/24/32/40/48/64). Bahnen 48 px, Kartenpolster 24 px, Zeilenpolster 12/16 px. Dicht, aber nie gedrängt – die Haarlinien schaffen die Luft.
- Rhythmus: Eyebrow → Überschrift → Einheit → gestrichelter Trenner. Der gestrichelte Trenner ist die einzige Ornamentlinie.

## Navigation
- Website: schlanke Kopfleiste auf gleicher Fläche, Menüpunkte 14 px/400 in #bdbdbd, rechts eine grüne Hauptaktion; Hamburger unter 768 px.
- App: durchgehende Leiste unten (kein schwebendes Element), Fläche #101010, oben 1 px #3d3a39. Vier Ziele (Start, Bibliothek, Suche, Profil), Icon 20 px + Label 12 px. Aktiv = 2 px grüner Balken auf der Oberkante des Ziels, Icon und Label grün und 600; inaktiv #8b949e. Beim Scrollen bleibt die Leiste, der Inhalt läuft unter die Haarlinie.
- TV: linke Spalte mit Haarlinien-Zeilen, Fokus = 2 px grüner Rahmen plus grüner Balken links (`activeIndicator`).

## Startscreen
- Versal-Eyebrow, darunter Begrüßung 36 px im Gewicht 400 mit −0.9 px Laufweite.
- Direkt darunter das Signatur-Fenster: Haarlinien-Karte mit Kopfzeile (Mono-Titel + Kopier-Icon) und vier Mono-Zeilen für Fotos, Videos, Titel, Speicher; im Fuß die drei Quellen mit grünem Statuspunkt.
- Gestrichelter Trenner, dann „Rückblick“ als Haarlinien-Karte mit quadratischem Bild und grüner Hauptaktion, zuletzt ein 2-up-Raster neuer Inhalte, unten angeschnitten.

## Komponenten
- Buttons: Hauptaktion grün #00d992 mit fast schwarzem Text, 16 px/600, Polster 12×16 px, Radius 6 px; sekundär = Fläche #101010 mit 1 px #3d3a39; tertiär = Text in #2fd6a1; quadratische Icon-Knöpfe 38 px mit Haarlinie.
- Karten und Kacheln: Fläche bleibt #101010, 1 px #3d3a39, Radius 8 px, Polster 24 px. Hervorgehoben = 2 px Rahmen (grau) bzw. 2 px grün für „aktiv“. Niemals Schatten, niemals Füllung.
- Listen: als Tabelle – Kopfzeile auf #1a1a1a mit 10–11 px Versallabels, Zeilen durch 1 px #3d3a39 getrennt, links 36-px-Vorschau (Radius 4 px), rechts Mono-Werte rechtsbündig.
- Suche und Eingabefelder: Fläche #1a1a1a, 1 px #3d3a39, Radius 6 px, Höhe 40–44 px, Text 14 px, Platzhalter #8b949e; Fokus = Rahmen grün.
- Chips, Tabs, Filter: Haarlinien-Pillen (Radius 9999 px, Polster 4×12 px, 14 px). Aktiv = 1.5 px grüner Rahmen, grüner Text und grüner Punkt; inaktiv Haarlinie und #bdbdbd.
- Dialoge und Sheets: gleiche Haarlinien-Karte, Radius 8 px, zusätzlich `0 20px 60px rgba(0,0,0,.7)` und innen 1 px helle Ringlinie – der einzige Ort mit Schatten.
- Signatur-Komponenten: `code-mockup` (Fenster mit Mono-Kopfzeile und Kopier-Icon), `code-inline-chip`, Datentabelle, gestrichelter Trenner, grüner Statuspunkt.

## Icons
- Stil: Lucide-Linien, durchgehend eine Stärke; eckige Enden (`stroke-linecap: square`) und Gehrung – technisch gezeichnet, nie gefüllt, nie zweifarbig.
- Größe und Strich: 1.5 px Strich; 16 px in Tabellen und Chips, 18 px in Knöpfen, 20 px in der Navigationsleiste.
- Einsatz: funktional und sparsam – Navigation, Kopieren, Quelle, Medienart, Statuspunkt. Keine Icon-Illustrationen.
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Sharp, Gewicht 400, Fill 0; iOS SF Symbols Regular, ohne `.fill`; Web Lucide mit `stroke-width: 1.5`.

## Bildsprache
- Die Marke selbst zeigt keine Fotos – Bilder werden deshalb wie Mockups behandelt: immer **im Rahmen**, nie randlos über den Screen.
- Jedes größere Bild sitzt in einem Editor-Fenster: Haarlinien-Karte, Mono-Kopfzeile mit Dateiangabe, darunter das Bild mit 4–6 px Radius.
- Vorschauen quadratisch, 36–96 px, Radius 4 px, leicht abgesenkt (`brightness(.95)`); Raster mit 4 px Lücke, so dass die Haarlinien das Bild rastern.
- Keine Verläufe über Bildern, kein Vollbild hinter der Statusleiste.

## Typografie-Stimme
- Inter für alles, Mono (SF Mono; Ersatz JetBrains Mono / Liberation Mono) für Zahlen, Dauern, Pfade und Befehle.
- Display bewusst **leicht**: 36–60 px im Gewicht 400 mit −0.65 bis −0.9 px Laufweite; Zwischenüberschriften 24 px/700 und 20 px/600; Fließtext 16 px/400 mit Zeilenhöhe 1.6.
- Signatur: Versal-Eyebrow 14 px/600 mit **+2.52 px** Laufweite (App: 11 px mit +1.8 px) über jedem Abschnitt.
- Zahlen nie fett setzen – die Mono-Stimme trägt die Betonung.
- Freier Ersatz: Inter + JetBrains Mono.

## Form, Tiefe und Material
- Radien: 4 px Inline-Chips und Vorschauen, 6 px Buttons und Eingaben, 8 px Karten und Fenster, Pille nur für Statuspillen und Filter.
- Linien und Rahmen: 1 px #3d3a39 ist das Grundmaterial – jede Karte, jeder Knopf, jede Tabellenzeile. 2 px für Hervorhebung, 2 px grün für „aktiv“.
- Schatten und Ebenen: keine. Tiefe entsteht aus Haarlinie (Ebene 1) und einem weichen Außenschein `0 0 15px rgba(92,88,85,.2)` (Ebene 2); Schatten erst im Dialog.
- Besondere Oberflächen: #1a1a1a als einzige abgesetzte Füllung (Eingaben, Tabellenkopf, Code-Chips); 1 px gestrichelte Linie `rgba(79,93,117,.4)` zwischen Bahnen; 2 px grüner Trennbalken als einziges farbiges Ornament.

## Bewegung
- Laut Datei: keine Angaben außer Hover-Schein `0 0 15px rgba(92,88,85,.2)` auf hervorgehobenen Karten.
- Empfehlung: klein 120 ms / Screenwechsel 200 ms, Easing `cubic-bezier(.4,0,.2,1)`; Druck = Rahmen von #3d3a39 auf #5c5855 plus `scale(.99)`; Fokus = Rahmen grün ohne Versatz; Einblenden als reines Fade mit 30 ms Staffel je Haarlinien-Einheit (kein Verschieben – die Linien sollen nicht wandern); Statuspunkt pulsiert 2 s; Fortschritt wächst linear.
- Compose: `tween(120, easing = CubicBezierEasing(.4f,0f,.2f,1f))`, `Crossfade` für Screenwechsel, `animateItem()` für Tabellenzeilen, `border()` statt `shadow()` bei Fokus.

## Signatur-Elemente
1. Haarlinien-Rahmen als einziges Baumaterial – alles ist ein 1-px-Rechteck auf gleicher Fläche.
2. Editor-Fenster mit Mono-Kopfzeile und Kopier-Icon, auch um Bilder herum.
3. Versal-Eyebrow mit sehr weiter Laufweite über jedem Abschnitt.
4. Datentabelle mit Kopfzeile auf #1a1a1a und rechtsbündigen Mono-Werten.
5. Elektrisches Grün nur als Hauptaktion, Aktiv-Balken und Statuspunkt – sonst Graustufen.

## Übertragung auf eine App
- Startscreen: Eyebrow + 36-px-Begrüßung im Gewicht 400, darunter das Mono-Fenster mit Bestand und Quellen, gestrichelter Trenner, Rückblick-Karte mit grüner Aktion, 2-up-Raster neuer Inhalte.
- Liste und Übersicht: Suchfeld, Haarlinien-Pillen als Filter, dann eine echte **Tabelle** – Kopfzeile mit Versallabels, Zeilen mit 36-px-Vorschau, Titel links, Art und Umfang rechtsbündig in Mono.
- Detail: Rückweg als Mono-Brotkrume, Eyebrow + Titel 32/400, Bild im Editor-Fenster, grüne Hauptaktion plus drei quadratische Haarlinien-Knöpfe, Musikhinweis als Code-Chip, gestrichelter Trenner, Haarlinien-Pillen als Umschalter, Fotoraster 3-up mit 4 px Lücke.
- Formulare und Einstellungen: Felder #1a1a1a mit Haarlinie, Label als Versal-Eyebrow darüber, Gruppen als Haarlinien-Karten, Schalter grün gefüllt mit schwarzem Knopf.
- Leere Zustände und Laden: Haarlinien-Rahmen mit Mono-Zeile in der Mitte; Laden als Haarlinien-Gerüst ohne Füllung (Skeleton aus Linien), kein Schimmern.
- TV: Tabellen in zwei Spalten, Fokus über 2 px grünen Rahmen; Navigation links.
- Musterscreens: Start mit Mono-Statusfenster und Quellen, Bibliothek als echte Datentabelle mit Haarlinien-Filtern, Detail mit gerahmtem Bild, grüner Hauptaktion und Code-Chip für die Diashow-Musik.

## Vermeiden
- Keine Hell-Variante – die Marke kennt nur die dunkle Fläche.
- Grün nie als Textfarbe im Fließtext, nie als großflächige Füllung.
- Keine weichen Schatten unter Karten; Haarlinien sind das Tiefensystem.
- Display nicht in 700 setzen – die Ruhe im Gewicht 400 ist der Markenkern.
- Keine randlosen Bilder, keine Verläufe, keine Illustrationen.
- Versal-Eyebrows nicht in Mono setzen; sie sind Inter 600 mit weiter Laufweite.
