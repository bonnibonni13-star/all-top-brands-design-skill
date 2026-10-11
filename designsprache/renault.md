---
slug: renault
marke: Renault
website: https://www.renault.com
ansatz: plakativ
ansatz2: buehne
modus: gemischt
aufbau: Vollbreite Bänder im Wechsel Weiß → Schwarz → Sonnengelb; eckige Kacheln, Foto oben, Text darunter
navigation: Oben 56-px-Leiste mit Haarlinie; unten schwarze Leiste mit 4 Zielen, aktiv = weißer Block, Icon invertiert
komponenten: Foto-Kachel ohne Radius, Gelb-Band mit Kennzahl, Haarlinien-Zeilen, Pillen-Filter, 40-px-Quadrat-Icons
icons: Linien-Icons 20–24 px, Strich 1,75 px, eckige Enden und Gehrung (square/miter), einfarbig Schwarz bzw. Weiß
bewegung: mechanisch-knapp; Druck = Farbwechsel #ffed00 → #e6d200, kein Transform; 160/320 ms, cubic-bezier(.33,0,.2,1)
schrift: eine schmale Grotesk (NouvelR, Ersatz TeX Gyre Heros Cn), nur 400 und 700, Display 40–56 px/0,95, Versalien
---
# Renault – Designsprache

**Kurz:** Ein Katalog-System aus vollbreiten Farbbändern: Weiß zum Blättern, Schwarz zum Erzählen, Sonnengelb (#ffed00) ein- bis zweimal pro Screen für die wichtigste Aktion. Alles ist eckig (0–2 px), Tiefe entsteht durch Farbblöcke und Haarlinien statt durch Schatten. Eine einzige, schmale Schrift in nur zwei Gewichten (400/700), Display-Zeilen auf Zeilenhöhe 0,95 gestapelt – diese Disziplin ist die Signatur.

## Wirkung
- Charakter: industriell, selbstbewusst, massentauglich; hart im Kontrast, nüchtern im Detail, nie luxuriös oder verspielt.
- Passt zu: Produktkatalogen, Konfiguratoren, Shops, Medien- und Fahrzeug-Apps, allem mit großen Fotos und klaren Entscheidungen.
- Passt weniger zu: verspielten Social-Apps, weichen Wellness-Themen, datenlastigen Dashboards mit vielen Farbcodes (es gibt nur einen Akzent).

## Aufbau und Raster
- Seitenaufbau: Bänder über die volle Breite, die Fläche wechselt hart (#ffffff → #000000 → #ffed00 → #000000); kein weiches Abstufen, keine Mittelgrautöne als Hintergrund.
- Ausrichtung: durchgehend linksbündig, Text sitzt auf einer Kante; Fotos laufen randlos bis an die Bandkante.
- Raster: 4-px-Basis, Tokens 4/8/12/16/20/24/32/40 px, Bandabstand 80 px (Web) bzw. 40 px (mobil); Web max. 1440 px, Kachelraster 2-up, Fahrzeugraster 3–4-up → 2-up → 1-up.
- Dichte und Weißraum: Kachel-Innenabstand 32 px (mobil 20 px), Listenzeile 24 px oben/unten mit Haarlinie #f2f2f2, Seitenrand in der App 20 px (Empfehlung). Dichte ist erlaubt – Weißraum ist strukturell, nicht dekorativ.
- Rhythmus: Overline 10/700 → Display 32–56/700/0,95 → Fließtext 16/400 → Aktion; danach Bandwechsel.

## Navigation
- Website: weiße Leiste 60 px mit Haarlinie unten, Zeichen links, 4 Hauptziele mittig in 14,4/700, Sprache und Konto rechts; unter 1024 px Burger. Darunter eine Reihe Pillen-Chips (Radius 46, 1 px schwarz, Höhe 36) als Unterebene, mobil horizontal scrollend.
- App (Empfehlung): oben 56-px-Leiste, weiß mit 1-px-Haarlinie, links ein neutrales Zeichen + Titel 20/700 Versalien, rechts ein 40-px-Quadrat-Knopf und der runde Avatar (Ziel „Profil" auch hier). Unten eine **schwarze** Leiste (wie der stets dunkle Footer) mit 4 Zielen: Icon 22 px + Label 10/700 Versalien. Aktiv = weiß gefüllter Block 44×44, Radius 2, Icon schwarz, Label weiß 700; inaktiv Icon und Label in rgba(255,255,255,.72), Gewicht 400. Die Leiste bleibt stehen, Detailseiten ersetzen sie durch eine Aktionsleiste.
- TV: Hauptziele als Pillen-Reihe oben, Inhalte als eckiges Kachelraster; Fokus siehe Bewegung.

## Startscreen
- Schmale Kopfleiste, dann sofort eine **schwarze Bühne**: Foto 16:9 randlos, darunter im Schwarz Overline 10/700, Display 40/700/0,95 (zweizeilig gestapelt), Angabenzeile 14/400 in rgba(255,255,255,.72), dann gelber Hauptknopf neben einem weiß umrandeten Zweitknopf.
- Danach **genau ein Gelb-Band** pro Screen: Kennzahl groß (32/700), eckiger Fortschrittsbalken in Schwarz, darunter kleine Quellen-Chips mit schwarzem Rand.
- Zum Schluss ein weißes Band „Abschnitt" (24/700 Versalien, Haarlinie darüber) mit Foto-Kacheln; die Reihe ist rechts bzw. unten sichtbar angeschnitten.

## Komponenten
- Buttons: Primär #ffed00, Text #000 14,4/700 +0,144 px, Radius 2, Höhe 48, Padding 14×24; gedrückt #e6d200. Sekundär schwarz mit weißem Text, gleiche Maße. Outline hell: weiß, 1 px #000; Outline dunkel: schwarz, 1 px #fff. Quadrat-Icon-Knopf 40×40, Radius 2, 1 px Rand. Pille (Radius 46, Höhe 36, 13/700) **nur** für Filter und Unterebenen, nie als Hauptaktion.
- Karten und Kacheln: Promo-Kachel ohne Radius und ohne Schatten, Variante hell (#fff), dunkel (#000) oder gelb (#ffed00), Innenabstand 32 px. Produktkachel: Foto randlos oben (4:3 oder 1:1), Text **darunter**, nie darauf – Titel 20/700, Unterzeile 14/400 #666, ein einzelner Pfeil rechts; gelbe „NEU"-Pille unten links auf dem Foto.
- Listen: Konfigurator-Zeilen auf Weiß, 24 px oben/unten, 1-px-Haarlinie #f2f2f2 dazwischen; links optional ein eckiges 56-px-Vorschaubild, rechts Wert oder Pfeil in #666. Gruppenköpfe als 10/700-Versalzeile auf #f7f7f7.
- Suche und Eingabefelder: Feld 48 px, Radius 0, **nur unten** 1 px #000, kein Rahmen oben und seitlich; Platzhalter #8a8a8a 16/400; Fokus = Unterlinie auf 2 px (Empfehlung, Datei macht keine Angabe).
- Chips, Tabs, Filter: Pillen weiß mit 1 px #000; aktiv schwarz gefüllt mit weißem Label 700 (Füllung, nicht nur Farbe). Horizontal scrollende Reihe, rechts angeschnitten.
- Dialoge und Sheets (Empfehlung): weiße Fläche, Radius 0, 1-px-Rand #000, Titel 24/700 Versalien, Aktionen als volle Breite unten; Scrim Schwarz 60 %.
- Signatur-Komponenten: Gelb-Kachel (genau eine pro Band), Konfigurator-Zeile mit runden 56-px-Farbkreisen (die einzigen Kreise im System, aktiv mit 1-px-Ring), Produktkachel mit Text unter dem Foto, eckiger Fortschrittsbalken.

## Icons
- Stil: schlichte Linien-Icons, geometrisch und technisch, **eckige Enden und Gehrung** (`stroke-linecap: square`, `stroke-linejoin: miter`) – passend zur Rhombus-Geometrie der Marke (Empfehlung; die Datei nennt nur Pfeil, Burger, Lupe, Konto).
- Größe und Strich: 20–24 px bei 1,75 px Strich, im 40-px-Quadrat-Knopf 18 px. Nie gefüllt, nie zweifarbig, nie in Gelb.
- Einsatz: einfarbig #000 auf hellen, #ffffff auf dunklen Flächen; der nachgestellte Pfeil auf Produktkacheln ist das meistgenutzte Icon. Aktivzustände entstehen durch invertierte Flächen, nicht durch gefüllte Icons.
- Umsetzung: Compose `Icons.Sharp` bzw. Material Symbols Sharp (Gewicht 400, Füllung 0, Grad 0); iOS SF Symbols Regular ohne Füllung; Web Lucide mit `stroke-width: 1.75` und `stroke-linecap: square`.

## Bildsprache
- Fotos sind das Hauptmaterial und immer **scharfkantig** (Radius 0) – keine abgerundeten Produktbilder, keine weichen Ecken.
- Seitenverhältnisse: 16:9 für Bühnen-Bänder, 1:1 für quadratische Promo-Kacheln, 4:3 für Katalogkacheln, 2:1 für vollbreite Lifestyle-Bänder. Beim Verkleinern wird enger beschnitten, nie Letterbox.
- Kein Text auf dem Foto, kein Verlauf darüber, keine Körnung – Beschriftung steht im angrenzenden Farbband. Einzige Ausnahme: kleine Badges (NEU, Zähler).
- Atmosphärische Verläufe (Violett-Magenta-Glühen) gibt es laut Datei ausschließlich in zwei definierten Produktwelten – sonst nie.

## Typografie-Stimme
- Eine Familie für alles (NouvelR), nur 400 und 700 – 500 und 600 sind verboten, der Sprung ist das System. Display 56/40/32 px, immer 700 und Zeilenhöhe 0,95, damit mehrzeilige Titel dicht stapeln; Überschriften 24/20/18 px 700/0,95; Fließtext 16/400/1,4, Angaben 14/400/1,57, Caption 12/400, Overline 10/700.
- Buttons 14,4/700 mit +0,144 px Laufweite – kaum sichtbar, sorgt aber für die mechanische Präzision. Versalien bei Overlines, Buttons und App-Titeln; keine Kursive, keine Serifen, keine Zweitschrift.
- Freier Ersatz: Inter Tight, Manrope oder HK Grotesk Semi Condensed (laut Datei) – Display-Zeilenhöhe ausdrücklich auf 0,95 klemmen. In den Musterscreens: TeX Gyre Heros Cn (schmal, nur 400/700 – trifft den Gewichtssprung exakt).

## Form, Tiefe und Material
- Radien: 0 px für Kacheln, Fotos, Bänder, Felder; 2 px für **alle** Buttons; 3–4 px für kleine Tags; 46 px Pille nur für Filter-Chips und Badges; voll nur für Farbkreise und Avatare.
- Linien und Rahmen: 1 px #000 als tragender Rand (Buttons, Kacheln, Felder), 1 px #f2f2f2 als Haarlinie zwischen Zeilen auf Weiß, rgba(255,255,255,.16) als Entsprechung im Schwarz.
- Schatten und Ebenen: praktisch keine. Ebenen entstehen durch Farbwechsel (Stufe 1 Umriss, Stufe 2 Flächenwechsel #fff auf #f7f7f7, Stufe 3 Inversion schwarze Karte auf Weiß). Höchstens eine sehr feine Stufe (~10 %, 2–4 px) für eine schwebende Zusammenfassungsleiste.
- Besondere Oberflächen: keine Glas-, Körnungs- oder Musterflächen; die Gelbfläche ist die einzige „laute" Oberfläche und bleibt auf eine pro Band beschränkt.

## Bewegung
- Laut Datei: Druckzustand des Primärknopfs = Farbwechsel #ffed00 → #e6d200 (kein Transform, kein Schatten); die schwebende Konfigurator-Leiste ist das einzige Element mit Schatten.
- Empfehlung: klein 160 ms, Screenwechsel 320 ms, Easing `cubic-bezier(0.33, 0, 0.2, 1)` (schnell los, hart gebremst – mechanisch, nicht federnd). Einblenden: Bänder schieben 16 px von unten und blenden auf, 60 ms gestaffelt je Band; Kacheln ohne Skalierung, nur Opazität. Druck auf Kacheln: Rand wechselt von #f2f2f2 auf #000. Screenwechsel: neue Fläche schiebt als volles Farbband über die alte. Fokus (TV): 3-px-Rahmen in #ffed00 plus Inversion der Kachel, 160 ms, keine Vergrößerung.
- Compose: `tween(160, easing = CubicBezierEasing(0.33f, 0f, 0.2f, 1f))`, Screens `tween(320, …)`; `AnimatedVisibility(fadeIn() + slideInVertically { it / 12 })`; `Modifier.animateItem()`; Shared Element nur für das Foto Kachel → Bühne, ohne Eckradius-Animation.

## Signatur-Elemente
1. Harte Bandfolge Weiß → Schwarz → Gelb über die volle Breite, ohne Zwischentöne.
2. Gestapelter Display-Titel in Versalien, 700, Zeilenhöhe 0,95, direkt auf der linken Kante.
3. Genau ein gelbes Element pro Screen (Hauptknopf oder Gelb-Kachel) – Gelb immer mit schwarzem Text.
4. Foto randlos und scharfkantig, Beschriftung **unter** dem Bild, abgeschlossen durch einen einzelnen Pfeil.
5. Eckige 40-px-Quadrat-Knöpfe und Haarlinien-Zeilen; runde Formen nur als Farbkreis oder Avatar.

## Übertragung auf eine App
- Startscreen: schmale weiße Kopfleiste, darunter eine schwarze Bühne (Foto 16:9 + gestapelter Titel + Gelb-Knopf), danach ein Gelb-Band mit Kennzahl, Fortschritt und Quellen-Chips, zuletzt ein weißes Band mit angeschnittener Kachelreihe.
- Liste und Übersicht: Titel in Versalien, Feld mit bloßer Unterlinie, Pillen-Filter (aktiv schwarz gefüllt), darunter eine dichte Katalogliste mit eckigem Vorschaubild, Haarlinien und rechtsbündigem Datum; Zählzeile in 10/700-Versalien darüber.
- Detail: Foto randlos als Bühne mit drei Quadrat-Knöpfen darauf, dann schwarzes Band mit Display-Titel, Angaben, gelbem Hauptknopf und Outline-Nebenaktionen; Umschalter als Pillen, Fotoraster scharfkantig mit 2-px-Fugen; unten eine feste Leiste mit rundem Farbkreis als Musik-Hinweis.
- Formulare und Einstellungen: Konfigurator-Zeilen (24 px, Haarlinie), Wert rechts in #666, Auswahl über runde 56-px-Kreise mit Ring oder über Pillen; Hauptaktion als gelbe Leiste über die volle Breite unten.
- Leere Zustände und Laden: schwarze Fläche mit Display-Titel und einem Outline-Knopf; Laden als graue Blöcke #f2f2f2 ohne Radius, kein Schimmern (Empfehlung).
- TV: Schwarz als Grundfläche, Kacheln 4-up ohne Radius, Titel 56/700 links, Fokus siehe Bewegung.
- Musterscreens: Start mit schwarzer Rückblick-Bühne, Gelb-Band für Speicher und Quellen und angeschnittener Kachelreihe; Bibliothek als weiße Katalogliste mit Unterlinien-Suche und Pillen-Filtern; Detail als schwarze Bühne mit gestapeltem Titel, gelbem Hauptknopf, Fotoraster und Musikleiste.

## Vermeiden
- Eine zweite Akzentfarbe; Gelb auf großen Flächen, als Textfarbe oder mehrfach pro Screen; Gelb mit weißem Text.
- Runde Ecken an Fotos, Kacheln und Karten; Schatten im Katalog; Pillen als Hauptknopf.
- Gewichte 500/600, gelockerte Display-Zeilenhöhe, Zweitschrift, Kursive, Versal-Fließtext.
- Mittelgraue Abschnittsflächen, weiche Verläufe außerhalb der definierten Produktwelten, hellgrauer Text auf Weiß (#8a8a8a nur für Platzhalter).
- Text über dem Foto statt darunter; Material-Standard (FAB, farbige App-Bar, abgerundete Chips mit Füllfarbe).
