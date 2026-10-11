---
slug: claude
marke: Claude
website: https://claude.com
ansatz: editorial
ansatz2:
modus: hell
aufbau: Creme-Lesespalte, linksbündig; Flächen wechseln im Takt Creme → Cremekarte → dunkle Produktkarte → Koralle
navigation: App-Muster: Menü-Schublade oben links, Avatar rechts, Suche als festes Eingabefeld unten; keine Tab-Leiste
komponenten: Korallen-Callout, dunkle Produktkarte mit Mono-Zeilen, Cremekarten 12 px, Kategorie-Tabs, Kreis-Buttons 36 px
icons: Empfehlung: humanistische Linien-Icons (Phosphor Regular) 18–20 px, Tinte, nie gefüllt, nie in Koralle
bewegung: Empfehlung: ruhig, 200/320 ms, cubic-bezier(.2,0,0,1); Zeilen blenden gestaffelt ein; Druck = Koralle dunkler
schrift: Serifen-Titel 400 mit negativer Laufweite + humanistische Sans 400/500; Mono nur in dunklen Produktkarten
---
# Claude – Designsprache

**Kurz:** Eine warme, literarische Lesefläche: Creme statt Weiß, Serifen-Überschriften in Gewicht 400 mit enger Laufweite, eine humanistische Sans für alles andere. Tiefe entsteht durch Flächenwechsel statt Schatten – Creme, dunklere Cremekarte, dunkle „Produktkarte“ mit Mono-Zeilen und selten eine volle Korallenfläche. Koralle ist knapp: ein Hauptbutton pro Screen, dazu Textlinks.

## Wirkung
- Charakter: warm, besonnen, belesen; wirkt wie eine Zeitschriftenspalte, nicht wie eine SaaS-Seite. Menschlich, ruhig, nie verspielt.
- Passt zu: Lese-, Schreib-, Wissens-, Notiz- und Assistenz-Apps; Bibliotheken und Medien-Apps mit kuratierten Rückblicken.
- Passt weniger zu: Spielen, Sport, Kinder-Apps, sehr dichten Dashboards, Neon- oder Dunkel-Ästhetik.
- Abgrenzung zu ElevenLabs (auch KI, auch Serife auf Hell): Claude ist warm-creme statt neutral-grau, setzt farbige Blöcke (Koralle, Dunkel) statt Pastell-Kugeln, rechteckige 8-px-Buttons statt Pillen, Serife 400 statt 300 und zeigt Produkt-Chrome (Mono-Zeilen) statt Wellenformen.

## Aufbau und Raster
- Seitenaufbau: einspaltige Lesespalte; oben ein Serifen-Titel, darunter Bänder mit wechselnder Fläche.
- Ausrichtung: linksbündig; Dauer und Zahlen rechtsbündig in Mono.
- Raster: 4-px-Basis, Abstände 4/8/12/16/24/32/48/96 px; Web 12 Spalten, max. 1200 px, Karten 3/2/1-spaltig. App: 20 px Seitenrand, 12 px Kartenabstand, Kartenraster 2-spaltig.
- Dichte und Weißraum: großzügig – Karten innen 32 px (Web) bzw. 20 px (App), Bänder 96 px (Web) bzw. 28–32 px (App) auseinander.
- Rhythmus: nie zweimal dieselbe Fläche hintereinander: Creme → Cremekarte #efe9de → dunkle Produktkarte #181715 → Creme → Korallen-Callout → dunkler Fuß.

## Navigation
- Website: Kopfleiste 64 px auf Creme, Wortmarke links, Menü 14 px 500, rechts Textlink „Anmelden“ und Korallen-Button; unter 768 px Hamburger, Menü als Creme-Vollbild.
- App (App-Muster der Marke, nicht in der Datei): keine Tab-Leiste. Oben 52 px: links Kreis-Button 36 px (Creme + Haarlinie) für die Menü-Schublade (Start, Bibliothek, Profil, darunter zuletzt geöffnete Alben), rechts Avatar 36 px als Profil. Die Suche ist ein festes Eingabefeld unten wie das Chat-Eingabefeld: 16 px Radius, Haarlinie, Plus-Knopf, Quellen-Auswahl als Text mit Pfeil, Korallen-Quadrat 32 px mit Pfeil nach oben. Es bleibt beim Scrollen stehen, Inhalt läuft in einen Creme-Verlauf aus. Aktiv in der Schublade: Fläche #efe9de + Tinte.
- Detail: Kreis-Button „Zurück“ links, rechts ein Textbutton; das Eingabefeld entfällt.
- TV: Schublade als dauerhaft offene Creme-Spalte links; Fokus = Korallen-Rand + 3-px-Ring Koralle 15 % (wie der Eingabefokus).

## Startscreen
- Begrüßung als Serifen-Titel 34 px/400/−0,5 px, darunter Kennzahlen 15 px muted.
- Ein Korallen-Callout (12 px Radius, 20 px innen) als Höhepunkt: Versal-Label, Serifen-Titel weiß, Angaben, Creme-Button „Ansehen“, Bild mit 8 px Radius eingesetzt.
- Darunter ein Abschnitt mit Serifen-Kopf 24 px und Korallen-Textlink „Alle“: Cremekarten in einer Reihe, die dritte angeschnitten.
- Fest unten das Eingabefeld der Suche.

## Komponenten
- Buttons: 8 px Radius, 14 px 500, 12 × 20 px, 40 px hoch (App 44). Primär Koralle #cc785c, gedrückt #a9583e, aus #e6dfd8 mit Text muted; Sekundär Creme + 1 px Haarlinie; auf Dunkel #252320; auf Koralle invers in Creme. Kreis-Icon-Button 36 px Creme + Haarlinie. Nie Pille.
- Karten und Kacheln: Cremekarte #efe9de, 12 px, kein Schatten; Bild darin mit 8 px Rand und 8 px Radius. Großes Bild 16 px. Dunkle Produktkarte #181715, 12 px, 20 px innen, Inhalt als Mono-Zeilen auf #1f1e1b mit Statusleiste #252320.
- Listen: Zeilen 56–64 px, Titel 16 px 500, Angaben 14 px muted, Trennlinie #ebe6df; Zahlen in Mono rechts.
- Suche und Eingabefelder: Creme, 1 px Haarlinie #e6dfd8, 8 px Radius, 10 × 14 px, 40–44 px hoch; Fokus: Rand Koralle + 3-px-Ring Koralle 15 %.
- Chips, Tabs, Filter: category-tab 8 × 14 px, 8 px Radius; inaktiv transparent + muted, aktiv Fläche #efe9de + Tinte. Badges als Pille 13 px 500 auf #efe9de; „NEU“ in Koralle, Versalien 12 px +1,5 px.
- Dialoge und Sheets: Creme-Sheet mit 16 px Radius oben; kurze Hinweise als dunkle Karte unten (wie der Cookie-Hinweis).
- Signatur-Komponenten: Korallen-Callout mit Serifen-Titel; dunkle Produktkarte mit Zeilennummern, Mono-Text, hervorgehobener aktueller Zeile und Statusleiste; Eingabefeld unten mit Korallen-Quadrat.

## Icons
- Stil (Empfehlung, die Datei nennt keine): humanistische Linien-Icons mit runden Enden und offenen Formen; Tinte, inaktiv muted; nie gefüllt, nie Koralle (außer Weiß auf dem Korallen-Button).
- Größe und Strich: 20 px in der Kopfleiste, 18 px in Buttons, 16 px vor Angaben; Strich etwa 1,5 px.
- Einsatz: meist im 36-px-Kreis-Button oder vor Text; Status als Punkt in Teal #5db8a6 statt farbiger Icons.
- Umsetzung: Compose `Icons.Rounded` bzw. Material Symbols Rounded, Gewicht 300, Füllung 0; iOS SF Symbols `.regular` ohne `.fill`; Web Phosphor Regular.

## Bildsprache
- Laut Datei: kaum Fotografie; stattdessen Strich-Illustrationen in Koralle und Dunkel auf Creme, Produkt-Mockups und Code-Fenster; Avatare rund 40 px.
- Übertragung: Medien sind Inhalt, nie Stimmung: Bilder immer eingefasst (8 px Rand in der Karte, Radius 8/12/16 px), nie randlos, kein Text auf Bildern, keine Verlaufs-Overlays. Empfehlung: leicht warm gedämpft (`saturate(.92) sepia(.06)`). Leere Zustände mit kleiner Strichzeichnung in Tinte + Koralle.

## Typografie-Stimme
- Display: Serife 400, nie fett: 64/48/36/28 px, Laufweite −1,5/−1/−0,5/−0,3 px, Zeilenhöhe 1,05–1,2. App: Titel 34–40 px, Abschnitte 24 px, Callout 30 px.
- Text: humanistische Sans 400 (16 px/1,55), Labels und Buttons 500 (14 px), Caption 13 px 500, Versal-Label 12 px 500 mit +1,5 px.
- Mono 13 px nur in dunklen Produktkarten (Zeilennummern, Titel, Dauer, Status).
- Betonung über eine größere Serife, nicht über mehr Gewicht.
- Freier Ersatz: Lora bzw. Cormorant Garamond 500 (−0,02 em) für Copernicus/Tiempos; Inter für StyreneB; JetBrains Mono. Im Muster: Lora, Inter, DejaVu Sans Mono.

## Form, Tiefe und Material
- Radien: 4 px Mini-Badges, 6 px kleine Buttons und Thumbnails, 8 px Buttons/Felder/Tabs, 12 px Karten, 16 px großes Bild und Eingabefeld unten, Pille für Badges, rund für Avatare und Icon-Buttons.
- Linien und Rahmen: 1 px #e6dfd8 auf Creme, #ebe6df innerhalb eines Bandes.
- Schatten und Ebenen: Farbblock zuerst, Schatten selten – höchstens `0 1px 3px rgba(20,20,19,.08)` für gehobene Zustände und das Eingabefeld unten.
- Besondere Oberflächen: Creme-Leiter #faf9f5 → #f5f0e8 → #efe9de → #e8e0d2; Dunkel-Leiter #181715 → #1f1e1b → #252320. Keine Verläufe (außer dem Auslauf über dem Eingabefeld), kein Glas, keine Körnung.

## Bewegung
- Laut Datei: keine Timings (Chat-Einblendung und Tipp-Effekt in Code-Blöcken werden erwähnt, aber nicht erfasst). Zustand: Primär wird beim Drücken dunkler (#a9583e), sonst ändert sich nichts.
- Empfehlung: Dauer klein 200 ms / Screenwechsel 320 ms, Easing `cubic-bezier(0.2, 0, 0, 1)`; Druck: Fläche dunkler, kein Skalieren; Einblenden: Deckkraft + 6 px Anheben, Abschnitte 60 ms gestaffelt; Mono-Zeilen erscheinen zeilenweise (40 ms); Screenwechsel: Überblenden; Fokus (TV): Korallenring blendet in 160 ms ein.
- Compose: `tween(200, easing = CubicBezierEasing(0.2f, 0f, 0f, 1f))`, `AnimatedVisibility(fadeIn() + slideInVertically { it / 16 })`, `Modifier.animateItem()`; kein Federn, kein Skalieren.

## Signatur-Elemente
1. Creme-Fläche #faf9f5 mit warmer Tinte #141413 – nie reines Weiß.
2. Serifen-Titel 400 mit negativer Laufweite gegen eine humanistische Sans.
3. Flächen-Rhythmus: Cremekarte → dunkle Produktkarte mit Mono-Zeilen → volle Korallenfläche.
4. Koralle knapp: ein rechteckiger 8-px-Hauptbutton, Textlinks, das Senden-Quadrat.
5. Suche als Eingabefeld unten wie im Chat (App-Muster).

## Übertragung auf eine App
- Startscreen: Kopf mit Menü-Kreis und Avatar, Serifen-Begrüßung mit Kennzahlen, Rückblick als Korallen-Callout, „Zuletzt hinzugefügt“ als Reihe von Cremekarten, Quellen-Band mit Haarlinie und Mono-Speicherstand, Eingabefeld unten.
- Liste und Übersicht: Serifen-Titel, Suchfeld mit Haarlinie, category-tabs, Sortierzeile; Alben als 2-spaltiges Cremekarten-Raster, Musik als dunkle Produktkarte mit Mono-Dauern (Flächenwechsel als Gruppierung).
- Detail: Versal-Label, Serifen-Titel 40 px, Angaben, Bild mit 16 px Radius, Korallen-Button „Diashow starten“ mit drei Kreis-Buttons, dunkle Produktkarte „Musik zur Diashow“ mit nummerierten Titeln, dann Tabs und Fotoraster (8 px Radius).
- Formulare und Einstellungen: Cremekarten-Gruppen mit 56-px-Zeilen, Label 16 px 500, Wert muted rechts, Felder mit Haarlinie und Korallen-Fokus; Gefahr als Text in #c64545.
- Leere Zustände und Laden: kleine Strichzeichnung (Tinte + Koralle), ein Serifen-Satz 24 px, ein Sekundärbutton; Laden als Mono-Zeilen, die nacheinander erscheinen, oder ruhige Platzhalter in #efe9de ohne Schimmer.
- TV: Creme-Spalte links, Inhalte als Cremekarten-Raster mit 12 px Radius; Rückblick als breites Korallen-Callout; Fokus = Korallen-Rand + Ring.
- Musterscreens: Start mit Serifen-Begrüßung, Korallen-Rückblick, Cremekarten-Reihe und Quellen-Band über dem Such-Eingabefeld; Bibliothek als Cremekarten-Raster mit dunkler Musik-Karte; Album „Lissabon“ als Artikel mit Mono-Titelliste.

## Vermeiden
- Reines Weiß oder kühles Grau als Fläche; kühles Blau oder Cyan als Akzent; eine vierte Flächenfarbe (Lila, Grün).
- Koralle auf vielen kleinen Elementen, für aktive Tabs, Icons oder Deko; Pillen-Buttons.
- Fette Serife (700), Sans-Display, Serife ohne negative Laufweite.
- Zwei gleiche Flächen direkt hintereinander; Schatten als Hauptmittel der Tiefe.
- Randlose Vollbild-Bilder mit Text darauf, Verläufe, Glas, Neon, Körnung.
- Hover- und Druck-Effekte über „Primär wird dunkler“ hinaus (kein Skalieren, kein Glühen).
