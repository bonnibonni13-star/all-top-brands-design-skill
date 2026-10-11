---
slug: intercom
marke: Intercom
website: https://www.intercom.com
ansatz: editorial
ansatz2: minimal
modus: hell
aufbau: Cremefarbene Grundfläche, darauf weiße Karten ohne Schatten; große ruhige Überschrift, Bild in gerahmter Kachel
navigation: Leiste unten in Creme mit Haarlinie, 4 Ziele, aktiv = weiße Pille mit Haarlinie („Anheben auf Weiß“)
komponenten: Kohle-Button 8 px, weiße Karten 12/16 px mit 1 px #d3cec6, Pill-Umschalter, Zeilen mit Haarlinien
icons: Empfehlung: feine Phosphor-Icons in Light, 18–22 px, kohlefarben; nie gefüllt, nie orange, nie unter 16 px
bewegung: Empfehlung: 160–240 ms, cubic-bezier(.3,0,0,1); Karte hebt sich auf Weiß, kein Skalieren, kein Schatten
schrift: Inter Display durchgehend: Display 500 mit −0,8 px, Text 400; Eyebrow 14 px 500 in Groß-/Kleinschreibung
---
# Intercom – Designsprache

**Kurz:** Eine warme Creme-Fläche (#f5f1ec) statt Weiß ist das Fundament; Hierarchie entsteht dadurch, dass sich weiße Karten ohne jeden Schatten von der Creme abheben. Die Schrift trägt alles: eine Familie, Gewicht 500 für große Titel mit deutlich negativer Laufweite, Gewicht 400 für Text, Zwischentitel in normaler Groß-/Kleinschreibung statt Versalien. Das einzige bunte Ereignis ist ein Orange (#ff5600), das ausschließlich einen Produktzustand markiert – nie eine Fläche und nie einen beliebigen Knopf.

**Widerspruch in der Datei:** Die Tokens führen `primary: #111111`, der Beschreibungstext nennt dagegen das Orange als Markenfarbe. Entscheidung nach Tokens und Komponenten-Abschnitt: **Kohle ist die Systemfarbe** (alle Haupt-Buttons), Orange bleibt ein Produkt-Akzent für genau einen Zustand.

## Wirkung
- Charakter: ruhig, redaktionell, erwachsen; wirkt wie ein gut gesetztes Produktmagazin, nicht wie bunte Software.
- Passt zu: Lese- und Dokumentationsapps, Produkt- und Hilfe-Apps, Medienbibliotheken mit ruhiger Anmutung, Preis- und Planseiten.
- Passt weniger zu: lauten Unterhaltungs-Apps, Gaming, Kinder-Apps, allem, was Signalfarben oder Verläufe braucht.
- Abgrenzung zu hellen Werkzeug-Marken: Die Fläche ist nie reines Weiß, die Haarlinien sind warm (#d3cec6 statt Neutralgrau), es gibt keine Schatten und keine Datentabellen – Inhalte stehen in Zeilen unter Haarlinien oder in einer weißen Karte.

## Aufbau und Raster
- Seitenaufbau: Creme-Kopfleiste → Eyebrow → großer Titel → kurze Zeile → gerahmte Bildkachel („Produkt-Mockup“) → Abschnitte, die entweder auf Creme liegen oder sich als weiße Karte abheben.
- Ausrichtung: linksbündig, eine Spalte; die Bildkachel läuft über die volle Inhaltsbreite und ist der Protagonist jedes Abschnitts.
- Raster: 8-px-Basis; Tokens 4·8·12·16·24·32·48·96 px. Web-Container ~1280 px, Karten 3-spaltig → 2 → 1 (1024/768 px).
- Dichte und Weißraum: Web-Abschnitte 96 px, Karten innen 24 px (Zitat/Hinweis 32 px, CTA-Banner 48 px). App (Empfehlung): Rand 20 px, Kartenabstand 10 px, Abschnitte 20–24 px, Zeilen 64–68 px.
- Rhythmus: Eyebrow 14 px 500 → Titel → Inhalt. Dieser Dreiklang wiederholt sich; Abstände oberhalb eines Eyebrows sind immer größer als darunter.

## Navigation
- Website: cremefarbene, klebende Kopfleiste 56 px, Wortmarke links, Links mittig, rechts Textlink plus Kohle-Button; unter 768 px Hamburger, Haupt-CTA bleibt sichtbar.
- App (Empfehlung, abgeleitet aus Kopfleiste und Pill-Umschalter): Leiste unten in Creme mit 1 px #d3cec6 oben, Höhe 78 px, 4 Ziele (Start, Bibliothek, Suche, Profil), Icon 21 px plus Beschriftung 11–12 px/500. Aktiv = weiße Pille (#ffffff, 1 px #d3cec6) – derselbe Mechanismus „auf Weiß anheben“ wie beim gewählten Umschalter; inaktiv #7b7b78 ohne Fläche.
- Kopfleiste der App: Creme, 52 px, Haarlinie unten, links neutrales Zeichen oder Zurück-Taste (weißer 36-px-Knopf, 8 px Radius, Haarlinie), rechts Icon-Knöpfe und Avatar 30 px.
- Detail: Leiste unten entfällt, Zurück-Taste oben links; die Bildkachel beginnt direkt unter der Kopfleiste.
- TV: Creme-Fläche, Kacheln weiß; Fokus = weiße Kachel mit 2 px #111111, keine Vergrößerung.

## Startscreen
- Eyebrow „Guten Abend, Lena“ 14 px/500, Titel 32–36 px/500 (−0,7 px), darunter eine Zeile in #626260.
- Knopfpaar: Kohle-Button (primär) und weißer Button mit Haarlinie (sekundär) – nie zwei gefüllte Knöpfe.
- Bildkachel: weiße Karte 16 px Radius, 12 px Innenabstand, Bild 12 px Radius, darunter eine Bildunterschrift-Zeile 12 px in #7b7b78 (Angaben, Musik, Zustand).
- Danach „Quellen“ als Pill-Umschalter auf Creme mit dünnem Speicherbalken und „Zuletzt hinzugefügt“ als weiße Zeilenkarte.

## Komponenten
- Buttons: 8 px Radius (nie Pille), 15 px 500, Padding 10 × 18 px, App-Höhe 42 px. Primär #111111 mit Weiß, gedrückt #000000; sekundär Weiß mit 1 px #d3cec6; tertiär ohne Fläche; Orange-Button #ff5600 nur für den einen Produktzustand und nie neben einem Kohle-Button im selben Bild.
- Karten und Kacheln: Weiß auf Creme, 12 px Radius (Bildkachel 16 px), 1 px #d3cec6, Innenabstand 14–24 px, **kein Schatten**. Getönte Variante #ebe7e1 für Hinweise; invertierte Karte #111111 mit weißer Schrift für die eine hervorgehobene Stufe; reines Schwarz nur für einen Zitatstreifen.
- Listen: Zeilen 64–68 px in einer weißen Karte, getrennt durch 1 px #ebe7e1; links Vorschaubild 44 px (8 px Radius), rechts Chevron. Auf Creme auch als Zeilen ganz ohne Karte, nur mit Haarlinie unten (FAQ-Muster).
- Suche und Eingabefelder: Weiß, 8 px Radius, 1 px #d3cec6, Padding 10 × 14 px, 44 px hoch; Fokus 1 px #111111, kein Leuchten.
- Chips, Tabs, Filter: Pill-Umschalter auf getönter Schiene #ebe7e1 (4 px Innenabstand); gewählt = weiße Pille mit 1 px #d3cec6 und Schrift #111111, ungewählt #626260 ohne Fläche. Kleine Chips 4 px Radius, 11–12 px.
- Dialoge und Sheets: Weiß, 16 px Radius, 24 px Innenabstand, 1 px #d3cec6, kein Schatten; Rückfläche Creme mit Deckkraft.
- Signatur-Komponenten: die gerahmte Bildkachel mit Unterschrift; der Pill-Umschalter „auf Weiß angehoben“; Zeilen unter warmen Haarlinien.

## Icons
- Stil (Empfehlung, die Datei nennt keine Icons): sehr feine, geometrische Linien mit runden Enden – so leise wie die Fläche; einfarbig #111111 bzw. #7b7b78, nie gefüllt, nie orange.
- Größe und Strich: 21 px in der Leiste, 18 px in Knöpfen und Zeilen, 16 px Minimum (darunter wird der feine Strich zu schwach); wirksame Strichstärke etwa 1 px auf 24er-Raster.
- Einsatz: sparsam, meist nur Chevron, Zurück, Leiste und Quellen; Zustände lieber als Wort oder Punkt als über ein Icon.
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Outlined, Gewicht 200–300, Füllung 0; iOS SF Symbols `.ultraLight`/`.light`; Web Phosphor `light`.

## Bildsprache
- Laut Datei: Produkt-Screenshots sind der Protagonist jedes Abschnitts, gerahmt in weißen Kacheln mit 16 px Radius; Bilder werden nie beschnitten, Logos klein und einfarbig, Avatare rund 40–48 px.
- Report-Farben (#65b5ff, #0bdf50, #ff2067, #b3e01c, #03b2cb) gehören laut Datei ausschließlich in Diagramme **innerhalb** eines Produktbildes – nie in die Oberfläche selbst.
- Übertragung: Bilder immer in einer weißen Kachel mit Luft ringsum (12 px) – nie randlos, nie unter die Statusleiste. Kein Verlauf, kein Text im Bild; die Angaben stehen als Unterschrift darunter. Rasterbilder 8 px Radius mit 8 px Fuge; Vorschaubilder 44 px mit 8 px Radius.

## Typografie-Stimme
- Eine Familie trägt alles; Hierarchie nur über Größe, Gewicht und Laufweite – kein zweiter Schriftschnitt.
- Gewichte: Display und Titel 500, Text 400, Buttons und Eyebrow 500. Nie fett (600+).
- Laufweite negativ proportional: −2,0 px bei 72, −1,4 bei 56, −0,8 bei 40, −0,5 bei 28, −0,3 bei 22, 0 ab 16.
- Zeilenhöhe: 1,05–1,2 im Display, 1,5 im Text. Eyebrow 14 px 500 in normaler Groß-/Kleinschreibung – **keine gesperrten Versalien**.
- Größen App: Titel 36, Kartentitel 22/17, Text 16/15, Angaben 13, Unterschrift 12.
- Mono nur in Code-Stellen innerhalb von Produktbildern, nie in der Oberfläche.
- Freier Ersatz: Inter Display (500/400) laut Datei als nächstes freies Pendant zu Saans, sonst Söhne oder Geist Sans; Mono JetBrains Mono.

## Form, Tiefe und Material
- Radien: 4 px Chips, 6 px Inline-Tags, 8 px Buttons und Felder, 12 px Karten, 16 px Bildkacheln, 24 px große Banner, Pille nur für Umschalter und Avatare.
- Linien und Rahmen: 1 px #d3cec6 (warmes Grau) als Standard, #ebe7e1 als leise Trennlinie zwischen Zeilen; keine doppelten Linien, keine Rahmen um Bilder im Raster.
- Schatten und Ebenen: Ebene 0 flach; Ebene 1 = Weiß auf Creme (der eigentliche Tiefenmechanismus); Ebene 2 = Weiß plus Haarlinie; Ebene 3 = reines Schwarz für einen Zitatstreifen. **Schatten werden bewusst vermieden.**
- Besondere Oberflächen: getöntes Creme #ebe7e1 für Hinweiskarten und Umschalter-Schienen; keine Verläufe, kein Glas, keine Körnung.

## Bewegung
- Laut Datei: keine Angaben (Hover-Zustände werden nicht dokumentiert).
- Empfehlung: Dauer klein 160 ms / Screenwechsel 240 ms, Easing `cubic-bezier(0.3, 0, 0, 1)`; Druck-Effekt: Kohle → Schwarz, weiße Fläche → #ebe7e1, kein Skalieren; Einblenden: Deckkraft + 6 px, Zeilen 50 ms gestaffelt; Screenwechsel: ruhiges Überblenden, die Creme-Fläche bleibt stehen; Fokus (TV): Rahmen 2 px in 160 ms.
- Compose: `tween(160, easing = CubicBezierEasing(0.3f, 0f, 0f, 1f))`, `AnimatedVisibility(fadeIn() + slideInVertically { it / 32 })`, `Modifier.animateItem()`; keine Feder, keine Hüpfer.

## Signatur-Elemente
1. Creme-Fläche #f5f1ec statt Weiß – warm, nie neutralgrau.
2. Weiße Karten ohne jeden Schatten, nur durch Flächenwechsel und warme 1-px-Linie abgehoben.
3. Die gerahmte Bildkachel mit 16 px Radius, Luft ringsum und kleiner Unterschrift darunter.
4. Eyebrow in normaler Groß-/Kleinschreibung über großen Titeln mit stark negativer Laufweite.
5. Pill-Umschalter, bei dem die Auswahl „auf Weiß angehoben“ wird – auch als Aktiv-Zustand der unteren Leiste.

## Übertragung auf eine App
- Startscreen: Eyebrow mit Begrüßung, großer Rückblick-Titel, Knopfpaar (Kohle + Weiß), Bildkachel mit Unterschrift, Quellen als Pill-Umschalter mit Speicherbalken, „Zuletzt hinzugefügt“ als weiße Zeilenkarte.
- Liste und Übersicht: Eyebrow mit Anzahl, Titel, weißes Suchfeld, Pill-Umschalter auf getönter Schiene, alle Einträge in **einer** weißen Karte mit 1-px-Trennlinien und Chevron; ein Orange-Chip markiert den einen neuen Eintrag.
- Detail: Zurück-Taste, Eyebrow, Titel 36 px, Angabenzeile, Bildkachel mit Unterschrift (dort auch „Musik zur Diashow“ samt Orange-Punkt für „läuft“), Kohle-Button plus weiße Icon-Knöpfe, Pill-Umschalter, Fotoraster; untere Leiste ausgeblendet.
- Formulare und Einstellungen: weiße Karte, Zeilen 64 px mit Haarlinie, Label links, Wert rechts in #626260; Abschluss mit Kohle-Button links unten.
- Leere Zustände und Laden: getönte Karte #ebe7e1 mit 12 px Radius, ein Satz in #626260, weißer Button; Laden als Creme-Platzhalter #ebe7e1, keine Illustration, kein Schimmern.
- TV: Creme-Fläche, weiße Kacheln, Titel 56 px mit −1,4 px, Fokus als 2-px-Rahmen.
- Musterscreens: Start mit Rückblick-Titel und gerahmter Bildkachel, Bibliothek als eine weiße Zeilenkarte mit Pill-Umschalter, Detail „Lissabon“ mit Bildkachel, Musik-Unterschrift und Fotoraster.

## Vermeiden
- Reines Weiß als Grundfläche, Schatten unter Karten, gesperrte Versal-Eyebrows.
- Orange als Fläche, als allgemeiner Haupt-Button oder gemeinsam mit einem Kohle-Button im selben Bild; die Report-Farben (Blau, Pink, Lime) außerhalb von Diagrammen.
- Pillenförmige Buttons, eine zweite Display-Schrift, Gewicht 600+.
- Randlose Vollbild-Fotos, beschnittene Produktbilder, bunte Abschnittsflächen.
