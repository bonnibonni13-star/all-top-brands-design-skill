---
slug: opencode.ai
marke: OpenCode AI
website: https://opencode.ai
ansatz: werkzeug
ansatz2: retro
modus: hell
aufbau: Warme Cremefläche, alles in Monospace; linksbündige Textblöcke mit 1-px-Linien, scharfe Ecken, kein Schatten
navigation: Leiste unten mit reinen Mono-Labels ohne Icons; aktiv = Label in eckigen Klammern, fett und in Ink
komponenten: Dunkler TUI-Block, ASCII-Marker [+]/[x]/[ ], Tab-Streifen mit Unterstrich, Figuren mit „fig n."-Bildunterschrift
icons: Keine Icon-Familie – ASCII-Klammern und Blockzeichen sind die Icons (laut Datei)
bewegung: Keine Animation, nur Zustandswechsel: 90 ms linear, Fläche/Unterstrich springt (Empfehlung)
schrift: Eine Monospace für alles, 400/500/700; Hierarchie nur aus Größe und Gewicht, Zeilenhöhe 1,5
---
# OpenCode AI – Designsprache

**Kurz:** Die Seite ist eine Manpage: jedes Wort steht in derselben Monospace, von der 38-px-Überschrift bis zur Fußnote. Inhalte sind linksbündige Textblöcke auf warmem Creme, getrennt durch 1-px-Linien und 96 px Luft – keine Schatten, keine Verläufe, keine Bilder. Statt Icons stehen ASCII-Klammern `[+]`, `[-]`, `[x]`; der einzige visuelle Moment je Seite ist ein dunkler Block, der ein Terminal nachbildet.

## Wirkung
- Charakter: sachlich, technisch, selbstbewusst reduziert; wirkt wie ein gut gesetztes Code-Listing, nicht wie Marketing.
- Passt zu: Entwickler- und Terminal-Werkzeugen, Dateiverwaltung, Protokollen, Open-Source-Projekten, Daten- und Status-Apps.
- Passt weniger zu: bildstarken Consumer-Apps, Marken mit Illustrationen, allem, was Wärme über Farbe oder Fotos transportiert.

## Aufbau und Raster
- Seitenaufbau: Kopfleiste 56 px mit Haarlinie unten, dann gestapelte Textblöcke; genau ein dunkler, randloser TUI-Block als Hero. Fußzeile als Linkraster mit senkrechten Haarlinien.
- Ausrichtung: alles linksbündig und bündig an der Spaltenkante – keine Einrückung, keine Zentrierung; Zahlen rechtsbündig in einer eigenen Spalte.
- Raster: Basis 8 px (fein 1/2/4), Abstände 1/4/8/12/16/24/32 px, Abschnittsabstand 96 px (Web) bzw. 24–28 px in der App; Inhalt max. 960 px, TUI-Block bis 1100 px.
- Dichte und Weißraum: Zeilen stehen dicht (Listenzeile 8 px vertikal, FAQ-Zeile 12 px), die Abschnitte dagegen weit auseinander. Nie 24 px Innenabstand in Karten – Karten gibt es nicht.
- Rhythmus: fettes Abschnitts-Label → 1-px-Linie → dichter Zeilenblock → viel Luft. Immer gleich, über die ganze Seite.

## Navigation
- Website: Kopfleiste 56 px auf Creme, links die Wortmarke als Block-Pixel-ASCII, mittig/rechts Textlinks in 16 px/500, ganz rechts der dunkle Hauptknopf; unter 768 px Hamburger, Hauptknopf bleibt sichtbar.
- App (Empfehlung, abgeleitet aus Tab-Streifen und ASCII-Markern): Leiste unten, 64 px, Creme, 1-px-Haarlinie oben, vier Ziele Start · Bibliothek · Suche · Profil als reine Mono-Labels in 13 px – keine Icons. Aktiv = Label in eckigen Klammern (`[start]`), Gewicht 700, Ink; inaktiv ohne Klammern, Gewicht 400, Mute. Darüber optional eine Tastenhinweis-Zeile in 11 px Ash wie in einem TUI.
- Oben je Screen eine 52-px-Zeile: links das Block-Pixel-Zeichen oder der Pfad, rechts ein dunkler 4-px-Knopf.
- Detailseiten: Pfadzeile statt Zurück-Pfeil – `[<] bibliothek/alben/lissabon` in 12 px Mono, aktuelles Glied in Ink.
- TV: waagerechter Tab-Streifen oben, Fokus = 2-px-Unterstrich plus Ink-Label; Listen bleiben Textzeilen mit ASCII-Marker.

## Startscreen
- Kopfzeile, dann eine fette Mono-Begrüßung in 26–28 px (Zeilenhöhe 1,5) und darunter eine Kennzahlenzeile in 13 px Mute.
- Hervorgehobener Inhalt als dunkler TUI-Block (randlos, 0 px Radius, #201d1d): Pfadzeile oben, darin eine Prompt-Zeile auf #302c2c mit 4 px Radius, darunter eine Tastenhinweis-Zeile in Ash. Text statt Bild – der Block ist die „Bühne" der Marke.
- Weitere Bereiche als Label (13 px/700) plus 1-px-Linie: eine angeschnittene Reihe Bild-Figuren mit `fig n.`-Unterschrift und ein Quellen-Block aus ASCII-Zeilen mit `[x]`/`[~]`/`[ ]`-Markern und einem Blockzeichen-Balken für den Speicher.
- Farbe erscheint ausschließlich im dunklen Block (Blau für den Befehl, Grün für Erfolg); die helle Fläche bleibt monochrom.

## Komponenten
- Buttons: 4 px Radius, Mono 15–16 px/500, Zeilenhöhe 2, Padding 4 × 20 px, Höhe 36–40 px. Primär: Ink-Fläche, cremefarbene Schrift, gedrückt #0f0000. Sekundär: Creme mit 1 px #646262. Nie Pill, nie farbig, kein Schatten.
- Karten und Kacheln: es gibt keine erhobenen Karten. „Kacheln" sind Figuren: scharfkantiges Bild (0 px Radius) mit 1-px-Haarlinie und einer Mono-Unterschrift `fig n. <name>` darunter; Abschnitte sind reine Textblöcke zwischen 1-px-Linien.
- Listen: Zeilen 8–12 px vertikal, beginnend mit einem ASCII-Marker `[+]`/`[-]`/`[x]`, dann fettes Label, dann Beschreibung in Body; Zahlen rechtsbündig in Mute. Trenner nur 1 px Haarlinie, oft gar keiner.
- Suche und Eingabefelder: Fläche #f8f7f7, 1 px Haarlinie, 4 px Radius, Padding 8 × 12 px, Höhe 40–44 px; Fokus: Fläche wird Creme, Rahmen 1 px Ink – kein Ring, kein Leuchten. Platzhalter als Prompt mit führendem `>`.
- Chips, Tabs, Filter: Tab-Streifen ohne Flächen – Labels in Mute, aktiv Ink mit 2-px-Unterstrich in Ash, darunter eine durchgehende 1-px-Linie in #646262. Badges: kleine dunkle Chips (Ink-Fläche, 4 px Radius, 14 px) oder Zahlen in eckigen Klammern `[342]`.
- Dialoge und Sheets: scharfkantige Blöcke auf Creme mit 1-px-Rahmen, Titelzeile fett, Aktionen als zwei Knöpfe unten rechts; kein Schatten, kein abgerundetes Sheet.
- Signatur-Komponenten: dunkler TUI-Block mit Prompt-Zeile und Tastenhinweisen; ASCII-Marker als Aufzählung; Block-Pixel-Zeichen; ASCII-Balken und -Diagramme (`████░░░░`) mit `fig n.`-Unterschrift.

## Icons
- Stil: keine Icon-Familie. Die Marke setzt ASCII-Zeichen als Icons ein – `[+]` hinzufügen/Merkmal, `[-]` entfernen, `[x]` erledigt, `[ ]` offen, `[~]` läuft, `[<]`/`[>]` Richtung, `[*]` Favorit, `[…]` mehr, `│` als Prompt-Strich. Sie sind Textinhalt, nicht Grafik.
- Größe und Strich: dieselbe Schriftgröße wie die Zeile (13–16 px), Mute im Normalfall, Ink bei Betonung; nie vergrößert, nie eingefärbt.
- Einsatz: immer am Zeilenanfang, in einer festen Spalte (3 Zeichen breit), damit alle Zeilen fluchten. Wenn eine echte Icon-Familie unvermeidbar ist (Empfehlung): eckige Linien-Icons, 16 px, Strich 1,5, `stroke-linecap: square` – sparsam und nur dort, wo ASCII unverständlich wäre.
- Umsetzung: Compose/iOS/Web gleichermaßen als `Text`-Glyphen in der Monospace setzen; falls doch Vektoren nötig sind, Material Symbols Sharp (Gewicht 400, Füllung 0) bzw. Lucide mit `stroke-linejoin: miter`.

## Bildsprache
- Laut Datei: keine Fotografie, keine Illustration. Visuelle Elemente sind Block-Pixel-ASCII, dünne ASCII-Diagramme und 32-px-Avatarkreise – alles Typografie.
- Übertragung (Empfehlung, da die App Medien zeigen muss): Bilder werden wie Abbildungen in einem Handbuch behandelt – scharfe Ecken (0 px Radius), 1-px-Haarlinie, keine Überlagerung, kein Text im Bild, kein Verlauf; darunter eine Mono-Unterschrift `fig 3. herbstwald · 86 fotos` in 11 px Mute. Raster mit 2–4 px Fugen, Seitenverhältnisse 4:3 und 1:1. Leichte Dämpfung (`saturate(.9)`) hält die Bilder neben der monochromen Fläche ruhig.
- Avatare bleiben die einzige runde Form im System (voller Radius, 28–32 px).

## Typografie-Stimme
- Eine einzige Monospace für alles – Überschrift, Text, Zahlen, Labels, Fußnoten. Kein Serif, kein Sans, kein Kursiv. Das ist die Marke.
- Gewichte 400 / 500 / 700; Hierarchie entsteht aus Größe und Gewicht: Display 38 px/700 (mobil 26–28), Abschnittslabel 16 px/700, Text 16 px/400, Betonung 500, Caption 14 px/400.
- Zeilenhöhe 1,5 für Text und Überschriften, 2,0 für Knopf- und Caption-Zeilen, 1,0 nur für kompakte Labels. Laufweite immer 0.
- Strukturelle Labels (Navigation, Abschnitte, Status, Pfade) klein geschrieben wie in einer Shell; Inhaltsnamen normal.
- Zahlen stehen in Spalten – Monospace liefert Tabellenziffern von selbst; Mengen gern in eckigen Klammern `[342]`.
- Freier Ersatz: JetBrains Mono (nächste Metrik), IBM Plex Mono oder Geist Mono, Gewichte 400/500/700.

## Form, Tiefe und Material
- Radien: 0 px für alles, was kein Bedienelement ist (Blöcke, Bilder, Leisten, TUI-Block); 4 px für jedes Bedienelement (Knopf, Feld, Badge, Prompt-Zeile); voll nur für Avatare.
- Linien und Rahmen: 1 px `rgba(15,0,0,0.12)` als Standardtrenner, 1 px #646262 als starke Linie (Tab-Streifen, Sekundärknopf), 2 px Ash als aktiver Unterstrich.
- Schatten und Ebenen: keine. Nichts schwebt. Die einzige „Erhebung" ist die dunkle Fläche #201d1d, darin eine Stufe #302c2c.
- Besondere Oberflächen: keine Verläufe, kein Glas, keine Körnung. Textur entsteht durch Zeichendichte – Blockzeichen (`█ ░ ─ │ ┼`), Klammern und ausgerichtete Spalten.

## Bewegung
- Laut Datei: keine Angaben; Hover-Zustände sind bewusst nicht dokumentiert, nur Default und Gedrückt.
- Empfehlung: keine Ein- oder Ausblendanimation. Zustände springen in 90 ms linear (Fläche Ink → #0f0000, Feldrahmen auf Ink, Unterstrich wechselt). Screenwechsel ohne Bewegung oder als 120-ms-Überblendung; Ladezustand als laufender ASCII-Spinner (`|/-\`) oder als Balken aus Blockzeichen – nie als Schimmer. Fokus (TV): 2-px-Unterstrich erscheint ohne Übergang.
- Compose: `tween(90, easing = LinearEasing)`, Zustände über `Modifier.background`-Wechsel; kein `spring`, kein `AnimatedVisibility` mit Slide, keine Shared-Element-Übergänge.

## Signatur-Elemente
1. Alles in einer Monospace – auch Überschriften und Zahlen; kein zweiter Schriftschnitt im ganzen Produkt.
2. ASCII-Klammern statt Icons, in einer festen Zeichenspalte ausgerichtet.
3. Genau ein dunkler, randloser TUI-Block je Screen mit Prompt-Zeile und Tastenhinweisen – der einzige Ort für Farbe.
4. Scharfe Ecken überall, 4 px nur für Bedienelemente; Trennung ausschließlich über 1-px-Linien.
5. Bilder als nummerierte Abbildungen mit `fig n.`-Unterschrift; Balken und Diagramme aus Blockzeichen.

## Übertragung auf eine App
- Startscreen: fette Mono-Begrüßung, dunkler TUI-Block als Rückblick (Pfad, Prompt-Zeile, Tastenhinweise), darunter Label + Linie je Bereich: angeschnittene Figuren-Reihe „zuletzt hinzugefügt", Quellen als ASCII-Zeilen mit Markern und Blockzeichen-Balken für den Speicher.
- Liste und Übersicht: Prompt-Suchfeld, Tab-Streifen mit Unterstrich, dann ein zweispaltiges Figuren-Raster – scharfe Bilder mit Haarlinie und `fig n.`-Unterschrift plus Mengen in eckigen Klammern; die letzte Reihe darf angeschnitten sein.
- Detail: Pfadzeile statt Zurück-Pfeil, fetter Titel, Metazeile, großes Bild als `fig 1.` mit Unterschrift, dunkler Primärknopf plus zwei Sekundärknöpfe mit ASCII-Glyphen, Tab-Streifen mit `[342]`-Mengen, dichtes Fotoraster mit 2-px-Fugen, unten eine dunkle Prompt-Leiste für die Musik.
- Formulare und Einstellungen: Label über dem Feld, Felder #f8f7f7 mit 4 px Radius und 1-px-Linie, Schalter als `[x]`/`[ ]`, Aktionen unten als Ink-Knopf plus Sekundärknopf.
- Leere Zustände und Laden: eine Zeile Mono-Text mit Marker (`[ ] keine einträge`), darunter ein Sekundärknopf; Laden als ASCII-Spinner oder Blockzeichen-Balken, nie als Platzhalter-Schimmer.
- TV: Tab-Streifen oben, Figuren-Raster, Fokus als 2-px-Unterstrich und Ink-Label.
- Musterscreens: Start mit Mono-Begrüßung, dunklem TUI-Rückblick, Figuren-Reihe und Quellen-Block; Bibliothek als Figuren-Raster unter Prompt-Suche und Tab-Streifen; Detail „Lissabon" mit Pfadzeile, großer Abbildung, Ink-Knopf und dunkler Musikleiste.

## Vermeiden
- Eine zweite Schriftfamilie, Kursive, Versal-Sperrung oder proportionale Zahlen – die Monoschrift trägt alles.
- ASCII-Marker durch SVG-Icons ersetzen; Icons einfärben oder vergrößern.
- Schatten, Verläufe, Glas, abgerundete Karten (über 4 px), graue Abschnittsbänder auf der Creme-Fläche.
- Die Semantikfarben (Blau, Rot, Orange, Grün) auf hellen Flächen oder für Hauptaktionen benutzen – sie gehören in den dunklen TUI-Block.
- Mehr als einen dunklen Block je Screen; die dunkle Fläche als Karten- oder Leistenmaterial zweckentfremden.
- Karten mit 24 px Innenabstand, zentrierte Textblöcke, Bilder mit Verlaufsschleier oder Text darauf.
- Unterschied zu anderen minimalen Entwicklermarken (z. B. Resend): OpenCode ist helles Papier mit durchgehendem Mono-Raster, scharfen Ecken und ASCII-Markern – nicht schwarze Fläche mit redaktioneller Serife, Glühen und weißem Akzent.
