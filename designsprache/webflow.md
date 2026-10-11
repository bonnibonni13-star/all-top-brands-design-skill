---
slug: webflow
marke: Webflow
website: https://webflow.com
ansatz: daten
ansatz2: werkzeug
modus: hell
aufbau: Weiße Fläche mit sichtbarem Haarlinien-Raster; Bänder, Karten und Tabellenzeilen stoßen kantig aneinander
navigation: Flache untere Leiste mit 4 Zielen und 1-px-Oberkante; aktiv = 2-px-Balken über dem Icon, Gewicht 500
komponenten: Haarlinien-Karte (8 px), 4-px-Buttons, Kennzahlen-Zellen, Datenzeilen mit Farbbalken, Kategorie-Kacheln
icons: Lucide-Linien, 1.75 px, eckige Enden (`square`/`miter`), 18–20 px
bewegung: Technisch knapp; 120 ms klein / 200 ms Screen, cubic-bezier(.4,0,.2,1), Druck = Füllung dunkler statt Skalierung
schrift: Inter 400/500/600 (nie 700), Display 30 px Gewicht 600 bei -0.8 px, Versal-Eyebrow 12 px mit +0.6 px
---
# Webflow – Designsprache

**Kurz:** Ein helles, durchkonstruiertes System: weiße Fläche, fast schwarze Schrift (#080808) und überall sichtbare 1-px-Haarlinien, die Karten, Zeilen und Zellen begrenzen. Geformt wird mit engen Radien – 4 px an Buttons, 8 px an Karten, niemals Pillen. Farbe kommt ausschließlich als vollgesättigte Kategorie-Fläche aus einer Fünferpalette; Aktionen bleiben schwarz.

## Wirkung
- Charakter: nüchtern, präzise, professionell; wirkt gebaut statt gestaltet
- Passt zu: Verwaltungs- und Werkzeug-Apps, Bibliotheken mit vielen Einträgen, Dashboards, Einstellungen, B2B
- Passt weniger zu: verspielten Consumer-Apps, Marken mit weicher Haptik, Dark-Mode-first
- Unterschied zu Figma (ebenfalls helles Design-Werkzeug): dort Pillen, randlose 24-px-Pastellblöcke und leichtes Display (Gewicht 300–340) ohne jede Linie; hier 4-px-Rechtecke, ein sichtbares Haarlinien-Raster, Gewicht 500–600 und Farbe nur in kleinen, vollgesättigten Kategorie-Kacheln. Figma ist Plakat, Webflow ist Werkbank

## Aufbau und Raster
- Seitenaufbau: Bänder voller Breite (`hero-band`, `content-band`) von oben nach unten, innerhalb davon Karten- und Zeilenraster; keine schwebenden Inseln
- Ausrichtung: linksbündig; Zahlen und technische Werte rechtsbündig in eigener Spalte
- Raster: Grundeinheit 4 px (2 · 4 · 8 · 12 · 16 · 20 · 24 · 32); Außenabstand 32 px im Web, 20 px in der App; Kacheln 2–4 Spalten, Preisraster 3-spaltig
- Dichte und Weißraum: mittel bis dicht. Karteninneres 32 px (App 16 px), Zeilenhöhe 60–64 px, Abstand zwischen Bändern 32–48 px
- Rhythmus: Eyebrow → Überschrift → Inhalt; jeder Abschnitt beginnt mit derselben Versal-Zeile, das gibt der Seite ein gleichmäßiges Taktmaß

## Navigation
- Website: weiße Sticky-Leiste, Links in 14 px Gewicht 500, rechts ein schwarzer 4-px-Button plus ein weißer mit Haarlinie; unter 992 px Hamburger
- App: flache Leiste am unteren Rand, weiß, 1 px #d8d8d8 Oberkante, Höhe 64 px, 4 Ziele (Start, Bibliothek, Suche, Profil) mit Icon und Beschriftung. Aktiv = 2-px-Balken in #080808 direkt über dem Icon, Icon und Text in #080808 bei Gewicht 500; inaktiv #898989 bei Gewicht 400. Die Leiste bleibt beim Scrollen stehen und wird nicht transparent (App-Muster, Empfehlung)
- TV: linke Seitenleiste mit Zeilen (`ex-app-shell-row`), Aktiv-Zeile mit 2-px-Balken links; Fokus als 2-px-Rahmen in #080808

## Startscreen
- Kopfzeile mit Haarlinie, darunter Eyebrow und Begrüßung in 30 px Gewicht 600
- Direkt danach eine Kennzahlen-Zeile aus drei gleichen Zellen in einem Haarlinien-Rahmen (Zahl 20 px Gewicht 600, Versal-Beschriftung 11 px)
- Ein einzelner hervorgehobener Inhalt als Karte mit mehrstufigem Schatten – der einzige erhobene Gegenstand auf dem Screen
- Zum Schluss das Kategorie-Raster in den fünf Akzentfarben

## Komponenten
- Buttons: Rechteck mit 4 px Radius, 12/20 px Innenabstand, Beschriftung 16 px Gewicht 500 bei -0.16 px. Primär #080808 auf Weiß, sekundär weiß mit 1 px #d8d8d8, tertiär Text mit Pfeil und Unterstrich. Nie Pillen, nie farbige Buttons
- Karten und Kacheln: 8 px Radius, 1 px #d8d8d8, Inneres 16–32 px. Nur eine Karte pro Screen bekommt den gestaffelten Schatten `0 30px 18px rgba(0,0,0,.04), 0 13px 13px rgba(0,0,0,.08), 0 3px 7px rgba(0,0,0,.09)`
- Listen: als Tabelle gedacht – Kopfzeile mit Versal-Beschriftungen, Zeilen 60–64 px, 1 px #d8d8d8 als Trenner, rechts eine Zahlenspalte, links ein 3-px-Farbbalken für die Kategorie
- Suche und Eingabefelder: 4 px Radius, 1 px #d8d8d8, 12/16 px Innenabstand, Platzhalter #ababab; Fokus = 1 px #146ef5 plus 2-px-Ring
- Chips, Tabs, Filter: 4-px-Rechtecke in einer Reihe. Ausgewählt = Fläche #080808 mit weißem Text; Reiter im Detail stattdessen mit 2-px-Unterstrich in #080808
- Dialoge und Sheets: 8-px-Karte mit schwerem mehrstufigem Schatten, Scrim schwarz 40 %; Toast gleiche Form, 12/16 px
- Signatur-Komponenten: fünf Kategorie-Kacheln in #7a3dff, #ed52cb, #3b89ff, #ff6b00, #00d722 (Grün mit schwarzem Text); Kennzahlen-Zellen; Info-Badge in #146ef5 (gefüllt oder als Kontur)

## Icons
- Stil: Linien-Icons, geometrisch, eckige Enden und Ecken – passend zu den 4-px-Radien; nie gefüllt, nie farbig außer auf Farbkacheln
- Größe und Strich: 18 px in Leisten und Zeilen, 20 px in Buttons; Strichstärke 1.75 px, `stroke-linecap:square`, `stroke-linejoin:miter`
- Einsatz: in Leisten, Kopfzeilen, Buttons, Zeilen-Zusätzen; ein Icon pro Zweck, keine Dekor-Icons
- Umsetzung: Compose `Icons.Sharp` bzw. Material Symbols Sharp, Gewicht 400, Füllung 0; iOS SF Symbols Regular; Web Lucide mit `stroke-width:1.75` und eckigen Enden

## Bildsprache
- Bilder sitzen in Kartenrahmen: 16:9, Radius 8 px oben, unten vom Karteninhalt begrenzt; im Raster 4 px Radius bei 4–6 px Abstand
- Keine Freisteller, keine Porträts in Marketingflächen, keine Filter und keine Verläufe über dem Bild
- Die Kategorie-Farbe steht neben dem Bild (Balken, Kachel), nie darauf
- Platzhalter: weißes Feld mit Haarlinie und mittigem Icon in #ababab

## Typografie-Stimme
- Eine Familie für alles, Gewichte 400 · 500 · 550 · 600 – nie 700 und schwerer
- Display 80/56/44.8 px Gewicht 600 mit -0.8 px; in der App 30 px Gewicht 600 bei -0.025em, Abschnittstitel 20 px Gewicht 500
- Fließtext 16/25.6 px Gewicht 400 bei -0.16 px in #363636; Nebentext 14 px in #5a5a5a, kleinste Stufe #898989
- Versal-Eyebrow 12 px Gewicht 500 mit +0.6 px markiert jeden Abschnitt; Badge-Beschriftung 12.8 px im markentypischen Gewicht 550
- Mono nur für technische Werte (Zählstände, Dauer, Speicher) in 12 px
- Freier Ersatz: Inter (400/500/600) mit `font-feature-settings:"ss01"`; Mono: Inconsolata oder DM Mono

## Form, Tiefe und Material
- Radien: 0 px randlose Bänder · 2 px winzige Marker · 4 px Buttons, Badges, Felder, Rasterbilder · 8 px Karten · voll nur für runde Icon-Behälter
- Linien und Rahmen: 1 px #d8d8d8 ist das wichtigste Gestaltungsmittel – Karten, Zeilen, Zellen, Kopf- und Fußleiste
- Schatten und Ebenen: 0 flach, 1 Haarlinie, 2 gestaffelter Mehrfachschatten (5 Stufen, sehr geringe Deckkraft), 3 stärker für Preis/Modal, 4 schwer für Dialoge. Höchstens ein erhobenes Element je Screen
- Besondere Oberflächen: keine. Keine Verläufe, kein Glas, keine Körnung – die Farbkacheln sind die einzige Atmosphäre

## Bewegung
- Laut Datei: keine Angaben zu Dauer oder Easing; als einzige Tiefenwirkung werden gestaffelte Schatten genannt
- Empfehlung: Dauer klein 120 ms / Screenwechsel 200 ms, Easing `cubic-bezier(.4,0,.2,1)`, Druck = Füllung von #080808 auf #222 (keine Skalierung), Einblenden = reine Deckkraft ohne Versatz, Screenwechsel = horizontales Schieben, Fokus (TV) = 2-px-Rahmen ohne Vergrößerung
- Compose: `tween(200, easing = CubicBezierEasing(.4f,0f,.2f,1f))`, Zustände über `animateColorAsState`, Listen mit `animateItem()`, kein Overshoot und keine Federn

## Signatur-Elemente
1. Sichtbares Haarlinien-Raster: jede Karte, Zeile und Zelle hat eine 1-px-Kante in #d8d8d8
2. Enge Geometrie – 4 px an Buttons und Feldern, 8 px an Karten, niemals eine Pille
3. Fünf vollgesättigte Kategorie-Kacheln (Lila, Pink, Blau, Orange, Grün) als einzige Farbe
4. Versal-Eyebrow mit +0.6 px Laufweite über jedem Abschnitt
5. Genau eine Karte je Screen mit gestaffeltem Mehrfachschatten; alles andere liegt flach

## Übertragung auf eine App
- Startscreen: Kopfzeile mit Haarlinie, Begrüßung, Kennzahlen-Zeile, eine erhobene Karte für den hervorgehobenen Inhalt, darunter das Kategorie-Raster
- Liste und Übersicht: Datentabelle – Kopfzeile mit Versal-Spalten, 64-px-Zeilen mit Haarlinie, 3-px-Farbbalken links, 40-px-Bild mit 4 px Radius, Zahlenspalte rechts in Mono; Filter als 4-px-Rechtecke, ausgewählt schwarz
- Detail: Bild in einer Haarlinien-Karte, Titel 30 px Gewicht 600, Kennzahlen-Zeile, schwarzer Hauptbutton plus zwei quadratische Sekundärbuttons, Reiter mit 2-px-Unterstrich, Fotoraster mit 4 px Radius und 6 px Abstand, Toast-Karte über der Leiste
- Formulare und Einstellungen: beschriftete Felder (Versal-Eyebrow als Label), 4 px Radius, Haarlinie, Hilfetext 13 px #5a5a5a, Fehler in #ee1d36
- Leere Zustände und Laden: weiße Karte mit Haarlinie, Icon in #ababab, eine Zeile Text, schwarzer Button; Platzhalter als #f3f3f3-Rechtecke mit 4 px Radius
- TV: Seitenleiste links mit Zeilen und Aktiv-Balken, Inhalt als Raster mit 4-px-Rahmen
- Musterscreens: Start mit Kennzahlen, erhobener Rückblick-Karte und fünf Farbkacheln; Bibliothek als Datentabelle mit Farbbalken und Mono-Spalte; Detail mit Haarlinien-Bildkarte, Unterstrich-Reitern und Toast

## Vermeiden
- Keine Pillen-Buttons und keine runden Kartenecken über 8 px
- Die fünf Akzentfarben nie als Button- oder Textfarbe – sie sind Flächen für Kategorien
- Keine sechste Akzentfarbe, keine Verläufe, keine Glas- oder Glüheffekte
- Keine Schriftgewichte ab 700; Betonung kommt aus 500/600 und aus der Haarlinie
- Nicht mehrere Karten gleichzeitig erheben – sonst verliert der gestaffelte Schatten seine Bedeutung
- Haarlinien nicht durch graue Flächen ersetzen; die Kante ist die Struktur
