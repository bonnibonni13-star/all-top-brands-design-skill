---
slug: tesla
marke: Tesla
website: https://www.tesla.com
ansatz: buehne
ansatz2: minimal
modus: hell
aufbau: Eine vollflächige Foto-Bühne pro Screen, darunter Weiß; mittig gestapelt: Titel → Zeile → zwei Buttons
navigation: Text-Buttons oben (Start · Bibliothek, aktiv = graue Fläche) + Avatar; Suche als feste Eingabeleiste unten
komponenten: Buttonpaar Blau/Weiß mit 4 px, Textlinks, 2:1-Kategoriekarten 12 px, Produktraster mittig, Kennzahlenzeile
icons: Empfehlung: dünne runde Linien (Phosphor Light), 20–24 px, Carbon/Pewter, nie gefüllt, nie blau
bewegung: Nur Farb- und Deckkraftwechsel, 330 ms, cubic-bezier(.5,0,0,.75); kein Skalieren, kein Verschieben
schrift: Ruhige Grotesk nur 400/500, normale Laufweite, keine Versalien; fast alles 14 px, Bühnentitel 28–40 px
---
# Tesla – Designsprache

**Kurz:** Ein Ausstellungsraum statt einer Oberfläche: Jeder Screen gehört einem einzigen vollflächigen Bild, auf dem nur ein mittiger Titel, eine Zeile und höchstens zwei Buttons stehen. Keine Schatten, Verläufe oder Rahmen – Tiefe kommt aus Fotografie, Weiß und milchigem Glas; ein einziges Blau markiert nur die Hauptaktion.

## Wirkung
- Charakter: still, technisch, selbstsicher, galerieartig; die UI tritt hinter das Bild zurück.
- Passt zu: Medien-, Foto- und Reise-Apps mit starken Bildern, Geräte- und Fahrzeugsteuerung, Showroom- und Konfigurator-Apps.
- Passt weniger zu: dichten Daten- und Werkzeug-Apps, verspielten Kinder-Apps, textlastigen Feeds.
- Abgrenzung zu SpaceX (gleiches Umfeld): Tesla ist hell, in Satzschreibung, 400/500 ohne Sperrung, mittig komponiert, mit gefülltem blauem 4-px-Button plus weißem Zweitbutton und Navigation oben. SpaceX ist schwarz, schmal-fett in gesperrten Versalien, linksbündig unten auf dem Foto, hat nur einen Umriss-Pill-Button, keine Farbe und eine Versal-Textleiste unten.

## Aufbau und Raster
- Seitenaufbau: Screen = eine Bühne. Foto vollflächig (Web 100vh, App 55–65 % der Höhe), oben mittig Titel + Zeile, unten das Buttonpaar; darunter auf Weiß genau ein weiteres Thema.
- Ausrichtung: mittig für Titel, Produktnamen, Buttons und Kennzahlen (Rhythmus Name → Zeile → Buttons); linksbündig nur Labels auf Kategoriekarten.
- Raster: 8-px-Basis (8/16/24/32/48), Kartenabstand 16 px, Seitenrand App 24 px; Produktraster 3/2/1 Spalten (Desktop/Tablet/Mobil), in der App 2 Spalten.
- Dichte und Weißraum: sehr luftig, Weißraum als Luxussignal – eine Botschaft pro Screen, freie Fläche wird nie aufgefüllt.
- Rhythmus: Bühne → 24 px → ein Thema → Ende; keine Kaskade aus Abschnittstiteln.

## Navigation
- Website: Kopfleiste ohne Fläche über dem Foto, Wortmarke links, fünf Text-Buttons mittig (14 px 500, Padding 4 × 16 px, min. 32 px, 4 px Radius, aktiv = dezente Fläche), rechts drei Icon-Buttons; beim Scrollen weiß bzw. Glas `rgba(255,255,255,.75)`, ohne Einschieben; mobil Hamburger.
- App: keine Tableiste, Profil oben rechts (App-Muster der Marke (nicht in der Datei)). Empfehlung: 48-px-Kopfleiste über der Bühne – neutrales Zeichen links, Text-Buttons „Start“ und „Bibliothek“ mittig (aktiv = Fläche `rgba(23,26,32,.06)`), Avatar 28 px rechts. „Suche“ ist die feste Eingabeleiste unten (abgeleitet von der dauerhaften Frage-Leiste der Website). Beim Scrollen wird die Kopfleiste zu Glas, ohne Linie und ohne Schatten.
- Detail: Text-Button „‹ Bibliothek“ links, rechts Teilen · Favorit · Mehr als 40-px-Icon-Buttons ohne Fläche.
- TV: Text-Buttons oben mittig; Fokus = Light-Ash-Fläche plus 2-px-Innenrahmen Carbon, kein Vergrößern.

## Startscreen
- Bühne vollflächig (0–480 px, rund 57 % der Höhe), ohne Verlauf; Titel 28 px 500 Carbon mittig, 118 px von oben, darunter eine Zeile 14 px und ein unterstrichener Textlink.
- Unten in der Bühne das Paar Blau über Weiß, je 40 px, volle Breite minus 24 px, 8 px Abstand; darunter drei Karussell-Punkte (6 px, aktiv gefüllt, inaktiv Ring).
- Auf Weiß ein Thema: Titel 17 px 500 mittig, darunter eine Reihe 2:1-Kategoriekarten (250×125 px), rechts deutlich angeschnitten, dann die Kennzahlenzeile.
- Unten fest die Suchleiste auf Glas.

## Komponenten
- Buttons: 4 px Radius, min. 40 px hoch, 14 px 500, 3 px transparenter Rand für den Fokus. Primär `#3E6AE1` mit Weiß (Hover dunkler, Empfehlung `#3457B1`); Sekundär Weiß mit Graphite `#393C41`, auf Weiß als Light Ash `#F4F4F4`. Höchstens zwei pro Screen, mobil gestapelt.
- Textlinks: 14 px 400 Pewter `#5C5E62`, 1-px-Unterstrich (box-shadow), paarweise unter Produktnamen („Ansehen“ · „Teilen“).
- Karten und Kacheln: Kategoriekarte 2:1, 12 px Radius, Foto randlos, weißes Label 16 px 500 oben links (16 px Abstand), kein Verlauf, kein Schatten. Produktkarte ohne Fläche und Rand: Bild freigestellt bzw. eckig, Name 17 px 500 mittig, Zeile 14 px, zwei Textlinks.
- Listen: Empfehlung: Zeilen 56 px ohne Trennlinien, Icon 24 px links, Text 14 px, Wert rechts in Pewter; Trennung nur durch Abstand.
- Suche und Eingabefelder: 44 px, 4 px Radius, 1 px `#D0D1D2`, Text Carbon, Platzhalter Silver Fog `#8E8E8E` 14 px; Fokus = 2-px-Innenrahmen Carbon. Feste Leiste unten: Glas, 1 px `#EEEEEE` oben, Lupe + Platzhalter + Senden-Pfeil auf Light Ash.
- Chips, Tabs, Filter: dieselben Text-Buttons wie die Navigation (14 px 500, 32 px hoch, 4 px), aktiv = graue Fläche, mittig gruppiert; keine Pill-Chips.
- Dialoge und Sheets: weiße Fläche ohne Schatten über Scrim `rgba(128,128,128,.65)`; Empfehlung: Sheet oben 12 px Radius.
- Signatur-Komponenten: Buttonpaar Blau/Weiß; Karussell-Punkte; feste Frage-/Suchleiste; Kennzahlenzeile (Wert 24–28 px 500 über Label 14 px, drei Spalten mittig) und Kaufleiste unten (Info links, Blau rechts) – beide App-Muster der Marke (nicht in der Datei), von Modell- und Konfigurator-Seiten.

## Icons
- Stil (Empfehlung; die Datei nennt nur Hilfe-, Globus- und Konto-Icons): dünne, runde, geometrische Linien-Icons, einfarbig Carbon bzw. Pewter; nie gefüllt, nie blau.
- Größe und Strich: 24 px in Leisten, 20 px in Feldern; sichtbarer Strich ≈ 1,1 px.
- Einsatz: sparsam – Leisten-Aktionen, Suche, Senden, Zurück; nie als Deko in Karten, nie neben Button-Text.
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Outlined, Gewicht 200–300, Füllung 0; iOS SF Symbols `.light`; Web Phosphor Light.

## Bildsprache
- Laut Datei: Fotografie trägt das ganze Gefühl – weite Landschaften, Studiolicht, randlos mit `object-fit: cover`; Text liegt ohne Verlauf direkt auf dem Bild (Carbon auf hellem Himmel, Weiß auf dunklen Bildern).
- Formate: Bühne vollflächig im Hochformat, Kategoriekarten 2:1 mit 12 px, Produkte freigestellt auf Weiß (App: 16:9, eckig), Fotoraster eckig mit 2 px Fuge.
- Keine Filter, Körnung, Rahmen; Hauptmotiv (Sonne, Fahrzeug, Straßenbahn) bleibt frei von Buttons.

## Typografie-Stimme
- Display/Text-Paar einer Familie: Bühnentitel 40 px Web / 28 px App, 500, Zeilenhöhe 1,2; Produktname 17 px 500; Text, Navigation, Buttons 14 px 400/500, Zeilenhöhe 20 px; Promo-Zeile 22 px 400.
- Nur zwei Gewichte (400, 500), Laufweite überall normal, keine Versalien, keine Kursive; Größenkontrast nur Bühnentitel gegen den 14-px-Rest.
- Freier Ersatz: Poppins 400/500 (geometrisch wie Universal Sans und Gotham); alternativ Inter 400/500.

## Form, Tiefe und Material
- Radien: 0 px Standard (Bilder, Flächen), 4 px alle Bedienelemente, 12 px Kategoriekarten, 50 % Punkte und Avatare.
- Linien und Rahmen: keine Kartenrahmen; nur Eingabefeld 1 px `#D0D1D2` und Leistenkante 1 px `#EEEEEE`.
- Schatten und Ebenen: keine Schatten. Ebenen über Lage und Deckkraft: Glas `rgba(255,255,255,.75)` + 20 px Unschärfe (Empfehlung), Scrim `rgba(128,128,128,.65)`, seltener Hover-Hauch `rgba(0,0,0,.05)`.
- Besondere Oberflächen: milchiges Glas nur für die Kopfleiste beim Scrollen; Fußleisten weiß mit 1-px-Kante; sonst nur Weiß, Light Ash und Foto.

## Bewegung
- Laut Datei: alle Zustandswechsel 0,33 s (border-color, background-color, color), box-shadow 0,25 s; Textlinks mit `cubic-bezier(0.5, 0, 0, 0.75)`; Fokus-Rahmen blendet per inset-Schatten ein; Karussell wechselt automatisch; Kopfleiste ohne Einschieben.
- Empfehlung: Dauer klein 330 ms / Screenwechsel 500 ms, Easing `cubic-bezier(.5, 0, 0, .75)`; Druck-Effekt nur Flächenfarbe; Einblenden reine Deckkraft (Bild 500 ms, Text 330 ms, 80–120 ms versetzt); Screenwechsel Überblenden; kein Skalieren, Verschieben, Federn; Fokus (TV) Rahmen in 330 ms.
- Compose: `tween(330, easing = CubicBezierEasing(0.5f, 0f, 0f, 0.75f))`, `animateColorAsState`, `Crossfade`, `AnimatedVisibility(fadeIn(), fadeOut())` ohne Slide.

## Signatur-Elemente
1. Vollflächige Foto-Bühne pro Screen, Titel mittig oben direkt auf dem Bild.
2. Buttonpaar mit 4 px Radius: Blau `#3E6AE1` + Weiß, mobil gestapelt.
3. Radikale Kargheit: keine Schatten, Rahmen, Verläufe; Blau nur für die Hauptaktion.
4. Text-Navigation mit grauer Aktiv-Fläche, Kopf- und Fußleiste aus milchigem Glas.
5. Feste Eingabeleiste unten.

## Übertragung auf eine App
- Startscreen: Bühne mit dem Hervorgehobenen (Titel, Zeile, Buttonpaar, Punkte), darunter ein Thema als 2:1-Kategoriekarten, unten die Suchleiste.
- Liste und Übersicht: Seitentitel 28 px mittig mit Zahlenzeile, Filter als Text-Buttons, 2-spaltiges Produktraster ohne Karten (Bild 16:9, Name, Zeile, zwei Textlinks).
- Detail: Bühne mit Titel, Kennzahlenzeile, Umschalter als Text-Buttons, randloses eckiges Fotoraster; Kaufleiste unten mit Info links und blauem Button rechts.
- Formulare und Einstellungen: Felder 44 px mit 4 px, Labels 14 px 500 darüber, Zeilen ohne Trennlinien; ein blauer Button am Ende, volle Breite.
- Leere Zustände und Laden: Weiß mit einem Satz 14 px Pewter und einem Sekundärbutton; Bilder laden als Light Ash und blenden ein, kein Schimmer.
- TV: eine Bühne pro Seite, Text-Navigation oben, darunter eine Reihe 2:1-Karten; Fokus = Rahmen, kein Zoom.
- Musterscreens: Start als Foto-Bühne „Herbstwald“ mit Buttonpaar und Kategoriekarten, Bibliothek als zentriertes Produktraster, Album „Lissabon“ mit Kennzahlenzeile, eckigem Raster und Kaufleiste.

## Vermeiden
- Schatten, Verläufe, Muster, Kartenrahmen; eine zweite Akzentfarbe; Blau für Deko, Links oder Aktiv-Zustände.
- Mehr als zwei Buttons pro Screen; Pill-Buttons oder große Radien an Bedienelementen.
- Versalien, Fett (700), Light (300), negative Laufweite; Titel über 40 px.
- Hover- und Druck-Effekte mit Skalieren oder Verschieben, Federn, Parallaxe.
- Dichte Kartenraster, mehrere Abschnitte übereinander, Verlauf hinter Text auf Fotos, Buttons über dem Hauptmotiv.
