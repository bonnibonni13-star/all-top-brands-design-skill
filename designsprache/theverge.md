---
slug: theverge
marke: The Verge
website: https://www.theverge.com
ansatz: plakativ
ansatz2: editorial
modus: dunkel
aufbau: Fast schwarze Fläche, riesige schmale Versal-Headline oben, darunter Zeitstrahl und gesättigte Farbblock-Kacheln
navigation: Unten vier Ziele nur als Mono-Versal-Text, aktiv mit 1-px-Minz-Unterstrich (Empfehlung aus der Web-Navigation)
komponenten: Pillen-Karten (20/24 px) mit 1-px-Haarlinie, Farbblock-Kacheln, Zeitstrahl mit Mono-Zeitstempel, 2-px-Eingaben
icons: Lucide-Linien, eckige Enden, 1,75 px Strich, 18–20 px, nie gefüllt, nie in der Navigation (Empfehlung)
bewegung: Keine Bewegung außer Farbe: 150–180 ms ease auf Farbe und Rahmen, kein Heben, kein Skalieren
schrift: Schmale schwere Display-Versalien gegen dünne 300er-Flüster-Zeilen; alle Labels Mono-Versal mit 1,5 px Laufweite
---
# The Verge – Designsprache

**Kurz:** Ein Magazin, das wie eine Konsole gebaut ist: fast schwarze Fläche (`#131313`), eine brutal schwere, schmale Display-Schrift über alles, und zwei Signalfarben – Säure-Minze (`#3cffd0`) und Ultraviolett (`#5200ff`) – die wie Absperrband eingesetzt werden. Tiefe entsteht nie durch Schatten, sondern durch 1-px-Haarlinien und vollflächige Farbblöcke. Jedes kleine Label steht in Mono-Versalien mit weiter Laufweite.

## Wirkung
- Charakter: laut, redaktionell, technisch; zwischen Clubflyer und Entwicklerkonsole – ernst genug für Nachrichten, laut genug für Besprechungen.
- Passt zu: Nachrichten-, Magazin-, Feed-, Release- und Community-Apps, Medienarchiven mit Chronologie.
- Passt weniger zu: ruhigen Produktiv-Werkzeugen, hellen Shop-Oberflächen, Finanz- und Gesundheits-Apps.

## Aufbau und Raster
- Seitenaufbau: Kopf mit riesiger Display-Zeile → ein gesättigter Farbblock als Aufmacher → vertikaler Zeitstrahl („StoryStream“) aus Pillen-Karten, immer wieder von vollflächigen Farbkacheln unterbrochen.
- Ausrichtung: linksbündig, Zeitstempel in einer schmalen linken Spalte am Strahl; Inhalte brechen bewusst aus dem Raster aus.
- Raster: Basis 8 px (2/4/5/6/9/10/12/16/20/24/25 px), Rand 24 px mobil / 48 px Desktop, 12 Spalten, Inhalt max. 1280–1300 px; Kacheln dürfen 2–3 Spalten überspannen.
- Dichte und Weißraum: Abschnitte 32–64 px auseinander, Zeitstrahl-Einträge nur 12–16 px; Karteninnenabstand 20–32 px, Feature-Karten 40–48 px. Schwarz zwischen zwei Farbblöcken ist die Pause.
- Rhythmus: laut – still – laut. Pro Bildschirm höchstens zwei gesättigte Blöcke, sonst kippt das Absperrband-Prinzip.

## Navigation
- Website: schmale Leiste mit riesigem Schriftzug links, Mono-Versal-Kategorien, rechts eine Minz-Pille; aktive Kategorie bekommt einen 1-px-Minz-Unterstrich (`inset 0 -1px 0 0 #3cffd0`), Links wechseln beim Überfahren auf Blau (`#3860be`). Mobil klappt alles in eine Schublade.
- App: untere Leiste, `#131313`, 64 px, 1-px-Haarlinie oben, vier Ziele **nur als Mono-Versal-Text** (10–11 px, 1,5 px Laufweite) ohne Icons; aktiv = Weiß plus 1-px-Minz-Unterstrich, inaktiv `#949494` (Empfehlung, übertragen aus der Web-Navigation).
- TV: Empfehlung – horizontale Mono-Versal-Leiste oben; Fokus als 1-px-Minz-Rahmen um die Kachel plus Wechsel der Kachelfüllung auf Minze, nie Vergrößerung.

## Startscreen
- Oben eine Flüsterzeile (19/300, 1,9 px Laufweite) über zwei Zeilen Display-Versalien (58–68 px, Zeilenhöhe 0,88) – der Kontrast zwischen Flüstern und Schreien ist die Stimme.
- Darunter eine Mono-Zeile mit Kennzahlen, getrennt durch minzfarbene Schrägstriche.
- Dann der Aufmacher als vollflächiger Minz-Block mit schwarzer Schrift, Bild innen mit kleinerem Radius und schwarzer Pille.
- Danach der Zeitstrahl: 1-px-Linie in Violett, Mono-Zeitstempel links, Pillen-Karten rechts.

## Komponenten
- Buttons: Minz-Pille (`#3cffd0`, schwarzer Mono-Versal-Text, Radius 24 px, 10×24 px) als Hauptaktion; Schiefer-Pille (`#2d2d2d`, Text `#e9e9e9`) als zweite; Umriss-Pille 1 px Minze, Radius 40 px, für ruhige Aktionen. Druck: Fläche wird grau-transluzent, kein Skalieren.
- Karten und Kacheln: entweder `#131313` mit 1-px-weißer Haarlinie oder vollflächig gesättigt (Minze, Ultraviolett, Weiß; laut Datei zusätzlich Gelb, Pink, Orange – ohne Hex-Werte, daher frei zu wählen). Radius 20 px, Feature 24 px, Innenabstand 20–32 px.
- Listen: keine klassische Liste, sondern ein Zeitstrahl – 1-px-Linie (`#3d00bf` oder Weiß) als Rückgrat, Mono-Zeitstempel in der linken Spalte, je Eintrag eine Pillen-Karte mit Kicker, Schlagzeile und optionalem Vorschaubild (4 px Radius).
- Suche und Eingabefelder: bewusst hart – 2 px Radius, 1-px-Rahmen Weiß oder `#949494`, Platzhalter in Mono-Versalien; Fokus färbt den Rahmen minzfarben, Fehler ultraviolett. Kein Glühen.
- Chips, Tabs, Filter: Pillen-Tags (Radius 20–40 px) in Mono-Versalien 11 px mit 1,8 px Laufweite; aktiv = Minze gefüllt mit schwarzem Text, inaktiv = 1-px-Rahmen in `#949494`. Seiten-Tabs stattdessen mit 1-px-Minz-Unterstrich.
- Dialoge und Sheets: `#131313` mit 1-px-weißer Haarlinie, Radius 24 px, Mono-Versal-Kopfzeile; kein abgedunkelter Verlauf, nur eine Fläche mit `rgba(0,0,0,.33)`-Ring.
- Signatur-Komponenten: Zeitstrahl mit Mono-Zeitstempeln; vollflächige Farbblock-Kachel als „Hervorhebung ohne Schatten“; der 1-px-Unterstrich als aktiver Zustand.
- Widerspruch in der Datei: Der Fließtext verbietet minzfarbenen Text unter 16 px auf Schwarz, der Komponenten-Abschnitt zeigt aber 11–12-px-Minz-Kicker. Entscheidung: Komponenten-Abschnitt gilt, Minz-Labels aber nie unter 10,5 px und immer fett mit weiter Laufweite.

## Icons
- Stil: nüchterne Linien-Icons mit eckigen Enden, nie gefüllt, nie dekorativ; Icons tragen keine Bedeutung, die der Text nicht schon trägt (Empfehlung – die Datei nennt nur Lupe und Einkaufs-Glyphen).
- Größe und Strich: 18–20 px bei 1,75 px Strich, in runden 40–44-px-Knöpfen mit 1-px-Rahmen; in Pillen 16 px.
- Einsatz: nur für Aktionen (Zurück, Suche, Abspielen, Teilen, Favorit, Mehr) – die Navigation bleibt reiner Text.
- Umsetzung: Compose `Icons.Sharp` bzw. Material Symbols Sharp, Gewicht 400, Fill 0; iOS SF Symbols Regular ohne `.fill`; Web Lucide mit `stroke-width:1.75` und `stroke-linecap:square`.

## Bildsprache
- Bilder sind nie randlos auf der Seite: sie sitzen in Kacheln, bekommen den inneren Radius (3–4 px) oder den Kachelradius (20 px) und eine 1-px-Haarlinie (`#313131` oder Weiß) – wie ein gerahmtes Polaroid.
- Seitenverhältnisse 16:9 (Aufmacher), 4:3 (Feed), 1:1 (Vorschau und Avatare).
- Keine Verläufe, keine Abdunklung, kein Zoom beim Überfahren – das Bild bleibt still, nur die Schlagzeile reagiert mit Farbe.
- In Farbblock-Kacheln läuft das Bild bis an den Innenrand des Blocks; die Kachelfarbe bleibt sichtbarer Rahmen.

## Typografie-Stimme
- Zwei Register: eine schmale, sehr schwere Display-Schrift ausschließlich groß (Versalien, 50–107 px, Zeilenhöhe 0,80–0,92, Laufweite ~1 px) und eine neutrale Grotesk für alles andere (34/700, 24/700, 20/700, 16/500 Zeilenhöhe 1,6).
- Dritter Ton: Mono, immer Versalien, nie klein geschrieben – Kicker, Zeitstempel, Tags, Knopftexte, 10–12 px mit 1,1–1,8 px Laufweite.
- Signatur: dünne 300er-Zeilen bei 19–20 px mit 1,9 px Laufweite als „Flüstern“ direkt über oder unter dem Display-Schrei.
- Serif bleibt redaktionellen Auszügen vorbehalten (16/400, Laufweite −0,16 px) und taucht nie in der Oberfläche auf.
- Freier Ersatz: Archivo Black, Anton oder Oswald (Display – Zeilenhöhe um 0,10–0,15 lockern), Space Grotesk oder DM Sans (Grotesk), Space Mono oder JetBrains Mono (Mono), Newsreader (Serif).

## Form, Tiefe und Material
- Radien: 2 px Eingaben und Tags, 3–4 px Bilder in Karten, 20 px Standardkachel, 24 px Feature und Hauptpille, 30 px Werbepille, 40 px Umriss-Pille, 50 % Icon-Knöpfe – die Staffel ist Teil der Hierarchie.
- Linien und Rahmen: 1 px in Weiß, `#313131`, Minze oder Ultraviolett – sie ersetzen jeden Schatten.
- Schatten und Ebenen: keine. Erlaubt sind nur der 1-px-Innenunterstrich (aktiver Zustand) und ein `rgba(0,0,0,.33) 0 0 0 1px`-Ring.
- Besondere Oberflächen: keine Verläufe, kein Glas, kein Blur. Hervorhebung ist immer eine vollflächige, gesättigte Farbe.

## Bewegung
- Laut Datei: 150–180 ms ease auf Hintergrund, Rahmenfarbe und Schriftfarbe; Links wechseln auf `#3860be`; Kacheln heben sich beim Überfahren **nicht**, es ändert sich nur die Schlagzeilenfarbe.
- Empfehlung: Dauer klein 150 ms / Screenwechsel 200 ms, Easing `cubic-bezier(.2,0,0,1)`, Druck-Effekt nur Farbwechsel (Fläche grau-transluzent), Einblenden als hartes Erscheinen mit 30-ms-Staffel ohne Verschiebung, Fokus (TV) 1-px-Minz-Rahmen.
- Compose: `tween(150, easing = CubicBezierEasing(.2f,0f,0f,1f))` auf `animateColorAsState`, kein `scale`, kein `elevation`; Listen mit `animateItem()` ohne Versatz.

## Signatur-Elemente
1. Riesige schmale Versal-Display-Zeile über einer dünnen, weit gesperrten Flüsterzeile.
2. Zeitstrahl mit 1-px-Rückgrat und Mono-Versal-Zeitstempeln in der linken Spalte.
3. Vollflächig gesättigte Farbblock-Kacheln (Minze, Ultraviolett, Weiß) als einzige Form von Hervorhebung.
4. 1-px-Haarlinien statt Schatten – auch um Bilder.
5. Mono-Versal-Labels mit 1,5–1,8 px Laufweite, inklusive der Navigation, die nur aus Text besteht.

## Übertragung auf eine App
- Startscreen: Flüsterzeile plus zweizeilige Display-Überschrift, Mono-Kennzahlen, ein Minz-Block als Aufmacher, darunter der Zeitstrahl mit zwei bis drei Einträgen.
- Liste und Übersicht: zweispaltige Collage aus umrandeten Bildkacheln und vollflächigen Farbblöcken, davor harte 2-px-Suche und Pillen-Filter; eine Kachel pro Screen darf weiß sein („Spotlight“).
- Detail: gerahmtes Bild, Mono-Kicker, Display-Titel, Minz-Pille als Hauptaktion, Mono-Tabs mit Minz-Unterstrich, Bildraster mit 4-px-Radius, unten ein ultravioletter Block für die begleitende Musik.
- Formulare und Einstellungen: 2-px-Felder mit Mono-Versal-Labels, Schalter als Pillen, Fehler in Ultraviolett statt Rot.
- Leere Zustände und Laden: `#131313` mit 1-px-Rahmen und einer Mono-Versal-Zeile; Laden als Haarlinien-Rahmen ohne Füllung, kein Schimmern.
- TV: gleiche Kacheln, größere Display-Zeile; Fokus als Minz-Rahmen plus Wechsel der Füllung, Zeitstempel bleiben Mono.
- Musterscreens: Start mit Display-Kopf, Minz-Aufmacher und Zeitstrahl; Bibliothek als Farbblock-Collage mit Pillen-Filtern; Detail mit gerahmtem Bild, Minz-Pille und ultraviolettem Musikblock.

## Vermeiden
- Helle Flächen, Schatten, Verläufe, Glühen, Weichzeichner – alles davon bricht die Haltung.
- Eckige Karten und Knöpfe; jede Fläche gehört auf eine Stufe der Radienstaffel.
- Display-Schrift klein (unter ~50 px) oder in Knöpfen; Mono in Kleinbuchstaben; Versal-Labels ohne Laufweite.
- Minze oder Ultraviolett als großflächige Hintergrundtönung oder als Textfarbe unter 16 px auf Schwarz.
- Weitere Akzentfarben erfinden oder Serif in die Oberfläche holen.
