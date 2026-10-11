---
slug: clay
marke: Clay
website: https://www.clay.com
ansatz: verspielt
ansatz2: editorial
modus: hell
aufbau: Cremeboden #fffaf0 durchgehend; darauf satte einfarbige 24-px-Blöcke, die reihum die Farbe wechseln
navigation: Untere Leiste auf Creme mit 4 Zielen; aktiv = gefüllte 14-px-Farbkachel hinter dem Icon, Label 600
komponenten: Farbkarte 24 px mit weißer 16-px-Innenkachel, Knetberg-SVG, Near-Black-Knopf 12 px, Pillen-Chips
icons: Phosphor Fill, 20–22 px, massiv und rund – passend zur Knetform; nie Linien
bewegung: Weich und leicht federnd; Empfehlung 180 ms klein / 300 ms Screen, cubic-bezier(.22,1,.36,1), Druck 0.97
schrift: Gerundete Display-Grotesk, Gewicht 500, −0,05 em (Plain Black → Inter Display); Text Inter 400/600
---
# Clay – Designsprache

**Kurz:** Eine warme Cremefläche, auf der satte einfarbige Blöcke mit sehr großen Radien die Seite takten – jeder Block trägt im Inneren eine kleine weiße Kachel mit echtem Produktinhalt. Die Überschriften sind groß, gerundet und nur Gewicht 500, nie fett. Tiefe entsteht ausschließlich durch Farbkontrast, nie durch Schatten.

## Wirkung
- Charakter: handgemacht-freundlich, bunt aber nicht laut, erwachsen durch den fast schwarzen Knopf
- Passt zu: Medien- und Sammlungs-Apps, Lern- und Community-Apps, B2B-Werkzeugen mit Persönlichkeit
- Passt weniger zu: Finanz- und Sicherheits-Apps, Dashboards mit vielen Zahlenreihen, dunklen Kino-Oberflächen

## Aufbau und Raster
- Seitenaufbau: durchgehende Creme-Bahn; Inhalte sind Blöcke, keine Spalten. Farbfolge Pink → Teal → Lavendel → Pfirsich → Ocker → Creme, nie zweimal dieselbe Farbe hintereinander
- Ausrichtung: linksbündig, Überschrift und Blockkante teilen sich dieselbe Flucht
- Raster: 4-px-Basis; Abstände 4 / 8 / 12 / 16 / 24 / 32 / 48 px, Bandrhythmus 96 px (App: 28–32 px)
- Dichte und Weißraum: Karteninnenpolster 32 px (App 16–20 px), Seitenrand 20 px, Blockabstand 12 px
- Rhythmus: ein großer Farbblock, danach zwei kleine – die Größe wechselt, der Radius bleibt

## Navigation
- Website: 64-px-Cremeleiste, Menü mittig in 14 px/500, rechts Textlink plus Near-Black-Knopf
- App: untere Leiste auf Creme mit 1-px-Haarlinie oben, 4 Ziele (Start, Bibliothek, Suche, Profil) mit Icon und 11-px-Label. Aktiv = gefüllte Farbkachel (14 px Radius, Markenfarbe) hinter dem weißen Icon plus Label in 600; inaktiv Icon in #9a9a9a. Leiste bleibt beim Scrollen stehen, Inhalt läuft darunter aus
- TV: Zeilen aus Farbblöcken, Fokus = Block wächst auf 1,04 und bekommt einen 3-px-Creme-Ring

## Startscreen
- Begrüßung als Display-Zeile (32–36 px, Gewicht 500, −1,2 px), rechts daneben der runde Avatar
- Darunter der große Farbblock mit dem Rückblick: Versal-Eyebrow, Titel, weiße Innenkachel mit Bild und Angaben, heller Knopf auf Farbe
- Dann zwei kleine Blöcke nebeneinander (Speicher mit Knetbergen, Quellen) und ein angeschnittenes Regal „Zuletzt hinzugefügt“ aus Farbkarten

## Komponenten
- Buttons: Primär #0a0a0a, weiße Schrift, 14 px/600, 12 px Radius, Höhe 44 px, Polster 12×20 px. Sekundär cremefarben mit 1-px-Haarlinie #e5e5e5. Auf Farbe: weiße Fläche mit Ink-Schrift (`button-on-color`)
- Karten und Kacheln: Farbkarte 24 px Radius ohne Schatten; Inhaltskarte 16 px; in jeder Farbkarte sitzt eine weiße 16-px-Kachel als „Produktausschnitt“
- Listen: keine Trennlinien – jede Zeile ist eine eigene kleine Karte mit 16 px Radius auf Creme
- Suche und Eingabefelder: Creme mit 1-px-Haarlinie, 12 px Radius, 44 px hoch, Lupe links; Fokus verdickt den Rand auf Ink
- Chips, Tabs, Filter: Pillen, Polster 8×16 px. Laut Datei ist aktiv = Creme-Karte #f5f0e0 mit Ink-Schrift; für Mobil **Empfehlung:** aktiv als gefüllte Ink-Pille mit Creme-Schrift, damit der Zustand auch ohne Farbe trägt
- Dialoge und Sheets: Cremeblatt mit 24 px oben, 20 px Rand, Griff als 4-px-Haarlinie
- Signatur-Komponenten: Farbblock mit weißer Innenkachel; Knetberg-Horizont (gerundete Bergsilhouette in Pfirsich/Ocker/Mint) am unteren Rand eines Blocks; Bild im Farbrahmen (Foto mit 10-px-Luft in einer 24-px-Farbkarte)

## Icons
- Stil: massiv gefüllt und rund (Phosphor Fill) – die Icons sind kleine Knetformen, keine Striche
- Größe und Strich: 20 px in Leisten und Knöpfen, 22 px in Karten, kein Strich; Ink auf Creme, Weiß auf Farbe
- Einsatz: sparsam, nie zwei Icons nebeneinander ohne Text; runde 40-px-Flächen für Einzelaktionen
- Umsetzung: Compose `Icons.Filled` bzw. Material Symbols Rounded, Fill 1, Gewicht 400; iOS SF Symbols `.fill`, Gewicht Regular; Web Phosphor `fill`

## Bildsprache
- Bilder liegen fast immer **in** einer Farbfläche, nicht auf der Creme: weiße 16-px-Kachel oder 10 px Luft in einer 24-px-Farbkarte
- Seitenverhältnis 4:3 in Karten, 16:10 im Detailkopf; Radien 12–16 px innen, 24 px außen
- Keine Filter, keine Verläufe über dem Bild – die Farbe daneben macht die Stimmung
- Zusätzlich 3D-Knetillustrationen (Berge, Figuren); frei nachgebaut als gerundete Inline-SVG-Silhouetten mit weicher Oberkante

## Typografie-Stimme
- Display 32–40 px, Gewicht **500** (nie 700), Laufweite −1 bis −2,5 px, Zeilenhöhe 1,0–1,15
- Titel 16–24 px/600, Fließtext 16 px/1,55, Angaben 13 px/500, Versal-Eyebrow 12 px/600 mit 1,5 px Sperrung
- Größenkontrast ist groß (36 px gegen 13 px), Gewichtskontrast klein – das hält den Ton freundlich
- Freier Ersatz: Inter Display 500 mit −0,05 em für Display, Inter für alles andere (laut Datei der nächste Ersatz für Plain Black); alternativ Recoleta 500

## Form, Tiefe und Material
- Radien: 6 px Mini-Badges, 8 px kleine Knöpfe, 12 px Knöpfe und Felder, 16 px Inhaltskarten, 24 px Farbkarten, Pille für Chips
- Linien und Rahmen: nur 1 px #e5e5e5 an Feldern und hellen Karten; Farbkarten haben nie einen Rahmen
- Schatten und Ebenen: keine. Ebene entsteht durch Creme → Farbe → Weiß im Block
- Besondere Oberflächen: Creme-Abstufung #fffaf0 / #faf5e8 / #f5f0e0 / #ebe6d6; dunkles Teal #1a3a3a als seltener Gegenpol

## Bewegung
- Laut Datei: keine Angaben (Animation ausdrücklich nicht im Umfang), Hover wird bewusst nicht dokumentiert
- Empfehlung: Dauer klein 180 ms / Screenwechsel 300 ms, Easing `cubic-bezier(.22, 1, .36, 1)`, Druck-Effekt `scale(.97)` ohne Farbwechsel, Einblenden der Blöcke um 10 px von unten mit 60 ms Versatz, Screenwechsel als weiches Schieben, Fokus (TV) Wachsen auf 1,04
- Compose: `tween(300, easing = CubicBezierEasing(.22f, 1f, .36f, 1f))`, Druck über `spring(dampingRatio = .7f)`, Blöcke mit `AnimatedVisibility` + `slideInVertically`, Liste mit `animateItem()`

## Signatur-Elemente
1. Satte einfarbige 24-px-Blöcke, die reihum die Farbe wechseln und die Seite takten
2. Die weiße 16-px-Innenkachel in jedem Farbblock – echter Inhalt im Farbfeld
3. Große gerundete Display-Schrift in Gewicht 500 mit stark negativer Laufweite
4. Knetberg-Horizont aus weich gerundeten Silhouetten am unteren Rand eines Blocks
5. Cremefläche von oben bis unten – nie Weiß, nie ein dunkler Fuß

## Übertragung auf eine App
- Startscreen: Begrüßung groß, ein großer Farbblock als Hauptinhalt, darunter zwei kleine Blöcke und ein angeschnittenes Farbkarten-Regal
- Liste und Übersicht: 2-spaltiges Raster aus Farbkarten; jede Karte trägt eine weiße Bildkachel, Titel und Angaben – die Farbe markiert die Reihenfolge, nicht die Art
- Detail: Bild im Farbrahmen, Titel groß in 500, Near-Black-Knopf als einzige Hauptaktion, Nebenaktionen als runde Cremeknöpfe mit Haarlinie
- Formulare und Einstellungen: Cremefelder mit Haarlinie, Gruppen als 16-px-Karten, ein Primärknopf unten, nie zwei
- Leere Zustände und Laden: leerer Farbblock mit Knetberg-Silhouette und einer Zeile Text; Platzhalter als cremefarbene 16-px-Flächen ohne Schimmer
- TV: Farbblöcke als Zeilen, Titel 48 px/500, Fokusring in Creme
- Musterscreens: Start mit Ocker-Rückblick und Teal-Speicherblock, Bibliothek als 2-spaltiges Farbkarten-Raster, Detail mit Foto im Pfirsich-Rahmen und Lavendel-Musikkarte

## Vermeiden
- Kein kühles Grau und kein reines Weiß als Fläche – die Cremetönung ist gesetzt
- Display nie über Gewicht 500 setzen; fett wirkt marktschreierisch
- Nie zwei gleiche Farbblöcke hintereinander, nie eine siebte Markenfarbe
- Keine Schatten und keine Verläufe auf Karten; Tiefe kommt aus der Farbe
- Kein dunkler Fuß und keine dunkle Navigationsleiste – die Seite bleibt warm bis unten
- Flache Vektor-Cliparts statt gerundeter Knetformen zerstören den Ton
