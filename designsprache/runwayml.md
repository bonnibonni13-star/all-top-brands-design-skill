---
slug: runwayml
marke: Runway
website: https://runwayml.com
ansatz: buehne
ansatz2: editorial
modus: gemischt
aufbau: Randlose Foto-/Video-Bühnen auf Schwarz, dazwischen helle Lesebänder; Mosaik-Raster, UI fast unsichtbar
navigation: Keine Leiste unten: Versal-Textnavigation oben über dem Bild (3 Ziele + Avatar), aktiv = weiß + Unterstrich
komponenten: Vollbild-Bühne mit Titel unten links, Mosaik mit Bildtiteln, Versal-Labels, 4-px-Buttons schwarz/weiß
icons: Haarfeine Linien-Icons (Lucide 1.25), 18–22 px, einfarbig, nie gefüllt, nie in Kreisen (Empfehlung)
bewegung: Filmisch ruhig: Blenden 200/500 ms, cubic-bezier(.25,.1,.25,1), langsamer Bild-Zoom, kein Federn (Empfehlung)
schrift: Eine Schrift: Titel 400 mit Zeilenhöhe 1,0 und −1,2 px, Labels 11–14 px versal gesperrt, nie fett
---
# Runway – Designsprache

**Kurz:** Bilder und Videos sind die Oberfläche: randlose, filmische Bühnen tragen jeden Screen, die UI zieht sich auf Text, Haarlinien und zwei Graustufen zurück. Abschnitte trennen sich durch den Wechsel von Schwarz zu hellen Lesebändern – nie durch Schatten, Karten oder Farbe. Eine einzige Schrift mit engen Filmtitel-Zeilen und gesperrten Versal-Labels gibt die Struktur.

## Wirkung
- Charakter: filmisch, ernst, kuratiert; wirkt wie eine Produktionsmappe oder ein Festival-Programm, nicht wie eine App-Oberfläche.
- Passt zu: Video-, Foto- und Medien-Apps, Kreativ- und Kamera-Werkzeugen, Portfolios, Streaming mit Autorenfilm-Anspruch.
- Passt weniger zu: Apps ohne starke Bilder, Formular- und Finanz-Apps, verspielten oder bunten Marken.
- Abgrenzung zu Framer (gleiche Branche, auch dunkel): Runway zeigt Bilder randlos und eckig (0–8 px), ohne Farbe, Karten und Pills, mit Versal-Text-Navigation und hellen Lesebändern; Framer setzt alles in gerundete Kacheln (15–30 px) mit Verlaufs-Spotlights und Pill-Knöpfen.

## Aufbau und Raster
- Seitenaufbau: Vollbild-Bühne (55–65 % der Höhe) → helles Leseband oder schwarzer Abschnitt mit Mosaik → nächste Bühne; wie Szenenwechsel.
- Ausrichtung: linksbündig; Bühnentitel unten links auf dem Bild, Angaben direkt darunter.
- Raster: 8-px-Basis, Skala 4/6/8/12/16/20/24/28/32/48/64/78 px; Web-Container bis 1600 px, Bühnen randlos. Raster asymmetrisch: groß + zwei klein gestapelt, mehrspaltig → 2 → 1.
- Dichte und Weißraum: Abschnitte 48–78 px (Web), App 28–48 px; Komponenten 16–24 px; Seitenrand App 20 px, Mosaik-Fuge 6 px. „Bilder ersetzen Weißraum“ – leere Flächen werden mit Bildern gefüllt, nicht mit Luft.
- Rhythmus: Bild – Text – Bild; nie zwei Textabschnitte hintereinander ohne Bild.

## Navigation
- Website: minimale, transparente Leiste über dem Hero, Links 16 px 400–600; Hover = weiß bzw. deckender. Auf Mobil Hamburger.
- App (Empfehlung): keine Tab-Leiste unten. Oben 44 px transparent über der Bühne: neutrales Zeichen links, drei Versal-Textziele START · BIBLIOTHEK · SUCHE (12 px 500, +0,35 px, 22 px Abstand), rechts Avatar 28 px für Profil. Aktiv = Weiß 100 % + 1-px-Unterstrich 6 px unter der Grundlinie; inaktiv Weiß 62 %. Beim Scrollen bekommt die Leiste reines Schwarz, ohne Schatten oder Linie. Entscheidung: Hamburger der Website entfällt, weil vier Ziele als Text passen.
- Detail: nur Pfeil zurück (22 px) über dem Bild; Aktionen stehen im Leseband.
- TV: Versal-Textnavigation oben links über der Bühne; Fokus = Unterstrich + volle Deckkraft, keine Vergrößerung.

## Startscreen
- Vollbild-Bühne „Weiter ansehen“ (ein Video, 520 px hoch) mit Navigation oben, unten Versal-Label, Titel 44 px, Angaben, 2-px-Zeitleiste mit Zeitcodes und zwei 4-px-Buttons.
- Direkt darunter ein helles Leseband (Cool Cloud): Rückblick als Editorial-Zeile – Bild 4:5 links, Titel 24 px rechts, Textlink mit Pfeil; darunter eine Haarlinie und eine Quellen-/Speicherzeile aus Versal-Label, Namen, 2-px-Balken und Micro-Zahlen.
- Danach ein Mosaik „Zuletzt hinzugefügt“ im Anschnitt. Keine Kennzahlen-Kacheln, keine Icons.

## Komponenten
- Buttons: 14 px 600, 4 px Radius, 44 px hoch, Padding 0 × 16 px. Primär = Vollfläche in Gegenfarbe des Abschnitts (Weiß auf Schwarz/Bild, Schwarz auf Hell); Sekundär = transparent, 1 px #27272a (dunkel) bzw. #c9ccd1 (hell), auf Bildern Schwarz 35 % + 1 px Weiß 28 %. Textlink 14 px 600 mit Pfeil. Entscheidung: Der Index nennt Pill-Buttons, Datei (Komponenten, Don'ts) verlangt 4 px → 4 px.
- Karten und Kacheln: „Das Bild ist die Karte“ – Foto mit 8 px Radius ohne Fläche, Rand oder Schatten; Titel als Overlay unten links (Verlauf von unten) oder als Bildunterschrift. Gerahmter Container nur für Hinweise: #1a1a1a, 1 px #27272a, 16 px Radius.
- Listen: Editorial-Zeilen – Bild links (4:5 oder 1:1, 4–8 px), daneben Versal-Label 11 px, Titel 20–24 px, Angaben 13 px Cool Slate; Trennlinie 1 px #27272a bzw. #d0d4d4, keine Kästen.
- Suche und Eingabefelder: 44 px, 4 px Radius; dunkel #1a1a1a mit 1 px #27272a, hell #e9ecf2 ohne Rand; Lupe 18 px, Platzhalter Mid Slate #7d848e. Fokus: Rand Weiß 40 % (Empfehlung).
- Chips, Tabs, Filter: Versal-Textreiter 12 px 500, +0,35 px, 20 px Abstand, auf 1-px-Grundlinie; aktiv Weiß bzw. Schwarz + 1-px-Unterstrich, inaktiv Cool Slate. Keine Pill-Chips.
- Dialoge und Sheets: reines Schwarz #030303 oder hell, oben 16 px Radius, ohne Schatten; Scrim Schwarz 70 % (Empfehlung).
- Signatur-Komponenten: Vollbild-Bühne mit Titel und Zeitcode-Leiste; Mosaik-Raster mit Overlay-Titeln und Dauer-Etikett (11 px auf Schwarz 55 %, 4 px); helles Leseband im dunklen Fluss; Versal-Label als Wegweiser.

## Icons
- Stil (Empfehlung; die Datei zeigt statt Icons echte Bilder): haarfeine Linien, runde Enden, einfarbig Weiß bzw. Schwarz; nie gefüllt, nie in Kreisen oder Flächen. Navigation und Kategorien sind Text oder Bild, nicht Icon.
- Größe und Strich: 16–18 px in Buttons und Feldern, 22 px in Kopfzeilen; sichtbarer Strich etwa 1 px (Lucide 1.25 auf 24er-Raster).
- Einsatz: nur Funktionen – Zurück, Suche, Play, Teilen, Favorit, Mehr, Pfeil am Textlink. Icon-Buttons 44 × 44 px mit 1-px-Rahmen und 4 px Radius oder ganz ohne Fläche.
- Umsetzung: Compose Material Symbols Outlined, Gewicht 200, Füllung 0, bzw. `Icons.Outlined`; iOS SF Symbols `.ultraLight`/`.thin`, ohne `.fill`; Web Lucide `stroke-width: 1.25`.

## Bildsprache
- Laut Datei: filmische Vollbilder und Videos sind die Hauptelemente; Hero randlos; Raster asymmetrisch in Magazin-Größen; dunkle Überlagerung für Lesbarkeit; Screenshots mit 8 px Radius.
- Übertragung: Bühnen ohne Radius bis an den Rand; Mosaik-Kacheln 8 px, kleine Fotos 4 px, Fuge 4–6 px; Seitenverhältnisse wechseln (16:9, 4:5, 1:1). Verlauf Schwarz 0 → 85 % nur unter Text, oben 50 % für Statusleiste. Farben unverändert; Empfehlung: leichte Filmkörnung auf Bühnen (Deckkraft 0,10).

## Typografie-Stimme
- Eine Schrift für alles; Vielfalt nur über Größe, Gewicht, Versalien und Laufweite.
- Display 48/40/36 px, 400, Zeilenhöhe 1,0, −1,2/−1/−0,9 px; Kartentitel 24/20 px 400, 1,0; Text 16 px, 1,3–1,5, −0,16 px; Klein 13 px, −0,16 bis −0,26 px; Label 14 px 500–600 versal +0,35 px; Micro 11 px 450 versal.
- App: Bühnentitel 44–48 px, Screen-Titel 40 px, Abschnittstitel 24 px, Kacheltitel 16–20 px, Angaben 13 px, Labels 11–12 px versal.
- Nie 700+, Text-Zeilenhöhe nie über 1,5, Versalien nie ohne Sperrung.
- Freier Ersatz: Inter (Text) + Inter Display (ab 20 px) als eine Familie; laut Datei auch DM Sans. 450 ohne variable Schrift → 500.

## Form, Tiefe und Material
- Radien: 0 Bühnen, 4 px Buttons/kleine Fotos, 6 px Links/kleine Container, 8 px Bildkarten, 16 px Hinweis-Container; rund nur Avatare; nie Pill.
- Linien und Rahmen: 1 px #27272a auf Dunkel, #c9ccd1/#d0d4d4 auf Hell; nur für Felder, Reiter-Grundlinie und Trennung.
- Schatten und Ebenen: keine. Tiefe = Wechsel Schwarz (#000/#1a1a1a) ↔ Hell (#fefefe/#e9ecf2), Bildtiefe, Überlagerungen.
- Besondere Oberflächen: keine Verläufe außer Lesbarkeits-Scrim auf Bildern, kein Glas; mittlere Grautöne nie als Fläche.

## Bewegung
- Laut Datei: Hover → Text wird weiß bzw. deckender; sonst keine Angaben.
- Empfehlung: Dauer klein 200 ms / Screenwechsel 500 ms, Easing `cubic-bezier(0.25, 0.1, 0.25, 1)`; Druck = Deckkraft 100 → 70 %, kein Skalieren; Einblenden: Bühne blendet aus Schwarz auf und zoomt in 1,2 s von 1,04 auf 1,0, Titel folgt 120 ms später mit 8 px Anheben; Screenwechsel = Kreuzblende über Schwarz; Fokus (TV) = Unterstrich wächst in 200 ms.
- Compose: `tween(500, easing = CubicBezierEasing(0.25f, 0.1f, 0.25f, 1f))`, `Crossfade`, `AnimatedVisibility(fadeIn(tween(400)) + slideInVertically { it / 12 })`, Ken-Burns über `graphicsLayer { scaleX/scaleY }`; kein `spring` mit Überschwingen.

## Signatur-Elemente
1. Randlose Foto-/Video-Bühne mit Titel 44–48 px (400, Zeilenhöhe 1,0, negative Laufweite) unten links.
2. Wechsel Schwarz ↔ helles Leseband statt Karten und Schatten.
3. Versal-Labels 11–14 px mit +0,35 px als einzige Wegweiser; Navigation als Text.
4. Asymmetrisches Mosaik (groß + klein) mit Bildtiteln – das Bild ist die Karte.
5. Farblose UI aus Schwarz, Weiß und kühlem Schiefergrau; jede Farbe kommt aus dem Bild.

## Übertragung auf eine App
- Startscreen: Bühne „Weiter ansehen: Konzert im Park“ mit Zeitleiste und zwei 4-px-Buttons; darunter helles Leseband mit Rückblick als Editorial-Zeile und Quellen-/Speicherzeile, dann eine seitlich angeschnittene Bildreihe mit Versal-Bildtiteln.
- Liste und Übersicht: schwarzer Screen, Titel 40 px, dunkles Suchfeld, Versal-Reiter, Mosaik mit Overlay-Titeln, Videos mit Dauer-Etikett.
- Detail: randlose Bühne mit Pfeil zurück; helles Leseband mit Versal-Label, Titel 48 px, schwarzem Primärbutton, drei gerahmten 44-px-Icon-Buttons, Musik-Zeile, Versal-Reitern und Foto-Mosaik.
- Formulare und Einstellungen: helles Leseband, Zeilen 56 px, Label 16 px links, Wert Cool Slate rechts, Trennlinien 1 px #d0d4d4; Schalter eckig mit 4 px (Empfehlung).
- Leere Zustände und Laden: ein Standbild oder Schwarz mit einem Satz in 20 px und Textlink; Laden als Aufblenden aus Schwarz, Platzhalter #1a1a1a ohne Schimmer; keine Illustrationen.
- TV: Bühne füllt den Bildschirm, Versal-Navigation oben links, Reihen als Mosaik; Fokus = Unterstrich + 2-px-Rahmen Weiß mit 4 px Radius (Empfehlung).
- Musterscreens: Start als Video-Bühne mit hellem Rückblick-Band, Bibliothek als schwarzes Mosaik mit Overlay-Titeln, Album „Lissabon“ als Bühne mit hellem Leseband.

## Vermeiden
- Farbige UI-Elemente, Akzentfarben, Verlaufsflächen – Farbe kommt nur aus Bildern.
- Schatten, dicke Rahmen, Karten mit Fläche um Bilder; Pill-Formen und Chips.
- Gewicht 700+, zweite Schrift, Text-Zeilenhöhe über 1,5, Versalien ohne Sperrung, warme Grautöne.
- Tab-Leiste mit Icons unten, Kategorie-Icons, Illustrationen; Text, der mit dem Bild konkurriert.
- Mittelgraue Flächen (#333–#666) als Hintergrund; Bilder verkleinert in gleichförmige Raster ohne Größenwechsel.
