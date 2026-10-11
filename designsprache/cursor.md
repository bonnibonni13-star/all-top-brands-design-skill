---
slug: cursor
marke: Cursor
website: https://cursor.com
ansatz: werkzeug
ansatz2: editorial
modus: hell
aufbau: Warme Cremefläche, darauf weiße Flächen mit 1-px-Haarlinie und 12 px Radius; Tabelle statt Karten
navigation: Obere Textreiter mit 2-px-Unterstrich, Avatar rechts, dazu eine angedockte Befehlszeile unten
komponenten: Haarlinien-Panel, Stufen-Zeitleiste mit Pastellpillen, Datentabelle, orangefarbener 8-px-Knopf
icons: Lucide, Strich 1.25–1.5, eckige Enden und Gehrung, 15–18 px, nie gefüllt
bewegung: Knapp und sachlich, 120/220 ms, cubic-bezier(.2,.8,.2,1), Zeilen blenden gestaffelt ein
schrift: Display im Gewicht 400 mit −1.5 % Laufweite; alle Zahlen, Pfade und Zeiten im Monospace
---
# Cursor – Designsprache

**Kurz:** Eine warme Cremefläche statt Weiß, darauf weiße Flächen, die nur durch eine 1-px-Haarlinie definiert sind – keine Schatten, keine Ebenen. Die Überschriften bleiben im Gewicht 400 mit enger Laufweite und klingen dadurch eher nach Magazin als nach Technik. Den technischen Ton liefert stattdessen das Monospace: jede Zahl, jeder Pfad, jede Zeitangabe wird mono gesetzt, dazu winzige Versal-Labels und fünf Pastellpillen für Verarbeitungsstufen.

## Wirkung
- Charakter: ruhig, sachlich, handwerklich; warm statt kühl, trotz Werkzeug-Charakter nie technisch-düster.
- Passt zu: Werkzeugen, Entwickler- und Verwaltungsapps, allem mit Dateien, Vorgängen, Protokollen und Fortschritt.
- Passt weniger zu: bildgetriebenen Lifestyle-Apps, Marken mit lauter Typografie, verspielten Oberflächen.

## Aufbau und Raster
- Seitenaufbau: Cremefläche `#f7f7f4` als Boden; Inhalte sitzen entweder direkt darauf (Tabellen, Listen) oder in weißen Panels `#ffffff` mit 1 px `#e6e5e0` und 12 px Radius.
- Ausrichtung: linksbündig für Text, **rechtsbündig für alle Zahlen** – Zahlen stehen in einer eigenen Monospace-Spalte.
- Raster: Basis 4 px, Stufen 4/8/12/16/20/24/32/48, Abschnittsrhythmus 80 px am Desktop (mobil 28–32 px); Container 1200 px, 12 Spalten.
- Dichte und Weißraum: Seitenrand 16–20 px, Panelpolster 16–24 px, Tabellenzeile 50–54 px, Zeilenabstand in Panels 12–16 px. Dichter als eine Marketing-Seite, luftiger als eine klassische Tabelle.
- Rhythmus: Versal-Label → Überschrift 400 → Monospace-Zeile → Panel. Jeder Abschnitt beginnt mit einem 11-px-Versal-Label.

## Navigation
- Website: 64 px hohe Leiste auf der Cremefläche, Wortmarke links, 5–6 Textlinks (14 px/500), rechts ein orangefarbener Primärknopf.
- App: **obere Textreiter** statt unterer Leiste – Marke links, 3 Ziele als Text (Start, Bibliothek, Suche), aktiv in Ink mit 2 px Unterstrich, inaktiv `#807d72`; Profil als 28-px-Avatar ganz rechts. Darunter eine 1-px-Haarlinie über die volle Breite. Unten dockt eine **Befehlszeile** an (weißes Feld, Haarlinie, 8 px Radius, Monospace-Platzhalter, orangefarbener Senden-Knopf) – das App-Gegenstück zur Eingabeleiste des Editors. App-Muster der Marke (nicht in der Datei), aus Produkt-Mockups abgeleitet.
- TV: linke Spalte mit Textzielen, Fokus als 2 px Unterstrich plus hellere Fläche.

## Startscreen
- Versal-Label, dann eine Begrüßung in 28–30 px/400 mit −1.5 % Laufweite, darunter eine Monospace-Zeile mit den Gesamtzahlen.
- Ein weißes Panel als Aufmacher (Bild im Panel, Versal-Badge, Titel 22 px/400, Monospace-Angaben, orangefarbener Knopf).
- Darunter das Signaturstück: die Stufen-Zeitleiste der Quellen mit Pastellpillen und Monospace-Pfaden.

## Komponenten
- Buttons: Primär = Orange `#f54e00`, weiße Schrift, **8 px Radius**, Polster 10/18 px, Höhe 40 px, Label 14 px/500. Sekundär = weiß mit 1 px `#cfcdc4`, gleiche Maße. Dunkel = Ink `#26251e` mit Cremeschrift, Höhe 44 px. Tertiär = reiner Textlink in Ink. Orange kommt höchstens einmal pro Screen vor.
- Karten und Kacheln: weiße Panels, 12 px Radius, 1 px `#e6e5e0`, Polster 16–24 px, **kein Schatten**. Innenflächen (Bild, Code, Vorschau) in `#fafaf7` mit 8 px Radius.
- Listen: als **Tabelle** – Kopfzeile in 11 px/600 Versalien mit +0.88 px Laufweite in `#807d72`, Zeilen durch 1 px `#efeee8` getrennt, kein Kasten darum. Links ein 32-px-Bild mit 4 px Radius, dann Titel 15 px/600, rechts zwei Monospace-Spalten (Menge, Datum).
- Suche und Eingabefelder: weiß, 1 px `#cfcdc4`, 8 px Radius, Höhe 44 px, Platzhalter im Monospace, links ein Tastenkürzel-Täfelchen (4 px Radius, `#e6e5e0`).
- Chips, Tabs, Filter: Reiter als Text mit Unterstrich; Filter als kompakte 6-px-Chips, inaktiv weiß mit Haarlinie, aktiv Ink-Fläche mit Cremeschrift. Badges als Pille in `#e6e5e0` mit 11-px-Versalien.
- Dialoge und Sheets: weißes Panel, 12 px Radius, 1 px Haarlinie, keine Verdunklung mit Weichzeichner – nur Ink bei 40 %.
- Signatur-Komponenten: die **Stufen-Zeitleiste** – eine senkrechte Haarlinie, daran Zeilen aus Pastellpille (11 px Versalien) + Monospace-Pfad + rechter Monospace-Wert. Pillenfarben: Pfirsich `#dfa88f`, Mint `#9fc9a2`, Blau `#9fbbe0`, Lavendel `#c0a8dd`, Gold `#c08532` (weiße Schrift).

## Icons
- Stil: feine Linien-Icons mit **eckigen Enden und Gehrung** (Lucide, `stroke-linecap: square; stroke-linejoin: miter`) – technisch, nie gefüllt, nie rund abgeschlossen.
- Größe und Strich: 15–18 px bei `stroke-width: 1.25–1.5`; in Knöpfen 16 px, in Tabellenzeilen 15 px.
- Einsatz: sparsam – Chevrons, Abspielen, Teilen, Mehr, Filter. Dateiarten werden durch Monospace-Text benannt, nicht durch Icons.
- Umsetzung: Compose `Icons.Sharp` bzw. Material Symbols Sharp, Gewicht 200–300, Füllung 0; iOS SF Symbols `.light`; Web Lucide mit `stroke-width: 1.5` und eckigen Enden.

## Bildsprache
- Bilder sind **Inhalt in einem Panel**, nicht Bühne: sie liegen in einer weißen Fläche, bekommen 8 px Radius und eine 1 px Haarlinie.
- Kleine Vorschaubilder in Tabellen mit 4 px Radius bei 32 px – fast wie Dateisymbole.
- Raster sind eng (6–8 px Abstand, 4 px Radius), weil sie als Dateiübersicht gelesen werden, nicht als Galerie.
- Keine Verläufe, keine Überblendungen, kein Text auf dem Bild; Beschriftung steht immer darunter oder daneben.

## Typografie-Stimme
- Eine Textschrift für alles, **Display im Gewicht 400** mit negativer Laufweite: 72/−2.16 px (Web-Hero), mobil 28–30 px/−1.5 %, 26 px/−0.33 px, 22 px/−0.11 px. Nie 700.
- Titel und Labels 600 bei 15–18 px, Fließtext 400 bei 15–16 px mit Zeilenhöhe 1.5, `#5a5852`.
- Versal-Label 11 px/600 mit +0.88 px Laufweite – das einzige Versal-Element.
- **Monospace für jede Zahl, jeden Pfad, jede Dauer** (13 px/400). Dieser Wechsel trägt die halbe Stimme der Marke.
- Freier Ersatz: **Inter** 400 mit `letter-spacing: -1.5%` für Display; **JetBrains Mono** (ersatzweise DejaVu Sans Mono) für alle Monospace-Flächen.

## Form, Tiefe und Material
- Radien: 4 px Inline-Täfelchen und Vorschaubilder, 6 px kompakte Zeilen und Filter, **8 px Knöpfe und Eingaben**, 12 px Panels, 16 px nur selten, 9999 px ausschließlich für Badge- und Stufenpillen.
- Linien und Rahmen: 1 px `#e6e5e0` für Panels, 1 px `#efeee8` für Zeilentrenner, 1 px `#cfcdc4` für Knöpfe und Felder, 2 px Ink für den aktiven Reiter.
- Schatten und Ebenen: **keine**. Tiefe entsteht nur aus Haarlinie plus Weiß auf Creme.
- Besondere Oberflächen: `#fafaf7` als eingelassene Innenfläche; die fünf Pastellpillen sind der einzige Farbreichtum und gelten nur für Verarbeitungsstufen.

## Bewegung
- Laut Datei: keine Angaben („Animation timings out of scope“, Hover nicht dokumentiert).
- Empfehlung: klein 120 ms / Screenwechsel 220 ms, Easing `cubic-bezier(.2,.8,.2,1)`. Druck: Orange auf `#d04200`, keine Skalierung. Einblenden: Tabellenzeilen 4 px von unten, je 30 ms versetzt; Zeitleisten-Pillen erscheinen nacheinander. Screenwechsel: hartes Überblenden ohne Bewegung. Fokus (TV): Unterstrich wandert in 160 ms.
- Compose: `tween(120, easing = CubicBezierEasing(.2f,.8f,.2f,1f))`, `animateItem()` für Tabellen, `AnimatedContent` mit `fadeIn/fadeOut` statt Slide.

## Signatur-Elemente
1. Warme Creme statt Weiß, dazu Weiß nur als Panel mit 1-px-Haarlinie – nirgends ein Schatten.
2. Überschriften im Gewicht 400 mit enger Laufweite neben Monospace-Zahlen.
3. Die Stufen-Zeitleiste mit fünf Pastellpillen in 11-px-Versalien.
4. Obere Textreiter mit 2-px-Unterstrich plus angedockte Befehlszeile unten.
5. Datentabelle mit Versal-Kopfzeile und rechtsbündigen Monospace-Spalten.

## Übertragung auf eine App
- Startscreen: Versal-Label, Begrüßung in 400, Monospace-Gesamtzahlen, ein Panel als Aufmacher, darunter die Stufen-Zeitleiste der Quellen.
- Liste und Übersicht: volle Breite als Tabelle mit Versal-Kopfzeile, 32-px-Vorschaubildern und zwei Monospace-Spalten rechts; Filter als kompakte 6-px-Chips darüber.
- Detail: Pfad-Krümelzeile im Monospace, Bild in einem Panel, Titel 26/400, orangefarbener Knopf plus Umriss-Knöpfe, Unterreiter mit Unterstrich, enges Fotoraster.
- Formulare und Einstellungen: beschriftete Felder (Versal-Label, 8-px-Feld) untereinander, Hilfetext 13 px `#807d72`, Abschluss mit Orange-Knopf links statt mittig.
- Leere Zustände und Laden: Panel mit Haarlinie, Monospace-Satz in `#807d72`, ein Textlink als Ausweg; Laden als Zeitleisten-Pille „LIEST“ mit laufendem Pfad.
- TV: linke Textspalte, rechts Tabelle und Panels, Fokus als Unterstrich.
- Musterscreens: Start mit Begrüßung in 400, Aufmacher-Panel und Quellen-Zeitleiste; Bibliothek als Tabelle mit Versal-Kopfzeile und Monospace-Spalten; Detail mit Pfadzeile, Bild-Panel und engem Raster – alle drei mit oberen Reitern und unterer Befehlszeile.

## Vermeiden
- Kein reines Weiß als Fläche, keine Schatten, keine zweite Akzentfarbe neben Orange.
- Überschriften nie fett setzen; das Gewicht 400 ist die Stimme.
- Die Pastellpillen nie als allgemeine Status- oder Aktionsfarben verwenden – sie gehören zur Stufen-Zeitleiste.
- Zahlen nie in der Textschrift setzen, wenn eine Monospace-Spalte möglich ist.
- Keine großen Radien: ab 16 px wirkt es sofort wie eine andere Marke.
- Nicht mit Wise und Mastercard verwechseln: Cursor hat Haarlinien, Monospace und 8/12-px-Radien; Wise hat fette 900er Titel in schattenlosen 24-px-Blöcken, Mastercard Kreise und volle Pillen.
