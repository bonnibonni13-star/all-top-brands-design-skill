---
slug: x.ai
marke: xAI
website: https://x.ai
ansatz: minimal
ansatz2: werkzeug
modus: dunkel
aufbau: Fast schwarze Fläche, Inhalte als Bänder: Mono-Eyebrow, großer Titel 400, Haarlinie; Bilder klein gerahmt
navigation: Empfehlung: schwebende Umriss-Pill unten mit 3 Text-Tabs (aktiv = hellere Pill), Profil als Avatar oben
komponenten: Umriss-Pills (1 px Weiß 25 %), 8-px-Rahmen mit Haarlinie, Mono-Kennzahlen, Index-Liste mit Nummern
icons: Empfehlung: dünne Linien-Icons (Lucide 1.25), 16–20 px, weiß/grau, nie gefüllt, oft in Umriss-Kreisen
bewegung: Empfehlung: nüchterne Überblendungen 160/280 ms, cubic-bezier(.4,0,.2,1); Umriss hellt beim Drücken auf
schrift: Geometrische Grotesk nur in 400 mit negativer Laufweite; Mono-Versalien +1,2 px für Labels und Zahlen
---
# xAI – Designsprache

**Kurz:** Ein Forschungslabor, kein Werbeauftritt: fast schwarze Fläche ohne Schatten, große Titel ausschließlich in Gewicht 400 mit enger Laufweite, darüber Mono-Versal-Labels wie Code-Kommentare. Die Umriss-Pill mit 25 % Weiß ist die einzige Interaktionsform; Bilder sind kleine, gerahmte Abbildungen, Farbe taucht nur als winziges Abendrot-Detail auf.

## Wirkung
- Charakter: technisch-kosmisch, sparsam, selbstsicher; Bänder aus Text statt Bühnen aus Bildern.
- Passt zu: Werkzeug-, KI-, Forschungs-, Entwickler- und Bibliotheks-Apps; Archiv- und Medienverwaltung für Technikaffine.
- Passt weniger zu: hellen, warmen Lifestyle- oder Kinder-Apps, Shopping mit vielen Bildern, verspielten Marken.
- Abgrenzung zu Mistral AI (gleiche Branche): xAI ist kalt, dunkel, monochrom, Grotesk + Mono, alles Pill, keine Fotografie, keine Schatten; Mistral ist warm, hell/cremefarben, Serif + Inter, Buttons eckig (8 px), Sonnenuntergangs-Bilder und Streifen.

## Aufbau und Raster
- Seitenaufbau: gestapelte Bänder (Hero-, Inhaltsband) auf derselben Fläche #0a0a0a; jedes Band = Mono-Eyebrow → Titel → Inhalt, getrennt durch 1 px Haarlinie #212327 über die volle Breite.
- Ausrichtung: konsequent linksbündig; Kennzahlen in Spalten, Status rechts in Mono.
- Raster: 4-px-Basis, Abstände 2/4/8/12/16/24/32/48/64 px; Web-Container ~1200 px, Karten 2-spaltig, mobil 1-spaltig.
- Dichte und Weißraum: Bänder auf dem Web 64 px, in der App 24–28 px zwischen Haarlinie und Eyebrow; Seitenrand 24 px; Karten-Innenabstand 24 px (App 16–24).
- Rhythmus: Eyebrow 12 px → 8 px → Titel 32–48 px → 8 px → Text 14 px → 16 px → Inhalt; großer Kontrast zwischen Titelgröße und kleinem Mono.

## Navigation
- Website: schmale Leiste oben auf Canvas, Padding 12 × 24 px, Text-Links 14 px 400 in Weiß, rechts Umriss-Pills; mobil Hamburger.
- App (Empfehlung): schwebende Umriss-Pill unten mittig (30 px über dem Rand, 48 px hoch, 4 px Innenrand, 1 px Weiß 25 %) mit 3 Text-Tabs ohne Icons: Start · Bibliothek · Suche (14 px 400). Aktiv = innere Pill mit Fläche #363a3f, Umriss 45 % und weißem Text; inaktiv = grauer Text ohne Rahmen. Profil als 32-px-Avatar oben rechts mit 1-px-Ring. Die Pill bleibt stehen, Inhalte laufen per Maske davor aus.
- Detailseiten: Zurück als 40-px-Umriss-Kreis, daneben Pfad in Mono-Versalien („Bibliothek / Alben“); die Navigations-Pill wird durch eine gleich geformte Musik-Pill ersetzt.
- TV: Text-Links in einer linken Spalte; Fokus = Umriss hellt auf 60 % auf plus Fläche #1a1c20, keine Vergrößerung.

## Startscreen
- Kopf: Mono-Begrüßung links (12 px, grau), Avatar rechts; kein Logo, kein Titelbalken.
- Hero-Band: Eyebrow „Rückblick / vor einem Jahr“, Titel 48 px 400 (−1,2 px), Angaben 14 px grau, darunter das Bild als gerahmte Abbildung (8 px, 16 : 10) und zwei Umriss-Pills.
- Weitere Bänder unter Haarlinien: Kennzahlen 1.248 · 96 · 312 in Mono mit Versal-Labels; Speicher als 2-px-Linie (einziger Abendrot-Verlauf) mit Quellen-Zeilen und Mono-Status.

## Komponenten
- Buttons: Pill 9999 px, 1 px Weiß 25 %, transparent, Text 14 px 400, Padding 8 × 16 (App 40–44 px hoch); klein 4 × 12 px. Hauptaktion als einzige weiß gefüllte Pill (Text #0a0a0a) – höchstens eine pro Screen. Icon-Buttons als Umriss-Kreise 40 px.
- Karten und Kacheln: #191919, 1 px #212327, 8 px Radius, 24 px Innenabstand; keine Schatten, kein Hover-Heben.
- Listen: Index-Liste – Mono-Nummer (01, 02 …), Thumbnail 48 px mit 8 px Radius, Titel 18 px 400, darunter Mono-Versalien 11 px; Zeilen 76 px, Haarlinie über die volle Breite.
- Suche und Eingabefelder: #1a1c20, 1 px Haarlinie, 8 px Radius (nicht Pill), Padding 12 × 16, Text 16 px; Fokus: Umriss 45 % Weiß (Empfehlung).
- Chips, Tabs, Filter: Umriss-Pills 32 px; gewählt = Fläche #363a3f + Umriss 45 % (Flächenstufe statt Farbe). Umschalter ohne Rahmen für Inaktive, wie die Navigation.
- Dialoge und Sheets: Canvas mit Haarlinie und 8 px Radius, Scrim Schwarz 60 %, keine Schatten.
- Signatur-Komponenten: Mono-Eyebrow über jedem Band; Hero-Band mit riesigem 400er-Titel; Mono-Kennzahlen; Haarlinie zwischen Bändern; Umriss-Pill.

## Icons
- Stil (Empfehlung, die Datei nennt keine Icon-Sammlung): dünne, geometrische Linien-Icons, einfarbig weiß oder grau #7d8187; nie gefüllt, nie farbig.
- Größe und Strich: 16 px in Pills und Zeilen, 18–20 px in Leisten; sichtbarer Strich ca. 0,8–1 px (Lucide 1.25 auf 24er-Raster).
- Einsatz: sparsam; meist in einem Umriss-Kreis oder rechts neben Pill-Text (Pfeil schräg nach oben für „Öffnen“).
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Outlined, Gewicht 200, Füllung 0; iOS SF Symbols `.ultraLight`/`.light`; Web Lucide `stroke-width: 1.25`.

## Bildsprache
- Laut Datei: keine Fotografie auf der Website; sparsame SVG-Illustrationen für Produktmomente, Farben aus Abendrot-Orange #ff7a17, #ffc285, Dämmerungs-Violett #7c3aed, #c4b5fd, Brise-Blau #a0c3ec, Mitternacht #0d1726.
- Übertragung: Bilder als „Abbildungen“ – immer gerahmt (8 px Radius, 1 px Haarlinie innen), nie randlos, kein Text und kein Verlauf auf dem Bild, keine Filter. Hero 16 : 10, Thumbnails 48 px, Raster 3-spaltig mit 6 px Fuge. Avatare rund mit 1-px-Ring.

## Typografie-Stimme
- Zwei Stimmen: geometrische Grotesk (Universal Sans) in Gewicht 400 für alles, Mono (Geist Mono) in Versalien für Eyebrows, Labels und Kennzahlen.
- Laufweite: Titel −0,025 em (96 px −2,4; 48 px −1,2; 32 px −0,6), Zeilenhöhe 1,0 bei Displays; Text 0. Mono +1,2 px bei 12 px, +1,4 px bei 14 px.
- Größen App: Display 48, Abschnittstitel 32, Listen-Titel 18–20, Text 16/14, Mono 11–12. Nie fett – Betonung nur durch Größe und Weiß gegen Grau.
- Freier Ersatz: Inter bzw. Inter Display 400 mit −0,025 em (oder Geist); Mono Geist Mono, JetBrains Mono (Mockups: DejaVu Sans Mono).

## Form, Tiefe und Material
- Radien: 0 für randlose Bänder, 8 px für Karten, Felder und Bilder, 9999 px für jeden Button, Chip und die Navigation; rund für Avatare.
- Linien und Rahmen: 1 px #212327 zwischen Bändern und um Karten; Pill-Umriss 1 px Weiß 25 % (nie deckendes Weiß).
- Schatten und Ebenen: keine Schatten. Ebenen: #0a0a0a → #191919 (Karte) → #1a1c20 (Feld, Hover) → #363a3f (gewählt).
- Besondere Oberflächen: keine Verläufe, kein Glas, keine Körnung; Abendrot-Verlauf (#7c3aed → #ff7a17 → #ffc285) nur als winziges Illustrations-Detail (Speicherlinie, Wellenform).

## Bewegung
- Laut Datei: keine Angaben (Hover-Zustände bewusst ausgelassen).
- Empfehlung: Dauer klein 160 ms / Screenwechsel 280 ms, Easing `cubic-bezier(0.4, 0, 0.2, 1)`; Druck-Effekt: Umriss 25 % → 45 % plus Fläche #1a1c20, kein Skalieren; Einblenden: Deckkraft + 6 px Anheben, Bänder 40 ms gestaffelt; Screenwechsel: Überblenden ohne Seitwärtsbewegung; Fokus (TV): Umriss 60 % in 160 ms.
- Compose: `tween(160, easing = FastOutSlowInEasing)`, `AnimatedVisibility(fadeIn(tween(280)) + slideInVertically { it / 24 })`, `animateItem()`; kein `spring` mit Überschwingen.

## Signatur-Elemente
1. Fast schwarze Fläche #0a0a0a ohne Schatten; Bänder nur durch 1-px-Haarlinien getrennt.
2. Mono-Versal-Eyebrow (+1,2 px) über jedem Titel; Kennzahlen und Status in Mono.
3. Große Titel ausschließlich in 400 mit negativer Laufweite – nie fett.
4. Umriss-Pill mit 25 % Weiß als einzige Interaktionsform; höchstens eine weiß gefüllte Pill pro Screen.
5. Bilder klein und gerahmt; Abendrot-Verlauf nur als winziges Detail.

## Übertragung auf eine App
- Startscreen: Mono-Begrüßung + Avatar, Hero-Band mit Eyebrow, 48-px-Titel und gerahmtem Bild, Umriss-Pills; Kennzahlen- und Speicher-Band unter Haarlinien.
- Liste und Übersicht: großer Titel, 8-px-Suchfeld, Filter-Pills (gewählt = Flächenstufe), Mono-Werkzeugzeile, Index-Liste mit Nummern, Thumbnail und Mono-Angaben.
- Detail: Umriss-Kreis zurück + Mono-Pfad, Eyebrow + 48-px-Titel, Mono-Kennzahlen, gerahmtes Bild, eine weiße Pill „Diashow starten“ + Umriss-Kreise, Pill-Umschalter, 3-spaltiges Raster, Musik-Pill unten.
- Formulare und Einstellungen: Bänder mit Mono-Eyebrow, Zeilen 56 px mit Haarlinie, Werte rechts in Mono; Felder 8 px auf #1a1c20.
- Leere Zustände und Laden: ein Mono-Satz in Versalien, eine Umriss-Pill; Laden als 1-px-Linie oder blinkender Mono-Cursor, keine Illustration mit Figuren.
- TV: Text-Navigation links, Inhalte als gerahmte 8-px-Abbildungen, Fokus = Umriss hellt auf.
- Musterscreens: Start als Hero-Band mit Mono-Kennzahlen, Bibliothek als nummerierte Index-Liste, Album „Lissabon“ mit weißer Haupt-Pill und Musik-Pill.

## Vermeiden
- Helles Theme, fette Titel, Titel ohne negative Laufweite, generische Grotesk ohne angepasste Laufweite.
- Gefüllte Buttons in Serie, eckige Buttons, deckend weiße Umrisse, Schatten auf Karten.
- Verlaufs-Hero, Glühen, Atmosphäre-Hintergründe; Akzentfarben als Flächen oder für Aktiv-Zustände.
- Randlose Fotos mit Text darauf, farbige oder gefüllte Icons, klassische Tab-Leiste mit Icons.
