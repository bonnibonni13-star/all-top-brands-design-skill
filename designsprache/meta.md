---
slug: meta
marke: Meta
website: https://www.meta.com
ansatz: galerie
ansatz2: buehne
modus: hell
aufbau: Reines Weiß als Bühne; Inhalte als große Fotokarten mit 32 px Radius, dazwischen viel Luft
navigation: Keine untere Leiste – oben eine Pillen-Reiter-Reihe mit 4 Zielen, aktiv als dunkel gefüllte Pille
komponenten: Fotokarte 32 px, Pillen-Knöpfe (Radius 100), runde 40-px-Icon-Knöpfe, Kachelraster, Kennzahl-Tabelle
icons: Phosphor Regular, 20–22 px, geometrisch-rund, nie gefüllt; in weißen Kreisen mit Haarlinie
bewegung: Empfehlung – sachlich, 180 ms klein / 250 ms Screen, ease-out; Pille drückt auf Charcoal, kein Federn
schrift: Geometrisch-humanistisch (Optimistic VF → Poppins): 500 Display, 300 Zwischentitel, 700 Buttons
---
# Meta – Designsprache

**Kurz:** Ein Händler-Layout aus großen, randlos bebilderten Karten mit sehr großen Radien auf reinem Weiß. Alles Bedienbare ist eine Pille, alles Kreisrunde ist ein Icon-Knopf. Die Hierarchie entsteht aus drei Gewichten derselben Schrift – 500 für Display, 300 für Zwischenüberschriften, 700 für Knöpfe und Labels.

## Wirkung
- Charakter: selbstbewusst, produktverliebt, sachlich-freundlich; nie verspielt, nie technisch
- Passt zu: Shop- und Katalog-Apps, Hardware- und Produkt-Apps, Medien-Bibliotheken mit starken Bildern
- Passt weniger zu: dichten Datenwerkzeugen, Terminal-Ästhetik, dunklen Kino-Oberflächen

## Aufbau und Raster
- Seitenaufbau: dünnes dunkles Hinweisband ganz oben, darunter weiße Leiste, darunter Pillen-Reiter, dann eine Folge großer Karten
- Ausrichtung: links; Fotokarten laufen bis 16 px an beide Ränder, Text sitzt 16–24 px innerhalb der Karte
- Raster: 4-px-Basis mit 8 px als Hauptschritt; Abstände 4/8/10/12/16/20/24/32/40, Bandrhythmus 64–80 px (App 20–24 px)
- Dichte und Weißraum: Kartenpolster 32 px (App 16–20 px), Spaltenabstand 24 px (App 12 px), Bild bekommt 50–70 % der Fläche
- Rhythmus: eine große Bildkarte, dann ein Kachelraster, dann eine ruhige helle Karte – Bild, Auswahl, Erklärung

## Navigation
- Website: weiße 64-px-Leiste mit Pillen-Reitern in der Mitte, Such-Pille und runden Icon-Knöpfen rechts; darüber ein volles Hinweisband
- App: **keine Tab-Leiste unten.** Oben eine Reihe Pillen-Reiter (Start, Bibliothek, Suche, Profil) in 14 px/700; inaktiv weiß mit 1-px-Rand #ced0d4, aktiv #0a1317 gefüllt mit weißer Schrift und ohne Rand. Die Reihe scrollt waagerecht und bleibt beim Scrollen oben stehen. Im Detail ersetzt ein Brotkrumenpfad die Reiter
- TV: Reiterreihe oben bleibt; Fokus = Pille füllt sich dunkel und wächst auf 1,06

## Startscreen
- Dunkles Hinweisband mit einer Zeile Status und einem Textlink rechts
- Weiße Leiste mit neutralem Zeichen links, Glocke und Avatar rechts; darunter die Pillen-Reiter
- Große randlose Fotokarte (32 px) mit Verlauf nach unten, gelbem Hinweis-Pill, Titel in 28–30 px/500 und zwei Pillen (gefüllt + Umriss)
- Darunter eine waagerechte Kachelreihe und eine ruhige helle Karte (#f1f4f7, 24 px) mit Quellen

## Komponenten
- Buttons: alles Pille (Radius 100). Primär schwarz #000, weiße Schrift 14/700, Polster 14×30 px; Kauf-/Abschlussaktion in Kobalt #0064e0 (**Übertragung:** die eine ausführende Hauptaktion des Screens, z. B. „Diashow starten“); Sekundär transparent mit 2-px-Rand #0a1317; auf Foto beides in Weiß
- Karten und Kacheln: Fotokarte 32 px ohne Rand und ohne Schatten (das Bild ist die Oberfläche); Inhaltskarte 16 px mit 1-px-#dee3e9; ruhige Karte #f1f4f7 mit 24 px; Produktkachel 1:1 oder 4:3 auf #f1f4f7 mit 16 px
- Listen: keine klassischen Zeilen, sondern Kennzahl-Tabelle – Label 14/700 links, Wert 14/400 rechts, 1-px-#dee3e9 dazwischen
- Suche und Eingabefelder: Such-Pille auf #f1f4f7, 40 px hoch, Lupe links, Text #5d6c7b; Textfeld 8 px Radius, 44 px, 1-px-#ced0d4, Fokus 2-px-#1876f2
- Chips, Tabs, Filter: dieselbe Pille wie die Reiter – weiß mit Haarlinie, aktiv dunkel gefüllt
- Dialoge und Sheets: weißes Blatt mit 32 px oben; feste untere Leiste mit Schatten `rgba(20,22,26,.3) 0 1px 4px`
- Signatur-Komponenten: Galerie mit senkrechtem Miniaturstreifen links (52 px, 8 px Radius, aktiv 2-px-Rand in Ink); feste untere Abschlussleiste mit Info links und Kobalt-Pille rechts; gelbe Hinweis-Pille #f7b928

## Icons
- Stil: geometrisch-runde Linien (Phosphor Regular) – gleiche Rundung wie die Schrift, nie gefüllt, nie kantig
- Größe und Strich: 20 px in Leisten und Zeilen, 22 px in runden 40-px-Knöpfen, 32 px in Erklärkacheln
- Einsatz: immer entweder in einem weißen Kreis mit 1-px-Haarlinie oder als stiller Anker vor einer Zeile; Pillen-Reiter bleiben reiner Text
- Umsetzung: Compose `Icons.Rounded` bzw. Material Symbols Rounded, Gewicht 400, Fill 0; iOS SF Symbols Regular ohne Füllung; Web Phosphor `regular`

## Bildsprache
- Fotos sind die Oberfläche: randlos in der Karte, 32 px Radius, nie mit Rahmen oder Schatten
- Verhältnisse: 1:1 für Auswahlkacheln, 4:3 für die Galerie, 16:9 für breite Bänder
- Über dunkle Bildteile legt sich ein Verlauf `rgba(10,19,23,0)` → `.72`, damit weißer Text trägt – kein Grau-, Duplex- oder Sepiafilter
- Miniaturen behalten ihren 8-px-Radius in jeder Größe und werden nie vollbreit

## Typografie-Stimme
- Drei Stufen einer Familie: Display 28–64 px/500, Zwischenüberschrift 18–28 px/**300**, Text 14–16 px/400, alles Bedienbare 14 px/700
- Laufweite −0,14 px bei 14 px und −0,16 px bei 16 px; Zeilenhöhe nie unter 1,5 im Fließtext
- Die 300er-Zwischenüberschrift ist der Signaturmoment – sie schafft Ruhe zwischen 500er Display und 400er Text
- Freier Ersatz: Poppins (300/400/500/700) als nächster freier Ersatz für Optimistic VF; alternativ Montserrat

## Form, Tiefe und Material
- Radien: 2/4/6 px Mikro, 8 px Felder und Miniaturen, 16 px Inhaltskarten, 24 px ruhige Karten, 32 px Fotokarten, 40 px Bühnenpanele, 100 px alle Pillen, Kreis für Swatches
- Linien und Rahmen: 1 px #dee3e9 an Karten und Tabellenzeilen, 1 px #ced0d4 an Feldern, 2 px Ink am Umriss-Knopf und an der aktiven Miniatur
- Schatten und Ebenen: flach. Nur zwei Ausnahmen: aktiver Reiter `rgba(0,0,0,.2) 1px 1px 0` und feste Leiste `rgba(20,22,26,.3) 0 1px 4px`
- Besondere Oberflächen: #f1f4f7 als einzige ruhige Fläche, #0a1317 als dunkles Band; keine Verläufe außer über Fotos

## Bewegung
- Laut Datei: nicht erfasst; empfohlen werden dort 150–250 ms ease-out für Flächen und 300 ms ease-in-out fürs Aufklappen
- Empfehlung: Dauer klein 180 ms / Screenwechsel 250 ms, Easing `cubic-bezier(.2, 0, 0, 1)`, Druck-Effekt Pille wird #444950 (kein Skalieren), Einblenden der Karten um 12 px von unten, Screenwechsel als Querschieben, Fokus (TV) Pille füllt sich und wächst auf 1,06
- Compose: `tween(250, easing = CubicBezierEasing(.2f, 0f, 0f, 1f))`, Aufklappen `tween(300, FastOutSlowInEasing)`, Galerie-Wechsel als Shared-Element zwischen Miniatur und großem Bild

## Signatur-Elemente
1. Randlose Fotokarte mit 32 px Radius – das Bild ist die Oberfläche, kein Rahmen, kein Schatten
2. Alles Bedienbare als Pille mit Radius 100, nie eckig
3. Pillen-Reiter oben statt Tab-Leiste unten, aktiv dunkel gefüllt
4. Galerie mit senkrechtem Miniaturstreifen links und 2-px-Ink-Rand an der aktiven Miniatur
5. Dünnes dunkles Hinweisband über der Leiste und gelbe Hinweis-Pille im Bild

## Übertragung auf eine App
- Startscreen: Hinweisband, Leiste, Pillen-Reiter, dann eine große Fotokarte mit zwei Pillen, eine waagerechte Kachelreihe und eine ruhige #f1f4f7-Karte
- Liste und Übersicht: Such-Pille, Filter als Pillen, danach ein 2-spaltiges Kachelraster – Bildkachel auf #f1f4f7 mit 16 px, Name 14/700 und Angabe 14/400 **unter** der Kachel
- Detail: Brotkrumenpfad, Galerie mit Miniaturstreifen links, Titel 500 über Zwischenzeile 300, Kennzahl-Kacheln, Pillen-Reiter für Fotos/Videos/Orte, feste untere Leiste mit Kobalt-Pille
- Formulare und Einstellungen: Auswahlkarten mit 8 px Radius, ausgewählt 2-px-Rand in tiefem Kobalt; Felder 44 px; genau eine Pille schließt ab
- Leere Zustände und Laden: #f1f4f7-Fläche mit 32 px Radius, Linien-Icon 32 px, eine Zeile in 300; Platzhalter als graue 16-px-Flächen
- TV: Fotokarten als Reihe, Titel 48 px/500, Pillen-Fokus
- Musterscreens: Start mit Fotobühne und Kachelreihe, Bibliothek als Kachelraster mit Pillenfiltern, Detail als Galerie mit Miniaturstreifen und fester Kobalt-Leiste

## Vermeiden
- Keine eckigen Knöpfe – die Pille ist gesetzt; auch kein 8-px-Kompromiss
- Kobalt nicht als allgemeine Markenfarbe verwenden; es gehört allein der abschließenden Aktion
- Keine weiteren Akzentfarben außer Kobalt (und Lila für VR-Kontexte)
- Fotokarten nie unter 32 px runden und nie mit Rahmen oder Schatten versehen
- Zeilenhöhe im Fließtext nicht unter 1,5 drücken – die negative Laufweite reicht als Verdichtung
- Schatten sind ein Signal für feste Leisten, kein Gestaltungsmittel für Karten
