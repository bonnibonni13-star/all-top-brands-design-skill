---
slug: lamborghini
marke: Lamborghini
website: https://www.lamborghini.com
ansatz: plakativ
ansatz2: buehne
modus: dunkel
aufbau: Reines Schwarz als Leere, einzelne große Blöcke darin; Versal-Display in schmaler Schrift, alles kantig und 0px
navigation: Oben: MENU-Zeile (Hamburger links, Zeichen mittig, Icons rechts) plus Versal-Rail mit 4 Zielen, aktiv weiß + 2px Strich
komponenten: Vollbild-Bühne mit Fortschrittslinie, Sechseck-Knopf, Goldbutton 0px, Geister-Button weiß 50 %, Charcoal-Zeilen #202020
icons: Lucide-Linie, Strich 2px, eckige Enden und Gehrung, 20–22px; Sechseck als Markenform
bewegung: Nur Farb- und Deckkraftwechsel, 200ms linear/ease-out; kein Skalieren, kein Versetzen, Blenden statt Gleiten
schrift: Eine schmale Neo-Grotesk in Versalien, Gewicht 400, Zeilenhöhe 0,92–1,19, 10px-Mikrolabels mit +0,96px
---
# Lamborghini – Designsprache

**Kurz:** Eine Kathedrale aus Dunkelheit: reines Schwarz `#000000` füllt alles, und nur wenige Dinge treten als Lichtpunkte daraus hervor. Display-Typografie schreit in Versalien bei engem Zeilenabstand, Gold `#FFC000` ist die einzige Farbe und gehört allein der Hauptaktion. Keine Rundung, kein Schatten, keine Verläufe – Tiefe entsteht nur durch Flächen, die eine Stufe heller sind.

## Wirkung
- Charakter: nächtlich, theatralisch, aggressiv, kompromisslos; hart geschnitten statt fließend, Einzelstücke statt Fülle.
- Passt zu: Medien- und Event-Apps, Fahrzeug- und Produktbühnen, Launch- und Ticket-Apps, Streaming mit Kinoanspruch.
- Passt weniger zu: Formular- und Verwaltungs-Apps, datendichte Oberflächen, helle oder freundliche Produkte, alles mit vielen Kleinteilen.
- Abgrenzung zur anderen Supersportwagen-Sprache in diesem Katalog (`ferrari`): hier **hart und kantig** – reines Schwarz ohne jede helle Bahn, Versal-Display in schmaler Schrift mit Zeilenhöhe 0,92 statt ruhiger gemischter Schreibweise, Icons mit eckigen Enden und Gehrung plus Sechseck-Geometrie, Navigation oben statt unten, Bewegung nur als Blende statt filmischem Auslauf.

## Aufbau und Raster
- Seitenaufbau: Vollbild-Bühne (100 vh) mit Bild oder Video, Text und Aktionen darauf; darunter wenige, große, durch 1px `#202020` getrennte Blöcke. Dunkelheit ist der Weißraum.
- Ausrichtung: links; Marke und Hauptmotiv zentriert, Zahlen und Zeiten rechts.
- Raster: Bootstrap-12-Spalten, max. 1440px, Inhaltsbereiche 1200px; Hero bricht randlos aus. App: eine Spalte, Seitenrand 24px.
- Dichte und Weißraum: Basis 8px, Skala 2 · 4 · 5 · 8 · 10 · 12 · 15 · 16 · 20 · 24 · 32 · 40 · 48 · 56px. Abschnitt 48–56px vertikal (mobil 24px), Buttons 24px (Gold) bzw. 16px (Geist) Innenabstand.
- Rhythmus: eine Bühne, eine Aussage, viel Schwarz; nie mehrere konkurrierende Blöcke nebeneinander.

## Navigation
- Website: Kopfleiste ohne Fläche und ohne Linie, frei über dem Schwarz schwebend – „MENU“ plus Hamburger links, Zeichen mittig, Suche und Merkliste rechts; nie eine ausgeklappte horizontale Leiste.
- App: dieselbe Kopfzeile (56px) und darunter – Empfehlung, da eine App ständige Zielwechsel braucht – ein schmaler Versal-Rail mit 4 Zielen (Start · Bibliothek · Suche · Profil), 12px/400/0,96px, inaktiv `#7D7D7D`, aktiv weiß **plus** 2px weißer Strich darunter (Entscheidung: Gold gehört laut Datei ausschließlich der Hauptaktion, nie einem Zustand). Keine untere Leiste – der untere Bildrand bleibt der Bühne vorbehalten. Beide Zeilen liegen ohne Fläche über dem Hero.
- TV: Vollbild-Bühne, Fokus als 2px weißer Rahmen plus Flächenstufe `#000000` → `#202020`; kein Vergrößern, kein Schatten.

## Startscreen
- Vollbild-Bühne über zwei Drittel der Höhe: Motiv randlos, dunkler Verlauf an Ober- und Unterkante, Kopfzeile und Rail schwebend darüber.
- Darauf untereinander: graue Mikro-Marke (`#969696`, 10px Versal, 2px Radius), Display 54px Versal mit Zeilenhöhe 0,92, Angaben 12px Versal `#7D7D7D`.
- Darunter gestapelt die Aktionen: Goldbutton (`#FFC000`, schwarzer Text) über Geister-Button (1px Weiß, 50 % Deckkraft).
- Am unteren Bühnenrand: Sechseck-Knopf rechts, dünne weiße Fortschrittslinie über die volle Breite.
- Nach der Bühne ein einziger weiterer Bereich: Versal-Label mit 1px-Linie und zwei große Bildkacheln nebeneinander, rechts angeschnitten.

## Komponenten
- Buttons: alle 0px Radius. Gold `#FFC000` mit Text `#000000`, 16px/400, Innenabstand 24px, Höhe ≥ 52px, Druck `#917300`. Geister-Button transparent, 1px `#FFFFFF`, Deckkraft 0,5, 14,4px Versal/0,2px, Innenabstand 16px. Weiß gefüllt (`#FFFFFF` auf `#202020`) für helle Abschnitte, Grau `#969696` für Nebensächliches.
- Karten und Kacheln: Fläche `#202020` auf Schwarz oder randloses Foto mit Text darauf; 0px Radius, keine Schatten, Trennung über 1px `#202020`.
- Listen: dichte Zeilen mit quadratischer Miniatur 64px, Versaltitel 20px schmal, Angaben 10–12px Versal `#7D7D7D`, Zeit rechtsbündig, 1px `#202020` unter jeder Zeile. Keine Einrückung, keine Radien.
- Suche und Eingabefelder: schwarzes Feld, 1px `#7D7D7D`, 0px Radius, Höhe 52px, Platzhalter 12px Versal `#7D7D7D`.
- Chips, Tabs, Filter: keine Pillen – Versaltext nebeneinander (12px/0,96px), aktiv weiß mit 2px weißem Strich, inaktiv `#7D7D7D`; darunter eine durchgehende 1px-Linie.
- Dialoge und Sheets: `#202020` auf `rgba(0,0,0,.7)`-Überlagerung, 0px Radius, Versal-Titel, Schließen-Icon 2px eckig.
- Signatur-Komponenten: Sechseck-Knopf (Umriss, ~48px, für Wiedergabe/Pause), dünne weiße Fortschrittslinie am Bühnenrand, Mikro-Badge `#969696` mit 2px Radius, Geister-Button mit 50 % Deckkraft.

## Icons
- Stil: harte Linie, eckige Enden, Gehrung statt Rundung – dieselbe Geometrie wie die abgeschrägten Schriftterminals; Sechseck als wiederkehrende Form.
- Größe und Strich: 20px in Zeilen, 22px in der Kopfzeile, 2px Strichstärke (Empfehlung – die Datei nennt keinen Icon-Satz, aber Hexagon-Geometrie und harte Kanten); nie gefüllt.
- Einsatz: wenige, große Icons; Sechseck nur für den Wiedergabeknopf. Icons bleiben weiß oder `#7D7D7D`, nie Gold – Gold gehört der Hauptaktion.
- Umsetzung: Compose `Icons.Sharp` bzw. Material Symbols Sharp, Gewicht 400–500, Füllung 0; iOS SF Symbols `.medium`, nicht gefüllt; Web Lucide `stroke-width: 2` mit `stroke-linecap: square; stroke-linejoin: miter`.

## Bildsprache
- Vollbild und kinematografisch, 16:9 und breiter; Motive dunkel, kontrastreich, nächtlich – das Bild liefert die gesamte visuelle Reichhaltigkeit.
- Dunkle Verläufe nur an Ober- und Unterkante (`rgba(0,0,0,.75)` → transparent), damit Text trägt; zusätzlich leichte Absenkung von Helligkeit und Sättigung, damit Gold als einziger Farbpunkt bleibt.
- Kein Radius, keine Rahmen, keine Fugen: Bildraster liegen Kante an Kante als ein Block.
- Keine Porträt-Freisteller und keine runden Avatare – ein Profilbild ist ein 30px-Quadrat.

## Typografie-Stimme
- Versalien sind der Normalzustand: Display, Abschnitte, Buttons, Labels. Gemischte Schreibweise nur im Fließtext.
- Extreme Spannweite 120 / 80 / 54 / 40 / 27 / 24px gegen 10px-Mikrotext (12:1). Zeilenhöhe im Display 0,92–1,19 – Textblöcke wirken gestanzt.
- Gewicht 400 trägt die Überschriften (nie fett); schmale bis ultraschmale Schnitte bei großen Größen.
- Laufweite: Captions negativ (-0,42px bei 14px), Mikrotext positiv (+0,225px bei 10px), Labels +0,96px bei 12px.
- Freier Ersatz: Archivo Narrow, Oswald oder Roboto Condensed (Gewicht 400) für Display; Inter oder Roboto für Fließtext.

## Form, Tiefe und Material
- Radien: 0px für alles – Buttons, Karten, Bilder, Felder; 2px nur für Mikro-Badges; 20px nur für Schalter.
- Linien und Rahmen: 1px `#202020` als Abschnitts- und Zeilentrenner, 1px Weiß bei 50 % für Geister-Buttons, 1px `#7D7D7D` an Eingabefeldern.
- Schatten und Ebenen: keine Schatten. Stufen `#000000` → `#181818` → `#202020` → `#494949`; Überlagerungen `rgba(0,0,0,.7)` / `.5` / `.25`.
- Besondere Oberflächen: keine Verläufe auf UI-Flächen, keine Glanzeffekte; einzige „Textur“ ist das Foto und die dünne weiße Linie.

## Bewegung
- Laut Datei: Interaktionen sind ausdrücklich nur Farb- und Deckkraftwechsel; Skalieren oder Versetzen beim Hover ist untersagt. Konkrete Zeiten werden nicht genannt.
- Empfehlung: Dauer klein 200ms / Screenwechsel 300ms, Easing `cubic-bezier(.2, 0, 0, 1)` bzw. linear bei Deckkraft. Druck-Effekt: Gold → `#917300`, Geist 0,5 → 0,7 Deckkraft, keine Transformation. Einblenden: reines Überblenden der Bühne (300ms), Textblöcke ohne Versatz. Screenwechsel: harter Schnitt mit kurzer Schwarzblende. Fokus (TV): weißer Rahmen erscheint in 200ms ohne Skalierung.
- Compose: `tween(200, easing = LinearEasing)` für `animateColorAsState`, `Crossfade(targetState, animationSpec = tween(300))` für Screenwechsel, `AnimatedVisibility` nur mit `fadeIn()/fadeOut()`, ausdrücklich ohne `scaleIn`/`slideIn`.

## Signatur-Elemente
1. Reines Schwarz als Fläche, in der nur Weiß und ein einziger Goldpunkt existieren.
2. Versal-Display in schmaler Schrift mit Zeilenhöhe 0,92 – dichte, gestanzte Textblöcke.
3. Sechseck-Umrissknopf plus dünne weiße Fortschrittslinie am unteren Bühnenrand.
4. Scharfkantiger Goldbutton über einem Geister-Button mit 50 % weißer Kontur.
5. Keine Rundung an irgendeiner Stelle – auch Miniaturen, Felder und Profilbild sind Quadrate.

## Übertragung auf eine App
- Startscreen: Bühne über zwei Drittel der Höhe mit einem hervorgehobenen Inhalt, Versal-Titel und gestapelten Aktionen darauf; darunter genau ein weiterer Bereich mit zwei großen Kacheln.
- Liste und Übersicht: Versal-Titel, schwarzes Suchfeld mit heller Kontur, Versal-Filter mit weißem Strich, danach dichte Zeilen mit quadratischer Miniatur und rechtsbündiger Zeitangabe, getrennt durch 1px `#202020`.
- Detail: randloses Bild über die obere Hälfte mit Versal-Titel darauf, Goldbutton plus Geister-Quadrat, Versal-Umschalter, fugenloses Bildraster, unten eine Charcoal-Leiste mit Sechseck-Knopf.
- Formulare und Einstellungen: Felder 52px mit 1px `#7D7D7D`, Label 10px Versal darüber, Abschnitte nur durch 1px-Linien getrennt; Schalter sind das einzige runde Element.
- Leere Zustände und Laden: schwarze Fläche, zentrierter Versal-Satz in `#7D7D7D`, darunter ein Goldbutton; Ladeplatzhalter als `#202020`-Rechtecke, kein Schimmern.
- TV: Vollbild-Bühne mit Versal-Titel, Zeilenliste rechts, Fokus als weißer Rahmen; Fortschrittslinie bleibt als Orientierung.
- Musterscreens: Start als nächtliche Vollbild-Bühne mit Sechseck-Knopf und Fortschrittslinie; Bibliothek als dichte Versal-Zeilenliste mit weiß unterstrichenen Versal-Filtern; Detail mit randlosem Bild, Goldaktion und fugenlosem Fotoblock über einer Charcoal-Musikleiste.

## Vermeiden
- Keine weitere Akzentfarbe neben Gold; Gold nie dekorativ, nie für Icons, Linien oder Text.
- Kein Radius an Buttons, Karten, Bildern – abgerundete Ecken widersprechen der Fahrzeuglinie.
- Kein Dunkelgrau als Hauptfläche statt `#000000` und keine hellen Flächen als Grundzustand.
- Display nie gemischt schreiben und nie fett – Versalien in Gewicht 400 sind die Stimme.
- Keine Schatten (auf Schwarz wirkungslos), keine Verläufe auf Flächen, keine Skalier- oder Versatz-Animationen.
- Keine vollen, kleinteiligen Layouts: lieber ein großes Element und viel Schwarz.
