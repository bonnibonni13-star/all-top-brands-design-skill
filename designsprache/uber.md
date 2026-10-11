---
slug: uber
marke: Uber
website: https://www.uber.com
ansatz: plakativ
ansatz2: minimal
modus: hell
aufbau: Weiße Fläche, fette satzweise Titel, 16-px-Karten; schwarze Promo-Karten als Polaritätswechsel mitten im Fluss
navigation: App-Muster der Marke: feste untere Leiste mit 4 Zielen, Icon + 12-px-Label, aktiv gefüllt und schwarz, inaktiv #afafaf
komponenten: Anfrage-Karte mit grauen 8-px-Eingabezeilen, Pillen (999 px) überall, schwarze Promo-Karte, Chip-Reihe, 36-px-Tab-Pille
icons: Empfehlung: kräftige geometrische Icons 20–24 px, nur Schwarz/Grau; aktiv gefüllt, inaktiv als Kontur
bewegung: Empfehlung: sachlich 150/260 ms, cubic-bezier(.4,0,.2,1); Druck färbt Pillen (#e2e2e2), kein Skalieren
schrift: Geometrische Display 700 satzweise, nie gesperrt; Text 400/500 bei 12–18 px, Button-Label 500
---
# Uber – Designsprache

**Kurz:** Ein Schwarz-Weiß-Duett ohne dritte Farbe: fette, satzweise Titel in einer geometrischen Display-Schrift, alles Interaktive als Pille (999 px), alle Flächen als 16-px-Karten. Rhythmus entsteht durch den Wechsel weißer und tiefschwarzer Karten, nicht durch Farbe oder Schatten.

## Wirkung
- Charakter: urban, direkt, zupackend; Großstadt-Infrastruktur, die jeder sofort bedienen kann.
- Passt zu: Alltags-, Buchungs-, Liefer-, Mobilitäts- und Medien-Apps mit klaren Hauptaktionen und großen Zielen.
- Passt weniger zu: feingliedrigen Werkzeugen mit dichten Tabellen, verspielten Marken, allem mit Farbkodierung.

## Aufbau und Raster
- Seitenaufbau: weiße Leinwand; Inhalte als gestapelte Karten mit 16 px Radius, dazwischen 24–32 px Luft; mitten im Fluss eine schwarze Promo-Karte als Polaritätswechsel, am Ende ein schwarzes Band.
- Ausrichtung: linksbündig, Titel oben links, Hauptaktion als breite Pille darunter oder am Kartenfuß.
- Raster: 4-px-Basis, Abstände 4/6/8/12/16/20/24/32; Web-Container 1200 px, Rand 32 px Desktop / 16 px mobil; Promo-Karten 2-spaltig (Bild + Text), mobil Bild oben.
- Dichte und Weißraum: innerhalb einer Karte eng (8 px zwischen Titel, Text und Aktion), zwischen Karten weit (24–32 px); Kartenrand 24 px, Formularkarte 16 px.
- Rhythmus: Karte – Luft – Karte; genau eine schwarze Pille pro sichtbarem Ausschnitt.

## Navigation
- Website: weiße Kopfleiste (16 × 32 px) mit Links in 16 px 500, rechts Hilfe, Anmelden und schwarze Pille; mobil Zeichen + Menü als Vollbild-Overlay; Fuß als tiefschwarzes Band.
- App (App-Muster der Marke, nicht in der Datei): feste weiße Leiste unten mit 1-px-Linie und 4 Zielen Start · Bibliothek · Suche · Profil; Icon 24 px plus Label 12 px; aktiv = gefülltes Icon und schwarzer Text 500, inaktiv Kontur in #afafaf (Füllung plus Gewicht, nicht nur Farbe). Oben keine zweite Leiste – der Screen beginnt mit dem Titel.
- Detailseiten: Leiste bleibt stehen; Zurück als schwebende weiße Pille mit Level-3-Schatten über dem Bild, daneben runde Icon-Knöpfe.
- TV: Reihen mit großen 16-px-Kacheln; Fokus = weiße Pille unter der Kachel plus 3-px-Rahmen, keine Vergrößerung.

## Startscreen
- Titel satzweise 32 px 700, darunter eine Zeile Text in #5e5e5e.
- Anfrage-Karte (Übertragung von `request-form-card`): weiße 16-px-Karte mit Level-2-Schatten, darin graue Eingabezeilen (#efefef, 8 px Radius, 16 px Innenabstand) mit Icon und Wert, eine graue Chip-Pille und die schwarze Hauptaktion als Pille.
- Darunter eine angeschnittene Reihe grauer Chip-Pillen (Quellen) und eine schwarze Promo-Karte mit Bild, Titel 24 px und weißer Pille.

## Komponenten
- Buttons: alles Pille 999 px – primär Schwarz mit weißem 16-px-Label 500 (12 px Innenabstand), sekundär Weiß, tertiär Grau #efefef (8 × 16 px), schwebend Weiß mit Schatten `0 2px 8px rgba(0,0,0,.16)`; Druckzustand #e2e2e2. Einzige Ausnahme: der große schwarze Formular-Knopf mit 16 px Radius.
- Karten und Kacheln: 16 px Radius für alles Flächige (Inhalt, Promo, Formular, Bildkarte), 12 px für kleinere Nebenkarten; grau getönte Karte #efefef für Nebenbereiche; schwarze Promo-Karte mit weißem Text und weißer Pille.
- Listen: Zeilen ohne Kartenrahmen, nur 1-px-Linie #e2e2e2 dazwischen; links Bild 4:3 mit 12 px Radius, Titel 16 px 500, Zusatz 14 px #5e5e5e, rechts Pfeil oder Zeitangabe.
- Suche und Eingabefelder: graue Fläche #efefef (verschachtelt #f3f3f3), 8 px Radius, 16 px Innenabstand, Text 16 px, Platzhalter #afafaf – nie rund, nie mit Rahmen.
- Chips, Tabs, Filter: Chip-Pillen 999 px in Grau mit vorangestelltem Icon (Label 14 px 500), aktiv Schwarz auf Weiß; Umschalter als 36-px-Tab-Pille: graue Schiene, aktives Feld weiß mit leichtem Schatten.
- Dialoge und Sheets: weißes Sheet mit 16 px Radius oben, 24 px Innenabstand, Hauptaktion als breite schwarze Pille am Fuß.
- Signatur-Komponenten: Anfrage-Karte mit gestapelten grauen Eingabezeilen; schwarze Promo-Karte; Chip-Reihe mit Icons; schwebende weiße Pille über Bildern; 36-px-Tab-Pille.

## Icons
- Stil (Empfehlung, die Datei nennt keine Icon-Familie): kräftige, geometrisch konstruierte Icons mit gleichmäßiger Strichstärke und wenig Detail; aktiv gefüllt, inaktiv als Kontur.
- Größe und Strich: 24 px in der Leiste, 20 px in Zeilen und Chips, 18 px in Pillen; Strich kräftig (Phosphor Bold bzw. 2 px auf 24er-Raster).
- Einsatz: immer mit Label oder in runden grauen Icon-Knöpfen (40–44 px); keine Farbe, keine Zweifarbigkeit.
- Umsetzung: Compose `Icons.Filled` für aktiv, `Icons.Outlined` für inaktiv bzw. Material Symbols Rounded, Gewicht 600, Füllung 0/1; iOS SF Symbols `.semibold`, aktiv `.fill`; Web Phosphor `ph-bold` und `ph-fill`.

## Bildsprache
- Laut Datei: redaktionelle Bilder im festen Seitenverhältnis (4:3 in Promo-Karten, 16:9 in Bühnenkarten, 4:5 bei Porträts); nie rund beschnitten, nie gekippt, Seitenverhältnis bleibt erhalten; Bilder sitzen in der 16-px-Kartenform oder randlos; Avatare quadratisch oder rund, nie abgerundetes Quadrat.
- Übertragung: Albumbild randlos 4:3 über die volle Breite oder als 16-px-Karte; Listenbilder 4:3 mit 12 px Radius; Fotoraster mit 12 px Radius und 8 px Fuge; keine Filter, keine Verläufe, Text nur auf der großen Bildkarte (unten, weiß).

## Typografie-Stimme
- Zwei Stimmen aus einer Familie: geometrische Display-Schrift ausschließlich 700 für Titel (52/36/32/24/20 px, Zeilenhöhe 1,22–1,25, nie gesperrt, immer satzweise); Text-Schrift 400/500 für Text, Buttons und Links (18/16/14/12 px).
- Keine Versalien-Titel; Versalien höchstens als seltene Eyebrow. Button-Label nie 700, sondern 500.
- App-Größen: Screen-Titel 32 px, Kartentitel 24 px, Zeilentitel 16 px 500, Zusatz 14 px #5e5e5e, Leiste 12 px.
- Freier Ersatz: Poppins 700 (hier verwendet) oder Inter 700 für Display – die Datei nennt Inter als nächsten Ersatz, der Markentext beschreibt die Schrift aber als geometrisch; Inter 400/500 für Text.

## Form, Tiefe und Material
- Radien: 0 für randlose Bänder und Bilder, 8 px Eingabezeilen, 12 px kleine Karten, 16 px kanonische Karte, 36 px Tab-Pille, 999 px alles Interaktive.
- Linien und Rahmen: nur 1-px-Trennlinien #e2e2e2 zwischen Zeilen; Karten haben keinen Rahmen, der Kontrast zur Fläche genügt.
- Schatten und Ebenen: Stufe 0 flach als Normalfall; `0 4px 16px rgba(0,0,0,.12)` für gehobene Karten, `0 4px 16px rgba(0,0,0,.16)` für die Formularkarte, `0 2px 8px rgba(0,0,0,.16)` für die schwebende Pille – sonst keine Schatten.
- Besondere Oberflächen: keine Verläufe, kein Glas, keine Körnung; die einzige „Oberfläche“ ist der Wechsel Weiß ↔ Schwarz (#000) mit Grau #efefef/#f3f3f3 als Zwischenton.

## Bewegung
- Laut Datei: keine Angaben zu Animationen; dokumentiert sind Druck- und Hover-Farben (#e2e2e2 für weiße Pillen, #282828 für die Tab-Pille).
- Empfehlung: Dauer klein 150 ms / Screenwechsel 260 ms, Easing `cubic-bezier(0.4, 0, 0.2, 1)`; Druck färbt die Fläche (Schwarz → #282828, Weiß → #e2e2e2) ohne Skalieren; Einblenden mit Deckkraft + 10 px Aufsteigen, Karten 50 ms gestaffelt; Screenwechsel als Schieben von rechts, Leiste bleibt stehen; Fokus (TV) weiße Pille in 150 ms.
- Compose: `tween(150, easing = CubicBezierEasing(0.4f, 0f, 0.2f, 1f))`, `AnimatedVisibility(fadeIn() + slideInVertically { it / 10 })`, `Modifier.animateItem()`, Druck über `indication` statt `scale`.

## Signatur-Elemente
1. Pille (999 px) als einzige Form für alles Interaktive – vom Chip bis zur Hauptaktion.
2. Anfrage-Karte: weiße 16-px-Karte mit gestapelten grauen Eingabezeilen und schwarzer Pille am Fuß.
3. Schwarze Promo-Karte mitten im weißen Fluss, mit weißem Text und weißer Pille.
4. Fette, satzweise Titel in geometrischer Display-Schrift ohne jede Laufweitenänderung.
5. Reine Schwarz-Weiß-Palette mit zwei Grautönen – Farbe kommt ausschließlich aus den Bildern.

## Übertragung auf eine App
- Startscreen: Titel, Anfrage-Karte („Diashow vorbereiten“: Album-Zeile, Musik-Zeile, Zeit-Chip, schwarze Pille), angeschnittene Chip-Reihe der Quellen, schwarze Promo-Karte für den Rückblick; feste Leiste unten.
- Liste und Übersicht: Titel, graues Suchfeld (8 px), Chip-Pillen als Filter (aktiv schwarz), danach Zeilen mit 4:3-Bild, Titel und Zusatz, 1-px-Linien, letzte Zeile angeschnitten.
- Detail: randloses 4:3-Bild mit schwebender weißer Zurück-Pille und rundem Icon-Knopf, darunter Titel 32 px, Zusatzzeile, schwarze Pille „Diashow starten“ plus graue Pillen, 36-px-Tab-Pille für Fotos · Videos · Orte, grau getönte Musikkarte, Fotoraster.
- Formulare und Einstellungen: graue Eingabezeilen untereinander in einer weißen Karte, Label über dem Wert, Absenden als breite schwarze Pille; Einstellungen als Zeilen mit Linie und Wert rechts.
- Leere Zustände und Laden: graue 16-px-Karte mit kurzem Satz 16 px und schwarzer Pille; Laden als graue Blöcke (#efefef) in Karten- und Pillenform, ohne Schimmer.
- TV: weiße Fläche mit großem Titel links, Kachelreihen 16 px; Fokus als weiße Pille mit Schatten.
- Musterscreens: Start mit Anfrage-Karte und schwarzer Rückblick-Karte, Bibliothek mit Chip-Filtern über Bildzeilen, Album „Lissabon“ mit randlosem Bild, Pillen und Tab-Umschalter.

## Vermeiden
- Eine zweite Akzentfarbe (Orange, Blau, Grün) oder farbige Zustände; Farbe gehört allein den Bildern.
- Eckige oder 16-px-Hauptaktionen (Ausnahme: großer Formular-Knopf), runde 9999-px-Karten, Pillen als Kartenform.
- Versal-Titel, gesperrte Display-Schrift, Button-Labels in 700.
- Schatten auf allen Karten, Rahmen um Karten, Verläufe als Hintergrund.
- Unterschied zu Cohere und Together AI (ebenfalls hell bzw. gemischt): hier fette geometrische Titel, Pillen und 16-px-Karten in reinem Schwarz-Weiß; dort mono-artige Riesentitel mit Korallen-Chips (Cohere) bzw. Nachtblau-Bänder mit Verlaufsband und 4-px-Rechtecken (Together AI).
