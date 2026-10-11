---
slug: wise
marke: Wise
website: https://wise.com
ansatz: plakativ
ansatz2: daten
modus: hell
aufbau: Salbeigrüne Fläche, darauf weiße 24-px-Blöcke; linksbündige Schwergewicht-900-Titel über dichten Wertzeilen
navigation: Untere weiße Leiste, 4 Ziele, Icon + fettes Label, aktiv mit limettener Pille hinter dem Icon
komponenten: 24-px-Karten ohne Schatten, Haarlinien-Rahmen-Karte, Limetten-Pille, Zeilen mit rechtsbündiger Kennzahl
icons: Phosphor Bold, 20–24 px, kompakt; aktiv gefüllt (ph-fill)
bewegung: Sachlich-federnd, 180/280 ms, cubic-bezier(.2,0,0,1), Druck skaliert auf 0.97
schrift: Inter Display 900 für Titel, Inter 600/400 für alles andere – maximaler Gewichtssprung
---
# Wise – Designsprache

**Kurz:** Eine salbeigrüne Fläche trägt weiße Blöcke mit 24 px Radius – ohne jeden Schatten, die Flächenkontraste allein erzeugen Tiefe. Darüber linksbündige Titel im Gewicht 900 mit engem Zeilenabstand, darunter ruhige Zeilen aus Inter 400/600 mit rechtsbündigen Zahlen. Der Charakter entsteht aus dem brutalen Gewichtssprung 900 → 400 und aus Limettengrün, das ausschließlich die Hauptaktion markiert.

## Wirkung
- Charakter: freundlich-direkt, nordisch-nüchtern, laut in der Typografie, leise in der Farbe.
- Passt zu: Finanz- und Kontoapps, Tracker, Verbrauchs- und Speicherübersichten, alles mit Zahlen und Status.
- Passt weniger zu: bildlastige Galerien, Luxus- und Editorial-Marken, dunkle Medien-Oberflächen.

## Aufbau und Raster
- Seitenaufbau: gestapelte Bänder auf `#e8ebe6`; jedes Band ist entweder ein weißer Block (`#ffffff`, 24 px) oder ein dunkler Block (`#0e0f0c` mit limettener Schrift). Keine Spaltenraster auf dem Handy.
- Ausrichtung: durchgehend linksbündig; Zahlen rechtsbündig in einer eigenen Spalte am Zeilenende.
- Raster: Basiseinheit 4 px; Marken-Container 1200 px, Hero zweispaltig (Titel links, Rechner-Karte rechts), mobil gestapelt.
- Dichte und Weißraum: Seitenrand 20 px, Kartenpolster 24 px (`spacing.xl`), Abstand zwischen Blöcken 16 px, zwischen Abschnitten 24–32 px. Zeilen in Listen 56–64 px hoch.
- Rhythmus: großer Titel – knappe Unterzeile – Block – Block. Kein Band ohne Zahl.

## Navigation
- Website: weiße, oben klebende Leiste, Links in 14 px/600, rechts die limettene Aktions-Pille.
- App: untere weiße Leiste, 64 px hoch über 20 px Sicherheitsrand, 4 Ziele (Start, Bibliothek, Suche, Profil), Icon 22 px + Label 11 px/600. Aktiv: gefülltes Icon in einer limettenen Pille (40×28 px) plus Label im Gewicht 700. Leiste bleibt beim Scrollen stehen; Detailseiten ersetzen sie durch eine Zurück-Pille oben links. App-Muster der Marke (nicht in der Datei): Avatar oben rechts statt Profil-Tab ist ebenfalls üblich.
- TV: linke Spalte mit 4 Zielen, Fokus als limettene Pille hinter dem Label, Skalierung 1.04.

## Startscreen
- Begrüßung im Gewicht 900 über zwei Zeilen (`line-height: .88`), darunter eine Zahlenzeile in 14 px/400.
- Danach ein dunkler Block als Aufmacher (Polaritätswechsel: `#0e0f0c` mit Titel in `#9fe870`), dann ein weißer Kennzahlen-Block mit Haarlinien-Rahmen, dann die Quellenliste.
- Höchstens drei Blöcke; lieber groß und luftig als viele Abschnitte.

## Komponenten
- Buttons: Primär = Limette `#9fe870` auf Ink-Text, 24 px Radius, Polster 12/24 px, Label 16 px/600, Höhe 48 px. Sekundär = `#e8ebe6` mit Ink-Text, gleiche Form. Tertiär = weiß mit 1 px Ink-Rahmen. Icon-Button = weißer Kreis, 40–44 px.
- Karten und Kacheln: weiß, 24 px Radius, **kein Schatten, kein Rahmen** – sie liegen auf der Salbeifläche. Varianten: salbei (`#e8ebe6`), blassgrün (`#e2f6d5`), dunkel (`#0e0f0c` + limettene Schrift). Innenbilder 16 px Radius.
- Listen: Zeilen in einer weißen Karte, getrennt durch 1 px `#e8ebe6`; links 44–48 px Bildquadrat (12 px Radius), Mitte Titel 16 px/600 + Unterzeile 14 px/400 `#868685`, rechts die Kennzahl 16 px/600 mit kleiner Einheit darunter.
- Suche und Eingabefelder: weiß, 1 px Rahmen in Ink, 12 px Radius, Polster 12/16 px, Platzhalter `#868685`. Der Rahmen (nicht ein Schatten) ist das Erkennungszeichen.
- Chips, Tabs, Filter: Pillen, 36 px hoch. Inaktiv weiß mit 1 px Ink-Rahmen, aktiv Ink-Fläche mit weißer Schrift (Form- statt Farbwechsel). Statuspillen: `#e2f6d5` mit `#054d28`.
- Dialoge und Sheets: weißes Sheet, oben 24 px Radius, Griff 36×4 px in `#e8ebe6`, Aktionen als volle Pillen untereinander.
- Signatur-Komponenten: die Rechner-Karte – weiße Karte mit 1 px Ink-Rahmen, zwei durch eine Haarlinie getrennte Wertfelder und ein dicker Fortschrittsbalken (8 px, limettene Füllung auf `#e2f6d5`).

## Icons
- Stil: Phosphor **Bold** – kompakte, kräftige Linien, die neben dem 900er Titel bestehen. Ein Stil pro Screen; aktiv wechselt auf `ph-fill`.
- Größe und Strich: 20 px in Zeilen, 22 px in der Navigation, 18 px in Chips. Keine dünnen Striche, kein Duoton.
- Einsatz: funktional (Quelle, Art, Aktion), nie dekorativ; immer mit Text oder in einem Kreis/einer Pille.
- Umsetzung: Compose `Icons.Rounded` / Material Symbols Rounded, Gewicht 600, Füllung 0 → 1 beim Aktivwerden; iOS SF Symbols `.semibold`, gefüllte Variante aktiv; Web Phosphor `bold` / `fill`.

## Bildsprache
- Die Marke arbeitet sparsam mit Fotos; in der App werden Bilder in Blöcke eingefasst statt randlos gezeigt.
- Bilder sitzen **innerhalb** der weißen Karte mit 16 px Radius und 24 px Luft ringsum – nie unter der Statusleiste, nie als Vollbild-Bühne.
- Seitenverhältnisse: 16:10 für Aufmacher, 1:1 für Zeilenbilder und Raster. Keine Verläufe über Bildern; Text liegt daneben, nicht darauf.
- Im dunklen Block darf das Bild leicht abgedunkelt werden, damit die limettene Schrift trägt.

## Typografie-Stimme
- Zwei Rollen, hart getrennt: Titel in Inter Display **900** (32–44 px, `line-height: .86–.9`, `letter-spacing: -.02em`), alles andere Inter 600 (Labels, Buttons, Werte) oder 400 (Fließtext, 14/16 px, Zeilenhöhe 1.4–1.5).
- Kein Gewicht dazwischen: 700 wirkt sofort falsch. Keine Versalien außer in 12-px-Mikro-Labels mit +0.06em.
- Größenkontrast ist extrem: 42 px/900 direkt über 14 px/400.
- Freier Ersatz: **Inter** (900 für Display) oder **Manrope** 800/900; Body stets Inter.

## Form, Tiefe und Material
- Radien: 8 px Mikro-Pillen, 12 px Eingaben und Zeilenbilder, 16 px Bilder in Karten, **24 px die kanonische Karte und der Button**, 9999 px Chips und Kreise. Nichts ist scharfkantig.
- Linien und Rahmen: 1 px Ink für Eingaben, Rechner-Karte und tertiäre Buttons; 1 px `#e8ebe6` als Trennlinie in Listen.
- Schatten und Ebenen: **keine**. Ebene entsteht durch Flächenkontrast salbei → weiß → ink.
- Besondere Oberflächen: Polaritätswechsel (dunkler Block mit limettener Schrift) als einziger „Effekt“; keine Verläufe, kein Glas, keine Körnung.

## Bewegung
- Laut Datei: keine Angaben; nur „Active/pressed“-Zustände für Buttons.
- Empfehlung: klein 180 ms / Screenwechsel 280 ms, Easing `cubic-bezier(.2,0,0,1)`. Druck: `scale(.97)` plus Abdunkeln der Limette auf `#cdffad`. Einblenden: 12 px von unten + Deckkraft, pro Block um 50 ms gestaffelt. Screenwechsel: horizontales Schieben ohne Skalierung. Fokus (TV): Pille wächst in 160 ms auf.
- Compose: `tween(180, easing = CubicBezierEasing(.2f,0f,0f,1f))` für Zustände, `tween(280)` für Screens, `animateItem()` für Listen, Zahlen mit `animateIntAsState`.

## Signatur-Elemente
1. Salbeigrüne Fläche mit weißen 24-px-Blöcken – ohne Schatten, ohne Rahmen.
2. Linksbündiger Titel im Gewicht 900 mit `line-height: .88` direkt über 14-px-Text.
3. Die Limette nur an genau einer Stelle pro Screen: der Hauptaktion.
4. Der dunkle Block mit limettener Schrift als einziger Aufmacher.
5. Kennzahlen-Karte mit 1 px Ink-Rahmen, Haarlinien-Teiler und dickem limettenem Balken.

## Übertragung auf eine App
- Startscreen: Begrüßung 900 → dunkler Aufmacher-Block → Kennzahlen-Block mit Rahmen → Quellenliste. Eine Limetten-Pille, sonst nichts Buntes.
- Liste und Übersicht: eine weiße Karte, darin alle Zeilen mit Haarlinien getrennt, rechts die Kennzahl – wie eine Umsatzliste. Filter als Pillen darüber.
- Detail: Bild in einer Karte (nicht randlos), darunter 900er Titel, dann die Limetten-Pille in voller Breite mit drei weißen Kreis-Buttons daneben, dann Segment-Umschalter und Raster.
- Formulare und Einstellungen: Felder mit 1 px Ink-Rahmen untereinander, Label 14 px/600 darüber, Hilfetext 12 px `#868685`, Abschluss mit voller Limetten-Pille.
- Leere Zustände und Laden: salbeifarbene Karte mit 24 px Radius, Titel in 24 px/600, eine Pille als Ausweg; Laden als salbeifarbene Platzhalterblöcke ohne Schimmer.
- TV: linke Zielspalte, rechts weiße Blöcke auf Salbei, Fokus als limettene Pille.
- Musterscreens: Start mit 900er Begrüßung, dunklem Rückblick-Block und Speicher-Kennzahlen; Bibliothek als eine weiße Karte mit Wertzeilen und Ink-Filterpillen; Detail mit eingefasstem Bild, Limetten-Pille und Fotoraster.

## Vermeiden
- Keine zweite Akzentfarbe und keine Limette als Erfolgsfarbe – dafür gibt es `#2ead4b`.
- Limette nie auf grünem Grund; immer auf Salbei, Weiß oder Ink.
- Titel nie in 700 oder leichter, nie zentriert, nie in Versalien.
- Keine Schatten, keine 8–12-px-Radien an Karten und Buttons, keine scharfen Ecken.
- Keine randlosen Bilder unter der Statusleiste – das ist eine andere Marke.
- Nicht mit Mastercard verwechseln: Wise stapelt rechteckige 24-px-Blöcke mit sehr fetter Typografie dicht übereinander; Mastercard arbeitet mit Kreisen, vollen Pillen, weiten Leerräumen und mittlerem Schriftgewicht.
