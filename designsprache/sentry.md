---
slug: sentry
marke: Sentry
website: https://sentry.io
ansatz: verspielt
ansatz2: plakativ
modus: gemischt
aufbau: Zwei getrennte Welten – violette Mitternacht für Einstieg und Detail, weiße Fläche für dichte Listen; dazwischen schwebende Sticker.
navigation: Unten schwebende dunkle Leiste (Radius 12 px) mit 4 Zielen, aktiv als weiß gefülltes Feld
komponenten: Sticker-Illustration, Limetten-Schlagwortchip, Karten in 18 px, Versal-Knöpfe, Mono-Werte
icons: Phosphor Bold, 18–22 px, kräftige Konturen; Statusleiste ausgenommen
bewegung: Empfehlung – knapp und federnd, 160/260 ms, cubic-bezier(.2,.8,.2,1), Druck 0.97, Sticker kippt leicht
schrift: Chunky-Schmal-Display (TeX Gyre Heros Cn Bold) über geometrischer UI-Schrift (Poppins), Versalien mit 0.2 px Laufweite, Mono für Zahlen
---
# Sentry – Designsprache

**Kurz:** Eine Entwicklermarke, die ihre Ernsthaftigkeit selbst stört: tiefviolette Mitternacht (`#1f1633`), ein einziges Limettengrün (`#c2ef4e`), das wie eine Syntaxmarkierung einzelne Wörter in der Überschrift unterlegt, und handgezeichnete Sticker, die über Abschnittsgrenzen hinausragen. Tiefe entsteht nicht durch Schatten, sondern durch Textur, Illustration und den harten Wechsel der Polarität. Dunkel und Hell sind zwei vollständige Welten, nie gemischt.

## Wirkung
- Charakter: dunkel, selbstbewusst, leicht subversiv; Konsolen-Kadenz in Versalien, dazu Comic-Persönlichkeit.
- Passt zu: Entwickler- und Monitoring-Werkzeugen, Communitys, Medien-Apps mit Haltung, allem mit Maskottchen.
- Passt weniger zu: Banken, Gesundheit, Luxus, allem, was neutral und unsichtbar wirken soll.

## Aufbau und Raster
- Seitenaufbau: Bänder mit einer Polarität pro Band. Dunkle Bänder = Einstieg, Feature, Detail; helle Bänder = Preise, Formulare, dichte Referenz. Kein Verlaufsübergang dazwischen.
- Ausrichtung: linksbündig, Überschrift über Fließtext über Aktion; Karten nebeneinander im 12-Spalten-Denken, max. 1152 px.
- Raster: Basis 8 px. Abstände 2 · 4 · 8 · 12 · 16 · 24 · 32 px, Bandabstand 96 px (mobil 32–48 px).
- Dichte und Weißraum: dunkle Flächen großzügig (96 px zwischen Bändern, 32 px Kartenpolster), helle Flächen dicht (Zeilen 56–68 px, 16 px Polster) – Marketing atmet, Transaktion scannt.
- Rhythmus: große Überschrift → luftiger Fließtext (Zeilenhöhe 2.0) → eine Aktion. In der App: Zeilenhöhe 1.5, „wie ein Log“.

## Navigation
- Website: helle oder dunkle Kopfleiste, Wortmarke links, Menüpunkte mittig mit Klapppfeilen, rechts Geist-Knopf plus ein gefüllter Hauptknopf; mobil Hamburger unter 768 px.
- App (Empfehlung, aus Komponenten abgeleitet): unten eine schwebende Leiste, 16 px vom Rand, Radius 12 px („navigation pill chrome“), Füllung `#150f23`, 4 Ziele (Start, Bibliothek, Suche, Profil) mit Bold-Icon 20 px und Versal-Label 10 px/600. Aktiv = weiß gefülltes Innenfeld mit dunklem Icon (Polaritätswechsel wie beim `button-inverted`), nie nur Farbe. Beim Scrollen bleibt sie stehen.
- TV: Empfehlung – waagerechte Kopfzeile mit Versal-Labels; Fokus als weiß gefülltes Feld, dazu 2 px Limettenkante.

## Startscreen
- Versal-Augenbraue 10 px, darunter zweizeilige Display-Überschrift; genau ein Wort steckt im Limettenchip (hier der Name).
- Darunter eine Mono-Zeile mit den Zahlen der Bibliothek – Konsolenausgabe statt Marketingtext.
- Ein hervorgehobener Inhalt in einer Karte `#150f23` mit 1 px Haarlinie `#362d59`, Radius 18 px, Bild darin leicht gekippt; weißer Versal-Knopf als einzige starke Aktion.
- Ein Sticker ragt über die Kartenkante hinaus und bricht das Raster.
- Weitere Bereiche: angeschnittene Reihe „Weiter ansehen“, danach Quellen als Zeilen mit Mono-Status.

## Komponenten
- Buttons: Hauptknopf gefüllt – auf Hell `#150f23` mit weißer Schrift, auf Dunkel weiß mit `#1f1633`; Radius 8 px, Polster 12/16 px, Label 14 px/700 VERSALIEN mit 0.2 px Laufweite. Gedrückt kippt die Polarität (`#efefef`/`#1a1a1a`). Geist-Knopf auf Dunkel: Füllung rgba(255,255,255,.18), Radius 12 px, 8 px Polster.
- Karten und Kacheln: dunkle Karte `#150f23` oder `#1f1633` mit Haarlinie `#362d59`, Radius 18 px (Bildcontainer) bzw. 12 px (Listenkarten); helle Karte weiß mit `#e5e7eb`. Niemals Schlagschatten auf dunklem Grund.
- Listen: nur auf heller Fläche. Zeile 68 px, Trenner 1 px `#e5e7eb`, Vorschaubild 44 px mit Radius 4 px, Titel 16 px/500, Beiwert 14 px/400 in `#79628c`, rechts Zahlenwert in Mono.
- Suche und Eingabefelder: weiß, 1 px `#cfcfdb`, Radius 6 px, Polster 8/12 px, Fokus mit Innenschatten `rgba(0,0,0,.15) 0 2px 10px inset`; Fokusring `#9dc1f5` – das einzige Blau im System.
- Chips, Tabs, Filter: Versal-Pillen, Radius 12 px, Polster 8/16 px; inaktiv transparent mit Haarlinie, aktiv gefüllt (`#150f23` auf Hell, `#79628c` auf Dunkel). Statuspillen `#150f23`, Radius 4 px, 4/8 px.
- Dialoge und Sheets: Polarität des Screens behalten, Radius 18 px, Haarlinie statt Schatten; auf Hell Ebene 2 (`0 10px 15px -3px rgba(0,0,0,.1)`).
- Signatur-Komponenten: Limetten-Schlagwortchip (Radius 4 px, 12 px seitliches Polster, 0 vertikal) im Display-Titel; Sticker-Ebene; Limetten-Schlängellinie als Trenner, ~3 px Strich; Sternenfeld-Textur auf dunkler Fläche; gekippter Bildrahmen mit Haarlinie.

## Icons
- Stil: Phosphor **Bold** – kräftige, geschlossene Konturen, runde Enden; passt zu den handgezeichneten Stickern.
- Größe und Strich: 18 px in Zeilen, 20 px in der Navigation, 22 px in Knöpfen; keine Mischung mit dünnen Linien.
- Einsatz: sparsam, immer mit Label oder Versal-Kürzel; Aktiv-Zustand kommt aus der Fläche, nicht aus dem Icon.
- Umsetzung: Compose `Icons.Rounded` bzw. Material Symbols Rounded, Gewicht 600, Füllung 0; iOS SF Symbols `bold`; Web Phosphor `weight="bold"` oder Lucide mit `stroke-width: 2.25`.

## Bildsprache
- Keine klassische Fotografie: Produkt-Mockups in Rahmen mit Radius 18 px, oft 2–3° gekippt, ohne Schatten, nur Haarlinie `#362d59`.
- Illustrierte Sticker mit harter dunkler Außenlinie und satten Flächen (`#fa7faa`, `#c2ef4e`) liegen ohne Container direkt auf der Fläche und überlappen Kanten um 30–40 % ihrer Höhe.
- Fotos in einer App: Seitenverhältnis 16:10 bis 3:2, Radius 12–18 px, leichte Körnung (`.grain`, 0.12) und ein violetter Dunst, damit sie zur Mitternachtsfläche gehören; Rasterbilder Radius 8 px.
- Logos und Porträts im Strip grau statt farbig.

## Typografie-Stimme
- Display chunky und fast schmal, 40–88 px, Gewicht 700, Zeilenhöhe 1.0–1.2 – Überschrift als Block, nicht als Satz.
- UI-Schrift geometrisch (Rubik), 16 px/500 für Fließtext, 14 px/400 für Beiwerk; Marketingtext mit Zeilenhöhe 2.0, Produkttext mit 1.5.
- Versalien mit 0.2 px Laufweite für alle Knöpfe und Augenbrauen, 10 px/600 mit 0.25 px für Mikro-Labels. Zahlen gern Mono (Monaco), 13–16 px.
- Freier Ersatz: Space Grotesk oder Archivo (Display), Rubik (UI), JetBrains Mono (Code). Hier gerendert: TeX Gyre Heros Cn Bold, Poppins, DejaVu Sans Mono.

## Form, Tiefe und Material
- Radien: 4 px Chips und Statuspillen · 6 px Eingaben · 8 px Knöpfe, Code, Rasterbilder · 10 px Blöcke · 12 px Karten und Navigationsleiste · 18 px Bildrahmen und große Karten · voll für Avatare.
- Linien und Rahmen: 1 px `#362d59` auf Dunkel, 1 px `#e5e7eb` auf Hell, 1 px `#cfcfdb` an Eingaben. Linien tragen die Struktur, nicht Schatten.
- Schatten und Ebenen: auf Dunkel keine; nur der helle Knopf auf dunklem Grund darf einen Hof in der Flächenfarbe tragen (`0 0 8px 6px #150f23`). Auf Hell Ebene 2 für Karten und Dialoge.
- Besondere Oberflächen: Sternenfeld-Textur (feine helle Punkte, sehr niedrige Deckkraft), Körnung, Limetten-Schlängellinie, gekippte Rahmen.

## Bewegung
- Laut Datei: keine Angaben (nur Default- und Druck-Zustände dokumentiert).
- Empfehlung: klein 160 ms / Screenwechsel 260 ms, Easing `cubic-bezier(.2,.8,.2,1)`; Druck = Polaritätswechsel plus `scale(.97)`; Einblenden 12 px von unten, 40 ms gestaffelt; Sticker beim Erscheinen von 8° auf 0° drehen; Fokus (TV) als weiß gefülltes Feld in 120 ms.
- Compose: `tween(160, easing = CubicBezierEasing(.2f,.8f,.2f,1f))`, Druck über `animateFloatAsState` auf 0.97f, Listen mit `animateItem()`, Screenwechsel als `AnimatedContent` mit `slideInVertically`.

## Signatur-Elemente
1. Limettenchip um ein einzelnes Wort in der Display-Überschrift – genau ein Limettenelement pro Screen.
2. Handgezeichneter Sticker, gekippt, über die Kartenkante hinausragend, ohne Container und ohne Schatten.
3. Harter Polaritätswechsel: dunkelvioletter Einstieg, weiße Listenfläche, dunkles Detail.
4. Versal-Knöpfe und Mikro-Labels mit 0.2 px Laufweite, dazu Mono-Zahlen.
5. Schwebende dunkle Navigationsleiste mit weiß gefülltem Aktiv-Feld.

## Übertragung auf eine App
- Startscreen: dunkle Fläche, Augenbraue, Display-Titel mit Limettenchip, Mono-Zahlenzeile, eine große Karte mit gekipptem Bild und weißem Versal-Knopf, darüber ein Sticker; danach eine angeschnittene Reihe und Quellen als Zeilen mit Mono-Status.
- Liste und Übersicht: auf **weißer** Fläche, dicht – Suchfeld, Versal-Filterpillen, Zählzeile, 68-px-Zeilen mit Haarlinien und rechtsbündigen Mono-Werten. Die dunkle Navigationsleiste bleibt dunkel und schwebt darüber.
- Detail: zurück zur dunklen Fläche; gekippter Bildrahmen mit Haarlinie, Display-Titel, Statuspillen, weißer Hauptknopf plus zwei Geist-Knöpfe, Violettpillen als Umschalter, dichtes Fotoraster, unten die Limetten-Schlängellinie über der Musikzeile.
- Formulare und Einstellungen: immer auf heller Fläche, Felder mit 1 px `#cfcfdb` und Radius 6 px, Labels 16 px/500, ein einziger gefüllter Hauptknopf unten.
- Leere Zustände und Laden: Sticker plus ein Satz in 16 px/400 und ein Versal-Knopf; Ladeplatzhalter als Blöcke in `#150f23` ohne Schimmer.
- TV: dunkle Fläche beibehalten, Reihen mit 18-px-Rahmen, Fokus weiß gefüllt mit Limettenkante, Labels in Versalien.
- Musterscreens: Start dunkelviolett mit Limettenchip und Sticker, Bibliothek als dichte weiße Liste mit Mono-Werten, Detail dunkel mit gekipptem Rahmen, Violettpillen und Limetten-Schlängellinie.

## Unterschied zu ClickHouse (beides Entwickler-Infrastruktur)
Sentry ist **verspielt und plakativ**: violette Mitternacht, runde 12–18-px-Flächen, Illustration, fette geschlossene Icons, eine riesige Schmal-Display-Zeile, Polaritätswechsel zwischen Screens. ClickHouse ist **Daten und Werkzeug**: fast schwarze Fläche, Tabellen mit Spaltenköpfen, Kennzahlen in Gelb, Mono-Zellen, dünne eckige Linien-Icons, 8–12-px-Radien, durchgehend dunkel. Kurz: Sentry erzählt, ClickHouse misst.

## Vermeiden
- Limette als Knopffarbe, Fließtext oder zweite Flächenfarbe – sie ist ein Chip, und nur einer pro Screen.
- Weitere Akzentfarben neben Limette und Pink; Türkis oder Orange zerstören die Signatur.
- Schlagschatten auf dunklen Karten – Tiefe kommt aus Textur und Illustration.
- Hell und Dunkel in einem Band mischen oder Flächen ineinander überblenden.
- Den Hauptknopf zu einem freundlichen Violett weichspülen; das Fast-Schwarz ist der Punkt.
- Sticker in Karten sperren oder gerade stellen – sie sollen das Raster brechen.
- Display-Größe 88 px außerhalb der einen Hauptüberschrift einsetzen.
