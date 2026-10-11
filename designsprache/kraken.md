---
slug: kraken
marke: Kraken
website: https://www.kraken.com
ansatz: daten
ansatz2: werkzeug
modus: hell
aufbau: Durchgehend Weiß; Inhalte liegen als einzeln abgesetzte Karten mit 12 px Radius und Flüster-Schatten darauf
navigation: Unten weiße Leiste mit 1-px-Linie, 4 Ziele; aktives Icon auf einer 12-px-Kachel in Lila-Tönung 16 %
komponenten: Kennzahlen-Karte mit Balken, Karten-Zeile statt Listenzeile, Segment-Schalter, getönte Badges
icons: Phosphor Bold / kräftige Linien, 22–24 px, nie dünn; auf 12-px-Kachelknöpfen statt auf Kreisen
bewegung: knapp und sachlich; Empfehlung 150 ms klein / 250 ms Screen, cubic-bezier(.2,0,.2,1), Druck = Farbe + 0,98
schrift: Helvetica-Grotesk in nur zwei Gewichten: 700 für alles Benannte, 400 für Beiwerk; Titel 28–36 px, −0,5 bis −1 px
---
# Kraken – Designsprache

**Kurz:** Eine weiße, kompakte Börsen-Oberfläche, in der Lila (#7132f5) nicht sparsam, sondern als Arbeitsfarbe auftritt – als Button, als 16 % getönte Fläche, als Balken. Alles Bedienbare hat 12 px Radius; Pillen sind ausdrücklich verboten. Tiefe entsteht nur durch Flüster-Schatten (`rgba(0,0,0,.03) 0 4px 24px`), nie durch dunkle Flächen. Die Typografie kennt faktisch zwei Gewichte: fett (700) für alles Benannte, normal für alles Erklärende.

**Unterschied zu Coinbase** (beide Krypto-Börsen): Kraken bleibt durchgehend weiß und gliedert mit abgesetzten, weich schattierten Karten; Coinbase bleibt flach mit Haarlinien und bringt pro Screen ein tiefschwarzes Band. Kraken ist eckiger (12 px, nie Pille), fetter (700 statt 400) und farbiger (Lila als Fläche, grüne Tönungs-Badges); Coinbase ist runder (Pillen, Kreise), leichter und fast monochrom. In Graustufen erkennt man Kraken an den schwebenden Kartenzeilen und quadratischen Bildern, Coinbase an schwarzem Band und Kreisbildern.

## Wirkung
- Charakter: sachlich, zupackend, professionell; mehr Werkzeug als Magazin, aber freundlicher als eine reine Tabelle.
- Passt zu: Finanz- und Handels-Apps, Verwaltungs- und Konto-Apps, Dashboards, allem mit Zuständen, Werten und Fortschritt.
- Passt weniger zu: bildlastigen Erzähl-Apps, verspielten Produkten, dunklen Medien-Oberflächen (die Datei kennt keinen Dark Mode).

## Aufbau und Raster
- Seitenaufbau: weißer Kopf mit fettem Titel → eine Kennzahlen-Karte als Ankerblock → darunter Abschnitte aus einzeln abgesetzten Karten; keine durchlaufenden Haarlinien-Tabellen.
- Ausrichtung: linksbündig; Werte und Badges rechts in der Zeile.
- Raster: feine Abstandsleiter 1/2/3/4/5/6/8/10/12/13/15/16/20/24/25 px (laut Datei) – daraus in der App 16 px Seitenrand, 12 px Innenabstand, 8 px zwischen Karten, 24 px zwischen Abschnitten.
- Dichte und Weißraum: dichter als übliche Marketing-Seiten; Kartenzeile 72 px hoch, Button-Padding 13×16 px, Abschnittsabstand 24 px.
- Rhythmus: Karte – Luft – Karte; jeder Block ist ein eigenes, klar begrenztes Rechteck.

## Navigation
- Website: weiße Kopfleiste, Zeichen links, Textlinks mittig, rechts ein lila Primärbutton und ein umrandeter Zweitbutton (beide 12 px Radius). Breakpoints 375/425/640/768/1024/1280/1536 px.
- App (Empfehlung): weiße Leiste unten, 1 px #dedee5 oben, Höhe 72 px, 4 Ziele (Start, Bibliothek, Suche, Profil). Icon 24 px Phosphor Bold, Label 11/700; aktiv liegt das Icon auf einer 12-px-Kachel in `rgba(133,91,251,.16)` und wird lila, das Label wird schwarz – Form plus Fläche, nicht nur Farbe. Leiste bleibt beim Scrollen stehen; Detailscreens verzichten auf sie und führen über einen Kachel-Zurückknopf oben links zurück.
- TV (Empfehlung): Zielspalte links als 12-px-Kacheln, aktive Kachel in Lila-Tönung mit lila 2-px-Rahmen.

## Startscreen
- Fetter Begrüßungstitel 28/700 mit −0,5 px, keine große Bühne, kein Bild im Kopf.
- Direkt darunter die Kennzahlen-Karte: große Zahl 32/700, Vergleichswert daneben in #9497a9, grünes Tönungs-Badge rechts, darunter ein 6 px hoher Lila-Balken und eine Fußzeile aus drei Quellen mit senkrechten Trennern.
- Danach ein hervorgehobener Inhalt als Karten-Zeile mit Bild links und umrandetem Lila-Button rechts, anschließend eine Folge gleichartiger Karten-Zeilen.

## Komponenten
- Buttons: Primär Lila #7132f5, Text weiß 16/600, Padding 13×16, Radius 12. Outline weiß mit 1 px #5741d8 und Text #5741d8, Radius 12. Subtil `rgba(133,91,251,.16)` mit lila Text, Padding 8, Radius 12. Weiß mit Flüster-Schatten, Radius 10. Sekundär grau `rgba(148,151,169,.08)`, Text #101114, Radius 12. **Nie Pille** – 12 px ist das Maximum.
- Karten und Kacheln: weiß, Radius 12, 1 px #dedee5 oder ganz ohne Rand, Schatten `rgba(0,0,0,.03) 0 4px 24px`; Innenabstand 12–16 px. Bilder darin quadratisch mit 10 px Radius.
- Listen: keine Haarlinien-Liste, sondern gestapelte Karten-Zeilen mit 8 px Abstand – Bild 56 px (Radius 10), Titel 16/700, Unterzeile 14/400 #9497a9, rechts Wert 15/700 über Einheit 13/400 oder ein neutrales Badge.
- Suche und Eingabefelder: weißes Feld, Höhe 48, Radius 12, 1 px #dedee5, Flüster-Schatten, Lupe 20 px #9497a9, Text 16/400; Fokus 1 px → #5741d8 plus 3 px Lila-Tönung außen (Empfehlung).
- Chips, Tabs, Filter: Chip 12 px Radius, inaktiv `rgba(148,151,169,.08)` mit #101114 in 400, aktiv `rgba(133,91,251,.16)` mit #7132f5 in 700. Segment-Schalter: Spur `rgba(148,151,169,.08)` Radius 12 mit 3 px Innenabstand, aktives Segment weiß, Radius 10, Flüster-Schatten, Text 700.
- Dialoge und Sheets (Empfehlung): weißes Blatt mit 16 px oberen Ecken, Scrim Schwarz 40 %, Flüster-Schatten statt Rand.
- Signatur-Komponenten: Kennzahlen-Karte mit Balken; Badges mit **kleinerem** Radius als Buttons (Erfolg 6 px in `rgba(20,158,97,.16)` mit #026b3f, neutral 8 px in `rgba(104,107,130,.12)` mit #484b5e); Segment-Schalter; Kachel-Icon-Knöpfe.

## Icons
- Stil: kräftige, geometrische Linien ohne dünne Stellen – Phosphor Bold oder Material Symbols Rounded mit Gewicht 500; gefüllte Icons nur, wo ein Zustand markiert wird (Favorit).
- Größe und Strich: 24 px in Navigation und Kachelknöpfen, 20 px in Feldern und Zeilen, 16 px in Buttons; optische Strichstärke ~2 px.
- Einsatz: Icons sitzen auf 12-px-Kacheln (36–48 px, Fläche `rgba(148,151,169,.08)`), nie auf Kreisen; Farbe #101114, sekundär #9497a9, lila nur zusammen mit einer lila Fläche.
- Umsetzung: Compose `Icons.Rounded` bzw. Material Symbols Rounded (Gewicht 500, Füllung 0; Favorit Füllung 1); iOS SF Symbols Semibold; Web Phosphor Bold oder Lucide stroke 2.25.

## Bildsprache
- Bilder sind Beleg, nicht Bühne: immer rechteckig mit 10 px Radius, in der Zeile 56 px quadratisch, im Detail als eingerückte Platte (16 px Rand ringsum, Radius 12, Flüster-Schatten) – nie randlos über die ganze Breite.
- Keine Verläufe, keine Körnung, kein Text auf dem Bild; nur ein neutrales Badge mit 8 px Radius darf aufliegen.
- Raster-Ausschnitte mit 8 px Radius und 6 px Abstand; die eckigere Bildbehandlung ist das Gegenstück zu den runden Bildkreisen anderer Finanzmarken.

## Typografie-Stimme
- Zwei Familien laut Datei: Kraken-Brand (Display, 700) und Kraken-Product (UI). Praktisch zwei Gewichte: 700 für Titel, Zeilennamen, Werte, aktive Labels; 400 für Unterzeilen und Fließtext.
- Skala: Hero 48/700/1,17/−1 px · Abschnitt 36/700/−0,5 · Unterüberschrift 28/700/−0,5 · Feature-Titel 22/600 · Text 16/400/1,38 · Button 16/500–600 · Caption 14 · Klein 12 · Mikro 7/500 Versalien (laut Datei; in der App auf 9–10 px angehoben, Empfehlung).
- Negative Laufweite nur ab 28 px; Versalien nur für Mikro-Labels; Zahlen in derselben Schrift, aber in 700 – keine eigene Mono.
- Freier Ersatz: Helvetica-Grotesk (TeX Gyre Heros/Arimo) für UI laut Fallback-Kette; für Display IBM Plex Sans Bold (laut Datei) oder Inter Display 700 (Empfehlung).

## Form, Tiefe und Material
- Radien: 3 / 6 (Erfolgs-Badge) / 8 (neutrales Badge, Bildausschnitt) / 10 (weiße Knöpfe, Bild in der Zeile, aktives Segment) / 12 (Buttons, Karten, Felder, Chips) / 16 (Blätter) / 9999 und 50 % nur für Avatare. Buttons nie als Pille.
- Linien und Rahmen: 1 px #dedee5 als Kartenrand und Trenner, #686b82 bei 24 % für feine Ränder; Outline-Button 1 px #5741d8.
- Schatten und Ebenen: zwei sehr leise Stufen – `rgba(0,0,0,.03) 0 4px 24px` für Karten und Felder, `rgba(16,24,40,.04) 0 1px 4px` für Mikro-Elemente. Nie dunkel, nie hart.
- Besondere Oberflächen: getönte Flächen statt Farbflächen – Lila 16 %, Grün 16 %, Grau 8–12 %; dadurch bleibt Weiß die Grundfläche und die Tönung trägt die Bedeutung.

## Bewegung
- Laut Datei: keine Angaben (keine Animations- oder Übergangswerte dokumentiert).
- Empfehlung: klein 150 ms / Screenwechsel 250 ms, Easing `cubic-bezier(0.2, 0, 0.2, 1)`; Druck = dunklere Lila-Stufe (#5741d8) plus 0,98-Skalierung; Karten blenden mit 4 px von unten ein, 25 ms gestaffelt; Segment-Schalter lässt die weiße Fläche gleiten statt zu springen; Balken wächst einmalig von 0 in 400 ms; Fokus (TV) Lila-Tönung plus 2-px-Rahmen in 150 ms.
- Compose: `tween(150, easing = CubicBezierEasing(0.2f, 0f, 0.2f, 1f))`, Druck `animateFloatAsState(0.98f)`, `AnimatedVisibility(fadeIn() + slideInVertically { it / 16 })`, Segment per `animateDpAsState` der Indikator-Position.

## Signatur-Elemente
1. 12 px überall – Buttons, Karten, Felder, Chips, Icon-Kacheln; keine einzige Pille.
2. Getönte Flächen: Lila 16 % für Aktives, Grün 16 % für Positives, Grau 8 % für Ruhiges.
3. Einzeln abgesetzte Karten-Zeilen mit Flüster-Schatten statt einer durchlaufenden Liste.
4. Kennzahlen-Karte: große 700er-Zahl, Vergleichswert daneben, Lila-Balken darunter, Quellen-Fußzeile mit senkrechten Trennern.
5. Zwei Gewichte, harter Kontrast: fett benannt, normal erklärt – Badges mit kleinerem Radius als Buttons.

## Übertragung auf eine App
- Startscreen: fette Begrüßung, Kennzahlen-Karte (Speicher, Balken, Quellen), eine hervorgehobene Karten-Zeile mit Outline-Button, dann gleichartige Karten-Zeilen.
- Liste und Übersicht: Suchfeld mit 12 px Radius, Chips in Tönung (aktiv lila), eine Sortierzeile mit Anzahl links und grauem Chip rechts, darunter gestapelte Karten-Zeilen mit quadratischem Bild, Wert und Badge.
- Detail: eingerückte Bildplatte statt Vollbild, fetter Titel mit Badge, breiter Lila-Button plus Kachel-Icon-Knöpfe, Segment-Schalter für Fotos/Videos/Orte, enges Raster, abschließende Karte für die Musik.
- Formulare und Einstellungen: Karten-Gruppen statt durchlaufender Liste; Felder 48 px/12 px Radius, Schalter und Werte rechts, Primärbutton unten voll breit in Lila.
- Leere Zustände und Laden: zentriert in einer weißen Karte, Titel 22/600, Satz 16/400 #9497a9, Outline-Button; Laden als graue 12-px-Blöcke in `rgba(148,151,169,.08)` ohne Pulsieren.
- TV: weiße Fläche beibehalten, Karten auf 16 px Radius vergrößern, Fokus als Lila-Tönung plus 2-px-Rahmen.
- Musterscreens: Start mit fetter Begrüßung, Speicher-Karte mit Balken und Quellen-Fußzeile, Rückblick-Zeile und Karten-Liste; Bibliothek mit 12-px-Suchfeld, Tönungs-Chips, Sortierzeile und schwebenden Karten-Zeilen; Detail mit eingerückter Bildplatte, Lila-Button, Kachel-Knöpfen, Segment-Schalter und engem Raster.

## Vermeiden
- Pillen-Buttons und Radien über 12 px an Bedienelementen; harte 0-px-Ecken ebenso.
- Andere Lilatöne als #7132f5 / #5741d8 / #5b1ecf oder eine zweite Akzentfarbe neben Grün.
- Kräftige Schatten, dunkle Flächen, Verläufe oder Glas – die Tiefe bleibt auf Flüster-Niveau.
- Dünne Icon-Striche und leichte Überschriften; die Marke lebt vom fetten 700er-Kontrast.
- Volle Farbflächen statt Tönungen für Badges und aktive Zustände.
