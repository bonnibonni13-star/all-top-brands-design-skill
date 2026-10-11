---
slug: sanity
marke: Sanity
website: https://www.sanity.io
ansatz: werkzeug
ansatz2: plakativ
modus: dunkel
aufbau: Fast schwarze Grundfläche, Inhalte als abgegrenzte Blöcke mit Haarlinien; große, extrem eng laufende Titel
navigation: Flache untere Leiste auf #0b0b0b mit 1-px-Oberkante, 4 Ziele, aktiv = #212121-Pille mit Versal-Mono-Label
komponenten: Korallen-Pille als Hauptaktion, #212121-Karten mit 1-px-#353535-Kante, Mono-Versal-Marken, Zahlenleiste
icons: Phosphor light, dünne Linien, 20–22 px, nie gefüllt
bewegung: Sachlich; 120 ms klein / 220 ms Screen, cubic-bezier(.4,0,.2,1), Aktivierung schaltet auf Blau #0052ef
schrift: Inter: Titel 34–40 px Gewicht 400 bei -0.04em, Fließtext 15–16 px/1.5, Mono-Versalien als Systemanzeige
---
# Sanity – Designsprache

**Kurz:** Ein nächtlicher Kontrollraum: fast schwarze Fläche (#0b0b0b), rein achromatische Graustufen, Haarlinien statt Schatten und Tiefe allein über Flächenhelligkeit. Darüber liegen sehr große, extrem eng laufende Titel im Gewicht 400 und Mono-Versalien als Systemanzeige. Farbe ist Signal, nicht Dekor: Korallenrot für die Hauptaktion, Elektrikblau für jeden aktiven Zustand, Neongrün für „läuft“.

## Wirkung
- Charakter: präzise, technisch, ernsthaft; wirkt wie ein Werkzeug, nicht wie eine Werbeseite
- Passt zu: Entwickler- und Verwaltungswerkzeugen, Medienbibliotheken, Archiven, Monitoring, Editoren
- Passt weniger zu: kinderfreundlichen Apps, warmen Lifestyle-Marken, hellen Papier-Layouts

## Aufbau und Raster
- Seitenaufbau: randlose dunkle Abschnitte übereinander, Inhalt jeweils in einem begrenzten Container; jeder Abschnitt wirkt wie eine eigene Folie
- Ausrichtung: linksbündig; technische Werte rechtsbündig in Mono
- Raster: Grundeinheit 8 px (1 · 2 · 4 · 6 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96–120); Außenabstand 32 px im Web, 16 px auf dem Handy
- Dichte und Weißraum: innerhalb eines Blocks dicht (16–32 px), zwischen Blöcken großzügig (64–120 px, auf dem Handy 24–32 px). Dichte Information, getrennt durch Leere
- Rhythmus: Mono-Versal-Marke → großer Titel → dichter Inhalt; dieselbe Folge in jedem Abschnitt

## Navigation
- Website: fixierte Leiste auf #0b0b0b mit Rückblende, Links 16 px in #b9b9b9, Hover auf #0052ef, rechts eine Korallen-Pille; Abschluss 1 px #212121
- App: flache Leiste unten auf #0b0b0b, 1 px #212121 Oberkante, Höhe 72 px, 4 Ziele (Start, Bibliothek, Suche, Profil). Icon 20 px darüber eine Mono-Versal-Beschriftung 10 px. Aktiv = Pille in #212121 mit weißem Icon und weißer Schrift; inaktiv #797979. Die Leiste bleibt beim Scrollen stehen (App-Muster, Empfehlung)
- TV: Reihe aus Versal-Label-Buttons oben; Fokus = 2-px-Ring in #0052ef plus Fläche #212121, keine Vergrößerung

## Startscreen
- Kopfzeile mit Mono-Versal-Marke links, Geist-Button rechts
- Großer Begrüßungstitel 40 px im Gewicht 400 mit -0.04em, direkt darunter eine Zahlenleiste in Mono-Versalien, durch 1-px-Striche in #353535 getrennt
- Hervorgehobener Inhalt als 12-px-Karte mit Vollbild und dunklem Verlauf; Marke als weiße Pille, Hauptaktion als Korallen-Pille
- Danach ein Regal aus #212121-Karten und ein dichter Quellen-Block mit Statuspunkten

## Komponenten
- Buttons: Hauptaktion = Pille (Radius 99999 px) in #f36458 mit weißem Text, 8/16 px. Sekundär = Pille in #0b0b0b mit #b9b9b9. Hell = weiße Pille mit 1 px #0b0b0b. Geist = #212121 mit 1 px #212121, Radius 5 px. Alle Zustände schalten auf #0052ef
- Karten und Kacheln: Inhaltskarte #212121, 1 px #353535, Radius 6 px, Inneres 16–24 px. Große Medienkarte Radius 12 px, randloses Bild, kein Rahmen. Nichts schwebt – alles liegt auf der Fläche
- Listen: ein Container mit 1 px #353535 und Radius 6 px, Zeilen durch 1 px #212121 getrennt, 60–64 px hoch; links eine Mono-Ordnungszahl, rechts eine Mono-Versal-Art
- Suche und Eingabefelder: Fläche #0b0b0b, 1 px #212121, Radius 3 px, 8/12 px, Platzhalter #797979; Fokus = 2-px-Ring in #0052ef
- Chips, Tabs, Filter: Versal-Label-Buttons, 11 px Gewicht 600, Großbuchstaben. Inaktiv transparent mit #b9b9b9, aktiv Fläche #0052ef mit weißem Text (Fläche plus Farbe, nicht Farbe allein)
- Dialoge und Sheets: #212121 mit 1 px #353535, Radius 12 px, Hintergrund abgedunkelt mit Rückblende; kein Schlagschatten
- Signatur-Komponenten: Mono-Versal-Zahlenleiste mit Trennstrichen; Statuszeile mit 6-px-Punkt (Neongrün #19d600 aktuell, Blau #0052ef Abgleich, #797979 getrennt); Korallen-Pille als einzige warme Farbe

## Icons
- Stil: sehr dünne Linien-Icons, geometrisch, gleichmäßige Strichstärke; nie gefüllt, nie zweifarbig – sie sollen wie eingraviert wirken
- Größe und Strich: 20 px in Leisten und Zeilen, 22 px in Buttons; optische Strichstärke ~1.2 px (Phosphor `light`)
- Einsatz: Navigation, Geist-Buttons, Quellen- und Statuszeilen; nie als Schmuck neben Überschriften
- Umsetzung: Compose Material Symbols Rounded, Gewicht 200–300, Füllung 0; iOS SF Symbols Ultralight/Light; Web Phosphor `light` oder Lucide mit `stroke-width:1.25`

## Bildsprache
- Bilder liegen randlos in 12-px-Karten oder als 6-px-Kacheln im Raster; sie werden nicht beschnitten wie Avatare und nie rund
- Über Bildern liegt ein Verlauf von #0b0b0b (unten, ~85 %) nach transparent, damit weißer Text und Mono-Marken darauf stehen können
- Farben bleiben kräftig – der dunkle Rahmen macht sie zum Signal; leichte Abdunklung (ca. 92 % Helligkeit) hält sie im System
- Raster mit 6 px Abstand; keine Rahmen um Bilder, nur die Kante der Karte

## Typografie-Stimme
- Eine Familie für alles, enger Gewichtsbereich: 400 für Titel und Fließtext, 425 für Zwischentitel, 500–600 nur für 11-px-Versal-Labels. Nie 700
- Extrem negative Laufweite im Großen: 112 px/-4.48 px, 72 px/-2.88 px, 48 px/-1.68 px, 38 px/-1.14 px; in der App Titel 34–40 px bei -0.04em
- Zeilenhöhe: Titel 1.00–1.24 (sehr eng), Fließtext 1.50 – der Kontrast trägt die Hierarchie
- Mono in Versalien für Marken, Werte, Zeitangaben und Statusmeldungen – nie für Fließtext
- Textfarben: #ffffff primär, #b9b9b9 für Fließtext, #797979 für Metadaten
- Freier Ersatz: Inter oder Space Grotesk (Titel im Gewicht 400 mit -0.04em) und IBM Plex Mono

## Form, Tiefe und Material
- Radien: 3 px Felder · 5 px Geist-Buttons und Labels · 6 px Karten, Zeilencontainer, Bildkacheln · 12 px große Medienkarten · voll für Pillen. Zwischen 13 px und Pille gibt es nichts
- Linien und Rahmen: 1 px #212121 (dezent) und 1 px #353535 (sichtbar) sind das einzige Trennmittel
- Schatten und Ebenen: keine Schlagschatten. Tiefe entsteht über Flächenhelligkeit #0b0b0b → #212121 → #353535 → #ffffff; Ringe (`0 0 0 1px`) statt Versatz; Fokus 2 px #0052ef
- Besondere Oberflächen: Rückblende (`backdrop-filter: blur`) nur an fixierten Leisten und Overlays; keine Verläufe außer der Bildabdunklung

## Bewegung
- Laut Datei: Zustände wechseln durchgehend auf #0052ef; Fokus als 2-px-Ring; Overlays mit Rückblende. Keine Dauer- oder Easing-Angaben
- Empfehlung: Dauer klein 120 ms / Screenwechsel 220 ms, Easing `cubic-bezier(.4,0,.2,1)`, Druck = Flächenwechsel auf #0052ef statt Skalierung, Einblenden = Deckkraft plus 4 px Versatz, Screenwechsel = Überblendung mit leichtem Hochschieben, Fokus (TV) = 2-px-Ring ohne Bewegung
- Compose: `tween(220, easing = CubicBezierEasing(.4f,0f,.2f,1f))`, Zustände über `animateColorAsState` auf `Color(0xFF0052EF)`, Listen mit `animateItem()`, keine Federn und kein Overshoot

## Signatur-Elemente
1. Fast schwarze Fläche mit rein neutralen Grautönen – kein warmer oder kühler Stich
2. Sehr großer Titel im Gewicht 400 mit extrem enger Laufweite (-0.04em), direkt über dichtem Kleintext
3. Mono-Versalien als Systemanzeige: Marken, Ordnungszahlen, Werte, Statusmeldungen
4. Korallen-Pille als einzige warme Farbe, Elektrikblau als einziger Aktiv-Zustand
5. Keine Schatten – nur 1-px-Kanten in #212121/#353535 und Flächenstufen

## Übertragung auf eine App
- Startscreen: Mono-Marke, großer Begrüßungstitel, Zahlenleiste, eine 12-px-Medienkarte mit Verlauf, ein Regal aus #212121-Karten, darunter Quellen mit Statuspunkten
- Liste und Übersicht: ein Container mit Haarlinien-Zeilen, links Mono-Ordnungszahl, 44-px-Bild mit 6 px Radius, rechts Mono-Versal-Art; Filter als Versal-Label-Buttons, aktiv auf #0052ef
- Detail: 12-px-Bildkarte mit Verlauf und weißer Pillen-Marke, Titel 38 px bei -0.04em, Mono-Metazeile, Korallen-Pille plus Geist-Pillen für Nebenaktionen, Reiter als Versal-Labels, Fotoraster mit 6 px Radius, fixierte Musikleiste in #212121
- Formulare und Einstellungen: Felder 3 px auf #0b0b0b mit 1 px #212121, Beschriftung als Mono-Versal-Label, Hilfetext 13 px #797979, Fehler #dd0000, Senden als Korallen-Pille über volle Breite
- Leere Zustände und Laden: #212121-Karte mit 1-px-Kante, dünnem Icon in #797979, einer Zeile #b9b9b9 und Korallen-Pille; Platzhalter als #212121-Flächen ohne Schimmer
- TV: Versal-Label-Reihe oben, Raster aus 6-px-Kacheln, Fokus als 2-px-Ring in #0052ef
- Musterscreens: Start mit Zahlenleiste, Rückblick-Bildkarte und Quellen-Status; Bibliothek als nummerierte Haarlinien-Liste mit blauem Aktiv-Filter; Detail mit Bildkarte, Korallen-Pille und Musikleiste mit Neongrün-Anzeige

## Vermeiden
- Keine warmen oder kühlen Grautöne – die Skala ist rein achromatisch
- Keine Schlagschatten; Tiefe kommt aus der Flächenhelligkeit
- Keine Radien zwischen 13 px und Pille
- Korallenrot und Elektrikblau nie am selben Element mischen; Korallenrot nur für die Hauptaktion
- Keine Gewichte ab 700, keine lockeren Zeilenhöhen bei Titeln (nie über 1.24)
- Mono nie als Fließtext; Grau auf Grau nur mit geprüftem Kontrast
