---
slug: figma
marke: Figma
website: https://www.figma.com
ansatz: editorial
ansatz2: verspielt
modus: hell
aufbau: Weißes Papier als Grundfläche, unterbrochen von übergroßen Pastell-Farbblöcken (Radius 24 px) mit je einem Thema
navigation: Schwebende schwarze Pillen-Leiste unten mit 3 Zielen, aktiv = weiße Pille darin; Profil über Avatar oben rechts
komponenten: Farbblock-Sektion, Pillen-Buttons (schwarz/weiß), 40-px-Kreis-Icon-Buttons, Kachel auf #f7f7f5, Mono-Eyebrow
icons: Phosphor regular, 1 Stärke, 18–22 px, nie gefüllt – Form statt Füllung
bewegung: Ruhig und knapp; 140 ms klein / 240 ms Screen, cubic-bezier(.2,0,0,1), Druck = Mikro-Skalierung 0.97
schrift: Inter: Display 32–40 px im Gewicht 300 mit -0.02em, Fließtext 15–16 px Gewicht 400, Mono-Versalien als Rubrik
---
# Figma – Designsprache

**Kurz:** Ein schwarzweißer, redaktionell ruhiger Rahmen, der immer wieder in riesige Pastell-Farbblöcke kippt – wie große Haftnotizen auf einem aufgeräumten Tisch. Die Chrome (Navigation, Fließtext, Buttons) bleibt streng monochrom; die Farbe trägt ganze Abschnitte, nicht einzelne Details. Alle Buttons sind Pillen, alle Icon-Buttons Kreise, Schatten gibt es praktisch nicht.

## Wirkung
- Charakter: technisch und fröhlich zugleich, aufgeräumt, selbstbewusst, nie laut
- Passt zu: Kreativ- und Sammel-Apps, Medien- und Notiz-Apps, Lernen, Team-Werkzeuge, Onboarding
- Passt weniger zu: Finanz-Dashboards, Dark-Mode-Produkte, dichte Daten-Tabellen, luxuriöse/seriöse Marken
- Unterschied zu Webflow (ebenfalls helles Design-Werkzeug): hier Pillen, 24-px-Pastellblöcke als Abschnittsfläche, leichtes Display in Gewicht 300–340 und gar keine Rahmen; bei Webflow 4-px-Rechtecke, Haarlinien-Raster, Gewicht 500–600 und Farbe nur in kleinen vollgesättigten Kategorie-Kacheln. Figma ist Plakat, Webflow ist Werkbank

## Aufbau und Raster
- Seitenaufbau: Weiße Fläche → Farbblock → weiße Fläche → Farbblock. Jeder Block ist ein Thema; zwischen zwei Blöcken immer weiße Luft (Web: 96 px, App: 28–32 px)
- Ausrichtung: linksbündig, eine Spalte; Überschriften und Fließtext teilen dieselbe Kante
- Raster: Web max. 1280 px, Außenabstand 48 → 24 px; App: 20 px Seitenrand, Blockinnenraum 20–24 px (Web 48 px)
- Dichte und Weißraum: großzügig. Abstände 4 · 8 · 12 · 16 · 24 · 32 · 48 px; Abschnittsrhythmus 96 px (Web)
- Rhythmus: nie zwei Farbblöcke gleichzeitig im Blick – weiß trennt sie. Auf dem Handy darf ein Block randlos bis zur Kante laufen (Poster-Effekt)

## Navigation
- Website: weiße Sticky-Leiste 56 px, links Wortmarke, rechts das Pillen-Paar (weiß „sekundär“ + schwarz „primär“); darunter ein 36 px schmales schwarzes Laufband
- App: schwebende schwarze Pillen-Leiste unten (Radius voll, 8 px über der Kante, 12 px Innenabstand). 3 Ziele mit Icon + Beschriftung; aktiv = weiße Pille mit schwarzem Icon und Gewicht 500, inaktiv weiß auf Schwarz ohne Fläche. Das Ziel „Profil“ liegt stattdessen als 40-px-Avatarkreis oben rechts (App-Muster, Empfehlung). Beim Scrollen bleibt die Leiste stehen; sie verdeckt Inhalt absichtlich halb, so wirkt sie wie aufgelegt
- TV: horizontale Pillen-Reihe oben, aktiv = weiße Pille; Fokus als 3 px schwarzer Ring um die 8-px-Bildrahmen

## Startscreen
- Oben Begrüßung als Display-Zeile (32–40 px, Gewicht 300, -0.02em) plus Avatarkreis rechts – keine Suchleiste als Erstes
- Darunter ein Farbblock als Hauptinhalt (z. B. Rückblick) mit Mono-Eyebrow, Headline 20–22 px Gewicht 600, Bild im 8-px-Rahmen und schwarzem Pillen-Button
- Dann weiße Fläche mit einer Kachelreihe (#f7f7f5), zuletzt ein zweiter Farbblock in anderer Pastellfarbe (z. B. Quellen/Speicher)

## Komponenten
- Buttons: ausschließlich Pillen (Radius 50 px). Primär schwarz #000 auf Weiß, Text weiß, 10/20 px Innenabstand; sekundär weiß mit schwarzer Schrift, ohne Rahmen; tertiär reiner Text. Promo-Pille in Magenta #ff3d8b genau einmal pro Screen
- Karten und Kacheln: Farbblock-Sektion Radius 24 px, Innenabstand 20–24 px, keine Schatten, kein Rahmen. Inhaltskachel auf #f7f7f5, Radius 8 px, Innenabstand 16 px. Preis-/Infokarte weiß mit 1 px #e6e6e6 statt Schatten
- Listen: selten; Inhalte stehen eher als Kacheln im 2er-Raster. Listenzeilen bekommen 1 px #f1f1f1 als Trenner, nie Grau als Textfarbe
- Suche und Eingabefelder: Rechteck mit Radius 8 px, 1 px #e6e6e6, Innenabstand 12/14 px, Platzhalter schwarz in Gewicht 400 – nie Mittelgrau. Fokus über Ring, nicht über Füllung
- Chips, Tabs, Filter: Pillen. Ausgewählt = schwarze Fläche mit weißem Text (identisch zum Primärbutton), nicht ausgewählt = weiß mit 1 px Haarlinie
- Dialoge und Sheets: Blatt mit Radius 24 px oben, weiße Fläche, Scrim schwarz 60 %, Griff als schwarze 4-px-Pille
- Signatur-Komponenten: Farbblock-Sektion in Limette #dceeb1, Flieder #c5b0f4, Creme #f4ecd6, Mint #c8e6cd, Rosa #efd4d4, Koralle #f3c9b6, Navy #1f1d3d; 40-px-Kreis-Icon-Button auf #f7f7f5; leicht schräg gelegte Haftnotiz-Kachel (Radius 6 px, ±4°)

## Icons
- Stil: schlichte Linien-Icons in einer Stärke, geometrisch, mittlere Rundung; nie gefüllt, nie zweifarbig
- Größe und Strich: 18 px in Leisten, 20–22 px in Kreis-Buttons; Strich optisch ~1.8 px (Phosphor regular)
- Einsatz: sparsam – Navigation, Kreis-Buttons, Zustandszeilen. Keine Icons neben Überschriften, keine Icon-Illustrationen in Listen
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Rounded, Gewicht 400, Füllung 0; iOS SF Symbols Regular, ungefüllt; Web Phosphor `regular` oder Lucide mit `stroke-width:1.75`

## Bildsprache
- Bilder sitzen immer im 8-px-Rahmen – auch große; nur Hero-Panels gehen auf 32 px. Keine Kreise, keine randlosen Vollbilder
- Farben bleiben unverändert (keine Filter, keine Tönung); das Bild liegt häufig in einem Pastellblock und bekommt durch die Blockfarbe seinen Rahmen
- Seitenverhältnisse 4:3 und 1:1 im Raster, 16:9 für Hero; Raster mit 8 px Abstand
- Keine Avatare in Marketingflächen; in der App nur ein kleiner Kreis für die Nutzerin

## Typografie-Stimme
- Eine Familie in fein abgestuften Gewichten (320 · 330 · 340 · 480 · 540 · 700) – die Hierarchie kommt aus dem Gewicht, nicht aus Grau
- Display groß und leicht: 86/64 px im Gewicht 340 mit -1.72/-0.96 px; in der App 32–40 px bei -0.02em. Fließtext 18 px Gewicht 320, Zeilenhöhe 1.45
- Mono nur als Rubrik: Versalien, +0.5 px Laufweite, 11–12 px – markiert Abschnitte wie ein Reiter
- Kein Mittelgrau im Text; Betonung über Gewicht 480 bei gleicher Größe
- Freier Ersatz: Inter (Sans, Gewichte 300–700) und JetBrains Mono (Rubriken); Zeilenhöhen ca. 0.02 kleiner setzen

## Form, Tiefe und Material
- Radien: 2 px Deko · 6 px Haftnotiz/Chip · 8 px Felder, Bilder, Kacheln · 24 px Farbblöcke und große Karten · 32 px Hero-Panel · 50 px Pillen · voll für Kreise
- Linien und Rahmen: 1 px #e6e6e6 an Feldern und Karten, 1 px #f1f1f1 als Zeilentrenner – sonst keine Rahmen
- Schatten und Ebenen: praktisch keine. Farbwechsel ersetzt Erhebung; nur schwebende Kacheln bekommen 0 4px 16px rgba(0,0,0,.06)
- Besondere Oberflächen: #f7f7f5 als zweite weiße Stufe; Pastellflächen flach, ohne Verlauf; keine Glas- oder Glüh-Effekte

## Bewegung
- Laut Datei: keine Angaben (Laufband und Block-Einblendung ausdrücklich nicht dokumentiert); Druckzustand des Primärbuttons arbeitet mit Mikro-Skalierung statt dunklerer Füllung
- Empfehlung: Dauer klein 140 ms / Screenwechsel 240 ms, Easing `cubic-bezier(.2,0,0,1)`, Druck = `scale(.97)` in 90 ms, Einblenden = 8 px von unten + Deckkraft, Blöcke um 60 ms gestaffelt, Fokus (TV) = 3 px schwarzer Ring ohne Vergrößerung
- Compose: `tween(240, easing = CubicBezierEasing(.2f,0f,0f,1f))`, Druck über `animateFloatAsState(.97f)`, Listen mit `animateItem()`, Detailbild als Shared-Element mit 8-px-Radius-Interpolation

## Signatur-Elemente
1. Übergroßer Pastell-Farbblock mit 24 px Radius, der einen ganzen Abschnitt trägt – nie zwei gleichzeitig
2. Pillen-Geometrie überall: Buttons, Filter, Navigation; ausgewählt = schwarze Fläche, weißer Text
3. Mono-Versalien als Rubrik über jedem Abschnitt
4. 40-px-Kreis-Icon-Buttons auf #f7f7f5
5. Leichtes Display in Gewicht 300–340 mit spürbar negativer Laufweite, Fließtext tiefschwarz statt grau

## Übertragung auf eine App
- Startscreen: Begrüßung groß und leicht, darunter abwechselnd weiße Flächen und je ein Pastellblock pro Thema; Hauptaktion als schwarze Pille im Block
- Liste und Übersicht: 2er-Raster aus Kacheln auf #f7f7f5 mit 8-px-Bild, Titel in Gewicht 600 und Mono-Angabe; Filter als Pillenreihe, ausgewählt schwarz; eine Kachel darf eine schräge Haftnotiz tragen
- Detail: Bild in einem Pastellblock (Bild selbst 8 px), Titel groß und leicht, Mono-Rubrik darüber, schwarze Pille als Hauptaktion plus drei Kreis-Icon-Buttons, Umschalter als Pillen, Fotoraster mit 8 px Abstand
- Formulare und Einstellungen: Felder 8 px mit Haarlinie, Beschriftung schwarz in Gewicht 480, Schalter als Pille; Abschnitte durch Farbblöcke statt Überschriften getrennt
- Leere Zustände und Laden: Pastellblock mit einer Zeile Text und einer Pille; Platzhalter als graue 8-px-Rechtecke auf #f7f7f5, kein Schimmer-Effekt
- TV: Pillen-Reihe oben, Inhalt in 8-px-Rahmen, Farbblock als Kulisse hinter der Reihe
- Musterscreens: Start mit Flieder-Rückblick und Limetten-Quellenblock, Bibliothek als Kachelraster mit Pillenfiltern und Haftnotiz, Detail mit Creme-Bildblock, schwarzer Pille und Flieder-Banner mit Magenta-Pille

## Vermeiden
- Kein Mittelgrau für Text – Hierarchie kommt aus dem Gewicht
- Keine Schatten auf Farbblöcken; Farbe ist das Tiefenmittel
- Keine eckigen Buttons und keine Pillen-Karten; Pille = Aktion, 24 px = Fläche
- Nicht zwei Farbblöcke im selben Blick; keine Farbe außerhalb der Blockpalette plus Magenta
- Mono nie als Fließtext, Schwarz nie als Dekofarbe (nur echte Primäraktion und ausgewählter Zustand)
- Nicht jede Kachel einfärben – die Wirkung entsteht aus dem monochromen Rahmen um die Farbe
