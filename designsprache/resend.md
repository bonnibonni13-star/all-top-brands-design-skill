---
slug: resend
marke: Resend
website: https://resend.com
ansatz: editorial
ansatz2: minimal
modus: dunkel
aufbau: Reines Schwarz als Papier, darauf linksbündige Textblöcke; ein atmosphärisches Glühen je Screen, viel Luft
navigation: Leiste unten auf Schwarz, 1-px-Haarlinie oben, 4 Ziele; aktiv = 24-px-Weißstrich über dem Ziel
komponenten: Haarlinien-Karten 12 px, weiße Karten-Insel, Code-Fenster mit Ampelpunkten, Pill-Chips, Weißer Knopf
icons: Sehr feine Linien-Icons (Phosphor Thin), 18–20 px, einfarbig, nie gefüllt (Empfehlung)
bewegung: Ruhig: 140 ms / 240 ms, cubic-bezier(.2,.6,.2,1); Einblenden + 6 px Anheben, 40 ms gestaffelt (Empfehlung)
schrift: Editorial-Serife 44–56 px auf Zeilenhöhe 1,0 gegen 12–14 px Inter; Zahlen und Protokolle in Mono
---
# Resend – Designsprache

**Kurz:** Ein Entwicklerwerkzeug mit der Typografie eines Magazins: reines Schwarz (#000000) als Papier, darauf eine überdimensionierte Serifen-Überschrift als lautestes Element – nicht Farbe, nicht Knöpfe. Tiefe entsteht nur aus 1-px-Linien in durchscheinendem Weiß und tief gedeckten Flächenstufen; Farbe erscheint ausschließlich als schwaches Glühen im Hintergrund.

## Wirkung
- Charakter: still, literarisch, teuer; technisch im Detail (Mono-Protokolle, Code-Fenster), redaktionell in der Geste.
- Passt zu: Entwickler- und Infrastruktur-Apps, Lese- und Archiv-Apps, ruhigen Medien- und Portfolio-Apps, Statusansichten.
- Passt weniger zu: verspielten Consumer-Apps, farbgetriebenen Shops, dichten Daten-Dashboards mit vielen Flächenfarben.

## Aufbau und Raster
- Seitenaufbau: Kopfleiste 64 px auf Canvas mit einer Haarlinie unten, dann Bänder: Hero-Streifen → Abschnitt mit Glühen → Code-Fenster → helle Karten-Insel → Raster → schwarze Fußzeile.
- Ausrichtung: linksbündig, eine Spalte; nur Preis- und Feature-Raster sind mehrspaltig (3 / 2 / 1 Spalten ab 1024 / 768 px).
- Raster: Basis 4 px, Abstände 2/4/8/12/16/24/32/48 px, Bandabstand 96 px, Hero und Fußzeile 128 px; Inhalt max. 1200 px, helle Karten-Insel max. 640 px.
- Dichte und Weißraum: großzügig und redaktionell – die Überschrift braucht Platz, damit sie als Block wirkt. Karten-Innenabstand 32 px (Web), in der App 16–20 px; Screen-Seitenrand 24 px.
- Rhythmus: Überschriftenblock → kurze Unterzeile → ein einziges Objekt (Karte, Bild, Code-Fenster) → nächster Abschnitt. Nie zwei gleich laute Objekte nebeneinander.

## Navigation
- Website: Kopfleiste 64 px, Wortmarke links, Textlinks mittig (14 px, +0,35 px Laufweite), rechts ein Textlink plus der weiße Hauptknopf; unter 1024 px Hamburger. Unterseiten bekommen eine Zeile Pill-Chips über dem Inhalt. Fußzeile schwarz, mehrspaltiges Linkraster in 14 px, getrennt durch 4-%-Linien.
- App (Empfehlung, abgeleitet aus Kopfleiste und Pill-Chips): unten eine Leiste 76 px auf reinem Schwarz, abgesetzt durch eine einzige 1-px-Haarlinie (6 %); vier Ziele Start · Bibliothek · Suche · Profil, Icon 20 px darüber, Label 10 px, +0,35 px Laufweite. Aktiv = Text und Icon in Ink plus ein 24 px breiter, 1 px hoher Weißstrich direkt auf der Haarlinie über dem Ziel; inaktiv Mute. Profil als 22-px-Avatar, aktiv mit 1-px-Ring. Die Leiste steht fest; der Inhalt läuft darunter per schwarzer Maske aus. Oben je Screen nur eine 52-px-Zeile: neutrales Zeichen links, höchstens zwei Icon-Knöpfe rechts.
- Detailseiten: statt Leiste eine Rückzeile – feiner Chevron plus Herkunft in 13 px Mute, rechts zwei Icon-Knöpfe; unten eine eigene Aktionsleiste.
- TV: horizontale Textnavigation oben auf Schwarz, Fokus = Weißstrich unter dem Wort plus Ink-Text, keine Vergrößerung.

## Startscreen
- 52-px-Kopfzeile, dann ein Serifen-Block: Begrüßung in 46 px, Zeilenhöhe 1,0, −1,4 px Laufweite, zweizeilig; darunter eine Mute-Zeile 13 px mit den Kennzahlen.
- Hervorgehobener Inhalt als helle Karten-Insel: weiße Karte (12 px Radius) auf Schwarz, Bild oben randlos, darunter schwarzer Text – die einzige helle Fläche des Screens und damit der visuelle Anker.
- Danach ein Abschnittslabel (11 px, Mute, +0,6 px) mit Haarlinie, darunter eine angeschnittene Reihe gerahmter Bildkarten (4:5, 12 px Radius, 1-px-Haarlinie).
- Zahlen und Quellen gehören ins Code-Fenster: Flächenstufe surface-deep, Ampelpunkte, Mono-Zeilen mit Statuspunkt und ein 2-px-Balken für den Speicher.
- Ein einziges Glühen (z. B. Orange, 6–22 % Deckkraft) sitzt an der Oberkante und ist nach ~380 px verschwunden.

## Komponenten
- Buttons: 8 px Radius, 14 px/500, Padding 8 × 16 px, Höhe 36 px (App 40–44 px). Primär weiß (#fcfdff) mit schwarzem Text – höchstens eine solche helle Fläche je Screen, gedrückt #f1f7fe. Sekundär „Ghost“: #101012 plus 1-px-Linie (14 %). Tertiär: Canvas plus 1-px-Linie. Nie Pill, nie farbig.
- Karten und Kacheln: #0a0a0c, 12 px Radius, 1-px-Haarlinie (14 %), Innenabstand 32 px (App 16–20 px); ohne Schatten. Hervorgehoben = #101012, nur eine Luminanzstufe höher. Große Panels 16 px Radius.
- Listen: keine Flächen – Zeilen 72–76 px direkt auf Schwarz, getrennt durch 1-px-Haarlinien (6 %) über die volle Breite. Links ein 40 × 50-px-Bild (4:5, 8 px Radius, Haarlinie), Titel in der Serife 18 px, Angaben 12 px Mute, rechts ein Mono-Wert 12 px und ein 14-px-Chevron.
- Suche und Eingabefelder: #0a0a0c, 8 px Radius, 1-px-Linie (14 %), Padding 10 × 14 px, Höhe 40 px (App 44–48 px); Fokus verstärkt die Linie auf Ink, kein farbiger Ring. Platzhalter Mute.
- Chips, Tabs, Filter: Pill-Chips (voller Radius, 6 × 14 px, 14 px/500, +0,35 px) – inaktiv Canvas plus Haarlinie, aktiv weiße Fläche mit schwarzem Text. Alternativ Code-Tabs: Text plus 1-px-Unterstrich in 14 % Weiß beim aktiven Tab.
- Dialoge und Sheets: #0a0a0c mit 16 px Radius oben und 1-px-Haarlinie, Scrim reines Schwarz bei 70 %; kein Schatten.
- Signatur-Komponenten: Code-Fenster (surface-deep #06060a, drei Ampelpunkte Rot/Gelb/Grün, Tab-Streifen, Mono 13 px); helle Karten-Insel; Badge-Pill (#101012, 12 px, voller Radius); 8-px-Statuspunkt in Grün.

## Icons
- Stil (Empfehlung, die Datei nennt keine Icon-Familie): sehr feine, gleichmäßige Linien-Icons mit runden Enden – optisch die Fortsetzung der 1-px-Haarlinien. Einfarbig, nie gefüllt, nie zweifarbig, nie farbig (Ausnahme: die drei Ampelpunkte, die keine Icons sind).
- Größe und Strich: 14 px in Zeilen und Chips, 18 px in Knöpfen, 20 px in der Leiste; sichtbarer Strich ~1 px (Phosphor Thin auf 24er-Raster).
- Einsatz: sparsam. Icons ersetzen nie einen Titel; Icon-Knöpfe 36–40 px mit 8 px Radius auf Ghost-Fläche oder ganz ohne Fläche.
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Outlined, Gewicht 200, Füllung 0, 18–20 dp; iOS SF Symbols `.ultraLight`/`.thin`; Web Phosphor `thin` oder Lucide `stroke-width: 1.25`.

## Bildsprache
- Laut Datei: fast keine Fotografie. Visuelles Interesse kommt aus Typografie, Glühen, Code-Fenstern und der hellen Karten-Insel. Porträts rund, 32 px. Die hellen Mockup-Karten laufen im Hochformat 4:5 mit 12 px Radius.
- Übertragung: Bilder werden wie Drucktafeln gesetzt – gerahmt, nie randlos über den ganzen Screen. Hochformat 4:5 für Kacheln und Zeilenbilder, 16:10 für das Detailbild; 12 px Radius (Raster 8 px), immer 1-px-Haarlinie als Rahmen, nie Schatten. Leichte Dämpfung (`saturate(.92) brightness(.95)`) hält die Bilder im schwarzen Satzspiegel; kein Text im Bild, keine Verlaufsschleier, keine Körnung.
- Die einzige Ausnahme ist die helle Karten-Insel: Bild randlos oben in einer weißen Karte, darunter schwarzer Text.

## Typografie-Stimme
- Drei Spuren, strikt getrennt: Editorial-Serife nur für Displaygrößen und Listentitel, Grotesk (Inter) für alle UI-Labels, Mono für Code, Protokolle und Zahlen. Hierarchie entsteht durch Familienwechsel, nicht durch fettere Gewichte.
- Größenkontrast ist extrem: 46–56 px Serife gegen 12–14 px Grotesk, dazwischen fast nichts.
- Display: Gewicht 400, Zeilenhöhe 1,0 (nie lockerer), Laufweite −1 % (−0,96 px bei 96 px, −1,4 px bei 46 px). Text 400, Labels und Knöpfe 500; Pill- und Leistenlabels mit +0,35 px Laufweite. Keine Versalien, keine 600er-Betonung im Fließtext.
- Mono 12–13 px, Zeilenhöhe 1,6, ohne Ligaturen, kleingeschrieben für Schlüssel/Status.
- Freier Ersatz: Lora, Tiempos Headline oder Source Serif 4 für die Display-Serife (Zeilenhöhe hart auf 1,0 klemmen); Inter oder Geist für UI; Geist Mono oder JetBrains Mono für Code.

## Form, Tiefe und Material
- Radien: 0 px für Vollbänder, 4 px für Inline-Tags, 6 px für Code-Tabs, 8 px für Knöpfe, Felder und Rasterbilder, 12 px für Karten, Code-Fenster und Bildtafeln, 16 px für große Panels, voll für Pills, Punkte und Avatare.
- Linien und Rahmen: 1 px, immer durchscheinendes Weiß – 6 % als Trenner zwischen Zeilen, 14 % als Rahmen von Karten, Feldern und Code-Fenstern, 4 % in Fußzeilen. Linien ersetzen jede Schattenlogik.
- Schatten und Ebenen: keine Schlagschatten. Stufen: canvas #000000 → card #0a0a0c → elevated #101012; Code-Fenster geht nach unten weg auf #06060a (kühler und dunkler als die Fläche).
- Besondere Oberflächen: atmosphärisches Glühen – ein einzelner radialer Verlauf in Orange, Blau, Grün, Gelb oder Rot bei 6–22 % an der Oberkante eines Abschnitts, nach ~380 px auf Schwarz ausgelaufen. Nie zwei Glühen in einem Abschnitt, nie Akzentfarbe als Fläche oder Knopf.

## Bewegung
- Laut Datei: keine Angaben zu Animationen; dokumentiert sind Zustände (Primärknopf gedrückt auf #f1f7fe, Feldfokus verstärkt die Linie auf Ink).
- Empfehlung: Dauer klein 140 ms / Screenwechsel 240 ms, Easing `cubic-bezier(0.2, 0.6, 0.2, 1)`; Druck-Effekt: Fläche eine Luminanzstufe heller und Linie von 6 % auf 14 %, kein Skalieren; Einblenden: Deckkraft plus 6 px Anheben, Listen und Karten 40 ms gestaffelt; Glühen blendet über 600 ms ein; Screenwechsel als reines Überblenden ohne Seitwärtsbewegung; Fokus (TV): Weißstrich wächst in 140 ms von der Mitte.
- Compose: `tween(140, easing = CubicBezierEasing(0.2f, 0.6f, 0.2f, 1f))`, `AnimatedVisibility(fadeIn(tween(240)) + slideInVertically { it / 24 })`, `Modifier.animateItem()`; kein `spring` mit Überschwingen.

## Signatur-Elemente
1. Reines Schwarz (#000000, nie #0a0a0a) mit einer einzigen überdimensionierten Serifen-Überschrift auf Zeilenhöhe 1,0.
2. Weiß als Akzent: genau eine helle Fläche je Screen – weißer Knopf, weißer Chip oder helle Karten-Insel.
3. 1-px-Haarlinien in durchscheinendem Weiß statt jeder Form von Schatten.
4. Ein schwaches, farbiges Glühen an der Oberkante – Farbe erscheint nur als Atmosphäre.
5. Code-Fenster mit Ampelpunkten und Mono-Zeilen als Ort für Zahlen, Status und Technik.

## Übertragung auf eine App
- Startscreen: Serifen-Begrüßung über Mute-Kennzahlen, Rückblick als helle Karten-Insel, eine angeschnittene Reihe gerahmter Bildkarten, Quellen und Speicher im Code-Fenster mit Mono-Zeilen und Statuspunkten.
- Liste und Übersicht: Serifen-Screentitel, Suchfeld, Pill-Chips mit genau einem weißen (aktiven) Chip, danach flächenlose Zeilen auf Schwarz – 4:5-Bild, Serifentitel, Mute-Angaben, Mono-Wert rechts, getrennt durch Haarlinien.
- Detail: Rückzeile statt Leiste, Serifentitel 52 px, Mute-Metazeile über einer Haarlinie, Bild als gerahmte Tafel (16:10), weißer Hauptknopf neben Ghost-Icon-Knöpfen, Code-Tabs mit Unterstrich, Fotoraster im Hochformat, unten eine Aktionsleiste für die Musik.
- Formulare und Einstellungen: Zeilen 52 px auf Schwarz, Label links in Inter 14 px, Wert rechts Mute oder Mono, Haarlinie dazwischen; Abschnittsüberschriften in 11 px Mute mit Laufweite; Felder #0a0a0c mit 14-%-Linie.
- Leere Zustände und Laden: ein dünnes 24-px-Icon, ein Satz Mute, ein Ghost-Knopf; Laden als Mono-Zeilen im Code-Fenster oder als Platzhalterzeilen in #0a0a0c – kein Schimmer, keine Illustration.
- TV: Textnavigation oben, Inhalte als gerahmte Tafeln im 3er-Raster, Fokus = Weißstrich plus Ink-Titel.
- Musterscreens: Start mit Serifen-Begrüßung, weißer Rückblick-Insel und Quellen-Code-Fenster; Bibliothek als haarlinien-getrennte Liste mit 4:5-Bildern und Mono-Werten; Detail „Lissabon“ mit 52-px-Serifentitel, gerahmter Bildtafel und weißem Hauptknopf.

## Vermeiden
- Fast-Schwarz (#0a0a0a) als Fläche; ein helles Theme; Akzentfarben als Knopf, Chip oder Kartenfläche.
- Mehr als eine helle Fläche je Screen; farbige Hauptaktion; Pill-förmige Knöpfe.
- Schlagschatten, Glas, Körnung, Verlaufsbänder über ganze Flächen, zwei Glühen in einem Abschnitt.
- Display-Zeilenhöhe über 1,0, Serife ohne negative Laufweite, Betonung durch Gewicht 600 statt durch Familienwechsel.
- Code, Status oder Zahlen in der Grotesk setzen; Fließtext in Mono; randlose Vollbild-Fotos mit Text darauf.
- Unterschied zu anderen minimalen Entwicklermarken (z. B. OpenCode): Resend ist schwarzes Papier mit redaktioneller Serife und Atmosphäre – nicht helles Terminal-Raster aus durchgehender Monoschrift.
