---
slug: framer
marke: Framer
website: https://www.framer.com
ansatz: leuchten
ansatz2: galerie
modus: dunkel
aufbau: Fast schwarze Arbeitsfläche, alles liegt in gerundeten Kacheln (15/20/30 px); ein Verlaufs-Spotlight bricht den Rhythmus
navigation: Schwebende Pillen-Leiste unten (4 Ziele); aktiv = weiße Pille mit schwarzem Icon und Text, inaktiv nur graues Icon
komponenten: Weiße Pill-Buttons, Charcoal-Pillen, Verlaufs-Spotlight-Karte, Vorschau-Kacheln, runde 40-px-Icon-Knöpfe
icons: Phosphor Regular, gleichmäßige runde Linie, 20–22 px, nie gefüllt; Aktionen in Kreisen 40–44 px
bewegung: Kurz und federnd: 150/300 ms, cubic-bezier(.2,.8,.2,1), Druck = Skalieren auf 0,96, kein Verschieben
schrift: Geometrische Display-Schrift 500 mit −5 % Laufweite, Fließtext Inter 400/500, Hierarchie über Größe statt Gewicht
---
# Framer – Designsprache

**Kurz:** Die Seite ist eine schwarze Arbeitsfläche, auf der alles als gerundete Kachel liegt – es gibt keine hellen Abschnitte und keine randlosen Flächen. Hierarchie entsteht durch Flächenstufen (Canvas → Surface 1 → Surface 2), nicht durch Schriftgewicht oder Farbe. Signatur ist eine einzige, übergroße Verlaufs-Spotlight-Karte, die den monochromen Kachelrhythmus bricht, dazu weiße Pill-Buttons und Display-Schrift mit extrem negativer Laufweite.

## Wirkung
- Charakter: selbstbewusst, modern, plakativ-ruhig; wirkt wie ein Werkzeug-Canvas mit Poster-Typografie.
- Passt zu: Kreativ- und Bau-Werkzeugen, Vorlagen- und Galerie-Apps, Entwickler- und SaaS-Produkten, Portfolios.
- Passt weniger zu: hellen Lese-Apps, verspielten Kinder-Apps, Marken mit vielen Akzentfarben.
- Abgrenzung zu Runway (gleiche Branche, auch dunkel): Framer rahmt jedes Bild in eine gerundete Kachel (15–30 px) auf durchgehend schwarzem Canvas, nutzt Pillen, eine farbige Verlaufskarte und eine Leiste unten; Runway zeigt Bilder randlos und eckig (0–8 px), ohne Karten und Pillen, mit Versal-Textnavigation oben und hellen Lesebändern.

## Aufbau und Raster
- Seitenaufbau: Poster-Kopf (große Aussage) → Kachelgitter → ein Verlaufs-Spotlight → wieder Kacheln. Abschnitte trennen sich durch Flächenwechsel, nicht durch Linien.
- Ausrichtung: linksbündig, Inhalt in einer Spalte; Kacheln füllen die Breite.
- Raster: Basiseinheit 5 px, Skala 1/4/8/12/15/20/30/40/96 px; Web-Container ca. 1199 px, Kachelgitter 2-spaltig ab 810 px, darunter 1-spaltig.
- Dichte und Weißraum: Abschnittsabstand 96 px (Web), App 24–30 px; Kachel-Innenabstand 20 px (Karten), 30 px (Spotlight), 12 px (Vorschau-Kacheln); Seitenrand App 20 px, Kachelfuge 8–12 px.
- Rhythmus: „Das Schwarz ist der Weißraum“ – lange ruhige Strecken, dann eine laute Kachel.

## Navigation
- Website: klebende Leiste 56 px auf Canvas, Wortmarke links, Links mittig, rechts Charcoal-Pille + weiße Pille; unter 810 px Hamburger, die weiße Pille bleibt sichtbar.
- App (Empfehlung): schwebende Pillen-Leiste unten, 16 px Abstand zum Rand, Höhe 62 px, Radius 100 px, Fläche Surface 1 mit 0,5-px-Lichtkante oben und Schatten 0 10px 30px rgba(0,0,0,.25). Vier Ziele (Start, Bibliothek, Suche, Profil). Aktiv = weiße Pille mit schwarzem Icon **und** Beschriftung (Markenlogik „Auswahl = Fläche, nicht Farbe“), inaktiv nur Icon in Ink-Muted. Beim Scrollen bleibt sie stehen.
- Detail: runder 40-px-Zurück-Knopf (Surface 1) oben links, Nebenaktionen als runde Knöpfe oben rechts; die Pillen-Leiste bleibt.
- TV: horizontale Pillen-Leiste oben; Fokus = weiße Pille, kein Leuchten.

## Startscreen
- Kopfzeile 56 px: neutrales Zeichen links, rechts runder Icon-Knopf und weiße Pill-Aktion.
- Poster-Begrüßung 40 px, darunter Kennzahlen in Ink-Muted.
- Danach **eine** Verlaufs-Spotlight-Karte (30 px Radius) mit Rückblick: Augenbrauen-Label, Titel 30 px, Angaben, weiße Pille, Vorschaubild 15 px.
- Danach Quellen als Charcoal-Pillen mit Icon und ein Kachelgitter „Zuletzt hinzugefügt“ (2-spaltig), unten von der Leiste angeschnitten.

## Komponenten
- Buttons: Primär = weiße Pille, Text Schwarz 14 px 500, Radius 100 px, Polster 10 × 15 px, Mindesthöhe 44 px. Sekundär = Pille in Surface 1 mit weißem Text. Auf unruhigem Grund = Pille in Surface 2 bzw. Weiß 18 %. Runde Icon-Knöpfe 40 px (Touch 44 px) in Surface 1. Nie Ghost-Buttons mit Rahmen, nie eckige CTAs.
- Karten und Kacheln: Surface 1 (#141414), Radius 20 px, Polster 20–24 px; hervorgehobene Karte Surface 2 (#1c1c1c), gleiche Form. Vorschau-Kachel: Surface 1, Radius 15 px, Polster 12 px, Bild innen Radius 10 px, Titel 14 px 500, Angaben 13 px Ink-Muted. Schwebende Karten: 0,5 px Lichtkante Weiß 10 % oben + Schatten 0 10px 30px rgba(0,0,0,.25).
- Listen: Zeilen als eigene Kacheln (Surface 1, Radius 15 px, 8 px Fuge) statt durchgehender Liste mit Trennlinien; Bild 56 px Radius 10 px, Titel 15 px, Angaben 13 px Ink-Muted, rechts Wert oder Caret.
- Suche und Eingabefelder: Surface 1, Radius 10 px, Polster 10 × 14 px, Höhe 44 px, Text 15 px, Platzhalter Ink-Muted. Fokus: Ring `0 0 0 1px rgba(0,153,255,.15)` plus 1 px #0099ff – die einzige farbige Tiefe.
- Chips, Tabs, Filter: Pillen. Inaktiv Canvas-Fläche mit Ink-Muted, aktiv Surface 2 mit weißem Text (Auswahl = Flächenstufe). Polster 8 × 14 px, Höhe ≥ 40 px, horizontal scrollbar statt umbrechend.
- Dialoge und Sheets: Surface 1, Radius 30 px oben, Lichtkante + Schatten Stufe 2, Griff 36 × 4 px in Weiß 20 %.
- Signatur-Komponenten: Verlaufs-Spotlight-Karte (30 px Radius, Verlauf aus Violett/Magenta/Orange/Koralle, weißer Text, weiße Pille); weiße Pille als einzige Primäraktion; schwebende Pillen-Leiste.

## Icons
- Stil (Empfehlung; die Datei nennt nur runde Icon-Knöpfe 32–40 px): gleichmäßige, runde Linien-Icons im geometrischen Raster – Phosphor Regular. Nie gefüllt, nie zweifarbig, nie mit Akzentfarbe.
- Größe und Strich: 20 px in Leiste und Zeilen, 22 px in runden Knöpfen, 16 px in Pillen; Strich ca. 1,6 px auf 24er-Raster.
- Einsatz: sparsam – Navigation, runde Aktionsknöpfe, Quellen-Pillen, Caret in Zeilen. Kategorien werden benannt, nicht bebildert; Text vor Icon.
- Umsetzung: Compose `Icons.Rounded` bzw. Material Symbols Rounded, Gewicht 400, Füllung 0; iOS SF Symbols `.regular`, ohne `.fill`; Web Phosphor Regular oder Lucide `stroke-width: 1.75` mit runden Enden.

## Bildsprache
- Laut Datei: eingebettete Vorschauen behalten ihr Seitenverhältnis und werden nie beschnitten; Vorschau-Kacheln 20 px Radius mit 15 px Innenabstand; Verlaufskarten behalten ihre Verlaufsrichtung über alle Breiten.
- Übertragung: Bilder liegen immer **in** einer Kachel, nie randlos – Radius 10 px (im Polster), 15 px (Vorschau), 20 px (großes Bild); Seitenverhältnis 16:9 oder 4:3, Fuge 8 px. Kein Verlauf über dem Bild, kein Filter; Titel stehen unter dem Bild, nicht darauf. Farbe im Screen kommt aus genau einer Verlaufskarte, nicht aus den Fotos.

## Typografie-Stimme
- Zwei Rollen: geometrische Display-Schrift (500) für Aussagen, Inter für alles Lesbare. Hierarchie über Größe und Laufweite, nie über 700er-Gewichte.
- Display 110/85/62/32 px, Gewicht 500, Zeilenhöhe 0,85–1,13, Laufweite −5,5/−4,25/−3,1/−1,0 px (etwa −5 % der Größe). App: Poster 40 px/−2 px, Kacheltitel 30 px/−1,5 px, Abschnitt 22 px/−0,8 px.
- Text 18/15 px, 400, Zeilenhöhe 1,3, Laufweite −0,18/−0,15 px; dicht 14 px 500; Caption 13 px 500; Micro 12 px 400. Zahlen tabellarisch (`tnum`).
- Zweistufige Hierarchie im Text: Ink (Weiß) oder Ink-Muted (#999) – nichts dazwischen.
- Freier Ersatz: Poppins Medium (500) oder Mona Sans/Geist für Display, Inter für Text; Laufweite von Hand nachziehen, OpenType-Varianten `cv01/cv05/cv09/cv11`, `ss03/ss07` einschalten.

## Form, Tiefe und Material
- Radien: 4 px Chip, 6 px Tag, 10 px Feld/Bild im Polster, 15 px Vorschau-Kachel und Listenzeile, 20 px Karte, 30 px Spotlight und Sheet, 100 px Pille, voll rund Icon-Knopf und Avatar.
- Linien und Rahmen: 1 px #262626 nur an Eingabegruppen und Tabellen; feiner #1a1a1a zwischen Zeilen. Keine Umrandung an Karten – Flächenstufe statt Rahmen.
- Schatten und Ebenen: Stufe 0 flach; Stufe 1 Surface 1 auf Canvas; Stufe 2 Lichtkante Weiß 10 % oben + `0 10px 30px rgba(0,0,0,.25)`; Stufe 3 Ring `rgba(0,153,255,.15)` für Fokus und Auswahl.
- Besondere Oberflächen: Verläufe ausschließlich als Karte (Violett #6a4cf5, Magenta #d44df0, Orange #ff7a3d, Koralle #ff5577), nie als Abschnittsgrund; höchstens ein bis zwei pro Ansicht. Kein Glas, keine Muster, kein Leuchten um Buttons.

## Bewegung
- Laut Datei: Druckzustand der Primärpille ist ein Verkleinern per `transform: scale`, kein Abdunkeln; Fokus erscheint als blauer Ring.
- Empfehlung: Dauer klein 150 ms / Screenwechsel 300 ms, Easing `cubic-bezier(0.2, 0.8, 0.2, 1)`; Druck = `scale(0.96)`; Einblenden = Kacheln 10 px von unten, gestaffelt 40 ms; Screenwechsel = Detail wächst aus der Kachel (Shared Element); Fokus (TV) = weiße Pille wächst in 150 ms.
- Compose: `tween(300, easing = CubicBezierEasing(0.2f, 0.8f, 0.2f, 1f))`, `spring(dampingRatio = 0.8f, stiffness = 400f)` für den Druck, `animateItem()` für Listen, `SharedTransitionLayout` von Kachel zu Detail.

## Signatur-Elemente
1. Eine einzige übergroße Verlaufs-Spotlight-Karte (30 px Radius) in einem sonst monochromen Kachelgitter.
2. Weiße Pille als einzige Primäraktion – nie eckig, nie farbig.
3. Flächenstufen Canvas → Surface 1 → Surface 2 als einziges Tiefen- und Auswahlsignal.
4. Poster-Typografie mit etwa −5 % Laufweite über ruhigem Schwarz.
5. Schwebende Pillen-Leiste unten, aktives Ziel als weiße Pille mit Text.

## Übertragung auf eine App
- Startscreen: Poster-Begrüßung mit Kennzahlen, eine Verlaufs-Spotlight-Karte für den Rückblick, Quellen als Charcoal-Pillen, darunter ein 2-spaltiges Kachelgitter.
- Liste und Übersicht: Poster-Titel, Suchfeld (Radius 10), Filter-Pillen, dann Einträge als einzelne Surface-1-Zeilenkacheln mit 8 px Fuge – keine durchgehende Liste mit Trennlinien.
- Detail: großes Bild als 20-px-Kachel (nicht randlos), Titel 40 px, weiße Pille als Hauptaktion neben runden Icon-Knöpfen, eine Verlaufskarte für die Diashow-Musik, Pillen-Umschalter, Fotoraster mit 10 px Radius.
- Formulare und Einstellungen: Zeilen als Kacheln (Surface 1, 15 px), Label links Ink, Wert rechts Ink-Muted; Felder Radius 10 px, Fokus mit blauem Ring; Umschalter als Pille.
- Leere Zustände und Laden: Kachel in Surface 1 mit kurzem Satz (15 px Ink-Muted) und weißer Pille; Platzhalter = Surface 1 mit Puls von 0,6 auf 1 Deckkraft, kein Schimmer-Verlauf.
- TV: Kachelgitter mit 20 px Radius auf Canvas, Pillen-Leiste oben, Fokus = weiße Pille bzw. 2 px weiße Umrandung an der Kachel (Empfehlung).
- Musterscreens: Start mit Verlaufs-Spotlight und Kachelgitter, Bibliothek als Pillen-Filter über Zeilenkacheln, Album „Lissabon“ als Bildkachel mit weißer Pille und Verlaufskarte für die Musik.

## Vermeiden
- Helle Abschnitte oder ein Light-Mode; die Identität ist durchgehend dunkel.
- Blau (#0099ff) als Flächen- oder Buttonfarbe – es ist Signalfarbe für Links, Fokus und Auswahl.
- Verläufe als Abschnittshintergrund oder drei und mehr Verlaufskarten in einer Ansicht.
- Eckige CTAs, Ghost-Buttons mit Rahmen, Rahmen um Karten statt Flächenstufen.
- Grautöne zwischen Ink und Ink-Muted, Gewichte 700+ für Hierarchie, entschärfte Display-Laufweite.
- Randlose Vollbilder und Bildtitel auf dem Bild – Bilder bleiben in Kacheln, Titel stehen darunter.
