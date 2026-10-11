---
slug: nvidia
marke: NVIDIA
website: https://www.nvidia.com
ansatz: daten
ansatz2: editorial
modus: gemischt
aufbau: Schwarze Kopf- und Fußkapitel rahmen weiße Inhaltsflächen; darin Karten mit 1-px-Haarlinie im engen Raster
navigation: Oben Utility-Leiste 32 px + schwarze Hauptleiste 56 px + graue Brotkrumen; unten schwarze Leiste, aktiv grün mit 2-px-Oberkante
komponenten: Haarlinien-Karte mit grünem Eckquadrat, Versal-Etikett, Kennzahl-Kachel, Tabelle, Segment-Tabs (aktiv invertiert)
icons: solide Flächen-Icons (Font-Awesome-Sharp-Art) 18–22 px, kein Strich, Tinte oder Grün, nie zweifarbig
bewegung: sachlich, fast unbewegt; 150/250 ms, cubic-bezier(.4,0,.2,1), Druck = Grün wird dunkler, Fokus = 2 px Grün
schrift: eine Grotesk (NVIDIA-EMEA, Ersatz Inter) nur 400/700; Hierarchie aus Gewicht, Zeilenhöhe locker 1,25–1,5
---
# NVIDIA – Designsprache

**Kurz:** Ein Marketing-System, das wie technische Dokumentation gebaut ist: weiße Inhaltsflächen voller flacher Karten mit 1-px-Haarlinie, gerahmt von schwarzen Kopf- und Fußkapiteln. Genau **eine** Akzentfarbe – NVIDIA-Grün #76b900 – trägt jeden Hauptknopf, jeden Aktivzustand und das kleine grüne Eckquadrat an der Karte. Alles ist kantig (2 px Radius), die Hierarchie entsteht aus Schriftgewicht statt aus Farbe, und es gibt weder Schatten noch Verläufe.

## Wirkung
- Charakter: ingenieurhaft, sachlich, dicht; Vertrauen durch Struktur und Faktenfülle, nicht durch Wärme oder Weichheit.
- Passt zu: technischen Produkten, Dokumentation, Katalogen, Dashboards, Entwickler- und Medien-Werkzeugen, allem mit vielen gleichrangigen Einträgen.
- Passt weniger zu: verspielten Consumer-Apps, emotionalen Erzähl-Apps, Marken mit weicher, runder Formsprache.

## Aufbau und Raster
- Seitenaufbau: vorhersehbarer Wechsel Schwarz (Kopfkapitel) → Weiß (Inhalt) → Schwarz (Fuß). Im Weißen stapeln sich Abschnitte ohne Trenner im 64-px-Takt; jeder Abschnitt ist ein Kartenraster.
- Ausrichtung: linksbündig; die Bühne ist bewusst **unsymmetrisch** – Text sitzt im linken Drittel, das Bild füllt rechts.
- Raster: 8-px-Basis (2/4/8/12/16/24/32/64 px), Web max. 1280 px, Rinnen 24 px; Kartenraster 4-up → 3-up (1024) → 2-up (768) → 1-up (480). Auf dem Handy ist einspaltig bzw. 2-up die Regel.
- Dichte und Weißraum: Karteninnenabstand 24–32 px, Abschnittstakt 64 px (mobil 32 px), Bühnenkapitel 80/48 px. Luft entsteht durch den Flächenwechsel Schwarz/Weiß, nicht durch Polster.
- Rhythmus: Versal-Etikett 14/700 → Überschrift 24–36/700 → Fließtext 16/400 → grüner Pfeil-Link; dann die nächste Karte.

## Navigation
- Website: oben eine 32-px-Utility-Leiste (Schwarz, 12/400, rechtsbündig Sprache/Konto), darunter die 56–64-px-Hauptleiste (Schwarz, Zeichen links, Zielreihe mittig in 16/700, rechts Lupe und grüner Knopf). Auf Unterseiten folgt eine 48-px-Brotkrumenleiste auf #f7f7f7 in Versalien und bei Bedarf ein 56-px-Sprungband. Unter 768 px Burger und Vollbild-Schublade von rechts.
- App (Empfehlung): dieselbe schwarze Kopfzone (Utility 32 px + Leiste 56 px) plus Brotkrumen auf Unterseiten. Unten eine schwarze Leiste 76 px mit 4 Zielen: Icon 20 px + Label 11/700 Versalien; aktiv = Grün **plus** 2-px-grüne Oberkante über der Zelle und Label 700, inaktiv rgba(255,255,255,.7) in 400. Die Leiste bleibt stehen; Detailseiten ersetzen sie durch eine weiße Aktionsleiste mit Haarlinie.
- TV: schwarze Fläche, Zielreihe oben, Inhalte im 4-up-Raster; Fokus siehe Bewegung.

## Startscreen
- Bühnenkapitel in Schwarz: vollflächiges Bild mit dunklem Verlauf, Text im linken Drittel – Versal-Etikett 14/700, Überschrift 32/700 (Web 48) mit Zeilenhöhe 1,25, Unterzeile 15/400 in rgba(255,255,255,.7), dann ein grüner Hauptknopf neben einem weiß umrandeten Zweitknopf.
- Danach Weiß: eine Reihe Kennzahl-Kacheln (Zahl 28–36/700 in Grün, Beschriftung 12/400 darunter, 1-px-Haarlinie, kein Schatten).
- Dann ein Abschnitt mit Versal-Etikett und Überschrift, darunter das Kartenraster (2-up); die zweite Reihe ist angeschnitten. Keine dekorativen Trennlinien zwischen Abschnitten.

## Komponenten
- Buttons: Primär #76b900, Text #000 16/700, Radius 2, Höhe 44, Padding 11×24; gedrückt #5a8d00. Sekundär hell: transparent, **2 px grüner Rand**, Text schwarz. Sekundär dunkel: transparent, 1 px weißer Rand, Text weiß. Geist-Link: grüner Text 16/700 mit kleinem Pfeil, ohne Fläche. Deaktiviert #f7f7f7 auf #a7a7a7.
- Karten und Kacheln: weiße Fläche, 1 px #cccccc, Radius 2, kein Schatten; Bild 16:9 oben, Versal-Etikett, Titel 17/700/1,47, Beschreibung 15/400/1,67, unten der grüne Pfeil-Link. **Grünes Eckquadrat 12×12 px** an einer Ecke – das Erkennungszeichen des Systems.
- Listen: technische Tabelle – Kopfzeile in Versalien 11–14/700 auf #f7f7f7, Zeilen durch 1-px-#cccccc getrennt, Werte rechtsbündig, Zeilenhöhe 56 px; jede zweite Zeile darf auf #f7f7f7 liegen.
- Suche und Eingabefelder: weiß, 1 px #cccccc, Radius 2, Höhe 44 (Suche 40) mit Lupe links; Fokus = Rand 2 px #76b900 – das einzige Fokus-Signal im System.
- Chips, Tabs, Filter: Segment-Tabs, Radius 2, 14,4/700 +0,144 px, Padding 10×18; aktiv **invertiert** (schwarze Fläche, weißer Text), inaktiv transparent auf Tinte. Etikett-Badge: #f7f7f7, Text #1a1a1a, 14/700 Versalien, 4×10, Radius 2.
- Dialoge und Sheets (Empfehlung): weiße Fläche, Radius 2, 1 px #cccccc, Titel 24/700, Aktionen rechts unten; auf Dunkel die 5-px-Umgebungsschattierung der Sticky-Leisten.
- Signatur-Komponenten: Eckquadrat; Kennzahl-Kachel (36/700 in Grün); Brotkrumenleiste auf #f7f7f7 in Versalien; schwarze CTA-Bänder zwischen den Abschnitten; dichte Mehrspalten-Tabelle.

## Icons
- Stil: solide Flächen-Icons mit scharfen Ecken (die Marke nutzt Font Awesome 6 Pro/Sharp); keine Linien-Icons, keine zwei Stärken nebeneinander, nie zweifarbig (Empfehlung auf Basis der Datei).
- Größe und Strich: 14–22 px, im App-Chrome 18–20 px, in Merkmal-Karten 22–24 px in Grün; keine Strichstärke, da gefüllt.
- Einsatz: Chevrons als Brotkrumen- und Listen-Trenner in #757575, Lupe und Menü in Weiß auf Schwarz, Merkmals-Icons in #76b900 über dem Kartentitel. Aktivzustände nie nur per Icon-Farbe, sondern zusätzlich durch Inversion oder die 2-px-Kante.
- Umsetzung: Compose `Icons.Filled` bzw. Material Symbols Sharp (Gewicht 500, Füllung 1); iOS SF Symbols `.fill`, Gewicht Semibold; Web Phosphor Fill oder Font Awesome Solid/Sharp Solid.

## Bildsprache
- Fotos und 3D-Renderings tragen die Tiefe – es gibt keine CSS-Effekte dafür. Bühnenbilder laufen vollflächig mit dunklem Verlauf darunter, damit weißer Text sitzt.
- Seitenverhältnisse fest: 16:9 (Bühne und Karten-Vorschau), 1:1 (Produktkarte), 3:2 (Artikelkarte); mobil schwenkt die Bühne auf 4:5 Hochformat, Karten behalten ihr Verhältnis und skalieren nur.
- Radius immer 2 px, keine Rahmen um Bilder innerhalb der Karte, keine Körnung, keine Farbfilter. Raster aus Bildausschnitten mit 2-px-Fugen.

## Typografie-Stimme
- Eine Familie (NVIDIA-EMEA) in genau zwei Gewichten, 400 und 700. Ungewöhnlich flach: Zeilenhöhen bleiben locker bei 1,25–1,5, Größen springen wenig – die Hierarchie kommt fast ausschließlich aus dem Gewicht. Das gibt den Seiten einen Zeitungs-Charakter.
- Stufen: Display 48/36 (mobil 32), Überschrift 24/22/20/18, Kartentitel 17/700/1,47, Text 16/400/1,5, klein 15/400/1,67, Etikett 14/700 Versalien, Caption 12/400, Chip 11/700, Fußzeile 10/700 Versalien. Versalien nur bei Etiketten, Brotkrumen und Fußzeile – niemals bei Überschriften.
- Farbe trennt keine Textstufen: Fließtext bleibt #000000 bzw. #1a1a1a, Grün ist nur für Links auf Dunkel und Kennzahlen reserviert, Blau #0046a4 ausschließlich für Links im Fließtext.
- Freier Ersatz: Inter 400/700 (laut Datei, Abweichung ~2 %), amtlicher Rückfall Arial; Helvetica-Varianten ausdrücklich meiden.

## Form, Tiefe und Material
- Radien: 0 px für Kapitel, Leisten und Fußbereich; 1 px für dekorative Mikro-Linien; **2 px für jedes Bedienelement** – Knöpfe, Karten, Felder, Tabs, Badges; voll nur für Avatare und Social-Punkte.
- Linien und Rahmen: 1 px #cccccc als Kartenrand und Tabellenlinie auf Weiß, 1 px #5e5e5e als Trenner auf Schwarz; Sekundärknopf trägt 2 px Grün.
- Schatten und Ebenen: praktisch keine. Stufe 0 flach, Stufe 1 Haarlinie, Stufe 2 Haarlinie auf Dunkel, Stufe 3 nur `0 0 5px 0 rgba(0,0,0,.3)` an klebenden Leisten. Karten heben sich nie.
- Besondere Oberflächen: #f7f7f7 als einzige weiche Fläche (Brotkrumen, Sprungband, Etiketten, Wechselzeilen); keine Verläufe außer dem Lesbarkeits-Verlauf über Bühnenbildern.

## Bewegung
- Laut Datei: keine Hover-Zustände dokumentiert (Systempolitik). Belegt sind nur Druck (#76b900 → #5a8d00) und Fokus (2 px grüner Rand) sowie die 5-px-Schattierung an klebenden Leisten.
- Empfehlung: klein 150 ms, Screenwechsel 250 ms, Easing `cubic-bezier(0.4, 0, 0.2, 1)`; Einblenden nur als Opazität (kein Versatz, keine Skalierung), Karten 40 ms gestaffelt; Tab-Wechsel = harter Wechsel der Inversion ohne gleitende Pille; Kennzahlen zählen beim Erscheinen in 600 ms hoch; Fokus (TV) 2-px-grüner Rahmen plus grünes Eckquadrat, keine Vergrößerung.
- Compose: `tween(150, easing = CubicBezierEasing(0.4f, 0f, 0.2f, 1f))`, Screens `tween(250, …)`; `AnimatedVisibility(fadeIn())` ohne Slide; `Modifier.animateItem()`; `animateIntAsState` für Kennzahlen.

## Signatur-Elemente
1. Grünes 12-px-Eckquadrat an der Ecke jeder wiederverwendbaren Karte.
2. Weiße Karten mit 1-px-Haarlinie ohne jeden Schatten, dicht im Raster gestapelt.
3. Schwarzes Bühnen- bzw. Fußkapitel mit linksbündigem Text im ersten Drittel und vollflächigem Bild.
4. Genau ein Grün: gefüllter Hauptknopf, 2-px-grüner Rand am Zweitknopf, grüne Kennzahl, grüner Pfeil-Link.
5. Graue Versal-Bänder (Brotkrumen, Etiketten, Tabellenkopf) auf #f7f7f7 als technische Beschriftungsebene.

## Übertragung auf eine App
- Startscreen: schwarze Kopfzone aus Utility-Leiste und Hauptleiste, Bühnenkapitel mit Bild und linksbündigem Text, darunter Kennzahl-Kacheln und ein 2-up-Kartenraster mit Eckquadraten; zweite Kartenreihe angeschnitten.
- Liste und Übersicht: Brotkrumen, großer Titel, Suchfeld mit Haarlinie, Segment-Tabs (aktiv invertiert), danach eine **Tabelle** mit Versal-Kopfzeile, 56-px-Zeilen, Etikett-Badge und rechtsbündigen Werten – kein Kartenraster, sondern Dokumentations-Dichte.
- Detail: Brotkrumen, Bühnenkapitel mit Bild, Titel, Angaben und grünem Hauptknopf neben grün umrandetem Zweitknopf; darunter Segment-Tabs und ein 4-up-Bildraster mit 2-px-Fugen; feste weiße Aktionsleiste unten mit Eckquadrat.
- Formulare und Einstellungen: Felder 44 px mit 1-px-Haarlinie, Beschriftung 14/700 Versalien darüber, Fokus 2 px Grün, Gruppen als Karten mit Haarlinie; Hauptaktion grün gefüllt unten rechts.
- Leere Zustände und Laden: weiße Karte mit Haarlinie, Versal-Etikett, einem Satz 16/400 und grün umrandetem Knopf; Laden als flache #f7f7f7-Blöcke ohne Schimmern (Empfehlung).
- TV: schwarze Fläche, 4-up-Raster, Kennzahlen in Grün, Fokus siehe Bewegung.
- Musterscreens: Start mit schwarzer Bühne, grünen Kennzahl-Kacheln und Haarlinien-Karten mit Eckquadrat; Bibliothek als Dokumentations-Tabelle mit Versal-Kopf, Segment-Tabs und Etikett-Badges; Detail mit Bühne, Tabs, 4-up-Bildraster und weißer Musikleiste.

## Vermeiden
- Eine zweite Akzentfarbe oder ein anderes Grün für Knöpfe; Blau #0046a4 außerhalb von Fließtext-Links.
- Schatten an Karten, weiche Ebenen, Verläufe als Dekoration; Radien über 2 px, Pillenformen, runde Chips.
- Hierarchie über Textfarbe statt über Gewicht; Versal-Überschriften; Kursive, Serifen, Monospace.
- Symmetrisch gesetzte Bühnentexte; grün gefüllter Knopf direkt auf hellem Foto (dort den grün umrandeten Zweitknopf nehmen).
- Dekorative Trennlinien zwischen Abschnitten und zusätzliche „Luftbänder" – der Flächenwechsel ist die Trennung.
