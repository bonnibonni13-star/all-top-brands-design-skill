---
slug: vodafone
marke: Vodafone
website: https://www.vodafone.com
ansatz: plakativ
ansatz2: buehne
modus: gemischt
aufbau: Bänderfolge: dunkles Foto-Band mit riesiger Versal-Headline, danach weißes Inhaltsband, unten wieder dunkel
navigation: Dunkle Leiste unten (4 Ziele), aktiv = 3-px-Balken in Rot plus weißes Label; Versal-Labels 12 px
komponenten: 60-px-Pillen-Buttons, Story-Karten mit 16:9-Bild (6 px), Chip-Pillen 32 px, weiße Kreis-Icon-Knöpfe
icons: Phosphor Fill, kompakt und massiv, 20–24 px, einfarbig Tinte bzw. Weiß auf Dunkel (Empfehlung)
bewegung: Entschlossen: 180/320 ms, cubic-bezier(.4,0,.2,1); Pille füllt sich, Headline fährt 16 px hoch (Empfehlung)
schrift: Eine Grotesk in zwei Extremen: 800 in Versalien (−1 px, enge Zeilen) gegen 300 für ruhige Sätze
---
# Vodafone – Designsprache

**Kurz:** Eine Plakat-Sprache: ein dunkles Foto-Band mit einer riesigen Versal-Headline in Gewicht 800 schreit, das darauffolgende weiße Band spricht ruhig in Gewicht 300. Alles Anklickbare ist eine 60-px-Pille, es gibt genau eine Akzentfarbe (Scharlachrot) und keine Schatten – Tiefe entsteht allein aus dem Wechsel dunkler und heller Flächen.

## Wirkung
- Charakter: laut, selbstsicher, massenwirksam; Kampagne statt Werkzeug, Nähe über Fotografie statt über Illustration.
- Passt zu: Telekommunikation, Tarif- und Vertragsportalen, Nachrichten, Sport, Unterhaltung, allem mit starkem Bildmaterial.
- Passt weniger zu: feinen Werkzeug-Oberflächen, Datentabellen, ruhigen Lese-Apps, zurückhaltenden Luxusmarken.

## Aufbau und Raster
- Seitenaufbau: strenge Bänderfolge – dunkles Hero-Band `#25282b` mit Foto → weißes Inhaltsband → dunkles Fußband. Keine Zwischentöne, keine grauen Flächen dazwischen.
- Ausrichtung: Headline links oben im Hero, Fließtext linksbündig; Karten in gleichen Spalten.
- Raster: 4-px-Basis (2/4/8/12/16/20/24/32 px), Bänder randlos mit 32 px Außenabstand (in der App 20–24 px), Story-Karten 2-spaltig, mobil 1-spaltig.
- Dichte und Weißraum: im Hero füllt die Headline die Fläche; in Karten hängen Titel und Text eng beieinander (8 px), zwischen Karten 24–32 px.
- Rhythmus: Eyebrow in Versalien → Riesen-Headline → ruhiger 300er-Satz → Pillenreihe. Dieser Vierklang wiederholt sich in jedem Band.

## Navigation
- Website: dunkle Kopfleiste `#25282b` über die volle Breite, Logo links, Linkreihe rechts mit Login und Suche, 16×32 px Innenabstand; unter 600 px Hamburger mit dunkler Overlay-Liste.
- App (Empfehlung): untere Leiste in `#25282b`, 4 Ziele Start · Bibliothek · Suche · Profil, Icon 22 px gefüllt, Label 12 px/600 in Versalien (0,57 px gesperrt). Aktiv = 3-px-Balken in `#e60000` an der Oberkante der Zelle plus weißes Label und volle Deckkraft; inaktiv Weiß bei 55 %.
- Detail: weiße Kreis-Icon-Knöpfe (40 px) schweben über dem Foto – links Zurück, rechts Favorit, Teilen, Mehr; die Leiste weicht einer dunklen Musikzeile.
- TV: dunkle Kopfzeile mit Versal-Labels; Fokus = rote 4-px-Unterkante plus leichte Aufhellung der Kachel, keine Rundung ändert sich.

## Startscreen
- Hero-Band über die halbe Höhe: Foto ganzflächig auf `#25282b`, Deckkraft ~60 %, darüber Eyebrow 16 px/800 Versalien, Headline 54 px/800 Versalien (Zeilenhöhe 0,84, −1 px) und ein 300er-Satz mit den Angaben.
- Im Hero genau zwei Pillen: gefüllte rote Hauptaktion, daneben weiß umrandete Nebenaktion.
- Darunter das weiße Band: Abschnittstitel 28–32 px in Gewicht 300, dann zweispaltige Story-Karten mit 16:9-Bild, Chip und Titel in 700; die letzte Reihe ist angeschnitten.

## Komponenten
- Buttons: Pille `#e60000` mit weißem Text, 18 px/400, Innenabstand 12×24 px, Radius 60 px – das ist die einzige gefüllte Aktionsfarbe. Sekundär: weiße Pille mit rotem Text und rotem 1-px-Rand; tertiär: weiße Pille mit Tinte-Rand; auf Dunkel: transparente Pille mit weißem 1-px-Rand. Nie eckig.
- Karten und Kacheln: Story-Karte auf Weiß, Radius 6 px, 16:9-Bild oben, darunter Chip, Titel 20–24 px/700 und Angabe 14 px in `#7e7e7e`; kein Schatten, kein Rahmen – die Bildkante trägt die Form.
- Listen: als zweispaltiges Kartenraster statt als Zeilenliste; wo Zeilen nötig sind, 1-px-Trenner in `#bebebe` und Titel in 16 px/700.
- Suche und Eingabefelder: weiß mit 1 px `#25282b`, Radius 6 px, Innenabstand 12×16 px, Höhe 48 px, Platzhalter `#bebebe`; Fokus verdoppelt die Randstärke.
- Chips, Tabs, Filter: Chip-Pillen `#f2f2f2`, 14 px/700, 4×12 px, Radius 32 px; aktiv = `#e60000` mit weißem Text. Tabs im Detail als Versal-Labels mit 3-px-Unterstrich in Rot.
- Dialoge und Sheets: weiße Fläche mit 6 px Radius über dunklem Schleier `rgba(37,40,43,.6)`; kein Schlagschatten, Aktionen als Pillenreihe unten.
- Signatur-Komponenten: Foto-Hero mit Riesen-Headline; roter Markerstein (rotes 6-px-Quadrat mit weißem Zeichen) als Blickanker zwischen den Bändern; die Pillenreihe.

## Icons
- Stil: kompakte, massive Flächen-Icons (Phosphor Fill) – sie halten gegen Gewicht 800 stand; keine feinen Linien (Empfehlung).
- Größe und Strich: 22 px in der Leiste, 20 px in Knöpfen und Chips, 24 px in Kreisknöpfen; keine Strichstärke, da gefüllt.
- Einsatz: immer mit Text oder in einem Kreis; Zustände über roten Balken, Füllung oder Deckkraft, nie über die Icon-Farbe allein.
- Umsetzung: Compose `Icons.Filled` bzw. Material Symbols Rounded mit Füllung 1, Gewicht 500; iOS SF Symbols Semibold gefüllt; Web Phosphor Fill oder Lucide mit `fill: currentColor`.

## Bildsprache
- Fotografie ist das einzige dekorative System: echte Menschen, Städte, Technik – groß, nah, randlos. Keine Illustration, keine Verläufe als Dekor.
- Hero: ganzflächig 4:3 oder 16:9 auf der Tinte-Fläche, Deckkraft 55–65 %, zusätzlich ein Verlauf nach unten zu `#25282b`, damit die Headline steht.
- Karten: 16:9 mit 6 px Radius, Bildkante bündig zur Kartenkante; Fotoraster 3-spaltig mit 8 px Fuge und 6 px Radius.
- Keine Duplex- oder Graustufenfilter, keine Körnung – das Foto bleibt farbig und direkt.

## Typografie-Stimme
- Eine Grotesk in zwei Extremen: 800 in Versalien für jede Headline (144/126/90 px im Web, 42–56 px in der App), −1 px gesperrt, Zeilenhöhe 0,79–0,88; 300 für Abschnittstitel in 28–48 px.
- Dazwischen 700 für Kartentitel (20–32 px) und Chips, 400 für Text (16–18 px, Zeilenhöhe 1,4–1,55), 14 px für Angaben, 12 px/600 Versalien (+0,57 px) für Metadaten und Leisten-Labels.
- Versalien ausschließlich im Hero, in Eyebrows, Tabs und Leisten-Labels; Fließtext nie in Versalien.
- Freier Ersatz: die Hausschrift ist proprietär; Inter 800 mit `letter-spacing: -1px` kommt am nächsten (hier gerendert), Geist 700–800 als zweite Wahl, Helvetica-Ersatz TeX Gyre Heros für Textgrößen.

## Form, Tiefe und Material
- Radien: 0 px für Bänder, 6 px für Karten, Bilder und Felder, 32 px für Chips, 60 px für alle Knöpfe, 9999 px für Kreis-Icon-Knöpfe.
- Linien und Rahmen: 1 px `#25282b` an Feldern, 1 px Weiß (oft 25 % Deckkraft) als Trenner auf dunklen Flächen, 1 px `#bebebe` in Tabellen.
- Schatten und Ebenen: keine. Ebene entsteht durch Polaritätswechsel Tinte ↔ Weiß; nur die weißen Kreisknöpfe liegen sichtbar über dem Foto.
- Besondere Oberflächen: Verlauf von transparent zu `#25282b` am Fuß jedes Fotos; roter Markerstein als einziger Farbfleck im weißen Band.

## Bewegung
- Laut Datei: keine Angaben (die Marke dokumentiert keine Animationszeiten).
- Empfehlung: klein 180 ms / Screenwechsel 320 ms, Easing `cubic-bezier(.4, 0, .2, 1)`; Druck = Pille dunkelt auf `#c40000` und schrumpft auf 0,98; Einblenden = Headline 16 px nach oben mit 80 ms Staffel zwischen Eyebrow, Headline und Pillen; Screenwechsel als Bandwechsel (neues Band schiebt sich über das alte); Fokus (TV) = roter Balken wächst in 180 ms.
- Compose: `tween(320, easing = CubicBezierEasing(.4f, 0f, .2f, 1f))`, Pillen-Druck über `animateFloatAsState(.98f)`, Hero-Einzug mit `AnimatedVisibility(slideInVertically)`, Listenkarten mit `animateItem()`.

## Signatur-Elemente
1. Riesige Versal-Headline in Gewicht 800 über einem randlosen Foto auf fast schwarzem Grund.
2. Der Gewichtssprung 800 → 300 direkt untereinander: Schrei und ruhiger Satz.
3. 60-px-Pillen in Rot und als Umriss – nie ein eckiger Knopf.
4. Harte Bänderfolge dunkel → hell → dunkel, ganz ohne Schatten.
5. Roter Markerstein (6-px-Quadrat) als einziger Farbanker im weißen Band.

## Übertragung auf eine App
- Startscreen: halbhohes Foto-Hero mit Eyebrow, Riesen-Headline, 300er-Angabenzeile und zwei Pillen; darunter ein weißes Band mit 300er-Abschnittstitel und zweispaltigen Story-Karten.
- Liste und Übersicht: dunkles Kopfband mit Versal-Titel, darunter weißes Band mit Suchfeld, Chip-Pillen und zweispaltigem Kartenraster; die letzte Reihe angeschnitten.
- Detail: randloses Foto mit Versal-Titel im Verlauf, weiße Kreisknöpfe darüber; im weißen Band rote Hauptpille plus Umriss-Pille, Versal-Tabs mit rotem Unterstrich, Fotoraster, unten eine dunkle Musikzeile.
- Formulare und Einstellungen: Felder 48 px mit 1-px-Tinte-Rand, Label 14 px/700 darüber, Hilfetext `#7e7e7e`; Absenden als rote Pille über die volle Breite.
- Leere Zustände und Laden: weißes Band mit `#f2f2f2`-Fläche, roter Markerstein, Satz in 18 px/400 und einer Umriss-Pille; Laden als `#f2f2f2`-Blöcke in Kartenform.
- TV: Hero wird zur Vollbild-Bühne, Karten zu großen 16:9-Kacheln mit rotem Fokusbalken.
- Musterscreens: Start mit Foto-Hero „VOR EINEM JAHR“ und weißem Kartenband; Bibliothek mit dunklem Versal-Kopf, Chip-Pillen und Kartenraster; Detail mit randlosem Foto, roter Pille, Versal-Tabs und dunkler Musikzeile.

## Vermeiden
- Keine zweite Akzentfarbe neben Rot, Tinte und Grauwerten; Rot nie als große Fläche, sondern nur für Aktion und Anker.
- Headlines im Hero nie in Gemischtschreibung und nie unter Gewicht 800 setzen; die Laufweite −1 px gehört dazu.
- Keine eckigen Knöpfe und keine 6-px-Radien an Aktionen – Pillen sind Pflicht.
- Keine Schlagschatten und keine grauen Zwischenflächen zur Trennung; Bänder wechseln hart.
- Gewicht 300 nicht unter 24 px einsetzen – darunter wird es unleserlich.
- Fotos nicht einfärben, nicht als kleine Vignetten verstecken und nicht durch Illustrationen ersetzen.
