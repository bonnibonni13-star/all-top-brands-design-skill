---
slug: bugatti
marke: Bugatti
website: https://www.bugatti.com
ansatz: buehne
ansatz2: editorial
modus: dunkel
aufbau: Schwarze Fläche, randlose Kinoformat-Fotos, darunter viel Leere und ein gesperrter Versaltitel
navigation: Transparente 56-px-Kopfzeile (Menü · Wortmarke · Aktion); unten vier Mono-Versallabels mit weißem Strich
komponenten: Foto-Band, Spezifikationszellen mit Haarlinien, Listenzeile mit Pfeil, transparente Umriss-Pille
icons: Dünne Linien, eckige Enden, keine Füllung, 16–20 px, sehr selten eingesetzt
bewegung: Langsam und gleitend; 400–700 ms, ease-out; Bild zoomt kaum merklich, Text blendet gestaffelt auf
schrift: Dreiklang: schmale Versal-Display mit 2–6 px Sperrung, Serifen-Fließtext, Mono für Labels
---
# Bugatti – Designsprache

**Kurz:** Reines Schwarz, weiße Versalschrift mit weiter Sperrung und randlose Fotografie – mehr gibt es nicht. Keine Akzentfarbe, kein Schatten, kein Verlauf, keine abgerundete Karte. Die Hierarchie entsteht aus Größe, Laufweite, Groß-/Kleinschreibung und dem Wechsel zwischen drei Schriftfamilien, nie aus Fettung oder Farbe.

## Wirkung
- Charakter: streng, teuer, zurückhaltend; technische Präzision statt Wärme. Leere ist Inhalt.
- Passt zu: Portfolio- und Galerie-Apps, Fahrzeug- und Produktbühnen, Reiseberichten, Premium-Katalogen.
- Passt weniger zu: verspielten Alltagsapps, datendichten Werkzeugen, allem mit vielen gleichzeitigen Aktionen.

## Aufbau und Raster
- Seitenaufbau: Bänder im Wechsel – randloses Foto im Kinoformat, darunter ein Textblock aus Mono-Überzeile, Versaltitel und höchstens einer Aktion. Danach wieder Leere.
- Ausrichtung: linksbündig in Listen und Tabellen, mittig in Bühnenbändern. Kein zentriertes Durcheinander.
- Raster: Inhalt max. ~1280 px, Fotobänder vollbreit ohne Maximum; Newsroom 2-spaltig, Stellenliste einspaltig; Rinnen 40 px (App: 16 px).
- Dichte und Weißraum: sehr niedrig. Grundeinheit 4 px; Marken 4/8/12/16/24/40/64 px, zwischen großen Bändern 120 px (App: 28–40 px). Karteninnenabstand 16–24 px, im Fotoband 64 px.
- Rhythmus: Foto → Luft → Titel → Luft → eine Pille. Nie zwei Aktionen nebeneinander um Aufmerksamkeit kämpfen lassen.

## Navigation
- Website: `top-nav` 56 px, vollständig transparent über dem Foto, ohne Rahmen – links „MENU“, mittig die Wortmarke (14 px, 6 px Sperrung), rechts „STORE“. Alles Mono-Versalien, 12 px, 2 px Sperrung.
- App: dieselbe Kopfzeile, nur auf Schwarz gesetzt, damit die Beschriftung über hellen Fotos lesbar bleibt (Empfehlung). Unten vier Ziele als reine Mono-Versallabels 10 px/2 px Sperrung ohne Icons, getrennt durch eine 1-px-Haarlinie #262626 nach oben; aktiv = weiß plus 1-px-Strich über dem Label, inaktiv #999999. Detailseiten tauschen die Leiste gegen eine Aktionszeile. Empfehlung, die Datei kennt keine App-Leiste.
- TV: horizontale Mono-Reiter oben, Inhalt als Vollbild-Foto; Fokus durch weißen 1-px-Rahmen und leichtes Aufhellen, nie durch Farbe.

## Startscreen
- Kein Begrüßungstext. Oben ein randloses Foto im Verhältnis ~2:1, darunter auf Schwarz: Mono-Überzeile („RÜCKBLICK · VOR EINEM JAHR“), Versaltitel 34–40 px mit 3 px Sperrung, eine transparente Pille.
- Darunter ein Band aus Spezifikationszellen: Werte 20 px Display, Labels 10 px Mono, getrennt durch senkrechte Haarlinien, oben und unten je eine waagerechte Haarlinie.
- Zum Schluss eine angeschnittene Querreihe aus Fotokarten (Foto ohne Radius, darunter der Name in Versalien). Mehr Bereiche verträgt der Screen nicht.

## Komponenten
- Buttons: `button-primary` – transparent, 1 px weißer Rand, volle Pille, 14/32 px, Höhe 44 px, Label Mono-Versalien 14 px mit 2,5 px Sperrung. Niemals gefüllt. `button-icon`: 40 px Kreis, transparent, 1 px weiß.
- Karten und Kacheln: kein Kartengefühl. `model-photo-card` ist nur Foto auf Schwarz plus Name (32 px Display) und Mono-Zeile. Echte Flächen gibt es nur als #141414 (`surface-card`) oder #1f1f1f, ohne Schatten, Radius 0.
- Listen: `career-listing-row` – transparente Zeile, 24 px Innenabstand (App 16 px), Haarlinie #262626 dazwischen, Titel links in Display-Versalien 18–20 px, Zusatz rechts in Mono 10–11 px, ganz rechts ein dünner Pfeil.
- Suche und Eingabefelder: `text-input` – transparent, kein Rahmen, nur eine 1-px-Unterkante #3a3a3a, Höhe 44 px, Text im Serifen-Fließtext 16 px, Platzhalter #999999. Fokus macht die Unterkante weiß.
- Chips, Tabs, Filter: keine Chips. Filter sind Mono-Versallabels nebeneinander; aktiv = weiß mit 1-px-Unterstrich, inaktiv #999999.
- Dialoge und Sheets: Fläche #141414, Radius 0, 1-px-Haarlinie oben, Aktionen als Umriss-Pillen.
- Signatur-Komponenten: `spec-cell` (Wert über Label, Haarlinien als einziges Gitter), `caption-overlay` (Mono-Versalien 11 px über oder unter dem Foto), `hero-photo-band`.

## Icons
- Stil: sehr dünne Linien, eckige Enden und Ecken, keine Füllung, keine Rundungen. Icons sind Werkzeug, nicht Schmuck. Empfehlung – die Datei nennt nur Tasche, Pfeil und Karussellpfeile.
- Größe und Strich: 16–20 px bei ~1,25/24 px Strichstärke; im 40-px-Kreisknopf 18 px.
- Einsatz: maximal drei Icons pro Screen. Beschriftungen ersetzen Icons, wo immer es geht; Pfeil nach rechts als Fortsetzungszeichen in Listenzeilen.
- Umsetzung: Compose `Icons.Sharp` bzw. Material Symbols Sharp, Gewicht 200, Füllung 0; iOS SF Symbols Ultralight/Thin; Web Lucide mit `stroke-width: 1.25` und `stroke-linecap: square; stroke-linejoin: miter`.

## Bildsprache
- Fotografie ist die einzige Spannung und die einzige Farbe im System. Randlos, Radius 0, Kinoformat 2:1 bis 21:9; im Raster quadratisch bis 5:4.
- Kein Verlauf, keine Tönung, kein Filter über dem Bild. Text liegt deshalb bevorzugt unter dem Foto auf Schwarz, nicht darauf; nur über dunklen Motiven darf eine Mono-Bildunterschrift im Bild stehen.
- Fugen im Raster 1–2 px, sodass das Schwarz als Linie durchscheint. Keine Rahmen um Bilder.
- Motive zeigen Bewegung oder Dreiviertelansicht, nie flache Frontalansichten.

## Typografie-Stimme
- Dreiklang, strikt getrennt: Display (schmale Grotesk, Versalien, 2–6 px Sperrung) für alle Titel und die Wortmarke; Serifenschrift für Fließtext in gemischter Schreibung ohne Sperrung; Mono-Versalien für Knöpfe, Navigation, Labels und Datumsangaben mit 2–2,5 px Sperrung.
- Größen: 64 / 48 / 32 / 24 / 20 / 16 / 14 / 11 px. Zeilenhöhe 1.1–1.3 bei Titeln, 1.5 im Fließtext. Alles bleibt Gewicht 400 – es gibt keine Fettung.
- Hierarchie entsteht aus Größe, Sperrung, Schreibweise und Familienwechsel. Engere Laufweite bei Titeln ist ein Markenbruch.
- Freier Ersatz: Saira Condensed (Display), EB Garamond oder Cormorant Garamond (Fließtext), JetBrains Mono oder IBM Plex Mono (Mono).

## Form, Tiefe und Material
- Radien: 0 px für alles – Karten, Fotos, Felder, Zellen. Pille 9999 px nur für Knöpfe, Kreis nur für Icon-Knöpfe. Nichts dazwischen.
- Linien und Rahmen: 1 px #262626 als Trenner und Kartenkontur, 1 px #3a3a3a unter Eingabefeldern, 1 px Weiß als Knopfrand. Die Haarlinie ist das einzige Gitter.
- Schatten und Ebenen: keine. Tiefe kommt aus dem Foto. Flächen stufen sich nur in kaum merklichen Schwarztönen: #000000 → #0d0d0d → #141414 → #1f1f1f.
- Besondere Oberflächen: keine. Kein Glas, keine Körnung, kein Muster, kein Emblem.

## Bewegung
- Laut Datei: keine Angaben (Animationen stehen ausdrücklich nicht im Umfang).
- Empfehlung: klein 400 ms / Screenwechsel 700 ms, Easing `cubic-bezier(0.16, 1, 0.3, 1)`; Druck-Effekt nur Deckkraft 0.6 statt Skalierung; Einblenden von Titeln als reines Fade über 600 ms mit 120 ms Staffel; Fotos erscheinen mit 1.03 → 1 Zoom; Screenwechsel als langsame Überblendung, nie als Sprung; Fokus (TV) weißer 1-px-Rahmen in 200 ms.
- Compose: `tween(600, easing = CubicBezierEasing(0.16f, 1f, 0.3f, 1f))`, `AnimatedVisibility(fadeIn(tween(600)))`, Bildzoom über `graphicsLayer`-Skalierung, Shared-Element für Foto → Detail mit 700 ms.

## Signatur-Elemente
1. Reines Schwarz ohne jede Akzentfarbe – Farbe gibt es nur im Foto.
2. Versaltitel in schmaler Grotesk mit 2–4 px Sperrung, immer Gewicht 400.
3. Die transparente Pille mit 1-px-weißem Rand als einzige Schaltfläche.
4. Spezifikationszellen und Listenzeilen, die nur von 1-px-Haarlinien gegliedert werden.
5. Der Familienwechsel Display / Serif / Mono innerhalb eines Blocks.

## Übertragung auf eine App
- Startscreen: Foto-Band oben, darunter Mono-Überzeile, Versaltitel und eine Umriss-Pille; dann ein Haarlinien-Band mit drei Kennzahlen; zuletzt eine angeschnittene Querreihe aus Fotokarten.
- Liste und Übersicht: großer Versaltitel, Suchfeld nur mit Unterkante, Filter als Mono-Labels mit Unterstrich, danach haarliniengetrennte Zeilen mit kleinem 16:9-Vorschaubild, Versaltitel, Mono-Zusatz und Pfeil.
- Detail: randloses Foto im 2:1-Format, darunter Mono-Überzeile, Versaltitel, ein Satz Serifen-Fließtext, Haarlinien-Zellen mit den Zahlen, dann die Umriss-Pille mit einem Kreis-Icon daneben, Umschalter als Mono-Labels, Fotoraster mit 1-px-Fugen, unten eine Aktionszeile mit Haarlinie.
- Formulare und Einstellungen: Felder nur mit Unterkante untereinander, Labels in Mono-Versalien darüber, am Ende eine Umriss-Pille. Keine Gruppenkästen.
- Leere Zustände und Laden: eine Mono-Zeile mittig auf Schwarz und viel Leere; Laden als langsames Aufblenden grauer Flächen #141414, kein Schimmern.
- TV: Vollbild-Foto mit Mono-Unterschrift, Reiter oben, Fokus als weißer 1-px-Rahmen.
- Musterscreens: Start als Fotoband mit Kennzahlen-Haarlinien, Bibliothek als haarliniengetrennte Zeilenliste mit Mono-Filtern, Detail als Fotoband mit Serifen-Satz, Umriss-Pille und 1-px-Fugenraster.

## Vermeiden
- Keine Akzentfarbe, kein gefüllter Knopf, kein farbiger Aktiv-Zustand – aktiv wird über Strich und Helligkeit gezeigt.
- Keine Fettung; Emphase nur über Größe, Sperrung und Schreibweise.
- Keine abgerundeten Karten oder Bilder; Radius bleibt 0, einzige Ausnahme sind Pillen und Kreise.
- Weißraum nicht zusammenziehen, um mehr unterzubringen; lieber einen Bereich weniger.
- Display nie in Knöpfen, Mono nie im Fließtext, Serif nie in Labels – der Dreiklang bleibt getrennt.
- Keine Schatten, Verläufe, Glaseffekte oder Embleme; Tiefe kommt allein aus dem Foto.
