---
slug: miro
marke: Miro
website: https://miro.com
ansatz: verspielt
ansatz2: galerie
modus: hell
aufbau: Weiße Fläche; Inhalte liegen auf einer gepunkteten Leinwand als Karten mit sehr großen Radien (20–28 px)
navigation: Schwebende schwarze Pillenleiste unten mit 4 Icons; aktives Ziel als weißer Kreis in der Pille
komponenten: Board-Mockup mit Haftnotizen und Mitlesen-Zeiger, Pastellkarten (28 px), Pill-Tabs, Chip-Tags
icons: runde, geometrische Linien-Icons 20–22 px, Strich 2 px; auf 36-px-Kreisknöpfen mit 1-px-Haarlinie
bewegung: freundlich, kurz; Empfehlung 180 ms klein / 240 ms Screen, cubic-bezier(.2,.8,.3,1), leichter Pop beim Drücken
schrift: geometrische Grotesk (Roobert PRO → Poppins) in nur 400/500/600; Hero 32–40 px mit enger Zeilenhöhe 1,05
---
# Miro – Designsprache

**Kurz:** Eine weiße, freundlich-geometrische Werkzeugsprache: Schwarz ist die Aktionsfarbe (Pillen-Buttons), das Kanariengelb bleibt klein und nur Zeichen, Tag und Banner. Die Persönlichkeit kommt aus zwei Quellen – pastellige Flächenkarten mit sehr großen Radien (28 px) und dem echten Produkt als Illustration: eine gepunktete Leinwand mit Haftnotizen, Auswahlrahmen und einem fremden Mauszeiger mit Namensschild.

## Wirkung
- Charakter: offen, kooperativ, leicht verspielt, aber sachlich; nie laut, weil die Farbe in Pastell bleibt und die Aktion schwarz ist.
- Passt zu: Werkzeugen für Zusammenarbeit, Sammlungen, Boards, Planung, Lernen; Apps, die Inhalte zum Anordnen zeigen.
- Passt weniger zu: ernsten Finanz-Oberflächen, dunklen Medien-Apps, Marken, die über Fotografie erzählen (die Datei verbietet Stockfotos ausdrücklich).

## Aufbau und Raster
- Seitenaufbau: schmaler weißer Kopf → großer Titel mit enger Zeilenhöhe → ein Board-Mockup als Hauptbild → Reihen aus Pastell- und Weißkarten; Leisten und Werkzeuge schweben über dem Inhalt statt ihn zu begrenzen.
- Ausrichtung: Marketing zentriert, Produktflächen linksbündig; in der App linksbündig mit zentrierter Pillenleiste.
- Raster: 4-px-Basis (8 px Hauptschritt), Tokens 4/8/12/16/20/24/32/40/48/64/96/120 px; Web 1280 px mit 32 px Rinnen. App: 20 px Seitenrand, 12 px zwischen Karten (Empfehlung).
- Dichte und Weißraum: Marketing großzügig (96–120 px Bänder), Produktflächen dicht; Kartenpolster 24 px (kompakt) bzw. 32 px (Feature).
- Rhythmus: eine große Fläche, dann zwei bis vier kleine Pastellflächen; weiße und pastellige Karten stehen laut Datei immer gemeinsam im Bild.

## Navigation
- Website: 64-px-Kopfleiste weiß, gelbes Zeichen links, Textlinks, rechts schwarzer Pillen-Button; darüber optional ein schwarzer Promo-Streifen mit gelber Pille.
- App (Empfehlung): schwebende schwarze Pillenleiste unten (Radius voll, 16 px über dem Rand, Höhe 60 px, Schatten `rgba(5,0,56,.12) 0 16px 48px -8px`), 4 Ziele als 22-px-Icons in Weiß; aktiv liegt das Icon in einem weißen Kreis (44 px) – Form statt Farbe. Werkzeuge und Filter schweben ebenfalls, der Inhalt läuft darunter durch.
- TV (Empfehlung): Pillenleiste nach oben, Fokus als weißer Kreis bzw. 4-px-Rahmen in `#4262ff`.

## Startscreen
- Kleiner Kopf (Zeichen links, Kreisknopf und Avatar rechts), dann Titel 32/500 mit Zeilenhöhe 1,05 und −1 px Laufweite, darunter eine Zeile in `#555a6a`.
- Hauptbild ist das Board-Mockup: weiße Karte mit 16 px Radius, 1 px `#eef0f3`, Schatten `rgba(5,0,56,.08) 0 12px 32px -4px`; darin die gepunktete Leinwand mit Bildkachel, zwei Haftnotizen, gestricheltem Auswahlrahmen und Zeiger mit Namensschild.
- Darunter drei Pastellkacheln (gelb, türkis, koralle) als Quellen und eine angeschnittene Reihe aus Vorlagenkarten (16 px Radius, 1 px Haarlinie).

## Komponenten
- Buttons: Primär schwarz `#1c1c1e`, Text weiß 14/500, Padding 12×24, Radius voll; gedrückt `#2c2c34`; deaktiviert `#e0e2e8` mit `#a5a8b5`. Sekundär transparent mit 1 px `#c7cad5`. Gelb `#ffd02f` mit schwarzem Text nur für Markenmomente, blau `#4262ff` für Hinweis-Aktionen. Geist-Button rechteckig mit 8 px Radius. Kreisknopf 36 px weiß mit 1 px `#e0e2e8`.
- Karten und Kacheln: Standardkarte weiß, Radius 16, 1 px `#eef0f3`, Polster 24; Feature- und Pastellkarte Radius 28, Polster 32, ohne Rand; CTA-Banner Radius 32 in Schwarz. Vorlagenkarte Radius 16 mit 16 px Polster.
- Listen: Miro listet selten – Inhalte stehen als Karten im Raster; Zeilen gibt es nur in der Vergleichstabelle (Zeile 16×20 px, 1 px `#eef0f3` unten). In der App daher 2-spaltiges Kartenraster statt Liste (Empfehlung).
- Suche und Eingabefelder: Suchfeld `#f7f8fa`, Radius 8, Höhe 40, 1 px `#e0e2e8`, Text 14/400 `#6b6f7e`. Textfeld weiß, Radius 8, Höhe 44, 1 px `#c7cad5`; Fokus 2 px `#4262ff`.
- Chips, Tabs, Filter: Pill-Tab weiß mit 1 px `#e0e2e8`, Text 14/500 `#6b6f7e`; aktiv schwarz gefüllt mit weißem Text. Filter-Dropdown als Pille mit 1 px `#c7cad5`. Tag-Chips pastellig mit dunklem Eigenton: gelb `#fff8e0`/`#746019`, lavendel `#f5f3ff`/`#4262ff`, koralle `#ffc6c6`/`#600000`.
- Dialoge und Sheets (Empfehlung): weißes Blatt mit 28 px oberen Ecken, Schatten `rgba(5,0,56,.12) 0 16px 48px -8px`, Griff 40×4 px `#e0e2e8`.
- Signatur-Komponenten: Board-Mockup (gepunktete Leinwand, Haftnotizen, gestrichelter Auswahlrahmen mit Eckpunkten, Zeiger mit Namensschild); Pastellkarten; schwarze Pillen; schwebende Werkzeugleiste.

## Icons
- Stil: runde, geometrische Linien-Icons, gleichmäßige Strichstärke, keine Füllungen; sie wirken wie Werkzeuge auf einer Leinwand.
- Größe und Strich: 20–22 px in Leisten und Knöpfen, 16 px in Chips; Strich 2 px mit runden Enden.
- Einsatz: Icons sitzen auf 36-px-Kreisknöpfen (weiß, 1 px `#e0e2e8`) oder frei in `#1c1c1e`; auf der schwarzen Pillenleiste in Weiß, das aktive im weißen Kreis dann in Schwarz. Pastellkarten tragen ihr Icon im Eigenton der Karte.
- Umsetzung: Compose `Icons.Rounded` bzw. Material Symbols Rounded (Gewicht 400, Füllung 0); iOS SF Symbols Medium; Web Lucide stroke 2 oder Phosphor Regular.

## Bildsprache
- Laut Datei keine Stockfotografie, sondern das Produkt selbst: Board-Ausschnitte mit Haftnotizen und Farbkacheln. Übertragen heißt das: Inhalte liegen wie Zettel auf einer Leinwand – leicht gedreht (±2–3°), mit weißem Rand und weichem Schatten.
- Geometrie: Mockups 16 px Radius mit Schatten, Geschichten-Karten 28 px mit randlosem Bild, Vorlagenbilder 16 px, Rasterbilder 12 px.
- Hintergrund der Inhaltsfläche ist die gepunktete Leinwand (`#fafbfc` mit 1,2-px-Punkten im 18-px-Raster, Empfehlung) – sie ersetzt bei dieser Marke jeden Verlauf und jede Körnung.

## Typografie-Stimme
- Eine geometrische Grotesk für alles (Roobert PRO; freier Ersatz Poppins, alternativ Hanken Grotesk oder Outfit). Nur drei Gewichte: 400 Text, 500 Überschriften und Labels, 600 Badges und Versal-Mikro – kein 700.
- Skala: Hero 80/500/1,05/−2 px (App 32–40 px), Überschrift 36/500/−0,5, Kartentitel 28/500, Kachel 22/500, klein 18/500, Text 16/400/1,5, Angaben 14/400, Caption 13, Mikro 12/500, Versal-Mikro 11/600 +0,5 px, Button 14/500, Kennzahl 64/500/−1,5.
- Enge Zeilenhöhe im Hero (1,05) ist ausdrücklich Pflicht; negative Laufweite nur in den großen Graden.
- Freier Ersatz: Poppins (Empfehlung, geometrisch und leicht rund wie Roobert); Noto Sans laut Fallback-Kette der Datei.

## Form, Tiefe und Material
- Radien: 4 / 6 (Rabatt-Badge) / 8 (Felder, Geist-Button) / 12 (Karten, Rasterbilder) / 16 (Standardkarte, Mockup) / 20 / 28 (Pastell- und Geschichten-Karten) / 32 (CTA-Banner) / voll (jeder Button, Pill-Tab, Badge).
- Linien und Rahmen: 1 px `#eef0f3` an ruhigen Karten, `#e0e2e8` an Trennern und Kreisknöpfen, `#c7cad5` an Eingaben; Fokus 2 px `#4262ff`.
- Schatten und Ebenen: fünf leise Stufen mit blauem Unterton – 1 `rgba(5,0,56,.04) 0 1px 2px`, 2 `rgba(5,0,56,.06) 0 4px 12px`, 3 `rgba(5,0,56,.08) 0 12px 32px -4px` (nur Mockups), 4 `rgba(5,0,56,.12) 0 16px 48px -8px` (Schwebendes). Flache Karten bleiben ohne Schatten.
- Besondere Oberflächen: Pastellflächen als eigene „Materialien“ (gelb, koralle, türkis, rosé, orange) und die gepunktete Leinwand; keine Verläufe, kein Glas.

## Bewegung
- Laut Datei: keine Zeiten erfasst; empfohlen werden dort 150–200 ms mit Ease.
- Empfehlung: klein 180 ms / Screenwechsel 240 ms, Easing `cubic-bezier(0.2, 0.8, 0.3, 1)`; Druck als kurzer Pop (0,97 → 1) statt Farbwechsel; Karten blenden mit 8 px von unten ein, 35 ms gestaffelt; Haftnotizen und Zeiger erscheinen leicht versetzt, als würde jemand mitarbeiten; Sheets gleiten mit 28-px-Ecken herein; Fokus (TV) weißer Kreis bzw. 4-px-Rahmen in `#4262ff`, 180 ms.
- Compose: `tween(180, easing = CubicBezierEasing(0.2f, 0.8f, 0.3f, 1f))`, Druck `spring(dampingRatio = 0.65f, stiffness = 600f)`, `AnimatedVisibility(fadeIn() + slideInVertically { it / 10 })`, `Modifier.animateItem()`.

## Signatur-Elemente
1. Board-Mockup: gepunktete Leinwand, leicht gedrehte Zettel, gestrichelter Auswahlrahmen mit Eckpunkten, fremder Zeiger mit Namensschild.
2. Schwarze Pillen als einzige Hauptaktion – Gelb nur als Zeichen, Tag oder Banner, nie als Button.
3. Pastellkarten mit 28 px Radius neben weißen Karten im selben Bild.
4. Schwebende schwarze Pillenleiste mit weißem Kreis für das aktive Ziel.
5. Geometrische Schrift in nur drei Gewichten mit sehr enger Zeilenhöhe im Titel.

## Übertragung auf eine App
- Startscreen: Titel mit 1,05 Zeilenhöhe, darunter das Board-Mockup als Rückblick, dann drei Pastellkacheln für die Quellen und eine angeschnittene Reihe Vorlagenkarten.
- Liste und Übersicht: Suchfeld mit 8 px Radius, Pill-Tabs als Filter (aktiv schwarz), darunter ein 2-spaltiges Kartenraster auf gepunkteter Leinwand, Karten abwechselnd weiß und pastellig mit Tag-Chip; ein Mitlesen-Zeiger macht die Fläche als Board erkennbar.
- Detail: Bild als Mockup-Rahmen (16 px, Schatten), Titel 32–36/500, Tag-Chips, schwarze Pille als Hauptaktion neben umrandeter Pille und Kreisknopf, Pill-Tabs, 12-px-Raster, zum Schluss eine gelbe Pastellkarte für die Musik.
- Formulare und Einstellungen: weiße Karten mit 16 px Radius, Felder 44 px/8 px Radius, Fokus 2 px Blau, Hauptaktion als schwarze Pille; Hinweise als pastellige Tag-Chips.
- Leere Zustände und Laden: leere gepunktete Leinwand mit einer einzelnen Pastellkarte, Titel 22/500, Satz 16/400 `#555a6a`, schwarze Pille; Laden als `#f7f8fa`-Blöcke mit 16 px Radius.
- TV: gepunktete Leinwand als Hintergrund, Karten 28 px, Pillenleiste oben, Fokus als weißer Kreis.
- Musterscreens: Start mit engem Titel, Board-Mockup samt Zeiger, Pastell-Quellen und Vorlagenreihe; Bibliothek als Kartenraster auf gepunkteter Leinwand mit Pill-Tabs und schwebender Pillenleiste; Detail mit Mockup-Bild, Tag-Chips, schwarzer Pille und gelber Musikkarte.

## Vermeiden
- Gelb als Buttonfarbe oder große Fläche; weitere Akzentfarben neben Gelb und den Pastellen.
- Eckige oder leicht gerundete Buttons – die Pille ist Pflicht; Pastellkarten unter 28 px Radius.
- Zeilenhöhe unter 1,05 im Titel, Gewicht 700, Versalien in Fließtexten.
- Schwere Schatten auf flachen Karten; Tiefe bleibt den Mockups und Schwebenden vorbehalten.
- Stockfotografie oder Fotoflächen ohne Board-Charakter – Inhalte sollen wie Material auf einer Leinwand liegen.
