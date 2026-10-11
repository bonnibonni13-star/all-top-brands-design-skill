---
slug: ollama
marke: Ollama
website: https://ollama.com
ansatz: minimal
ansatz2: werkzeug
modus: hell
aufbau: Eine papierweiße Lesespalte wie ein README, zentrierter Einstieg, viel Luft
navigation: Oben Textlinks (3 Ziele) mit grauer Pille als Aktiv-Fläche, Profil als Avatar; keine Leiste unten
komponenten: Schwarze Pille 36 px, Mono-Pfad-Pille, Terminal-Karte, eine dunkle Karte je Screen
icons: Dünne Strichzeichnungen ohne Füllung, 16–20 px, Schwarz; Zustände als Mono-Text (Empfehlung)
bewegung: Fast keine: 120 ms Farbwechsel, kein Versatz, kein Skalieren (Empfehlung)
schrift: Runde geometrische Überschrift 30–36 px über System-Grotesk 16/400, Mono für Technisches
---
# Ollama – Designsprache

**Kurz:** Eine Oberfläche, die aussieht wie ein sorgfältig gesetztes README: papierweiß von Rand zu Rand, eine schmale Lesespalte, große Luft zwischen den Abschnitten und keinerlei Dekoration. Alles Bedienbare ist eine Pille, alles Technische steht in Mono, und genau eine dunkle Fläche pro Seite sagt „hier schauen".

## Wirkung
- Charakter: ruhig, ehrlich, technisch; wirkt wie Dokumentation statt wie Marketing – Zurückhaltung ist hier die Gestaltung.
- Passt zu: Werkzeugen, Entwickler- und Datei-Apps, Einstellungen, Dokumentation, lokalen/privaten Apps, Lese- und Listen-Apps.
- Passt weniger zu: bildgetriebenen Feeds, Shops, Unterhaltung, allem, was Atmosphäre oder Begeisterung erzeugen soll.

## Aufbau und Raster
- Seitenaufbau: eine durchgehende weiße Fläche ohne Bandwechsel. Zentrierter Einstieg (Zeichen → Überschrift → Zahlenzeile → Mono-Pille → schwarze Pille), danach linksbündige Abschnitte.
- Ausrichtung: Einstieg zentriert, alles darunter linksbündig in einer Spalte; Zahlen rechts in Mono.
- Raster: 8-px-Basis (2 · 4 · 8 · 12 · 16 · 24 · 32 px) plus ein einziger großer Abstand von 88 px zwischen Abschnitten (mobil 48 px). Lesespalte max. 720 px, mobil 24 px Seitenrand. Karteninnenabstand 32 px (Preis-/Inhaltskarte), 16 px (Terminal-Karte), Listenzeilen 16 px oben und unten.
- Dichte und Weißraum: innen eng (4–8 px zwischen Titel, Text und Liste), außen sehr weit. Der Weißraum ersetzt jede Trennlinie.
- Rhythmus: Überschrift → kurzer Absatz → Komponente (Pille, Karte, Liste) → viel Luft. Niemals zwei Karten nebeneinander auf dem Handy.

## Navigation
- Website: Kopfleiste 56 px weiß, flach, ohne Rahmen: Zeichen links, Textlinks 14/500, mittig eine Suchpille (#fafafa, 36 px, voll gerundet), rechts „Anmelden" plus die schwarze Pille, die nie verschwindet. Mobil Zeichen links und Hamburger rechts.
- App (Empfehlung, die Datei beschreibt nur die Website): dieselbe flache Kopfleiste als einzige Navigation – drei Textlinks (Start · Bibliothek · Suche) in 14/500; aktiv = schwarze Schrift in einer #fafafa-Pille, inaktiv #737373 ohne Fläche. Rechts Avatar = Profil. Keine untere Leiste, keine Tableiste, kein Schatten beim Scrollen.
- Detail: zurück als sekundäre Pille mit Pfeil (weiß, 1 px #d4d4d4, 36 px) links oben; Favorit, Teilen und Mehr als gleich große Pillen rechts. Darunter optional eine Mono-Zeile als Pfad.
- TV: linke Textliste ohne Flächen, aktiver Eintrag in einer #fafafa-Pille; Fokus = 2-px-Rahmen in Schwarz, keine Bewegung.

## Startscreen
- Zentrierter Einstieg: kleines Strichzeichen (48–56 px), Überschrift 30–36 px/500 in der runden Schrift, eine graue Zahlenzeile 16/400 in #737373.
- Direkt darunter die Signatur: die Mono-Pille (#fafafa, 48 px hoch, voll gerundet) mit Pfad und Menge plus Kopiersymbol rechts – sie ersetzt jedes Hero-Bild. Darunter eine einzige schwarze Pille als Hauptaktion.
- Dann zwei Abschnitte mit 48 px Luft: die eine dunkle Karte (#171717, Radius 12) für den Rückblick und die Terminal-Karte mit Ampelpunkten für die Quellen; zum Schluss eine Liste aus Haarlinienzeilen.

## Komponenten
- Buttons: Pille 9999 px, 36 px hoch, Polster 8/20 px, Label 14/500. Primär Schwarz auf Weiß (Druck #090909), Sekundär weiß mit 1 px #d4d4d4, auf der dunklen Karte weiße Pille mit schwarzer Schrift, deaktiviert #fafafa mit #a3a3a3. Höchstens eine schwarze Pille je Bildschirmhälfte. Keine zweite Buttonform.
- Karten und Kacheln: nur zwei Behandlungen – weiß mit 1 px #e5e5e5 und Radius 12 px, oder invertiert #171717 mit weißer Schrift und Radius 12 px. Nie Schatten, nie Verlauf, nie mehr als eine dunkle Karte pro Screen.
- Listen: Zeilen ohne Seitenpolster, 16 px oben und unten, 1 px #e5e5e5 als Abschluss; Titel 16/500 schwarz, Antwort/Unterzeile 16 bzw. 14/400 in #737373, rechts eine Mono-Zahl. Immer ausgeklappt, keine Akkordeons.
- Suche und Eingabefelder: Suchpille #fafafa, 36–40 px, voll gerundet, Polster 8/16, Lupe 16 px davor; Fokus: Fläche wird weiß plus blauer Standard-Fokusring rgba(59,130,246,.5). Textfeld weiß mit 1 px #e5e5e5, ebenfalls voll gerundet.
- Chips, Tabs, Filter: Befehls-Chips in Mono 14 px, klein geschrieben, Fläche #fafafa, voll gerundet, Polster 6/12; aktiv komplett schwarz mit weißer Mono-Schrift. Keine Unterstrich-Tabs, keine Segment-Schalter.
- Dialoge und Sheets: weißes Blatt, Radius 12 px, 1 px #e5e5e5, Polster 24–32 px, Aktionen als zwei Pillen nebeneinander (schwarz, dann weiß mit Rand).
- Signatur-Komponenten: Mono-Pille mit Kopiersymbol; Terminal-Karte mit drei Ampelpunkten (#ff5f56, #ffbd2e, #27c93f) und Mono-Ausgabe (Kommentare in #a3a3a3); Häkchenliste (✓ schwarz, Text 14/400 in #525252); eine invertierte dunkle Karte als einziger Blickfang.

## Icons
- Stil (Empfehlung, die Datei nennt nur Schloss und Maskottchen): reine Strichzeichnung ohne Füllung, gleichmäßiger dünner Strich, runde Enden, schwarz; wirkt handgezeichnet-ruhig, nie technisch-scharf, nie zweifarbig.
- Größe und Strich: 16 px in Pillen und Listen, 20 px in der Kopfleiste, 48–56 px für das eine Zeichen im Einstieg; Strich 1,5 auf 24er-Raster.
- Einsatz: so selten wie möglich. Zustände („aktuell", „getrennt") stehen als Mono-Wort da, nicht als Symbol; Ampelpunkte nur in der Terminal-Karte; keine Icons in der Navigation.
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Outlined, Gewicht 300, Füllung 0; iOS SF Symbols `.light`/`.regular` ohne `.fill`; Web Lucide `stroke-width: 1.5` mit runden Enden.

## Bildsprache
- Laut Datei: Es gibt keine Fotografie. Die einzigen Bildelemente sind eine handgezeichnete Maskottchen-Illustration, eine Strich-Schlosszeichnung und die drei Ampelpunkte.
- Übertragung: Bilder bleiben Gäste im Dokument – klein, nie randlos, nie als Hintergrund, nie mit Text darauf. Thumbnails 44–56 px und Raster-Fotos mit Radius 12 px und 8-px-Fuge; das eine große Bild im Detail 16:9 mit Radius 12 px und 1 px #e5e5e5, ohne Schatten und ohne Verlauf. Farben der Fotos unverändert lassen – sie sind der einzige Farbfleck auf der weißen Seite. Platzhalter: Fläche #fafafa.

## Typografie-Stimme
- Drei Stimmen: runde geometrische Schrift für Überschriften (36 · 30 · 24 px, Gewicht 500–600), System-Grotesk für alles andere (20 · 18 · 16 · 14 · 12 px, 400/500) und Mono für Pfade, Befehle, Zustände und Zahlen (16 und 14 px).
- Enge Treppe ohne Zwischengrößen (36 → 30 → 24 → 20 → 16), Laufweite überall 0, keine Versalien, keine Kursive, keine Sperrung.
- Fließtext in #737373, nicht in Schwarz; Schwarz bleibt Überschriften, Links und Button-Text vorbehalten. Links sind unterstrichen.
- Größen App: Einstieg 30/33, Screen-Titel 30/36, Abschnitt 24/32, Zeile 16/24, Hilfstext 14/20, Mono 14/20, Fußnote 12/16.
- Freier Ersatz: Überschrift Nunito oder Quicksand 500/600 (hier TeX Gyre Adventor); Text Inter 400/500; Mono JetBrains Mono oder Fira Code (hier DejaVu Sans Mono).

## Form, Tiefe und Material
- Radien: 9999 px für alles Bedienbare (Buttons, Suchfeld, Mono-Pille, Chips, Punkte), 12 px für Karten, Bilder und Raster, 6 px nur für Inline-Code; 0 px für Trennlinien und Leisten. Dazwischen gibt es nichts.
- Linien und Rahmen: 1 px #e5e5e5 für Karten, Listen und die Linie über der Fußzeile; 1 px #d4d4d4 für sekundäre Pillen und stärkere Trennung. Mehr nicht.
- Schatten und Ebenen: keine. Nichts hebt ab, nichts schwebt, nichts überlagert. Tiefe entsteht nur durch die eine invertierte Fläche #171717.
- Besondere Oberflächen: #fafafa als einzige weiche Fläche (Mono-Pille, Chips, aktive Navigation), #171717 als einziger Blickfang; keine Verläufe, kein Glas, keine Körnung, keine Muster.

## Bewegung
- Laut Datei: keine Angaben außer Druckzuständen (Primärpille wechselt auf #090909) und dem blauen Standard-Fokusring.
- Empfehlung: Dauer klein 120 ms / Screenwechsel 180 ms, Easing `cubic-bezier(.4,0,.2,1)`; nur Farb- und Flächenwechsel, kein Skalieren, kein Versatz, kein Staffeln; Einblenden höchstens als Deckkraft in 150 ms; Kopiersymbol wechselt kurz zum Häkchen; Fokus (TV): Rahmen ohne Übergang.
- Compose: `tween(120, easing = CubicBezierEasing(0.4f, 0f, 0.2f, 1f))` nur für Farben, `Crossfade(180)` für Screens; kein `spring`, keine geteilten Elemente, keine Parallaxe.

## Signatur-Elemente
1. Mono-Pille (#fafafa, voll gerundet) mit Pfad und Kopiersymbol direkt unter der Überschrift – sie ersetzt das Hero-Bild.
2. Terminal-Karte mit drei Ampelpunkten und Mono-Ausgabe, Kommentare in Grau.
3. Genau eine invertierte dunkle Karte (#171717, Radius 12) pro Screen als einziger Blickfang.
4. Befehls-Chips in kleingeschriebener Mono statt Tabs oder Segment-Schaltern.
5. Papierweiße Lesespalte mit 48–88 px Luft zwischen Abschnitten und Häkchenlisten statt Kacheln.

## Übertragung auf eine App
- Startscreen: zentriertes Zeichen, Begrüßung, graue Zahlenzeile, Mono-Pille mit Speicherpfad, eine schwarze Pille; danach die dunkle Rückblick-Karte und die Terminal-Karte für die Quellen.
- Liste und Übersicht: Titel 30/500 mit grauer Anzahl, Suchpille, Mono-Befehls-Chips als Filter, dann eine Liste aus Haarlinienzeilen mit kleinem 12-px-Thumbnail, Titel, grauer Unterzeile und rechter Mono-Zahl – kein Raster, keine Karten.
- Detail: Zurück- und Aktionspillen, Bild 16:9 mit Haarlinie, Titel 30/500, graue Angabenzeile, Mono-Pfad-Pille, schwarze Pille neben sekundärer Pille, Häkchenliste für die Angaben, Mono-Chips als Umschalter, Fotoraster mit Radius 12.
- Formulare und Einstellungen: Beschriftung 14/500 über voll gerundetem Feld, Hilfstext 14/400 in #737373 darunter, Abschnitte nur durch Luft getrennt, Abschluss mit einer schwarzen Pille links.
- Leere Zustände und Laden: ein Satz in 16/400 #737373 und eine schwarze Pille, zentriert; Laden als #fafafa-Flächen in Zeilenhöhe, ohne Schimmer.
- TV: Textliste links, Inhalte als 12-px-Raster rechts, keine Flächenwechsel; Fokus als schwarzer Rahmen.
- Musterscreens: README-artiger Start mit Mono-Pille, dunkler Rückblick-Karte und Terminal-Quellen, Bibliothek als Haarlinienliste mit Mono-Chips, Album-Detail mit Häkchenliste und Fotoraster.

## Vermeiden
- Verläufe, Schatten, schwebende Karten, farbige Flächen, Markenfarbe neben Schwarz.
- Mehr als eine dunkle Karte oder mehr als eine schwarze Pille pro Bildschirmhälfte.
- Radien zwischen 13 und 9998 px; Pillen für Karten oder 12 px für Buttons.
- Randlose Bilder, Bildhintergründe, Text auf Fotos, getönte oder gerasterte Fotos.
- Mono für Fließtext, Versalien, gesperrte Schrift, Fließtext in Schwarz.
- Dekorative Trennlinien statt Weißraum; eng gestapelte Abschnitte ohne Luft.
- Abgrenzung zu Vercel: dort Haarlinienkarten mit gestapelten Schatten, Mesh-Verlauf und Tinten-Band; hier gar keine Tiefe, dafür Mono-Pillen und eine Terminal-Karte.
