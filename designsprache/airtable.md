---
slug: airtable
marke: Airtable
website: https://airtable.com
ansatz: editorial
ansatz2: galerie
modus: hell
aufbau: Weiße Bahn mit viel Luft, unterbrochen von vollflächigen Signatur-Karten in Koralle, Waldgrün, Creme und Tintenschwarz.
navigation: Weiße Kopfleiste 64 px + untere Leiste mit vier Zielen; aktives Ziel als tintenschwarze 12-px-Fläche mit weißer Schrift
komponenten: Signatur-Farbkarten, Demo-Raster mit ungleichen Höhen, Creme-Callout, schwarzer CTA + weißer Umriss-Knopf
icons: Lucide, 20 px, Strich 1,75, runde Enden, immer in Tinte (#181d26) oder Weiß auf Farbkarten
bewegung: sachlich; 160/260 ms, cubic-bezier(.2,.6,.2,1), Druck dunkelt den CTA auf #0d1218, Karten blenden nur ein
schrift: Haas-Grotesk-Stimme (Ersatz Inter Display), Display im Gewicht 400, nie fett, Text 14 px, Beschriftungen 500
---
# Airtable – Designsprache

**Kurz:** Weiße Fläche, tintenschwarze Schrift, sehr viel Weißraum – und alle paar Abschnitte eine vollflächige Farbkarte in Koralle, Waldgrün, Creme oder Tintenschwarz, die den Takt bricht. Große Überschriften stehen im Gewicht 400: Betonung kommt aus Größe und Farbfläche, nie aus Fettschrift. Tiefe entsteht aus Farbblöcken, nicht aus Schatten.

## Wirkung
- Charakter: nüchtern-redaktionell, ruhig, erwachsen, mit gezielten Farbausbrüchen; „Magazin über Arbeitswerkzeuge“.
- Passt zu: Produktiv- und Verwaltungs-Apps, Sammlungen, Lese- und Lern-Apps, alles mit Kategorien und Listen.
- Passt weniger zu: dunkle Medien-Bühnen, Apps, die von Glanz, Verlauf oder Tiefe leben.

## Aufbau und Raster
- Seitenaufbau: 64-px-Kopfleiste → Textblock in Weiß → Signatur-Farbkarte → wieder Weiß → Creme-Callout → ggf. dunkle Karte. Nie zwei gleiche Flächen hintereinander.
- Ausrichtung: linksbündig, eine Spalte; Karten laufen über die volle Textbreite (16 px Rand in der App).
- Raster: 4-px-Basis (4/8/12/16/24/32/48 px), Abschnittsrhythmus 96 px auf Web, **in der App 28–32 px**; Rasterabstände 12–16 px.
- Dichte und Weißraum: locker. Kartenpolsterung 24 px (Web 32–48), Eingaben 44 px hoch, Zeilenhöhe Text 1,25.
- Rhythmus: Überschrift → ein bis zwei Zeilen Text → Luft → Farbkarte. Raster bewusst mit **ungleichen Kartenhöhen** (keine Tabellenoptik).

## Navigation
- Website: weiße 64-px-Kopfleiste, Links in 14 px, rechts Umriss-Knopf + schwarzer CTA; die Leiste bleibt auf jeder Seite hell, auch über dunklen Abschnitten.
- App (Empfehlung): oben eine weiße Leiste (Web 64 px, App 56–60 px) mit Zeichen links und zwei 40-px-Kreisknöpfen rechts (Haarlinie, Tinten-Icon, einer davon Avatar = Profil). Unten eine weiße Leiste mit 1-px-Haarlinie und vier Zielen (Start, Bibliothek, Suche, Profil), Icon 20 px über Beschriftung 12 px/500. Aktiv = **tintenschwarze Fläche mit 12 px Radius** und weißer Schrift – dieselbe Form wie der Haupt-Knopf; inaktiv = Tinte auf Weiß. Beim Scrollen bleiben beide Leisten stehen.
- TV: helle Fläche beibehalten, Fokus = tintenschwarze 12-px-Fläche mit weißer Schrift, Reihen mit 24-px-Abstand.

## Startscreen
- Begrüßung in 30–32 px/400 Tinte, darunter eine 14-px-Zeile mit Kennzahlen – ringsum Luft, kein Bild, kein Verlauf.
- Danach sofort eine **Signatur-Karte in Koralle** (#aa2d00, 12 px Radius, 24 px Polsterung): Versal-Beschriftung, Titel in Weiß 400, Angaben, weißer Umriss-Knopf und ein Bildausschnitt mit 10 px Radius innerhalb der Karte.
- Danach ein Demo-Raster aus zwei Spalten mit ungleich hohen Karten (Weiß mit Haarlinie, Pfirsich, Minze, Creme) und ein Creme-Callout mit Speicherzahl, 4-px-Balken und Quellen als Umriss-Chips.

## Komponenten
- Buttons: primär Tinte #181d26, weiße Schrift, 16/500, **Radius 12 px**, Polsterung 16/24 px (App: Höhe 48 px) – höchstens einer pro Bildschirmhöhe, Druck #0d1218. Sekundär: Weiß, Tintenschrift, 1 px #dddddd, gleicher Radius – auch auf Farbkarten bleibt er weiß. Kreisknopf 40 px mit Haarlinie. Pillen-Knöpfe nur im Preis-Dialekt, sonst nie.
- Karten und Kacheln: Signatur-Karten (Koralle #aa2d00, Waldgrün #0a2e0e, Tinte #181d26) 12 px Radius, weiße Schrift; Inhaltskarten 10 px Radius, 16 px Polsterung, Fläche Weiß + Haarlinie oder Pastell (Pfirsich #fcab79, Minze #a8d8c4, Creme #f5e9d4, Gelb #f4d35e, Senf #d9a441). **Keine Schatten.**
- Listen: Karten statt Zeilen; wo Zeilen nötig sind, 12 px Polsterung mit 1-px-Trenner #dddddd, Beschriftung links, Wert rechts.
- Suche und Eingabefelder: Weiß, 1 px #dddddd, **Radius 6 px**, Höhe 44 px, Polsterung 12/16 px, Text 14 px; Fokus = Rand in #458fff.
- Chips, Tabs, Filter: Umriss-Chips mit 6-px-Radius, 14 px/500, Haarlinie; aktiv = Tintenfläche, weiße Schrift, Zahl als Badge in halbtransparentem Weiß. Versal-Kategoriemarken (11 px, 0,12 em) über Kartentiteln.
- Dialoge und Sheets: weiße Fläche, 12 px Radius oben, 24 px Polsterung, Titel 20 px/400, Knöpfe in der Signaturpaarung (schwarz + weißer Umriss).
- Signatur-Komponenten: vollflächige Farbkarte, Creme-Callout, Demo-Raster mit ungleichen Höhen, Versal-Kategoriemarke, schwarzer CTA mit weißem Umriss-Partner.

## Icons
- Stil: schlichte Linien-Icons, geometrisch, runde Enden, mittlere Stärke (Lucide – Empfehlung; die Datei dokumentiert kein Icon-System).
- Größe und Strich: 20 px in Leisten und Knöpfen, 18 px in Karten, Strichstärke 1,75; Farbe Tinte #181d26, auf Farbkarten Weiß.
- Einsatz: zurückhaltend – Navigation, Kreisknöpfe, Quellen-Chips. Inhalte tragen Bilder und Text, keine Icon-Dekoration.
- Umsetzung: Compose `Icons.Outlined`/Material Symbols Rounded, Fill 0, Gewicht 400, 20 dp; iOS SF Symbols regular; Web Lucide stroke-width 1,75.

## Bildsprache
- Bilder sind **Ausschnitte in Karten**, nie randlose Bühnen: 10 px Radius innerhalb einer Karte, 12 px bei der großen Detailansicht, 16 px Außenrand.
- Seitenverhältnisse: 4:3 und 16:10 im Raster, 16:9 bei Artikelkarten, 1:1 für Avatare (Kreis).
- Farbe bleibt unverändert – die Bilder liefern Farbe, die Flächen liefern die Marke. Keine Verläufe, keine Tönung, keine Textauflage über dem Bild.
- Auf Farbkarten sitzt das Bild als Fragment innerhalb der Polsterung, sodass ringsum ein Farbrahmen stehen bleibt.

## Typografie-Stimme
- Großer Größenkontrast bei sehr geringem Gewichtskontrast: Display 30–32 px/**400**, Titel 20–24 px/400, Beschriftungen 16 px/500, Text 14 px/400 (Zeilenhöhe 1,25), Meta 14 px/500 mit 0,16 px Laufweite.
- Nie 600/700 im redaktionellen Teil; Betonung über Größe, Farbe und Fläche. Versalien nur als kleine Kategoriemarke.
- Freier Ersatz: **Inter Display** für Display und Titel, Inter für Text (laut Datei der empfohlene Ersatz für Haas), Zeilenhöhe rund 5 % enger.

## Form, Tiefe und Material
- Radien: 2 px nur für Rechtstexte, 6 px Eingaben und Chips, 10 px Inhaltskarten, 12 px CTA und Signatur-Karten, Kreis für Icon-Knöpfe und Avatare.
- Linien und Rahmen: 1 px #dddddd für Eingaben, Umriss-Knöpfe und Trenner; #9297a0 nur für deaktivierte Umrisse.
- Schatten und Ebenen: praktisch keine. Tiefe entsteht aus dem Farbkontrast zwischen weißer Bahn und Farbkarte (Prinzip „Farbblock vor Schatten“).
- Besondere Oberflächen: Pastellflächen für Rasterkarten, Creme für Callouts; keine Verläufe, kein Glas, keine Körnung.

## Bewegung
- Laut Datei: keine Angaben (Animation ausdrücklich nicht im Umfang).
- Empfehlung: klein 160 ms / Screenwechsel 260 ms, Easing `cubic-bezier(.2,.6,.2,1)`; Druck = CTA auf #0d1218 und `scale(.99)`, Karten `opacity` + 8 px nach oben, im Raster um 40 ms gestaffelt; Screenwechsel als Schieben nach links; Fokusring 2 px #458fff in 120 ms.
- Compose: `tween(160, easing = CubicBezierEasing(.2f,.6f,.2f,1f))`, `AnimatedVisibility(fadeIn() + slideInVertically { 8.dp.roundToPx() })`, `animateItemPlacement()` im Raster.

## Signatur-Elemente
1. Vollflächige Signatur-Karte in Koralle, Waldgrün oder Tinte mit weißer Schrift und weißem Umriss-Knopf.
2. Tintenschwarzer 12-px-CTA neben weißem Umriss-Knopf – immer als Paar.
3. Demo-Raster aus zwei Spalten mit **ungleichen Kartenhöhen** und Pastellflächen.
4. Creme-Callout (#f5e9d4) für Kennzahlen.
5. Große Überschriften im Gewicht 400 auf viel Weiß, dazu kleine Versal-Kategoriemarken.

## Übertragung auf eine App
- Startscreen: Begrüßung in 400, Koralle-Signaturkarte als Rückblick mit weißem Knopf, Demo-Raster „Zuletzt hinzugefügt“ mit ungleichen Höhen, Creme-Callout mit Speicher und Quellen-Chips.
- Liste und Übersicht: Titel 30 px/400, 44-px-Suchfeld mit 6 px Radius, Umriss-Filterchips (aktiv tintenschwarz mit Zahl), danach ein zweispaltiges Raster aus Karten mit Versal-Kategoriemarke, Bildausschnitt (10 px), Titel 16/500 und Meta 14 px; Musik- und Video-Einträge bekommen Pastellflächen, Alben weiße Karten mit Haarlinie.
- Detail: weiße Kopfzeile mit drei Kreisknöpfen, dann **Text vor Bild** (Titel 30 px/400 + Meta), Bild in 12-px-Karte, Knopfpaar „Diashow starten“ (Tinte) + „Teilen“ (Umriss), Creme-Callout für die Diashow-Musik, Umschalter als Chips, zum Schluss ein dreispaltiges Fotoraster mit 10 px Radius.
- Formulare und Einstellungen: Beschriftung 14/500 über dem Feld, Felder 44 px mit 6 px Radius, Abschnitte durch Haarlinien getrennt, Hilfetext 14 px #41454d, Aktionen als Knopfpaar unten.
- Leere Zustände und Laden: Creme- oder Pastellkarte mit Titel 20/400, einer Textzeile und einem Umriss-Knopf; Laden als hellgraue Flächen (#e0e2e6) in Kartenform, kein Spinner.
- TV: weiße Bahn beibehalten, Raster auf drei bis vier Spalten, Fokus als tintenschwarze Fläche, Signatur-Karten als ganze Reihen.
- Musterscreens: Start mit Koralle-Rückblick, ungleich hohem Demo-Raster und Creme-Speicherkarte, Bibliothek als zweispaltiges Karten-Raster mit Filterchips, Detail „Lissabon“ mit Text vor Bild, Knopfpaar und Creme-Musikkarte – alle drei mit heller Kopf- und Fußleiste.

## Vermeiden
- Kein Verlauf, kein Nebel, kein Leuchten hinter der Überschrift; Weiß ist die Atmosphäre.
- Display-Schrift nie fett (600/700); Link-Blau #1b61c9 nie als Knopf-Farbe – der Haupt-Knopf ist tintenschwarz.
- Pillen-Radien außerhalb des Preis-Dialekts vermeiden; keine Schatten unter Karten.
- Rasterkarten nicht alle gleich hoch (wirkt wie ein Datenblatt) und nie zwei gleiche Flächen hintereinander.
- Nicht mit anderen hellen Karten-Marken verwechseln: Airtable blockt **Farbflächen mit weißer Schrift** und setzt Bilder als Ausschnitte in Karten – es arbeitet nicht mit randlosen Fotokarten, runden Pillen und bunten Icons.
