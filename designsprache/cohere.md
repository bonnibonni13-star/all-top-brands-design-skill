---
slug: cohere
marke: Cohere
website: https://cohere.com
ansatz: editorial
ansatz2: minimal
modus: hell
aufbau: Weiße Redaktionsfläche mit einer Riesen-Überschrift je Screen, runden Medienkarten (22 px) und eingesetzten dunkelgrünen Bändern
navigation: Empfehlung: schwebende weiße Pillenleiste unten (4 Ziele, 1 px #d9d9dd), aktiv = fast schwarze Pille; Profil als runder Avatar
komponenten: Medienkarte 22 px mit dunklem Konsolen-Modul, übergroße Korallen-Chips, Linienliste mit Datum rechts, Stein-Karte #eeece7
icons: Empfehlung: dünne geometrische Linien (Lucide 1,25, runde Enden), 18–20 px, einfarbig #212121 bzw. Weiß
bewegung: Empfehlung: ruhig 220/420 ms, cubic-bezier(.22,1,.36,1); 12 px Aufblenden, Medienkarte 1,01 beim Druck
schrift: Mono-artige Display-Titel 400, satzweise, −0,02 em; UI-Grotesk 400 16/18 px; Mono-Versal-Label 11–14 px +0,28 px
---
# Cohere – Designsprache

**Kurz:** Ein Forschungslabor-Look mit redaktioneller Ruhe: viel weiße Fläche, pro Screen genau eine große, eng gesetzte Überschrift in einer mono-artigen Display-Schrift, danach zurückhaltende 16-px-Typografie. Farbe kommt aus Fotos, dunkelgrünen Bändern und übergroßen Korallen-Chips – nie aus der Oberfläche selbst; Karten sind rund (8/22 px), flach und nur mit Haarlinie.

## Wirkung
- Charakter: nüchtern, erwachsen, kontrolliert; „Enterprise-Kommandozentrale mit Magazin-Satz“.
- Passt zu: Bibliotheks-, Archiv-, Lese-, Recherche- und Medien-Apps, Unternehmens-Werkzeugen mit Inhaltsverzeichnis-Charakter.
- Passt weniger zu: verspielten Apps, Dashboards mit vielen Farbflächen, Oberflächen mit starken Schatten und Verläufen.

## Aufbau und Raster
- Seitenaufbau: weiße Leinwand als Grundzustand; große typografische Erklärung oben, darunter gerundete Medienkarten, dann ein eingesetztes dunkelgrünes Band (#003c33, 22 px Radius) und zuletzt Formular/Fuß.
- Ausrichtung: Web-Hero mittig, alle Listen und Produktabschnitte linksbündig; in der App durchgehend linksbündig, Metadaten rechts in der Zeile.
- Raster: 8-px-Basis mit Zwischenwerten (2/6/8/10/12/16/20/22/24/28/32/40/56/64/80); Web 3-spaltige Kartenraster, Forschungslisten volle Breite; App 1-spaltig, Fotoraster 3-spaltig mit 8 px Fuge.
- Dichte und Weißraum: Weißraum als Vertrauenssignal – 32–48 px zwischen Abschnitten (Web 80 px), 20–24 px zwischen Titel und Inhalt; dicht wird es nur dort, wo Information es verlangt (Listenzeilen 14–16 px vertikal).
- Rhythmus: eine Riesen-Überschrift, dann lange Ruhe, dann ein Block mit Inhalt – nie zwei große Stimmen auf einem Screen.

## Navigation
- Website: schwarze Ankündigungsleiste (36 px, Mikrotext) über der Kopfzeile; Kopfzeile dreizonig (Zeichen links, Menü mittig, Anmeldung + Pill-CTA rechts); mobil kompaktes Menü.
- App (Empfehlung, abgeleitet aus Pill-CTA und Filter-Pillen): schwebende weiße Pillenleiste unten (links/rechts 16 px Abstand, Radius 32 px, 1 px #d9d9dd, kein Schatten) mit 4 Zielen Start · Bibliothek · Suche · Profil; aktiv = fast schwarze Pille (#17171c) mit weißem Icon **und** Text, inaktiv nur Icon – der Aktivzustand ist Fläche plus Beschriftung, nicht Farbe. Oben keine Leiste, nur Mono-Label links und runder Avatar rechts.
- Detailseiten: Leiste entfällt; Zurück als runder Umriss-Knopf (36 px, 1 px #d9d9dd) über der Medienkarte, Nebenaktionen als unterstrichene Textlinks.
- TV: linke Spalte mit Textlinks in 24 px, aktiv unterstrichen; Fokus = 2-px-Rahmen in #4c6ee6, keine Vergrößerung.

## Startscreen
- Mono-Label (Versalien, 11 px) als Ortsmarke, darunter die Begrüßung als Riesen-Überschrift 34–40 px, Zeilenhöhe 1,0, −0,02 em; eine Zeile Lead 18 px in #616161.
- Hervorgehobener Inhalt als `hero-photo-card`: Foto mit 22 px Radius, darin unten ein dunkles Konsolen-Modul (#17171c, 8 px) mit Status-Chip, Titel, Angaben und weißer Pille.
- Darunter eine Reihe runder Medienkarten (22 px, rechts angeschnitten) und ein eingesetztes dunkelgrünes Band mit den Quellen und dem Speicherstand.

## Komponenten
- Buttons: Primär = Pille #17171c, Text 14 px 500 weiß, Innenabstand 12 × 24 px, Radius 32 px (auf Dunkel weiße Pille mit dunklem Text); Sekundär = reiner Textlink, unterstrichen, kein Rahmen; Umriss-Pille (1 px, Radius 30 px, 6 × 12 px) für Filter und Umschalter.
- Karten und Kacheln: Medienkarten 22 px (groß) und 8 px (klein), flach, keine Schatten; `product-card` in Warmstein #eeece7 mit 8 px Radius und 16–32 px Innenabstand; `capability-card` oft nur mit Oberlinie statt Rahmen.
- Listen: regelgetrennt und ungerahmt – Titel links (20–24 px), Chip oder Mono-Angabe darunter, Datum rechts in #93939f, 1 px #d9d9dd zwischen den Zeilen; Zeilen hoch (64–80 px), keine Vorschaubilder.
- Suche und Eingabefelder: rechteckig mit 4 px Radius, 1 px #d9d9dd, 12–16 px Innenabstand, Platzhalter #93939f; Fokusrahmen violett #9b60aa, Fokusring #4c6ee6.
- Chips, Tabs, Filter: übergroße Korallen-Taxonomie-Chips (#ff7759) in Überschriftengröße (App 18–20 px, Radius 8 px) – aktiv Korallenfläche mit dunklem Text, inaktiv Korallen-Umriss auf blassem Grund; daneben kleine Umriss-Pillen für Unterfilter.
- Dialoge und Sheets: weiße Karte mit 22 px Radius auf dunkelgrünem oder steinfarbenem Grund, 24–32 px Innenabstand, Aktion als Pille unten.
- Signatur-Komponenten: `hero-photo-card` mit dunklem Konsolen-Modul; dunkelgrünes `dark-feature-band` mit blassen Trennlinien; Korallen-Chip-Reihe; Linienliste mit Datumsspalte; Warmstein-Karte.

## Icons
- Stil (Empfehlung, die Datei nennt nur „dünne geometrische Linien-Illustrationen“ und eine eigene Icon-Schrift): dünne, geometrisch konstruierte Linien mit runden Enden, viel Innenraum, nie gefüllt.
- Größe und Strich: 18 px in Listen und Leiste, 20 px in Knöpfen, 24 px in Illustrationen; Strich 1,25 px auf 24er-Raster.
- Einsatz: sparsam – Suche, Quellen, Wiedergabe, Zurück; kein Icon neben jeder Zeile, Information trägt der Text.
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Rounded, Gewicht 200, Füllung 0; iOS SF Symbols `.ultraLight`/`.thin`; Web Lucide `stroke-width: 1.25; stroke-linecap: round`.

## Bildsprache
- Laut Datei: Bilder sind sichtbare Karten, keine Hintergründe – Produktvideos, Unternehmensfotografie, Artikelbilder und abstrakte 3-D-Renderings mit 8 px bzw. 22 px Radius; Text liegt nur in CTA-Bändern über dem Bild. Keine Verläufe als Oberfläche; Farbe entsteht aus dem Motiv.
- Übertragung: Albumbild als große Karte 22 px (4:3), Fotoraster 8 px mit 8 px Fuge, Avatar rund; keine Filter, keine Tönung, keine Verlauf-Overlays – nur im Konsolen-Modul liegt eine dunkle Fläche über dem Bildfuß.

## Typografie-Stimme
- Zwei Stimmen: mono-artige Display-Schrift für die eine Riesen-Überschrift je Screen (400, Zeilenhöhe 1,0, −1,92 px bei 96 px / −0,02 em), UI-Grotesk 400 für alles andere (18 px Lead, 16 px Text, 14 px Buttons 500, 12 px Mikro).
- Mono-Versal-Label 14 px mit +0,28 px für Kategorie- und Systemmarken; in der App 11 px. Keine fetten Gewichte – Hierarchie entsteht aus Größe, Weißraum und Fläche.
- App-Größen: Screen-Titel 34–40 px, Abschnittstitel 20–24 px, Listentitel 20 px, Text 16 px, Metadaten 14 px #93939f.
- Freier Ersatz: Space Grotesk oder JetBrains Mono 400 für Display (hier DejaVu Sans Mono), Inter 400/500 für UI (Unica77-Ersatz laut Datei).

## Form, Tiefe und Material
- Radien: 4 px Felder und kleine Bilder, 8 px Karten/Chips/Fotokacheln, 16 px gruppierte Blöcke, 22 px große Medienkarten und Bänder, 30 px Filter-Pillen, 32 px CTA-Pillen, voll rund für Avatar und Statuspunkte.
- Linien und Rahmen: 1 px #d9d9dd als Standardlinie, #e5e7eb als Nebenlinie, #f2f2f2 als weichste Kartenlinie; auf Dunkelgrün blasse Linien rgba(255,255,255,.2).
- Schatten und Ebenen: flach – Tiefe entsteht durch Flächenwechsel (Weiß → Stein → Dunkelgrün), Rundung und Bildkontrast; keine Schlagschatten auf Karten.
- Besondere Oberflächen: Warmstein #eeece7, Blassgrün #edfce9, Blassblau #f1f5ff als ruhige Füllflächen; Korallen nur als Taxonomie, Aktionsblau #1863dc nur für Textlinks.

## Bewegung
- Laut Datei: keine Angaben zu Animationen; dokumentiert sind nur Fokuszustände (#4c6ee6 Ring, #9b60aa Feldrahmen) und der Hinweis, keine undokumentierten Interaktionsvarianten zu erfinden.
- Empfehlung: Dauer klein 220 ms / Screenwechsel 420 ms, Easing `cubic-bezier(0.22, 1, 0.36, 1)`; Einblenden mit Deckkraft + 12 px Aufsteigen, Abschnitte 60 ms gestaffelt; Druck: Pille dunkelt leicht ab, Medienkarte skaliert auf 1,01 ohne Schatten; Screenwechsel als ruhiges Überblenden, große Überschrift bleibt stehen; Fokus (TV) 2-px-Rahmen in 220 ms.
- Compose: `tween(220, easing = CubicBezierEasing(0.22f, 1f, 0.36f, 1f))`, `AnimatedVisibility(fadeIn() + slideInVertically { it / 8 })`, `Modifier.animateItem()`, Shared-Element für Medienkarte → Detailbild; kein Überschwingen.

## Signatur-Elemente
1. Genau eine Riesen-Überschrift je Screen in mono-artiger Display-Schrift, satzweise und eng – darunter sofort ruhige 16-px-Typografie.
2. Runde Medienkarte (22 px) mit eingelegtem dunklem Konsolen-Modul (Status-Chip, Titel, weiße Pille).
3. Übergroße Korallen-Chips als Taxonomie auf Überschriftenniveau statt kleiner Filterleiste.
4. Eingesetztes dunkelgrünes Band (#003c33) mit blassen Trennlinien mitten im weißen Fluss.
5. Ungerahmte, regelgetrennte Liste mit Datum rechts – keine Vorschaubilder, keine Kartenränder.

## Übertragung auf eine App
- Startscreen: Mono-Label, Begrüßung als Riesen-Überschrift, Medienkarte mit Konsolen-Modul (Rückblick), angeschnittene Reihe runder Karten, dunkelgrünes Quellen-Band mit Speicherbalken; schwebende Pillenleiste.
- Liste und Übersicht: Riesen-Titel, rechteckiges Suchfeld, Korallen-Chip-Reihe als Filter, danach regelgetrennte Zeilen mit Titel, Umriss-Pille und Datum rechts; keine Vorschaubilder, letzte Zeile angeschnitten.
- Detail: große Medienkarte 22 px mit runden Umriss-Knöpfen, Mono-Label, Titel, Lead-Zeile, Pille „Diashow starten“ plus unterstrichene Textlinks, Umriss-Pillen als Umschalter, Fotoraster 8 px, Warmstein-Karte für die Musik.
- Formulare und Einstellungen: weiße Karte 22 px auf Stein oder Dunkelgrün, Felder rechteckig 4 px mit Label 14 px darüber, Absenden als dunkle Pille; Einstellungen als regelgetrennte Zeilen mit Wert rechts.
- Leere Zustände und Laden: weiße Fläche, dünne geometrische Linien-Illustration, ein Satz 18 px, darunter Textlink; Laden als blasse Stein-Platzhalter mit 8/22 px Radius, ohne Schimmer.
- TV: weiße oder dunkelgrüne Fläche mit großer Überschrift links, Medienkarten 22 px als Reihe; Fokus = blauer 2-px-Rahmen.
- Musterscreens: Start mit Konsolen-Medienkarte und grünem Quellen-Band, Bibliothek mit Korallen-Chips über einer regelgetrennten Liste, Album „Lissabon“ als Medienkarte mit Pille, Textlinks und Stein-Musikkarte.

## Vermeiden
- Koralle oder Blau als große Flächenfarbe; gesättigte Verläufe als UI-Hintergrund; Mitteltöne als Seitenhintergrund.
- Schlagschatten auf Karten; Medienkarten mit weniger als 8 px Radius; jede Zeile in eine Karte stecken, statt Linien und offene Flächen zu nutzen.
- Fette Gewichte und zwei große Stimmen auf einem Screen; die Display/UI-Trennung zu einer einzigen Grotesk einebnen.
- Unterschied zu Together AI (gleiche Branche): dort randlose Nachtblau-Bänder, Verlaufsband, 4-px-Rechtecke, Mono nur klein und versal, dichte Datentabelle mit grauem Kopf und schwarzem Segment-Steg; hier weiße Redaktionsfläche, mono-artige Riesentitel in Satzschreibung, 22-px-Rundungen, Pillen, Korallen-Chips und eine bildlose Linienliste.
