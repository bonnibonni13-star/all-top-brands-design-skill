---
slug: together.ai
marke: Together AI
website: https://www.together.ai
ansatz: leuchten
ansatz2: daten
modus: gemischt
aufbau: Vollflächige Nachtblau-Bänder (#010120) im Wechsel mit weißen Datenbändern; linksbündig, 4-px-Ecken
navigation: Empfehlung: angedockte Segment-Schiene unten (4 Ziele) auf #ebebeb, aktiv = schwarzes Feld, Mono-Versalien
komponenten: Verdrehtes Verlaufsband, Mono-Versal-Eyebrows, Datentabelle mit grauem Kopf, Pastell-Kennzahlkacheln
icons: Empfehlung: Lucide 1.5 mit eckigen Enden, 16–20 px, einfarbig Schwarz/Weiß; nie gefüllt, nie im Verlauf
bewegung: Empfehlung: technisch knapp 160/280 ms, cubic-bezier(.2,0,0,1); Aufsteigen 8 px gestaffelt, Band driftet
schrift: Grotesk 500 mit negativer Laufweite für Titel (satzweise); Mono-Versalien 11 px +0,55 px für Labels/Buttons
---
# Together AI – Designsprache

**Kurz:** Ein Infrastruktur-Look aus zwei Polaritäten: nachtblaue Bühnen-Bänder mit einem einzigen Schmuckobjekt – dem verdrehten Verlaufsband Orange → Magenta → Periwinkle – und weiße, tabellarische Datenbänder. Alles Technische spricht in Mono-Versalien, alles Erzählende in einer engen Grotesk; Ecken sind fast eckig (4 px), Tiefe entsteht durch den Hell-Dunkel-Wechsel statt durch Schatten.

## Wirkung
- Charakter: ingenieurhaft, präzise, nüchtern mit einem einzigen leuchtenden Auftritt; „Datenblatt mit Bühne“.
- Passt zu: Werkzeug-, Daten-, Entwickler-, Verwaltungs- und Medien-Apps mit Zahlen (Speicher, Umfang, Status); Dashboards.
- Passt weniger zu: verspielten, kindlichen oder sehr emotionalen Lifestyle-Apps; Marken mit vielen Akzentfarben.

## Aufbau und Raster
- Seitenaufbau: Bänder über die volle Breite ohne Radius – oben dunkel (#010120, Bühne mit Titel und Verlaufsband), darunter weiß (Daten, Tabellen, Kacheln); Rhythmus dunkel → hell → dunkel.
- Ausrichtung: streng linksbündig, Text-Stapel nie mittig; Zahlen in Tabellen rechtsbündig mit Tabellenziffern.
- Raster: 4-px-Basis; Abstände 2/4/8/12/16/20/24/32/44/48 px, Abschnitte 80 px (Web); Container 1280 px, Rand 32 px Desktop / 16 px mobil; Karten 3-/2-spaltig, mobil 1-spaltig.
- Dichte und Weißraum: Titel und Lead eng (16 px), dann größere Lücke zur Aktion; Tabellenzeilen dicht (12 px vertikal), Kachel-Innenabstand 24–32 px (App 14–16 px).
- Rhythmus: Der Flächenwechsel trennt die Abschnitte, nicht Linien oder Schatten; innerhalb eines Bands nur 1-px-Linien.

## Navigation
- Website: Kopfleiste auf Nachtblau (16 × 32 px Innenabstand, Links 16 px 400 weiß, 24 px Abstand), nach dem Scrollen weiß; rechts schwarzer und weißer Rechteck-Button; mobil Zeichen + Menü-Icon, Menü als Vollflächen-Overlay.
- App (Empfehlung, abgeleitet aus `toggle-pill-group`): unten angedockt (weiße Fläche, 1 px Linie oben) eine Segment-Schiene #ebebeb mit 4 px Innenabstand und 4 px Radius; 4 Ziele Start · Bibliothek · Suche · Profil, je Icon 18 px + Mono-Versal-Label 10 px. Aktiv = schwarzes Feld mit weißer Schrift (Fläche, nicht nur Farbe); Profil als quadratisches Porträt. Oben nur Zeichen, Glocke und Porträt; die Kopfzeile gehört zum dunklen Band und wird beim Scrollen weiß.
- Detailseiten: Zurück als quadratischer Geister-Knopf (#313641, 36 px, 4 px Radius) im dunklen Band; Schiene ausgeblendet, unten eine dunkle Mono-Leiste (Musik).
- TV: linke Seitenleiste wie `ex-app-shell-row`: aktiv mit schwarzem bzw. weißem Kantenbalken links; Fokus = 2-px-Rahmen, keine Vergrößerung.

## Startscreen
- Nachtblaues Bühnen-Band: Mono-Eyebrow, Begrüßung 36 px 500 (−0,7 px), darunter das Verlaufsband über die volle Breite (Titel steht immer darüber).
- Hervorgehobener Inhalt als `research-card` im Band (1 px rgba(255,255,255,.12), 4 px): Bild, Mono-Etikett, Titel 22 px, Mono-Angaben, weißer + minzfarbener Button.
- Weißes Band: Pastell-Kennzahlkacheln (Minze, Periwinkle, Pfirsich) mit großer Zahl und Mono-Label; Speicher als Tabellenzeile mit Mono-Werten.

## Komponenten
- Buttons: Rechteck 4 px, Label in Mono-Versalien (Datei 16 px, App 13–14 px, +0,08 px), Padding 4 × 24 px, mobil ≥ 44 px hoch. Primär schwarz (#000) – genau einer pro Ansicht; auf Dunkel weiß bzw. Minze #c8f6f9 (nur Bühne); Geist #313641 auf Dunkel; Outline weiß mit 1 px rgba(0,0,0,.08) und 3,25 px Radius. Nie Pill.
- Karten und Kacheln: 4 px Radius, 1 px Linie statt Schatten; `research-card` dunkel mit Linie rgba(255,255,255,.12), 24 px Innenabstand; `stats-card-tinted` pastell, Zahl 28–40 px 500, Label Mono-Versal, 32 px Innenabstand.
- Listen: als Datentabelle – Kopfzeile #ebebeb mit Mono-Versal-Eyebrow 11 px in #959494, Zeilen 12 × 16 px mit 1-px-Linie unten, links Icon/Bild + Name, rechts Zahlenzellen.
- Suche und Eingabefelder: weiß, 1 px rgba(0,0,0,.08), 4 px Radius, Text 16 px; auf Dunkel bleibt das Feld weiß (stärkster Kontrast).
- Chips, Tabs, Filter: `pricing-sub-tab` (3,25 px Radius, 8 × 16 px, Text 14–16 px) – aktiv mit Fläche #ebebeb und 500; Umschalter als Segment-Schiene (aktiv schwarz); `badge-neutral` 4 px Radius, 2 × 8 px.
- Dialoge und Sheets: wie `article-card` (weiß, 4 px, 32 px Innenabstand), Tiefe über getönten Scrim statt Kartenschatten.
- Signatur-Komponenten: Verlaufsband in Bühnengröße; Pastell-Kennzahlkachel; Tabelle mit grauem Mono-Kopf; dunkler Code-Block als Polaritätswechsel im weißen Band; runder schwarzer Schwebe-Knopf (einzige Rundform, einziger Schatten).

## Icons
- Stil (Empfehlung, die Datei nennt keine Icon-Familie): technische Linien-Icons mit eckigen Enden und Gehrungsecken, passend zu 4-px-Ecken und Mono-Labels; einfarbig Schwarz auf Weiß, Weiß auf Nachtblau.
- Größe und Strich: 16 px in Tabellen und Buttons, 18 px in der Schiene, 20 px im Kopf; Strich 1,5 px auf 24er-Raster.
- Einsatz: immer mit Mono-Label oder in quadratischen Knöpfen (36–44 px); nie gefüllt, nie farbig, nie im Verlauf.
- Umsetzung: Compose `Icons.Sharp` bzw. Material Symbols Sharp, Gewicht 300, Füllung 0; iOS SF Symbols `.light`, ohne `.fill`; Web Lucide `stroke-width: 1.5; stroke-linecap: square; stroke-linejoin: miter`.

## Bildsprache
- Laut Datei: einziges Schmuckobjekt ist das Verlaufsband (Orange #fc4c02 → Magenta #ef2cc1 → Periwinkle #bdbbff) aus übereinanderliegenden, durchscheinenden Strängen – nur groß, nie als Fläche, nie umsortiert, keine vierte Farbe. Artikelbilder 16:9 mit 4 px Radius oben; Porträts 1:1 hart beschnitten, keine runden Avatare.
- Übertragung: Medien ohne Filter, 4 px Radius, im Raster mit 4 px Fuge; Vollbild nur randlos ohne Radius am Bandende. Avatare quadratisch. Kein Text auf Bildern, keine Verlauf-Overlays auf Fotos.

## Typografie-Stimme
- Zwei Stimmen: Grotesk für alles Erzählende (Titel satzweise, 400/500, nie 700), Mono-Versalien für alles Technische (Eyebrows, Buttons, Tabellenköpfe, Einheiten).
- Größen: Display 64/40/28/22 px (500; −1,92 / −0,8 / −0,42 / −0,22 px), Lead 18 px, Text 16 px (−0,16 px), Caption 14 px; Mono 16 px Buttons, 11 px Eyebrows (+0,55 px), 10 px Kleingedrucktes.
- App: Begrüßung 36 px, Screen-Titel 28–40 px, Kartentitel 20–22 px, Tabelle 15 px 500, Mono-Labels 10–11 px.
- Freier Ersatz: Inter / Inter Display 400/500 mit `ss01` und etwas engerer Laufweite; Mono JetBrains Mono oder Geist Mono 500 (hier DejaVu Sans Mono).

## Form, Tiefe und Material
- Radien: 0 für Bänder und Vollbilder, 3,25 px Outline-Button und Unter-Tabs, 4 px kanonisch (Buttons, Karten, Kacheln, Badges, Felder), 8 px Feature-Tabs; voll rund nur der Schwebe-Knopf.
- Linien und Rahmen: 1 px rgba(0,0,0,.08) auf Weiß, 1 px rgba(255,255,255,.12) auf Nachtblau; graue Fläche #ebebeb nur für Tabellenkopf und Schienen.
- Schatten und Ebenen: flach; einziger Schatten `0 4px 10px rgba(1,1,32,.1)` für schwebende Elemente.
- Besondere Oberflächen: Verlaufsband mit weichem Glühen auf Nachtblau; dunkler Code-Block im weißen Band als „eine Stufe hoch“. Widerspruch der Datei: Token `hairline` #959494 vs. Fließtext #ebebeb – entschieden: Text-Grau #959494 (Token), Linien laut Komponenten rgba(0,0,0,.08), weiche Fläche #ebebeb.

## Bewegung
- Laut Datei: keine Angaben zu Animationen; das Verlaufsband wirkt als „Tiefe“, die Kopfleiste wechselt beim Scrollen von Dunkel zu Weiß.
- Empfehlung: Dauer klein 160 ms / Screenwechsel 280 ms, Easing `cubic-bezier(0.2, 0, 0, 1)`; Druck: Schwarz → #313641, Outline → Fläche #ebebeb, kein Skalieren; Einblenden: Deckkraft + 8 px Aufsteigen, Zeilen 40 ms gestaffelt; Verlaufsband driftet langsam (14 s, hin und her); Screenwechsel: Überblenden, Kopfband bleibt stehen; Fokus (TV): 2-px-Rahmen in 160 ms.
- Compose: `tween(160, easing = CubicBezierEasing(0.2f, 0f, 0f, 1f))`, `AnimatedVisibility(fadeIn() + slideInVertically { it / 12 })`, `Modifier.animateItem()`, Band per `rememberInfiniteTransition`; kein `spring` mit Überschwingen.

## Signatur-Elemente
1. Wechsel aus nachtblauen und weißen Vollbreiten-Bändern ohne Zwischengrau.
2. Ein verdrehtes Verlaufsband Orange → Magenta → Periwinkle als einziges Ornament, nur in Bühnengröße.
3. Mono-Versalien für Eyebrows, Buttons, Tabellenköpfe und Einheiten gegen satzweise Grotesk-Titel.
4. Datentabelle mit grauem Mono-Kopf und Pastell-Kennzahlkacheln (Minze, Periwinkle, Pfirsich).
5. Fast eckige 4-px-Form überall; schwarzer Rechteck-Button; nur der Schwebe-Knopf ist rund.

## Übertragung auf eine App
- Startscreen: Bühnen-Band mit Begrüßung, Verlaufsband und Rückblick-Karte; weißes Band mit drei Pastell-Kacheln (Fotos, Videos, Titel) und Speicher-Zeile; Segment-Schiene unten.
- Liste und Übersicht: dunkles Kopfband mit Titel, Mono-Zählzeile und weißem Suchfeld; darunter Unter-Tabs und eine Datentabelle (TITEL · ART · UMFANG) mit Badges und rechtsbündigen Zahlen; runder schwarzer Schwebe-Knopf „Hinzufügen“.
- Detail: Band mit Mono-Eyebrow, Titel 40 px und randlosem Bild; im weißen Band schwarzer Button „Diashow starten“ plus Outline-Quadrate, Segment-Umschalter, 3-spaltiges Raster; Musik in dunkler Mono-Leiste.
- Formulare und Einstellungen: Felder weiß mit 1-px-Linie, Label als Mono-Eyebrow darüber; Einstellungen als Tabelle (Name links, Wert rechts, Mono-Einheit).
- Leere Zustände und Laden: weiße Fläche mit 48 px Innenabstand, Mono-Eyebrow + ein Satz + schwarzer Button; Laden als graue Tabellenzeilen (#ebebeb) ohne Schimmer; am Listenende ein riesiges, fast weißes Stencil-Wort (#ebebeb, 64 px) als Abschluss.
- TV: nachtblaue Bühne mit großem Verlaufsband, darunter Kachel-Raster mit 4 px Radius; Fokus = weißer 2-px-Rahmen.
- Musterscreens: Start mit Bühnen-Band und Pastell-Kennzahlen, Bibliothek als Datentabelle unter dunklem Kopf, Album „Lissabon“ mit Hell-Dunkel-Wechsel und Mono-Musikleiste.

## Vermeiden
- Den Verlauf als Flächenfarbe, Icon-Füllung, kleinen Akzent oder Button nutzen; Stopps umsortieren, eine vierte oder fünfte Akzentfarbe ergänzen.
- Pill-Buttons und runde Avatare; weiche Schatten auf hellen Karten; Graustufen-Flächen zwischen Dunkel und Weiß.
- Titel in Mono oder Versalien; Fließtext in Mono; Grotesk-Labels auf Buttons; positive Laufweite bei der Grotesk.
- Mittig gesetzte Textblöcke unter linksbündigem Titel; Text auf Fotos.
- Unterschied zu Cohere (gleiche Branche): dort helle Redaktionsfläche, mono-artige Riesentitel, runde 22-px-Medienkarten und Pill-CTA – hier randlose Nachtblau-Bänder, Verlaufsband, Mono nur klein und versal, 4-px-Rechtecke.
