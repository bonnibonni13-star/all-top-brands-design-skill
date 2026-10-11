---
slug: posthog
marke: PostHog
website: https://posthog.com
ansatz: werkzeug
ansatz2: verspielt
modus: hell
aufbau: Durchgehende warme Cremebahn #eeefe9; darauf flache weiße Karten mit 1-px-Olivrand und nur 6 px Radius
navigation: Leiste oben (56 px) + Infostreifen (40 px); unten 4 Ziele, aktiv als weiße 6-px-Karte mit Haarlinie
komponenten: Versal-Eyebrow mit Haarlinie, Pastell-Hinweisband, dunkles Olivpanel mit Mono-Zeilen, gelbe Pille
icons: Lucide-Linien, Strich 1,75 px, runde Enden, 17–19 px; nie gefüllt, nie bunt
bewegung: Sachlich und kurz; Empfehlung 140 ms klein / 220 ms Screen, cubic-bezier(.3,0,.2,1), kein Federn
schrift: Eine Grotesk über die Leiter 400–800 (IBM Plex Sans → Inter); Mono für Zahlen und Zustände
---
# PostHog – Designsprache

**Kurz:** Ein freundliches Ingenieurs-Notizbuch: warme Creme statt Weiß, flache weiße Karten mit dünnem Olivrand und nur 6 px Radius, Hierarchie fast nur über Schriftgewicht und Versal-Zeilen. Genau ein lautes Element pro Bildschirm – die gelb-orange Pille. Das Gegenstück dazu ist ein dunkles Olivpanel mit Mono-Zeilen.

## Wirkung
- Charakter: sachlich, dicht, warm und ein bisschen handgezeichnet; ohne Hochglanz, ohne Effekte
- Passt zu: Werkzeugen, Dokumentation, Verwaltungs- und Statusansichten, Entwickler- und Datenapps
- Passt weniger zu: Kino-Erlebnissen, Luxus- und Modemarken, bildlastigen Bühnen

## Aufbau und Raster
- Seitenaufbau: eine einzige Cremebahn ohne Bandwechsel; Abschnitte trennt nur der Versal-Eyebrow mit Haarlinie
- Ausrichtung: strikt links; Zahlen und Zustände rechtsbündig in Mono
- Raster: 8-px-Basis mit 2/4/6-px-Feinschritten; Abstände 2/4/8/12/16/24/32, Abschnittsrhythmus 80 px (App 20–24 px)
- Dichte und Weißraum: Kartenpolster 24 px (App 14–16 px), Zeilenabstand in Listen 10–12 px, Seitenrand 16 px
- Rhythmus: Eyebrow → Karte → Eyebrow → Karte; nie zwei Karten ohne Zwischenüberschrift

## Navigation
- Website: 56-px-Cremeleiste (Menü, Suche, gelbe Pille rechts) plus darunter ein 40-px-Streifen auf #e5e7e0 mit Ankerlinks; in der Doku zusätzlich eine 240-px-Seitenspalte mit Umriss-Icons
- App: oben dieselbe 56-px-Cremeleiste (Zeichen, Titel, Lupe, Avatar) und darunter der 40-px-Infostreifen auf #e5e7e0 mit Mono-Kennzahlen. Unten 4 Ziele (Start, Bibliothek, Suche, Profil) mit Icon und 11-px-Label; **aktiv = weiße 6-px-Karte mit 1-px-Olivrand**, die sich von der Creme abhebt, Label in 700. Inaktiv ohne Fläche in #6c6e63
- TV: Seitenspalte links (240 px) mit Umriss-Icons; Fokus = weiße Karte plus 2-px-Ink-Rand

## Startscreen
- Leiste, Infostreifen mit Mono-Zahlen (Fotos, Videos, Titel, Speicher)
- Versal-Eyebrow „RÜCKBLICK“ mit Haarlinie, darunter ein blaues Pastell-Hinweisband mit Info-Icon
- Weiße Karte mit Bild, Titel, Mono-Angaben, gelber Pille und grauem Zweitknopf; eine kleine gezeichnete Vignette am Kartenrand
- Zweiter Eyebrow, dichte Liste in einer weißen Karte; dritter Eyebrow, dunkles Olivpanel mit Mono-Zeilen zu den Quellen

## Komponenten
- Buttons: Primär #f7a501 mit **dunkler** Schrift #23251d, 14 px/700, 6 px Radius, Höhe 40 px, Polster 8×16 px; Sekundär #e5e7e0 mit Ink-Schrift, gleiche Maße; Tertiär transparent mit „→“; genau eine gelbe Pille je Bildschirmhöhe
- Karten und Kacheln: weiß #ffffff, 1 px #bfc1b7, 6 px Radius, kein Schatten; Dokumentkarten in #fcfcfa; Innenzeilen trennt 1 px #dcdfd2
- Listen: dichte Zeilen in einer Karte – links 40-px-Miniatur (4 px), darüber ein Versal-Kategorie-Label, Titel 15 px/600, rechts Mono-Werte; Trennlinie #dcdfd2
- Suche und Eingabefelder: weiß, 1 px #bfc1b7, 6 px Radius, 36 px hoch, Lupe links in #6c6e63; Fokus 2 px #2c84e0 plus Fokusring `rgba(59,130,246,.5)`
- Chips, Tabs, Filter: Pille 6×14 px, Text 13 px/500; aktiv vollständig invertiert (#23251d mit weißer Schrift). Abschnittsreiter dagegen flippen auf eine weiße Karte
- Dialoge und Sheets: weißes Blatt, 6 px oben, 1 px Olivrand, kein Schatten
- Signatur-Komponenten: Versal-Eyebrow mit durchlaufender Haarlinie; Pastell-Hinweisband (blau/grün/rot/violett) mit 3-px-Farbkante links; dunkles Olivpanel #23251d mit Mono-Zeilen; gezeichnete Vignette als Randnotiz

## Icons
- Stil: feine Umrisslinien mit runden Enden (Lucide) – „gezeichnet“, nie gefüllt, nie zweifarbig
- Größe und Strich: 17–19 px bei 1,75 px Strich in Leisten und Zeilen, 20 px in Hinweisbändern, 32 px in leeren Zuständen
- Einsatz: Icons stehen immer vor Text, nie allein als Bedeutungsträger; in Hinweisbändern übernehmen sie die Rolle der Emoji-Marker der Website
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Rounded, Gewicht 300–400, Fill 0; iOS SF Symbols Light; Web Lucide (1,75) oder Phosphor `light`

## Bildsprache
- Die Marke selbst arbeitet ohne Fotografie; Bilder werden deshalb wie Abbildungen in einem Lehrbuch behandelt: innerhalb einer weißen Karte, 4 px Radius, 1 px #dcdfd2 Rand, darunter eine Mono-Zeile als Bildunterschrift
- Seitenverhältnis 16:9 im Kopf, 1:1 im Raster; Raster eng mit 6-px-Fugen
- Keine Verläufe, keine Masken, keine Filter – die Creme ringsum liefert die Wärme
- Dazu kleine, bewusst leicht krumme Strichzeichnungen (Vignetten) in den Rändern als einzige Dekoration

## Typografie-Stimme
- Eine Familie über die ganze Leiter: 400 Text, 500 Metadaten, 600 Titel, 700 Buttons und Eyebrows, 800 nur für Display 24 px mit −0,6 px
- Hierarchie entsteht aus Gewicht, nicht aus Größe: 24/800 gegen 15/600 gegen 15/400 bei Zeilenhöhe 1,5–1,71
- Versalien ausschließlich für Eyebrows und Fußzeilen-Spaltenköpfe, 12 px/700 mit 0,06 em Sperrung
- Mono (Source Code Pro → DejaVu Sans Mono) trägt alle Zahlen, Dauern, Zustände und das dunkle Panel
- Freier Ersatz: IBM Plex Sans ist frei verfügbar; sonst Inter 400–800 mit −0,5 bis −0,6 px auf Displaygrößen

## Form, Tiefe und Material
- Radien: 0 px für strukturelle Leisten und Streifen, 2 px Inline-Code, 4 px Miniaturen und Felder, **6 px für fast alles andere**, Pille nur für Filter-Chips
- Linien und Rahmen: 1 px #bfc1b7 um Karten, 1 px #dcdfd2 zwischen Zeilen, 3 px Farbkante links an Hinweisbändern
- Schatten und Ebenen: keine. Die einzige „erhöhte“ Fläche ist das invertierte dunkle Olivpanel
- Besondere Oberflächen: Creme #eeefe9 als Boden, #e5e7e0 für Streifen und Zweitknöpfe, Pastelltöne #dceaf6 / #d9eddf / #f7d6d3 / #e7d8ee nur für Hinweisbänder

## Bewegung
- Laut Datei: keine Angaben; Hover ist per Systemregel nicht dokumentiert
- Empfehlung: Dauer klein 140 ms / Screenwechsel 220 ms, Easing `cubic-bezier(.3, 0, .2, 1)`, Druck-Effekt Gelb wird #dd9001 (kein Skalieren), Einblenden ohne Versatz nur über Deckkraft, Screenwechsel als knapper Querschnitt, Fokus (TV) weiße Karte mit 2-px-Rand
- Compose: `tween(220, easing = CubicBezierEasing(.3f, 0f, .2f, 1f))`, Zustände über `animateColorAsState`, Listen ohne `animateItem()` – die Marke bewegt Inhalte nicht

## Signatur-Elemente
1. Warme Cremefläche von oben bis unten, nie Weiß als Boden
2. Flache weiße Karten mit 1-px-Olivrand und nur 6 px Radius – nirgends ein Schatten
3. Versal-Eyebrow mit durchlaufender Haarlinie als einziger Abschnittstrenner
4. Genau eine gelb-orange Pille mit dunkler Schrift je Bildschirm
5. Dunkles Olivpanel mit Mono-Zeilen als einziger „erhöhter“ Moment

## Übertragung auf eine App
- Startscreen: Leiste und Mono-Infostreifen, dann Eyebrow → Hinweisband → Karte → Eyebrow → dichte Liste → Eyebrow → dunkles Panel
- Liste und Übersicht: Suche, Filter-Pillen, danach **eine** Karte, die alle Einträge als Tabelle hält – mit Mono-Spaltenkopf, Versal-Kategorie je Zeile und rechtsbündigen Mono-Werten
- Detail: Bild als Abbildung in der Karte mit Mono-Bildunterschrift, Titel 24/800, gelbe Hauptaktion plus graue Icon-Knöpfe, Raster mit 6-px-Fugen, grünes Hinweisband für die Musik
- Formulare und Einstellungen: Felder 36 px, Beschriftung 14/500 darüber, Hilfetexte 13/500 in #6c6e63, Hinweise als Pastellband
- Leere Zustände und Laden: weiße Karte mit 32-px-Umriss-Icon, einer Zeile in 15/400 und einer gezeichneten Vignette; Platzhalter als #e5e7e0-Flächen ohne Schimmer
- TV: linke Seitenspalte mit Umriss-Icons, Inhalt als Tabelle, Fokus als weiße Karte
- Musterscreens: Start mit blauem Hinweisband und dunklem Quellen-Panel, Bibliothek als Tabellenkarte mit Mono-Spalten, Detail mit Abbildungskarte, gelber Hauptaktion und grünem Musikband

## Vermeiden
- Kein reines Weiß als Fläche und kein dunkles Vollbild-Band – die Creme ist die Marke
- Keine Schatten auf Karten; Rand statt Erhebung
- Keine zweite laute Farbe neben dem Gelb-Orange, und nie mehr als eine gelbe Pille pro Bildschirmhöhe
- Pastelltöne der Hinweisbänder nicht als Kartenflächen zweckentfremden
- Versalien nur für Eyebrows – nicht für Buttons, Titel oder Navigation
- Radien über 8 px zerstören den Ton; Pillen nur für Filter-Chips
