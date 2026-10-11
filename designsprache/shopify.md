---
slug: shopify
marke: Shopify
website: https://www.shopify.com
ansatz: buehne
ansatz2: galerie
modus: gemischt
aufbau: Zwei getrennte Spuren: kinoschwarze Bildseiten mit riesiger dünner Schrift, helle Creme-Seiten zum Handeln
navigation: Empfehlung: volle Leiste unten, Polarität des Screens; aktives Ziel als gefüllte Pille mit Icon + Label
komponenten: Pillen als einzige Knopfform, randlose Fotoflächen, 12-px-Karten mit gestapelten Mini-Schatten, Mint-Tags
icons: Empfehlung: dünne Linien-Icons (Lucide 1.5), 20–22 px, nur Schwarz oder Weiß – passend zur dünnen Schrift
bewegung: Empfehlung: ruhig und lang, 180/320 ms, cubic-bezier(.2,.8,.2,1); Bild blendet auf, Pille füllt sich
schrift: Riesige Grotesk im Gewicht 300–330 für Titel, Inter 420–550 für alles Bedienbare; Versal-Eyebrow 12 px
---
# Shopify – Designsprache

**Kurz:** Zwei Spuren, die sich nie mischen: kinoschwarze Seiten mit randloser Fotografie, riesigen Titeln im Gewicht 330 und genau einer Aktion – und helle Creme-Seiten zum Vergleichen und Handeln mit Mint- und Pistaziengrün. Gemeinsam ist beiden die Pille als einzige Knopfform und die Trennung von dünner Display-Grotesk und kräftigerem Inter.

## Wirkung
- Charakter: redaktionell-kinohaft, ruhig, erwachsen; Großzügigkeit statt Dekoration, Fotografie trägt die Seite.
- Passt zu: Medien-, Foto-, Reise- und Shop-Apps, Portfolios, allem mit starken Bildern und klaren Entscheidungen.
- Passt weniger zu: Daten-Werkzeugen mit vielen Reglern, Apps ohne Bildmaterial, verspielten Kinder-Apps.
- Besonderheit beim Übertragen: Pro Screen eine Spur wählen – ein Screen ist entweder schwarz-kinohaft oder hell-transaktional, nie beides.

## Aufbau und Raster
- Seitenaufbau (dunkel): Text in freier schwarzer Fläche, darunter oder darüber ein randloses Bild, das über den Rand hinausläuft; pro Band genau eine Aktion.
- Seitenaufbau (hell): dichtere Bänder auf #fbfbf5 mit Karten, Tabellen und Tags; Abstände halbieren sich gegenüber der dunklen Spur.
- Ausrichtung: linksbündig, Bilder randlos von Kante zu Kante.
- Raster: 8-px-Basis (feine Schritte 2/4), Abstände 2/4/8/12/16/24/32/64; Web-Container 1440–1600 px, Lesespalte 720–840 px, App-Seitenrand 24 px.
- Dichte und Weißraum: dunkel 64–128 px zwischen Bändern (App 28–40), hell 48–64 px (App 16–20); Karten-Innenabstand 32 px (App 16).
- Rhythmus: Versal-Eyebrow 12 px → 10 px → Titel 48–96 px (App 44–56) → 12 px → Text 16 px → 24 px → genau eine Pille.

## Navigation
- Website: Leiste oben in der Polarität der Seite (schwarz bzw. weiß), Padding 16 × 24, Wortmarke links, Links mittig, rechts zwei Pillen (Umriss + gefüllt); mobil Hamburger.
- App (Empfehlung): feste Leiste unten über die volle Breite, 76 px, in der Polarität des Screens – Schwarz #000 mit 1 px #1e2c31 Oberkante auf dunklen Screens, Weiß auf hellen. Vier Ziele (Start, Bibliothek, Suche, Profil). Aktiv: Icon **und** Label in einer gefüllten Pille (Weiß mit schwarzer Schrift auf Dunkel, Schwarz mit weißer Schrift auf Hell), 44 px hoch. Inaktiv: nur Icon in Schatten-40 #a1a1aa, kein Label – die Pille ist der Aktiv-Zustand.
- Detailseiten: Zurück als 44-px-Pillenkreis mit 2 px weißem Umriss über dem Bild; die Navigation bleibt, darüber darf eine schmale Zeile mit Haarlinie stehen.
- TV: Reiter oben als Pillen; Fokus = gefüllte Pille (Weiß auf Schwarz), keine Vergrößerung, kein Leuchten.

## Startscreen
- Kinospur: schwarze Fläche, Versal-Eyebrow, Titel 52–56 px im Gewicht 300, eine Zeile Angaben in Schatten-40, darunter ein randloses Bild über die volle Breite, darunter genau eine Pille mit weißem 2-px-Umriss.
- Kein Text auf dem Bild, kein Verlauf darüber – die Typografie steht in freier schwarzer Fläche.
- Darunter ein zweites Band („Zuletzt hinzugefügt“) als angeschnittene Reihe aus 20-px-Fotoflächen mit kleinen Versal-Labels darüber.

## Komponenten
- Buttons: ausschließlich Pillen 9999 px, Padding 12 × 24, Label Inter 16/420, Höhe 44–48 px. Gefüllt Schwarz mit Weiß (gedrückt #3f3f46); auf Dunkel Umriss 2 px Weiß auf transparent; auf Hell Umriss 1 px Schwarz; Mint #c1fbd4 mit schwarzer Schrift für die hervorgehobene Aktion (nur helle Spur). Icon-Knöpfe sind 44-px-Kreise mit derselben Umrissregel.
- Karten und Kacheln: hell – Weiß, 12 px Radius, 1 px #e4e4e7, gestapelte Mini-Schatten `0 8px 8px rgba(0,0,0,.1), 0 4px 4px rgba(0,0,0,.1), 0 2px 2px rgba(0,0,0,.1), 0 0 0 1px rgba(0,0,0,.1)`; hervorgehoben in Mint #c1fbd4, breite Bänder in Pistazie #d4f9e0. Dunkel – #0a0a0a, 12 px, Lichtsaum `inset 0 1px 0 rgba(255,255,255,.04)`, keine Schlagschatten. Fotoflächen 20 px Radius oder ganz randlos.
- Listen: helle Spur – volle Kartenzeilen mit Bild links (96 × 72, 8 px), Titel 20/500, Angaben 14/500 in Schatten-50, rechts ein Pillen-Tag für die Art. Dunkle Spur – Fotoflächen statt Zeilen.
- Suche und Eingabefelder: Weiß, 8 px Radius (nicht Pille!), 1 px #e4e4e7, Höhe 44 px, Text 16/420; Fokus 1 px Schwarz.
- Chips, Tabs, Filter: Pillen-Tags, Padding 4 × 12, Versal-Eyebrow 12 px. Inaktiv Weiß mit 1 px #e4e4e7, aktiv gefüllt Schwarz mit Weiß (auf Dunkel umgekehrt); Mint #c1fbd4 und Schatten-30 #d4d4d8 für Kategorien und Zustände.
- Dialoge und Sheets: Weiß, 12 px, Schatten `0 25px 50px -12px rgba(0,0,0,.25)`; auf der dunklen Spur #0a0a0a flach mit Lichtsaum.
- Signatur-Komponenten: randlose Fotofläche, riesiger dünner Titel in leerer schwarzer Fläche, Umriss-Pille mit 2 px Weiß, Mint-/Pistazien-Flächen, gestapelte Mini-Schatten auf Hell.

## Icons
- Stil (Empfehlung, die Datei nennt keine Icon-Sammlung; die Marke arbeitet fast ohne Icons): sehr sparsame, dünne Linien-Icons, einfarbig Schwarz oder Weiß, passend zur dünnen Display-Schrift.
- Größe und Strich: 22 px in der Navigation, 18–20 px in Pillen und Zeilen; Strich 1,5 px, runde Enden.
- Einsatz: nur dort, wo ein Wort fehlt; Aktiv-Zustände über die gefüllte Pille, nie über Farbe allein. Kein Icon über 24 px, keine Flächenfüllung.
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Outlined, Gewicht 200–300, Füllung 0; iOS SF Symbols `.light`; Web Lucide `stroke-width: 1.5`.

## Bildsprache
- Laut Datei: Fotografie randlos und ohne Rahmen, auf Kinoseiten über den Container hinaus; kein Scrim, kein Text auf dem Bild; auf der hellen Spur Bilder in 12-px-Behältern ohne Schatten; Logostreifen in Graustufen, 24–32 px hoch.
- Übertragung: Hauptbild über die volle Breite ohne Radius (die Statusleiste darf darüber liegen), Reihenbilder als 20-px-Fotoflächen, Raster randlos mit 2 px Fuge von Kante zu Kante.
- Keine Verläufe, keine Tönung, kein Text im Bild; Avatare in Graustufen (`filter: grayscale(1)`), rund, ohne Rahmen – das ist der einzige Bildfilter der Marke.

## Typografie-Stimme
- Zwei Stimmen: Display-Grotesk (Neue Haas Grotesk Display) im Gewicht 330 für alle Titel – die Dünnheit ist die Marke –, Inter 420–550 für Text, Labels, Knöpfe.
- Größen: Display 96/70/55/48 px (App 56/44/36), Überschriften 28/24/20/18 px in 400–500, Text 18/16 px, Bildunterschrift 14/500, Versal-Eyebrow 12 px/400 mit +0,72 px.
- Laufweite: nur das größte Display bekommt +2,4 px, darunter 0; Überschriften +0,3 bis +0,7 px; Zeilenhöhe 1,0–1,16 bei Displays, 1,5 im Text.
- Besonderheit: `font-feature-settings: "ss03"` auf allen Rollen (Zeichen-Signatur der Marke).
- Freier Ersatz: Display – Inter Display im Gewicht 200–300 (nie 400+); Text – Inter; Code – Systemschrift Mono.

## Form, Tiefe und Material
- Radien: 4 px Felder und Haarlinien-Tags, 5–8 px Bildbehälter und Eingaben, 12 px Karten, 20 px Fotoflächen, 9999 px für jeden Knopf und Tag.
- Linien und Rahmen: 1 px #e4e4e7 auf Hell, 1 px #1e2c31 auf Dunkel; Umriss-Pille 2 px Weiß auf Dunkel, 1 px Schwarz auf Hell.
- Schatten und Ebenen: dunkel flach mit Lichtsaum `inset 0 1px 0 rgba(255,255,255,.04)`; hell gestapelte Mini-Schatten (vier Lagen à 10 % Schwarz) als weicher Papierhof; Modal `0 25px 50px -12px rgba(0,0,0,.25)`.
- Besondere Oberflächen: Mint #c1fbd4 und Pistazie #d4f9e0 als Flächen nur auf der hellen Spur; Creme #fbfbf5 als Grundfläche; dunkles Teal #1e2c31 nur für Haarlinien und seltene Karten. Keine Verläufe, keine Körnung.

## Bewegung
- Laut Datei: keine Angaben.
- Empfehlung: Dauer klein 180 ms / Screenwechsel 320 ms, Easing `cubic-bezier(0.2, 0.8, 0.2, 1)`; Druck-Effekt: gefüllte Pille zu #3f3f46, Umriss-Pille füllt sich weiß und dreht den Text auf Schwarz; Einblenden: Bild von Deckkraft 0 in 320 ms, Titel 60 ms später; Reihen 80 ms gestaffelt; Screenwechsel als Überblendung mit 1,02-Bildzoom; Fokus (TV): Pille füllt sich in 180 ms.
- Compose: `tween(180, easing = CubicBezierEasing(0.2f, 0.8f, 0.2f, 1f))`, `tween(320)` für Screenwechsel, `AnimatedVisibility(fadeIn(tween(320)))`, `animateItem()`; kein Federn, kein Überschwingen.

## Signatur-Elemente
1. Zwei getrennte Spuren: kinoschwarz oder hell-creme – nie gemischt, auch die Navigation dreht die Polarität.
2. Riesiger Titel im Gewicht 300–330 in freier Fläche, Bild strikt daneben statt darunterliegend.
3. Randlose Fotografie von Kante zu Kante, ohne Scrim und ohne Text darauf.
4. Die Pille als einzige Knopfform – gefüllt, 2 px weiß umrissen oder mint.
5. Mint- und Pistazienflächen plus gestapelte Mini-Schatten auf der hellen Spur.

## Übertragung auf eine App
- Startscreen (dunkle Spur): Eyebrow, 56-px-Titel, Angabe, randloses Bild, genau eine Umriss-Pille; darunter eine angeschnittene Reihe aus 20-px-Fotoflächen.
- Liste und Übersicht (helle Spur): Creme-Fläche, 44-px-Titel, 8-px-Suchfeld, Pillen-Filter (aktiv gefüllt schwarz), Pistazien-Band für Speicher und Quellen, danach volle Kartenzeilen mit Bild links und Pillen-Tag rechts.
- Detail (dunkle Spur): randloses Bild bis unter die Statusleiste, darunter Eyebrow, 52-px-Titel, Angaben, eine gefüllte Pille plus zwei Kreis-Pillen, Pillen-Umschalter, randloses Fotoraster mit 2 px Fuge, schmale Musikzeile mit Haarlinie.
- Formulare und Einstellungen: helle Spur, Felder 8 px, Abschnitte als weiße Karten mit Mini-Schatten, Absenden als schwarze Pille, Hervorhebung als Mint-Pille.
- Leere Zustände und Laden: dunkel – ein Satz in 36 px und eine Umriss-Pille; hell – Pistazien-Band mit kurzem Satz; Laden als ruhiges Aufblenden der Fotoflächen, kein Spinner.
- TV: Kinospur mit randlosem Bild, Titel links in freier Fläche, Reihen aus Fotoflächen, Fokus als gefüllte Pille.
- Musterscreens: Start kinoschwarz mit randlosem Bild und einer Umriss-Pille, Bibliothek hell-creme mit Pistazien-Band und Kartenzeilen, Album „Lissabon“ wieder kinoschwarz mit randlosem Raster.

## Vermeiden
- Dritte Grundfläche (Grau, Beige, Blau) oder beide Spuren auf einem Screen mischen.
- Eckige oder abgerundete Rechteck-Knöpfe; Pillen sind nicht verhandelbar.
- Titel ab Gewicht 400 aufwärts, Titel unter 36 px auf Bühnenflächen.
- Mint oder Pistazie auf der dunklen Spur, Grün als Textfarbe, Grün hinter weißer Schrift.
- Scrim, Verlauf oder Text auf Fotos; Schlagschatten auf dunklen Karten.
