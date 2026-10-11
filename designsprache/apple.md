---
slug: apple
marke: Apple
website: https://www.apple.com
ansatz: buehne
ansatz2: minimal
modus: gemischt
aufbau: Randlose Vollbreit-Kacheln im Wechsel hell/dunkel, jede eine zentrierte Bühne für ein Bild
navigation: Schwarze 44-px-Leiste oben + milchige Unterleiste mit Titel und blauer Pille; unten vier Ziele
komponenten: Vollbreit-Kachel, blaue Pillen-Schaltfläche, weiße Rasterkarte 18 px, runder 44-px-Chip über Bildern
icons: Linie, gleichmäßige Stärke, runde Enden, 24–26 px; aktiv gefüllt (SF-Symbols-Art)
bewegung: Sehr ruhig; 200–400 ms, ease-out; Druck = scale(0.95); Einblenden von unten ohne Versatzspielerei
schrift: SF Pro Display/Text, 600 für Titel mit negativer Laufweite, Fließtext 17 px/400
---
# Apple – Designsprache

**Kurz:** Fotografie steht im Mittelpunkt, die Oberfläche tritt zurück. Seiten sind ein Stapel randloser Kacheln, die zwischen Weiß, Pergament (#f5f5f7) und Fast-Schwarz (#272729) wechseln – der Farbwechsel selbst ist der Trenner, es gibt keine Rahmen, keine Deko-Verläufe, keine Schatten an der Oberfläche. Ein einziges Aktionsblau (#0066cc) trägt jede Interaktion.

## Wirkung
- Charakter: ruhig, souverän, museal; Produkt bzw. Bild bekommt eine Bühne, alles andere flüstert.
- Passt zu: Medien- und Fotoapps, Produktkatalogen, Hardware-Begleitern, Shops, Präsentationsapps.
- Passt weniger zu: datendichten Werkzeugen, Dashboards, Apps mit vielen gleichzeitigen Aktionen.

## Aufbau und Raster
- Seitenaufbau: vertikaler Stapel randloser Kacheln ohne Abstand dazwischen; jede Kachel ≈ eine Bildschirmhöhe, Inhalt mittig gestapelt: Titel → einzeilige Unterzeile → ein bis zwei Pillen → Bild.
- Ausrichtung: zentriert in den Bühnen-Kacheln, linksbündig nur in Rasterkarten, Listen und Fußzeile.
- Raster: Textsektionen max. ~980 px, Produktraster ~1440 px, Kacheln vollbreit; Raster 3–5 Spalten, Rinnen 20–24 px. Auf dem Handy eine Spalte, Karten zweispaltig.
- Dichte und Weißraum: sehr niedrig. Kachel-Innenabstand 80 px (Handy 40–48 px), ≥ 64 px Luft über jeder Überschrift, ≥ 40 px um jedes Bild. Karteninnenabstand 24 px, Knopfabstand 11/22 px.
- Rhythmus: hell → dunkel → hell → Pergament. Gleiche Bausteine, nur andere Fläche; dadurch pulsiert die Seite ohne jede Linie.

## Navigation
- Website: zwei Zeilen. Oben `global-nav` 44 px, reines Schwarz, 12-px-Links mit −0.12 px Laufweite, rechts Suche und Tasche. Darunter `sub-nav-frosted` 52 px: Pergament bei 80 % mit `backdrop-filter: blur(20px) saturate(180%)`, links Kategoriename 21 px/600, rechts Inline-Links und eine dauerhafte blaue Pille.
- App: beide Leisten bleiben. Oben die schwarze Leiste (Markenzeichen + zwei Werkzeug-Icons), darunter die milchige Unterleiste mit Screen-Titel 21 px/600 und rechter blauer Pille. Unten vier Ziele (Start, Bibliothek, Suche, Profil) auf Pergament bei 80 % mit Blur, Icon 24 px + Beschriftung 10–11 px; aktiv = gefülltes Icon + 600er Beschriftung + Aktionsblau (nie nur Farbe). Beim Scrollen bleiben beide Leisten stehen, die Unterleiste wird transluzent. App-Muster der Marke (nicht in der Datei).
- TV: horizontale Reiterzeile oben, Inhalte als vollflächige Bühne; Fokus über leichte Vergrößerung und helleren Rand, nicht über Farbe.

## Startscreen
- Ohne Begrüßungskopf: Der Titel der Unterleiste ist die Überschrift, darunter beginnt sofort die erste Bühne.
- Kachel 1 (weiß): Überzeile 12 px/600 Versalien gesperrt, Titel 36–40 px/600 mit −0.4 px, Unterzeile 17 px/400 grau, zwei Pillen (blau gefüllt + blauer Geister-Rand), darunter randloses Bild.
- Kachel 2 (fast schwarz): gleicher Bausatz, Text weiß, Sekundärtext #cccccc; gern zwei nebeneinanderliegende Halbkacheln mit Bild darunter.
- Kachel 3 (Pergament): nüchterne Zahlen – Speicher, Quellen – als Feinschrift mit haarfeiner Fortschrittslinie.

## Komponenten
- Buttons: `button-primary` Aktionsblau #0066cc, Text 17 px/400 weiß, volle Pille, 11/22 px – die Pille ist das Aktionssignal. Geister-Pille: transparent, 1 px #0066cc, blaue Schrift. `button-dark-utility` #1d1d1f, 14 px, Radius 8 px, 8/15 px. Druck: `scale(0.95)`; Fokus: 2 px #0071e3.
- Karten und Kacheln: zwei Sorten. Bühnen-Kachel randlos, Radius 0, ohne Rahmen. `store-utility-card` weiß, 1 px #e0e0e0, Radius 18 px, Innenabstand 24 px, Bild 1:1 mit 8 px Innenradius, Name 17 px/600, Zusatz 17 px/400, darunter blauer Textlink. Kein Schatten.
- Listen: schlichte Textreihen mit 2.41-facher Zeilenhöhe (dichte Linkspalten der Fußzeile), Trenner nur als 1-px-Haarlinie #f0f0f0 oder gar nicht.
- Suche und Eingabefelder: weiß, volle Pille, Höhe 44 px, 12/20 px, 1 px rgba(0,0,0,.08), Lupe 14 px gedämpft, Text 17 px.
- Chips, Tabs, Filter: `configurator-option-chip` – weiße Pille, 12/16 px, 14 px Schrift, 1 px #e0e0e0; ausgewählt 2 px #0071e3 plus 600er Schrift.
- Dialoge und Sheets: Pergament bei 80 % mit Blur, Radius 18 px oben, keine Schatten; Aktionen als Pillen.
- Signatur-Komponenten: `floating-sticky-bar` (64 px, Pergament 80 % + Blur, links Zahl/Hinweis, rechts blaue Pille) und `button-icon-circular` (44 px, rgba(210,210,215,.64), Symbol #1d1d1f) über Fotos.

## Icons
- Stil: Linien-Icons mit gleichmäßiger Stärke und runden Enden, optisch ruhig, nie verspielt (SF-Symbols-Art). Empfehlung, die Datei nennt nur Lupe und Tasche.
- Größe und Strich: 24–26 px in Leisten, 14–18 px inline; Stärke ~1,5/24 px, Umschalter Linie → gefüllt für den aktiven Zustand.
- Einsatz: sparsam. Icons begleiten Beschriftungen, ersetzen sie nur in Leisten und in runden Chips über Bildern.
- Umsetzung: Compose `Icons.Rounded` bzw. Material Symbols Rounded, Gewicht 400, Füllung 0→1 für aktiv; iOS SF Symbols Regular, `.fill` für aktiv; Web Phosphor `regular`/`fill` oder Lucide bei `stroke-width: 1.6`.

## Bildsprache
- Fotos sind der Inhalt, nicht die Dekoration: randlos, rechteckig, Radius 0 in Bühnen-Kacheln; 8 px innerhalb von Karten, 18 px nur bei der Karte selbst.
- Seitenverhältnisse: 21:9 oder höher in der Startbühne, 16:9 in Inhaltsabschnitten, 1:1 im Raster.
- Keine Verläufe über dem Bild, keine Tönung, keine Filter – die Atmosphäre steckt im Motiv. Text liegt neben dem Bild, nicht darauf; Ausnahme: runde 44-px-Chips über dem Vollbild.
- Genau ein Schatten im System: `rgba(0,0,0,.22) 3px 5px 30px` unter freigestellten Motiven auf einer Fläche. Nie an Karten, Knöpfen oder Text.

## Typografie-Stimme
- Größenkontrast groß und ruhig: 56 / 40 / 34 / 28 / 21 / 17 / 14 / 12 px. Gewichtsleiter 300 / 400 / 600 / 700 – 500 fehlt bewusst.
- Titel 600 mit negativer Laufweite (−0.28 bis −0.374 px), Zeilenhöhe 1.07–1.19. Fließtext 17 px/400, Zeilenhöhe 1.47 – nicht 16 px, nicht enger.
- Versalien nur in kleinen Überzeilen (12–14 px) mit ~0.08 em Sperrung. Gewicht 300 bleibt den seltenen luftigen Momenten vorbehalten (24 px Lead, 18 px Store-Knopf).
- Freier Ersatz: Inter (Variable) mit `letter-spacing: -0.01em` auf Displaygrößen und Zeilenhöhe 1.44 im Fließtext; große Titel in Inter Display.

## Form, Tiefe und Material
- Radien: 0 (Kacheln), 5, 8 (Werkzeugknöpfe, Bild in Karte), 11 (Perlkapsel), 18 (Rasterkarte), Pille 9999 (jede Aktion), Kreis (Chip über Foto).
- Linien und Rahmen: 1 px #e0e0e0 an Karten und Chips, 1 px rgba(0,0,0,.08) am Suchfeld, weiche Trennlinie #f0f0f0. Sonst keine Rahmen.
- Schatten und Ebenen: Flächenwechsel statt Höhe. Nur zwei Ausnahmen: der Produktschatten am Bild und `backdrop-filter` an den klebenden Leisten.
- Besondere Oberflächen: Milchglas (Pergament 80 % + Blur) an Unterleiste, Tableiste und Sticky-Bar; drei Fast-Schwarz-Töne (#272729/#2a2a2c/#252527) für kaum merkliche Trennung zweier dunkler Kacheln.

## Bewegung
- Laut Datei: Druckzustand `transform: scale(0.95)` auf allen Knöpfen, Fokusring 2 px #0071e3, `backdrop-filter`-Leisten; Hover wird bewusst nicht dokumentiert.
- Empfehlung: klein 200 ms / Screenwechsel 400 ms, Easing `cubic-bezier(0.25, 0.1, 0.25, 1)`; Einblenden mit 16 px Aufwärtsversatz und 60 ms Staffel je Kachel; Bilder leicht zoomend (1.04 → 1) beim Erscheinen; Fokus (TV) Skalierung 1.06 ohne Farbwechsel.
- Compose: `tween(200, easing = CubicBezierEasing(0.25f, 0.1f, 0.25f, 1f))`, Druck über `animateFloatAsState(0.95f)`, `AnimatedVisibility(fadeIn() + slideInVertically { it / 12 })`, Shared-Element für Bild → Detail.

## Signatur-Elemente
1. Randlose Vollbreit-Kacheln, die zwischen Weiß, Pergament und Fast-Schwarz wechseln – ohne Trennlinie.
2. Zentrierte Stapel: großer 600er Titel mit enger Laufweite, eine Unterzeile, zwei kleine Pillen, darunter das Bild.
3. Genau ein Aktionsblau #0066cc für alles Klickbare; auf dunkler Fläche #2997ff.
4. Milchglasleisten oben und unten plus runde 44-px-Chips über dem Vollbild.
5. Nur ein einziger Schatten im ganzen System – und der liegt unter einem Bild.

## Übertragung auf eine App
- Startscreen: kein Begrüßungsblock, sondern Kachel um Kachel. Erste Kachel = hervorgehobener Inhalt mit Titel, Unterzeile, zwei Pillen, randlosem Bild; zweite Kachel dunkel mit zwei Halbkacheln; dritte Kachel Pergament mit Speicherzahlen.
- Liste und Übersicht: Pergamentfläche, Suchpille, Filterchips als weiße Pillen, zweispaltiges Raster aus weißen 18-px-Karten mit 1:1-Bild; Rinnen 20 px.
- Detail: Vollbild oben mit zwei runden Chips, darunter weiße Bühne mit zentriertem Titel und zwei Pillen, Umschalter als Chips, Fotoraster randlos mit 2-px-Fugen, unten die Milchglas-Sticky-Bar.
- Formulare und Einstellungen: gruppierte Blöcke auf Pergament, Felder als Pillen oder 8-px-Rechtecke, eine blaue Pille als Abschluss, keine Rahmen um Gruppen.
- Leere Zustände und Laden: eine zentrierte Zeile 21 px/600 plus eine blaue Pille auf weißer Fläche; Ladezustände als ruhiges Aufblenden, keine Skelett-Streifen mit Schimmer.
- TV: Bühne vollflächig, Reiter oben, Beschriftungen groß und ruhig, Fokus über Skalierung.
- Musterscreens: Start als Kachelstapel hell/dunkel/pergament, Bibliothek als Rasterkarten auf Pergament, Detail als Vollbild mit zentrierter Bühne, randlosem Fotoraster und Sticky-Bar.

## Vermeiden
- Keine zweite Akzentfarbe; alles Klickbare ist Aktionsblau.
- Keine Schatten an Karten, Knöpfen oder Text – Schatten gehört allein dem Bild.
- Keine Deko-Verläufe und keine getönten Bildüberlagerungen.
- Kein Gewicht 500 und keine abgerundeten Vollbreit-Kacheln.
- Fließtext nie auf 16 px oder enger als 1.47 setzen; Radien nicht mischen (8 / 18 / Pille, nichts dazwischen).
- #2997ff nie auf heller Fläche verwenden – das ist die Dunkelvariante.
