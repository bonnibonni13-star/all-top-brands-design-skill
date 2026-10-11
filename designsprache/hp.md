---
slug: hp
marke: HP
website: https://www.hp.com
ansatz: galerie
ansatz2: daten
modus: hell
aufbau: Weißes Katalog-Raster in Bändern: dunkles Ink-Band, weiße Leiste, weiße Bühne mit blauen Chevrons, Cloud-Band, Ink-Block
navigation: Dunkle Utility-Leiste oben + weiße Navigationsleiste; unten weiße Tab-Leiste, aktiv = 2-px-Unterstrich in Blau + 600
komponenten: Karten 16 px mit Soft Lift, Buttons 4 px versal gesperrt, Pill-Filter, Hairline-Zeilen, blaue Chevron-Schrägen
icons: Lucide-Linien, 1,75 px Strich, eckige Enden und Gehrung, 20–24 px, nie gefüllt (Empfehlung)
bewegung: Sachlich und kurz: 160/280 ms, cubic-bezier(.2,0,.2,1); Druck = Blau wird zu #0e3191, kein Skalieren
schrift: Eine Familie, Display immer Gewicht 500 bei Zeilenhöhe 1,0; nur Buttons versal mit +0,7 px
---
# HP – Designsprache

**Kurz:** Ein weißer Katalog, der in klar getrennten Bändern läuft: weiß, hellgrau (Cloud/Fog), dunkles Ink – mehr Flächenvokabular gibt es nicht. Genau eine Signalfarbe (Elektroblau) trägt Hauptaktion, Links und das Chevron-Motiv, höchstens zweimal pro Ansicht. Prägend ist die Zweiteilung der Form: Karten und Bildrahmen weich bei 16 px, Buttons und Felder scharf bei 4 px mit versalen, gesperrten Beschriftungen.

## Wirkung
- Charakter: sachlich, zugänglich, kaufmännisch; Technik-Katalog trifft Unternehmens-Produktseite.
- Passt zu: Shop- und Katalog-Apps, Geräte- und Verwaltungs-Apps, Support und Tarife, Business-Werkzeugen mit vielen Daten.
- Passt weniger zu: dunklen Medien- oder Nachtmodus-Apps, verspielten Marken, Apps mit vielen Akzentfarben.

## Aufbau und Raster
- Seitenaufbau: feste Bandfolge Utility (Ink) → Navigation (Weiß) → weißer Inhalt → Cloud-Band → Ink-Block → Ink-Fuß. Jede Ansicht wählt pro Abschnitt genau eine der Flächen Canvas #ffffff, Cloud #f7f7f7, Fog #e8e8e8, Ink #1a1a1a.
- Ausrichtung: linksbündig; Bühne als eine große Karte, Überschrift oben links darin.
- Raster: Basis 8 px (Halbschritt 4), Skala 4/8/12/16/20/24/32/80 px; Web 1366 px Container, Produktraster 4 → 3 → 2 → 1 Spalte, App 2 Spalten, Rinne 16 px.
- Dichte und Weißraum: Abschnittsabstand 80 px (Web) bzw. 32–40 px (App); Kartenpolster 24 px (Produkt), 32 px (Feature), 16 px (kompakte Kachel); Seitenrand App 20 px. Über und unter Bildern mindestens 16 px Luft.
- Rhythmus: Weiß und Grau wechseln sich ab, das dunkle Band schließt den Takt – Tiefe entsteht aus Flächenkontrast, nicht aus Schatten.

## Navigation
- Website: Utility-Leiste 36 px auf Ink (Caption 14 px, weiß) über der weißen Hauptleiste 64 px mit Wortmarke links, Kategorien mittig, Suche + Konto + Warenkorb rechts, 1 px Hairline unten. Aktive Seite bekommt 2 px Unterstrich in Primär-Blau.
- App (App-Muster der Marke, ergänzt als Empfehlung): dieselbe Doppelleiste oben – Ink-Streifen 32 px für Status- und Kontextangaben, darunter weiße Leiste 64 px mit Zeichen, Suchfeld (4 px, 1 px Steel) und zwei 24-px-Icons. Unten weiße Tab-Leiste 76 px mit 1 px Hairline oben, vier Ziele (Start, Bibliothek, Suche, Profil), Icon 24 px + Label 12 px; aktiv = Blau, Gewicht 600 **und** 2 px blauer Unterstrich unter dem Label. Die Leiste bleibt beim Scrollen stehen.
- Detail: weiße Leiste mit Zurück-Chevron und Beschriftung links, Nebenaktionen als 24-px-Icons rechts; der Ink-Streifen zeigt den Pfad.
- TV: horizontale Kategorien-Pillen oben; Fokus = Ink-Pille mit weißem Text und 2 px blauer Unterstrich (Empfehlung).

## Startscreen
- Ink-Utility-Streifen mit Nebenangaben (Abgleich, Speicher), darunter weiße Leiste mit Suche.
- Bühne: eine weiße Karte (16 px, Soft Lift) mit Bild im 16-px-Rahmen, Augenbrauen-Label 14 px, Titel 32 px Gewicht 500, Angaben 14 px Charcoal, darunter blaue Hauptaktion und Ink-Umriss-Aktion; links und rechts die blauen Chevron-Schrägen.
- Danach ein Ink-Block (16 px Radius) mit Kennzahlen und Quellen als weiß umrandete Pillen.
- Darunter ein Cloud-Band „Zuletzt hinzugefügt“ mit zweispaltigem Kartenraster, unten angeschnitten.

## Komponenten
- Buttons: Höhe 44 px, Radius 4 px, Polster 12 × 24 px, Beschriftung 14 px, Gewicht 600, **Versalien mit +0,7 px** – die einzige Stelle mit Sperrung. Primär = Blau #024ad8 auf Weiß (Druck #0e3191, gesperrt Steel #c2c2c2); Ink-Variante = #1a1a1a für Aktionen über Bildern; Umriss = Weiß mit 1 px Blau und blauem Text; Umriss-Ink = Weiß mit 1 px Ink. Textlink 16 px Gewicht 500 in Blau mit Unterstrich. Nie Radius über 4 px, nie Pill.
- Karten und Kacheln: Weiß, 16 px Radius, Polster 24 px (kompakt 16 px), Soft Lift `0 2px 8px rgba(26,26,26,.08)` – nur Produkt- und Preiskarten bekommen ihn. Feature-Karte auf Cloud #f7f7f7, 16 px, Polster 32 px. Dunkler Promo-Block: Ink, 16 px, weißer Text.
- Listen: eine weiße Karte (16 px, Soft Lift) als Behälter, Einträge darin durch 1 px #e8e8e8 getrennt – keine schwebenden Einzelzeilen. Zeile 68 px: Bild 56 px (8 px Radius), Titel 16 px Gewicht 500, Angaben 14 px Charcoal, rechts Wert 14 px Graphite + Chevron 18 px.
- Suche und Eingabefelder: Höhe 44 px (Suche in der Leiste 40 px), Radius 4 px, Polster 12 × 16 px, 1 px Steel #c2c2c2; Fokus = 1 px Ink, kein Schein. Platzhalter Graphite #636363.
- Chips, Tabs, Filter: Kategorie-Pillen, Polster 8 × 20 px (Touch 12 × 24), Text 16 px Gewicht 500. Inaktiv Weiß mit 1 px Hairline, aktiv Ink-Fläche mit weißem Text. Sale-Etikett: Coral #ff5050, 3 px Radius, 14 px Gewicht 700.
- Dialoge und Sheets: Weiß, 16 px Radius oben, Schatten `0 8px 24px rgba(26,26,26,.12)` – nur für flüchtige Überlagerungen.
- Signatur-Komponenten: blaues Chevron-Paar an den Rändern der Bühne; Ink-Utility-Streifen; Ink-Block als Abschluss; weiße Listenkarte mit Hairlines; versale Buttons.

## Icons
- Stil (Empfehlung; die Datei nennt nur 48-px-Kategorie-Icons und 24-px-Glyphen in der Leiste): schlichte Linien-Icons mit eckigen Enden und Gehrung – mechanisch, geometrisch, nie gefüllt, nie zweifarbig, nie in farbigen Kreisen.
- Größe und Strich: 24 px in Leisten und Kategorie-Karten (dort 48 px), 20 px in Zeilen, 18 px als Chevron, 16 px in Buttons; Strich 1,75 px auf 24er-Raster.
- Einsatz: Navigation, Zeilen-Chevrons, Suche, Nebenaktionen, Quellen. Kategorie-Karten kombinieren 48-px-Icon über Beschriftung. Icon-Knöpfe sind 44 × 44 px mit 4 px Radius und 1 px Rahmen – nie rund.
- Umsetzung: Compose `Icons.Sharp` bzw. Material Symbols Sharp, Gewicht 400, Füllung 0; iOS SF Symbols `.regular` ohne `.fill`; Web Lucide `stroke-width: 1.75` mit `stroke-linecap: square; stroke-linejoin: miter`.

## Bildsprache
- Laut Datei: Bühnen- und Produktfotos sitzen in 16-px-Rahmen ohne Rand; Produktbilder 1:1 auf Weiß, Motiv auf etwa 70 % der Fläche; Kundengeschichten 16:9 im selben Rahmen; Lifestyle-Fotos im Ink-Band randlos und ungerundet; keine runden Masken, Avatare sind 4-px-gerundete Quadrate; gleiche Bilddatei über alle Breiten, Zuschnitt horizontal.
- Übertragung: Bühnenbild 16:9 im 16-px-Rahmen; Kartenbild 4:3, 8 px; Listen-Vorschau 56 px, 8 px; Fotoraster 8 px Radius, 8 px Fuge. Keine Verläufe, keine Filter, keine Textüberlagerung auf dem Bild – Titel stehen darunter; nur ein Ink-Etikett (8 px) darf oben links auf dem Bild liegen.

## Typografie-Stimme
- Eine Familie für alles; Hierarchie über Größe und die Gewichte 400/500/600/700, nie über Laufweite (Ausnahme: Buttons).
- Display 72/56/44/32/24/20 px, **immer Gewicht 500**, Zeilenhöhe 1,0 (24 px: 1,17) – auch die größte Überschrift wird nicht fetter. App: Bühne 32 px, Screen-Titel 32 px, Kartentitel 20 px, Zeilentitel 16 px.
- Text 18/16 px, 400, Zeilenhöhe 1,33–1,4; Betonung 16 px 500; Caption 14 px 400 mit 1,5; Fett-Caption 14 px 700; Kleinstes 12 px (Untergrenze 11 px).
- Buttons 14 px 600 versal mit +0,7 px; kompakt 12,6 px 700. Kein Kursiv außer in Rechtshinweisen. Hierarchie nie über Deckkraft – stattdessen Charcoal #3d3d3d oder Graphite #636363.
- Freier Ersatz: Manrope (ohne Anpassung) oder Inter mit etwa 3 % größerem Schriftgrad; Zeilenhöhe für Display ausdrücklich auf 1,0 und für Text auf 1,4 setzen.

## Form, Tiefe und Material
- Radien: 0 Chevrons und randlose Bänder; 2 px Chips; 3 px Sale-Etikett; 4 px Buttons, Felder, Icon-Knöpfe, Avatare; 8 px Badges, Kategorie-Karten, kleine Vorschauen; 16 px Karten, Preisstufen, Bildrahmen; Pille nur für Kategorie-Tabs und Filter.
- Linien und Rahmen: 1 px Hairline #e8e8e8 für Trennung und Umriss-Elemente, 1 px Steel #c2c2c2 bei stärkerer Betonung (Felder, aktiver Filter), 2 px Blau als aktiver Indikator.
- Schatten und Ebenen: Stufe 0 flach (Bänder, randlose Bilder); Stufe 1 Hairline; Stufe 2 Soft Lift `0 2px 8px rgba(26,26,26,.08)` nur für Produkt- und Preiskarten; Stufe 3 `0 8px 24px rgba(26,26,26,.12)` nur für Überlagerungen.
- Besondere Oberflächen: blaue Chevron-Schrägen (Parallelogramme, Schnitt etwa 60°, ohne Radius und Schatten) als architektonisches Element an der Bühne. Entscheidung: Die Datei lässt sie auf Mobil verschwinden; in den Musterscreens bleiben sie angeschnitten stehen, weil sie das Signaturelement sind – sonst wäre die Marke nicht erkennbar. Keine Verläufe, kein Glas, keine Muster.

## Bewegung
- Laut Datei: nur Zustände – Primärfläche wechselt beim Druck auf #0e3191, Feld bekommt im Fokus 1 px Ink ohne Schein; keine Hover-Angaben.
- Empfehlung: Dauer klein 160 ms / Screenwechsel 280 ms, Easing `cubic-bezier(0.2, 0, 0.2, 1)`; Druck = Farbwechsel statt Skalieren; Einblenden = Karten 8 px von unten, gestaffelt 50 ms; Screenwechsel = horizontales Schieben; aktiver Tab-Unterstrich wandert in 200 ms; Fokus (TV) = Ink-Pille plus 2 px blauer Unterstrich.
- Compose: `tween(280, easing = CubicBezierEasing(0.2f, 0f, 0.2f, 1f))`, `animateColorAsState` für Druckzustände, `AnimatedVisibility(fadeIn() + slideInVertically { it / 16 })`, `animateItem()`; keine Feder mit Überschwingen.

## Signatur-Elemente
1. Blaues Chevron-Paar (scharfe Schrägen, 0 Radius) an den Rändern der Bühne.
2. Zweiteilige Form: Karten und Bildrahmen 16 px weich, Buttons und Felder 4 px scharf.
3. Versale, gesperrte Button-Beschriftungen in Elektroblau oder Ink.
4. Bandrhythmus Weiß → Cloud → Ink mit dunklem Streifen oben und dunklem Block als Abschluss.
5. Weiße Listenkarte mit 1-px-Hairline-Zeilen statt einzelner schwebender Zeilen.

## Übertragung auf eine App
- Startscreen: Ink-Utility-Streifen, weiße Leiste mit Suche, Bühnenkarte mit Chevrons und Blau-CTA, Ink-Block mit Kennzahlen und Quellen-Pillen, Cloud-Band mit zweispaltigem Kartenraster.
- Liste und Übersicht: Screen-Titel in der weißen Leiste, Suchfeld 4 px, Kategorie-Pillen, dann **eine** weiße Karte auf Cloud mit Hairline-Zeilen (Bild 56 px, Titel, Angaben, Wert, Chevron).
- Detail: Bild 16:9 im 16-px-Rahmen mit Ink-Etikett, Titel 32 px, Angaben in Charcoal, blaue Hauptaktion neben zwei eckigen Umriss-Icon-Knöpfen, Hairline-Zeile für die Diashow-Musik, Kategorie-Pillen, Fotoraster 8 px.
- Formulare und Einstellungen: Felder 44 px mit 4 px Radius und 1 px Steel, Label 14 px darüber, Hilfetext 12 px Graphite, Gruppen als weiße Karte mit Hairline-Zeilen; Hauptaktion unten als blauer Versal-Button über die volle Breite.
- Leere Zustände und Laden: weiße Karte mit 48-px-Icon, Satz 16 px, blauem Umriss-Button; Platzhalter als Fog-Flächen #e8e8e8 mit 4 bzw. 16 px Radius, kein Schimmer.
- TV: weißes Raster mit 16-px-Karten auf Cloud, Kategorie-Pillen oben, Fokus = Ink-Pille und 2 px blauer Rahmen (Empfehlung).
- Musterscreens: Start mit Chevron-Bühne, Ink-Kennzahlenblock und Kartenraster; Bibliothek als Pillen-Filter über einer weißen Hairline-Listenkarte; Album „Lissabon“ mit gerahmtem Bild, versalem Blau-Button und Fotoraster.

## Vermeiden
- Blau als Flächen- oder Bandfarbe und mehr als zwei blaue Elemente pro Ansicht.
- Weitere gesättigte Farben außer Coral (Sale) und den Storm-Tönen für Infografiken.
- Buttons über 4 px Radius oder als Pille; Karten unter 16 px Radius.
- Schwere Schatten, Schatten auf Bändern, Tiefe über Deckkraft statt Flächenwechsel.
- Gewicht über 500 bei Überschriften, Text unter 12 px, Sperrung außerhalb von Buttons.
- Chevrons als Dekoration in Karten oder Listen; runde Masken und runde Avatare.
