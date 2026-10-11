---
slug: spotify
marke: Spotify
website: https://open.spotify.com
ansatz: regale
ansatz2:
modus: dunkel
aufbau: Fast schwarze Fläche; Cover-Regale, Schnellzugriff-Kacheln und dichte Listen; Farbe kommt nur aus den Covern
navigation: Leiste unten mit 3 Zielen (Icon über Label) als Verlauf ins Schwarz, darüber Mini-Player; Profil per Avatar
komponenten: Schnellzugriff-Kacheln, Cover-Regale, Pill-Chips (aktiv grün), grüner Play-Kreis, Mini-Player
icons: Linien-Icons ca. 2 px auf 24 px, aktive Ziele gefüllt; Play/Pause gefüllt; Grün nur für Zustände
bewegung: Empfehlung: kurz und funktional, 150/300 ms, Ease-out; Druck 0,97×; Hover hellt Flächen auf (Datei)
schrift: kompakte Grotesk 10–24 px, fast nur 700/400; Button-Labels versal mit 1,4–2 px Laufweite
---
# Spotify – Designsprache

**Kurz:** Eine fast schwarze Bühne (`#121212`), auf der nur die Inhalte leuchten: Cover liefern alle Farbe, die Oberfläche bleibt grau. Prägend sind Pill- und Kreisformen, ein einziges funktionales Grün (`#1ed760`) für Play und Aktiv-Zustände, kompakte fette Typografie und eine dichte Anordnung in Regalen, Kacheln und Listen mit dauerhaft sichtbarer Wiedergabe.

## Wirkung
- Charakter: immersiv, nächtlich, wie ein hochwertiges Audiogerät; ruhig, weil nur die Inhalte Farbe tragen.
- Passt zu: Musik, Podcasts, Hörbücher, Video, Foto- und Medienbibliotheken – alles mit Covern oder Thumbnails.
- Passt weniger zu: textlastigen Apps, Formularen, Finanzen/Behörden, hellen Tageslicht-Apps, Apps ohne Bildmaterial (wirkt dann leer).

## Aufbau und Raster
- Seitenaufbau: Web: feste Seitenleiste + Inhaltsbereich + Wiedergabeleiste unten über volle Breite, auf allen Größen. App: Kopfzeile, Chips, Inhalte in Regalen und Listen, Wiedergabe als Mini-Player über der Leiste.
- Ausrichtung: konsequent linksbündig an 16 px Rand; nur das große Cover der Detailseite steht mittig; Regale laufen rechts aus dem Bild.
- Raster: Basis 8 px, Skala 4/8/12/16/20 px (Datei: 1–20 px). Cover-Raster 5 → 3 → 2 → 1 Spalten; Tablet ab 576 px zweispaltig. App: Schnellzugriff 2 Spalten mit 8 px Abstand.
- Dichte und Weißraum: dicht („dark compression“): 8 px zwischen Kacheln, 16 px zwischen Covern, 24–32 px zwischen Abschnitten; das Dunkel ersetzt Weißraum.
- Rhythmus: Abschnitt = fette Überschrift 24 px + Reihe oder Liste, gleichförmig wiederholt; Abwechslung kommt nur aus den Covern.

## Navigation
- Website: dunkle Seitenleiste `#121212`; aktiv 14 px 700 weiß, inaktiv 14 px 400 `#b3b3b3`; runde Icon-Buttons (50 %); Wiedergabeleiste unten bleibt immer stehen.
- App: Laut Datei wird die Seitenleiste mobil zur Leiste unten. Empfehlung: 3 Ziele (Start, Suche, Bibliothek), Icon 24–26 px über Label 10 px; aktiv weiß, 700, Icon gefüllt; inaktiv `#b3b3b3`, 400, Linien-Icon; keine Aktiv-Pille. Keine feste Fläche, sondern Verlauf von transparent zu Schwarz, Inhalte scrollen darunter. Mini-Player (56 px) direkt darüber; Leiste und Player bleiben auf Unterseiten sichtbar. Profil und Einstellungen über den Avatar-Kreis (32 px) oben links statt eigenem Tab. Unterseiten: Zurück als runder Icon-Button oben links.
- TV: Empfehlung: schmale Icon-Leiste links (Suche, Start, Bibliothek), Inhalte als Cover-Regale, Wiedergabe als Leiste unten; Fokus siehe Bewegung.

## Startscreen
- Empfehlung: Kopfzeile mit Avatar, Begrüßung nach Tageszeit (24 px 700) und 1–2 Icons; darunter Filter-Chips; dann Schnellzugriff als 2×3-Raster aus Kacheln (56 px hoch, Cover links bündig, Titel 13 px 700, laufender Eintrag mit grünen Balken); danach Abschnitte mit fetter Überschrift: eine hervorgehobene Karte in Cover-Farbe mit grünem Play-Kreis und Cover-Regale (148 px), rechts angeschnitten.

## Komponenten
- Buttons: immer Pill (500–9999 px) oder Kreis (50 %). Dark Pill `#1f1f1f`, Text `#fff`/`#b3b3b3`, 8×16 px; Light Pill `#eeeeee` mit `#181818` (selten); Outlined Pill transparent, 1 px `#7c7c7c`, Innenabstand 4/16/4/36 px (Platz für Icon links); Haupt-CTA grün `#1ed760` mit Schwarz, 14 px 700, versal, Laufweite 1,4–2 px.
- Karten und Kacheln: `#181818`/`#1f1f1f`, Kacheln `#252525`, Radius 6–8 px, keine sichtbaren Rahmen; Hover/Druck hellt die Fläche auf (`#272727`); erhöht mit Schatten `rgba(0,0,0,.3) 0 8px 8px`.
- Listen: Empfehlung: Zeile 72 px mit Cover 56 px (Radius 4 px), Titel 16 px 400 weiß, darunter „Typ · Angaben“ 14 px `#b3b3b3`; laufender Eintrag mit grünem Titel; angeheftet/geladen als kleines grünes Icon vor den Angaben.
- Suche und Eingabefelder: Pill-Feld `#1f1f1f`, Radius 500 px, Lupe links (Innenabstand 12 px 96 px 12 px 48 px), Rand als Inset-Schatten `rgb(18,18,18) 0 1px 0, rgb(124,124,124) 0 0 0 1px inset`; Fokus: Rand `#000`, 1 px Outline.
- Chips, Tabs, Filter: Dark Pill 32 px hoch, 14 px 400; aktiv Grün mit schwarzer Schrift (Empfehlung); keine Unterstrich-Tabs, auch Umschalter sind Chips.
- Dialoge und Sheets: Fläche `#252525`, Radius 8 px, Schatten `rgba(0,0,0,.5) 0 8px 24px`; Menüs als dichte Liste 14 px.
- Signatur-Komponenten: grüner Play-Kreis (44–56 px, schwarzes Dreieck), Mini-Player in Cover-Farbe mit 2-px-Fortschritt (Empfehlung), Schnellzugriff-Kacheln (Empfehlung), grüne Equalizer-Balken für „läuft gerade“ (Empfehlung).

## Icons
- Stil: Empfehlung (Datei nennt keinen Icon-Satz): geometrische Linien-Icons mittlerer Stärke mit runden Enden; aktive Navigationsziele, Play/Pause und Status-Icons gefüllt.
- Größe und Strich: 24 px Standard, 26 px in der Leiste, 13–16 px in Zeilen; Strich ca. 2 px.
- Einsatz: weiß oder `#b3b3b3`; Grün nur für Zustände (läuft, angeheftet, geladen, Favorit an); im grünen Kreis schwarz.
- Umsetzung: Compose `Icons.Rounded`, aktiv `Icons.Filled`, bzw. Material Symbols Rounded, Gewicht 500, Füllung 0 → 1; iOS SF Symbols Semibold, aktiv `.fill`; Web Phosphor Bold, aktiv Phosphor Fill.

## Bildsprache
- Quadratische Cover sind das einzige farbige Material; keine Filter, keine Körnung, kein Rahmen. Radius 4 px (klein) bis 6 px (groß); großes Cover mit schwerem Schatten.
- Empfehlung: Flächen hinter einem Inhalt (Detail-Kopf, Mini-Player, hervorgehobene Karte, leichter Schleier oben auf Start) in einer stark abgedunkelten Cover-Farbe, Verlauf in `#121212` (Android: `Palette`-Bibliothek, dominante Farbe abdunkeln).
- Menschen und Profile rund (Avatar 50 %), Medien immer eckig.

## Typografie-Stimme
- Kompakt: 10–24 px; Hierarchie über Gewicht (700/400, 600 sparsam), nicht über Größe. Titel 24 px 700; Zwischentitel 18 px 600, Zeilenhöhe 1,3; Text 16 px; Angaben 14 px; klein 12 px; Badge 10,5 px 600; Micro 10 px.
- Zeilenhöhe normal bis eng; keine lockeren Lesetexte, keine Display-Größen.
- Button-Labels versal, 14 px 700, Laufweite 1,4–2 px, Zeilenhöhe 1,0 – eine eigene „Etiketten“-Stimme neben dem Inhalt.
- Freier Ersatz: Inter (Text) und Inter Display (Titel); näher am geometrischen Circular: Figtree oder DM Sans (Google Fonts).

## Form, Tiefe und Material
- Radien: 2 px Badge, 4 px Eingaben und kleine Cover, 6 px Cover und Karten, 8 px Panels und Dialoge, 10–20 px Overlays, 500–9999 px Buttons und Suche, 50 % Play, Avatare, Icon-Buttons.
- Linien und Rahmen: kaum Linien; Ränder als Inset-Schatten statt sichtbarer grauer Rahmen; Trenner `#b3b3b3` nur wo nötig.
- Schatten und Ebenen: Ebene 0 `#121212` → 1 `#181818`/`#1f1f1f` → 2 `rgba(0,0,0,.3) 0 8px 8px` → 3 `rgba(0,0,0,.5) 0 8px 24px` (Dialoge, großes Cover, Mini-Player). Schwer, weil leichte Schatten auf Dunkel unsichtbar sind.
- Besondere Oberflächen: Empfehlung: Verläufe nur aus Cover-Farben und als Auslauf ins Schwarz hinter der Leiste; kein Glas, keine Muster.

## Bewegung
- Laut Datei: Karten hellen beim Hover leicht auf, erhöhte Karten bekommen Schatten; sonst keine Angaben.
- Empfehlung: Dauer klein 150 ms / Screenwechsel 300 ms, Easing `cubic-bezier(0.3, 0, 0, 1)`; Druck: 0,97× plus hellere Fläche; Play-Kreis und CTA beim Hover 1,04×; Einblenden: 8 px von unten, Zeilen um 40 ms gestaffelt; Screenwechsel: Detail schiebt von rechts, Cover wächst aus der Kachel; „läuft gerade“ als springende grüne Balken; Fokus (TV): 1,05× plus weißer Ring 2 px in 150 ms.
- Compose: `tween(150, easing = CubicBezierEasing(0.3f, 0f, 0f, 1f))` für Druck und Farbe, `tween(300, …)` für Screens; `animateItem()` in Listen; `SharedTransitionLayout` für Cover → Detail-Cover und Mini-Player → Vollbild-Player.

## Signatur-Elemente
1. Fast schwarze Fläche `#121212`; Farbe nur aus Covern, als Verlauf hinter Detail-Kopf und Mini-Player.
2. Ein funktionales Grün `#1ed760` – nur Play, Aktiv-Zustand, laufender Titel, Haupt-CTA.
3. Pill- und Kreis-Geometrie: Chips, Suchfeld, CTA als Pill; Play, Avatar, Zurück als Kreis.
4. Schnellzugriff-Kacheln und Cover-Regale unter fetten 24-px-Überschriften.
5. Mini-Player über einer Leiste, die als Verlauf ins Schwarz ausläuft.

## Übertragung auf eine App
- Startscreen: Avatar + Begrüßung, Chips, 2×3 Schnellzugriff-Kacheln, hervorgehobene Karte in Cover-Farbe mit grünem Play-Kreis, dann Regale („Zuletzt hinzugefügt“ u. Ä.).
- Liste und Übersicht: Kopf mit Avatar, Titel und „+“; Pill-Suchfeld; Chips (aktiv grün); Sortierzeile „⇅ Zuletzt …“ mit Raster-Umschalter rechts; dichte Zeilen mit Cover 56 px.
- Detail: Verlauf aus Cover-Farbe in `#121212`, Zurück-Kreis, großes Cover mittig (ca. 55–60 % Breite) mit schwerem Schatten, Titel 24 px linksbündig, Besitzer mit Mini-Avatar, Angaben grau, Aktionszeile mit Icons links und grüner Pill bzw. Play-Kreis rechts, darunter Chips und Inhalt.
- Formulare und Einstellungen: dunkle Listen mit 16-px-Zeilen, Schalter im Aktiv-Zustand grün, Pill-Eingaben mit Inset-Rand; Fehler `#f3727f`, Warnung `#ffa42b`, Hinweis `#539df5`.
- Leere Zustände und Laden: großes Linien-Icon `#b3b3b3`, Titel 24 px 700, Text 14 px grau, Light Pill als Aktion; Laden als Skelett-Flächen `#1f1f1f`/`#252525` in Cover- und Zeilenform statt Spinner (Empfehlung).
- TV: Regale mit großen Covern (ab 200 px), Fokus statt Hover, Icon-Leiste links, Text größer.
- Musterscreens: Start mit Begrüßung, Chips, Schnellzugriff, Rückblick-Karte und Regal; Bibliothek als dichte Liste mit Pill-Suche, Chips und Sortierzeile; Detail „Lissabon“ mit Cover-Verlauf, Outlined Pill für die Musik, grüner Diashow-Pill und Fotoraster – alle mit Mini-Player und Verlaufsleiste.

## Vermeiden
- Grün dekorativ oder als Fläche; zusätzliche Markenfarben; helle Hauptflächen.
- Eckige Buttons oder Buttons ohne Pill-/Kreisform.
- Dünne, zarte Schatten; sichtbare graue Rahmen statt Inset-Schatten.
- Lockere Zeilenhöhen, Schrift über 24 px, viel Weißraum – das ist eine App, kein Magazin.
- Beim Übertragen: Material-Standardleiste mit Aktiv-Pille, Karten mit Rahmen, farbige UI-Flächen ohne Bezug zum Inhalt, Profil als vierter Tab.
- Für eigene Produkte das Grün leicht abwandeln, besonders in derselben Branche; kein Logo, keine markeneigenen Sonder-Kacheln nachbauen.
