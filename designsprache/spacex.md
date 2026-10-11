---
slug: spacex
marke: SpaceX
website: https://www.spacex.com
ansatz: buehne
ansatz2: plakativ
modus: dunkel
aufbau: Vollbild-Foto auf reinem Schwarz, Text linksbündig am unteren Bildrand, darunter Haarlinien-Bänder
navigation: Versal-Textleiste unten (Start · Bibliothek · Suche · Profil), aktiv = weiße 2-px-Oberkante; keine Icons
komponenten: Ein Umriss-Pill pro Band, Versal-Augenbrauen, Haarlinien-Zeilen, Kennzahlenband, abgedunkelte Vollbilder
icons: Empfehlung: nur Pfeile/Winkel, Lucide 1,5 px mit eckigen Enden, 16–20 px, weiß; sonst Text statt Icon
bewegung: Empfehlung: nur Deckkraft/Haarlinien, 240 ms / 420 ms, cubic-bezier(.22,1,.36,1); kein Federn
schrift: Schmale Industrie-Grotesk, Versalien, 700, gesperrt (+1,0–1,6 px), Zeilenhöhe 0,95; Fließtext 16 px 400
---
# SpaceX – Designsprache

**Kurz:** Jedes Band ist ein einziges randloses Foto auf reinem Schwarz, über das linksbündig eine gesperrte Versal-Schlagzeile und genau ein Umriss-Pill gesetzt sind – wie eine Filmtitelkarte, nicht wie eine Landingpage. Es gibt keine Akzentfarbe, keine Schatten, keine Verläufe und keinen Scrim: Braucht Text Kontrast, wird das Foto abgedunkelt, nicht die Fläche. Alles Bedienbare spricht in Versalien.

## Wirkung
- Charakter: technisch, nüchtern, pathetisch-groß; Ingenieurssprache statt Produktsprache.
- Passt zu: Medien- und Foto-Apps mit starken Bildern, Missions-, Fahrzeug- und Telemetrie-Apps, Event- und Launch-Apps.
- Passt weniger zu: verspielten Apps, Formular- und Buchungsstrecken, farbig kodierten Daten-Apps, Kinder- und Lifestyle-Apps.
- Abgrenzung zu Tesla (gleiches Umfeld, beide vollflächig): Tesla ist weiß, mittig komponiert, in Satzschreibung mit normaler Laufweite, Gewichte 400/500, Buttonpaar Blau/Weiß mit 4 px und Text-Navigation oben. SpaceX ist schwarz, linksbündig am unteren Bildrand, schmal-fett in gesperrten Versalien, hat genau einen Umriss-Pill mit 32 px, Haarlinien statt Weißraum, abgedunkelte Fotos und die Versal-Textleiste unten.

## Aufbau und Raster
- Seitenaufbau: Bänder statt Abschnitte. Jedes Band ist ein Vollbild-Foto (Web volle Höhe, App 55–60 %) mit Textblock unten links; darunter schmale Bänder auf `#000` bzw. `#0a0a0a`, nur durch 1-px-Haarlinien `#3a3a3f` getrennt.
- Ausrichtung: durchgehend linksbündig, Textkante bei 24 px; Zahlen in Kennzahlenbändern mittig in ihrer Spalte.
- Raster: 8-px-Basis mit Zwischenwerten 4/12/16/18/24/32/48; Web ohne Container (volle Breite), Lesespalte max. 1200 px; Shop-Raster 4/2/1 Spalten.
- Dichte und Weißraum: auf der Bühne extrem luftig (Negativraum ist Himmel oder Marsfläche), in den Bändern dicht – Zeilen stoßen an Haarlinien, kein Polsterrand.
- Rhythmus: Bild → Versal-Augenbraue → Schlagzeile → Zeile → ein Pill; danach gestapelte Haarlinien-Bänder ohne Zwischenraum.

## Navigation
- Website: feste Kopfleiste direkt über dem Foto, ohne Fläche und ohne Kante, Wortmarke links (~147×19 px), Versal-Punkte 13 px 700 mit 1,17 px Sperrung, Polster 24/32 px; unter 768 px Hamburger mit derselben dunklen Überlagerung. Fuß: schwarzes Band, Spalten in 12-px-Versalien.
- App (Empfehlung, abgeleitet aus Kopfleiste und Fuß): Versal-Textleiste unten, 72 px, `#000` mit 1-px-Oberkante `#3a3a3f`, vier Ziele (Start · Bibliothek · Suche · Profil) als 12-px-Versalien mit 0,96 px Sperrung, ohne Icons; aktiv = volle Weiße plus 2-px-Oberkante über dem Ziel, inaktiv `#5a5a5f`. Die Leiste bleibt beim Scrollen stehen und bekommt nie eine Fläche.
- Detail: Versal-Textlink „‹ BIBLIOTHEK“ oben links über dem Foto; Nebenaktionen oben rechts als drei 20-px-Linien-Icons; unten die Aktionsleiste mit genau einem Pill.
- TV: Versal-Punkte oben, Fokus = 2-px-weißer Rahmen um die Kachel plus Versal-Beschriftung, kein Vergrößern und kein Glühen.

## Startscreen
- Bühne 0–486 px: Foto randlos, abgedunkelt (`filter: brightness(.72) contrast(1.08) saturate(.85)`), kein Verlauf, kein Scrim.
- Textblock am unteren Bildrand, linksbündig: Versal-Augenbraue 12 px, Schlagzeile 48 px 700 Versalien (Zeilenhöhe 0,95, Sperrung 1,2 px), Angabenzeile 12 px, darunter genau ein Umriss-Pill.
- Darunter zwei Bänder: eine Reihe Foto-Kacheln mit Versal-Labels (rechts angeschnitten) und ein Kennzahlenband aus drei Spalten mit Haarlinien dazwischen.
- Unten die Versal-Textleiste.

## Komponenten
- Buttons: nur ein Typ pro Fläche. Umriss-Pill 32 px Radius, 1 px `#fff` (auf Hell 1 px `#000`), Fläche transparent, Label 13 px 700 Versalien mit 1,17 px Sperrung, Polster 18/24 px, Höhe ≥ 50 px. Höchstens einer pro Band, nie gefüllt, nie farbig; gefüllt (`#f0f0fa` auf Schwarz) nur im Shop-Kontext.
- Karten und Kacheln: Fotoband ohne Polster und ohne Rahmen, Radius 4 px (faktisch kantig); Shop-Karte hell, 8 px Radius, 16 px Polster, 1 px `#e0e0e8`. Kacheln tragen ihr Label als Versal-Microtext darunter, nicht im Bild.
- Listen: Empfehlung: Manifest-Zeilen 72 px, links ein kantiges 56-px-Vorschaubild, Titel 16 px 700 Versalien mit 0,6 px Sperrung, darunter 12-px-Versal-Angaben, rechts ein Wert in 12-px-Versalien; Trennung durch 1 px `#3a3a3f`, keine Radien, keine Abstände zwischen Zeilen.
- Suche und Eingabefelder: Höhe 44 px, Radius 4 px, Fläche transparent bzw. `#0a0a0a`, 1 px `#3a3a3f`, Platzhalter 12 px Versalien `#5a5a5f`; Fokus = Rahmen wird weiß.
- Chips, Tabs, Filter: keine Pillen – Versal-Textpunkte 12 px in einer Zeile über einer durchgehenden Haarlinie, aktiv = weiß plus 2-px-Unterstrich; Abstand 20 px.
- Dialoge und Sheets: schwarzes Blatt ohne Radius und ohne Schatten, 1-px-Haarlinie als obere Kante, Titel in Versalien, Schließen als Versal-Textlink.
- Signatur-Komponenten: Versal-Schlagzeile auf dem abgedunkelten Vollbild; der einzelne Umriss-Pill; das Kennzahlenband (Wert 28 px 700 über 12-px-Versal-Label, Spalten durch Haarlinien getrennt); die Versal-Augenbraue über jeder Schlagzeile.

## Icons
- Stil (Empfehlung; die Datei nennt ausdrücklich „keine Icons außer wenigen Pfeil-Winkeln“): streng geometrische Linien-Icons mit eckigen Enden und spitzen Ecken (`stroke-linecap: square; stroke-linejoin: miter`), nur Weiß; im Zweifel Versal-Text statt Icon.
- Größe und Strich: 16 px in Zeilen, 20 px in Leisten, Strich 1,5 px; nie gefüllt, nie zweifarbig.
- Einsatz: Winkel und Pfeile (weiter, zurück, senden), Lupe, Wiedergabe – mehr nicht. Navigation und Filter bleiben reiner Text.
- Umsetzung: Compose `Icons.Sharp` bzw. Material Symbols Sharp, Gewicht 300, Füllung 0; iOS SF Symbols `.regular`; Web Lucide mit `stroke-width: 1.5` und eckigen Enden.

## Bildsprache
- Laut Datei: Fotografie und Startvideo sind das gesamte Dekor; randlos, nie in einer Karte, kein erzwungenes Seitenverhältnis – das Bild führt. Kein Scrim, kein Verlauf: Für Textkontrast wird das Foto selbst dunkler gradiert.
- Umsetzung: Bühnenbilder mit `filter: brightness(.72) contrast(1.08) saturate(.85)`, Kacheln mit `brightness(.85)`; dadurch bleibt alles im Schwarz-Weiß-Gefüge und Text liegt ohne Fläche sauber auf.
- Formate: Bühne hochformatig vollflächig, Kacheln 16:10 kantig, Fotoraster 3 Spalten 4:3 mit 1-px-Fuge randlos; Radius höchstens 4 px, Rahmen nie.
- Motivwahl: zentrales Motiv mittig halten (mobil wird auf das Motiv beschnitten), Textblock in die ruhige untere Bildhälfte.

## Typografie-Stimme
- Zwei Schnitte einer schmalen Industrie-Grotesk: Display 700 Versalien (80/60/48/40 px, Zeilenhöhe 0,95–1,25, Sperrung +1,6 bis +0,96 px) und Text 400 (16 px, Zeilenhöhe 1,5–1,7, Sperrung 0,32 px).
- Versal-Microtext ist die zweite Stimme: 12 px 400, Zeilenhöhe 2,0, Sperrung 0,96 px für Augenbrauen, Navigation, Labels; Button 13 px 700, Sperrung 1,17 px.
- Größenkontrast sehr hoch (48 px gegen 12 px), dazwischen fast nichts; nie Satzschreibung im Display, keine Serifen, keine humanistischen Groteske, kein Mono.
- Freier Ersatz: schmale Grotesk (Oswald, Archivo Narrow, Roboto Condensed) für Display, Inter/Roboto 400 für Text; ersatzweise Inter 700 mit `letter-spacing: 1.6px`, `text-transform: uppercase`, `line-height: .95`.

## Form, Tiefe und Material
- Radien: 4 px Felder und Fotobänder, 8 px Shop-Karten und Videorahmen, 16 px größere Flächen, 32 px nur der Pill, 50 % nur der runde Wiedergabeknopf über Videos.
- Linien und Rahmen: 1 px `#3a3a3f` auf Dunkel, 1 px `#e0e0e8` auf Hell – Haarlinien ersetzen Abstände, Karten und Schatten als Gliederung.
- Schatten und Ebenen: nur zwei Stufen – flach und fotografisch. Keine Schatten, keine Unschärfe, kein Glühen, kein Verlauf über dem Bild.
- Besondere Oberflächen: `#0a0a0a` als kaum angehobenes Schwarz für Bänder, die sich vom Bild lösen sollen; `#f0f0fa` als kühles Weiß für Sekundärtext.

## Bewegung
- Laut Datei: keine Angaben außer automatisch laufendem Startvideo und kleinen Pfeil-Winkeln in Hover-Zuständen.
- Empfehlung: Dauer klein 240 ms / Screenwechsel 420 ms, Easing `cubic-bezier(.22, 1, .36, 1)`; Druck-Effekt nur Rahmen- und Textfarbe (Pill invertiert zu weißer Fläche mit schwarzem Text); Einblenden als reine Deckkraft, Schlagzeile 80 ms nach dem Bild; Screenwechsel Überblenden mit stehendem Bild; Fokus (TV) 2-px-Rahmen in 240 ms. Kein Skalieren, kein Federn, keine Parallaxe.
- Compose: `tween(240, easing = CubicBezierEasing(0.22f, 1f, 0.36f, 1f))`, `Crossfade` für Screenwechsel, `AnimatedVisibility(fadeIn(), fadeOut())`, `animateColorAsState` für Rahmen.

## Signatur-Elemente
1. Randloses, dunkel gradiertes Vollbild ohne Scrim, Text direkt darauf.
2. Linksbündige Versal-Schlagzeile, schmal und fett, gesperrt, Zeilenhöhe 0,95.
3. Genau ein Umriss-Pill mit 32 px Radius pro Band – nie gefüllt, nie farbig.
4. Versal-Augenbrauen und Versal-Textleiste unten; Navigation und Filter ganz ohne Icons.
5. Haarlinien `#3a3a3f` als einziges Gliederungsmittel, dazu das Kennzahlenband.

## Übertragung auf eine App
- Startscreen: eine Bühne mit dem Hervorgehobenen (Augenbraue, Versal-Titel, Angaben, ein Pill), darunter eine angeschnittene Kachelreihe und ein Kennzahlenband, unten die Versal-Textleiste.
- Liste und Übersicht: Versal-Seitentitel mit Zahlenzeile, Suchfeld mit 4 px Radius, Filter als Versal-Textpunkte über einer Haarlinie, darunter ein Manifest aus 72-px-Zeilen mit kantigem Vorschaubild und rechtem Wert.
- Detail: Bühne mit Versal-Titel unten links, darunter Kennzahlenband, Versal-Umschalter und ein randloses 3-spaltiges Fotoraster; unten eine Aktionsleiste mit genau einem Pill und einer Versal-Zeile darüber.
- Formulare und Einstellungen: Zeilen 56 px, nur durch Haarlinien getrennt, Label links in Versalien, Wert rechts; Felder 44 px mit 4 px Radius; am Ende ein Umriss-Pill über die volle Breite.
- Leere Zustände und Laden: schwarze Fläche, eine Versal-Zeile 12 px in `#5a5a5f`, darunter ein Pill; Bilder laden als `#0a0a0a` und blenden auf, kein Schimmer, keine Skelette mit Radius.
- TV: ein Vollbild-Band pro Seite, Versal-Punkte oben, darunter eine Kachelreihe; Fokus = weißer 2-px-Rahmen.
- Musterscreens: Start als dunkel gradierte Bühne „Herbstwald“ mit Versal-Schlagzeile und einem Pill, Bibliothek als Haarlinien-Manifest mit Versal-Filtern, Album „Lissabon“ mit Kennzahlenband, 3-spaltigem Raster und einem Pill in der Aktionsleiste.

## Vermeiden
- Akzentfarben, Verläufe, Schatten, Glühen, Scrims und Weichzeichner – Schwarz, Weiß und das Foto sind die ganze Palette.
- Zwei Buttons nebeneinander oder gefüllte Buttons auf Bild-Flächen; Pillen als Filter oder Chips.
- Display in Satzschreibung, negative Laufweite, Serifen oder humanistische Groteske; lange Fließtexte im Display-Schnitt.
- Icon-Navigation, bunte Zustandspunkte, Karten mit Schatten und großen Radien, abgerundete Bildkacheln über 8 px.
- Weißraum als Gliederung, wo die Marke Haarlinien setzt; Text auf unbearbeiteten hellen Fotos ohne Gradierung.
