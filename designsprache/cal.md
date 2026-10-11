---
slug: cal
marke: Cal.com
website: https://cal.com
ansatz: minimal
ansatz2: galerie
modus: hell
aufbau: Weiße Fläche, weich gerundete Karten (12 px) mit echten Produkt-Bausteinen darin; eine einzige dunkle Fläche schließt ab
navigation: Oben weiße 64-px-Leiste; Unterebene als Pillen-Gruppe (Pille in Pille); unten die eine dunkle Leiste mit 4 Zielen
komponenten: Pillen-Gruppe mit weißem Aktivsegment, Produkt-Karte mit Kalenderraster, graue Merkmal-Karte, Badge-Pille, 36-px-Kreise
icons: Linien-Icons 18–20 px, Strich 2, runde Enden, in Tinte; nie gefüllt, keine zweite Stärke
bewegung: ruhig und knapp; 150/250 ms, cubic-bezier(.2,0,0,1), Druck = #111111 → #242424, sonst nichts
schrift: Zwei Rollen – geometrische Display-Schrift (Cal Sans, Ersatz Poppins/Inter 600) mit −0,5…−2 px, Inter für alles andere
---
# Cal.com – Designsprache

**Kurz:** Freundliche, moderne SaaS-Oberfläche: weiße Fläche, viel Luft, weich gerundete Karten (8/12/16 px) und schwarze Hauptknöpfe – fast ohne Farbe. Die Spannung kommt aus zwei Dingen: einer geometrischen Display-Schrift mit negativer Laufweite für alle Überschriften und **echten Produkt-Bausteinen in den Karten** (Kalenderraster, Zeitlisten, Auswahlzeilen) statt gemalter Illustrationen. Genau eine dunkle Fläche pro Seite schließt sie ab.

## Wirkung
- Charakter: ruhig, sachlich-freundlich, aufgeräumt; wirkt wie durchdachte Software, ohne zu beeindrucken zu wollen.
- Passt zu: Terminen, Planung, Produktivität, Konten und Einstellungen, Medienverwaltung – allem, wo Struktur und Vertrauen zählen.
- Passt weniger zu: lauten Marken, dichten Datenwänden, dunklen Medien-Apps (das System kennt nur eine dunkle Fläche).

## Aufbau und Raster
- Seitenaufbau: Bänder im Wechsel Weiß → Hellgrau-Karte → Weiß → Produkt-Karte → Weiß → dunkler Abschluss. Nie zwei gleiche Flächen hintereinander.
- Ausrichtung: linksbündig; die Bühne ist am Desktop 7/5 geteilt (Überschrift links, Produkt-Karte rechts), mobil gestapelt: Text zuerst, Karte darunter.
- Raster: 4-px-Basis (4/8/12/16/24/32/48/96 px), Web max. 1200 px, Rinnen 24 px; Karten 3-up → 2-up → 1-up; in der App ein Seitenrand von 20 px (Empfehlung).
- Dichte und Weißraum: Bandabstand 96 px (mobil 32–40 px), Karteninnenabstand 32 px (kompakt 24 px, in der App 14–16 px), Knöpfe und Felder 40 px hoch. Großzügig, aber nicht leer.
- Rhythmus: Überschrift → ein Satz in Grau → eine Karte mit echtem Produkt-Baustein → eine Hauptaktion. Nie dichte Listenwände.

## Navigation
- Website: weiße 64-px-Kopfleiste, Zeichen links, Ziele mittig in 14/500, rechts Textlink und schwarzer Knopf; unter 768 px Burger und Vollbild-Sheet. Unterebenen laufen über die **Pillen-Gruppe**: grauer Rahmen #f8f9fa, Radius voll, 6 px Innenabstand, darin Segmente mit 8×14; aktiv weiß mit zartem Schatten.
- App (Empfehlung): weiße 64-px-Kopfleiste mit Zeichen, Titel und rundem 36-px-Icon-Knopf plus Avatar rechts (Ziel „Profil" auch hier). Unten die **eine dunkle Leiste** #101010 mit 4 Zielen – sie übernimmt die Rolle des dunklen Footers, der jede Seite schließt. Icon 19 px + Label 11/500; aktiv = weißer 38-px-Kreis mit tintenfarbenem Icon und Label in Weiß 600; inaktiv #a1a1aa. Filter und Umschalter immer als Pillen-Gruppe, nie als Unterstrich-Tabs.
- TV: weiße Fläche, Pillen-Gruppe oben, Karten 3-up; Fokus siehe Bewegung.

## Startscreen
- Begrüßung als Display-Zeile (28 px, Gewicht 600, −0,5 px Laufweite) mit einer grauen Zahlenzeile darunter – keine große Bühne, kein Vollbild.
- Direkt darunter die **Produkt-Karte**: Weiß, 1 px #e5e7eb, Radius 16, zarter Schatten, darin ein echter Baustein der App (Monatsraster mit Punkten an Tagen mit Aufnahmen, gewählter Tag als schwarzer Kreis) und als Abschluss eine Zeile mit Vorschaubild, Titel und schwarzem Knopf.
- Danach ein Abschnitt mit kleiner Überschrift und „Alle ›", darunter eine Reihe hellgrauer Karten (#f5f5f5, Radius 12) mit Bild (Radius 8), Titel 16/600 und Angaben 14/400 in Grau; die Reihe ist rechts angeschnitten.

## Komponenten
- Buttons: Primär #111111, Text weiß 14/600, Radius 8, Höhe 40, Padding 12×20; gedrückt #242424; deaktiviert #e5e7eb auf #6b7280. Sekundär weiß mit 1 px #e5e7eb, gleiche Maße. Runder Icon-Knopf 36 px, weiß mit Haarlinie. Textlink in Tinte, 14/600.
- Karten und Kacheln: drei Sorten mit klarer Bedeutung – **hellgraue Merkmal-Karte** (#f5f5f5, Radius 12, Padding 32/24) für Behauptungen, **weiße Produkt-Karte** (Radius 12, 1 px Haarlinie) für echte Oberfläche, **Bühnen-Karte** (Radius 16, zarter Schatten) für den Auftritt. Die dunkle Karte (#101010) gibt es nur als hervorgehobene Stufe – sonst nirgends.
- Listen: weiße Karte mit 1 px #e5e7eb und Radius 12, darin Zeilen à 60 px, getrennt durch #f3f4f6; links Bild 40 px mit Radius 8, Titel 16/600, Angaben 14/400 #6b7280, rechts Badge-Pille oder Chevron. Gruppen bekommen eine kleine Überschrift über der Karte.
- Suche und Eingabefelder: weiß, 1 px #e5e7eb, Radius 8, Höhe 40, Padding 10×14, Text 16/400, Platzhalter #6b7280; Fokus = Rand wird tintenfarben oder dicker (keine Leuchtfarbe).
- Chips, Tabs, Filter: ausschließlich die Pillen-Gruppe (grauer Rahmen, weißes Aktivsegment mit Schatten; Segmentradius 8 laut Token-Tabelle, der Rahmen ist voll gerundet – der Fließtext der Datei nennt das Segment „Pille", die Tabelle gewinnt). Badge-Pille: #f5f5f5, Text Tinte, 13/500, Radius voll, 4×12; Pastelltöne (#fb923c, #ec4899, #8b5cf6, #34d399) nur auf Badges und Avataren, nie auf Knöpfen.
- Dialoge und Sheets (Empfehlung): weißes Sheet, Radius 16 oben, 24 px Innenabstand, Griff als graue Pille, Hauptknopf schwarz über die volle Breite.
- Signatur-Komponenten: Pillen-Gruppe (Pille in Pille); Produkt-Baustein in der Karte; 36-px-Kreise (Avatar, Icon-Knopf); die eine dunkle Fläche als Abschluss.

## Icons
- Stil: schlichte Linien-Icons mit runden Enden, einfarbig in Tinte oder Grau, nie gefüllt, nie zweifarbig (Empfehlung – die Datei beschreibt Icons nicht).
- Größe und Strich: 18–20 px bei 2 px Strich, in runden 36-px-Knöpfen 16–18 px; Chevrons in #6b7280.
- Einsatz: Icons stehen neben Text, nicht über ihm; Aktivzustände zeigt die weiße Pille oder der weiße Kreis, nicht das Icon.
- Umsetzung: Compose `Icons.Rounded` bzw. Material Symbols Rounded (Gewicht 400, Füllung 0); iOS SF Symbols Regular ohne Füllung; Web Lucide mit `stroke-width: 2`.

## Bildsprache
- Bilder sind Inhalt in Karten, nicht Bühne: immer eingerückt mit Radius 8 (in Karten) bzw. 16 (Bühnen-Karte), nie randlos über den Screen.
- Seitenverhältnisse 16:9 oder 4:3 in Karten, 1:1 im Raster; Raster mit 8-px-Fugen und 8 px Radius.
- Keine Verläufe, keine Körnung, kein Text auf dem Bild – Beschriftung steht unter oder neben dem Bild. Avatare sind perfekte Kreise mit 36 px, gern mit Pastellfüllung.
- Statt gemalter Illustrationen lieber ein echter Oberflächen-Ausschnitt der App (Kalender, Zeitliste, Auswahlzeile) als „Bild".

## Typografie-Stimme
- Strikte Zweiteilung: **Display** (Cal Sans) für alle Überschriften – Gewicht 600, niemals 700 oder 500, mit negativer Laufweite −2 px (64) / −1,5 px (48) / −1 px (36) / −0,5 px (28); **Inter** für alles andere – Titel 22/18/16 in 600, Text 16/400/1,5, klein 14/400, Caption 13/500, Button 14/600, Navigation 14/500.
- Die Laufweite gehört zur Stimme: Display ohne negatives Tracking wirkt falsch. Größer schlagen heißt größer setzen, nicht fetter.
- Fließtext niemals in der Display-Schrift, Überschriften niemals in Inter. Keine Versalien, keine Kursive; Mono (JetBrains Mono, 14/400) nur für Code.
- Freier Ersatz: Inter 600 mit −0,04 em (laut Datei) oder Manrope 700; in den Musterscreens Poppins (geometrisch, mittleres Gewicht) für Display und Inter für den Rest.

## Form, Tiefe und Material
- Radien gestuft nach Bedeutung: 6 px kleine Knöpfe, **8 px** Knöpfe, Felder, Bilder in Karten und Segmente, **12 px** Inhaltskarten, **16 px** Bühnen-Karte, voll für Pillen-Gruppe, Badges, Avatare und Icon-Knöpfe. Über 16 px wirkt es nach Consumer-App.
- Linien und Rahmen: 1 px #e5e7eb an Feldern, Karten und Tabellen; #f3f4f6 als kaum sichtbarer Trenner innerhalb einer weißen Karte.
- Schatten und Ebenen: zwei sehr zarte Stufen – `0 1px 2px rgba(0,0,0,.05)` und `0 4px 12px rgba(0,0,0,.08)`. Sonst arbeitet der Flächenwechsel (#ffffff ↔ #f5f5f5 ↔ #101010). Kein Neumorphismus, kein Glas.
- Besondere Oberflächen: #f8f9fa nur als Rahmen der Pillen-Gruppe; #101010 als einzige dunkle Fläche.

## Bewegung
- Laut Datei: ausdrücklich keine Hover-Zustände dokumentiert; belegt ist nur der Druckzustand #111111 → #242424. Zeiten für Kalender und Bestätigung sind nicht erfasst.
- Empfehlung: klein 150 ms, Screenwechsel 250 ms, Easing `cubic-bezier(0.2, 0, 0, 1)`; Einblenden 6 px von unten mit Opazität, 40 ms gestaffelt; das Aktivsegment der Pillen-Gruppe gleitet in 200 ms an seine neue Stelle (einziger gleitender Effekt im System); Druck auf Karten = 0,99-fach, kein Schattenwechsel; Fokus (TV) 2-px-Tintenrahmen mit 3 px Abstand plus Schattenstufe 2.
- Compose: `tween(150, easing = CubicBezierEasing(0.2f, 0f, 0f, 1f))`, Screens `tween(250, …)`; Pillen-Segment als `animateDpAsState`; `AnimatedVisibility(fadeIn() + slideInVertically { it / 16 })`; `Modifier.animateItem()`.

## Signatur-Elemente
1. Pillen-Gruppe: grauer voll gerundeter Rahmen mit weißem Aktivsegment und zartem Schatten.
2. Echter Produkt-Baustein in einer weißen Karte mit Radius 16 (hier: Monatsraster mit Aufnahme-Punkten).
3. Schwarzer Hauptknopf mit 8 px Radius – die einzige kräftige Fläche auf hellem Grund.
4. Dreiklang der Karten: hellgrau = Behauptung, weiß mit Haarlinie = echte Oberfläche, dunkel = genau einmal als Abschluss.
5. Display-Überschrift mit negativer Laufweite über einer grauen Einzeiler-Zeile.

## Übertragung auf eine App
- Startscreen: weiße Kopfleiste, Begrüßung in Display-Schrift, graue Zahlenzeile, Produkt-Karte mit Monatsraster und Abschlusszeile (Vorschaubild + schwarzer Knopf), darunter eine angeschnittene Reihe hellgrauer Karten.
- Liste und Übersicht: Titel, Suchfeld mit Haarlinie, Pillen-Gruppe als Filter, danach nach Gruppen getrennte weiße Karten mit 60-px-Zeilen, Bild 40 px (Radius 8), Angaben in Grau und Badge-Pille rechts.
- Detail: eingerückte Bühnen-Karte (Radius 16) mit Bild und einer inneren Abschlusszeile für die Diashow-Musik, darunter Titel, Badge-Pillen, schwarzer Hauptknopf neben runden Icon-Knöpfen, Pillen-Gruppe als Umschalter und ein 3-up-Raster mit 8-px-Fugen.
- Formulare und Einstellungen: weiße Karte mit Haarlinie, Zeilen 60 px mit Trenner #f3f4f6, Beschriftung 16/600 links, Wert oder Schalter rechts; Felder 40 px, Radius 8; Hauptknopf schwarz unten rechts.
- Leere Zustände und Laden: hellgraue Karte, Titel in Display 22–28, ein Satz in #6b7280, ein schwarzer Knopf; Laden als #f3f4f6-Blöcke mit denselben Radien.
- TV: weiße Fläche, Karten 3-up, Pillen-Gruppe oben, Fokus siehe Bewegung.
- Musterscreens: Start mit Begrüßung, Kalender-Produktkarte und angeschnittener Kartenreihe; Bibliothek mit Suchfeld, Pillen-Gruppe und gruppierten Listenkarten; Detail mit eingerückter Bühnen-Karte samt Musikzeile, Badge-Pillen, schwarzem Knopf und 3-up-Raster.

## Vermeiden
- Farbige Hauptknöpfe (auch nicht das Markenblau #3b82f6) und Pastelltöne auf Aktionen – das System ist auf der Handlungsebene einfarbig.
- Display-Schrift in Gewicht 700 oder ohne negative Laufweite; Fließtext in der Display-Schrift; Versal-Überschriften.
- Radien über 16 px an Karten, harte Ecken, kräftige Schatten, Glas- oder Verlaufsflächen.
- Weitere dunkle Flächen neben dem Abschluss; zwei gleiche Flächen in aufeinanderfolgenden Bändern.
- Dichte Listenwände ohne Karten, Unterstrich-Tabs statt der Pillen-Gruppe, gemalte Produkt-Illustrationen statt echter Oberfläche.
