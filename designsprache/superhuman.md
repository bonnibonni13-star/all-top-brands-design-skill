---
slug: superhuman
marke: Superhuman
website: https://superhuman.com
ansatz: editorial
ansatz2: buehne
modus: gemischt
aufbau: Drei Leinwände nacheinander – Indigo-Bühne oben, ruhige weiße Mitte, dunkles Petrol als Schlussakkord
navigation: Oben eine Leiste mit drei Zielen (aktiv unterstrichen) und Avatar für Profil; keine Leiste unten
komponenten: Halb angeschnittenes Porträt, Violett-Pille (nur im Hero), 8-px-Rechteckbutton, Petrol-Abschlussband
icons: Phosphor Light 20–22 px, dünne Linien, nie gefüllt, sparsam eingesetzt
bewegung: Empfehlung – langsam und ruhig, 180/320 ms, cubic-bezier(.22,1,.36,1), sanftes Heraufblenden
schrift: Zwischen-Gewichte 460/540, Display mit Zeilenhöhe 0.96 und negativer Laufweite; Fließtext warmes Grau
---
# Superhuman – Designsprache

**Kurz:** Eine Seite besteht aus genau drei Leinwänden: eine dunkle Indigo-Bühne mit atmosphärischem Violett-Himmel und einem halb angeschnittenen Porträt, ein stiller weißer Mittelteil mit warmem Grau, und ein dunkles Petrol-Band als Abschluss. Pro Band gibt es **eine** Aktion. Die Typografie trägt alles: Zwischen-Gewichte (460/540), Zeilenhöhe 0.96 im Display und negative Laufweite – das wirkt eher wie ein hochwertiger Newsletter als wie eine SaaS-Oberfläche.

## Wirkung
- Charakter: ruhig, erwachsen, editorial; langsames Tempo, viel Luft, nichts drängt.
- Passt zu: Lese- und Produktivitäts-Apps, Journalen, Rückblicken, kuratierten Medien-Sammlungen, Premium-Abos.
- Passt weniger zu: dichten Datenoberflächen, verspielten Apps, allem mit vielen gleichzeitigen Aktionen.

## Aufbau und Raster
- Seitenaufbau: Bänder mit klarer Rollenverteilung – Indigo-Bühne (Einstieg) → Weiß (Inhalt) → Petrol (Abschluss). Eine vierte Leinwandfarbe bricht das System.
- Ausrichtung: links; im Hero steht der Text links, das Bild schneidet rechts halb an.
- Raster: 8-px-Basis mit 2/4/12 für Feinarbeit; Abschnittspolster 64–96 px (App: 24–32 px), Abschlussband 96–128 px (App: 24 px innen).
- Dichte und Weißraum: großzügig auf beiden Polen; Karten 32 px innen, Wechselzeilen 24 px, Zeilenabstand im Fließtext 1.5.
- Rhythmus: große Zeile – kleine Zeile – eine Aktion – Pause. Danach erst der nächste Block.

## Navigation
- Website: 16×24-px-Leiste, Logo links, Links mittig, rechts eine Aktion. Über dem Indigo-Hero dunkel (`nav-bar-dark`), auf hellen Seiten weiß (`nav-bar-light`). Unter 768 px Hamburger.
- App (App-Muster abgeleitet, Empfehlung): **oben** eine Leiste mit drei Zielen (Start, Bibliothek, Suche) als Textlinks in 15 px/460; aktiv = weiß bzw. Ink plus 2-px-Unterstrich in Violett-Soft (dunkel) bzw. Indigo (hell). Profil steckt im Avatar rechts. Keine Leiste unten – die Marke hält den unteren Rand für den Abschluss frei. Auf Detailseiten ersetzt ein Zurück-Pfeil die Ziele.
- TV: Ziele oben als Textreihe, Fokus durch Unterstrich und Aufhellung der Leinwand, keine Rahmen.

## Startscreen
- Indigo-Bühne über etwa 40 % der Höhe: Violett-Himmel als weicher Radialverlauf, rechts halb angeschnittenes Porträt, das links in die Leinwand ausblendet.
- Links Mikro-Zeile (12 px/540), Display-Zeile (32–40 px/540, Zeilenhöhe 0.96, Laufweite -1.1 px; die Spalte ist schmal, der Titel darf drei Zeilen hoch stapeln), eine Caption-Zeile in gedämpftem Hellgrau – und **eine** Violett-Pille als Aktion.
- Weißer Mittelteil: eine Überschrift in 20 px/540, darunter abwechselnde Inhaltszeilen auf #fafaf8 mit 8-px-Ecken.
- Unten das Petrol-Band mit Kennzahl, feinem Balken und einem weißen 8-px-Button.

## Komponenten
- Buttons: Standard ist das **Rechteck mit 8 px** – Indigo #1b1938 auf Weiß, Text 16 px/700, Polster 12×20 px. Im Petrol-Band weiß mit petrolfarbenem Text. Umriss-Variante weiß mit 1 px #3f3a52. **Pille ausschließlich im Hero**, gefüllt in Violett-Soft #c9b4fa mit Indigo-Text.
- Karten und Kacheln: weiß oder #fafaf8, Radius 12 px (Wechselzeilen 8 px), 1 px #e8e4dd, Polster 32 px bzw. 24 px; Schatten höchstens `0 1px 3px rgba(0,0,0,.08)`.
- Listen: editorial statt tabellarisch – Titel 22 px/460 mit -0.3 px, Meta 14 px in #73706d, 1-px-Haarlinie als Trenner, Bild links mit 8-px-Ecken, viel Luft (Zeilenhöhe ≥ 72 px).
- Suche und Eingabefelder: weiß, Radius 6 px, 1 px #e8e4dd, Polster 10×12 px, Text 16 px/460; Mindesthöhe 44 px.
- Chips, Tabs, Filter: `pill-tab-light` – weiße Pille mit Haarlinie, Beschriftung 14 px/600; aktiv gefüllt in Indigo mit weißem Text (Empfehlung, Datei nennt nur den Ruhezustand).
- Dialoge und Sheets: weiß, Radius 16 px, Schatten `0 8px 24px rgba(0,0,0,.12)`, eine Aktion unten, Abbrechen als Textlink.
- Signatur-Komponenten: halb angeschnittenes Porträt im Hero, Violett-Pille, Petrol-Abschlussband, invertierte Indigo-Karte für das hervorgehobene Angebot.

## Icons
- Stil: sehr feine, gleichmäßige Linien ohne Füllung; Icons sind Beiwerk, die Schrift führt. Phosphor Light trifft die Stimmung.
- Größe und Strich: 20–22 px in Leisten und Aktionen, 18 px in Zeilen; Strich ≈1 px bei 20 px, runde Enden.
- Einsatz: höchstens zwei Icons je Band; Nebenaktionen (Teilen, Favorit, Mehr) liegen in der oberen Leiste, nicht neben der Hauptaktion.
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Outlined, Gewicht 200–300, Füllung 0; iOS SF Symbols Light/Ultralight; Web Phosphor `light` oder Lucide `stroke-width: 1.25`.

## Bildsprache
- Leitmotiv ist das **halb angeschnittene Bild**: es füllt die rechte Hälfte des dunklen Bandes randlos von oben nach unten und blendet links weich in die Leinwand aus. Technisch als Maske (`mask-image: linear-gradient(90deg, transparent, #000 62%)`) plus leichtem Indigo-Schleier – ein harter Verlauf **auf** dem Bild erzeugt sonst eine sichtbare Kante gegen den Himmel.
- Dahinter der atmosphärische Violett-Himmel als weicher Radialverlauf – die einzige Tiefe der Marke.
- Im hellen Teil sind Bilder sachlich: 8-px-Ecken, 1:1 oder 4:3, keine Verläufe, kein Text darauf.
- Fotoraster 3-up mit 12 px Abstand – luftiger als bei Werkzeugmarken.
- Keine Farbfilter, keine Körnung, keine runden Bildmasken außer dem Avatar.

## Typografie-Stimme
- Eine Familie (Super Sans VF; Ersatz: Inter Variable) in **Zwischen-Gewichten**: 460 statt 400/500, 540 statt 600, 700 nur für Buttons und betonte Inline-Stellen.
- Display 64/48/28/22 px mit Zeilenhöhe 0.96–1.14 und Laufweite -1.32 bis -0.315 px – gestapelt und dicht.
- Fließtext 16 px/460 mit 1.5; Lead 18 px/540; Caption 14 px/460; Mikro 12 px/540.
- Textfarbe ist warmes Dunkelgrau #292827, **nie reines Schwarz**; sekundär #73706d, tertiär #9a9794.
- Keine Versalien-Blöcke außer der 12-px-Mikro-Zeile; keine Kursive.
- Freier Ersatz: Inter Variable mit `font-variation-settings: "wght" 460/540`; ohne variable Schnitte 500/600 verwenden.

## Form, Tiefe und Material
- Radien: 4 px Tags, 6 px Eingabefelder, **8 px Buttons und Wechselzeilen**, 12 px Karten, 16 px Dialoge, 9999 px nur Hero-Pille und Avatar.
- Linien und Rahmen: 1 px #e8e4dd auf Hell (warmes Grau, kein Neutralgrau), 1 px #3f3a52 auf Dunkel.
- Schatten und Ebenen: Stufe 1 `0 1px 3px rgba(0,0,0,.08)`, Stufe 2 `0 8px 24px rgba(0,0,0,.12)`; die eigentliche Tiefe ist der atmosphärische Hintergrund, nicht der Schatten.
- Besondere Oberflächen: Violett-Himmel über Indigo; Petrol #0e3030 mit leicht gehobenem #155555 für eingebettete Elemente.

## Bewegung
- Laut Datei: keine Angaben (nur Pressed-Zustände).
- Empfehlung: klein 180 ms / Screenwechsel 320 ms, Easing `cubic-bezier(.22, 1, .36, 1)`. Druck = Farbe eine Stufe tiefer (#1b1938 → #0e0c1f), kein Skalieren. Einblenden: 10 px herauf plus Deckkraft, 70 ms Staffelung – das Tempo ist bewusst langsam. Screenwechsel: Überblenden mit leichter Vertikalbewegung. Fokus (TV): Unterstrich wächst von der Mitte in 180 ms.
- Compose: `tween(320, easing = CubicBezierEasing(.22f, 1f, .36f, 1f))`, `AnimatedVisibility` mit `fadeIn() + slideInVertically { 24 }`, Shared-Element-Übergang vom Listenbild zum Hero-Bild.

## Signatur-Elemente
1. Drei Leinwände in fester Reihenfolge: Indigo → Weiß → Petrol.
2. Halb angeschnittenes Bild rechts im dunklen Hero, links die dicht gestapelte Display-Zeile.
3. Violett-Soft-Pille als einzige Aktion des Hero – überall sonst 8-px-Rechtecke.
4. Petrol-Abschlussband mit genau einer weißen Schaltfläche.
5. Warmes Dunkelgrau statt Schwarz und Zwischen-Gewichte in der ganzen Hierarchie.

## Übertragung auf eine App
- Startscreen: Indigo-Bühne mit Begrüßungs-Mikrozeile, dem Rückblick als Display-Zeile, Porträt rechts und einer Violett-Pille; darunter weiße Wechselzeilen „Zuletzt hinzugefügt“; unten das Petrol-Band mit Speicherstand und einem weißen Button.
- Liste und Übersicht: weiße Seite, Display-Titel, Suchfeld, Pillen-Filter, danach großzügige Zeilen mit Bild links, 22-px-Titel und Haarlinien-Trennern – keine Kacheln, kein Raster.
- Detail: dunkle Bühne mit halb angeschnittenem Albumbild, Titel und einer Pille „Diashow starten“; Nebenaktionen oben in der Leiste; darunter Pillen-Umschalter und ein luftiges 3-up-Raster; Abschluss als Petrol-Band mit der Diashow-Musik.
- Formulare und Einstellungen: weiße Fläche, Beschriftung 14 px in #73706d über dem Feld, Felder mit 6-px-Ecken, eine Indigo-Schaltfläche unten rechts; Abschnitte durch Haarlinien getrennt.
- Leere Zustände und Laden: große ruhige Zeile in 28 px/540, ein Satz in #73706d, **eine** Schaltfläche; Ladeplatzhalter als #fafaf8-Blöcke ohne Schimmern.
- TV: Indigo-Bühne mit halb angeschnittenem Bild, Textreihe oben, Fokus als Unterstrich; Abschlussband bleibt unten stehen.
- Musterscreens: Start mit Indigo-Bühne, Porträt und Petrol-Abschluss; Bibliothek als helle, editoriale Zeilenliste mit Pillen-Filtern; Detail „Lissabon“ mit halb angeschnittenem Bild, Violett-Pille und Petrol-Band für die Diashow-Musik.

## Vermeiden
- Keine Pillen-Buttons außerhalb des Hero – im Inhalt sind es 8-px-Rechtecke.
- Keine zwei Hauptaktionen in einem Band; die zweite Aktion wird ein unterstrichener Textlink.
- Reines Schwarz für Text vermeiden – #292827 ist Teil der Marke.
- Das Petrol-Abschlussband nicht weglassen und nicht durch eine weitere Farbe ersetzen.
- Display-Gewicht nicht über 540 treiben; 700 bleibt Buttons und betonten Inline-Stellen vorbehalten.
- Zeilenhöhe 0.96 nur im Display verwenden – im Fließtext bleibt es bei 1.5.
- Keine zusätzlichen Akzentfarben neben Indigo, Violett-Soft, Petrol und den warmen Grautönen.
