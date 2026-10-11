---
slug: bmw-m
marke: BMW M
website: https://www.bmw-m.com
ansatz: buehne
ansatz2: plakativ
modus: dunkel
aufbau: Schwarze Fläche, randlose Fotobahnen über die volle Breite, Versal-Display darüber, dazwischen Spec-Zellen.
navigation: Untere Leiste ohne Icons, 4 Versal-Labels, aktiv mit 3px M-Tricolor-Streifen über dem Ziel.
komponenten: Fotobahn, Spec-Zelle auf #0d0d0d, 4px M-Streifen, Outline-Knopf, runde 48px-Icon-Knöpfe
icons: Phosphor gefüllt (ph-fill), 16–20px, sparsam als Steuerelement – nie als Dekor
bewegung: Schnell und bremsend; 100ms klein, 300ms Screen, cubic-bezier(.16,1,.3,1), Foto zieht nach
schrift: Schmaler Versal-Display (Ersatz für BMW Type Next Latin) gegen Light 300 im Fließtext, Labels 1.5px gesperrt
---
# BMW M – Designsprache

**Kurz:** Dieselbe typografische DNA wie die Konzernmarke, aber ins Motorsportliche gedreht: fast reines Schwarz als Boden, Versalien im Display, Fotografie über die volle Breite statt Karten, und der M-Tricolor-Streifen als einziges Dekor. Das System hat keine eigene Farbspannung – die Energie kommt aus dem Bild und aus dem Kontrast zwischen schwerem Versal-Titel und sehr leichtem Fließtext.

**Unterschied zur Konzernmarke BMW:** BMW ist hell, gemessen und karten-getrieben (weiße Fläche, Fotoplatte auf `#fafafa`, blauer Rechteck-Knopf, gemischte Schreibung, 80px Bahnrhythmus). BMW M ist dunkel, plakativ und bild-getrieben (schwarze Fläche, randloses Foto als Bahn, Outline-Knopf ohne Füllung, durchgehende Versalien, 96px Bahnrhythmus, Kartenpolster 40px statt 24px). Gleiches Raster, gegensätzliche Lautstärke.

## Wirkung
- Charakter: schnell, technisch, kompromisslos; europäisch-ingenieurhaft, nicht marktschreierisch.
- Passt zu: Sport- und Fahr-Apps, Video- und Foto-Bühnen, Performance-Dashboards, Event- und Rennkalendern, Hardware-Produkten.
- Passt weniger zu: Lesetexten, Formular- und Verwaltungs-Apps, Kinder- und Community-Produkten, allem, was Wärme braucht.

## Aufbau und Raster
- Seitenaufbau: Folge von Bahnen, die den Modus wechseln – Fotobahn → Spec-Tabelle → Fotobahn → Kartenraster → Fotobahn. Zwei Textbahnen hintereinander lesen sich wie ein Konzernauftritt und sind verboten.
- Ausrichtung: links; Fotos laufen randlos von Kante zu Kante, Text sitzt in 24px Seitenrand darüber oder darunter.
- Raster: 12 Spalten, max. 1440px; Kartenraster 3er (Desktop) → 2er → 1er; Spec-Tabellen 4er → 2er → 1er.
- Dichte und Weißraum: Bahnabstand 96px, Fotobahn-Innenabstand 64px, Kartenpolster 24px, Spec-Zellen 40px; Basiseinheit 4px.
- Rhythmus: M-Streifen → Versal-Augenbraue → großer Versal-Titel → Light-Zeile → Outline-Knopf. Immer in dieser Reihenfolge.

## Navigation
- Website: schwarze 64px-Leiste oben, Menüpunkte 14px/400 mit 0.5px Laufweite in gemischter Schreibung; unter 768px Vollbild-Overlay mit M-Streifen an der Oberkante.
- App: untere Leiste, 4 Ziele (Start, Bibliothek, Suche, Profil), Höhe 72px, Fläche `#000`, 1px `#3c3c3c` oben, kein Radius. **Ohne Icons** – nur Versal-Labels 10px/700 mit 1.5px Laufweite. Aktiv: Text `#ffffff` plus 3px M-Tricolor-Streifen an der Oberkante des Ziels; inaktiv `#7e7e7e`. Detailseiten behalten die Leiste. (App-Muster abgeleitet, Empfehlung.)
- TV: Versal-Reiter oben, Fokus als 4px M-Streifen unter dem Reiter und Aufhellung der Kachel auf `#1a1a1a`; Fotokacheln skalieren 1.04.

## Startscreen
- Oben eine randlose Fotobahn über rund die Hälfte des Screens, Statusleiste liegt darauf, Verlauf nach `#000` am Fuß.
- Darauf: 4px M-Streifen (40px breit), Versal-Augenbraue, Versal-Titel 42–48px schmal, Light-Zeile, ein Outline-Knopf.
- Darunter eine Spec-Zellen-Reihe auf `#0d0d0d` (Zahlen der Bibliothek) mit senkrechten Haarlinien.
- Dann ein Abschnitt mit M-Streifen und Versal-Kopf über einer seitlich angeschnittenen Reihe randloser Fotokarten.

## Komponenten
- Buttons: primär transparent mit 1px weißem Rand, Text weiß 14px/700 Versalien mit 1.5px Laufweite, 48px hoch, Polster 16/32, Radius 0 – die Füllung fehlt bewusst. Auf hellen Flächen invertiert (schwarze Fläche, weißer Text). Druck: Fläche `#1a1a1a`.
- Karten und Kacheln: Modellkarte ohne Kartenfläche – nur Foto 16:10 auf Schwarz, darunter Versal-Titel und Light-Zeile. Feature-Karte mit Fläche `#1a1a1a`, Radius 0, Polster 24px, 16:9-Foto oben.
- Listen: Zeilen wie ein Zeitenblatt – laufende Nummer in `#7e7e7e`, breites 16:10-Thumbnail, Versal-Titel, Light-Meta, rechts ein Versal-Wert; getrennt durch 1px `#3c3c3c`.
- Suche und Eingabefelder: Fläche `#1a1a1a`, 1px `#3c3c3c`, Radius 0, 48px hoch, Text 16px/300, Platzhalter `#7e7e7e`; Fokus verdickt den Rand auf Weiß.
- Chips, Tabs, Filter: keine Chips mit Füllung. Kategorie-Reiter rein typografisch, Versalien 11–14px/700/1.5px; aktiv weiß mit 2px weißer Unterlinie, inaktiv `#bbbbbb`.
- Dialoge und Sheets: Fläche `#000` mit 1px `#3c3c3c`, Radius 0, 24px Polster, Fließtext Light 300 selbst im Rechtstext.
- Signatur-Komponenten: der 4px-M-Tricolor-Streifen, die Spec-Zelle auf `#0d0d0d` (Wert 28–32px/700 über Versal-Label), die randlose Fotobahn, runde 48px-Icon-Knöpfe auf `#1a1a1a`.

## Icons
- Stil: gefüllte, kompakte Glyphen (Phosphor `ph-fill`) – massiv wie gefräste Schalter, nie dünne Linien. (Empfehlung, die Datei beschreibt keine Icon-Familie; abgeleitet aus „industrial precision" und den runden Steuer-Knöpfen.)
- Größe und Strich: 16px inline, 18–20px in runden Knöpfen; keine Strichstärke, da gefüllt; immer weiß oder `#bbbbbb`.
- Einsatz: ausschließlich funktional – Wiedergabe, Favorit, Teilen, Mehr, Quellenstatus. In der Navigation gibt es bewusst keine Icons, dort trägt das Versal-Label allein.
- Umsetzung: Compose `Icons.Filled` bzw. Material Symbols Sharp mit Fill 1, Weight 500; iOS SF Symbols `.fill`-Varianten, Semibold; Web Phosphor `fill`.

## Bildsprache
- Fotografie ist der Inhalt, nicht die Illustration: randlos, Radius 0, 16:9 oder 21:9 im Hero, 4:5 für Porträts, nie gelettert oder beschnitten in Briefkästen.
- Über Fotos liegt nur ein Verlauf nach `#000` am Fuß (und schwach an der Oberkante für die Statusleiste), nie eine Farbfläche, nie ein Muster.
- Raster aus Bildausschnitten sitzen fugenlos (0px) – die Kante selbst ist die Linie.
- Keine Schatten, keine Rundung, keine Tönung; die Helligkeit im Bild macht die Tiefe.

## Typografie-Stimme
- Display durchgehend VERSALIEN, Gewicht 700, Zeilenhöhe 1.0–1.15, Laufweite 0; Fließtext gemischt, Gewicht 300, Zeilenhöhe 1.5. Der Sprung ist die Stimme.
- Labels, Knöpfe und Reiter: 11–14px/700 Versalien mit **1.5px Laufweite** – ohne diese Sperrung wirkt die Marke sofort beliebig.
- Größenkontrast extrem: 42–80px Display gegen 13–14px Light; kein Zwischengewicht 400/500 im Display.
- Freier Ersatz: Inter 700/300 (von der Datei genannt); für den schmaleren Motorsport-Schnitt Saira Condensed bzw. hier `TeX Gyre Heros Cn` im Display – ausdrücklich als Alternative in der Datei vorgesehen (Empfehlung).

## Form, Tiefe und Material
- Radien: 0px für alles – Knöpfe, Felder, Karten, Fotos, Spec-Zellen; 9999px ausschließlich für runde Icon-Knöpfe und Karussell-Pfeile. Dazwischen nichts.
- Linien und Rahmen: 1px `#3c3c3c` als Trenner auf Dunkel, 1px Weiß als Knopfumriss, 2px Weiß als aktive Unterlinie, 4px M-Tricolor als Bedeutungsmarke.
- Schatten und Ebenen: keine. Ebenen entstehen über `#000` → `#0d0d0d` → `#1a1a1a` → `#262626`.
- Besondere Oberflächen: Carbon-Grau `#2b2b2b` für technische Spec-Flächen, sonst keine Verläufe außer dem Foto-Fuß.

## Bewegung
- Laut Datei: keine Angaben (Übergänge ausdrücklich außerhalb des Umfangs); dokumentiert sind nur Default und Aktiv/Druck.
- Empfehlung: klein 100ms, Screenwechsel 300ms, Easing `cubic-bezier(.16,1,.3,1)` (schnell an, spät bremsend). Druck: Fläche auf `#1a1a1a`, `scale(.98)`. Einblenden: Foto skaliert von 1.06 auf 1.0, Text 16px von unten, 60ms gestaffelt. Screenwechsel: Foto bleibt stehen, Text zieht nach (Shared Element). Fokus (TV): M-Streifen wächst von links in 180ms.
- Compose: `tween(300, easing = CubicBezierEasing(.16f,1f,.3f,1f))`, Bildeinzug über `graphicsLayer{scaleX=scaleY=1.06f→1f}`, `SharedTransitionLayout` für Foto → Detail, Listen mit `animateItem()`.

## Signatur-Elemente
1. 4px M-Tricolor-Streifen (`#0066b1` → `#1c69d4` → `#e22718`) als Bedeutungsmarke – nie als Füllung oder Knopf.
2. Randlose Fotobahn mit Versal-Titel darauf, Verlauf nach Schwarz, kein Rahmen.
3. Outline-Knopf: Rechteck, 1px weiß, keine Füllung, Versal-Label mit 1.5px Sperrung.
4. Spec-Zellen auf `#0d0d0d`: großer Wert über kleinem Versal-Label, senkrechte Haarlinien.
5. Navigation ohne Icons – nur gesperrte Versal-Labels mit Tricolor-Marke.

## Übertragung auf eine App
- Startscreen: halbe Bühne als Foto mit Versal-Titel und Outline-Knopf, darunter Spec-Zellen mit den Bibliothekszahlen, darunter eine angeschnittene Fotokarten-Reihe.
- Liste und Übersicht: Versal-Titel, dunkles Suchfeld, rein typografische Reiter mit Unterlinie, danach Zeitenblatt-Zeilen mit laufender Nummer, breitem Thumbnail und rechtsbündigem Wert.
- Detail: randloses Foto über ein Drittel des Screens, Titel darauf, Spec-Zellen, Outline-Hauptknopf neben runden Icon-Knöpfen, Versal-Reiter, fugenloses Fotoraster.
- Formulare und Einstellungen: Felder auf `#1a1a1a` mit Versal-Label darüber, Trennung durch Haarlinien, Gruppenköpfe mit M-Streifen, Aktion unten als Outline-Knopf.
- Leere Zustände und Laden: gefülltes Icon 28px in `#7e7e7e`, ein Satz in 300, Outline-Knopf. Laden als `#1a1a1a`-Rechtecke ohne Schimmern.
- TV: Bühne wird Vollbild, Spec-Zellen werden zur unteren Leiste, Fokus über M-Streifen und Aufhellung.
- Musterscreens: Start als Fotobühne mit Spec-Zeile und angeschnittener Kartenreihe; Bibliothek als nummeriertes Zeitenblatt mit Versal-Reitern; Detail mit Fotobühne, Spec-Zellen, Outline-Knopf und fugenlosem Fotoraster.

## Vermeiden
- Keine gerundeten Knöpfe oder Pillen – das Rechteck ist die Marke; rund ist nur der Icon-Knopf.
- Den M-Streifen nie als Knopffüllung, Fortschrittsbalken-Farbe oder Flächenmuster verwenden.
- Keine Verlaufsflächen hinter Überschriften – die Tiefe kommt aus dem Foto, der Boden bleibt schwarz.
- Fließtext nie auf 400/500 anheben; Display nie in gemischter Schreibung setzen.
- Versal-Labels nie unter 1.5px sperren.
- Keine zusätzliche Akzentfarbe außerhalb von Tricolor und Erbe-Blau `#1c69d4`.
- Nicht zwei reine Textbahnen hintereinander – das liest sich sofort wie die helle Konzernmarke.
