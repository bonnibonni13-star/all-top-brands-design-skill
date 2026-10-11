---
slug: raycast
marke: Raycast
website: https://raycast.com
ansatz: werkzeug
ansatz2: minimal
modus: dunkel
aufbau: Befehlsleiste oben als Einstieg, darunter dichte, gruppierte Befehlszeilen in randlosen Flächenstufen, unten eine Aktionsleiste.
navigation: Oben Suchfeld + Bereichsleiste mit vier Zielen und Tastenkürzel-Kappen (⌘1–⌘4); unten Aktionsleiste statt Tab-Leiste.
komponenten: Befehlspalette, Befehlszeile mit 32-px-Kachel und Keycap, Keycaps, Haarlinien-Karten, weiße CTA-Pille, Chips
icons: Phosphor Bold, 15–16 px, nur monochrom (#cdcdcd/#fff); farbige Glyphen nur in Icon-Kacheln
bewegung: nüchtern und schnell; 120/180 ms, cubic-bezier(.2,0,0,1), Auswahl springt ohne Nachfedern
schrift: Inter mit ss03, Gewichte 400/500/600, positive Laufweite 0,1–0,4 px, kleine Grade, 1,6 Zeilenhöhe
---
# Raycast – Designsprache

**Kurz:** Die Oberfläche ist eine Befehlspalette, auf App-Größe gezogen: nahezu schwarze Fläche, Haarlinien statt Schatten, dichte Zeilen mit kleiner Icon-Kachel links und Tastenkappe rechts. Navigiert wird über Suchen und Tastenkürzel, nicht über eine Tab-Leiste. Farbe ist knapp: Weiß für die eine Hauptaktion, gesättigte Töne nur in Icon-Kacheln.

## Wirkung
- Charakter: tastaturgetrieben, schnell, nüchtern, sehr dicht; „die Seite ist das Produkt“.
- Passt zu: Werkzeuge, Entwickler-Apps, Launcher, Suche, Verwaltung vieler Objekte, Power-User-Apps.
- Passt weniger zu: verspielte Consumer-Apps, Marken mit Bildbühne, helle oder bunte Produkte.

## Aufbau und Raster
- Seitenaufbau: feste Befehlsleiste oben → Bereichsleiste → scrollender Inhalt in Gruppen → feste Aktionsleiste unten.
- Ausrichtung: alles linksbündig an einer Kante; Metadaten rechtsbündig in derselben Zeile (zweispaltiges Zeilenbild).
- Raster: 8-px-Basis mit 2/4/12-px-Zwischenstufen; Tokens 2/4/8/12/16/24/32 px, Abschnittsabstand 96 px (App: 24–32 px).
- Dichte und Weißraum: hoch dicht. Zeilenhöhe 44–52 px, Kartenpolsterung 16–24 px (nie 32 px rundum), Seitenrand 16 px.
- Rhythmus: kleine Gruppenüberschrift (12 px, Versalien, mute) → Block aus Zeilen → 20 px Luft → nächste Gruppe.

## Navigation
- Website: 56-px-Kopfleiste, Links mittig, rechts „Sign in“ + weiße CTA-Pille; mobil Hamburger-Schublade.
- App (Empfehlung, aus Produktlogik der Marke abgeleitet): Suchfeld ganz oben ist der Einstieg; darunter eine Bereichsleiste mit vier Zielen (Start, Bibliothek, Suche, Profil) als Pill-Tabs, jeweils mit Keycap ⌘1–⌘4. Aktiv = Fläche eine Stufe heller (#101111) + weiße Schrift + sichtbare Keycap; inaktiv = transparent, #cdcdcd, Keycap ausgeblendet. Beim Scrollen bleiben Such- und Bereichsleiste stehen. Unten keine Tab-Leiste, sondern eine Aktionsleiste (44 px, Haarlinie oben): links Kontext („8 Einträge“), rechts „Aktionen“ + Keycap ⌘K. Profil wird zusätzlich über den Avatar rechts im Suchfeld erreicht.
- TV: dieselbe Palette im Vollbild, Fokus als eine Flächenstufe heller plus 1-px-Rahmen #242728; Tastenkappen zeigen Fernbedienungstasten.

## Startscreen
- Einmalig oben das rote Streifenband (drei diagonale Streifen #ff5757 → #a1131a), darüber Begrüßung in 30–34 px/600 und eine Kennzahlenzeile in 13 px mute.
- Darunter sofort die Befehlspalette: Suchzeile mit Lupe und Keycap ⌘K, dann 3–4 Vorschlagszeilen, die erste in Auswahlfläche #121212 mit ⏎ rechts.
- Danach eine Gruppe „Quellen“ als Zeilen mit Statuswort rechts und eine Speicherzeile mit 2-px-Balken. Keine Bildbühne, keine Regale.

## Komponenten
- Buttons: primär weiß (#fff) auf Schwarz, Text #000, 14/500, Radius 8 px, Höhe 36 px, Polsterung 8/16 px – höchstens eine weiße Pille pro Bildschirmhöhe. Tertiär: Fläche #101111, weiße Schrift, gleiche Maße. Sekundär: transparent, nur Text. Install-Variante: transparent mit 1-px-Rahmen rgba(255,255,255,.16).
- Karten und Kacheln: Fläche #0d0d0d, 1 px #242728, Radius 10 px (Palette 16 px), Polsterung 16–24 px, **nie Schatten**. Tiefe entsteht nur über die Flächenleiter #07080a → #0d0d0d → #101111 → #121212.
- Listen: Befehlszeilen, 6/10 px Polsterung, Radius 6 px, links 32-px-Kachel (Radius 8 px), Titel 15/500, darunter oder rechts Metadaten 12–13 px mute, ganz rechts Keycap. Aktive Zeile = Fläche #121212, kein Farbwechsel.
- Suche und Eingabefelder: Fläche #101111, 1 px #242728, Radius 8 px, Höhe 36 px (Suchleiste 44 px, Polsterung 10/16 px); Fokus hellt nur den Rahmen auf (#ffffff29), kein farbiger Ring.
- Chips, Tabs, Filter: Pill-Tabs, Radius 9999 px, 4/10 px, 13 px; aktiv eine Flächenstufe heller plus weiße Schrift. Badges: Radius 4 px, 2/6 px, 12 px, Fläche #101111.
- Dialoge und Sheets: wie die Palette – Haarlinien-Karte mit Radius 16 px, Kopfzeile mit Titel, Fußzeile mit Keycap-Hinweisen (⏎ bestätigen, Esc schließen).
- Signatur-Komponenten: Befehlspalette (Suchzeile + Zeilen + Fuß), Keycap (Radius 4 px, Höhe 20 px, Verlauf #121212 → #0d0d0d, Text 12 px #cdcdcd), Aktionsleiste unten, rotes Streifenband, Icon-Kachel 32–48 px mit farbiger Glyphe.

## Icons
- Stil: kompakte, geschlossene Formen; in der App konsequent **ein** Satz (Phosphor Bold als Entsprechung der 16-px-Produkt-Icons der Marke – Empfehlung).
- Größe und Strich: 15–16 px in Zeilen und Leisten, 18 px in Aktionsknöpfen; Icons stehen immer in einer 32-px-Kachel oder optisch auf der Textkante.
- Einsatz: Icon nie als Schmuck, immer als Objekt-Marke links in der Zeile oder als Knopf. Gesättigte Farben (#ffc533, #ff6161, #59d499, #57c1ff) ausschließlich als Glyphe in der Kachel, nie auf Text, Knöpfen oder Leisten.
- Umsetzung: Compose `Icons.Filled`/Material Symbols Rounded, Fill 1, Gewicht 500, 16 dp; iOS SF Symbols semibold, klein; Web Phosphor `bold` 16 px (oder Lucide mit stroke-width 2,25).

## Bildsprache
- Die Marke kennt keine Fotografie: Bilder werden wie App-Icons behandelt – quadratische Kacheln 32/48 px, Radius 8 px, 1 px Haarlinie.
- Größere Bilder nur als „Mockup-Container“: Radius 16 px, 1 px #242728, 16 px Abstand zum Rand, nie randlos über die volle Breite.
- Raster eng: 8-px-Abstand, Radius 6–8 px, quadratisch. Keine Verläufe über Bildern, keine Textauflagen – Beschriftung steht darunter oder daneben.
- Leichte Körnung (`--grain: .1`) und ein Hauch Entsättigung halten Bilder im dunklen Gesamtton.

## Typografie-Stimme
- Inter mit `font-feature-settings: "calt","kern","liga","ss03"` – das alternative `g` gehört zur Marke. Gewichte 400/500, 600 nur im Titel.
- Kleiner Größenkontrast: Titel 30–34 px, Überschriften 20–24 px, Text 15–16 px, Metadaten 12–13 px; Zeilenhöhe 1,4–1,6.
- Laufweite durchgehend leicht positiv (0,1–0,4 px); Gruppenüberschriften 12 px, Versalien, 0,08 em, Farbe #9c9c9d. Keine Kapitälchen-Titel, keine gesperrten Großtitel.
- Freier Ersatz: Inter (Google Fonts) mit ss03; sonst Geist oder system-ui.

## Form, Tiefe und Material
- Radien: 4 px Keycap/Badge, 6 px Zeile/Chip, 8 px Knopf/Eingabe/Kachel, 10 px Karte, 16 px Palette/Bildcontainer, 9999 px nur Pill-Tabs und Avatar.
- Linien und Rahmen: 1 px #242728 an jeder Kartenkante; stärkere Trennung rgba(255,255,255,.16); Trennlinien in Listen 1 px, auf voller Zeilenbreite.
- Schatten und Ebenen: keine. Ausschließlich Flächenleiter.
- Besondere Oberflächen: Keycap-Verlauf #121212 → #0d0d0d (einzige „Tiefe“), rotes Streifenband genau einmal pro Screen, weiche Akzentflächen rgba(…,.15) hinter Glyphen.

## Bewegung
- Laut Datei: keine Angaben (Hover-Zustände sind bewusst nicht dokumentiert).
- Empfehlung: klein 120 ms / Screenwechsel 180 ms, Easing `cubic-bezier(.2,0,0,1)`; Druck = Fläche eine Stufe heller + `scale(.985)`; Einblenden = 6 px nach oben + Deckkraft, Zeilen um 20 ms gestaffelt; Auswahl in Listen springt ohne Übergang (Tastaturgefühl), nur die Fläche blendet in 90 ms; Screenwechsel als Kreuzblende ohne Verschieben; Fokus (TV) 120 ms Flächenwechsel.
- Compose: `tween(120, easing = CubicBezierEasing(.2f,0f,0f,1f))`, Auswahl `snap()` für die Position + `tween(90)` für die Fläche, `AnimatedVisibility` mit `fadeIn + slideInVertically(6.dp)`, `animateItem()` für Listenumsortierung.

## Signatur-Elemente
1. Befehlspalette: Suchzeile mit Lupe und ⌘K, darunter Zeilen mit Kachel links und Keycap rechts, erste Zeile in Auswahlfläche.
2. Keycaps überall (⌘K, ⏎, Esc, ⌘1) – kleine Verlaufsflächen mit 4 px Radius.
3. Aktionsleiste unten statt Tab-Leiste: links Kontextzahl, rechts „Aktionen ⌘K“.
4. Rotes diagonales Streifenband genau einmal ganz oben, sonst streng monochrom.
5. Flächenleiter ohne jeden Schatten, Haarlinie #242728 an jeder Kante.

## Übertragung auf eine App
- Startscreen: Streifenband + Begrüßung, dann sofort die Befehlspalette mit Vorschlagszeilen, danach Gruppen „Quellen“ und Speicher als Zeilen mit rechtsbündigem Status.
- Liste und Übersicht: Suchfeld (fokussiert, Esc rechts), Filter-Pills, danach nach Art gruppierte Befehlszeilen mit 32-px-Bildkachel, Titel, Metazeile und rechtsbündiger Gattungsangabe; die gewählte Zeile trägt ⏎.
- Detail: Rückweg als Brotkrume („‹ Bibliothek / Lissabon“), Bild im 16-px-Container mit Haarlinie, Titel mit drei Badge-Chips, weiße Pille „Diashow starten“ mit eingebetteter ⏎-Keycap, daneben drei tertiäre Icon-Knöpfe, Pill-Tabs mit Zahlen, enges Fotoraster, zum Schluss eine Palettenkarte „Musik zur Diashow“ mit Titelzeilen und Laufzeiten.
- Formulare und Einstellungen: Zeilenliste mit Beschriftung links, Wert rechts, 1-px-Trennern; Schalter klein; Hilfetexte 12 px mute unter der Zeile.
- Leere Zustände und Laden: eine Zeile Text (15 px) plus Keycap-Hinweis statt Illustration; Laden als Zeilen-Skelette in #101111, kein Spinner.
- TV: dieselbe Palette, Zeilen auf 64 px gedehnt, Fokus = Fläche #121212 + Haarlinie, Tastenkappen zeigen Fernbedienungstasten.
- Musterscreens: Start mit Streifenband und Befehlspalette, Bibliothek als gruppierte Befehlsliste mit Filter-Pills, Detail „Lissabon“ mit Haarlinien-Bildcontainer, weißer CTA-Pille mit ⏎ und Musik-Palette – alle drei mit Bereichsleiste oben und Aktionsleiste unten.

## Vermeiden
- Keine helle Variante, keine Schatten, keine Farbflächen als Hauptaktion – die Hauptaktion ist weiß.
- Gesättigte Akzente nie auf Text, Knöpfen oder Leisten, nur in Icon-Kacheln.
- Das Streifenband nicht wiederholen; nicht mehr als eine weiße Pille pro Bildschirmhöhe.
- Keine Polsterung ≥ 32 px rundum, keine Radien > 16 px außer Pills; Inter nie ohne ss03.
- Nicht mit anderen dunklen Werkzeug-Marken verwechseln: Raycast ist **reinschwarz, positiv laufend, radius 6–16 px, zeilen- und keycap-getrieben** – Warp ist warm-braun, mono-getrieben, fast rechteckig (3–4 px) und arbeitet mit vollbreiten Linien statt Kacheln; Linear setzt auf Tab-Leiste unten und große Titel.
