---
slug: supabase
marke: Supabase
website: https://supabase.com
ansatz: werkzeug
ansatz2: minimal
modus: hell
aufbau: Weiße Fläche, Inhalte in Haarlinien-Karten, Datentabellen und dunklen Code-Panes; dicht, linksbündig, ohne Deko
navigation: Empfehlung: Icon-Leiste unten (4 Ziele, nur Icons), aktiv = graue 6-px-Kachel; oben Pfad mit Schrägstrichen
komponenten: Smaragd-Button mit dunkler Schrift (6 px), Tabelle mit Gitterlinien, dunkle Featured-/Code-Pane, Kennzahl-Karten
icons: Empfehlung: feine Linien-Icons (Lucide 1.5), 16–20 px, grau, aktiv fast schwarz; nie gefüllt, nie grün
bewegung: Empfehlung: nüchtern 120–220 ms, cubic-bezier(.2,0,0,1); Einblenden + 4 px; Grün wird beim Drücken #24b47e
schrift: Inter 500 für Titel, eng (−0,42 px bei 28 px); Text 13–14 px 400; Mono nur in dunklen Panes und Zahlenspalten
---
# Supabase – Designsprache

**Kurz:** Ingenieurs-Klarheit auf reinem Weiß: Eine Grauleiter von #ededed bis #171717 und 1-px-Haarlinien tragen fast alles, Grün ist das einzige Farbereignis – ein gefüllter Smaragd-Button mit fast schwarzer Schrift pro Screen. Das Produkt selbst ist die Dekoration: Tabellen, Kennzahl-Karten und dunkle Code-Panes in Mono statt Fotos, Verläufe oder Illustrationen.

## Wirkung
- Charakter: still-technisch, präzise, ehrlich; wirkt wie ein gut gebautes Entwickler-Dashboard, nicht wie Werbung.
- Passt zu: Verwaltungs-, Daten-, Admin- und Werkzeug-Apps, Medienbibliotheken für Power-User, Sync- und Speicher-Apps.
- Passt weniger zu: emotionalen Consumer-Apps, Mode, Kinder-Apps, bildgetriebenen Stimmungsmarken.
- Abgrenzung zu MongoDB (gleiche Branche, auch Grün): Supabase bleibt durchgehend weiß mit neutralem Grau, eckigen 6-px-Buttons und nur einem Grün pro Screen; Dunkel nur als eingesetzte Pane. MongoDB rahmt mit vollflächigen Petrol-Bändern, Pill-Buttons, geometrischer Schrift und farbigen Kategorie-Tags.

## Aufbau und Raster
- Seitenaufbau: schmale Kopfzeile mit Haarlinie, Seitentitel, darunter gestapelte Karten bzw. eine randlose Tabelle; jeder Abschnitt hat höchstens eine dunkle Pane.
- Ausrichtung: linksbündig; Zahlen rechtsbündig in Mono-Spalten.
- Raster: 8-px-Basis mit 2/4/12 für Feinarbeit; Tokens 2·4·8·12·16·24·32·64 px; Web-Container ~1280 px, Karten 4-/2-/1-spaltig (1024/768 px).
- Dichte und Weißraum: Web-Abschnitte 64–96 px Luft, Karten innen 32 px. App (Empfehlung): Rand 16 px, Kartenabstand 8 px, Abschnitte 24 px, Zeilen 44–48 px – dicht, aber nie gedrängt.
- Rhythmus: Abschnittstitel 18 px → 10 px → Karte/Tabelle → 24 px; die weiße Fläche ist das Design, keine Bänder oder Hintergründe.

## Navigation
- Website: weiße Kopfleiste (16 × 24 px Padding), Logo links, Links mittig, rechts Text-Link „Anmelden“ plus grüner Button; mobil Hamburger.
- App: App-Muster der Marke (nicht in der Datei) ist die schmale Icon-Leiste des Dashboards. Übertragen als Leiste unten: weiß, 1 px Haarlinie oben, 4 Ziele (Start, Bibliothek, Suche, Profil als 24-px-Avatar), nur Icons 20 px. Aktiv = Kachel 44 × 36 px in #ededed mit 6 px Radius, Icon #171717; inaktiv #707070. Bleibt beim Scrollen stehen.
- Kopfzeile: Pfad mit Schrägstrichen „Lenas Medien / Bibliothek“ (14 px 500, Schrägstrich #d4d4d4), Umschalt-Chevron; rechts 32-px-Icon-Buttons mit Haarlinie und 6 px Radius. Detail: Zurück-Button + Pfad, Leiste unten ausgeblendet.
- TV: linke Icon-Leiste, aufklappbar mit Beschriftung; Fokus = Kachel #ededed + 2 px Ring #171717.

## Startscreen
- Pfad-Kopf, Begrüßung 28 px 500 (−0,42 px), sonst kein Hero.
- Hervorgehoben als dunkle Featured-Pane (wie die dunkle Preisstufe): #1c1c1c, 12 px Radius, Kopfzeile mit Haarlinie, Bild eingesetzt (8 px Radius), Titel weiß, Angaben in Mono, der einzige Smaragd-Button.
- Darunter Kennzahl-Karten (Fotos, Videos, Titel) mit Mini-Balken und eine Quellen-Karte mit Speicherbalken und Statuspunkten.

## Komponenten
- Buttons: 6 px Radius, 14 px 500, Padding 8 × 16 px, App 36–40 px hoch. Primär #3ecf8e mit Schrift #171717 (nie weiß), gedrückt #24b47e – höchstens einer pro Screen. Sekundär weiß mit 1 px #c7c7c7; auf Dunkel #1c1c1c mit heller Haarlinie; Link-Button ohne Fläche, Unterstrich beim Hover.
- Karten und Kacheln: weiß, 1 px #dfdfdf, 12 px Radius (kompakt 8 px), Innenabstand 32 px Web / 12–16 px App; Featured-Karte invertiert #1c1c1c mit weißer Schrift.
- Listen: Datentabelle mit Gitterlinien #ededed, Kopfzeile #fafafa 12 px 500 grau, Zeilen 48 px, Auswahlkästchen 14 px (4 px Radius), Zahlen in Mono rechtsbündig; Tabellenfuß mit Anzahl und Blättern.
- Suche und Eingabefelder: weiß, 1 px #dfdfdf, 6 px Radius, Padding 8 × 12 px, mind. 36 px hoch; Fokus 1 px #c7c7c7 plus 2-px-Ring in Smaragd hell (Empfehlung).
- Chips, Tabs, Filter: Segment-Leiste (Empfehlung) auf #fafafa mit Haarlinie, gewählt = weißes Feld mit #c7c7c7-Rand und Schatten 1; Unterstrich-Tabs mit 2 px #171717; Pill-Tags 12 px (#fafafa bzw. Grün für „Neu“).
- Dialoge und Sheets: weiß, 16 px Radius, Schatten 3 (0 16px 48px rgba(0,0,0,.12)).
- Signatur-Komponenten: Produkt-Mockups als gestapelte Panes mit Schatten 2; Code-Block #1c1c1c in Mono mit 6 px Radius; Kennzahl-Karte mit Smaragd-Balken.

## Icons
- Stil (Empfehlung, die Datei nennt keine Icons): feine, geometrische Linien mit runden Enden, einfarbig, nie gefüllt, nie grün.
- Größe und Strich: 14–16 px in Karten und Zeilen, 20 px in der Leiste; Strich 1,5 px auf 24er-Raster.
- Einsatz: meist mit Text; Icon-Buttons 32 × 32 px (Detail 40 px) mit Haarlinie und 6 px Radius; Status als 8-px-Punkte, nicht als Icons.
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Outlined, Gewicht 300, Füllung 0; iOS SF Symbols `.light`; Web Lucide `stroke-width: 1.5`.

## Bildsprache
- Laut Datei: kaum Fotografie, nie Illustrationen; Fotos (selten) 4:3 in 12-px-Containern, Logos einheitlich grau.
- Übertragung: Medien sind Inhalt, nicht Stimmung – Bilder immer in Karten oder Panes eingesetzt (8 px Radius in der Pane, Thumbnails 28 px mit 4 px), nie randlos, kein Text auf Bildern, keine Verläufe oder Filter. Raster mit 6 px Fuge und 6 px Radius.

## Typografie-Stimme
- Mittleres Gewicht als Ingenieurs-Ton: Display immer 500 (nie 600+), Text 400, Buttons und Labels 500.
- Laufweite negativ nur im Display: −1,92 px bei 64, −1,44 bei 48, −0,72 bei 36, −0,42 bei 28; ab 22 px 0.
- Größen: 64/48/36/28 Display, 22/18 Überschriften, 16 Text, 14 Buttons, 13 Caption, 12 Micro. App: Titel 28–36, Abschnitte 18, Zeilen 14, Angaben 12–13.
- Mono (System-Mono) 12–14 px für Code, Panes, Zahlenspalten; nie für Fließtext.
- Freier Ersatz: Inter 500 (laut Datei nächstes Pendant), Geist Sans; Mono Liberation Mono, JetBrains Mono. Keine Helvetica.

## Form, Tiefe und Material
- Radien: 4 px Felder/Tags klein, 6 px Buttons und Code, 8 px kompakte Karten, 12 px Karten/Mockups, 16 px Dialoge, Pill nur für Tags und Avatare.
- Linien und Rahmen: 1 px #dfdfdf Standard, #c7c7c7 betont, #ededed/#efefef/#d4d4d4 als Feinleiter für Gitter und Trenner.
- Schatten und Ebenen: 0 flach + Haarlinie; 1 `0 1px 3px rgba(0,0,0,.06)`; 2 `0 8px 24px rgba(0,0,0,.08)` für schwebende Mockups; 3 `0 16px 48px rgba(0,0,0,.12)` für Dialoge.
- Besondere Oberflächen: dunkle Panes #1c1c1c/#202020 als einzige Kontrastfläche; keine Verläufe, kein Glas, keine Körnung.

## Bewegung
- Laut Datei: keine Animationen; dokumentiert ist nur der Druckzustand Grün → #24b47e und Unterstrich beim Link-Hover.
- Empfehlung: Dauer klein 120 ms / Screenwechsel 220 ms, Easing `cubic-bezier(0.2, 0, 0, 1)`; Druck-Effekt: Farbwechsel ohne Skalieren; Einblenden: Deckkraft + 4 px, Karten 40 ms gestaffelt; Screenwechsel: Überblenden + 8 px seitlich; Fokus (TV): Kachel und Ring in 120 ms.
- Compose: `tween(120, easing = CubicBezierEasing(0.2f, 0f, 0f, 1f))`, `AnimatedVisibility(fadeIn(tween(220)) + slideInVertically { it / 24 })`, `Modifier.animateItem()`; kein Federn.

## Signatur-Elemente
1. Ein Smaragd-Button #3ecf8e mit fast schwarzer Schrift und 6 px Radius – sonst keine Farbe.
2. Reines Weiß mit Grauleiter und 1-px-Haarlinien, Datentabelle mit Gitterlinien.
3. Dunkle Panes #1c1c1c (Featured, Code, Listen in Mono) als einziger Kontrast.
4. Inter 500 mit enger Laufweite gegen kleinen 12–14-px-Text.
5. Kennzahl-Karten mit Mini-Balken wie im Dashboard.

## Übertragung auf eine App
- Startscreen: Pfad-Kopf, Begrüßung, dunkle Featured-Pane „Rückblick“ mit dem Grün-Button, Kennzahl-Karten, Quellen-Karte mit Speicherbalken und Status.
- Liste und Übersicht: Titel mit Anzahl, Suchfeld, Segment-Leiste, Werkzeugzeile (Filter, Sortierung, grüner „Hinzufügen“-Button), randlose Datentabelle mit Gitter und Mono-Zahlen, Tabellenfuß.
- Detail: Pfad mit Zurück-Button, Titel 36 px, Tag und Mono-Angaben, Bild in Haarlinien-Karte, Hauptaktion grün plus Icon-Buttons, Musik als dunkle Code-Pane mit Titelnummern als Zeilennummern, Unterstrich-Tabs, Raster.
- Formulare und Einstellungen: Karten mit 44-px-Zeilen, Label links, Feld rechts oder darunter; Code-Werte (Pfade, Schlüssel) in Mono-Pane mit Kopieren.
- Leere Zustände und Laden: graue Haarlinien-Karte, ein Satz in #707070, sekundärer Button; Laden als graue Platzhalterbalken #ededed, keine Illustration.
- TV: Icon-Leiste links, Tabellen und Karten größer (Zeilen 64 px), Fokus mit Ring.
- Musterscreens: Start mit dunkler Rückblick-Pane und Kennzahlen, Bibliothek als Datentabelle, Album „Lissabon“ mit Code-Pane für die Diashow-Musik.

## Vermeiden
- Mehr als einen grünen Button pro Screen, weiße Schrift auf Grün, Grün als Fläche oder Icon-Farbe.
- Lila, Gelb, Pink als Systemfarben (nur in Diagrammen); Verläufe oder Stimmungs-Hintergründe.
- Pill-Buttons, Display-Gewicht über 500, Helvetica-Optik.
- Randlose Vollbild-Fotos, Text auf Bildern, große bunte Karten, Material-Schatten auf jeder Karte.
