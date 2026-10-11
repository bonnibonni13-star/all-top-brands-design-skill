---
slug: nike
marke: Nike
website: https://nike.com
ansatz: plakativ
ansatz2: buehne
modus: hell
aufbau: Katalog ohne Radien: randlose Kampagnenfläche mit Versal-Lockup, darunter Bildraster
navigation: Oben Utility-Zeile, Kopf, Versal-Tabs mit 2-px-Unterstrich; Profil als Avatar
komponenten: Schwarze Pille 48 px, invertierende Chips, radiuslose Bildkacheln, Haarlinien-Zeilen
icons: Wenige, strenge Linien-Icons 20–24 px in Tintenschwarz, nur in runden 40-px-Knöpfen oder neben Text
bewegung: Hart: 120 ms, Druck schrumpft auf 0,5 bei Deckkraft 0,5; Bilder blenden 400 ms ein
schrift: Geometrische Versalien 46 px/0,9 fürs Lockup gegen 12–16-px-Grotesk 500; dazwischen fast nichts
---
# Nike – Designsprache

**Kurz:** Ein Katalog aus Fotos: vollflächige Bildflächen mit riesigem Versal-Lockup darauf, darunter radiuslose Bildkacheln mit drei Textzeilen. Die gesamte Oberfläche besteht aus Schwarz, Weiß und einem einzigen Grau; jede Aktion ist eine schwarze Pille. Der Kontrast zwischen 46-px-Versalien und 12–16-px-Text ist die eigentliche Gestaltung.

## Wirkung
- Charakter: sportlich, absolut, laut im Bild und mechanisch ruhig in der Oberfläche; wirkt wie ein gedruckter Katalog, nicht wie eine Web-App.
- Passt zu: Shops, Foto- und Videobibliotheken, Kampagnen- und Event-Apps, Trainings-Apps, allem mit starkem Bildmaterial.
- Passt weniger zu: Dashboards mit vielen Zahlen, Text- und Lese-Apps, verspielten oder weichen Marken, dunklen Oberflächen.

## Aufbau und Raster
- Seitenaufbau: Bänder stoßen ohne Trennelement aneinander – Kampagnenfläche (randlos) → Abschnittstitel → Raster oder Reihe → nächster Abschnitt. Die Bildkante ist die Trennlinie.
- Ausrichtung: alles linksbündig; Lockup und Bild-Pille sitzen unten links im Bild.
- Raster: 8-px-Basis (2 · 4 · 8 · 12 · 18 · 24 · 30 · 48 px), Abschnittsabstand 48 px (mobil 24 px), Rasterfuge 8 px (mobil 4–8 px), Seitenrand 16 px mobil. Raster 2-spaltig (mobil), 3–4-spaltig ab Tablet.
- Dichte und Weißraum: dicht, aber nie gedrängt – die Luft kommt aus dem grauen Bildhintergrund #f5f5f5, nicht aus Rändern. Kacheln haben 0 Innenabstand, die Textzeilen stehen mit 8 px direkt unter dem Bild.
- Rhythmus: eine große Bühne, dann viele kleine gleich große Kacheln; nie zwei große Lockups nebeneinander.

## Navigation
- Website: Utility-Zeile 36 px auf #f5f5f5 (rechtsbündig, 12 px), darunter Kopfleiste 56–64 px weiß mit Zeichen links, Zielen mittig (16/500) und Suchpille, Herz und Tasche rechts; aktives Ziel bekommt 2-px-Unterstrich in #111, nie eine Fläche.
- App: dieselbe dreistöckige Kopfzone statt einer Leiste unten – Utility-Zeile 30 px mit Kennzahlen in Versalien, Kopf 52 px (neutrales Zeichen links, Suche und Avatar rechts), darunter Tab-Zeile 44 px mit drei Zielen in Versalien 13/500 und 2-px-Unterstrich; Inset-Haarlinie `inset 0 -1px 0 #e5e5e5` als einzige Kante. Profil liegt als Avatar oben rechts. So bleibt der untere Bildschirmrand frei für randlose Bilder.
- Detail: runde 40-px-Knöpfe auf dem Bild (Zurück links oben, Favorit und Teilen rechts oben), keine Kopfleiste über dem Bild.
- TV: Reihen aus 1:1-Kacheln, Fokus = 4-px-Rahmen in Weiß plus 1,04-fache Skalierung, kein Schatten.

## Startscreen
- Randlose Kampagnenfläche über etwa 40 % der Höhe: Foto ohne Rahmen, darauf das Versal-Lockup (46 px, Zeilenhöhe 0,9, Weiß) unten links und darunter eine weiße Pille als einzige Aktion im Bild.
- Danach Abschnittstitel in Versalien (20–24 px/500) und direkt darunter das Material: eine angeschnittene Reihe aus 4:5-Kacheln mit weißer Pille unten links, dann ein 2-spaltiges Raster aus 1:1-Kacheln mit Name, Art und Menge.
- Keine Begrüßungskarte, keine Statistikkachel, kein Verlauf – der Einstieg ist Bild plus Katalog.

## Komponenten
- Buttons: Pille 30 px Radius, 48 px hoch, Polster 16/32 px, Schrift 16/500. Primär `#111` auf Weiß, Sekundär `#f5f5f5` mit Tintenschrift, auf Bildern weiße Pille (Polster 12/24). Nie Rechteck, nie Umriss-Pille, höchstens eine schwarze Pille pro Bildschirmhälfte; Druck: Fläche bleibt, Element schrumpft und wird halbdurchsichtig.
- Karten und Kacheln: Radius 0, kein Schatten, kein Rahmen, kein Innenabstand. Bild 1:1 (Raster) bzw. 4:5 (Reihe) randlos, Hintergrund #f5f5f5; darunter mit 8 px Abstand Name 16/500, Art 14/500 in #707072, Menge 14/500 in #111.
- Listen: als Auskunftszeilen – Zeilenhöhe 56–64 px, Beschriftung 16/500, rechts Winkel-Icon, darunter 1 px #cacacb. Keine Trennlinien innerhalb von Rastern.
- Suche und Eingabefelder: Pille 24 px Radius, 40 px hoch, Fläche #f5f5f5, Polster 8/16 px, Lupe links, Text 16/400. Fokus: Fläche wird weiß, 2 px Rahmen #111 plus 12-px-Hof in #f5f5f5.
- Chips, Tabs, Filter: Filter-Chip 30 px Radius, 40 px hoch, Polster 8/16, weiß mit 1 px #cacacb; aktiv vollständig invertiert (Fläche #111, Schrift Weiß) – kein Zwischenzustand. Navigations-Tabs nur mit 2-px-Unterstrich. Abzeichen auf Bildern: weiße Pille mit Haarlinie, 12/500.
- Dialoge und Sheets: weißes Blatt ohne Radius, Titel 24/500, Aktionen als zwei gestapelte Pillen (schwarz über grau) in voller Breite.
- Signatur-Komponenten: Kampagnenfläche mit eingebranntem Versal-Lockup; weiße Pille unten links im Bild; radiuslose Bildkachel mit drei Textzeilen; invertierender Filter-Chip; Auskunftszeile mit Haarlinie.

## Icons
- Stil (Empfehlung, die Datei nennt nur Icon-Orte): strenge, schnörkellose Linien-Icons mit geraden Enden, einfarbig #111; nie gefüllt, nie mehrfarbig, nie dekorativ. Icons ersetzen nie ein Wort, wo Platz für ein Wort ist.
- Größe und Strich: 24 px in runden 40-px-Knöpfen, 20 px in Kopf und Suche, 16 px als Winkel in Auskunftszeilen; Strich 2 px auf 24er-Raster, eckige Enden (`stroke-linecap: square`).
- Einsatz: nur Zurück, Suche, Favorit, Teilen, Mehr, Winkel, Abspielen. Statusfarben nur dort, wo ein Zustand wirklich signalisiert wird (#007d48 für „fertig", #d30005 nur in Preiszeilen).
- Umsetzung: Compose `Icons.Sharp`/`Outlined`, Gewicht 500, Füllung 0; iOS SF Symbols `.medium`; Web Lucide `stroke-width: 2; stroke-linecap: square` bzw. Phosphor `bold`.

## Bildsprache
- Laut Datei: Fotografie trägt alles. Kampagnen randlos im 16:9 (Desktop) bzw. 4:5 (Mobil) mit eingebranntem Lockup; Produktfotos 1:1 (oder 4:5) auf #f5f5f5 ohne Rahmen und ohne Schatten; Kategorie-Reihen 4:5 mit weißer Pille unten links.
- Übertragung: Fotos nie abrunden, nie tönen, nie mit Verlauf überziehen – nur dort, wo weiße Schrift im Bild steht, ein sehr dezenter dunkler Verlauf von unten (0 → 55 %). Bildausschnitt so wählen, dass das Lockup auf eine ruhige Fläche fällt. Avatare rund, 30–32 px. Platzhalter: graue Fläche #f5f5f5, nie ein Icon-Muster.

## Typografie-Stimme
- Zwei Stimmen ohne Mittelfeld: geometrische Versalschrift fürs Lockup (96 px Desktop, 46–48 px App, Zeilenhöhe 0,9, Laufweite 0) und eine neutrale Grotesk für alles andere (12 · 14 · 16 · 20 · 24 · 32 px, Gewicht 400/500).
- Abschnittstitel in Versalien 20–24/500; Kachelname 16/500; Art 14/500 grau; Mikro-Zeile 12/500 Versalien für Utility. Laufweite überall 0 (beim Ersatz −0,5 % auf dem Lockup).
- Nur Links sind unterstrichen; Überschriften, Buttons und Mengen nie.
- Größen App: Lockup 46/41, Screen-Titel 28–32/34, Abschnitt 20/24, Kachelname 16/24, Meta 14/21, Utility 12/16.
- Freier Ersatz: Lockup Bebas Neue, Anton oder Poppins 500 in Versalien (hier Poppins); Text Inter 400/500 (Helvetica-Ersatz: TeX Gyre Heros).

## Form, Tiefe und Material
- Radien: 0 für alles Flächige (Kacheln, Bilder, Bänder, Blätter), 24 px Suchpille, 30 px alle CTAs und Chips, 9999 px runde Icon-Knöpfe und Punkte, 18 px nur für Avatar-Container.
- Linien und Rahmen: 1 px #cacacb als Trennlinie, 1 px #e5e5e5 als Inset-Kante unter klebenden Leisten, 1 px #cacacb als Chip-Rand. Mehr Linienarten gibt es nicht.
- Schatten und Ebenen: keine. Keine Erhebung, keine Karte, die abhebt – Tiefe entsteht nur durch das Foto selbst und durch Schwarz gegen Weiß.
- Besondere Oberflächen: #f5f5f5 ist die „Bühne" jedes Fotos und die Fläche von Utility-Zeile, Suchpille und Sekundär-Pille; sonst reines Weiß.

## Bewegung
- Laut Datei: Druckzustand der Primär-Pille = Skalierung 0,5 mit Deckkraft 0,5 bei gleicher Fläche („tap collapse"); Hover-Zustände bewusst nicht dokumentiert.
- Empfehlung: Dauer klein 120 ms / Screenwechsel 240 ms, Easing `cubic-bezier(.4,0,.2,1)`; Chips wechseln hart ohne Überblendung; Bilder blenden beim Laden in 400 ms ein (Deckkraft, kein Versatz); Kampagnenbild beim Scrollen leicht parallax (max. 12 px); Fokus (TV): Rahmen in 120 ms.
- Compose: `tween(120, easing = CubicBezierEasing(0.4f, 0f, 0.2f, 1f))`, Druck über `scaleIn/scaleOut` auf 0,5f mit `alpha 0.5f`, `Crossfade` für Rasterwechsel; keine Feder, kein Überschwingen, kein Wischen von Karten.

## Signatur-Elemente
1. Riesiges Versal-Lockup (Zeilenhöhe 0,9) direkt ins randlose Foto gebrannt.
2. Weiße Pille unten links im Bild als einzige Aktion auf der Bildfläche.
3. Radiuslose 1:1-Kacheln auf #f5f5f5 mit drei kleinen Textzeilen darunter – die Fotografie ist die Karte.
4. Schwarze 48-px-Pille als einzige Hauptaktion, darunter gegebenenfalls die graue Zwillings-Pille.
5. Filter-Chip, der beim Aktivieren vollständig zu Schwarz-Weiß invertiert; Tabs nur mit 2-px-Unterstrich.

## Übertragung auf eine App
- Startscreen: Utility-Zeile mit Kennzahlen, Kopf, Versal-Tabs; randlose Kampagnenfläche mit Lockup und weißer Pille; Abschnitt „Entdecken" als angeschnittene 4:5-Reihe; Abschnitt „Zuletzt hinzugefügt" als 2-spaltiges 1:1-Raster.
- Liste und Übersicht: Versal-Titel mit Anzahl in Klammern, Suchpille, angeschnittene Chip-Reihe (aktiver Chip invertiert), danach 2-spaltiges Raster mit 8-px-Fuge und drei Textzeilen je Kachel; Sortierung als Textknopf mit Winkel.
- Detail: 1:1-Bild randlos mit runden Knöpfen darauf, Titel 32/500 mit grauer Unterzeile, zwei gestapelte Pillen in voller Breite (schwarz, dann grau), Auskunftszeile mit Haarlinie für die Musik, Chip-Reihe als Umschalter, dichtes 3-spaltiges Fotoraster.
- Formulare und Einstellungen: linksbündige Beschriftung 16/500, Felder als 24-px-Pillen, Abschnitte durch Haarlinien getrennt, Abschluss mit schwarzer Pille in voller Breite.
- Leere Zustände und Laden: graue Fläche #f5f5f5 im Format der Kachel, darunter dieselben drei Textzeilen als graue Balken; leere Ansicht = Versal-Satz 20/500 plus eine schwarze Pille.
- TV: Reihen aus 1:1-Kacheln mit 8-px-Fuge, Kopfzeile als Versal-Tabs, keine Seitenleiste.
- Musterscreens: Start mit eingebranntem Lockup und angeschnittener 4:5-Reihe, Bibliothek als Chip-gefiltertes 1:1-Raster, Album-Detail mit randlosem Bild, gestapelten Pillen und Fotoraster.

## Vermeiden
- Schatten, abgerundete Karten, schwebende Flächen; Radien zwischen 1 und 17 px.
- Zwei große Lockups im selben Abschnitt; Versal-Lockup als Abschnittstitel oder Kachelname.
- Mehr als eine schwarze Pille pro Bildschirmhälfte; eine zweite Buttonform.
- Akzentfarben als Oberflächenfarbe; Rot außerhalb von Preiszeilen; farbige Icons.
- Innenabstand in Bildkacheln, Rahmen um Fotos, Verlaufsschleier über dem ganzen Bild.
- Unterstreichungen außer bei Textlinks und beim aktiven Tab.
- Abgrenzung zu Airbnb: dort runde Bildkarten, weiche Schatten und freundliche Farbe; hier Radius 0, keine Erhebung, Schwarz-Weiß.
