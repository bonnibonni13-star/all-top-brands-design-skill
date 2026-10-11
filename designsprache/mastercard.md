---
slug: mastercard
marke: Mastercard
website: https://www.mastercard.com
ansatz: editorial
ansatz2: minimal
modus: hell
aufbau: Warme Kitt-Creme-Fläche, darauf Kreise und Stadion-Pillen, asymmetrisch gesetzt mit viel Leerraum
navigation: Schwebende weiße Pille unten, 4 Kreis-Ziele, aktiv als ink-gefüllter Kreis
komponenten: Kreisporträt mit angedocktem Satelliten-Knopf, Stadion-Rahmen (40 px), Ink-Pille (20 px), Geister-Schriftzug
icons: Lucide Linie, Strich 1.5, runde Enden, 18–22 px, immer im Kreis
bewegung: Ruhig gleitend, 240/420 ms, cubic-bezier(.33,0,.1,1), Druck staucht leicht, Kreise ziehen auf ihrer Bahn
schrift: Eine geometrische Grotesk, Titel 500 mit −2 % Laufweite, Fließtext 450/400, Versalien nur im Eyebrow
---
# Mastercard – Designsprache

**Kurz:** Statt Weiß trägt eine warme Kitt-Creme die Seite, und fast nichts darauf hat eine Ecke: Kreise, Stadion-Rahmen mit 40 px und volle Pillen bestimmen jede Form. Bildinhalte sind rund maskiert, bekommen einen weißen Satelliten-Knopf an den Rand gedockt und werden von dünnen orangenen Bögen verbunden. Dazu eine einzige geometrische Grotesk im mittleren Gewicht mit enger Laufweite – editoriale Ruhe statt Banken-Dichte.

## Wirkung
- Charakter: warm-institutionell, redaktionell, langsam; Leerraum ist Struktur, nicht Rest.
- Passt zu: Marken- und Übersichtsapps, Magazin- und Portfolio-Strecken, Dienstleistungs- und Programmübersichten.
- Passt weniger zu: dichte Werkzeuge, Tabellen, Dashboards, alles mit vielen Zeilen pro Bildschirm.

## Aufbau und Raster
- Seitenaufbau: große, locker gesetzte Abschnitte auf `#F3F0EE`; pro Abschnitt ein Motiv (ein Kreis, ein Stadion-Rahmen, eine Pillen-Reihe) statt mehrerer gleichwertiger Karten.
- Ausrichtung: linksbündig, aber die Bildkreise sitzen **asymmetrisch** – mal links eingerückt, mal nach rechts versetzt. Nie ein sauberes Raster aus Kreisen.
- Raster: Basis 8 px, Stufen 8/16/24/32/48/64/96/128; Container 1200–1280 px mit 48–100 px Rinne; mobil 16–24 px Seitenrand.
- Dichte und Weißraum: Abschnittsabstand 96–128 px am Desktop, 48–64 px mobil; Kartenpolster 24–32 px. Zwischen Bildkreis und nächstem Abschnitt bleibt bewusst viel leer.
- Rhythmus: Eyebrow → Geister-Schriftzug → Bild → Titel → eine Aktion. Dann Pause.

## Navigation
- Website: weiße Pille, die 24 px unter der Fensterkante **schwebt**, Radius 999 px, Polster 16/40 px, Schatten `rgba(0,0,0,.04) 0 4px 24px`, höchstens sechs Links, Suche als 48-px-Kreis rechts.
- App: dieselbe Pille unten, 20 px über dem Rand, 16 px seitlich, Höhe 68 px, Radius 999 px, 4 Ziele (Start, Bibliothek, Suche, Profil) als 44-px-Kreise. Aktiv: Kreis in Ink `#141413` gefüllt, Icon in Creme, Label nur beim aktiven Ziel – Form statt Farbe. Beim Scrollen bleibt sie schwebend. Oben eine zweite Pille mit Marke links und Suchkreis rechts. Details ersetzen die Pille durch einen weißen Zurück-Kreis auf dem Bild.
- TV: obere Pillen-Leiste, Fokus als ink-gefüllter Kreis mit 1.06-Skalierung.

## Startscreen
- Eyebrow mit orangenem Punkt, dahinter ein Geister-Schriftzug in `#E8E2DA` (cremefarben auf Creme, 48–72 px), der rechts aus dem Bild läuft.
- Darüber gelegt das Kreisporträt (200–230 px) mit weißem Satelliten-Knopf unten rechts, der zu ~40 % über den Kreisrand ragt; ein dünner orangener Bogen führt zum nächsten Abschnitt.
- Darunter Titel 24 px/500 und eine einzige Ink-Pille. Weiter unten eine Reihe Stadion-Pillen als Hochformat-Kacheln.

## Komponenten
- Buttons: Primär = Ink `#141413`, Text in Creme `#F3F0EE`, Radius 20 px, Polster 10/24 px, 16 px/500, Laufweite −0.32 px. Sekundär = weiß mit 1.5 px Ink-Rahmen, gleiche Form. Satellit = weißer Kreis 50–56 px mit Pfeil. Orange `#CF4500` **nur** für Zustimmung/Rechtliches.
- Karten und Kacheln: drei Formen, nichts dazwischen – Kreis (50 %), Stadion-Rahmen (40 px) und volle Pille (999 px). Pillen-Kachel im Hochformat mit randlosem Bild und weißem Chip darin.
- Listen: Zeilen ohne Kasten; links ein 56–60 px **rundes** Bild, Mitte Titel 17 px/500 und Unterzeile 14 px/400 in `#696969`, rechts ein 36-px-Kreis mit Pfeil. Trennung durch 1 px `#E3DED9`, nie durch Schatten.
- Suche und Eingabefelder: Pille (999 px), weiß, 1 px Ink bei 50 % Deckkraft, Polster 12/24 px; eingeklappt nur ein 48-px-Kreis mit Lupe.
- Chips, Tabs, Filter: volle Pillen, 36–38 px hoch. Inaktiv weiß mit Haarlinie, aktiv Ink-Fläche mit Creme-Schrift.
- Dialoge und Sheets: weißes Sheet mit 40 px Radius oben, Schatten `rgba(0,0,0,.08) 0 24px 48px`, Aktionen als Ink-Pille plus Umriss-Pille.
- Signatur-Komponenten: Kreisporträt + Satellit; Geister-Schriftzug hinter Bildern; orangene Umlaufbögen (1–1.5 px, `#F37338`) zwischen Kreisen; Eyebrow aus Punkt + Versalien.

## Icons
- Stil: feine Linien-Icons mit gleichmäßiger Stärke und runden Enden (Lucide); geometrisch, nie gefüllt, nie zweifarbig.
- Größe und Strich: 18–22 px bei `stroke-width: 1.5`; im 36–48-px-Kreis zentriert.
- Einsatz: Navigation, Pfeil im Satelliten, Aktionskreise. Keine Icons in Fließtext, keine Icon-Listen.
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Rounded, Gewicht 300, Füllung 0; iOS SF Symbols `.light`/`.regular`, ungefüllt; Web Lucide `stroke-width: 1.5`.

## Bildsprache
- Quadratische Vorlagen werden **kreisrund** maskiert – das ist die Grundregel, keine abgerundeten Rechtecke für Inhaltsbilder.
- Zweite Form: der Stadion-Rahmen mit 40 px Radius für Vollbreiten-Aufmacher (16:9 oder breiter) und die Hochformat-Pille (3:4) für Reihen.
- Warme Motive bevorzugt; Ränder dürfen weich in die Creme auslaufen. Keine Verläufe über dem Bild, keine Farbfilter.
- Der Satelliten-Knopf ist Teil der Bildbehandlung: Jeder Bildkreis, der zu etwas führt, bekommt ihn unten rechts.

## Typografie-Stimme
- Eine Schrift für alles: geometrische Grotesk. Titel 500 mit −2 % Laufweite; H1 64/64 (1:1), H2 36/44, H3 24/28.8.
- Fließtext 16 px im Halbschritt-Gewicht 450 (ersatzweise 400 mit −0.5 % engerer Laufweite), Zeilenhöhe 1.4.
- Eyebrow 11–14 px/700, Versalien, +4 % Laufweite, davor ein 5-px-Punkt in `#CF4500`. Versalien **nur** hier.
- Zeilenhöhe sinkt mit der Größe: Display 1.0, H3 1.2, Text 1.4.
- Freier Ersatz: **Sofia Sans** (nächste Verwandtschaft), sonst **Poppins** oder **Inter** mit den Gewichten 400/500/700.

## Form, Tiefe und Material
- Radien: 3–6 px nur für Mikro-Elemente, **20 px** für Buttons, **40 px** für Stadion-Rahmen und große Flächen, 50 % für Kreise, 999 px für Pillen. Die Stufen 8–16 px fehlen bewusst.
- Linien und Rahmen: 1.5 px Ink an Pillen-Buttons, 1 px bei niedriger Deckkraft an Feldern und Trennern; orange Bögen mit 1–1.5 px.
- Schatten und Ebenen: Stufe 1 `rgba(0,0,0,.04) 0 4px 24px` für die schwebende Pille, Stufe 2 `rgba(0,0,0,.08) 0 24px 48px` für gehobene Kacheln. Immer großer Weichzeichner, höchstens 10 % Deckkraft, nie harte Kanten.
- Besondere Oberflächen: drei Flächentöne im Wechsel – Creme `#F3F0EE` → gehobene Creme `#FCFBFA` → Ink `#141413`; dazu der Geister-Schriftzug als „gepresstes Papier“.

## Bewegung
- Laut Datei: keine Animationswerte; Buttons zeigen Druck als leichtes Stauchen statt Hover, Bilder laden mit cremefarbenem Weichzeichner-Übergang.
- Empfehlung: klein 240 ms / Screenwechsel 420 ms, Easing `cubic-bezier(.33,0,.1,1)`. Druck: `scale(.98)`. Einblenden: Kreise wachsen von 0.94 auf 1 mit Deckkraft, Bögen zeichnen sich über 600 ms (`stroke-dashoffset`). Screenwechsel: weiches Überblenden, kein Schieben. Fokus (TV): Kreis wächst, Bogen leuchtet auf.
- Compose: `tween(240, easing = CubicBezierEasing(.33f,0f,.1f,1f))`, `AnimatedVisibility` mit `scaleIn(initialScale = .94f) + fadeIn`, Shared-Element vom Listenkreis zum Detail-Stadion.

## Signatur-Elemente
1. Kitt-Creme statt Weiß als Grundfläche – kein Screen ist rein weiß.
2. Kreisrund maskierte Bilder mit angedocktem weißem Satelliten-Knopf.
3. Dünne orangene Umlaufbögen zwischen Kreisen.
4. Geister-Schriftzug in Creme-auf-Creme hinter dem Bild.
5. Nur drei Radien: 20 px Button, 40 px Stadion, 999 px/50 % Pille und Kreis.
6. Eyebrow aus orangenem Punkt plus Versalien mit weiter Laufweite.

## Übertragung auf eine App
- Startscreen: schwebende Pille oben, dann ein einziger großer Bildkreis mit Geister-Schriftzug und Satellit, Titel, eine Ink-Pille – darunter eine Reihe Hochformat-Pillen. Mehr nicht.
- Liste und Übersicht: zwei versetzte Spalten aus Bildkreisen (zweite Spalte um ~34 px tiefer), Titel und Angaben darunter, orangene Bögen dazwischen. Alternativ Zeilen mit rundem Bild und Pfeilkreis rechts.
- Detail: Stadion-Rahmen mit 40 px über die volle Breite, weiße Kreis-Knöpfe darauf, darunter Eyebrow, Titel, Ink-Pille und Umriss-Kreise; Inhalt als Kreis-Raster.
- Formulare und Einstellungen: Pillen-Felder untereinander, Label als Eyebrow darüber, Abschluss mit Ink-Pille und Umriss-Pille nebeneinander.
- Leere Zustände und Laden: cremefarbener Kreis mit dünnem Umriss statt Illustration, Text 16 px/450 darunter; Laden als gehobene Creme-Kreise ohne Schimmer.
- TV: obere Pillen-Leiste, Inhalte als große Kreise in versetzten Reihen.
- Musterscreens: Start mit Geister-Schriftzug, Bildkreis samt Satellit und Hochformat-Pillen; Bibliothek als versetztes Kreis-Feld mit orangenen Bögen; Detail mit 40-px-Stadion-Bild, Ink-Pille und Kreis-Raster.

## Vermeiden
- Kein reines Weiß als Fläche, keine Radien zwischen 8 und 16 px – beides lässt das System sofort generisch wirken.
- Inhaltsbilder nie als abgerundete Rechtecke und nie in einem exakten Kreis-Raster; die Asymmetrie ist der Punkt.
- Signalorange nie für Marketing-Aktionen; es ist die Farbe für Zustimmung und Recht.
- Keine zweite Schriftart, keine Versalien über 14 px, keine harten oder engen Schatten.
- Den Punkt vor dem Eyebrow nicht weglassen und den Satelliten-Knopf nicht vergessen.
- Nicht mit Wise verwechseln: Mastercard setzt Kreise und volle Pillen mit viel Leerraum und mittlerem Schriftgewicht; Wise stapelt rechteckige 24-px-Blöcke dicht und schreibt Titel im Gewicht 900.
