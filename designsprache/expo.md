---
slug: expo
marke: Expo
website: https://expo.dev
ansatz: werkzeug
ansatz2: minimal
modus: hell
aufbau: Reines Weiß, Inhalte in haarlinien-gerahmten Panels; ein himmelblauer Verlauf nur hinter dem Kopfbereich
navigation: Weiße Leiste unten (4 Ziele), aktiv = graue 8-px-Platte hinter dem Icon plus Versal-Label 11 px
komponenten: Geräte-Rahmen mit Fensterleiste, Haarlinien-Karten 12 px, 32-px-Icon-Platten, dunkles Mono-Panel
icons: Lucide-Linien 1,5 px, eckige Enden (square/miter), 18–20 px, einfarbig Tinte oder Grau (Empfehlung)
bewegung: Sachlich: 120/220 ms, cubic-bezier(.2,0,0,1); Druck = 0,97 + #1a1a1a, Einblenden 8 px von unten (Empfehlung)
schrift: Eine Grotesk (Inter) 600/400 plus Mono für jede technische Zahl; Titel eng gesperrt bis −1,08 px
---
# Expo – Designsprache

**Kurz:** Entwicklerwerkzeug mit editorialer Ruhe: reinweiße Fläche, Haarlinien statt Schatten, pechschwarze Knöpfe mit 8 px Radius und ein himmelblauer Dunst, der ausschließlich hinter dem Kopfbereich liegt. Das Markenzeichen ist der Geräte-Rahmen – ein Bild sitzt in einer Karte mit Fensterleiste, als wäre es eine laufende Vorschau. Jede technische Zahl steht in Mono, oft auf einer dunklen Fläche.

## Wirkung
- Charakter: nüchtern, präzise, vertrauenswürdig; leise selbstbewusst statt laut, nie dekorativ.
- Passt zu: Werkzeug-, Entwickler-, Verwaltungs- und Datei-Apps, Dashboards, Medienverwaltung mit vielen Angaben.
- Passt weniger zu: emotionalen Lifestyle-, Kinder- oder Mode-Apps und allem, was sattes Farbspiel braucht.

## Aufbau und Raster
- Seitenaufbau: Kopfband mit Verlaufsdunst und Geräte-Rahmen, darunter weiße Bänder aus gerahmten Karten; 96 px Abschnittsrhythmus im Web, in der App 24–32 px.
- Ausrichtung: Kopfbereich zentriert, alle Listen und Karten strikt linksbündig; Zahlen rechts in eigener Spalte.
- Raster: 4-px-Basis (4/8/12/16/20/24/32/48 px), Inhalt max. 1200 px, 12 Spalten; Kachelraster 8-fach, Karten 3-/2-/1-spaltig.
- Dichte und Weißraum: Karten innen 20–24 px, Listenzeilen 56–64 px, Kartenabstand 16–24 px. Weiß trägt, Haarlinien trennen.
- Rhythmus: Versal-Label 11 px → Karte/Liste → 24 px → nächstes Label. Genau ein dunkles Panel je Screen als Gegengewicht.

## Navigation
- Website: 64 px hohe weiße Kopfleiste, Wortmarke links, Links 14 px/500, rechts Sekundär- plus schwarzer Primärknopf; unter 768 px Hamburger.
- App (Empfehlung): untere Leiste auf Weiß, 1 px `#dcdee0` oben, 4 Ziele Start · Bibliothek · Suche · Profil, Icon 20 px + Label 11 px/600 in Versalien (0,88 px gesperrt). Aktiv = Icon auf 8-px-Platte `#f0f0f3` plus Tinte-Label; inaktiv `#999999`. Leiste bleibt beim Scrollen stehen.
- Detail: Zurück als 36-px-Knopf mit Haarlinie, daneben Pfad „Bibliothek / Alben“ in 13 px; rechts Icon-Knöpfe gleicher Bauart. Statt der Navigation unten eine dunkle Aktionsleiste.
- TV: linke Spalte mit Versal-Labels; Fokus = 2 px Tinte-Rahmen plus `#f0f0f3`-Fläche, keine Vergrößerung.

## Startscreen
- Kopfband mit weichem Himmelverlauf (`#cfe7ff` → transparent, nur hier), darin Versal-Badge, Begrüßung 28 px/600/−0,84 px und eine Zahlenzeile in `#60646c`.
- Darunter der Geräte-Rahmen: weiße Karte, 16 px Radius, 1 px `#dcdee0`, oben eine Fensterleiste mit drei 7-px-Punkten und Mono-Titel, darin das Bild 16:9, darunter Titel, Angaben und ein schwarzer Knopf.
- Zwei weitere Bereiche: „Quellen“ als drei Zeilen mit 32-px-Icon-Platte, Name und Zustand; Speicher als dunkles Mono-Panel mit Balken.

## Komponenten
- Buttons: primär schwarz `#000000`, Text weiß, 14 px/500, 10×18 px, Höhe 40 px, Radius 8 px; sekundär weiß mit 1 px `#dcdee0`; tertiär nur Text in `#0d74ce` – Blau nie auf einem Knopf. Pillen sind Badges vorbehalten.
- Karten und Kacheln: weiß, Radius 12 px, 1 px `#dcdee0`, Innenabstand 20–24 px, höchstens ein Schatten `0 4px 12px rgba(0,0,0,.04)`. Dunkle Variante `#171717` für Code-, Zahlen- und Musikflächen. Quadratische 64-px-Kacheln (Radius 8 px, 1 px `#f0f0f3`) für Quellen und Logos.
- Listen: Tabellenhaltung – Kopfzeile aus Versal-Labels 11 px, Zeilen 64 px mit 48-px-Quadratbild (8 px Radius), Titel 16/600, Angaben 13 px `#60646c`, rechte Spalte in Mono 12 px; 1 px `#f0f0f3` zwischen den Zeilen.
- Suche und Eingabefelder: Höhe 44 px, Radius 8 px, 1 px `#dcdee0`, Innenabstand 12×16 px, Platzhalter `#999999`; Fokus verdickt den Rahmen auf 2 px Tinte.
- Chips, Tabs, Filter: Segmentreihe aus 8-px-Rechtecken mit Haarlinie, 32 px hoch, 13 px/500; aktiv = schwarze Füllung, weiße Schrift. Badge-Pillen nur als Metadaten: `#f0f0f3`, 11 px/600, Versalien, 4×10 px.
- Dialoge und Sheets: weiße Fläche, Radius 16 px oben, 1 px `#dcdee0`, kein starker Schatten; Grau `rgba(23,23,23,.4)` als Schleier.
- Signatur-Komponenten: Geräte-Rahmen mit Fensterleiste; dunkles Mono-Panel (Zahlen, Status, Fortschritt); 32-px-Icon-Platte als Schritt-Marke.

## Icons
- Stil: Linien-Icons, geometrisch und nüchtern (Lucide), eckige Enden – passend zu Haarlinien und 8-px-Radien (Empfehlung).
- Größe und Strich: 20 px in der Leiste, 18 px in Knöpfen, 16 px in Listen und Feldern; Strichstärke 1,5 px, nie gefüllt.
- Einsatz: sparsam, je Zeile höchstens eines; Zustände über Platte und Gewicht, nie nur über Farbe.
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Outlined, Gewicht 400, Füllung 0; iOS SF Symbols Regular ungefüllt; Web Lucide (`stroke-width: 1.5`, `stroke-linecap: square`) oder Phosphor Light.

## Bildsprache
- Bilder sind Produktvorschauen, keine Stimmungsbilder: sie sitzen im Geräte-Rahmen oder in einer gerahmten Kachel, nie randlos über den ganzen Screen.
- Radius 8 px (Kachel/Listenbild), 10–12 px innerhalb des Geräte-Rahmens, Rahmen stets 1 px `#dcdee0` oder `#f0f0f3`.
- Seitenverhältnisse 16:9 im Kopf, 1:1 in Listen und Rastern; keine Farbfilter, keine Verläufe über dem Bild – nur der Himmelsdunst hinter der Karte.
- Rasterbilder dicht an dicht mit 8 px Fuge; Fotoraster dreispaltig.

## Typografie-Stimme
- Inter als einzige Grotesk: Display 600, Text 400; Mono (JetBrains Mono) für jede Zahl, Dauer und Statuszeile.
- Größenkontrast moderat: 28/22/18/16/14/13/11 px. Negative Laufweite nur im Display: −0,5 px ab 22 px, −0,84 px bei 28 px, −1,08 px bei 36 px.
- Versalien ausschließlich im 11-px-Label (600, +0,88 px gesperrt). Zeilenhöhe 1,2 im Display, 1,5 im Text.
- Freier Ersatz: Inter und JetBrains Mono sind frei verfügbar (Google Fonts); hier gerendert mit Inter und DejaVu Sans Mono.

## Form, Tiefe und Material
- Radien: 4 px Inline-Tag, 6 px kompakte Zeile, 8 px Knopf/Feld/Kachel, 12 px Karte, 16 px Geräte-Rahmen, 24 px selten; Pille nur Badge.
- Linien und Rahmen: 1 px `#f0f0f3` als Standardtrenner, `#f5f5f7` leichter, `#dcdee0` für Karten- und Knopfkanten.
- Schatten und Ebenen: genau eine Stufe `0 4px 12px rgba(0,0,0,.04)`; Tiefe entsteht sonst aus Rahmen und aus dem Umschlag auf `#171717`.
- Besondere Oberflächen: der Himmelsverlauf `#cfe7ff`/`#a8c8e8` nur im Kopfbereich; dunkle Panels mit `#1a1a1a` als zweiter Stufe innen.

## Bewegung
- Laut Datei: keine Angaben (Animationszeiten ausdrücklich außerhalb des Umfangs).
- Empfehlung: klein 120 ms / Screenwechsel 220 ms, Easing `cubic-bezier(.2, 0, 0, 1)`; Druck = `scale(.97)` plus Füllung `#1a1a1a`; Einblenden 8 px von unten mit 40 ms Staffel je Karte; Screenwechsel als weiches Überblenden ohne Verschiebung; Fokus (TV) = Rahmen wächst von 1 px auf 2 px in 120 ms.
- Compose: `tween(220, easing = CubicBezierEasing(.2f, 0f, 0f, 1f))`, Druck über `animateFloatAsState(.97f)`, Listen mit `animateItem()`, Kopfbereich als Shared-Element-Übergang zwischen Liste und Detail.

## Signatur-Elemente
1. Geräte-Rahmen: Karte mit Fensterleiste (drei Punkte, Mono-Titel), in der das Bild wie eine laufende Vorschau sitzt.
2. Pechschwarzer 8-px-Knopf als einzige Aktionsfarbe – kein Buntton, keine Pille.
3. Dunkles Mono-Panel für Zahlen, Speicher und Status mitten im weißen Screen.
4. Haarlinien-Tabelle mit Versal-Kopfzeile und rechter Mono-Spalte.
5. Himmelblauer Verlaufsdunst ausschließlich hinter dem Kopfbereich.

## Übertragung auf eine App
- Startscreen: Verlaufs-Kopf mit Badge, Begrüßung und Zahlenzeile; darunter der Geräte-Rahmen als hervorgehobener Inhalt, dann Quellen-Zeilen und ein dunkles Mono-Panel für Speicher.
- Liste und Übersicht: Suchfeld 44 px plus Filter-Segmente, danach eine Tabelle mit Versal-Kopfzeile, quadratischen Vorschaubildern und rechter Mono-Spalte; keine schwebenden Karten.
- Detail: Geräte-Rahmen mit großem Bild, Titel 28 px, Badge-Pillen für Angaben, schwarzer Hauptknopf plus weiße Icon-Knöpfe, Segment-Umschalter, 3-spaltiges Fotoraster, unten eine dunkle Aktionsleiste.
- Formulare und Einstellungen: linksbündige Felder 44 px mit Versal-Label darüber, Gruppen als Haarlinien-Karten, Hilfetext 13 px `#60646c`, Primärknopf schwarz unten rechts.
- Leere Zustände und Laden: gerahmte Karte mit 32-px-Icon-Platte, Satz in 16 px und Mono-Zeile mit dem Grund; Laden als graue Haarlinien-Platzhalter in Zeilenform, kein Spinner.
- TV: Geräte-Rahmen wird zur Bühne, Listen behalten die Tabellenhaltung; Fokus über Rahmenstärke und Flächenwechsel.
- Musterscreens: Start mit Verlaufs-Kopf, Geräte-Rahmen und Mono-Speicherpanel; Bibliothek als Haarlinien-Tabelle mit Segmentfiltern; Detail mit großem Geräte-Rahmen, Badge-Angaben, schwarzem Hauptknopf und dunkler Musikleiste.

## Abgrenzung zu Lovable
Beide sind Werkzeuge zum App-Bauen, aber: Expo ist reinweiß, rechtwinklig-technisch (8/12 px), arbeitet mit Haarlinien-Tabellen, Mono-Zahlen, dunklen Panels und schwarzen Knöpfen. Lovable ist cremefarben, pillenförmig, ohne Mono, führt über ein großes Eingabefeld mit Vorschlags-Pillen und zeigt Inhalte als bordierte Galerie-Karten.

## Vermeiden
- Keine zweite Aktionsfarbe: Schwarz ist die einzige Füllung für Primärknöpfe; Blau `#0d74ce` bleibt Textlink im Fließtext.
- Keine Pillen-Knöpfe (9999 px) – Pillen sind Badges; CTAs bleiben bei 8 px.
- Display nicht unter 600 und nicht über 700 setzen; keine fetten 700er-Überschriften.
- Den Himmelsverlauf nicht über den Kopfbereich hinaus wiederholen und nicht auf Karten legen.
- Keine weichen Schlagschatten-Stapel und keine randlosen Vollbilder – Bilder bleiben gerahmt.
- Zahlen nicht in der Grotesk setzen, wenn Mono zur Verfügung steht; das Mono-Detail trägt den Charakter.
