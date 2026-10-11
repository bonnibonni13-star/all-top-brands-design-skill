---
slug: hashicorp
marke: HashiCorp
website: https://www.hashicorp.com
ansatz: daten
ansatz2: werkzeug
modus: dunkel
aufbau: Schwarze Leinwand, jeder Bereich beginnt mit einer Versal-Augenbraue; Anthrazit-Karten und Tabellenzeilen auf 8-px-Basis
navigation: Unten vier Ziele als eckige 8-px-Felder, aktiv = Anthrazit-Feld + fettes Icon; oben 64-px-Leiste mit weißem Button
komponenten: Augenbraue, Produktkarte in Identitätsfarbe, Anthrazit-Karte mit Haarlinie, Vergleichstabelle, Pill-Marker
icons: Phosphor Regular 20 px, aktiv Bold; sachlich-geometrisch, nie gefüllt-verspielt
bewegung: Empfehlung – nüchtern und knapp, 120/220 ms, cubic-bezier(.2,0,0,1), Flächenwechsel statt Bewegung
schrift: Eine Familie (Inter als Ersatz für hashicorpSans), Display 600/700 eng (1.17–1.21), Fließtext 500 locker (1.50–1.71)
---
# HashiCorp – Designsprache

**Kurz:** Eine schwarze Infrastruktur-Leinwand, auf der Hierarchie nicht durch Schatten, sondern durch Flächenstufen (Schwarz → Anthrazit → Grau) entsteht. Jeder Abschnitt wird von einer kleinen Versal-Augenbraue eingeleitet, und jedes Thema trägt seine eigene Identitätsfarbe – Farbe ist hier Zuordnung, nicht Dekoration. Die Chrome ist monochrom und eckig: 8-px-Ecken, 1-px-Haarlinien, ein weißer Hauptbutton.

## Wirkung
- Charakter: technisch, souverän, ruhig; „gebaut, nicht gestylt“. Mehrere Produkte unter einem Dach, sichtbar sortiert.
- Passt zu: Entwickler- und Infrastruktur-Apps, Verwaltungs- und Monitoring-Oberflächen, Medienarchive mit vielen Kategorien, Enterprise-Dashboards.
- Passt weniger zu: verspielten Consumer-Apps, Marken mit einer einzigen Signalfarbe, hellen Lese-Apps – die Datei kennt ausdrücklich keinen hellen Modus.

## Aufbau und Raster
- Seitenaufbau: Bänder übereinander. Jedes Band = Augenbraue (12 px, Versalien, +0.6 px) → Überschrift → Inhalt. Bänder trennen sich durch Flächenwechsel (canvas #000000 ↔ surface-1 #15181e), nicht durch Linien.
- Ausrichtung: links; Zahlen und Werte rechtsbündig in Tabellen.
- Raster: 8-px-Basis (4/8/12/16/24/32/48), Abschnittsabstand 96 px (App: 32 px), Kartenraster 3-up → 2-up → 1-up.
- Dichte und Weißraum: Kartenpolster 24 px (Preiskarten 32 px, Ressourcenkacheln 16 px), 32 px zwischen Karten, 24 px zwischen Zeilen. Die dunkle Fläche selbst ist der Weißraum.
- Rhythmus: Augenbraue – Titel – Fläche – nächste Augenbraue; nie zwei Überschriften ohne Augenbraue dazwischen.

## Navigation
- Website: klebende 64-px-Leiste auf Schwarz, Zeichen links, Links mittig, rechts weißer Hauptbutton + Anthrazit-Zweitbutton; unter 768 px Hamburger, Hauptbutton bleibt sichtbar.
- App (App-Muster abgeleitet, Empfehlung): oben 64 px hohe Leiste (Zeichen, Titel, weißer 8-px-Button „Importieren“), unten vier Ziele (Start, Bibliothek, Suche, Profil) als **eckige 8-px-Felder** statt Pillen. Aktiv = Feld in surface-2 #1f232b + Haarlinie + Icon in Bold + weißer Text; inaktiv ink-subtle #656a76. Beim Scrollen bleibt beides stehen; die obere Leiste bekommt beim Scrollen eine 1-px-Haarlinie.
- TV: horizontale Reihe oben, Fokus als 2-px-Rahmen in der Identitätsfarbe des Bereichs plus Flächenstufe – kein Zoom, keine Schatten.

## Startscreen
- Augenbraue „RÜCKBLICK“, darunter die große Display-Zeile (28–40 px, 600, -0.6 bis -1.0 px) und zwei Zeilen Fließtext in ink-muted.
- Ein Bild als Karte mit 12-px-Ecken, darunter weißer Hauptbutton (8 px) und Anthrazit-Zweitbutton nebeneinander.
- Danach Augenbraue „SAMMLUNGEN“ und ein 2-up-Raster chromatischer Identitätskarten (je Medienart eine Farbe) mit isometrischem Würfel als Ornament.
- Abschluss: Augenbraue „SPEICHER“ und eine Vergleichstabelle der Quellen mit Spaltenkopf und rechtsbündigen Werten.

## Komponenten
- Buttons: Hauptbutton weiß (#ffffff) auf Schwarz, Text schwarz, 14 px/600, Polster 10×18 px, Radius 8 px – **keine Pille**. Zweitbutton surface-2 #1f232b mit weißem Text, gleicher Form. Dritter Button nackt auf der Leinwand. Produktbuttons tragen die Identitätsfarbe des jeweiligen Bereichs (gelb/cyan mit schwarzem Text).
- Karten und Kacheln: surface-1 #15181e, 1 px Rahmen rgba(178,182,189,.1), Radius 12 px, Polster 24 px, **kein Schatten**. Identitätskarten ersetzen die Fläche durch die Produktfarbe (gleiche Ebene, andere Bedeutung).
- Listen: eher Tabelle als Liste – Spaltenkopf in 11–12 px Versalien (ink-subtle), Zeilen 14 px/500 mit 1-px-Trenner hairline-soft #252830, Werte rechts, kleine 8-px-Miniatur links.
- Suche und Eingabefelder: surface-1, Radius 8 px, Polster 10×14 px, Haarlinie; Fokus = 1 px Rahmen in Akzentblau #2b89ff.
- Chips, Tabs, Filter: `product-pill` – kleine Pille (9999 px), surface-1, 13 px/500 in ink-muted, Polster 4×10 px. Aktive Pille invertiert zu Weiß auf Schwarz. (Einzige Pille im System: die Chips, nie die Buttons.)
- Dialoge und Sheets: surface-1 mit 24-px-Ecken (`cta-banner`-Radius), Haarlinie, kein Schatten; Griff als 1-px-Linie.
- Signatur-Komponenten: Augenbraue; Identitätskarte in Produktfarbe; Vergleichstabelle; isometrische Würfel-Illustration; dichtes Link-Raster im Fuß.

## Icons
- Stil: sachlich-geometrische Linien, gleichmäßige Strichstärke, keine runden Spielereien. Phosphor Regular passt zur geometrisch-humanistischen Schrift.
- Größe und Strich: 20 px in der Navigation, 16–18 px in Zeilen und Buttons, 24 px in Identitätskarten; Strich entspricht Phosphor Regular (≈1.5 px bei 20 px).
- Einsatz: ein Icon je Zeile oder Karte, nie dekorative Häufung. Aktiv-Zustand wird über Fläche + Bold erzeugt, nicht über Füllung in Farbe.
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Outlined, Gewicht 400, Füllung 0 (aktiv Gewicht 600); iOS SF Symbols Regular, aktiv Semibold; Web Phosphor `regular`, aktiv `bold`.

## Bildsprache
- Bilder sind Inhalt, keine Stimmung: Rechtecke mit 12-px-Ecken, 1-px-Haarlinie, 16:9 oder 4:3, ohne Verlauf darüber.
- Auf der Leinwand stehen Bilder frei (keine Rahmenkarte um die Karte).
- Illustrative Ergänzung sind isometrische Formen (Würfel, Quader) in der Identitätsfarbe – flach, zweifarbig, ohne Schlagschatten.
- Miniaturen in Tabellen 36–40 px, Radius 8 px, nie rund.
- Keine Schlagschatten, keine Weichzeichner, keine Farbfilter über Fotos.

## Typografie-Stimme
- Eine Familie für alles (hashicorpSans; Ersatz: Inter). Hierarchie über Gewicht und Zeilenhöhe, nicht über eine zweite Schrift.
- Display 40/28/22 px in 600–700, Zeilenhöhe 1.17–1.21, Laufweite -1.0 bis -0.4 px – eng gestapelt.
- Fließtext 16/14 px in 500, Zeilenhöhe 1.50–1.71 – auffällig locker. Dieser Abstand zwischen eng und locker ist die Stimme der Marke.
- Augenbraue 12 px/600, Versalien, +0.6 px; Caption 13 px/500, +0.2 px.
- Kein Monospace – auch nicht für Zahlen (Entwickler-Marke, aber die Oberfläche bleibt proportional).
- Freier Ersatz: Inter (Google Fonts) 500/600/700, Zeilenhöhen um ~0.02 senken; Alternativen IBM Plex Sans, Geist Sans.

## Form, Tiefe und Material
- Radien: 4 px Chips, 6 px Tags, **8 px Buttons, Felder, Listenelemente**, 12 px Karten, 16 px große Kacheln, 24 px Banner, 9999 px nur für Pillen-Chips und Avatare.
- Linien und Rahmen: 1 px rgba(178,182,189,.1) an jeder Karte; Trenner in Tabellen hairline-soft #252830; Linien sind spürbar, nicht sichtbar laut.
- Schatten und Ebenen: **keine**. Ebene 0 flach, Ebene 1 surface-1, Ebene 2 surface-2, Ebene 3 Produktfarbe (Bedeutung, nicht Tiefe).
- Besondere Oberflächen: chromatische Identitätsflächen (Terraform-Violett #7b42bc, Vault-Gelb #ffcf25, Waypoint-Cyan #14c6cb, Nomad-Grün #00ca8e, Vagrant-Blau #1868f2, Consul-Rot #e62b1e, Boundary-Koralle #f24c53); dezente Verläufe nur in Identitätsflächen.

## Bewegung
- Laut Datei: keine Angaben (nur Pressed-Zustände als eigene Komponenten).
- Empfehlung: klein 120 ms / Screenwechsel 220 ms, Easing `cubic-bezier(.2, 0, 0, 1)`. Druck = Flächenstufe eine Stufe höher (surface-1 → surface-2) plus `scale(.985)`, kein Leuchten. Einblenden: 8 px nach oben + Deckkraft, 40 ms Staffelung je Karte. Screenwechsel: horizontales Schieben ohne Skalierung. Fokus (TV): 2-px-Rahmen in 120 ms.
- Compose: `tween(220, easing = CubicBezierEasing(.2f, 0f, 0f, 1f))`, Druck über `animateColorAsState` der Fläche, Listen mit `animateItem()`, kein `spring` mit Überschwingen.

## Signatur-Elemente
1. Versal-Augenbraue (12 px, +0.6 px) über **jedem** Abschnitt.
2. Chromatische Identitätskarten: je Thema eine eigene Produktfarbe als ganze Kartenfläche.
3. Anthrazit-Karte mit 1-px-Haarlinie und 12-px-Ecken, ohne jeden Schatten.
4. Vergleichstabelle mit Versal-Spaltenkopf und rechtsbündigen Werten auf schwarzer Leinwand.
5. Eckiger weißer Hauptbutton mit 8-px-Ecken – nie eine Pille.

## Übertragung auf eine App
- Startscreen: Augenbraue + Display-Zeile als Einstieg, ein hervorgehobenes Bild als Karte, danach ein 2-up-Raster der Medienarten als Identitätskarten (Fotos violett, Videos cyan, Musik gelb, Alben grün) und zum Schluss die Quellen als Vergleichstabelle mit Speicherwert.
- Liste und Übersicht: Tabelle statt Kartenraster – Spaltenkopf, dichte Zeilen (56–60 px), Miniatur 40 px, Art als kleiner Farbtag, Wert rechts. Filter als Pillen-Chips darüber.
- Detail: ein Thema = eine Farbe. Oben Pfad-Augenbraue, großes Bild, Titel, weißer Hauptbutton + Anthrazit-Zweitbutton, Umschalter als Segment auf surface-1, dann dichtes Fotoraster mit 8-px-Ecken.
- Formulare und Einstellungen: Felder surface-1 mit 8-px-Ecken und Haarlinie, Beschriftung 13 px in ink-subtle darüber, Fokus in Akzentblau; Abschnitte wieder mit Augenbrauen getrennt.
- Leere Zustände und Laden: Platzhalter als Anthrazit-Rechtecke mit Haarlinie (kein Schimmern), kurzer Satz in ink-muted, ein eckiger Zweitbutton.
- TV: schwarze Leinwand, Reihen aus Identitätskacheln, Fokus als 2-px-Rahmen in der Bereichsfarbe plus Flächenstufe.
- Musterscreens: Start mit Augenbraue, Rückblick-Karte, vier Identitätskarten und Quellen-Tabelle; Bibliothek als dichte Tabelle mit Spaltenkopf, Chips und Farbtags; Detail „Lissabon“ in genau einer Identitätsfarbe mit eckigem Hauptbutton und Fotoraster.

## Unterschied zu Mintlify (beide Entwickler-Dokuwelt)
HashiCorp ist **schwarz, eckig und tabellarisch**: Flächenstufen statt Rahmen, Versal-Augenbrauen über jedem Band, Identitätsfarbe je Thema, 8-px-Rechteckbuttons, kein Monospace. Mintlify ist **weiß, pillenförmig und dokumentenhaft**: Himmelsverlauf im Kopf, Haarlinien-Karten auf Weiß, Pillen-Buttons, Inter + Monospace als Paar, ein einziges Grün als Akzentpunkt. Gleiche Branche, gegensätzliche Mittel.

## Vermeiden
- Keine helle Variante der Marke bauen – die Designsprache ist dunkel.
- Keine Pillen-Buttons und keine 0-px-Ecken; 8 px ist die Signatur.
- Keine Schlagschatten auf Dunkel – Tiefe nur über Flächenstufen.
- Nicht mehrere Identitätsfarben in einem Bildausschnitt mischen, wenn der Ausschnitt **ein** Thema zeigt; im Übersichtsraster ist die Reihe der Farben gerade der Sinn (Entscheidung hier: Raster = Sortierung, Detail = genau eine Farbe).
- Keine Grautöne außerhalb von ink / ink-muted / ink-subtle erfinden.
- Keine zweite Schriftfamilie für Überschriften, kein Monospace für Zahlen.
- Augenbrauen nicht weglassen – Abschnitte wirken sonst wie lose Blöcke.
