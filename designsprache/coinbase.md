---
slug: coinbase
marke: Coinbase
website: https://www.coinbase.com
ansatz: daten
ansatz2: minimal
modus: gemischt
aufbau: Weiße Fläche mit Haarlinien-Listen, unterbrochen von einem tiefschwarzen Band mit schwebender Karte
navigation: Unten weiße Leiste mit Haarlinie; 4 Ziele als Icon-Knöpfe, das aktive wird zur grauen Pille mit Label
komponenten: Pillen-CTA (100 px), Werte-Zeile mit 40-px-Kreisbild und Mono-Zahlen rechts, dunkles Band mit Karte
icons: geometrische Linien-Icons, 20–24 px, Strich 1,75 px, keine Füllung; Kreisplatte #eef0f3 darunter
bewegung: ruhig und knapp; Empfehlung 160 ms klein / 280 ms Screen, cubic-bezier(.25,.1,.25,1), nur Farb- und Opazitätswechsel
schrift: eine Grotesk (Inter), Titel 32–40 px in Gewicht 400 mit −1 px Laufweite; jede Zahl in Mono 500
---
# Coinbase – Designsprache

**Kurz:** Eine institutionelle Finanzsprache: reines Weiß, fast monochrom, Haarlinien statt Schatten, und genau ein Blau (#0052ff), das pro Fläche höchstens ein- bis zweimal auftaucht. Das Unterscheidungsmerkmal ist die Typografie – große Titel stehen in **Gewicht 400**, nicht fett; dazu laufen alle Zahlen in einer Mono. Als Rhythmus wechseln helle Bänder mit einem vollflächigen, tiefschwarzen Band (#0a0b0d), in dem eine hellere Karte (#16181c) schwebt.

**Unterschied zu Kraken** (beide Krypto-Börsen): Coinbase ist ruhig, hell/dunkel geschichtet und rund – Pillen (100 px), Kreise, leichte 400er-Titel, Mono-Zahlen, keine Schatten. Kraken ist kompakt, durchgehend weiß und eckiger – 12-px-Radien ohne Pillen, fette 700er-Titel, getönte Badges und flüsternde Schatten. In Graustufen trennt sie das schwarze Band und die Kreisbilder von Kraken.

## Wirkung
- Charakter: seriös, institutionell, ruhig; „Bloomberg-Takt statt Trading-Dringlichkeit“ (Datei: 96-px-Bandrhythmus, Display in 400).
- Passt zu: Finanz-, Konto- und Portfolio-Apps, Statistik- und Verwaltungs-Apps, Sammlungen mit vielen Zahlen und Zuständen.
- Passt weniger zu: verspielten, illustrativen Apps, Kinder- und Spiele-Oberflächen, allem, was viel Farbe braucht.

## Aufbau und Raster
- Seitenaufbau: heller Kopf mit großem leichten Titel → ein dunkles Band als Blickfang mit schwebender Karte → darunter helle Haarlinien-Listen mit rechtsbündigen Zahlenspalten.
- Ausrichtung: durchgehend linksbündig; Zahlen rechtsbündig in eigener Spalte (`asset-row`).
- Raster: 4-px-Basis, Tokens 4/8/12/16/20/24/32/48/96 px; Web max. 1200 px, 12 Spalten, Karten-Innenabstand 32 px. App: 24 px Seitenrand (Empfehlung).
- Dichte und Weißraum: Bänder 96 px im Web → in der App 28–32 px zwischen Abschnitten; Listenzeile 16 px oben/unten, Karte 20–24 px innen.
- Rhythmus: hell → weich grau (#f7f7f7) → schwarz; pro Screen genau ein dunkles Band, sonst Weiß.

## Navigation
- Website: 64-px-Kopfleiste, Zeichen links, sechs Textlinks (14/500), rechts Suche, Sprache, zwei Pillen-Buttons; auf Dunkel dieselbe Leiste in #0a0b0d.
- App (Empfehlung, folgt der Pillen-Geometrie der Datei): weiße Leiste unten, 1 px #dee1e6 oben, Höhe 64 px, 4 Ziele (Start, Bibliothek, Suche, Profil) als 44-px-Icon-Knöpfe; das aktive Ziel wird zur Pille in #eef0f3 mit Icon + Label 13/600 daneben – Aktivität also über Form und Fläche, nicht über Farbe. Beim Runterscrollen bleibt die Leiste stehen.
- TV (Empfehlung): links eine schmale Spalte mit denselben vier Zielen, aktives Ziel als Pille; Inhalt rechts in Zeilen mit Zahlenspalte.

## Startscreen
- Kopf: kleine Zeile (Label + Glocke + Avatar), darunter Titel 36–40 px in Gewicht 400 mit −1 px Laufweite, darunter eine Mono-Zeile mit den Kennzahlen.
- Dann das Signatur-Band: vollflächig #0a0b0d, darin eine Karte #16181c mit 24 px Radius, Bild, Titel, Mono-Angaben und einem blauen Pillen-Button.
- Darunter auf Weiß ein bis zwei Haarlinien-Listen („Zuletzt hinzugefügt“, „Quellen“/Speicher) mit rechtsbündigen Mono-Werten; Zuwachs grün (#05b169), Rückgang rot (#cf202f) – nur als Textfarbe.

## Komponenten
- Buttons: Primär Blau #0052ff, Text weiß 16/600, Radius 100 px, Höhe 44 px (Hero-Variante 56 px, Padding 16×32); gedrückt #003ecc; deaktiviert #a8b8cc. Sekundär hell #eef0f3 mit Tintentext, dunkel #16181c mit Weiß, Outline auf Dunkel 1 px Weiß – alle in derselben Pillenform. Tertiär: blauer Text ohne Fläche.
- Karten und Kacheln: Container 24 px Radius; auf Weiß weiß mit 1 px #dee1e6, auf Schwarz #16181c ohne Rand. Innenabstand 32 px (App 20 px, Empfehlung). Genau eine Schattenstufe `0 4px 12px rgba(0,0,0,.04)` – im Standardzustand gar keine.
- Listen: `asset-row` ist die Leitkomponente – 40-px-Kreisbild links (Platte #eef0f3), Name 16/600 + Unterzeile 13/400 #7c828a, rechts Wert in Mono 16/500 und darunter eine zweite Zeile 13 muted; 1 px #dee1e6 zwischen den Zeilen, kein Kartenhintergrund.
- Suche und Eingabefelder: Suchfeld als Pille, Fläche #eef0f3, Höhe 44 px, Padding 12×20, Lupe 18 px muted. Textfeld 48 px, Radius 12 px, 1 px #dee1e6, Fokus 2 px Blau.
- Chips, Tabs, Filter: `badge-pill` – Fläche #eef0f3, Text 12/600, oft Versalien, Radius 100 px, Padding 4×12; aktiv invertiert zu schwarzer Fläche mit weißem Text (Empfehlung: Inversion statt Farbe, wie bei der hervorgehobenen Preisstufe).
- Dialoge und Sheets (Empfehlung): weißes Blatt mit 24 px oberen Ecken, Scrim Schwarz 60 %, Griff 36×4 px #dee1e6.
- Signatur-Komponenten: dunkles Band mit schwebender Produktkarte; Spaltenkopf in 11/600 Versalien +0,06 em über der Liste; Mono-Zahlenspalte; Pillen-Navigation.

## Icons
- Stil: geometrisch und minimal, reine Linien, keine Füllung, keine Duotöne; einheitliche Strichstärke über alle Größen.
- Größe und Strich: 20 px in Zeilen und Leisten, 24 px in der Navigation, 18 px in Feldern; Strich 1,75 px, runde Enden.
- Einsatz: Icons sitzen entweder auf einer runden Platte #eef0f3 (32–40 px) oder frei in Tinte/Weiß; auf Dunkel in #ffffff, sekundär #a8acb3. Blaue Icons nur dort, wo auch der blaue Button stünde.
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Outlined (Gewicht 400, Füllung 0, Grad 0); iOS SF Symbols Regular ohne Füllung; Web Lucide stroke 1.75 oder Phosphor Regular.

## Bildsprache
- Bilder sind Inhalt, nie Dekoration: im Dunkelband als Karte mit 16 px Radius innerhalb der 24-px-Karte (Karte-in-Karte, die Schichtung der Datei), auf Weiß als Kreis (40 px) in der Zeile oder als 16-px-Kachel im Raster.
- Keine Verläufe, keine Körnung, keine Texte auf dem Bild; auf Dunkel darf das Bild leicht abgedunkelt sein (Helligkeit 0,92), damit Weiß darüber ruhig bleibt.
- Der kreisrunde Bildausschnitt in Listen ist die Übertragung der runden Asset-Plättchen (Empfehlung) und das deutlichste Erkennungszeichen in Graustufen.

## Typografie-Stimme
- Eine Grotesk für alles (CoinbaseDisplay/Sans → Inter laut Datei), plus eine Mono für Zahlen (CoinbaseMono → JetBrains/Geist Mono).
- Größenkontrast ist groß, Gewicht aber klein: Titel 40/400/−1 px, Zwischentitel 32/400/−0,4 px, Abschnitt 18/600, Zeile 16/600, Text 16/400/1,5, Angaben 13/400, Badge 12/600, Spaltenkopf 11/600 Versalien.
- Display niemals fett setzen (Datei: „Don't bold display copy“); negative Laufweite nur bei 32 px und darüber, Fließtext bleibt bei 0.
- Jede Zahl in Mono 500: Zählwerte, Größen, Dauer, Prozente, Datum in Tabellenform.
- Freier Ersatz: Inter (laut Datei) + JetBrains Mono; Alternative Public Sans + IBM Plex Mono (Empfehlung).

## Form, Tiefe und Material
- Radien: 4 (Inline-Tags) / 8 (kompakte Zeilen) / 12 (Felder) / 16 (mittlere Kacheln, Bilder) / 24 (Karten, Produktkarten) / 100 px (alle Buttons, Suche, Badges) / voll (Bildkreise, Avatare). Harte Ecken kommen nicht vor.
- Linien und Rahmen: 1 px #dee1e6 als Standardtrenner, #eef0f3 für leisere; auf Dunkel rgba(255,255,255,.08). Fokus 2 px Blau.
- Schatten und Ebenen: genau eine Stufe `0 4px 12px rgba(0,0,0,.04)`; Tiefe entsteht durch Karte-auf-Karte und durch den Hell-Dunkel-Wechsel, nicht durch Schatten.
- Besondere Oberflächen: keine Verläufe, kein Glas, keine Muster – nur drei Flächenwerte: #ffffff, #f7f7f7/#eef0f3, #0a0b0d/#16181c.

## Bewegung
- Laut Datei: keine Angaben (Animationszeiten ausdrücklich außerhalb des Umfangs); dokumentiert sind nur Standard- und Druckzustand, kein Hover.
- Empfehlung: klein 160 ms / Screenwechsel 280 ms, Easing `cubic-bezier(0.25, 0.1, 0.25, 1)`; Druck nur als Farbwechsel (#0052ff → #003ecc) ohne Skalierung; Listenzeilen blenden mit 6 px von unten ein, 30 ms gestaffelt; Screenwechsel als ruhiges Überblenden; Zahlen zählen nicht hoch; Fokus (TV) 2 px Blau mit 3 px Abstand, 160 ms.
- Compose: `tween(160, easing = CubicBezierEasing(0.25f, 0.1f, 0.25f, 1f))`, `AnimatedVisibility(fadeIn() + slideInVertically { it / 12 })`, `Modifier.animateItem()`, kein `spring` mit Überschwingen.

## Signatur-Elemente
1. Ein tiefschwarzes Band (#0a0b0d) pro Screen, darin eine schwebende Karte #16181c mit 24 px Radius.
2. Große Titel in Gewicht 400 mit negativer Laufweite – leicht statt fett.
3. Mono-Zahlenspalte rechts in jeder Zeile, grün/rot nur als Textfarbe.
4. Pillen überall: Buttons, Suche, Badges, aktives Navigationsziel – daneben runde Bildkreise.
5. Blau genau ein- bis zweimal pro Fläche; sonst Weiß, Grau, Schwarz.

## Übertragung auf eine App
- Startscreen: leichter Begrüßungstitel + Mono-Kennzahlenzeile, dann das dunkle Band mit der Rückblick-Karte, darunter Haarlinien-Listen „Zuletzt hinzugefügt“ und „Speicher/Quellen“ mit Mono-Werten.
- Liste und Übersicht: Suchpille, Badge-Pillen als Filter (aktiv invertiert), Spaltenkopf in Versalien, dann Zeilen mit Kreisbild, Name, Unterzeile und rechter Mono-Spalte – Raster nur, wenn das Bild selbst der Inhalt ist.
- Detail: dunkles Band mit Zurück-Kreis, Badge-Pille, Titel in 400 und dem Bild als schwebende Karte; darunter auf Weiß die Aktionen als Pillen, Umschalter als Badge-Pillen, Fotoraster in 16-px-Kacheln und eine abschließende Zeile im Listenstil.
- Formulare und Einstellungen: weiße Liste mit Haarlinien, Felder 48 px/12 px Radius, Fokus 2 px Blau, Hauptaktion als blaue Pille unten; Werte rechts in Mono.
- Leere Zustände und Laden: zentriert, Titel 24/400, ein Satz 16/400 #5b616e, eine Pille als Aktion; Laden als graue Haarlinien-Platzhalter (#eef0f3) ohne Pulsieren.
- TV: dunkle Fläche #0a0b0d, Inhalte als Karten #16181c, Zahlen in Mono, Fokus als 2-px-Blaurahmen.
- Musterscreens: Start mit leichtem Titel, schwarzem Rückblick-Band und zwei Haarlinien-Listen; Bibliothek mit Suchpille, invertierten Filter-Pillen, Spaltenkopf und Kreisbild-Zeilen; Detail mit schwarzem Band, schwebender Bildkarte, Pillen-Aktionen und Fotoraster.

## Vermeiden
- Eine zweite Akzentfarbe oder Blau als Fläche; Grün/Rot als Buttonfarbe statt nur als Textfarbe.
- Fette Display-Titel (700+), gemischte Schriftarten in einer Überschrift, Zahlen in der Textschrift.
- Mehrere Schattenstufen, Glow, Verläufe; harte 0-px-Ecken an Bedienelementen.
- Dekorative Dunkelflächen ohne Inhalt: Das schwarze Band trägt immer eine Karte.
- Dichte Trading-Tabellen auf Einstiegsscreens – die Marke zeigt Dichte erst hinter dem Login.
