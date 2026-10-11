---
slug: slack
marke: Slack
website: https://slack.com
ansatz: galerie
ansatz2: daten
modus: hell
aufbau: Helle Karten auf Creme-Lavendel-Verlaufsfeldern; Inhalt schwebt über dem Verlauf, Abschluss als Aubergine-Band
navigation: Unten Pillen-Leiste, 4 Ziele; aktiv als gefüllte Aubergine-Pille mit Icon und Text, inaktiv nur Icon
komponenten: Pillen-Buttons (90px, 14×28px), Karten 16px, Kennzahl-Karten mit 40px Aubergine-Zahl, Versal-Pillen, Aubergine-Band
icons: Phosphor humanistisch, 22px, Linie; nur in der aktiven Pille gefüllt (Empfehlung – Datei nennt keinen Satz)
bewegung: Weich und freundlich, 180ms klein / 320ms Screen, cubic-bezier(.2,.8,.2,1), Pille staucht leicht, Verlauf blendet auf
schrift: Zwei Schnitte einer humanistischen Sans; Display 700 mit -0,26 bis -0,77px, Body 400/1,55, Versal-Eyebrow 12px/0,96px
---
# Slack – Designsprache

**Kurz:** Ein einziges tiefes Aubergine `#4a154b` trägt die ganze Marke – als Knopf, als Karte, als Abschlussband. Darum herum liegt eine weiche Welt aus Creme und Lavendel mit diffusen Pastell-Verläufen, über denen Inhalte zu schweben scheinen. Jeder Knopf ist eine großzügig gepolsterte Pille; Tiefe entsteht aus dem Verlauf, nicht aus Schatten.

## Wirkung
- Charakter: warm, professionell, freundlich; großzügig gepolstert statt kompakt, ruhig statt laut.
- Passt zu: Produktivität und Zusammenarbeit, Medien- und Bibliotheks-Apps, Onboarding, Preis- und Marketingflächen, allem mit viel Text.
- Passt weniger zu: nächtliche Kino-Erlebnisse, datendichte Werkzeuge mit vielen Zeilen, harte, technische oder aggressive Produkte.

## Aufbau und Raster
- Seitenaufbau: Verlaufsband oben (Creme/Lavendel mit Pastell-Mesh), darauf schwebender Inhalt; darunter weiße Abschnitte mit Karten; am Ende ein vollflächiges Aubergine-Band mit der Schlussaktion.
- Ausrichtung: links; Kennzahl-Karten zentriert.
- Raster: Web ~1240px Container, Verlauf läuft darüber hinaus; Preis-/Kartenraster 4 → 2 → 1; Kennzahlen 3-spaltig. App: eine Spalte, Seitenrand 16–20px, Kennzahlen 3-spaltig.
- Dichte und Weißraum: Leiter 4 · 8 · 12 · 16 · 20 · 24 · 28px. Abschnitt Web 64–96px (transaktional 48px); App 24px zwischen Abschnitten, 16px in Karten, Karteninnenraum 32px (Web) bzw. 16px (App).
- Rhythmus: Verlaufsband → Karten → Kennzahlen → Aubergine-Band. Nie zwei gefüllte Aubergine-Flächen im selben Blickfeld.

## Navigation
- Website: helle Kopfleiste auf Weiß, Wortmarke links, Menü mittig, rechts zwei Pillen (Lavendel sekundär, Aubergine primär); unter 768px Hamburger.
- App: untere Leiste auf Weiß mit 1px `#e6e6e6` Oberkante, 4 Ziele (Start · Bibliothek · Suche · Profil), Höhe 88px. Das aktive Ziel ist eine **gefüllte Aubergine-Pille** (Radius 90px, 10×18px) mit gefülltem Icon und Beschriftung nebeneinander; inaktive Ziele zeigen nur ein Linien-Icon in `#696969`. Aktiv unterscheidet sich also durch Form, Füllung und Beschriftung, nicht nur durch Farbe. Leiste bleibt beim Scrollen stehen.
- TV: Ziele als Pillenreihe oben; Fokus als gefüllte Aubergine-Pille plus 2px Rand `#592466`, keine Vergrößerung nötig.

## Startscreen
- Verlaufsband über dem oberen Drittel (Creme-Basis mit Pastell-Mesh aus Pfirsich, Lavendel und staubigem Grün), darin Begrüßung als Display 32px/700/-0,26px.
- Darüber schwebend der hervorgehobene Inhalt: Bild mit 12px Radius ohne Rahmen und ohne Schatten (der Verlauf trägt), darunter Titel 22px/600, Angaben 14px `#696969`, Versal-Eyebrow-Pille in Creme darüber.
- Aktionen als Pillenpaar: Aubergine gefüllt plus Lavendel sekundär – nebeneinander, nie gestapelt.
- Darunter auf Weiß drei Kennzahl-Karten (16px Radius, 1px `#e6e6e6`) mit großer Aubergine-Zahl, dann ein Abschnitt mit Bildkarten und einem blauen Textlink `#1264a3` rechts im Abschnittskopf.

## Komponenten
- Buttons: ausnahmslos Pillen (Radius 90px). Primär Aubergine `#4a154b`, Text weiß, 16px/700/0,2px, Polsterung 14×28px, Druck `#611f69`. Sekundär Lavendel `#f9f0ff` mit Text `#1d1d1d`, Polsterung 10×30px. Kontur: 2px Aubergine auf Weiß bzw. 2px Weiß auf Aubergine. Polsterung nie unter 14×28px – die Überpolsterung ist Teil der Marke.
- Karten und Kacheln: Radius 16px, Weiß mit 1px `#e6e6e6`, Innenraum 16–32px; Creme-Karte `#f4ede4` für Erklärungen; Aubergine-Karte für die hervorgehobene Stufe und das Schlussband; Bilder darin randlos mit 8–12px Radius.
- Listen: Einträge sind Karten, keine Zeilen – Miniatur 56px mit 8px Radius links, Titel 18px/600, Angaben 14px `#696969`, rechts eine Versal-Pille mit der Art; 10px Abstand zwischen den Karten, keine Trennlinien.
- Suche und Eingabefelder: Weiß, Radius **4px** (bewusster Gegensatz zu den Pillen), 1px `#e6e6e6`, Polsterung 10×12px, Höhe 44px, Text 16px.
- Chips, Tabs, Filter: Pillen. Aktiv Aubergine gefüllt mit weißem Text, inaktiv Weiß mit 1px `#e6e6e6` bzw. Lavendel; Versal-Eyebrow-Pille in Creme mit 12px/700/0,96px für Rubriken.
- Dialoge und Sheets: Weiß, Radius 16px oben, Schatten `rgba(0,0,0,.1) 0 0 32px`, Griff als 4px-Pille; Aktionen als Pillenpaar unten.
- Signatur-Komponenten: Pastell-Mesh-Verlauf als Hintergrund, schwebender Inhalt ohne Schatten darüber, Kennzahl-Karte mit 40–50px Aubergine-Zahl, Creme-Versal-Pille als Rubrik, vollflächiges Aubergine-Schlussband, blaue Inline-Links.

## Icons
- Stil: humanistische Linie mit offenen Formen und runden Enden, gleiche Weichheit wie die Pillen; gefüllt nur im aktiven Zustand.
- Größe und Strich: 22px in der Navigation, 20px in Karten, 18px in Pillen; Strich ca. 1,75px (Empfehlung – die Datei nennt keinen Icon-Satz; abgeleitet aus Pillengeometrie und 700er Buttons).
- Einsatz: sparsam, immer neben Text; Icons in `#696969` auf Hell, weiß in der Aubergine-Pille. Nie Aubergine als Icon-Farbe auf Weiß (Aubergine ist Fläche, nicht Textfarbe).
- Umsetzung: Compose `Icons.Rounded` bzw. Material Symbols Rounded, Gewicht 400, Füllung 0 (aktiv 1); iOS SF Symbols `.regular`, aktiv `.fill`; Web Phosphor `regular` (aktiv `fill`) oder Lucide `stroke-width: 1.75`.

## Bildsprache
- Bilder sind Karten, nie Vollbild: Radius 12px im Hero, 8px im Raster, 8px bei Miniaturen; immer mit Rand zum Bildschirm (16–20px).
- Kein Schatten unter dem Bild – der Pastell-Verlauf dahinter übernimmt das Anheben.
- Farben bleiben unangetastet (keine Tönung, kein Duplex); die Wärme kommt vom Creme-Untergrund.
- Raster mit 8px Fugen, Seitenverhältnis 1:1 oder 4:3; Personen als runder Avatar 32–36px.

## Typografie-Stimme
- Zwei Schnitte: Display (700/600) für Überschriften, UI-Schnitt (400/700) für Text und Buttons – der Unterschied ist Teil der Stimme.
- Größen 64 / 58 / 50 / 32 / 24 / 22 / 18px Display gegen 16px Body; in der App 32 / 22 / 18 / 16 / 14 / 12px.
- Negative Laufweite im Display (-0,768px bei 64px, -0,256px bei 32px); Body 16px/1,55 und damit bewusst ruhig; Eyebrow 12px/700 Versal mit +0,96px.
- Zahlen in Kennzahl-Karten: 40–50px/700 in Aubergine – Betonung allein über Größe.
- Freier Ersatz: Inter für beide Ebenen (so in der Datei empfohlen); Lato als weichere humanistische Alternative im Fließtext.

## Form, Tiefe und Material
- Radien: 90px alle Buttons und Chips; 16px Karten; 12px große Bilder; 8px kleine Bilder und kompakte Flächen; 4px Eingabefelder; 2px nur Mikro-Tags.
- Linien und Rahmen: 1px `#e6e6e6` an Karten und Feldern; 2px Aubergine bei Kontur-Pillen; keine Trennlinien in Listen (Abstand statt Linie).
- Schatten und Ebenen: sehr sparsam – `rgba(0,0,0,.1) 0 5px 20px` für schwebende Buttons, `rgba(0,0,0,.1) 0 0 32px` für große Komposite, `rgb(97,31,105) 0 0 0 1px inset` als Fokus. Inhalte über dem Verlauf bekommen **keinen** Schatten.
- Besondere Oberflächen: Pastell-Mesh als gestapelte `radial-gradient` (Pfirsich `#fff0e6`, Lavendel `#e9d8ff`, staubiges Grün `#e6f0e4`) auf Creme `#f4ede4`; Aubergine-Band als vollflächiger Abschluss.

## Bewegung
- Laut Datei: keine Angaben (nur Druck- und Hover-Zustände als Farbwechsel, Links mit Unterstreichung).
- Empfehlung: Dauer klein 180ms / Screenwechsel 320ms, Easing `cubic-bezier(.2, .8, .2, 1)` (weich auslaufend). Druck-Effekt: Pille auf `#611f69` und `scale(.98)`. Einblenden: Verlauf blendet auf (320ms), Karten steigen 12px gestaffelt um 50ms. Screenwechsel: sanftes Gleiten mit Überblenden. Fokus (TV): Pille füllt sich in 180ms.
- Compose: `tween(320, easing = CubicBezierEasing(.2f, .8f, .2f, 1f))`, `spring(dampingRatio = .8f)` für Druck, `AnimatedVisibility` mit `fadeIn() + slideInVertically()`, Liste `animateItem()`.

## Signatur-Elemente
1. Pastell-Mesh-Verlauf in Creme und Lavendel, über dem Inhalte ohne Schatten schweben.
2. Pillen überall – Buttons, Filter, Rubriken und sogar das aktive Navigationsziel.
3. Ein einziges tiefes Aubergine, das als Knopf, Kennzahl und Schlussband wiederkehrt.
4. Kennzahl-Karten mit sehr großer Aubergine-Zahl über einer kleinen Bildunterschrift.
5. Blaue Inline-Links als einzige zweite Farbe im Text.

## Übertragung auf eine App
- Startscreen: Verlaufsband mit Begrüßung und schwebendem Hervorhebungs-Bild, Pillenpaar als Aktionen, darunter drei Kennzahl-Karten und ein Abschnitt mit Bildkarten.
- Liste und Übersicht: Suchfeld mit 4px Radius, Pillen-Filter, danach Einträge als weiße Karten mit 16px Radius, Miniatur links und Art-Pille rechts; Abstand statt Trennlinien.
- Detail: Bild als große Karte mit 16px Radius auf dem Verlauf (nicht randlos), Versal-Pille als Rubrik, Titel, Pillenpaar, Pillen-Umschalter, Bildraster mit 8px Fugen und unten ein Aubergine-Band mit der Anschlussaktion.
- Formulare und Einstellungen: Felder 44px mit 4px Radius und 1px `#e6e6e6`, Beschriftung 14px darüber, Gruppen als weiße Karten mit 16px Radius, Hilfetext in `#696969`, Links blau.
- Leere Zustände und Laden: Creme-Karte mit kurzer Zeile in `#1d1d1d`, Hilfetext `#696969` und einer Aubergine-Pille; Ladeplatzhalter als `#f4ede4`-Flächen mit 8–16px Radius.
- TV: Pillenreihe oben, Karten im Raster mit 16px Radius, Fokus als gefüllte Aubergine-Pille bzw. 2px `#592466`-Rand.
- Musterscreens: Start mit Verlaufsband, schwebendem Rückblick-Bild, Pillenpaar und Kennzahl-Karten; Bibliothek mit Pillen-Filtern und Eintrags-Karten; Detail mit Bildkarte, Pillen-Umschalter, Fotoraster und Aubergine-Schlussband.

## Vermeiden
- Keine dritte Akzentfarbe – Aubergine plus blauer Link ist vollständig.
- Keine eckigen oder rechteckig gerundeten Buttons und keine knappe Polsterung unter 14×28px.
- Display nie mit Laufweite 0 setzen; Aubergine nie als Textfarbe im Fließtext.
- Bilder und Inhalte nicht in Rahmen oder Schatten sperren – sie liegen über dem Verlauf, nicht darin.
- Kein Hero ohne Pastell-Verlauf (nackte weiße Bühne wirkt markenfremd) und nie mehrere gefüllte Aubergine-Flächen gleichzeitig.
- Keine Trennlinien-Listen im Stil klassischer Einstellungen – die Marke trennt über Abstand und Kartenform.
