---
slug: airbnb
marke: Airbnb
website: https://www.airbnb.com
ansatz: galerie
ansatz2:
modus: hell
aufbau: Weiße Fläche, Fotokarten mit 14 px Radius und Angaben darunter; offener Kopf, dichter Marktplatz darunter
navigation: Such-Pille oben, Bereichs-Tabs mit Tinten-Unterstrich; unten Tab-Leiste mit 4–5 Zielen, aktiv in Rausch
komponenten: Such-Pille mit Segmenten und Rausch-Kugel, Fotokarte mit Herz und Badge, feste Aktionsleiste unten
icons: schlichte Linien-Icons 1,5–1,75 px, runde Enden, in Tinte; Herz weiß umrandet, gespeichert Rausch gefüllt
bewegung: ruhig; Drücken = nur Farbwechsel, Karten heben sich mit dem einen Schatten; 200 ms, cubic-bezier(.2,0,0,1)
schrift: eine freundliche Grotesk (Cereal, Ersatz Inter), moderat 500–600, Titel 20–28 px; einzig laut: 64-px-Kennzahl
---
# Airbnb – Designsprache

**Kurz:** Ein heller, fotogetriebener Marktplatz: Weiß und Tinte (#222222) tragen rund 90 % jedes Screens, das Pink-Rot „Rausch“ (#ff385c) erscheint nur ein- bis zweimal – Hauptbutton, Such-Kugel, gespeichertes Herz. Alles Bedienbare ist rund (Pillen, Kreise, 8–14 px), die Schrift bleibt bescheiden (500–600), Fotos tragen die Hierarchie. Angaben stehen unter dem Foto, nie darauf.

## Wirkung
- Charakter: warm, großzügig, vertrauenswürdig; freundlich durch runde Formen, ruhig durch fast keine Farbe; „offener Kopf, dichter Marktplatz darunter“.
- Passt zu: Marktplätzen, Reise- und Buchungs-Apps, Foto- und Sammel-Apps, Wunschlisten – überall, wo viele Bilder zur Auswahl stehen.
- Passt weniger zu: dichten Dashboards, Profi-Werkzeugen, dunklen Medien-Apps (die Datei kennt keinen Dark Mode).

## Aufbau und Raster
- Seitenaufbau: oben die Suche als Pille, darunter Bereichs-Tabs, dann Abschnitte „Titel ›“ mit Kartenreihen; Detail = Foto oben, Inhalt darunter, Hauptaktion in fester Leiste unten.
- Ausrichtung: linksbündig; im App-Detail Titelblock und Kennzahl-Karte zentriert (Empfehlung).
- Raster: 4-px-Basis mit 2-px-Mikroschritt, Tokens 2/4/8/12/16/24/32/48/64 px. Web max. ~1280 px (Detail ~1080 px); Karten 4-up → 2-up → mobil 1-up – Spalten werden reduziert, nie Reihen umbrochen.
- Dichte und Weißraum: Bänder 64 px (Web), Karten nur 16 px auseinander, Meta-Block 16 px, Datumszeilen 8 px, große Karten 24 px Innenabstand; in der App 24 px Seitenrand, Kartentext 8–10 px unter dem Foto, 22–32 px zwischen Abschnitten (Empfehlung).
- Rhythmus: Abschnittstitel 20/600 → Fotokarten → Luft; im Detail trennen 1-px-Haarlinien (#ebebeb) die Abschnitte.

## Navigation
- Website: 80 px weiße Kopfleiste mit Haarlinie; Zeichen links, drei Produkt-Tabs mittig (illustriertes 32-px-Icon über Label 16/600; aktiv 2-px-Unterstrich in Tinte, inaktiv #6a6a6a; „NEU“-Pille am Icon), Konto rechts. Unter 744 px: Menü-Sheet, Suche als eine Pille.
- App (Empfehlung): oben Such-Pille, darunter bis zu drei Bereichs-Tabs mit illustrierten Icons und Unterstrich. Unten Tab-Leiste mit 4–5 Zielen: Linien-Icon 24 px + Label 11/500; aktiv Rausch + Strich 2,25 px + Label 600 (Rausch allein wirkt in Graustufen heller als das inaktive Grau); inaktiv #6a6a6a; weiß mit Haarlinie oben; blendet beim Runterscrollen aus. Detailseiten ohne Tab-Leiste: runder Zurück-Knopf auf dem Foto, unten Aktionsleiste.
- TV (Empfehlung): Bereichs-Tabs als Reihe oben mit Unterstrich, Inhalte in horizontalen Kartenreihen; Fokus siehe Bewegung.

## Startscreen
- Such-Pille: mobil einteilig (laut Datei; Lupe + Text 14/600 zentriert als Empfehlung), breit mit Segmenten + Rausch-Kugel; darunter Bereichs-Tabs und Haarlinie.
- Titel bewusst klein direkt unter der Suche (Web-H1 28/700 laut Datei; App-Begrüßung 22/600, Empfehlung) – Fotos tragen die Hierarchie.
- Ein Highlight als große Fotokarte mit Badge, dann Abschnitte „Titel ›“ mit horizontal angeschnittenen Kartenreihen; unten ruhige Text- oder Pillen-Links ohne Kartenfläche.

## Komponenten
- Buttons: Primär Rausch, Text weiß 16/500, Radius 8, Höhe 48, Padding 14×24; gedrückt #e00b41 ohne Transform; deaktiviert #ffd1da. Sekundär weiß mit 1-px-Tintenrand, Radius 8. Tertiär: Tintentext, unterstrichen. Pillen-CTA: Rausch, Radius voll, 10×20, 14/500.
- Karten und Kacheln: Fotokarte ohne Fläche und Rahmen – Foto 1:1 (Erlebnis 4:5), 14 px Radius; links oben weiße Badge-Pille (11/600, 4×10, mit Schatten), rechts oben Herz, Karussell-Punkte; darunter (Web) 4–5 Zeilen: Titel 16/600, Angaben 14/400 #6a6a6a, Preis rechtsbündig; in der App kompakt Titel + eine Angabenzeile mit fetter Kennzahl (Empfehlung).
- Listen: Ausstattungszeilen Icon + Text 16/400, 12 px vertikal, ohne Trennlinien, Block oben/unten mit Haarlinie. Link-Raster: Titel 16/600 + Unterzeile 14 muted, ohne Fläche.
- Suche und Eingabefelder: Such-Pille weiß, Radius voll, Höhe 64, 1 px #dddddd + Schatten; Segmente durch 1-px-Linien getrennt (Label 14/500, Wert 14 muted; mobil 60 px hoch, Label 12/600, Empfehlung); rechts 48-px-Kreis in Rausch mit weißer Lupe. Textfeld 56 px, Radius 8, 1 px #dddddd, Label oben; Fokus 2 px Tinte, kein Glow.
- Chips, Tabs, Filter: Kategorie-Leiste 14/500, aktiv Tinte + 2-px-Unterstrich, inaktiv muted (Icon über Label: Empfehlung); Filter als weiße Pillen mit Haarlinie (Empfehlung); Datumskreise 40 px, gewählt Tinte gefüllt, Spanne dazwischen #f7f7f7.
- Dialoge und Sheets: weiße Fläche über Scrim Schwarz 50 %; Menüs mit dem einen Schatten; Inhalt als Textspalten ohne Kartenflächen.
- Signatur-Komponenten: Such-Pille mit Rausch-Kugel; Fotokarte mit Herz; Kennzahl mit Lorbeerzweigen links und rechts (64/700, darunter Wertespalten in Tinte; mobil als kompakte Haarlinien-Karte mit Lorbeer-Label und 2 Wertespalten, Empfehlung); Reservierungsleiste (mobil fest unten mit Zusammenfassung + Primärbutton; Zusammenfassung unterstrichen: Empfehlung).

## Icons
- Stil: Bedien-Icons als schlichte Linien mit runden Enden, einfarbig Tinte (Empfehlung); Sterne und Bewertungen in Tinte, nie gelb (laut Datei). Bunte, illustrierte Icons nur in den Bereichs-Tabs.
- Größe und Strich: 24 px mit 1,5–1,75 px Strich (Tab-Leiste, Kategorien; aktiver Tab 2,25 px), 16–18 px mit 2–2,75 px in Knöpfen – optisch immer ~1,5–2 px.
- Einsatz: Herz auf Fotos weiß umrandet mit 50 % schwarzer Füllung (Empfehlung), gespeichert Rausch gefüllt (laut Datei); Füllung sonst nirgends. Runde Icon-Knöpfe 32 px #f2f2f2 auf Weiß (laut Datei), auf Fotos weiß 36 px mit Schatten (Empfehlung).
- Umsetzung: Compose `Icons.Rounded` bzw. Material Symbols Rounded (Gewicht 300–400, Füllung 0; Herz gespeichert Füllung 1); iOS SF Symbols Regular (`heart.fill` gespeichert); Web Lucide (stroke 1.5–2.75 je nach Größe) oder Phosphor Regular.

## Bildsprache
- Fotos sind das Hauptmaterial und tragen die visuelle Last (laut Datei); immer mit 14 px Radius beschnitten, ohne Rahmen, ohne Text darauf – nur Badge, Herz, Punkte.
- Karten 1:1, Erlebnisse 4:5; Detail mobil vollbreit oben mit Zähler „1 / n“ als dunkle Pille, breit als Collage 1 groß + 4 klein mit nur außen runden Ecken (Empfehlung).
- Helle, natürliche Fotos ohne Filter, Verläufe, Körnung oder Duplex (Empfehlung).

## Typografie-Stimme
- Eine Familie für alles (Airbnb Cereal VF, Fallback Circular/System). Moderat: Startseiten-H1 28/700, Detail-H1 22/500 −0,44 px, Abschnitte 20/600 −0,18 px, Text 16/400/1,5, Angaben 14/400/1,43, Badge 11/600, NEU-Tag 8/700 Versalien +0,32 px.
- Einziger lauter Moment: Kennzahl 64/700 −1 px (Bewertung im Detail). Versalien sonst kaum; Laufweite neutral; Zahlen und Sterne in Tinte.
- Freier Ersatz: Inter (laut Datei; Display-Zeilenhöhe ~2 % enger), runder: DM Sans oder Nunito Sans (Empfehlung).

## Form, Tiefe und Material
- Radien: 4 / 8 (Buttons, Felder) / 14 (Karten, Fotos) / 20 / 32 (Kategorie-Elemente) / voll (Suche, Herz, Kugel, Badges); keine harte Ecke an Bedienelementen.
- Linien und Rahmen: 1 px #dddddd (Suche, Felder, Karten), #ebebeb für ruhige Trenner, #c1c1c1 für deaktivierte Ränder; Fokus 2 px Tinte.
- Schatten und Ebenen: genau eine Stufe `0 0 0 1px rgba(0,0,0,.02), 0 2px 6px rgba(0,0,0,.04), 0 4px 8px rgba(0,0,0,.1)` für Such-Pille, Badges, Menüs, schwebende Karten; sonst flach. Scrim Schwarz 50 %.
- Besondere Oberflächen: keine – Weiß auf Weiß, Tiefe nur durch Foto, Rundung und den einen Schatten.

## Bewegung
- Laut Datei: Primärbutton gedrückt nur Farbwechsel zu #e00b41, kein Transform, keine Schattenänderung; Karten heben sich beim Zeigen leicht (Schattenstufe); Feld-Fokus 2 px Tinte ohne Glow. Sonst keine Angaben.
- Empfehlung: klein 200 ms, Screenwechsel 350 ms, Easing `cubic-bezier(0.2, 0, 0, 1)`; Karten blenden 8 px von unten ein, 40 ms gestaffelt; Herz beim Speichern kurzer Pop (1 → 1,2 → 1, 400 ms, Feder); Karte → Detail als Shared Element (Foto wächst zur Bühne); Sheets gleiten von unten; Fokus (TV) Schattenstufe + 1,04-fach + 2-px-Tintenrahmen mit 3 px Abstand, 200 ms.
- Compose: `tween(200, easing = CubicBezierEasing(0.2f, 0f, 0f, 1f))`; Herz `spring(dampingRatio = 0.5f, stiffness = 400f)`; `AnimatedVisibility(fadeIn() + slideInVertically { it / 8 })`; `Modifier.animateItem()`; `SharedTransitionLayout` für Karte → Detail.

## Signatur-Elemente
1. Such-Pille (Radius voll, Haarlinie + Schatten), breit mit Segmenten und runder Rausch-Kugel.
2. Fotokarte: 14-px-Foto ohne Kartenfläche, weißes Badge links oben, Herz rechts oben, Punkte, Angaben darunter.
3. Rausch nur sparsam: Hauptbutton, Such-Kugel, gespeichertes Herz – sonst Weiß und Tinte.
4. Unterstrich-Tabs (2 px Tinte) mit illustrierten Bereichs-Icons und NEU-Pille.
5. Detail: Kennzahl mit Lorbeerzweigen und feste Aktionsleiste unten (Zusammenfassung unterstrichen + Rausch-Button).

## Übertragung auf eine App
- Startscreen: Such-Pille, drei Bereichs-Tabs mit illustrierten Icons, kleine Begrüßung, eine große Fotokarte als Highlight, dann Abschnitte „Titel ›“ mit angeschnittenen Kartenreihen und weiße Pillen als Schnellzugriff.
- Liste und Übersicht: segmentierte Such-Pille mit Rausch-Kugel, Kategorie-Leiste mit Unterstrich, 2-spaltiges Foto-Raster (1:1, 14 px) mit Titel + Angaben darunter; schwebende Tinten-Pille „Karte“ über der Tab-Leiste (Empfehlung).
- Detail: Foto vollbreit mit weißen Kreis-Knöpfen (Zurück, Teilen, Herz, Mehr), weißes Blatt mit 24 px oberen Ecken (Empfehlung), Titelblock zentriert, Kennzahl-Karte mit Lorbeer, Unterstrich-Tabs, Foto-Collage; feste Leiste unten: links Zusammenfassung, rechts Rausch-Button.
- Formulare und Einstellungen: weiße Liste, Zeilen Icon + Text 16 px + Chevron, Abschnitte durch Haarlinien; Felder 56 px, Radius 8, Fokus 2 px Tinte; Hauptbutton unten vollbreit in Rausch.
- Leere Zustände und Laden (Empfehlung): zentrierter Titel 22/600, ein Satz 16 muted, Sekundärbutton mit Tintenrand; Laden als graue Kartenformen (#f2f2f2, 14 px) mit sanftem Pulsieren.
- TV (Empfehlung): Fläche #f7f7f7 statt grellem Weiß, Karten 4-up, Bereichs-Tabs oben, Fokus wie unter Bewegung.
- Musterscreens: Start mit Such-Pille, illustrierten Bereichs-Tabs, Begrüßung, Rückblick-Karte, Kartenreihe und Quellen-Pillen; Bibliothek mit segmentierter Suche + Rausch-Kugel, Kategorie-Leiste, Foto-Raster und Karten-Pille; Detail mit Foto-Bühne, Lorbeer-Kennzahl, Collage und Diashow-Leiste.

## Vermeiden
- Rausch als Fläche, für mehrere Buttons pro Screen oder für Überschriften; eine zweite Markenfarbe (Luxe-Lila, Plus-Magenta nur in Sub-Marken).
- Text oder Verläufe auf Fotos, Rahmen um Fotokarten, mehrere Schattenstufen.
- Schwere oder riesige Titel (800+), Versal-Überschriften, gelbe Sterne, reines Schwarz für Text.
- Harte Ecken an Bedienelementen; Material-Standard (FAB, farbige App-Bar); dunkle Flächen als Standard.
