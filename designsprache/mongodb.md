---
slug: mongodb
marke: MongoDB
website: https://www.mongodb.com
ansatz: buehne
ansatz2: galerie
modus: gemischt
aufbau: Dunkles Petrol-Band oben als Bühne, darunter weiße Fläche mit 12-px-Karten; eine Karte überlappt die Bandkante
navigation: Leiste unten in Petrol #001e2b, 4 Ziele mit Icon und Beschriftung, aktiv = gefüllte Pille #00684a
komponenten: Grüne Pill-Buttons #00ed64 mit Petrol-Schrift, Katalogkacheln mit farbigem Kategorie-Tag, Mint-Badges
icons: Empfehlung: geometrische Phosphor-Icons in Bold, 18–22 px; weiß auf Petrol, Petrol/Steel auf Weiß
bewegung: Empfehlung: 150–200 ms ease-out, Pille drückt auf #008c34; Karten blenden mit 8 px von unten ein
schrift: Geometrisch (Euclid Circular A → Poppins): Titel 500 mit −0,5 px, Tags 11 px 600 Versalien, Sperrung 1 px
---
# MongoDB – Designsprache

**Kurz:** Zwei Modi in einem Screen: ein tiefes Petrol-Band (#001e2b) trägt Überschrift und Aktion, darunter beginnt eine stark weiße Fläche mit 12-px-Karten. Jeder Knopf ist eine Pille, jeder Inhalt bekommt ein farbiges Kategorie-Tag, und das helle Grün #00ed64 erscheint nur als gefüllte Pille mit petrolfarbener Schrift. Die Kante zwischen Dunkel und Hell wird bewusst von einer Karte durchbrochen.

## Wirkung
- Charakter: selbstbewusst, geometrisch, freundlich-technisch; Produkt und Lernkatalog in einem Ton.
- Passt zu: Medien- und Kurskatalogen, Cloud- und Speicher-Apps, Plattform-Dashboards, Onboarding-Strecken.
- Passt weniger zu: stillen Minimal-Apps, Editorial/Lesen, Luxus- und Mode-Marken.
- Abgrenzung zu Supabase (gleiche Branche, auch Grün): MongoDB rahmt mit vollflächigen Petrol-Bändern, Pill-Buttons, geometrischer Poppins-Schrift und bunten Kategorie-Tags; Inhalte sind Kacheln im Katalog-Raster. Supabase bleibt durchgehend weiß, eckig (6 px), neutral grau, mit Datentabelle und Inter – Dunkel nur als eingesetzte Code-Pane.

## Aufbau und Raster
- Seitenaufbau: Band (dunkel) → überlappende Karte → weiße Abschnitte mit Karten/Kacheln → dunkler Fuß bzw. dunkle Leiste.
- Ausrichtung: linksbündig in der App (Web-Hero zentriert); Tags und Badges immer oben links in der Karte.
- Raster: 4-px-Basis mit 8-px-Schritt; Tokens 4·8·12·16·20·24·32·40·48·64·96·120 px. Web 1280 px Container, 32 px Gassen; Katalog 3-spaltig → 2 → 1.
- Dichte und Weißraum: Web-Abschnitte 64–96 px, Hero 120 px. App (Empfehlung): Rand 20 px, Kartenabstand 12 px, Abschnitte 20–24 px, Karten innen 14–16 px.
- Rhythmus: Eyebrow 11 px Versalien → Überschrift → Fließtext → Pillenreihe; dieser Vierklang wiederholt sich in Band und Karten.

## Navigation
- Website: weiße Kopfleiste 64 px mit Haarlinie, Links mittig, rechts Textlink und grüne „Jetzt starten“-Pille; darüber ein dunkler Petrol-Promo-Streifen. Unter 1024 px Hamburger.
- App (Empfehlung, abgeleitet aus Band, Fuß und Pill-Tabs): Leiste unten in #001e2b, Höhe 76 px, 4 Ziele (Start, Bibliothek, Suche, Profil) mit Icon 21 px und Beschriftung 10 px. Aktiv = gefüllte Pille #00684a mit weißem Icon und Text; inaktiv #a8b3bc. Steht beim Scrollen.
- Im Band oben: runde 36-px-Icon-Buttons mit 1 px #1c2d38, Avatar 30 px; Zurück als runde Pille links.
- Filter in der Fläche: Pill-Tabs (inaktiv Haarlinie, aktiv gefüllt #001e2b, weiße Schrift), Unterabschnitte als Unterstrich-Tabs in #00684a.
- TV: Petrol-Fläche, linke Pillenliste; Fokus = Pille #00684a + 2 px #00ed64.

## Startscreen
- Petrol-Band mit Begrüßungszeile (Avatar + Name), Eyebrow in Grün, Überschrift 30 px 500, Zeile in #a8b3bc, zwei Pillen (grün primär, umrandet sekundär).
- Darunter die Signaturkarte: Petrol-Mitte #003d4f, 12 px Radius, Schatten 3, 56 px in das Band hineingezogen; enthält das Bild, Titel und die grüne Pille.
- Weiße Fläche: Quellen-Karte mit Pill-Tabs und Speicherbalken, danach ein 2-spaltiges Kachelraster „Zuletzt hinzugefügt“ mit Kategorie-Tags.

## Komponenten
- Buttons: immer Pille (9999 px), 14 px 600, Padding 10 × 22 px, App-Höhe 40–44 px. Primär #00ed64 mit Schrift #001e2b (nie weiß), gedrückt #008c34; sekundär transparent mit 1 px #c1ccd6 (auf Dunkel #1c2d38); Textlink in #00684a.
- Karten und Kacheln: weiß, 12 px Radius, 1 px #e1e5e8, Innenabstand 16–24 px, flach; Feature-Karten Schatten 2 `0 4px 12px rgba(0,30,43,.08)`; dunkle Karten #001e2b bzw. #003d4f mit Schatten 3. Kachel = Bild 12 px oben, Tag, Titel 18 px 600, Angaben 14 px, grüner Textlink.
- Listen: Vergleichszeilen 12 × 20 px mit 1 px #eceff1 unten, keine Gitterlinien, keine Zebrastreifen.
- Suche und Eingabefelder: 8 px Radius (nicht Pille!), 44 px hoch (groß 56 px), 1 px #c1ccd6, Fläche weiß oder #f9fbfa; Fokus 2 px #00684a.
- Chips, Tabs, Filter: Pill-Tabs 8 × 16 px; Unterstrich-Tabs mit 2 px #00684a; Badges als Pille: Mint #c3f0d2 auf #00684a, „beliebt“ als Petrol-Pille mit grüner Schrift.
- Dialoge und Sheets: weiß, 16 px Radius, Schatten 4 `0 16px 48px -8px rgba(0,30,43,.16)`.
- Signatur-Komponenten: Kategorie-Tag 4 px Radius, 11 px 600 Versalien, Sperrung 1 px, vollflächig in Lila #7b3ff2, Orange #fa6e39, Blau #3d4f9f oder Pink #f06bb8; Petrol-Mockup-Karte, die aus dem Band herausragt.

## Icons
- Stil (Empfehlung, die Datei nennt keine Icons): geometrische, kräftige Linien mit runden Ecken – zur Rundung der Schrift; einfarbig in Weiß, Petrol oder #5c6c7a, nie zweifarbig. Grün nur, wenn das Icon Teil eines grünen Textlinks ist (Pfeil hinter „Öffnen“).
- Größe und Strich: 21 px in der Leiste, 18 px in Karten und Knöpfen, 15 px in Zeilen; wirksame Strichstärke etwa 2 px auf 24er-Raster.
- Einsatz: in runden Icon-Buttons 36–40 px, in Pill-Tabs vor dem Text, als Quellenzeichen; Status als Mint-Badge statt als Icon.
- Umsetzung: Compose `Icons.Rounded` bzw. Material Symbols Rounded, Gewicht 500–600, Füllung 0; iOS SF Symbols `.semibold`; Web Phosphor `bold`.

## Bildsprache
- Laut Datei: Hero-Illustrationen vollflächig auf dunklem Grund, Kachelbilder mit 12 px Radius, Logos einheitlich 60–80 px, 16:9 für atmosphärische Bilder.
- Übertragung: Bilder immer gerundet (12 px, Kachel 10 px) und in Karten; im Band auf Petrol gesetzt, dort mit 1 px #1c2d38 gerahmt. Keine Filter, keine Verläufe über dem Motiv, kein Text im Bild – Text steht darunter. Raster mit 8 px Fuge.

## Typografie-Stimme
- Geometrisch und rund, mittleres Gewicht: Display 500 mit −1,5 px (72) bis −0,5 px (36/28), Fließtext 400 mit großer Zeilenhöhe 1,55.
- Größen: 72/56/48 Display, 36/28/22/18 Überschriften, 18/16/14 Text, 13 Badge, 11 Tag. App: Titel 30, Kartentitel 18 (600), Text 14, Angaben 13, Tag 11.
- Versalien nur im 11-px-Tag und im Eyebrow, dort 600 mit 1 px Sperrung – der typografische Fingerabdruck der Marke.
- Mono (Source Code Pro) ausschließlich in Code-Mockups, nie für Fließtext.
- Freier Ersatz: Poppins (500 für Titel, 400 für Text) oder TeX Gyre Adventor; Mono Liberation Mono, Source Code Pro. Hinweis: Poppins hat kein 600 – Buttons dort 500, Tags 700.

## Form, Tiefe und Material
- Radien: 4 px Kategorie-Tags, 6 px Typ-Badges, 8 px Felder und Code, 12 px Karten und Bilder, 16 px große Panels, 24 px Showcases, Pille für alle Buttons und Status-Badges.
- Linien und Rahmen: 1 px #e1e5e8 Standard, #eceff1 leise, #c1ccd6 für Felder, #1c2d38 auf Dunkel; Featured-Rahmen 2 px #00ed64 auf Mint #e3fcef.
- Schatten und Ebenen: 0 flach + Haarlinie (Dokumentationskarten), 1 `0 1px 2px rgba(0,30,43,.04)`, 2 `0 4px 12px rgba(0,30,43,.08)`, 3 `0 12px 24px -4px rgba(0,30,43,.12)` nur für die Karte über dem Band, 4 für Dialoge.
- Besondere Oberflächen: Petrol-Band mit leichtem atmosphärischem Verlauf nach #003d4f; Mint-Fläche #e3fcef als einzige getönte Fläche; keine Körnung, kein Glas.

## Bewegung
- Laut Datei: keine Angaben (Hover ausdrücklich nicht dokumentiert); empfohlen werden dort 150–200 ms ease.
- Empfehlung: Dauer klein 150 ms / Screenwechsel 200 ms, Easing `cubic-bezier(0.22, 1, 0.36, 1)`; Druck-Effekt: Pille auf #008c34 und 0,97 skalieren; Einblenden: Deckkraft + 8 px von unten, Kacheln 60 ms gestaffelt; Screenwechsel: Band bleibt, weiße Fläche schiebt nach; Fokus (TV): Pille wächst auf 1,04.
- Compose: `tween(150, easing = CubicBezierEasing(0.22f, 1f, 0.36f, 1f))`, `AnimatedVisibility(fadeIn() + slideInVertically { it / 12 })`, `Modifier.animateItem()`, Shared-Element für Kachel → Detailbild.

## Signatur-Elemente
1. Tiefes Petrol-Band #001e2b als Kopf jedes Screens, durchbrochen von einer überlappenden Karte.
2. Grüne Pille #00ed64 mit petrolfarbener Schrift – die einzige gefüllte Farbe als Aktion.
3. Kategorie-Tag in Lila, Orange, Blau oder Pink, 11 px Versalien mit 1 px Sperrung, 4 px Radius.
4. Rundes, geometrisches Schriftbild (Euclid/Poppins) mit großer Zeilenhöhe im Fließtext.
5. Alles rund: Pillen für Knöpfe und Badges, 12 px für Karten und Bilder.

## Übertragung auf eine App
- Startscreen: Petrol-Band mit Begrüßung, Eyebrow, Rückblick-Überschrift und zwei Pillen; darunter die überlappende Petrol-Karte mit Bild und grüner Pille; dann Quellen-Karte und Kachelraster.
- Liste und Übersicht: Band mit Titel und Anzahl, Suchfeld (8 px) über die Bandkante gezogen, Pill-Tabs als Filter, 2-spaltiges Kachelraster mit Kategorie-Tags und grünem Textlink.
- Detail: Band mit Zurück-Pille, Bild in gerahmter Karte, Titel 30 px, Badges, grüne Pille plus runde Icon-Buttons; in der weißen Fläche eine Musik-Karte, Unterstrich-Tabs und das Fotoraster.
- Formulare und Einstellungen: weiße Karten, Label 14 px 500 über dem Feld, Felder 44 px mit 8 px Radius, Abschluss mit grüner Pille rechts.
- Leere Zustände und Laden: Mint-Fläche #e3fcef mit 12 px Radius, ein Satz in #3d4f5b, grüne Pille; Laden als Kachel-Gerüste in #eceff1 mit 12 px Radius.
- TV: Band als Kopfzone, Kacheln 3-spaltig größer, Fokus als Pille.
- Musterscreens: Start mit Petrol-Band und überlappender Rückblick-Karte, Bibliothek als Kachelkatalog mit Kategorie-Tags, Detail „Lissabon“ mit gerahmtem Bild im Band und Musik-Karte darunter.

## Vermeiden
- Grün für Fließtext, große Flächen, Icons oder Rahmen von Karten; weiße Schrift auf der grünen Pille.
- Eckige oder leicht gerundete Buttons – die Pille ist Pflicht; Karten mit mehr oder weniger als 12 px.
- Weiße Hero-Bänder statt Petrol; zusätzliche Akzentfarben außerhalb der Kategorie-Tags.
- Schatten auf jeder Dokumentationskarte (flach + Haarlinie ist Standard); Mono für Fließtext.
