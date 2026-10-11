---
slug: lovable
marke: Lovable
website: https://lovable.dev
ansatz: minimal
ansatz2: editorial
modus: hell
aufbau: Warme Pergament-Fläche ohne Schatten; Inhalte liegen in 1-px-umrandeten Karten, getrennt durch viel Luft
navigation: Untere Leiste auf Creme; aktives Ziel wird zur dunklen Pille mit Icon + Label, inaktiv nur Icon
komponenten: Großes Eingabefeld mit Vorschlags-Pillen, bordierte Galerie-Karten, Pillen-Icon-Knöpfe, Zahlenleiste
icons: Phosphor Regular, runde Enden, 20–22 px, Strich in Kohle 82 %, nie gefüllt (Empfehlung)
bewegung: Weich und kurz: 150/260 ms, cubic-bezier(.32,.72,0,1); Druck = Deckkraft 0,8; Fokus = weicher Schatten
schrift: Humanistische Grotesk, nur 400 und 600, Titel eng gesperrt (−0,9 bis −1,5 px), Links unterstrichen
---
# Lovable – Designsprache

**Kurz:** Wärme durch Zurückhaltung: alles steht auf einem cremefarbenen Papierton, nicht auf Weiß. Begrenzt wird mit 1-px-Linien statt mit Schatten, alle Grautöne entstehen aus einem einzigen Kohleton bei verschiedenen Deckkräften. Der einzige Schatten im System ist die Inset-Kante auf dunklen Knöpfen – sie wirken eingedrückt, nicht schwebend. Eingestiegen wird über ein großes, einladendes Eingabefeld mit Vorschlags-Pillen.

## Wirkung
- Charakter: warm, analog, ruhig, handgemacht; wie ein gut gebundenes Notizbuch, nicht wie ein Tech-Dashboard.
- Passt zu: kreativen Werkzeugen, Sammlungs- und Lese-Apps, Tagebuch, Rezepte, Galerien, ruhigen KI-Assistenten.
- Passt weniger zu: datendichten Admin-Oberflächen, Sport- und Gaming-Apps, allem mit Neon oder harten Kontrasten.

## Aufbau und Raster
- Seitenaufbau: zentrierte Einzelspalte mit üppigem vertikalem Rhythmus; auf der Website 80–208 px zwischen Abschnitten, in der App 32–40 px.
- Ausrichtung: Kopfbereich zentriert oder linksbündig, Inhalte linksbündig; Zahlenleiste waagerecht mit gleichen Spalten.
- Raster: 8-px-Basis (8/10/12/16/24/32/40/56/80 px), Inhalt max. 1200 px, Kartenraster 3- → 2- → 1-spaltig, in der App 2-spaltig mit 12 px Fuge.
- Dichte und Weißraum: innen eng (12–24 px), außen weit – der Kontrast aus dichtem Karteninneren und großen Abschnittslücken ist der Leserhythmus.
- Rhythmus: Titel → Eingabefeld/Karte → 32 px → nächster Abschnitt; keine Trennlinien zwischen Abschnitten, nur Luft.

## Navigation
- Website: feste, schlichte Kopfleiste auf Creme, Wortmarke links, Links 14–16 px/400 in Kohle, rechts ein dunkler Knopf mit Inset-Schatten; ab 768 px Hamburger mit 6-px-Radius.
- App (Empfehlung): untere Leiste auf Creme, 1 px `#eceae4` oben, 4 Ziele Start · Bibliothek · Suche · Profil. Inaktiv nur Icon 22 px in `rgba(28,28,28,.4)`; aktiv wird das Ziel zur Pille (9999 px) in `#1c1c1c` mit Icon und Label in `#fcfbf8` und dem Inset-Schatten – Form und Fläche tragen den Zustand, nicht die Farbe.
- Detail: runder Pillen-Knopf mit Pfeil links oben, rechts drei Pillen-Icon-Knöpfe; die untere Leiste entfällt zugunsten einer Musikzeile.
- TV: linke Spalte mit Pillen-Einträgen; Fokus = Pille füllt sich in Kohle plus weicher Schatten `rgba(0,0,0,.1) 0 4px 12px`, keine Vergrößerung.

## Startscreen
- Begrüßung als Display 40 px/600, Laufweite −1,2 px, direkt auf Creme – ohne Kopfkarte.
- Darunter das Signaturfeld: ein großes Eingabefeld (Radius 16 px, 1 px `#eceae4`), Platzhalter in `#5f5f5d`, in der Fußzeile zwei Pillen-Icon-Knöpfe und eine dunkle Pille als Absenden.
- Vorschlags-Pillen in einer Reihe darunter (1 px `#eceae4`, 14 px/400), danach die hervorgehobene Karte „Vor einem Jahr“ mit bordiertem Bild und dunklem Knopf, zum Schluss die Zahlenleiste (28–36 px/600 über 13-px-Labels).

## Komponenten
- Buttons: primär `#1c1c1c` auf `#fcfbf8`-Text, 8×16 px, Radius 6 px, mit Inset-Schatten `rgba(255,255,255,.2) 0 .5px 0 inset, rgba(0,0,0,.2) 0 0 0 .5px inset, rgba(0,0,0,.05) 0 1px 2px`; Ghost: transparent mit 1 px `rgba(28,28,28,.4)`; Creme-Knopf ohne Rahmen für Nebensächliches; Druck überall Deckkraft 0,8.
- Karten und Kacheln: Fläche wie die Seite (`#f7f4ed`), 1 px `#eceae4`, Radius 12 px (16 px hervorgehoben, 8 px kompakt), kein Schatten. Bilder innen mit eigenem 1-px-Rahmen und 12 px Radius.
- Listen: als Galerie gedacht – zweispaltige Karten mit Bild, Titel 17–20 px/400 und Angabe 13–14 px in `#5f5f5d`; einspaltige Zeilen nur mit 1-px-Trenner, nie mit Flächenwechsel.
- Suche und Eingabefelder: Creme-Fläche, 1 px `#eceae4`, Radius 6–16 px, Platzhalter `#5f5f5d`; Fokus = weicher Schatten `rgba(0,0,0,.1) 0 4px 12px`, kein harter Ring.
- Chips, Tabs, Filter: Pillen (9999 px) mit 1 px `#eceae4`, 14 px/400; aktiv = Kohle-Füllung, Text `#fcfbf8`, Inset-Schatten. Tabs im Detail stattdessen als unterstrichene Textlinks.
- Dialoge und Sheets: Creme-Fläche, Radius 16 px, 1 px `#eceae4`, Schleier `rgba(28,28,28,.4)`; kein Schlagschatten.
- Signatur-Komponenten: Eingabefeld mit Pillen-Fußzeile; Vorschlags-Pillen; Galerie-Karte; Zahlenleiste; die aktive Navigations-Pille.

## Icons
- Stil: weiche Linien-Icons mit runden Enden (Phosphor Regular) – passend zur humanistischen Schrift; nie gefüllt, nie zweifarbig (Empfehlung).
- Größe und Strich: 22 px in der Leiste, 20 px in Pillen-Knöpfen, 16–18 px inline; Strich ≈1,8 px, Farbe `rgba(28,28,28,.82)`, inaktiv `rgba(28,28,28,.4)`.
- Einsatz: nur dort, wo eine Handlung dahinter steht; Icon-Knöpfe sind immer runde Pillen mit 36–40 px Durchmesser.
- Umsetzung: Compose `Icons.Rounded` bzw. Material Symbols Rounded, Gewicht 300, Füllung 0; iOS SF Symbols Regular; Web Phosphor Regular oder Lucide mit `stroke-linecap: round`.

## Bildsprache
- Bilder sind gerahmte Abbildungen, nie randlos: immer 1 px `#eceae4` und 12 px Radius, mit Creme-Rand ringsum.
- Seitenverhältnis 16:9 oder 4:3 in Karten, 1:1 im Fotoraster; Raster dreispaltig mit 10 px Fuge und 8 px Radius.
- Keine dunklen Verläufe über Bildern, keine Text-auf-Bild-Overlays – Titel stehen darunter auf Creme.
- Sehr dezenter warmer Mehrfarbverlauf (Rosa/Orange/Blau bei geringer Deckkraft) hinter dem Kopfbereich ist erlaubt; sonst keine Dekoration.

## Typografie-Stimme
- Humanistische Grotesk mit runden Enden, nur zwei Gewichte: 400 für alles, 600 für Überschriften – nie 700.
- Größen 40/36/28/20/17/16/14/13 px; Laufweite −1,5 px bei 60 px, −1,2 px bei 48 px, −0,9 px bei 36 px, normal ab 20 px. Zeilenhöhe 1,0–1,1 im Display, 1,5 im Text.
- Links in Textfarbe mit Unterstrich – der Unterstrich trägt den Hinweis, nicht die Farbe. Keine Versalien, keine Sperrung nach oben.
- Freier Ersatz: Camera Plain Variable ist proprietär; frei am nächsten kommen Figtree, Nunito Sans oder Carlito (hier gerendert: Carlito; da nur 400/700 vorliegen, stehen Überschriften im nächstliegenden Bold – 600 bleibt der Sollwert).

## Form, Tiefe und Material
- Radien: 4 px Mikro, 6 px Knopf/Feld/Menü, 8 px kompakte Karte, 12 px Karte und Bild, 16 px großer Container, 9999 px nur für Pillen und Icon-Knöpfe.
- Linien und Rahmen: 1 px `#eceae4` passiv, 1 px `rgba(28,28,28,.4)` interaktiv – die beiden nie mischen.
- Schatten und Ebenen: flach. Stufe 0 Creme, Stufe 1 Rahmen, Stufe 2 Inset-Schatten auf dunklen Knöpfen, Stufe 3 weicher Fokusschatten. Keine Schlagschatten für Karten.
- Besondere Oberflächen: Papierwärme der Fläche selbst; Tönungen aus `rgba(28,28,28,.03)` und `.04` für Hover und Mikroflächen.

## Bewegung
- Laut Datei: Druck- und Aktiv-Zustand über Deckkraft 0,8; Fokus über weichen Schatten `rgba(0,0,0,.1) 0 4px 12px`. Keine Dauern genannt.
- Empfehlung: klein 150 ms / Screenwechsel 260 ms, Easing `cubic-bezier(.32, .72, 0, 1)`; Druck = Deckkraft 0,8 ohne Skalierung; Einblenden 10 px von unten mit 60 ms Staffel; Screenwechsel als sanftes Schieben; Fokus (TV) = Schatten wächst in 150 ms.
- Compose: `tween(260, easing = CubicBezierEasing(.32f, .72f, 0f, 1f))`, Druck über `animateFloatAsState` auf `alpha = .8f`, Listen mit `animateItem()`, Pillen-Wechsel in der Leiste als `AnimatedContent` mit Breitenanimation.

## Signatur-Elemente
1. Cremefarbene Papierfläche statt Weiß – auch in Karten, Feldern und Leisten.
2. Großes Eingabefeld mit Pillen-Fußzeile und Vorschlags-Pillen als Einstieg in die App.
3. Dunkler Knopf mit Inset-Kante: heller Lichtstrich oben, dunkler Ring außen – wirkt eingedrückt.
4. Begrenzung ausschließlich durch 1-px-Linien in `#eceae4`; nirgends ein Schlagschatten.
5. Aktive Navigations-Pille, die Icon und Label umschließt.

## Übertragung auf eine App
- Startscreen: Begrüßung, Eingabefeld mit Vorschlags-Pillen, hervorgehobene Karte „Vor einem Jahr“, Zahlenleiste; alles ohne Kopfbild.
- Liste und Übersicht: Suchfeld in derselben Bauart, Filter als Pillen, Inhalte als zweispaltige Galerie-Karten mit gerahmtem Bild; keine dichten Tabellen.
- Detail: gerahmtes Bild mit Creme-Rand, Titel 36 px, Angaben in `#5f5f5d`, dunkler Hauptknopf plus Ghost-Knopf, Umschalter als unterstrichene Textlinks, Fotoraster, unten eine Musikzeile mit Pillen-Knopf.
- Formulare und Einstellungen: Felder mit 1-px-Rahmen und 6 px Radius, Label darüber in 14 px, Hilfetext in `#5f5f5d`, Schalter als Pillen; Speichern als dunkler Knopf unten.
- Leere Zustände und Laden: bordierte Karte mit einem Satz in 17 px/400 und einem Ghost-Knopf; Laden als Creme-Flächen mit 1-px-Rahmen, die sanft die Deckkraft wechseln – kein Spinner.
- TV: zweispaltig mit großen bordierten Karten; Fokus über Pillenfüllung und weichen Schatten.
- Musterscreens: Start mit Eingabefeld, Vorschlags-Pillen, Rückblick-Karte und Zahlenleiste; Bibliothek als zweispaltige Galerie mit Pillen-Filtern; Detail mit gerahmtem Bild, unterstrichenen Umschaltern und Musikzeile.

## Abgrenzung zu Expo
Beide sind Werkzeuge zum App-Bauen, doch Lovable ist das Gegenteil von Expos weißer Entwickleroberfläche: Pergament statt Reinweiß, Pillen statt 8-px-Rechtecke, Galerie-Karten statt Haarlinien-Tabelle, ein einladendes Eingabefeld statt Mono-Zahlen auf dunklem Panel, Unterstrich statt Versal-Label – und kein einziges dunkles Codefenster.

## Vermeiden
- Kein reines Weiß als Fläche und keine kalten Grautöne – alle Grauwerte aus `#1c1c1c` mit Deckkraft ableiten.
- Keine Schlagschatten an Karten; Begrenzung ist Aufgabe der 1-px-Linie.
- Kein Gewicht 700, keine gesperrten Versalien, keine zweite, gesättigte Akzentfarbe.
- Pillen-Radius nicht auf rechteckige Knöpfe legen – Pillen sind Icon- und Umschalt-Knöpfen vorbehalten.
- Keine harten Fokus-Ringe; Fokus ist ein weicher, diffuser Schatten.
- Den Inset-Schatten am dunklen Knopf nicht weglassen – ohne ihn wirkt der Knopf fremd.
