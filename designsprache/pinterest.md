---
slug: pinterest
marke: Pinterest
website: https://www.pinterest.com
ansatz: galerie
ansatz2: verspielt
modus: hell
aufbau: Warm-cremefarbene Hülle um ein Masonry-Raster: Bilder in Spalten unterschiedlicher Höhe, 8 px Fuge
navigation: Tableiste unten mit vier runden Icon-Zielen ohne Beschriftung; Suche als Pillen-Feld oben
komponenten: Pin-Karte 16 px ohne Polster, weiße Overlay-Pille, Pillen-Chips (aktiv invertiert), rote CTA
icons: Kräftig, rund, geschlossen (Phosphor Bold/Fill), 26 px in der Leiste, 20 px in Knöpfen; aktiv gefüllt
bewegung: Empfehlung: weich und kurz, 180 ms / 320 ms, cubic-bezier(.4,0,.2,1), Druck = Skalieren auf .96
schrift: Geometrische Grotesk, 400/500/600/700, Überschriften eng gesperrt (−1,2 px), Fließtext 16 px/1,4
---
# Pinterest – Designsprache

**Kurz:** Ein Entdeck-Werkzeug in der Hülle eines Magazins: Das Masonry-Raster aus randlosen Bildkacheln mit 16-px-Radius und 8-px-Fuge trägt den ganzen Screen, die Hülle ist warm-creme und tritt zurück. Genau ein gesättigtes Rot markiert die Hauptaktion; sonst gibt es nur Schwarz, Grau und Creme, keine Schatten, keine Verläufe und keine scharfen Ecken.

## Wirkung
- Charakter: freundlich, dicht, sammelnd; alles wirkt greifbar und rund, nichts wirkt technisch.
- Passt zu: Foto-, Rezept-, Mode-, Wohn- und Sammel-Apps, Entdecken- und Merklisten-Flächen, Shopping-Feeds.
- Passt weniger zu: Daten- und Admin-Werkzeugen, Lesestrecken mit langem Text, nüchternen Finanz- und Technik-Apps.
- Abgrenzung zu anderen hellen Bild-Marken: Nicht gleichmäßiges Raster mit Angaben unter dem Bild, sondern Spalten verschiedener Höhe mit Angaben **auf** dem Bild; keine Schatten, keine Unterstrich-Tabs, keine beschriftete Tableiste.

## Aufbau und Raster
- Seitenaufbau: zwei Modi wechseln sich ab – Magazin-Hülle (cremefarbene Flächen, große Überschrift, Feature-Karte aus Bild + Überschrift + roter CTA) und Entdeck-Fläche (reines Masonry mit Chip-Zeile darüber).
- Ausrichtung: durchgehend linksbündig; Overlay-Pillen in den Bildecken, runde Icon-Knöpfe rechts oben.
- Raster: Masonry nach Spalten, 5–6/4/3/2/1 Spalten (Ultrabreit bis Mobil), Fuge `{spacing.sm}` 8 px waagerecht und senkrecht, mobil 6 px; Inhaltsbreite max. 1280 px, Seitenrand 16–24 px; Abschnittsabstand 64 px (mobil 32 px).
- Dichte und Weißraum: in der Hülle großzügig (64 px zwischen Blöcken, 32 px Innenpolster in Karten), im Raster sehr dicht – Bilder berühren sich fast.
- Rhythmus: Suche → eine Überschrift → eine Feature-Karte mit rotem CTA → Abschnittstitel → Masonry bis zum Rand.

## Navigation
- Website: feste Kopfleiste 64 px auf Weiß, Wortmarke links, Pillen-Suchfeld mittig (48 px, voller Radius, Fläche `#f6f6f3`), rechts Textlinks und der stets rote Primärbutton; auf Unterseiten 1 px `#dadad3` als untere Kante, auf der Startseite ohne Kante. Unter 768 px Hamburger, Suche wird zum Lupen-Icon.
- App (App-Muster der Marke (nicht in der Datei)): Tableiste unten, 64 px, Weiß mit 1-px-Oberkante `#dadad3`, vier Ziele (Start · Bibliothek · Suche · Profil) als reine Icons ohne Beschriftung, 26 px; aktiv = gefülltes Icon in Schwarz plus 4-px-Punkt darunter, inaktiv = Umriss-Icon in `#91918c`. Die Leiste bleibt beim Scrollen stehen; das Suchfeld oben scrollt mit.
- Detail: runder 40-px-Icon-Knopf „zurück“ links oben, rechts Teilen und Mehr als gleiche runde Knöpfe; die Tableiste bleibt stehen, es gibt keine eigene Aktionsleiste.
- TV: Masonry als fokussierbares Raster, Fokus = 4-px-weißer Innenrahmen plus 16-px-Radius-Vergrößerung auf 1,04; Chips als Reihe oben.

## Startscreen
- Oben eine Zeile: Pillen-Suchfeld (48 px, voller Radius, `#f6f6f3`, Lupe links) plus ein runder 40-px-Icon-Knopf rechts.
- Begrüßung als Überschrift 28 px 700 mit −1,2 px Sperrung.
- Hervorgehobenes als Feature-Karte: großes Bild mit 32 px Radius, weiße Overlay-Pille oben links, darunter Überschrift 22 px 600, Angabenzeile 14 px und genau ein roter Button.
- Darunter ein Abschnittstitel 18 px 600 und das Masonry-Raster, das unten offen weiterläuft.

## Komponenten
- Buttons: Radius 16 px, Höhe 40 px, Label 14 px 700, Polster 6/14 px. Primär `#e60023` auf Weiß (gedrückt `#cc001f`), Sekundär `#e5e5e0` auf Schwarz (gedrückt `#c8c8c1`), Tertiär transparent mit schwarzem Text. Runder Icon-Knopf 40 px, Fläche `#f6f6f3`, voller Radius. Höchstens ein rotes Element pro Bildschirmhöhe.
- Karten und Kacheln: Pin-Karte = das Bild selbst, Radius 16 px, Polster 0, Fläche `#f6f6f3` als Ladefarbe, natürliches Seitenverhältnis (1:1, 4:5, 3:4, 2:3 – nie quer). Große Feature-Pins 32 px Radius. Kategoriekachel `#f6f6f3`, 16 px Radius, 16 px Polster, Bild plus Label 16 px 600.
- Listen: Empfehlung: Zeilen als cremefarbene Karten (`#f6f6f3`, 16 px Radius, 8 px Innenpolster) mit quadratischem 48-px-Bild links, Titel 14 px 700 und Angabe 12 px `#62625b`; keine Trennlinien, Abstand 8 px.
- Suche und Eingabefelder: Suchfeld 48 px, voller Radius, `#f6f6f3`, Platzhalter `#91918c` 16 px; im Fokus Weiß mit 1 px `#91918c`. Textfeld 44 px, 16 px Radius, Weiß, 1 px `#91918c`; Fokus = 2-px-Innenrahmen Schwarz plus 4-px-Außenring `#435ee5`.
- Chips, Tabs, Filter: Pillen-Chips, voller Radius, Polster 8/16 px, Label 14 px 700, Fläche `#f6f6f3`; aktiv vollständig invertiert (Fläche Schwarz, Text Weiß) – der Zustand ist damit auch ohne Farbe eindeutig.
- Dialoge und Sheets: Karte Weiß, 32 px Radius, 32 px Polster, über 50-%-Scrim mit 16-px-Weichschatten; mobil als Blatt mit oben 32 px Radius und Button am unteren Rand.
- Signatur-Komponenten: die weiße Overlay-Pille auf dem Bild (12 px 700, voller Radius, Polster 6/12 px) als Marken-Geste; das Masonry-Raster; der invertierte Chip; der runde Icon-Knopf auf Creme.

## Icons
- Stil (Empfehlung; die Datei nennt nur Lupe und kleine Winkel): kräftige, geschlossene, rundliche Glyphen – lieber gefüllt als dünn, nie fadendünn, nie eckig.
- Größe und Strich: 26 px in der Tableiste, 20 px in runden Knöpfen und Chips, 18 px in Zeilen; Strichstärke kräftig (entspricht Phosphor Bold), aktive Zustände als Füllung.
- Einsatz: Navigation, runde Knöpfe (zurück, teilen, mehr, favorisieren), Lupe im Suchfeld, Filter-Regler; nie als Zierde in Karten – dort arbeitet das Bild.
- Umsetzung: Compose `Icons.Rounded` bzw. Material Symbols Rounded, Gewicht 600, Füllung 1 für aktiv / 0 für inaktiv; iOS SF Symbols `.semibold`, `.fill` für aktiv; Web Phosphor `bold` und `fill`.

## Bildsprache
- Laut Datei: das Foto ist die Karte. Randlos, ohne Innenpolster, ohne Rahmen, ohne Schatten; natürliches Seitenverhältnis bleibt erhalten, die Spaltenzahl ändert sich, nicht das Format.
- Hochformate dominieren (4:5, 3:4, 2:3), Quadrate für Kategoriekacheln und Vorschaubilder, Querformate meiden.
- Keine Filter, keine Tönung, keine Verläufe über dem Bild – Kontrast für Text entsteht durch die weiße Overlay-Pille, nicht durch einen Scrim.
- Radius 16 px an Kacheln, 32 px an großen Feature-Pins, voller Radius an Avataren (32–48 px).
- Angaben unter der Kachel (12 px `#62625b`) sind das App-Muster der Marke; die Hülle der Karte selbst bleibt ungepolstert.

## Typografie-Stimme
- Eine geometrische Grotesk in 400/500/600/700, keine Serifen, kein Mono. Sehr steiler Sprung von der Schauzeile (70/44 px) direkt auf 16 px – dazwischen fast nichts.
- Sperrung: −1,2 px bei 70 px und 28 px, −0,8 px bei 44 px, sonst 0. Zeilenhöhe 1,1–1,25 bei Überschriften, 1,4 im Text.
- Hierarchie kommt aus Gewicht und Größe, nicht aus Farbe: Text bleibt `#33332e`, Angaben `#62625b`, Platzhalter `#91918c`.
- Rollen in der App: 28 px 700 Seitentitel, 22 px 600 Karten-Überschrift, 18 px 600 Abschnittstitel, 16 px 400 Text, 14 px 700 Button und Chip, 12 px 500 Overlay-Pille und Angaben.
- Freier Ersatz: Inter 400/500/600/700 (metrisch sehr nah), für die Schauzeile Manrope; Sperrung −1,2 px unabhängig vom Ersatz beibehalten.

## Form, Tiefe und Material
- Radien: nur drei Werte – 16 px für fast alles Bedienbare und für Kacheln, 32 px für große Karten und Dialoge, voll für Suchfeld, Chips, Avatare und runde Knöpfe. 0 px nur für strukturelle Flächen (Leisten, Fußbereich). Keinen Zwischenwert einführen.
- Linien und Rahmen: 1 px `#dadad3` als Leisten- und Zeilenkante, 1 px `#e5e5e0` als feine Innenlinie; Felder bekommen 1 px `#91918c`.
- Schatten und Ebenen: im Inhalt keine. Einzige Erhebung ist der Dialog: 16 px weicher Umgebungsschatten über 50-%-Scrim.
- Besondere Oberflächen: warme Cremetöne `#fbfbf9` (Seitenwäsche), `#f6f6f3` (Karten, Felder, Chips), `#e5e5e0` (Sekundärbutton); selten ein warm-schwarzes Band `#262622`.

## Bewegung
- Laut Datei: keine Angaben – Hover-Zustände sind bewusst nicht dokumentiert, nur Druck-Zustände als Farbwechsel (`#cc001f`, `#c8c8c1`).
- Empfehlung: Dauer klein 180 ms / Screenwechsel 320 ms, Easing `cubic-bezier(.4, 0, .2, 1)`; Druck-Effekt Fläche dunkler plus `scale(.96)`; Einblenden der Kacheln als Deckkraft mit 6 px Aufsteigen, spaltenweise um 40 ms versetzt (Masonry baut sich von oben auf); Screenwechsel als Aufziehen der Pin-Karte zum Detail (Shared Element über das Bild); Fokus (TV) 4-px-Rahmen plus `scale(1.04)` in 180 ms.
- Compose: `tween(180, easing = CubicBezierEasing(0.4f, 0f, 0.2f, 1f))`, `animateItem()` im `LazyVerticalStaggeredGrid`, `AnimatedVisibility(fadeIn() + slideInVertically())`, Shared-Element-Übergang vom Pin zum Detailbild.

## Signatur-Elemente
1. Masonry-Raster aus randlosen 16-px-Kacheln mit 8-px-Fuge und erhaltenem Hochformat.
2. Weiße Overlay-Pille in der Bildecke (12 px 700, voller Radius) – die Marken-Geste.
3. Genau ein gesättigtes Rot `#e60023` pro Bildschirmhöhe, nur als Hauptaktion.
4. Pillen-Chips, die im aktiven Zustand komplett auf Schwarz invertieren.
5. Warm-cremefarbene Hülle ohne Schatten und ohne scharfe Ecken, dazu runde 40-px-Icon-Knöpfe.

## Übertragung auf eine App
- Startscreen: Pillen-Suchfeld und runder Knopf oben, Begrüßung 28 px, eine Feature-Karte (großes Bild 32 px, Overlay-Pille, Überschrift, roter Button), darunter Abschnittstitel und offenes Masonry.
- Liste und Übersicht: Suchfeld, Chip-Zeile (rechts angeschnitten), Zähler in 14 px 700, darunter zweispaltiges Masonry mit gemischten Formaten; Titel als Overlay-Pille, Angaben als 12-px-Zeile unter der Kachel.
- Detail: großes Bild mit 32 px Radius und runden Knöpfen darüber, Titel 28 px mit −1,2 px, Angabenzeile, Aktionszeile aus rotem Primär- und cremefarbenem Sekundärbutton, cremefarbene Musik-Karte, Chip-Umschalter, darunter ein dreispaltiges Masonry aus Bildausschnitten.
- Formulare und Einstellungen: Felder 44 px mit 16 px Radius, Label 16 px 600 darüber, Zeilen als cremefarbene Karten statt Trennlinien, am Ende ein roter Button über die volle Breite.
- Leere Zustände und Laden: cremefarbene Platzhalterkacheln in `#f6f6f3` mit 16 px Radius im Masonry-Rhythmus, darüber ein Satz 16 px und ein roter Button; kein Schimmer, keine Umrisse.
- TV: Masonry mit drei bis vier Spalten, Chips oben, Fokus als weißer Rahmen plus leichtes Vergrößern.
- Musterscreens: Start mit Feature-Karte „Herbstwald“ und offenem Masonry, Bibliothek als zweispaltiges Masonry mit Chip-Zeile und Overlay-Pillen, Album „Lissabon“ mit großem Pin, Aktionszeile, Musik-Karte und dreispaltigem Ausschnitt-Raster.

## Vermeiden
- Scharfe Ecken an Buttons, Feldern und Kacheln; ein vierter Radiuswert zwischen 16 und 32 px.
- Schatten auf Karten; Verläufe oder Scrims über Bildern; Rot als Zierde, für Links, Zustände oder mehr als eine Aktion pro Bildschirmhöhe.
- Pin-Karten mit Innenpolster oder Rahmen; gleichmäßiges Raster mit festem Seitenverhältnis statt Masonry; Querformate im Raster.
- Hierarchie über Farbtöne statt über Gewicht und Größe; dünne Linien-Icons; beschriftete Tableisten.
- Große Fugen im Raster (mehr als 8 px) und Weißraum zwischen Kacheln, der den Sammel-Eindruck zerstört.
