---
slug: starbucks
marke: Starbucks
website: https://www.starbucks.com
ansatz: galerie
ansatz2: verspielt
modus: hell
aufbau: Warme Cremefläche in Farbblock-Bändern: Creme → weiße 12-px-Karten → tiefgrünes Band → Creme, nie Linien
navigation: Unten vier Ziele mit Icon und Text, aktiv gefüllt mit grünem Balken; dazu ein runder 56-px-Schwebeknopf
komponenten: Pillen (50 px) für alle Knöpfe, weiße Karten mit Flüsterschatten, Kreis-Auswahl mit grünem Ring
icons: Phosphor rund, 22–24 px, Linie inaktiv / gefüllt aktiv, nie eckig (Empfehlung)
bewegung: Ruhig und warm: 200 ms ease, Druck `scale(.95)`, Aufklappen 300 ms cubic-bezier(.25,.46,.45,.94)
schrift: Humanistische Grotesk, Laufweite −0,01em überall; Hierarchie über Gewicht und Grün, Serif nur für Zeremonie
---
# Starbucks – Designsprache

**Kurz:** Eine warme Ladenfläche statt einer Website: cremefarbene Leinwand, weiße Karten mit Flüsterschatten und tiefgrüne Bänder wechseln sich als Farbblöcke ab. Jeder Knopf ist eine volle Pille, jede Hierarchie entsteht aus Gewicht und einer von vier Grünstufen – nicht aus Größe. Ein runder, schwebender Knopf ist das einzige Element mit echter Höhe.

## Wirkung
- Charakter: warm, einladend, verlässlich; wie gute Ladenbeschilderung – gut lesbar, nie laut.
- Passt zu: Bestell-, Treue-, Katalog-, Rezept- und Medien-Apps mit Alltagscharakter, Familien-Apps.
- Passt weniger zu: technischen Werkzeugen, dunklen Medien-Regalen, nüchternen Daten-Dashboards.

## Aufbau und Raster
- Seitenaufbau: Farbblock-Rhythmus Creme (`#f2f0eb`) → weiße Karten → tiefgrünes Band (`#1E3932`) → Creme → grüner Abschluss. Das dunkle Band ist der „eingelassene“ Bereich, kein Schatten.
- Ausrichtung: linksbündig, Knöpfe in Reihen; Kennzahlen stehen in der Karte, nicht in Tabellen.
- Raster: 4/8/16/24/32/40/48/56/64 px; 1,6 rem = 16 px ist die Konstante (Außenabstand, Karteninnenabstand, Grundtext). Spaltenbreite 343 px (mobil), 500/720/1440 px darüber.
- Dichte und Weißraum: großzügig – 40–64 px zwischen Abschnitten, 16–24 px in Karten, 12–16 px zwischen Karten. Trennung über Weißraum und Flächenwechsel, nicht über Striche.
- Rhythmus: hell, hell, dunkel – ein tiefgrünes Band pro Screen genügt als Betonung.

## Navigation
- Website: fixe Kopfleiste (64 → 72 → 83 → 99 px) mit dreilagigem weichen Schatten, Textlinks, rechts „Anmelden“ (Umriss-Pille) und schwarze Pille; darunter eine 48–53 px hohe Unterleiste mit Tabs.
- App: untere Leiste, weiß, 76 px, vier Ziele (Start, Bibliothek, Suche, Profil) mit Icon **und** Beschriftung 11/600; aktiv = gefülltes Icon + Starbucks-Grün + 24×3-px-Balken über dem Icon. Darüber schwebt rechts der runde 56-px-Knopf (Hauptaktion), der auf jedem Screen bleibt und beim Scrollen nicht verschwindet (App-Muster der Marke, nicht in der Datei).
- TV: Empfehlung – horizontale Bandnavigation oben, aktiv als Pille in Grün mit weißem Text; Fokus durch 2-px-Ring in Green Accent plus leichte Vergrößerung (1,04).

## Startscreen
- Cremefläche, oben Begrüßung 24/600 in Starbucks-Grün (`#006241`) plus Zahlenzeile 14 in `rgba(0,0,0,.58)`, rechts runder Avatar mit 2-px-Ring.
- Darunter eine weiße Zeremonie-Karte (Bild oben, Serif-Überschrift, Pillenpaar gefüllt + Umriss) – der einzige Ort mit Serif.
- Dann ein randloses tiefgrünes Band mit weißer Reihe aus Kacheln, danach die Statuskarte mit Gold und die Quellen als Umriss-Pillen.

## Komponenten
- Buttons: immer 50 px Radius. Gefüllt `#00754A` + Weiß; Umriss `1px #00754A` + grüner Text; Schwarz gefüllt für Konversionsmomente; auf Grün invertiert (weiß gefüllt, grüner Text) oder weiß umrandet. Innenabstand 7×16 px, groß 14×32 px, Text 14–16/600.
- Karten und Kacheln: Weiß, 12 px Radius, Schatten `0 0 .5px rgba(0,0,0,.14), 0 1px 1px rgba(0,0,0,.24)` – flach mit Andeutung. Bilder füllen die Karte oben randlos mit gleichem Radius.
- Listen: Jede Zeile ist eine eigene weiße Karte mit 12 px Abstand, 56-px-Vorschaubild (8 px Radius), Titel 16/600, Angaben 14 soft, rechts Chevron. Keine Trennlinien.
- Suche und Eingabefelder: Suchfeld als volle Pille, weiß, `1px #d6dbde`, 48 px hoch; Formularfelder dagegen 4 px Radius mit über dem Rahmen schwebendem Label 13/700 in Versalien; Fokus färbt den Rahmen auf Green Accent, gültige Felder bekommen einen blassgrünen Schimmer (`#d4e9e2` 33 %).
- Chips, Tabs, Filter: Signatur ist die **Kreis-Auswahl** – Reihe aus 52-px-Kreisen mit Icon und Beschriftung darunter, aktiv mit 2-px-Ring in Green Accent (aus dem Größenwähler der Produktseite). Unterseiten-Tabs sind Text mit 2-px-Unterstrich in Grün.
- Dialoge und Sheets: 12 px Radius, Innenabstand 24 px, oben 88 px Luft für Kopf und Schließen; Aufklappen 300 ms `cubic-bezier(.25,.46,.45,.94)`.
- Signatur-Komponenten: runder Schwebeknopf 56 px (Green Accent, gestapelter Schatten); tiefgrünes Feature-Band mit weißem Text und Pillenpaar; Statuskarte mit Gold (`#cba258`) für Zeremonie-Momente – im Vorbild die Treuestufen, in der App der Sammlungs- und Speicherstand.

## Icons
- Stil: runde, freundliche Linien-Icons mit geschlossenen Formen; Wechsel auf gefüllt nur im aktiven Navigationsziel (Empfehlung, abgeleitet aus Pillen- und Kreisgeometrie).
- Größe und Strich: 22–24 px in der Navigation, 20 px in Karten, 18 px in Knöpfen; Strich wirkt mittel (Phosphor `regular`), nie haarfein, nie eckig.
- Einsatz: Icons stehen links vom Text in Pillen und über der Beschriftung in der Kreis-Auswahl; sie tragen nie Farbe außer Grün, Weiß oder `rgba(0,0,0,.58)`.
- Umsetzung: Compose `Icons.Rounded` bzw. Material Symbols Rounded, Gewicht 400, Fill 0 → 1 für aktiv; iOS SF Symbols Regular, `.fill`-Variante aktiv; Web Phosphor `regular`/`fill` oder Lucide 2 px mit runden Enden.

## Bildsprache
- Produkt- und Momentfotos mit warmem Licht auf cremefarbenem oder weißem Grund; nie kalt freigestellt.
- Bilder sind Teil der Karte: oben randlos, 12 px Radius, 16:9 oder 2,4:1; Vorschauen quadratisch mit 8 px Radius.
- Illustrationen (Geschenkkarten) wirken gemalt und physisch – im Medienkontext übersetzt: Bilder liegen wie Abzüge auf der Creme, leichter Schatten statt Rahmen.
- Einblenden beim Laden mit `opacity .3s ease-in`; keine Verläufe, keine Überlagerungsfarben, kein Blur.

## Typografie-Stimme
- Eine humanistische Grotesk für alles, Laufweite `-0.01em` (≈ −0,16 px) durchgehend – der Satz wirkt leicht verdichtet und selbstbewusst.
- Hierarchie über Gewicht und Farbe, nicht über Größe: H1 24/600 in Starbucks-Grün, H2 24/400 in `rgba(0,0,0,.87)`; Fließtext 16/400 Zeilenhöhe 1,5; klein 14, Mikro 13.
- Versal-Labels mit 0,1–0,15 em Laufweite für Eyebrows; Knopftexte 14–16/600 Zeilenhöhe 1,2.
- Zeremonie-Serif (Treue-Momente) nur für eine Überschrift pro Screen, nie im Fließtext; Schreibschrift bleibt Personalisierungs-Momenten vorbehalten.
- Freier Ersatz: Inter oder Manrope (Grotesk), Lora oder Source Serif (Zeremonie-Serif), Kalam (Schreibschrift).

## Form, Tiefe und Material
- Radien: 50 px alle Knöpfe und Chips, 12 px Karten/Modale/Bilder, 8 px Vorschaubilder, 4 px Formularfelder, 50 % Kreise und Avatare.
- Linien und Rahmen: `1px #d6dbde` nur an Eingaben und Umriss-Pillen; Inhaltsbereiche werden nie durch Linien getrennt.
- Schatten und Ebenen: immer 2–3 sehr schwache Lagen statt eines harten Schattens – Karte `0 0 .5px/.14 + 0 1px 1px/.24`, Leiste dreilagig, Schwebeknopf `0 0 6px/.24 + 0 8px 12px/.14`.
- Besondere Oberflächen: keine Verläufe. Tiefe entsteht durch Farbblöcke: Creme, Keramik (`#edebe9`), Weiß, House Green (`#1E3932`), Gold-Creme (`#faf6ee`).

## Bewegung
- Laut Datei: `all .2s ease` an Knöpfen, Druckzustand `transform: scale(.95)`, Aufklappen 300 ms `cubic-bezier(.25,.46,.45,.94)`, Bild-Einblenden `.3s ease-in`, federnde Auswahl `cubic-bezier(.32,2.32,.61,.27)`.
- Empfehlung: Dauer klein 200 ms / Screenwechsel 300 ms, Easing `cubic-bezier(.25,.46,.45,.94)`, Druck-Effekt `scale(.95)` plus Wegfall des Umgebungsschattens beim Schwebeknopf, Einblenden 300 ms mit 20-ms-Staffel je Karte, Fokus (TV) 2-px-Ring plus `scale(1.04)`.
- Compose: `tween(200, easing = CubicBezierEasing(.25f,.46f,.45f,.94f))`, Druck über `animateFloatAsState(.95f)`, Auswahlring mit `spring(dampingRatio = .45f)`, Karten mit `AnimatedVisibility` + `animateItem()`.

## Signatur-Elemente
1. Cremefläche statt Weiß – die warme Temperatur trägt die Marke.
2. Volle Pille (50 px) für jeden Knopf, ohne Ausnahme, mit `scale(.95)` beim Druck.
3. Runder, schwebender 56-px-Knopf mit gestapeltem Schatten über allem.
4. Tiefgrünes Farbblock-Band mit weißem Text und Pillenpaar mitten im hellen Screen.
5. Kreis-Auswahl mit 2-px-Ring als aktive Filteranzeige statt Chips.

## Übertragung auf eine App
- Startscreen: Begrüßung in Grün, eine weiße Zeremonie-Karte mit Bild und Serif-Überschrift, ein randloses tiefgrünes Band mit Kachelreihe, darunter Statuskarte (Gold) und Quellen-Pillen.
- Liste und Übersicht: Suchpille, Kreis-Auswahl als Filter, danach jede Zeile als eigene weiße Karte mit Vorschaubild – Weißraum trennt, keine Linien.
- Detail: tiefgrünes Kopfband mit Brotkrume, Titel und Bild, darunter auf Creme die Pillen-Aktionsreihe, Unterstrich-Tabs, Bildraster (12 px Radius) und eine feste weiße Karte für die begleitende Musik.
- Formulare und Einstellungen: 4-px-Felder mit schwebendem Versal-Label, gültige Felder blassgrün getönt, Abschluss immer als gefüllte grüne Pille unten rechts.
- Leere Zustände und Laden: weiße Karte mit rundem Icon-Kreis, Satz in `rgba(0,0,0,.58)` und einer Umriss-Pille; Laden als cremefarbene Platzhalterflächen mit 12 px Radius, kein Spinner.
- TV: Creme bleibt Hintergrund, Bänder werden breiter; Fokus als 2-px-Ring in Green Accent plus 1,04-Vergrößerung, Beschriftungen bleiben sichtbar.
- Musterscreens: Start mit Zeremonie-Karte, grünem Band und Goldstatus; Bibliothek mit Kreis-Auswahl und Kartenliste; Detail mit grünem Kopfband, Pillen-Aktionen und Musikkarte.

## Vermeiden
- Reines Weiß als Fläche, kalte Grautöne, reines Schwarz im Text (`rgba(0,0,0,.87)` nutzen).
- Nur ein Grün verwenden – die vier Stufen haben feste Rollen (Grün = Überschrift, Accent = Aktion, House = Band, Uplift = Dekor).
- Gold als allgemeine Akzentfarbe; es gehört nur zu Status- und Zeremonie-Momenten.
- Eckige Knöpfe, Verläufe, einzelne harte Schatten, Trennlinien zwischen Abschnitten.
- Serif oder Schreibschrift im normalen Ablauf; Hierarchie über Schriftgröße statt Gewicht und Grünstufe.
