---
slug: linear.app
marke: Linear
website: https://linear.app
ansatz: werkzeug
ansatz2: minimal
modus: dunkel
aufbau: Fast schwarze Fläche, Inhalte auf Haarlinien-Panels einer vierstufigen Flächenleiter; dicht, linksbündig
navigation: Schwebende Leiste unten (4 Ziele, Icon + Label), aktiv = hellere Fläche; oben Arbeitsbereich-Schalter
komponenten: Haarlinien-Panels 12/16 px, Listen mit Gruppenbändern, Pill-Umschalter, Status-Pills, Eigenschafts-Chips
icons: Feine Linien-Icons (Lucide 1.75), 16 px in Listen, 18 px in Leisten, einfarbig grau, nie gefüllt (Empfehlung)
bewegung: Knapp: 120–200 ms, cubic-bezier(.16,1,.3,1); Fläche eine Stufe heller beim Drücken, kein Federn (Empfehlung)
schrift: Eine Grotesk-Stimme: Titel 600 eng gesperrt, Text 400 in 12–14 px, Mono nur für Zahlen- und Status-Tokens
---
# Linear – Designsprache

**Kurz:** Software-Handwerk auf fast schwarzem Grund: Hierarchie entsteht durch eine vierstufige Flächenleiter und 1-px-Haarlinien, nie durch Schatten oder Verläufe. Inhalte stehen dicht in gerahmten Panels und gruppierten Listen mit kleiner Schrift; ein einziges Lavendelblau markiert nur Zeichen, Hauptaktion und Fokus.

## Wirkung
- Charakter: dicht, technisch, präzise, still-luxuriös; wirkt wie gut gemachte Werkzeug-Software, nicht wie Werbung.
- Passt zu: Werkzeug-, Produktivitäts-, Verwaltungs- und Bibliotheks-Apps mit vielen Einträgen; Pro-Medienverwaltung, Dashboards, Entwickler-Tools.
- Passt weniger zu: verspielten Consumer-Apps, Kinder- und Lifestyle-Apps, hellen, emotional bildgetriebenen Marken.

## Aufbau und Raster
- Seitenaufbau: schmale Kopfleiste, darunter gestapelte Panels; auf der Website führen Produkt-Screenshots in Panels jeden Abschnitt an.
- Ausrichtung: konsequent linksbündig; Zahlen, Dauern und Daten rechtsbündig in einer Spalte.
- Raster: 4-px-Basis, Abstände 4/8/12/16/24/32/48 px, Abschnitte 96 px (Web); Karten 3-/2-/1-spaltig (ab 1024/768 px), Inhalt max. 1280 px.
- Dichte und Weißraum: „Die dunkle Fläche ist der Weißraum“ – getrennt wird durch Anheben auf Panels, nicht durch große Lücken. Panel-Innenabstand 24 px (Web), in der App 12–16 px; Listenzeilen 48–56 px.
- Rhythmus: Abschnitts-Label 13 px → Panel → 24 px → nächstes Label; gleichmäßig, ohne Wechsel zwischen Bühnen- und Listenmaß.

## Navigation
- Website: Kopfleiste 56 px auf Canvas, Wortmarke links, Links 14 px, rechts Sekundär- plus Primärbutton; unter 768 px Hamburger. Fußzeile als dichtes Link-Raster in 12 px, ink-subtle.
- App (Empfehlung): oben 52 px mit Arbeitsbereich-Schalter (22-px-Zeichen in Lavendel, Name 15 px 600, Chevron) bzw. kompaktem Titel 22 px, rechts 32-px-Icon-Buttons. Unten eine schwebende Leiste (12 px seitlich, 28 px über dem Rand; surface-1, 1 px Haarlinie, 12 px Radius, 58 px hoch) mit 4 Zielen Start · Bibliothek · Suche · Profil: Icon 18 px + Label 11 px 500, Profil als 18-px-Avatar. Aktiv = Feld eine Stufe höher (surface-2, 8 px Radius, stärkere Haarlinie), Text ink; inaktiv ink-subtle – nie Lavendel. Die Leiste bleibt beim Scrollen stehen; Inhalte laufen kurz davor per Maske aus (kein farbiger Verlauf).
- Detailseiten: Zurück-Chevron plus Pfad „Bibliothek › Alben › Lissabon“ (14 px, ink-subtle, aktuelles Glied ink), rechts Favorit und Mehr als Icon-Buttons; Leiste ausgeblendet.
- TV: linke Seitenleiste wie in der Produkt-App, Einträge mit Icon + Text; Fokus = 2-px-Ring in Lavendel bei 50 % plus Flächenstufe, keine Vergrößerung.

## Startscreen
- Kopf mit Arbeitsbereich-Schalter; Begrüßung 28 px 600 (−0,6 px), darunter eine Kennzahlen-Zeile mit Tabellenziffern.
- Hervorgehobener Inhalt als „Screenshot-Panel“: surface-1, 16 px Radius, 6 px Rand, Bild (2:1) darin mit 10 px Radius; darunter im Panel Status-Pill als Etikett, Titel 20 px 600, Angaben 12 px und rechts ein Sekundärbutton.
- Weitere Bereiche als Panels unter 13-px-Labels, 24 px Abstand: Zeilenliste „Fortsetzen“ mit Fortschrittsring und Mono-Token (62%, 2/24); „Quellen“ als dreiteilige Leiste, Zellen durch Haarlinien getrennt, je Name + Statusring; Speicher als 2-px-Balken mit Token im Abschnittskopf.
- Nichts Atmosphärisches: kein Verlauf, kein Glühen, kein Vollbild-Hero.

## Komponenten
- Buttons: 8 px Radius, 14 px 500, Padding 8 × 14 px, in der App 36–40 px hoch. Primär Lavendel (Hover heller, gedrückt Fokus-Ton), höchstens einer pro Screen; Sekundär surface-1 mit 1 px Haarlinie; Tertiär ohne Fläche; Invers weiß, selten. Nie Pill.
- Karten und Kacheln: surface-1 mit 1 px Haarlinie und 12 px Radius, Innenabstand 24 px (App 12–16 px); hervorgehoben bzw. Hover = surface-2 mit stärkerer Haarlinie. Medien-Panels 16 px Radius.
- Listen: Gruppen mit Kopfband über die volle Breite (surface-1, Haarlinie oben/unten, Icon 14 px + Name 13 px 500 + Anzahl in ink-tertiary); Zeilen 52 px mit Thumbnail 36 px (6 px Radius), Titel 14 px 500, Angaben 12 px ink-subtle, rechts Tabellenziffern; Trennlinie 1 px ab Textbeginn. Darüber eine Werkzeugzeile 28 px: Anzahl und Gruppierung links (12 px), Sortierung rechts als Text-Button mit Icon.
- Suche und Eingabefelder: surface-1, 8 px Radius, Padding 8 × 12 px, 1 px Haarlinie, ≥ 44 px Touch-Höhe (Feld 40 px + Rand); Fokus behält die Fläche und bekommt einen 2-px-Ring in Lavendel bei 50 %. Platzhalter ink-tertiary.
- Chips, Tabs, Filter: Pill-Umschalter – Standard Canvas + ink-subtle, gewählt surface-2 + ink (Flächenstufe statt Farbe), Padding 6 × 14 px. Status-Pill: surface-2, ink-muted, 12 px, 2 × 8 px. Kleine Chips 4 px, Tags 6 px Radius.
- Dialoge und Sheets: Menüs auf surface-3 mit 12 px Radius und stärkerer Haarlinie; Scrim reines Schwarz.
- Signatur-Komponenten: Screenshot-Panel mit Bild darin; gruppierte Liste mit Kopfbändern; Pill-Umschalter mit Flächenstufe; Status-Pill mit grünem Punkt nur für Erfolg. Empfehlung: Eigenschafts-Chips (Icon + Wert, 26 px, 6 px Radius) und 14-px-Fortschrittsringe statt farbiger Punkte.

## Icons
- Stil (Empfehlung, die Datei nennt keine Icons): feine, geometrische Linien-Icons mit runden Enden, einfarbig; inaktiv ink-subtle, aktiv ink; nie gefüllt, nie farbig. Status und Fortschritt als kleine Kreisformen (Ring, Ring mit Segment, gestrichelter Ring).
- Größe und Strich: 14 px in Bändern und Chips, 16 px in Listen und Buttons, 18 px in Leisten; sichtbarer Strich etwa 1,0–1,3 px (Lucide 1.75 auf 24er-Raster).
- Einsatz: fast immer mit Text; Icon-Buttons 32 × 32 px mit 8 px Radius, ohne Fläche oder als Sekundärbutton.
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Outlined, Gewicht 300, Füllung 0, 16–18 dp; iOS SF Symbols `.light`/`.regular`, ohne `.fill`; Web Lucide `stroke-width: 1.75`.

## Bildsprache
- Laut Datei: Produkt-Screenshots sind die Hauptdarsteller, gerahmt in surface-1-Panels mit 16 px Radius und 24 px Rand; Seitenverhältnis bleibt, nie beschnitten. Keine Stimmungsbilder, keine Verläufe.
- Übertragung: Die Inhalte der App sind der „Screenshot“ – Bild im Panel mit 6–8 px Rand und 10 px Radius, darauf 1 px helle Innenlinie (7 %). Thumbnails 36 px mit 6 px, Raster-Fotos mit 4 px Radius und 4 px Fuge. Kein Text auf Bildern, keine Verlauf-Overlays, keine Körnung, keine Filter. Avatare rund, 20–40 px.

## Typografie-Stimme
- Eine Stimme von Display bis Text, der Familienwechsel ist unhörbar. Display 600 (nie 700+), Text 400, Labels und Buttons 500.
- Laufweite: −3 px bei 80 px, −1,8 bei 56, −1 bei 40, −0,6 bei 28, −0,4 bei 22, Text 0 bis −0,1 px. Eyebrow 13 px 500 mit +0,4 px, keine Versalien.
- Größen: Display 80/56/40, Headline 28, Kartentitel 22, Text 16/14, Caption 12. App: Screen-Titel 28, kompakter Listen-Titel 22, Paneltitel 20, Liste 14, Labels 13, Angaben 12, Leisten-Labels 11.
- Mono 13 px nur für IDs, Status-Tokens und Zahlen wie Dauer, Prozent, Speicher – nie für Fließtext.
- Freier Ersatz: Inter (Text) und Inter Display (Titel) 400/500/600, Geist Sans möglich; Mono JetBrains Mono oder Geist Mono. Zahlen in Spalten mit Tabellenziffern.

## Form, Tiefe und Material
- Radien: 4 px Badges/Raster-Fotos, 6 px Tags/Thumbnails, 8 px Buttons/Felder, 12 px Karten/Leisten, 16 px Medien-Panels, 24 px selten; Pill nur für Umschalter und Status, rund für Avatare.
- Linien und Rahmen: 1 px Haarlinie (hairline) als Standard, stärkere Haarlinie für Hervorgehobenes und gewählte Felder, dritte Stufe für verschachtelte Flächen.
- Schatten und Ebenen: keine Schlagschatten. Tiefe = Flächenleiter canvas → surface-1 → surface-2 → surface-3 → surface-4, keine Stufe überspringen; ein Element innerhalb eines Panels liegt eine Stufe höher.
- Besondere Oberflächen: feiner weißer Lichtsaum an der Oberkante gehobener Panels (`inset 0 1px 0 rgba(255,255,255,.05)`); sonst keine Verläufe, kein Glas, keine Körnung.

## Bewegung
- Laut Datei: keine Angaben zu Animationen; dokumentiert sind Zustände: Hover Lavendel heller, gedrückt Fokus-Ton, Hover-Karten auf surface-2, Fokus-Ring 2 px bei 50 %.
- Empfehlung: Dauer klein 120 ms / Screenwechsel 200 ms, Easing `cubic-bezier(0.16, 1, 0.3, 1)`; Druck-Effekt: Fläche eine Stufe heller, kein Skalieren; Einblenden: Deckkraft + 4 px Anheben, Listen 30 ms gestaffelt; Screenwechsel: Überblenden + 8 px seitlich; Fokus (TV): Ring blendet in 120 ms ein.
- Compose: `tween(120, easing = CubicBezierEasing(0.16f, 1f, 0.3f, 1f))`, `AnimatedVisibility(fadeIn(tween(200)) + slideInVertically { it / 20 })`, `Modifier.animateItem()`; kein `spring` mit Überschwingen.

## Signatur-Elemente
1. Fast schwarze Fläche mit vierstufiger Flächenleiter und 1-px-Haarlinien statt Schatten, Lichtsaum an der Panel-Oberkante.
2. Lavendelblau als einziger Akzent – nur Zeichen, Hauptbutton, Fokus und Link-Betonung.
3. Inhalte als gerahmte „Screenshot-Panels“ (16 px Radius, Bild mit Rand im Panel).
4. Dichte, gruppierte Listen mit Kopfbändern, kleinen Linien-Icons, Tabellenziffern und Status-Pills.
5. Titel 600 mit deutlich negativer Laufweite gegen kleinen 12–14-px-Text.

## Übertragung auf eine App
- Startscreen: Arbeitsbereich-Schalter, Begrüßung mit Kennzahlen-Zeile, Rückblick im Screenshot-Panel, darunter Panels „Fortsetzen“ (Fortschrittsringe) und „Quellen“ (Statusringe: Haken, Segment, gestrichelt).
- Liste und Übersicht: Suchfeld, Pill-Umschalter plus Icon-Button „Anzeige“, Werkzeugzeile (Anzahl, Sortierung), Einträge nach Art gruppiert unter Kopfbändern; jede Zeile mit Thumbnail, Titel, Angaben und rechter Zahlenspalte.
- Detail: Pfad-Kopf mit Favorit/Mehr, Titel 28 px mit Eigenschafts-Chips, Bild im Screenshot-Panel, eine lavendelfarbene Hauptaktion plus gleich hoher Sekundärbutton, Pill-Umschalter mit Anzahlen, dichtes 4-spaltiges Fotoraster; zugehörige Musik in einer schwebenden Panel-Leiste (surface-2) unten.
- Formulare und Einstellungen: gruppierte Panels mit 48-px-Zeilen, Label links 14 px, Wert rechts ink-subtle, Trennlinien 1 px; Felder surface-1 mit Fokus-Ring.
- Leere Zustände und Laden: ein Linien-Icon 24 px, ein Satz in ink-subtle, ein Sekundärbutton; Laden als Platzhalterzeilen in surface-2 ohne Schimmer oder als 2-px-Balken. Keine Illustrationen.
- TV: Seitenleiste links, Inhalte als Panel-Raster mit 16 px Radius, Fokus = Ring + Flächenstufe.
- Musterscreens: Start mit Rückblick-Panel, Fortsetzen-Liste und Quellen-Leiste; Bibliothek als gruppierte Liste mit Kopfbändern; Album „Lissabon“ als Pfad-Detail mit Eigenschafts-Chips und dichtem Fotoraster.

## Vermeiden
- Lavendel als Flächen-, Karten- oder Abschnittsfarbe, für aktive Tabs oder Deko; eine zweite Akzentfarbe (Grün nur für Erfolg).
- Verläufe, Glühen, Spotlight-Karten, Schlagschatten; reines Schwarz als Hintergrund; ein helles Theme.
- Pill-förmige Buttons; Display-Gewicht über 600; Titel ohne negative Laufweite; Versal-Überschriften.
- Vollbild-Hero mit Text auf dem Bild; große, luftige Karten im Material-Stil; gefüllte oder bunte Icons; Ebenen überspringen (surface-1 direkt auf surface-4).
