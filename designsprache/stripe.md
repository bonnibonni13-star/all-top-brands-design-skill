---
slug: stripe
marke: Stripe
website: https://stripe.com
ansatz: daten
ansatz2: leuchten
modus: hell
aufbau: Weiße Fläche, pastellener Mesh-Verlauf im oberen Drittel, darunter Haarlinien-Tabellen
navigation: Weiße Leiste unten, 4 Ziele, aktiv = Icon gefüllt + Indigo; Detail über Indigo-Rücklink
komponenten: Indigo-Pill, Haarlinienkarte 12 px, Tabelle mit Versal-Kopf, Segment-Schalter, Creme-Band
icons: Linien-Icons 18–22 px in Tinte #0d253d, aktiv gefüllt in Indigo (Empfehlung)
bewegung: Kurz und sachlich: 150 ms Fläche, 250 ms Screen, cubic-bezier(.2,.6,.3,1) (Empfehlung)
schrift: Grotesk 300 für alles Große, negative Laufweite bis −1,4 px; Zahlen mit Tabellenziffern (tnum)
---
# Stripe – Designsprache

**Kurz:** Eine Zahlen-Designsprache in Hell: tiefes Navy als einzige Textfarbe, ein einziges Indigo für genau eine gefüllte Pill pro Fläche, dazu 1-px-Haarlinien statt Schatten. Alles Große steht im dünnen Gewicht 300 mit stark negativer Laufweite, alles Kleine ist Tabelle mit Tabellenziffern. Die einzige Atmosphäre ist der pastellene Mesh-Verlauf im oberen Drittel.

## Wirkung
- Charakter: nüchtern, präzise, vertrauenswürdig; redaktionell luftig oben, dicht und tabellarisch unten.
- Passt zu: Verwaltungs- und Konto-Apps, Dashboards, Bibliotheken mit vielen Zahlen, Abrechnung, Statistik, Pro-Werkzeugen.
- Passt weniger zu: bildlauten Feeds, verspielten Lifestyle-Apps, dunklen Medien-Regalen, Kinder-Apps.

## Aufbau und Raster
- Seitenaufbau: Mesh-Verlauf randlos im oberen Drittel, darin die dünne Display-Überschrift; darunter weiße Fläche mit Karten, dann ruhige Bänder in #f6f9fc und ein warmes Creme-Band als Zwischenspiel.
- Ausrichtung: Text linksbündig, Zahlen rechtsbündig in Tabellenziffern; Überschrift und Inhalt an derselben linken Kante (24 px mobil).
- Raster: 8-px-Basis mit 2/4/12-Feinstufen (2 · 4 · 8 · 12 · 16 · 24 · 32 · 64 px); Inhalt max. 1200 px, Abschnittsabstand 64–96 px Marketing, 32–48 px Produkt, Kartenpolster 32 px (Marketing) bzw. 24 px (Produkt-Mockup).
- Dichte und Weißraum: oben großzügig (Mesh 280–300 px hoch, 24–32 px unter der Überschrift), unten dicht (Tabellenzeilen 56–62 px, Stapel 4–8 px).
- Rhythmus: Verlauf → Weiß → Karte mit Haarlinie → Creme-Band → Tabelle. Genau ein gefüllter Indigo-Knopf je Band.

## Navigation
- Website: weiße Kopfleiste über dem Mesh, Wortmarke links, Links mittig in #61718a, rechts Anmelden plus eine gefüllte Indigo-Pill; mobil Hamburger, Display fällt 56 → 36 px.
- App (App-Muster der Marke, nicht in der Datei): untere Leiste 1 px #e3e8ee auf Weiß, 4 Ziele (Start · Bibliothek · Suche · Konto), Icon 22 px über Label 10 px. Inaktiv Linien-Icon in #64748d, aktiv dieselbe Form **gefüllt** in Indigo #533afd plus Label in 500 – nie nur Farbe. Leiste bleibt beim Scrollen stehen; Profil liegt zusätzlich als Avatar oben rechts.
- Detail: kein Leisten-Wechsel, sondern Indigo-Rücklink „‹ Bibliothek“ oben links (link-on-light), rechts drei runde Geister-Icon-Buttons 32 px mit Haarlinie.
- TV: linke Spalte mit Haarlinie, aktive Zeile als pastellene Indigo-Fläche (#b9b9f9) mit Tinten-Text; Fokus = 2-px-Indigo-Rahmen, kein Schatten.

## Startscreen
- Mesh-Verlauf (Creme → Sherbet-Orange → Lavendel → Indigo → Rubin) randlos über dem oberen Drittel, nach unten in Weiß ausblendend; Statusleiste und Avatar liegen darüber.
- Darin: Versal-Eyebrow 10 px, Display 36 px/300 mit −0,9 px Laufweite, darunter eine Zeile Kennzahlen in Tabellenziffern.
- Darunter die Kennzahlen-Karte (Produkt-Mockup-Prinzip): drei Zahlenspalten mit Haarlinien-Trennern und ein Speicherbalken; dann das Creme-Band für den Rückblick, dann die Tabelle „Zuletzt hinzugefügt“ mit Indigo-Link „Alle“.

## Komponenten
- Buttons: Pill 9999 px, Polster 8/16 px (mobil auf 12/20 px und ≥ 44 px Höhe wachsend), Label 16/400. Primär Indigo #533afd auf Weiß, Druck #2e2b8c; Sekundär weiß mit 1 px Indigo-Rand und Indigo-Text; auf dunklen Flächen Navy #1c1e54. Nie Rechteck-Buttons, nie zwei gefüllte Pills nebeneinander.
- Karten und Kacheln: weiß, Radius 12 px, 1 px #e3e8ee, Polster 24–32 px, höchstens Schatten `0 1px 3px rgba(0,55,112,.08)`; schwebende Panels `0 8px 24px rgba(0,55,112,.08), 0 2px 6px rgba(0,55,112,.04)`. Hervorgehobene Karte invertiert in Navy #1c1e54 statt bunt. Creme-Karte #f5e9d4 als warmes Zwischenspiel.
- Listen: als Tabelle, nicht als Kartenstapel. Kopfzeile 28 px auf #f6f9fc, Versal-Labels 10 px #64748d, 1 px Linien oben und unten; Zeilen 56–62 px mit 1-px-Trenner, Thumbnail 4:3 40×30 px mit Radius 4 px, Titel 15/300, Unterzeile 13 px #64748d, rechte Spalte rechtsbündig mit tnum.
- Suche und Eingabefelder: 40 px hoch, weiß, Radius 6 px, 1 px #a8c3de (kühler als die Kartenlinie), Text 15/300, Platzhalter #64748d; Fokus: Rand Indigo plus 3-px-Ring rgba(83,58,253,.12) (Empfehlung).
- Chips, Tabs, Filter: Segment-Schalter auf #f6f9fc, Radius 9999 px, Polster 3 px; aktives Segment weiß mit Haarlinie, Mini-Schatten und Tinte in 500. Tag-Pill „pill-tag-soft“: Fläche #b9b9f9, Text #4434d4, 10 px Versalien, 4/8 px.
- Dialoge und Sheets: weißes Blatt, Radius 16 px oben, Polster 24 px, Level-2-Schatten, Griff als 4-px-Linie in #e3e8ee; Aktion als Indigo-Pill unten rechts.
- Signatur-Komponenten: Mesh-Verlauf; Kennzahlen-Karte mit Haarlinien-Spalten und Speicherbalken; Haarlinien-Tabelle mit Versal-Kopf und tnum-Spalte; Creme-Band; pastellene Tag-Pill.

## Icons
- Stil (Empfehlung, die Datei nennt keine Icons): sachliche Linien-Icons mit leicht runden Enden auf 24er-Raster, einfarbig Tinte #0d253d oder #64748d. Aktiv: dieselbe Form gefüllt in Indigo. Keine Duotöne, keine bunten Icons, nie Icons im Fließtext.
- Größe und Strich: 22 px in der Leiste, 18–20 px in Buttons und Tabellen, 14 px in Pills; Strich 1,75 (Lucide `stroke-width: 1.75`).
- Einsatz: sparsam und fast immer mit Text; Zustände als 6-px-Punkte (Indigo = aktuell, #64748d = getrennt, Rubin = Fehler), nie allein.
- Umsetzung: Compose `Icons.Rounded` bzw. Material Symbols Rounded, Gewicht 400, Füllung 0 → 1 beim Aktivwerden; iOS SF Symbols `.regular` / `.fill`; Web Lucide 1,75 bzw. Phosphor `regular` / `fill`.

## Bildsprache
- Laut Datei: Produkt-Mockups statt Fotografie; Fotos erscheinen nur in Referenz-Karten, eingesetzt im Verhältnis 4:3 **ohne** Schatten. Mockup-Chrome in 12–16 px Radius mit Level-2-Schatten.
- Übertragung: Fotos als klare 4:3-Ausschnitte mit Radius 4 px (Tabelle, Raster) bzw. 12 px (Detail-Bild), 1 px #e3e8ee als Kante statt Schatten, keine Verlauf-Overlays, keine Filter, keine Textzeilen im Bild. Avatare rund 30–32 px. Der Mesh-Verlauf ist Dekoration, nie Füllung eines Fotorahmens.

## Typografie-Stimme
- Eine Grotesk in nur zwei Gewichten: 300 für alles ab 15 px aufwärts, 400 nur für Buttons, Versal-Labels und Tabellen-Hilfstext. 400+ bei Display nimmt der Marke die Luft.
- Laufweite negativ und größenabhängig: 56/−1,4 · 48/−0,96 · 36/−0,9 · 32/−0,64 · 26/−0,26 · 20/−0,2 · 15/0 px; Versal-Eyebrow 10 px mit +0,1 px.
- Zahlen: Tabellenziffern (`font-feature-settings: "tnum"`) plus −0,39 bis −0,42 px in jeder Zelle mit Mengen, Dauern, Speicher oder Datum. Stilsatz `ss01` global.
- Größen App: Display 36/37, Screen-Titel 32/35, Abschnitt 20/28, Zeile 15/21, Hilfstext 13/18, Versal-Label 10/12.
- Freier Ersatz: Inter (hier Inter Light 300 / Inter Display für Display), sonst Work Sans 300; keine Helvetica und keine System-Schrift – sie wirken zu schwer.

## Form, Tiefe und Material
- Radien: 4 px Tags und Thumbnails, 6 px Eingabefelder, 8 px kompakte Karten, 12 px Karten und Detail-Bild, 16 px Mockup-Chrome und Sheets, 9999 px alle Buttons und Pills.
- Linien und Rahmen: 1 px #e3e8ee überall (Karten, Tabellen, Leisten), 1 px #a8c3de nur an Eingabefeldern; Linien sind die Hauptstruktur.
- Schatten und Ebenen: nur zwei Stufen, beide blau getönt – L1 `0 1px 3px rgba(0,55,112,.08)`, L2 `0 8px 24px rgba(0,55,112,.08), 0 2px 6px rgba(0,55,112,.04)`. Tiefe entsteht sonst durch den Verlauf, nicht durch Schatten.
- Besondere Oberflächen: Mesh-Verlauf aus weichen, organischen Flecken (Creme #f5e9d4, Sherbet, Lavendel, Indigo #533afd, Rubin #ea2261, Magenta #f96bee), stark weichgezeichnet und nach unten ausblendend; Band #f6f9fc; Creme-Fläche #f5e9d4; kein Glas, keine Körnung.

## Bewegung
- Laut Datei: keine Angaben zu Animationen.
- Empfehlung: Dauer klein 150 ms / Screenwechsel 250 ms, Easing `cubic-bezier(.2,.6,.3,1)`; Druck: Pill geht auf #2e2b8c, Skalierung 0,98; Einblenden: Deckkraft + 10 px Anheben in 320 ms, Tabellenzeilen 40 ms gestaffelt; Screenwechsel: Überblenden mit 8 px Schub; Mesh driftet in 24 s langsam hin und her; Fokus (TV): Rahmen in 150 ms.
- Compose: `tween(150, easing = CubicBezierEasing(0.2f, 0.6f, 0.3f, 1f))`, `AnimatedVisibility(fadeIn(tween(320)) + slideInVertically { it / 10 })`, `animateItem()` für Tabellenzeilen, `rememberInfiniteTransition` für den Verlauf; kein Federn, kein Überschwingen.

## Signatur-Elemente
1. Pastellener Mesh-Verlauf im oberen Drittel, nach unten in Weiß auslaufend – die einzige Dekoration.
2. Display in Gewicht 300 mit stark negativer Laufweite über sehr kleinem 13-px-Hilfstext.
3. Genau eine gefüllte Indigo-Pill je Fläche, alles andere Haarlinie oder Text.
4. Haarlinien-Tabelle mit Versal-Kopf und rechtsbündiger Tabellenziffern-Spalte.
5. Creme-Band #f5e9d4 als warmes Zwischenspiel zwischen Weiß und Indigo.

## Übertragung auf eine App
- Startscreen: Mesh-Hero mit dünner Begrüßung und Kennzahlenzeile, darunter Kennzahlen-Karte mit Speicherbalken, Creme-Band für den Rückblick, Haarlinien-Tabelle „Zuletzt hinzugefügt“, dann Quellen mit Zustandspunkten.
- Liste und Übersicht: Titel 32/300, Suchfeld mit kühler Haarlinie, Segment-Schalter für die Filter, danach eine echte Tabelle mit Versal-Kopf, Typ-Tag-Pill in der Unterzeile und rechtsbündiger Zahl-/Datumsspalte.
- Detail: Indigo-Rücklink, 4:3-Bild mit Radius 12 ohne Schatten, Titel 32/300 mit tnum-Unterzeile, Indigo-Pill „Diashow starten“ neben Rand-Pill „Teilen“, Haarlinienzeile für die Musik, Segment-Schalter und dichtes Fotoraster mit 4-px-Radien.
- Formulare und Einstellungen: weiße Karten mit Versal-Label über 40-px-Feld, Hilfstext 13 px #64748d darunter, Fußzeile auf #f6f9fc mit Indigo-Pill rechts.
- Leere Zustände und Laden: Karte mit Haarlinie, Satz in 15/300, eine Indigo-Pill; Laden als Skelettzeilen in #f6f9fc mit gleichen Zeilenhöhen wie die Tabelle.
- TV: linke Haarlinien-Spalte, Inhalte als 4:3-Raster mit 12-px-Radius; Verlauf nur hinter der obersten Zeile.
- Musterscreens: Mesh-Start mit Kennzahlen-Karte und Creme-Rückblick, Bibliothek als Haarlinien-Tabelle mit Segment-Filter, Album-Detail mit 4:3-Bild, Indigo-Pill und Fotoraster.

## Vermeiden
- Display in 400+ oder ohne negative Laufweite; Versal-Überschriften; Indigo als Fließtextfarbe.
- Zahlen ohne Tabellenziffern; Mengen linksbündig in der Tabelle.
- Mehrere gefüllte Pills je Band, Rechteck-Buttons, Button-Polster unter 8/16 px.
- Neue Akzentfarben außerhalb der Verlaufsstopps; Rubin oder Magenta als Button-Farbe.
- Den Verlauf klein in eine Karte sperren, als Icon, Button-Füllung oder Foto-Overlay verwenden.
- Weiche Material-Schatten, graue statt blau getönte Schatten, Karten ohne Haarlinie.
- Abgrenzung zu Vercel: dort Schwarz-Weiß, Gewicht 600 und Mono-Labels; hier Navy-Indigo, Gewicht 300 und Tabellenziffern.
