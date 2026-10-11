---
slug: ibm
marke: IBM
website: https://www.ibm.com
ansatz: werkzeug
ansatz2: daten
modus: hell
aufbau: Carbon-Raster: weiße Fläche, graue Bänder #f4f4f4, alles rechteckig (0 px) und von 1-px-Linien geteilt
navigation: App-Muster: 32-px-Hilfsleiste + 48-px-Kopfzeile + Reiterleiste mit 2-px-Blauunterstrich, keine Leiste unten
komponenten: Kachelraster mit geteilten Haarlinien, Datenliste mit Kopfzeile, Knopf mit Text links/Icon rechts, Content-Switcher
icons: Empfehlung: Linien-Icons 20 px, Strich 1,5 px, eckige Enden (stroke-linecap square, miter), nie gefüllt
bewegung: Empfehlung: sachlich, 110/240 ms, cubic-bezier(.2,0,.38,.9); kein Federn, Unterstrich wandert, Flächen tauschen
schrift: Eine Familie: Grotesk 300 für Displays ab 32 px, 400/600 für Text, Laufweite +0,16 px
---
# IBM – Designsprache

**Kurz:** Carbon pur: rechte Winkel, 1-px-Linien und ein 4-px-Raster, auf dem jedes Element sitzt. Hierarchie entsteht aus Fläche (Weiß → #f4f4f4 → #161616) und Linie, nie aus Schatten oder Radius. Die großen Überschriften laufen in Gewicht 300 – leise Autorität statt Fettdruck –, und IBM-Blau #0f62fe ist die einzige Farbe im ganzen System.

## Wirkung
- Charakter: technisch, präzise, vertrauenswürdig; dicht statt luftig – „viel auf der Seite“ ist Absicht.
- Passt zu: Werkzeugen, Verwaltung, Datenbanken, Medien-Bibliotheken, Dashboards, allem mit Tabellen und Zuständen.
- Passt weniger zu: verspielten Consumer-Apps, Lifestyle, Kinder-Apps, allem, was Wärme oder Weichheit braucht.
- Abgrenzung zu anderen hellen Systemen: hier gibt es keine Radien, keine Schatten, keine zweite Farbe – und die Linien sind sichtbar, statt zwischen Karten zu verschwinden.

## Aufbau und Raster
- Seitenaufbau: Hilfsleiste → Kopfzeile → Reiter → Inhalt in Bändern; Abschnitte trennen graue Zeilen (#f4f4f4), nicht große Lücken.
- Ausrichtung: alles links an der Rasterkante; Zahlen, Daten und Zustände rechtsbündig in derselben Zeile.
- Raster: 4-px-Basis, Abstände 4/8/12/16/24/32/48/96 px; Web 16 Spalten (max. 1584 px), Kacheln 4-up → 2-up → 1-up. App: 16 px Seitenrand, Kacheln teilen sich 1-px-Linien (Rasterabstand 1 px, kein Zwischenraum).
- Dichte und Weißraum: dicht – Kachel innen 16–24 px, Produkt-Kachel 32 px, Zeilenhöhe in Listen 56–64 px, Knöpfe und Felder 48 px.
- Rhythmus: Weiß → graues Band → Weiß; pro Bildschirm genau ein blauer Primärknopf, dazu blaue Links und das 2-px-Lineal des aktiven Reiters; am Ende der Seite die dunkle Fläche #161616.

## Navigation
- Website: 32-px-Hilfsleiste (#f4f4f4, 12 px) über einer 48-px-Kopfzeile (weiß, 1 px untere Linie) mit Marke links, Kategorien mittig, quadratischen Icon-Knöpfen rechts; unter 672 px Hamburger.
- App: dieselbe Dreiteilung. Hilfsleiste (Quelle, Stand, Speicher), Kopfzeile 48 px mit 48-px-Quadratknöpfen, die durch 1-px-Linien getrennt sind, darunter eine Reiterleiste 48 px mit vier Zielen (Start, Bibliothek, Suche, Profil). Aktiv = 2 px Blau unten **plus** Gewicht 600 und Tintenfarbe; inaktiv #525252. Die Reiterleiste scrollt mit, Kopfzeile und Hilfsleiste bleiben stehen. Keine Leiste am unteren Rand.
- Detail: statt Reitern eine Brotkrumenzeile („Bibliothek / Alben / Lissabon“, 14 px, Blau mit Schrägstrichen) unter der Kopfzeile.
- TV: linke Spaltennavigation mit 2-px-Blaumarke, Fokus als 2-px-Blaurahmen ohne Vergrößerung.

## Startscreen
- Hilfsleiste mit Quelle und Speicherstand, Kopfzeile, Reiter; dann eine Begrüßung in Gewicht 300 (32 px) mit Zahlenzeile.
- Ein hervorgehobener Inhalt als Kachel mit Bild oben, Augenbraue in Satzschreibung, Titel 24 px/400, Angaben 14 px und einem blauen Knopf über die volle Kachelbreite.
- Danach eine Kachelreihe „Zuletzt hinzugefügt“ und ein Quellen-Raster aus drei Kacheln mit Zustand – beides im geteilten Linienraster.

## Komponenten
- Buttons: 0 px Radius, 48 px hoch, Text links, Icon rechts, Innenabstand 12/16 px. Primär #0f62fe auf Weiß (Druck #002d9c), sekundär #161616, tertiär weiß mit 1 px blauem Rand und blauem Text, Geist = blauer Text mit Pfeil. Gruppen stoßen ohne Abstand aneinander.
- Karten und Kacheln: rechteckig, 1 px #e0e0e0, kein Schatten; Varianten auf Weiß oder #f4f4f4. Im Raster teilen sich benachbarte Kacheln die Linie (1-px-Lücke auf grauem Grund).
- Listen: Datentabellen-Prinzip – graue Kopfzeile 32 px mit 14 px/600, Zeilen 56–64 px mit 1-px-Trennung, quadratisches 48-px-Bild links, Zustand und Datum rechtsbündig; unten eine angeheftete Leiste „1–8 von 8“.
- Suche und Eingabefelder: #f4f4f4, 0 px Radius, 48 px, 1 px untere Linie; Fokus ersetzt sie durch 2 px #0f62fe. Kein Rahmen, keine Rundung, kein Schatten.
- Chips, Tabs, Filter: Reiter mit 2-px-Blauunterstrich; für Filter ein Content-Switcher (Empfehlung) – gleich breite Segmente mit 1 px Rahmen, gewähltes Segment #161616 mit weißer Schrift.
- Dialoge und Sheets: rechteckiges weißes Blatt, 1 px Linie, 24 px innen, Knöpfe als volle Breite aneinander – links sekundär, rechts primär.
- Signatur-Komponenten: Hilfsleiste, Kachelraster mit geteilten Haarlinien, Datenliste mit Kopf- und Fußzeile, blauer Knopf mit Pfeil rechts.

## Icons
- Stil: Empfehlung – Carbon-nahe Linien-Icons: geometrisch, eckige Enden (`stroke-linecap: square`, `stroke-linejoin: miter`), ohne Rundungen und ohne Füllung.
- Größe und Strich: 16 px in Zeilen, 20 px in Knöpfen und Reitern, 24 px in Kopfzeilen; Strich 1,5 px, Farbe #161616 oder #525252, Blau nur im Primärknopf.
- Einsatz: in Knöpfen immer rechts vom Text (Pfeil, Play, Download); in Zeilen rechts als Zustand; nie dekorativ.
- Umsetzung: Compose `Icons.Sharp` bzw. Material Symbols Sharp, Gewicht 400, Füllung 0; iOS SF Symbols Regular ungefüllt; Web Carbon Icons oder Lucide mit `stroke-width: 1.5` und eckigen Enden.

## Bildsprache
- Fotos laufen rechteckig und unbehandelt – kein Radius, keine Maske, kein Farbfilter, kein Verlauf darüber.
- Seitenverhältnisse aus dem Raster: 16:9 für Bühnenbilder, 1:1 in Rastern und Listen, 4:3 in Kacheln; Bild sitzt bündig an der Kachelkante.
- Raster aus Bildern haben 1 px Abstand auf grauem Grund, sodass eine durchgehende Linienstruktur entsteht.
- Text steht nie auf dem Bild, sondern darunter; die einzige erlaubte Atmosphäre ist ein sehr blasser Blau-nach-Weiß-Verlauf hinter einer Bühne.

## Typografie-Stimme
- Eine Familie für alles; Hierarchie nur über Größe und Gewicht: 32–76 px in 300, 20–24 px in 400, Text 16/14 px in 400, Betonung 14 px/600.
- Laufweite +0,16 px auf Text- und Knopfgrößen (Präzisionsdetail), −0,4 bis −0,5 px erst ab 60 px; Zeilenhöhe 1,17 im Display, 1,5 im Text.
- Augenbrauen und Abschnittsmarken in **Satzschreibung** 14 px – keine gesperrten Versalien.
- Freier Ersatz: IBM Plex Sans (Google Fonts, SIL OFL) ist die Originalschrift und frei nutzbar; sonst Inter 300/400/600 mit +0,16 px Laufweite.

## Form, Tiefe und Material
- Radien: 0 px überall – Knöpfe, Felder, Kacheln, Bilder, Avatare; 2 px nur für seltene Abzeichen.
- Linien und Rahmen: 1 px #e0e0e0 ist das Hauptwerkzeug; #161616 als 1-px-Unterstrich bei Fokus, 2 px #0f62fe für aktive Reiter und Fokusfelder.
- Schatten und Ebenen: keine. Tiefe kommt aus dem Flächenwechsel Weiß → #f4f4f4 → #161616.
- Besondere Oberflächen: die invertierte Fläche #161616 (Fuß, Statusband) und ein sehr blasser Blauverlauf hinter Bühnenbildern – mehr nicht.

## Bewegung
- Laut Datei: keine Angaben zu Dauer oder Easing (nur Zustände: Hover, Druck, Fokus).
- Empfehlung: klein 110 ms / Screenwechsel 240 ms, Easing `cubic-bezier(.2, 0, .38, .9)` (Carbon „productive“); Druck = Fläche wechselt sofort auf #002d9c bzw. #f4f4f4, keine Skalierung, kein Federn; Einblenden = reine Deckkraft über 110 ms, höchstens 40 ms Versatz je Zeile; Reiterwechsel = der 2-px-Unterstrich wandert in 240 ms; Fokus (TV) = 2-px-Blaurahmen erscheint hart.
- Compose: `tween(110, easing = CubicBezierEasing(.2f, 0f, .38f, .9f))` für Zustände, `tween(240, …)` für Screens; `AnimatedContent` mit `fadeIn/fadeOut`, keine `spring`-Animationen.

## Signatur-Elemente
1. Rechte Winkel überall: 0 px Radius an Knöpfen, Feldern, Bildern und Kacheln.
2. Sichtbares Linienraster – Kacheln und Bilder teilen sich 1-px-Linien statt Abstände zu haben.
3. Displayschrift in Gewicht 300 neben 14 px/600 – großer Größen-, kleiner Gewichtskontrast.
4. Blauer Knopf mit Text links und Icon rechts; blaues 2-px-Lineal unter dem aktiven Reiter.
5. Graue Hilfs- und Fußzeilen (#f4f4f4) als Rahmen um den Inhalt – oben Stand und Quelle, unten Zählung.

## Übertragung auf eine App
- Startscreen: Hilfsleiste, Kopfzeile, Reiter, Begrüßung in 300, eine Bild-Kachel mit blauem Knopf, eine Kachelreihe und ein Quellen-Raster mit Zuständen.
- Liste und Übersicht: Suchfeld in #f4f4f4, Content-Switcher als Filter, Werkzeugzeile mit Anzahl und quadratischen Icon-Knöpfen, dann eine Datenliste mit grauer Kopfzeile und angehefteter Zählleiste.
- Detail: Brotkrumen, Bild 16:9 bündig, Titel in 300, Angaben, Knopfgruppe (blau + anthrazit, ohne Abstand), Hinweis-Kachel für die Musik, Reiter und ein 1-px-Fotoraster.
- Formulare und Einstellungen: Beschriftung 12 px über dem Feld, Feld #f4f4f4 mit unterer Linie, Hilfetext 12 px #8c8c8c, Fehler = 2 px #da1e28 und rote Meldung darunter.
- Leere Zustände und Laden: eine Zeile Text in 400 plus Geist-Knopf; Laden als graue Rechteck-Skelette (#e0e0e0) in Zeilenhöhe, kein Kreisel, keine Welle.
- TV: linke Spalte, Inhalt im 1-px-Raster, Fokus als 2-px-Blaurahmen; Schrift eine Stufe größer, Dichte bleibt.
- Musterscreens: Start mit Hilfsleiste, Reitern und Bild-Kachel, Bibliothek als Datenliste mit Content-Switcher und Zählleiste, Detail mit Brotkrumen, Knopfgruppe und 1-px-Fotoraster.

## Vermeiden
- Keine Radien, keine Pillen, keine Schatten, keine Verläufe oder Glas.
- Display nie fett setzen; Laufweite +0,16 px nicht entfernen.
- Blau nicht als Kachelfläche, Augenbrauenfarbe oder zweite Akzentfarbe verwenden; keine zweite Markenfarbe einführen.
- Keine gesperrten Versalien-Augenbrauen.
- Abschnitte nicht durch große Lücken trennen, sondern durch graue Bänder und Linien.
