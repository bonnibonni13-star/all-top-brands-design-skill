---
slug: binance
marke: Binance
website: https://www.binance.com
ansatz: daten
ansatz2: werkzeug
modus: dunkel
aufbau: Fast schwarze Fläche #0b0e11, flache Blöcke #1e2329; Kennzahl oben, darunter dichte Tabellen-Listen
navigation: Oben Avatar + Suchfeld; unten feste Leiste (4 Ziele, Icon + Label), aktiv gefülltes Icon + Weiß + 600
komponenten: Gelber Button 6 px, Kennzahl-Block, Markt-Tabelle mit Spaltenköpfen, Text-Tabs mit Gelbstrich
icons: Phosphor Regular 20–22 px grau, aktiv Fill weiß; Richtung als gefüllte Dreiecke grün/rot (Empfehlung)
bewegung: Sachlich schnell: 150/250 ms, cubic-bezier(.2,0,0,1); Werte blitzen kurz grün/rot auf (Empfehlung)
schrift: Inter 600/700 (BinanceNova-Ersatz), Text 12–14 px; jede Zahl in eigener Tabellen-Stimme (Mono-Ersatz)
---
# Binance – Designsprache

**Kurz:** Eine Handelsplattform-Sprache: fast schwarze, flache Farbblöcke, auf denen Zahlen die Hauptrolle spielen – groß, fett und in einer eigenen tabellarischen Zahlenschrift. Ein einziger Akzent, Binance-Gelb (#FCD535) mit schwarzer Schrift, trägt jede Hauptaktion; Grün/Rot zeigen ausschließlich Richtung (steigt/fällt). Trennung entsteht durch Kontrast und Haarlinien, nicht durch Weißraum oder Schatten.

## Wirkung
- Charakter: selbstsicher, energisch, technisch-dicht, vertrauenswürdig durch Zahlen; eher Terminal als Magazin.
- Passt zu: Finanz-, Statistik-, Speicher- und Verwaltungs-Apps, Dashboards, Tracker, alles mit Werten über die Zeit.
- Passt weniger zu: ruhigen Lese-Apps, Kinder-Apps, emotional-bildgetriebenen Lifestyle-Marken.

## Aufbau und Raster
- Seitenaufbau: oben Kopf mit Avatar und Suchfeld, darunter ein Kennzahl-Block (Wert + Richtung + gelbe Aktion), dann flache Karten und Tabellen-Listen.
- Ausrichtung: linksbündig; Zahlen rechtsbündig in Spalten, jede Tabelle mit Spaltenkopf in muted 12 px.
- Raster: 4-px-Basis, Abstände 4/8/12/16/24/32/48 px; Web 12 Spalten, Produktseiten 8/4-Teilung; Inhalt max. 1280–1440 px.
- Dichte und Weißraum: dichter als übliche Marketing-Seiten; App-Ränder 16 px, Zeilen 52–60 px (12 px vertikal + Haarlinie), Kartenabstand 12–16 px, Karteninnen 16 px (Web 24 px).
- Rhythmus: Kennzahl → Karte → Tab-Reihe + Tabelle; Bänder im Web einheitlich 80 px – die Fläche wechselt, der Takt bleibt.

## Navigation
- Website: Kopfleiste 64 px auf #0b0e11, Wortmarke gelb links, Menü 14 px 500, rechts „Log In“ als Textbutton und gelber Primärbutton; unter 768 px Hamburger mit Vollbild-Sheet, gelbe Aktionen unten verankert.
- App (App-Muster der Marke, nicht in der Datei): oben Avatar 32 px rund (Profil) + Suchfeld (#1e2329, 8 px Radius, 40 px) + Icon-Buttons. Unten feste Leiste auf #0b0e11 mit 1-px-Haarlinie: 4 Ziele Start · Bibliothek · Suche · Profil, Icon 22 px + Label 11 px. Aktiv = gefülltes Icon, Weiß, Label 600; inaktiv Regular-Icon in #707a8a (Empfehlung). Leiste bleibt beim Scrollen stehen. Gelb nie in der Leiste.
- Detail: Kopf wie die Handelspaar-Seite – Zurück-Pfeil, Titel 18 px 600 mit kleinem Typ-Tag und Umschalt-Caret, rechts Favorit und Teilen; unten eine Aktionsleiste statt Navigation.
- TV: linke Spalte mit Zielen, Inhalte als Tabellen-Karten; Fokus = 2-px-Ring #3b82f6 bei 50 % plus Fläche #2b3139.

## Startscreen
- Kennzahl-Block wie „geschätzter Gesamtwert“: Label 13 px muted + Augen-Icon, Wert in der Zahlenstimme 32 px 700, Einheit mit Caret, darunter Richtung „Heute ▲ +1,6 GB (0,39 %)“ in Grün; rechts kompakter gelber Button.
- Darunter Kennzahl-Leiste (3 Spalten, Label 12 px, Wert 16 px) und ein 4-px-Fortschrittsbalken.
- Hervorgehobener Inhalt als Banner-Karte #1e2329 (12 px Radius): Tag, Titel 15 px 600, Angaben, kompakter gelber 28-px-Button, Bild rechts mit 8 px Radius, Seitenpunkte darunter.
- Weitere Bereiche als Tab-Reihe + Tabelle („Quellen · Zuletzt · Favoriten“), Werte mit Richtungszelle.

## Komponenten
- Buttons: Primär Gelb #FCD535, Text #181a20, 14 px 600, 40 px hoch, 6 px Radius, gedrückt #f0b90b, deaktiviert #3a3a1f; Pill-Variante nur für „die“ Aktion einer Seite. Sekundär #1e2329 (auf Hell: Weiß + Haarlinie). Kompakt 28 px, 4 px Radius, 6 × 16 px – passt in Tabellenzeilen. Nie weiße Schrift auf Gelb.
- Karten und Kacheln: flache Fläche #1e2329 auf #0b0e11, ohne Rand und Schatten; 8 px (Inhalt) bzw. 12 px (Container, Tabellen-Karten); verschachtelt #2b3139.
- Listen: Markt-Zeile – rundes Icon/Thumbnail 28–32 px, Titel 14–15 px 600 + kleines Typ-Tag, Angabe 12 px muted; rechts Zahl 14–16 px in der Zahlenstimme, Richtungs-Badge 72 × 30 px (4 px Radius, weiße Ziffern) oder Richtungstext mit Dreieck. Haarlinie #2b3139 bzw. nur Abstand.
- Suche und Eingabefelder: dunkel #1e2329, 8 px Radius, 40 px, 10 × 16 px, Lupe muted; auf Hell weiß mit Haarlinie #eaecef und 6 px. Fokus 2-px-Ring #3b82f6 bei 50 %.
- Chips, Tabs, Filter: Text-Tabs 14–16 px – aktiv Weiß 600 mit 16 × 3 px gelbem Strich darunter, inaktiv muted 500 (Empfehlung). Kleine Filter-Chips 28 px, 4 px Radius, aktiv #2b3139 + Weiß, sonst ohne Fläche. Spaltenköpfe 12 px muted mit Sortier-Caret.
- Dialoge und Sheets: transaktionale Schritte kippen ins Helle (Weiß, Text #181a20, Haarlinie #eaecef, 8 px Karten) – gelber Button bleibt identisch.
- Signatur-Komponenten: Kennzahl-Block mit gelber Aktion; Markt-Tabelle mit Spaltenköpfen und Richtungs-Badges; gelbe Statistik-Zahlen (Zahlenstimme 40 px 700) für Bestands-Aussagen; Banner-Karte mit Kompakt-Button.

## Icons
- Stil (Empfehlung, die Datei nennt nur Coin-Icons): schlichte, geometrische Linien-Icons mit runden Enden, einfarbig #707a8a; aktiv gefüllt in Weiß. Richtung immer als gefülltes Dreieck vor der Zahl.
- Größe und Strich: 16 px in Tabellen, 20 px in Kopf und Feldern, 22 px in der Leiste; Strich ca. 1,5 px. Runde „Coin“-Icons 28–32 px auf #2b3139.
- Einsatz: Icons mit Label in Leisten, allein nur im Kopf (Glocke, Favorit, Teilen); nie gelb, nie bunt.
- Umsetzung: Compose `Icons.Outlined` (aktiv `Icons.Filled`), 20–22 dp; iOS SF Symbols `.regular`, aktiv `.fill`; Web Phosphor Regular/Fill.

## Bildsprache
- Laut Datei: Coin-Icons rund 24/32 px; 3D-Münzstapel als Illustration neben großen Zahlen; Fotos mit 12 px Ecken, mobil randlos.
- Übertragung: Medien bleiben Daten-Objekte – Thumbnails rund 28–32 px wie Coin-Icons, Hero-Bild 12 px Radius ohne Verlauf und Text darauf, Raster 4 px Radius mit 4 px Fuge. Keine Filter, keine Körnung, kein Leuchten.

## Typografie-Stimme
- Zwei Stimmen: BinanceNova für Wörter, BinancePlex für jede Zahl (Preise, Mengen, Prozente, Zähler) – auch mitten im Fließtext.
- Display 64/48 px 700 (−1/−0,5 px), Sektionen 40/32 px 600, Titel 24/20/16 px 600, Text 14 px 400 (1,5), Caption 12 px 500, Buttons 14 px 600; Zahlen 40 px 700, 16/14 px 500.
- Gewicht bewusst hoch (700 für Display) – nie auf 400 abschwächen; keine negative Laufweite unter 40 px; keine Versalien außer kurzen Marken-Aussagen.
- Freier Ersatz: Inter für BinanceNova; IBM Plex Sans oder JetBrains Mono für BinancePlex (in den Musterscreens DejaVu Sans Mono, Zeilenhöhe Display −3 %).

## Form, Tiefe und Material
- Radien: 2 px kaum genutzt, 4 px kleine Buttons/Badges, 6 px Buttons/Felder, 8 px Suche/Karten, 12 px Container; Pill nur für die Haupt-Aktion; rund für Coin-Icons und Avatare.
- Linien und Rahmen: Haarlinie #2b3139 (dunkel) bzw. #eaecef (hell) für Felder, Tabellen und Akkordeons – wirkt wie eine Flächenstufe, nicht wie Tinte.
- Schatten und Ebenen: flach – Tiefe nur über Farbsprung #0b0e11 → #1e2329 → #2b3139; Schatten nur, wenn eine Karte über einem Bild liegt.
- Besondere Oberflächen: keine Verläufe, kein Glas; einzige Ausnahme Gelb→Schwarz-Verlauf für Event-Bühnen. Hell (#fafafa) als bewusster Abschluss unter dunklen Seiten.

## Bewegung
- Laut Datei: keine Timings dokumentiert; Zustände nur Normal und Gedrückt (Gelb → #f0b90b).
- Empfehlung: Dauer klein 150 ms / Screenwechsel 250 ms, Easing `cubic-bezier(0.2, 0, 0, 1)`; Druck-Effekt: Farbwechsel ohne Skalierung, Zeile → #1e2329; Einblenden: Deckkraft + 6 px, Zeilen 30 ms gestaffelt; geänderte Werte blitzen 600 ms grün/rot hinterlegt auf; Screenwechsel: seitliches Schieben 250 ms; Fokus (TV): Ring + #2b3139 in 150 ms.
- Compose: `tween(150, easing = CubicBezierEasing(0.2f, 0f, 0f, 1f))`, `animateColorAsState` für Kurs-Blitz, `AnimatedContent` für Zahlenwechsel, `Modifier.animateItem()`; kein Federn.

## Signatur-Elemente
1. Binance-Gelb mit schwarzer Schrift als einzige Akzentfarbe – jede Hauptaktion, gelbe Bestandszahlen, gelber Tab-Strich.
2. Zahlen in eigener tabellarischer Stimme, groß und fett (700), daneben Richtung in Grün/Rot mit Dreieck.
3. Markt-Tabellen: Spaltenköpfe, runde Coin-Icons, rechtsbündige Zahlen, kleine gefüllte Richtungs-Badges.
4. Fast schwarze Fläche mit flachen #1e2329-Blöcken, kleine Radien 4–12 px, keine Schatten.
5. Dichte: 12–14 px Text, 52–60 px Zeilen, Kontrast statt Weißraum.

## Übertragung auf eine App
- Startscreen: Avatar + Suchfeld; Kennzahl „Belegter Speicher 412,0 GB“ mit Tagesrichtung und gelbem „Hinzufügen“; Kennzahl-Leiste Fotos/Videos/Titel; Rückblick als Banner-Karte; Quellen als Tab-Tabelle mit GB-Werten und Richtung.
- Liste und Übersicht: wie die Markt-Seite – Titel, Suchfeld, Text-Tabs mit Gelbstrich, Quellen-Chips, Spaltenkopf (Titel · Inhalte · Aufrufe 7 T.), Zeilen mit rundem Thumbnail, Zahl und Richtungs-Badge.
- Detail: wie die Handelspaar-Seite – Kopf mit Tag und Caret, Bild 12 px, Kennzahl „342 Fotos“ groß mit Richtung, rechts Stat-Spalte, Text-Tabs, dichtes Raster; unten Aktionsleiste mit Musik-Zeile und breitem gelbem Button.
- Formulare und Einstellungen: transaktionale Schritte (Export, Teilen, Speicher kaufen) hell: weiße Fläche, 40-px-Felder mit Haarlinie, Beträge in der Zahlenstimme 40 px, gelber Bestätigen-Button unten.
- Leere Zustände und Laden: ein Icon 32 px muted, ein Satz 14 px, gelber Button; Laden als #1e2329-Platzhalterzeilen, Zahlen erst „--“, dann einblitzen.
- TV: Tabellen-Karten in 2–3 Spalten, große Kennzahlen, Fokus-Ring blau 2 px.
- Musterscreens: Start als Speicher-Dashboard, Bibliothek als Markt-Tabelle mit Richtungs-Badges, Album „Lissabon“ als Handelspaar-Seite mit gelber Aktionsleiste.

## Vermeiden
- Ein zweiter Markenakzent (Türkis ist ein Einzelprodukt-Experiment); Gelb für Fließtext, große Flächen oder Deko; weiße Schrift auf Gelb.
- Grün/Rot für allgemeinen Erfolg/Fehler oder als Kartenfläche – nur Richtung, als Text oder kleines Badge.
- Zahlen in der Text-Schrift; Display-Gewicht 400; atmosphärische Verläufe, Glühen, Glas, Schlagschatten.
- Reines Schwarz als Fläche; große Radien (über 12 px) und Pills für normale Buttons; luftige Material-Karten mit viel Weißraum.
- Unterschied zu Revolut (gleiche Branche): kein Wechsel Schwarz/Weiß in Bändern, keine Pill-Buttons, keine riesigen 500er-Headlines, keine bunten Kategorie-Kreise – Binance bleibt einheitlich dunkel, dicht, gelb und tabellarisch.
