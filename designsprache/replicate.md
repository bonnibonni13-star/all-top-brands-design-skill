---
slug: replicate
marke: Replicate
website: https://replicate.com
ansatz: editorial
ansatz2: werkzeug
modus: hell
aufbau: Warme Cremefläche, Abschnitte als Farbblöcke (Creme → Orangeband → Creme → dunkles Code-Feld), linksbündig
navigation: Schwebende weiße Pillenleiste unten (4 Ziele), aktiv = dunkle Pille mit Label; oben 60-px-Leiste mit Avatar
komponenten: Weiße Modellkarten (10 px) mit quadratischem Bild, Pillen-Tags, Status-Badge, dunkles Mono-Code-Feld
icons: Lucide-Linien, 1,75 px Strich, runde Enden, 18–20 px, einfarbig Ink; nie gefüllt, nie orange (Empfehlung)
bewegung: Ruhig editorial: 160 ms klein / 260 ms Screen, cubic-bezier(.2,.7,.3,1), Druck = Fläche dunkler (Empfehlung)
schrift: Drei Familien, drei Aufgaben: schwere schmale Display-Grotesk riesig (LH 1,0), humanistischer Text 400, Mono für Werte
---
# Replicate – Designsprache

**Kurz:** Entwicklerwerkzeug im Gewand eines Kunst-Zines: warme Creme statt Weiß, Tiefe durch Farbblöcke statt Schatten, und eine schwere, leicht schmale Display-Grotesk, die so groß gesetzt wird, dass mehrzeilige Titel als geometrischer Block lesen. Jedes bedienbare Element ist vollrund, jede Inhaltskarte 10–16 px – scharfe Ecken gibt es nicht. Orange ist ein Stempel, kein Anstrich: höchstens ein oranges Element pro Bildschirm.

## Wirkung
- Charakter: warm, handgemacht, selbstbewusst; „Laborheft trifft Printmagazin“ – präzise, aber nie steril.
- Passt zu: Werkzeug- und Katalog-Apps, Entwickler- und KI-Produkten, Medien- und Bibliotheks-Apps mit Textcharakter, Blogs, Preis- und Dokuseiten.
- Passt weniger zu: dunklen Entertainment-Oberflächen, verspielten Kinder-Apps, Marken mit mehreren Akzentfarben oder viel Glas und Glühen.

## Aufbau und Raster
- Seitenaufbau: Bänder über die volle Breite im festen Wechsel – Creme (`#f9f7f3`) → vollflächiges Orangeband mit Verlaufsnebel → Creme → dunkles Band `#202020` mit Code → Creme → schwarze Fußzeile. Tiefe entsteht durch diesen Flächenwechsel.
- Ausrichtung: linksbündig, Fließtext in schmaler Spalte; Display-Titel sitzen bündig an der Satzkante, nie zentriert.
- Raster: 4-px-Basis (2/4/8/12/16/24/32/48 px), Abschnitte 96 px, Editorialbänder 160 px; Inhalt max. 1280 px, Hero 1440 px; Modellraster 4/3/2/1-spaltig ab 1440/1280/768/425 px.
- Dichte und Weißraum: außen großzügig (96 px), innen kompakt – Karteninnenabstand 16 px, Preis-/Großkarten 32 px. In der App: Seitenrand 16 px, Abschnittsabstand 28–32 px, Karten 14–16 px innen.
- Rhythmus: großer Abschnittstitel (Display) → knappe Zeile in 14 px Charcoal → Karten oder Code-Feld → nächster Block. Immer Titel groß, Inhalt klein; kein Zwischenmaß.

## Navigation
- Website: Kopfleiste 60 px auf Creme mit 1 px Haarlinie unten, Wortmarke links, Links 14 px/600 mittig, rechts Icon + „Sign in“ + oranger Pillen-Button; unter 1024 px Hamburger. Unterhalb Filter als Pillen-Chips (6 × 14 px), unter 768 px als Scroll-Schiene.
- App (Empfehlung, aus Pillenform und Band-Logik abgeleitet): oben 60 px – links ein neutrales Zeichen (Kreis), rechts runder Icon-Button 36 px (weiß, Haarlinie) und 32-px-Avatar; Haarlinie unten. Unten eine **schwebende Pillenleiste** (weiß, vollrund, 1 px Haarlinie, 58 px hoch, 12 px Seitenrand, 20 px über dem Rand) mit 4 Zielen Start · Bibliothek · Suche · Profil. Aktiv = dunkle Pille (`#202020`, weiße Schrift, Icon + Label), inaktiv nur Linien-Icon in Charcoal – Aktivzustand also Fläche plus Label, nie Farbe. Leiste bleibt beim Scrollen stehen.
- Detailseiten: runde weiße Icon-Buttons (36 px, Haarlinie) links Zurück, rechts Teilen/Favorit/Mehr; Pillenleiste bleibt.
- TV: Kopfzeile mit Pillen-Chips statt Seitenleiste; Fokus = 3 px Ring in Orange bei 50 % plus 1,03-fache Skalierung der Karte.

## Startscreen
- Kopfleiste, direkt darunter ein **Orangeband über die volle Breite** (`#ea2804`, radialer Nebel `#ff6a3d` → `#f4a8a0` nach unten, Körnung 10 %): Begrüßung in Display 52–56 px, Zeilenhöhe 1,0, Laufweite −1,4 px, weiß; darunter die Zahlen der Bibliothek in 14 px bei 72 % Deckkraft und ein weißes Pillen-Suchfeld (44 px, vollrund).
- Danach auf Creme: Abschnittstitel „Rückblick“ in Display 30–34 px, dazu eine weiße Karte (10 px Radius, Haarlinie, 14 px innen) mit 16:9-Bild (10 px Radius), grünem Status-Badge, Titel 20 px/600 und Angaben 14 px Charcoal.
- „Zuletzt hinzugefügt“ als angeschnittene Reihe quadratischer Modellkarten (Bild 1:1, darunter Name + Mono-Angabe + Tag-Pille).
- Ein **dunkles Code-Feld** (`#202020`, 10 px Radius) als Quellen- und Speicherblock: schwarze Tab-Leiste oben (aktiver Tab mit 2 px orangem Unterstrich), darin Mono 12/13 px, Werte rechtsbündig, Status als grüner Punkt, Speicher als 2-px-Balken.
- Kein Vollbild-Hero mit Bild, keine Schatten, kein zweites Orange.

## Komponenten
- Buttons: immer vollrund (9999 px), 44 px hoch, Label 16 px/600, Padding 12 × 24 px. Primär Orange `#ea2804` auf Weiß (gedrückt `#c01f00`), Dunkel `#202020`/`#fcfcfc` als gleichwertige Zweitaktion, Outline weiß mit 1 px `#202020`, Ghost auf Creme ohne Rand (36 px), Icon-Button rund 36 px weiß mit Haarlinie.
- Karten und Kacheln: weiß (`#ffffff`) mit 1 px Haarlinie `rgba(32,32,32,.12)`, Radius 10 px (große Karten 16 px), Innenabstand 16 px, **kein Schatten**. Quadratisches Bild oben oder links, bündig bis zur Innenkante, selbst 10 px Radius. Kachel-Variante: Creme auf Knochenfläche (`#f3f0e8`), 24 px innen, Titel 24 px/600.
- Listen: Karten statt Zeilen – jede Zeile ist eine eigene weiße Karte mit 72-px-Bild links, Titel 18 px/600 (−0,35 px), Beschreibung 14 px Charcoal, darunter Tag-Pillen und Mono-Zahl rechts. Abstand zwischen Karten 10 px, keine Trennlinien.
- Suche und Eingabefelder: weiß, vollrund, 1 px Haarlinie, Padding 12 × 20 px, 44 px hoch, Platzhalter Ash `#8d8d8d`; Fokus 3 px Ring `rgba(59,130,246,.5)`.
- Chips, Tabs, Filter: Pillen-Chips 36 px (6 × 14 px, 14 px/600) – inaktiv weiß mit Haarlinie, aktiv dunkel gefüllt; Tag-Pillen 12 px auf Creme mit Haarlinie; Code-Tabs eckig (4 px) auf Schwarz, aktiv mit orangem Unterstrich.
- Dialoge und Sheets: weißes Blatt mit 16 px Radius oben, Griffleiste als 4-px-Pille, 24 px innen, Scrim `rgba(32,32,32,.4)`.
- Signatur-Komponenten: dunkles Code-Feld mit Tab-Leiste; Status-Badge grün (`#2b9a66`, vollrund, 4 × 10 px); Tag-Pillen für Art und Quelle; Avatar-Mosaik aus runden 32–40-px-Bildern; Orangeband mit Display-Titel.

## Icons
- Stil (Empfehlung, die Datei nennt keine Icon-Familie): schlichte Linien-Icons mit runden Enden und offenen Formen, einfarbig Ink bzw. Charcoal – passend zur „freundlichen Präzision“ der vollrunden Formen. Nie gefüllt, nie orange, keine zwei Stile nebeneinander.
- Größe und Strich: 16 px in Karten und Tags, 18 px in Buttons, 20 px in der Navigationsleiste; Strich 1,75 px auf 24er-Raster.
- Einsatz: in Pillen immer mit Label, allein nur in runden 36-px-Icon-Buttons (weiß, Haarlinie). Status zeigt ein Punkt-Badge, kein Icon.
- Umsetzung: Compose `Icons.Outlined` / Material Symbols Rounded, Gewicht 400, Füllung 0, 20 dp; iOS SF Symbols `.regular`, ohne `.fill`; Web Lucide `stroke-width: 1.75` oder Phosphor `regular`.

## Bildsprache
- Laut Datei: Modell-Thumbnails quadratisch (1:1) mit 10 px Radius, randlos bis zur Kartenkante; Hero-Beispiele 4:3 oder 16:9 mit 10 px Radius; Beitragende als runde 40-px-Avatare (32 px in Metadaten); Illustration im Hero schwarze Tusche, bleibt im Orangeband.
- Übertragung: Bilder sind gerahmte Platten auf Creme, nie Vollbild hinter der Oberfläche – 16 px Seitenrand, 10 px Radius, kein Verlauf und kein Text darauf. Fotoraster 3-spaltig, 6 px Fuge, Quadrate mit 10 px Radius. Leichte Körnung (6–10 %) nur auf dem Orangeband und auf dunklen Flächen.

## Typografie-Stimme
- Drei Familien, strikt getrennte Aufgaben: schwere, leicht schmale Display-Grotesk ab 30 px, humanistischer Sans für Oberfläche und Text 12–18 px, Mono für jeden Wert, Pfad und Status.
- Größenkontrast ist extrem: 128/72/48/30 px Display gegen 16/14/12 px Text; dazwischen liegt nichts.
- Zeilenhöhe im Display immer 1,0, Laufweite negativ und mit der Größe wachsend (−3 px bei 128, −1,8 bei 72, −1 bei 48, −0,5 bei 30); Text 1,5–1,56 bei Laufweite 0.
- Textgewicht bleibt 400 – Betonung kommt aus dem Familienwechsel, nie aus 500. Buttons und Labels 600. Keine Versalien, keine Sperrung.
- Freier Ersatz: Bricolage Grotesque oder Archivo Condensed Bold fürs Display, Geist oder Inter für Oberfläche und Text, JetBrains Mono für Code und Werte.

## Form, Tiefe und Material
- Radien: 0 px Bänder und Fußzeile, 4 px Code-Tabs, 6 px kleine Einsätze, 10 px Karten/Bilder/Code-Felder, 16 px große Karten und Sheets, vollrund für alles Bedienbare und Avatare. Nie Pillenform für Inhaltskarten.
- Linien und Rahmen: 1 px Haarlinie `rgba(32,32,32,.12)` als Standardtrennung, 1 px `#202020` für Outline-Buttons und harte Schnitte, `rgba(255,255,255,.2)` auf dunklen Flächen.
- Schatten und Ebenen: Stufe 0 flach, 1 Kontur, 2 Knochenfläche als Einsatz, 3 dunkle Umkehrung, 4 weicher Schatten `0 8px 24px rgba(32,32,32,.08)` nur für schwebende Bilder und die Navigationsleiste. Auf Creme grundsätzlich keine Schlagschatten.
- Besondere Oberflächen: radialer Orangenebel (`#ea2804` → `#ff6a3d` → `#f4a8a0`) nur im Hero; Knochenfläche `#f3f0e8` für Einsatzgruppen; dunkle Code-Felder als gedruckte Zitatblöcke; feine Körnung auf Farbflächen.

## Bewegung
- Laut Datei: keine Angaben zu Animationen; dokumentiert sind Zustände – Primär gedrückt `#c01f00`, Fokusring `rgba(59,130,246,.5)` 3 px, schwebende Thumbnails mit weichem Schatten.
- Empfehlung: Dauer klein 160 ms / Screenwechsel 260 ms, Easing `cubic-bezier(0.2, 0.7, 0.3, 1)`; Druck-Effekt: Fläche eine Stufe dunkler plus 0,98-fache Skalierung bei runden Buttons; Einblenden: Deckkraft + 10 px Anheben, Karten 40 ms gestaffelt; Display-Titel blendet ohne Versatz ein (die Typo ist statisch, nicht theatralisch); Screenwechsel: Creme-Band schiebt 16 px nach, Orangeband bleibt stehen; Fokus (TV): Ring in 140 ms.
- Compose: `tween(160, easing = CubicBezierEasing(0.2f, 0.7f, 0.3f, 1f))`, `AnimatedVisibility(fadeIn(tween(260)) + slideInVertically { it / 12 })`, `Modifier.animateItem()`; kein Überschwingen, kein `spring` mit Bounce.

## Signatur-Elemente
1. Warme Cremefläche statt Weiß – Weiß erscheint nur als Karte, Feld und Pille.
2. Vollflächiges Orangeband mit riesigem Display-Titel (Zeilenhöhe 1,0, negative Laufweite) als einziger Farbauftritt.
3. Dunkles Code-Feld mit eckiger Tab-Leiste und Mono-Werten mitten im hellen Layout.
4. Alles Bedienbare vollrund (Buttons, Felder, Chips, Avatare), Inhaltskarten dagegen 10 px.
5. Weiße Karten mit Haarlinie und quadratischem Bild plus grünem Status-Badge und Tag-Pillen – Schatten fehlen vollständig.

## Übertragung auf eine App
- Startscreen: Orangeband mit Begrüßung, Zahlen und Pillen-Suchfeld; darunter Rückblick-Karte, angeschnittene Reihe „Zuletzt hinzugefügt“ und das dunkle Code-Feld für Quellen und Speicher.
- Liste und Übersicht: Display-Titel, Pillen-Suchfeld, Chip-Reihe für Filter (aktiv dunkel), dann Karten-Liste – Bild links 72 px, Titel, Beschreibung, Tag-Pillen und Mono-Zahl rechts; der letzte Eintrag wird angeschnitten.
- Detail: runde Icon-Buttons als Kopf, Bildplatte 16:9 mit 10 px Radius, Display-Titel 48 px, Tag-Pillen für Angaben, orange Hauptaktion neben weißer Outline-Pille, dunkles Mono-Feld für die Musik zur Diashow, Chip-Umschalter, 3-spaltiges Fotoraster.
- Formulare und Einstellungen: Abschnitte als Knochenflächen-Gruppen, Zeilen 52 px mit Label 16 px links und Wert in Mono rechts, Felder vollrund; Schalter als dunkle Pille.
- Leere Zustände und Laden: Display-Zeile in 30 px, ein Satz 16 px Charcoal, eine orange Pille; Laden als Knochen-Platzhalter ohne Schimmer, Fortschritt als 2-px-Balken im Code-Feld.
- TV: Pillen-Chips oben, Karten-Raster 4-spaltig auf Creme, Fokus als oranger Ring; dunkles Band für Details.
- Musterscreens: Start mit Orangeband, Rückblick-Karte und dunklem Quellen-Feld; Bibliothek als Karten-Liste mit Chip-Filtern; Album „Lissabon“ als editoriale Detailseite mit Bildplatte, Riesen-Titel und Mono-Musikfeld.

## Vermeiden
- Reines Weiß als Seitenfläche; eine zweite Akzentfarbe neben Orange (Grün ist semantisch, Blau nur Fokus).
- Mehr als ein oranges Element pro Bildschirm; Orange für Fließtext, große Flächen oder Deko.
- Schlagschatten auf Creme; Code oder Werte in hellgrauen Kästen statt auf `#202020`.
- Display-Zeilenhöhe über 1,0, lockere Laufweite, Versalien oder Textgewicht 500 zur Betonung.
- Vollrunde Inhaltskarten, scharfe 0-px-Ecken bei Karten, Material-artige Karten mit Elevation.
- Code oder Zahlen im Textfont setzen; Mischung aus Linien- und gefüllten Icons.
