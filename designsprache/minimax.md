---
slug: minimax
marke: MiniMax
website: https://minimax.io
ansatz: plakativ
ansatz2: galerie
modus: hell
aufbau: Reinweiße Fläche mit schwarzer Typo; dazwischen vollfarbige Produktkarten mit 32-px-Radius wie Plattenhüllen
navigation: Weiße Leiste unten, 4 Ziele mit Icon + Label, aktiv = Ink plus 2-px-Unterstrich (Segment-Tab-Logik)
komponenten: Farbkarten 32 px, weiße Karten 16 px, schwarze Pillen-Buttons, Unterstrich-Tabs, Tabelle, Kennzahlen-Zeile
icons: Phosphor Bold, geometrisch, 20–22 px, einfarbig Ink/Stone; nie gefüllt, nie in Markenfarbe (Empfehlung)
bewegung: Sachlich: 150–200 ms ease, Pille wird beim Drücken Charcoal, Farbkarten blenden gestaffelt ein (Empfehlung)
schrift: Eine geometrische Grotesk für alles; Display 1,10 Zeilenhöhe mit −2 px, Text 1,50, Gewichte 400/500/600
---
# MiniMax – Designsprache

**Kurz:** Zwei Oberflächen in einem System: eine stark schwarzweiße Marketing- und Dokumentationsebene aus reinem Weiß, schwarzen Pillen-Buttons und sehr großer Display-Typografie – und mitten darin vollfarbige Produktkarten mit 32-px-Radius, die wie Plattenhüllen nebeneinander liegen. Jede Farbe steht für eine Produktlinie, nie für Dekoration. Der Radius-Kontrast (32 px bunt gegen 16 px weiß) ist das sichtbare Markenzeichen.

## Wirkung
- Charakter: selbstbewusst, technisch, fast redaktionell; ruhiger Rahmen, laute Inhalte.
- Passt zu: Medien- und Katalog-Apps mit Sammlungen, Produkt-/Modellübersichten, Preis- und Doku-Oberflächen, Dashboards.
- Passt weniger zu: warmen, gemütlichen Marken, dunklen Entertainment-Oberflächen, verspielten Illustrations-Apps.

## Aufbau und Raster
- Seitenaufbau: zentrierter Marketing-Hero (Display + Unterzeile + Button-Paar) → horizontale Reihe bunter Produktkarten → Raster weißer Kacheln → Kennzahlen-Zeile → schwarze Fußzeile. Doku-Seiten dagegen dreispaltig: Seitenleiste, Fließtext, Inhaltsverzeichnis.
- Ausrichtung: Marketing zentriert, Plattform und Doku strikt linksbündig – dieser Wechsel ist Teil der Sprache.
- Raster: 4-px-Basis mit 8-px-Schritten (4/8/12/16/20/24/32/40 px), Abschnitte 48/64/80/96 px; Inhalt max. 1280 px, 32 px Rinne; Produktmatrix 4-spaltig, auf dem Handy waagerecht scrollend.
- Dichte und Weißraum: oben großzügig (96 px), in Doku und Tabellen dicht (Zeilen 16 px Innenabstand, Seitenleiste 8 px Rhythmus). In der App: Seitenrand 16 px, Abschnittsabstand 24–28 px, Farbkarten 20–24 px innen.
- Rhythmus: große ruhige Headline → kleine graue Unterzeile → Fläche voller Farbe → wieder Weiß. Nichts dazwischen.

## Navigation
- Website: weiße Kopfleiste 64 px mit Haarlinie unten, links Wortmarke und Links, rechts schwarze Pille plus Outline-Pille; darüber bei Bedarf ein schwarzer Hinweisstreifen (promo-banner, 13 px/500 weiß). Doku-Leiste 56 px mit Suchfeld in der Mitte (8 px Radius, Fläche `#f7f8fa`).
- App (Empfehlung): oben 52–56 px – links neutrales Zeichen bzw. runder Zurück-Button (36 px, Haarlinie), Mitte optional das Suchfeld, rechts runder Icon-Button und Avatar. Unten eine weiße Leiste (72 px, 1 px Haarlinie oben, kein Schatten) mit 4 Zielen Start · Bibliothek · Suche · Profil: Icon 22 px über Label 12 px; aktiv Ink mit 2-px-Unterstrich unter dem Label und Gewicht 500, inaktiv Stone – also Strich plus Gewicht statt Farbe. Keine schwebende Pille, keine Schatten.
- Detailseiten: runder Zurück-Button links, runde Icon-Buttons rechts; Inhalts-Umschalter als Unterstrich-Tabs direkt unter der Hauptaktion; Leiste bleibt stehen.
- TV: Unterstrich-Tabs oben, Farbkarten im Raster; Fokus = 3-px-Ring in Ink plus 1,04-fache Skalierung, auf Farbkarten weißer Ring.

## Startscreen
- Optional ein schwarzer Hinweisstreifen über der Kopfleiste (13 px/500, weiß) für einen sachlichen Zustand (Speicher, Abgleich).
- Zentrierter Hero: Begrüßung in 36–40 px, Zeilenhöhe 1,10, Laufweite −1,2 px, Ink; darunter eine Kennzahlen-Zeile aus drei Zellen (Zahl 26 px/600, Label 12 px Steel), getrennt durch senkrechte Haarlinien.
- Hervorgehobener Inhalt als **Farbkarte**: volle Breite, 32 px Radius, Markenfarbe als Fläche, Bild darin als getönte Silhouette (keine eigenen Ecken), Badge-Pille oben rechts, Titel 32–40 px weiß, Unterzeile 13 px bei 80 % Weiß, weiße Pille als Aktion unten links.
- „Zuletzt hinzugefügt“ als waagerecht scrollende Produktmatrix: Farbkarten 160–180 px breit, gleiche Höhe, je eigene Markenfarbe (Koralle, Blau, Magenta, Violett, Schwarz-Foto), rechts angeschnitten.
- Weiße Karten (16 px Radius, Haarlinie) erst darunter – der Radius-Kontrast zur Farbkarte muss im selben Blick sichtbar sein.

## Komponenten
- Buttons: immer vollrund. Primär Schwarz `#0a0a0a` mit weißer Schrift 14 px/600, Padding 11 × 24 px (App 44 px hoch); Sekundär transparent mit 1 px Ink; Tertiär weiß mit 1 px Haarlinie (auch auf Farbkarten); runder Icon-Button 36 px weiß mit Haarlinie (App 44 px). Gedrückt = Charcoal `#222`.
- Karten und Kacheln: zwei Familien. **Farbkarte** 32 px Radius, Markenfarbe, 24–32 px innen, weiße Typo, eigene atmosphärische Tiefe statt Schatten. **Weiße Karte** 16 px Radius (Varianten 12/20/24 px), 1 px Haarlinie `#e5e7eb`, 20–24 px innen, flach.
- Listen: als Datentabelle – Kopfzeile auf `#f7f8fa` (13 px/600 Steel), Zeilen 56 px mit 16 px Innenabstand und 1 px `#eaecf0` als Trennung, Zahlenspalte rechtsbündig, Ganzes in 8 px Radius mit Haarlinie. Zeilenname 14 px/500 Ink, Zweitzeile 12 px Stone.
- Suche und Eingabefelder: **nicht** vollrund – 8 px Radius, Fläche `#f7f8fa` bzw. Weiß, 1 px Haarlinie, 40–44 px hoch, Text 14 px; Fokus 2 px `#1d4ed8`. Der Kontrast runder Button gegen eckiges Feld ist Absicht.
- Chips, Tabs, Filter: Unterstrich-Tabs (inaktiv Steel, aktiv Ink mit 2 px Ink unten, Padding 16 × 20 px) für Inhalts-Umschalter; Pillen-Tabs (inaktiv weiß mit Haarlinie, aktiv schwarz gefüllt) für Zeitraum- und Quellenfilter.
- Dialoge und Sheets: weißes Blatt, 20 px Radius oben, Schatten `rgba(36,36,36,.08) 0 12px 16px -4px`, Aktionen als Pillen-Paar.
- Signatur-Komponenten: Produktmatrix aus Farbkarten; Kennzahlen-Zeile; schwarzer Hinweisstreifen; Badges (Koralle „Neu“, Blassgrün „Verfügbar“, Blassblau „Beta“) vollrund, 13 px/600, 4 × 10 px.

## Icons
- Stil (Empfehlung, die Datei nennt keine Icon-Familie): geometrische Linien-Icons mit kräftigem, gleichmäßigem Strich – passend zur geometrischen Grotesk und zu den schwarzen Pillen. Ein Stil überall, nie gefüllt, nie in Markenfarbe; auf Farbkarten weiß.
- Größe und Strich: 20 px in Leisten und Buttons, 22 px in der Navigationsleiste, 16 px in Tabellenzeilen; sichtbarer Strich etwa 2 px (Phosphor Bold).
- Einsatz: in der Navigationsleiste über dem Label, sonst sparsam – die Marke erklärt lieber mit Text. Icon allein nur im runden 36-px-Button.
- Umsetzung: Compose `Icons.Rounded` bzw. Material Symbols Rounded, Gewicht 500–600, Füllung 0, 22 dp; iOS SF Symbols `.semibold`, ohne `.fill`; Web Phosphor `bold` oder Lucide `stroke-width: 2.25`.

## Bildsprache
- Laut Datei: Bilder in Farbkarten sind fotografischer Inhalt (Silhouetten, dunkle Studioporträts) **ohne eigene gerundete Rahmen**, mit internen Verläufen; Avatare rund; weiße Kacheln tragen Illustrationen oder Liniengrafiken statt Fotos.
- Übertragung: Fotos in Farbkarten werden in die Produktfarbe getönt (Luminanz des Bildes über der Markenfarbe, 40–55 % Deckkraft, darüber ein dunkler Verlauf für die Typo) und laufen randlos bis zur Kartenkante. Außerhalb der Farbkarten bleiben Bilder neutral: Raster-Fotos 12 px Radius, Thumbnails 36 px mit 6 px Radius, keine Tönung, kein Schatten.

## Typografie-Stimme
- Eine einzige geometrische Grotesk für alles – kein zweiter Schriftschnitt, keine Kursive; Betonung nur über Gewicht 400 / 500 / 600 (700 selten inline).
- Display: 80/56/40/32 px mit Zeilenhöhe 1,10 und Laufweite −2 bis −0,5 px; App-Hero 36–40 px mit −1,2 px. Zeilenhöhe nie unter 1,10 drücken.
- Text: 16/14 px bei Zeilenhöhe 1,50, Captions 13 px bei 1,70; Labels und Buttons 14 px/600, Mikro-Labels 12 px. Keine Versalien, keine Sperrung.
- Zahlen in Kennzahlen-Zellen groß (26–40 px/600) über kleinem Label – der Größensprung ersetzt Farbe.
- Freier Ersatz: DM Sans selbst (Google Fonts), sonst Poppins oder Inter; Mono nur als Systemrückfall in Code.

## Form, Tiefe und Material
- Radien: 4 px Code-Chips, 6 px kleine Steuerungen, 8 px Felder und Tabellen, 12 px Empfehlungskarten, 16 px Standardkarten, 20/24 px große Panels, **32 px Farbkarten**, vollrund für Buttons, Tabs und Badges.
- Linien und Rahmen: 1 px `#e5e7eb` als Standardrahmen, 1 px `#eaecf0` für Tabellenzeilen; Trennung geschieht über Linien und Flächenwechsel, nicht über Schatten.
- Schatten und Ebenen: Stufe 0 flach mit Haarlinie (Standard), 1 `0 1px 2px rgba(0,0,0,.04)`, 2 `0 4px 6px rgba(0,0,0,.08)`, 3 diffuses Leuchten `0 0 22px rgba(0,0,0,.08)` nur unter Farbkarten, 4 Modal `0 12px 16px -4px rgba(36,36,36,.08)`.
- Besondere Oberflächen: Farbkarten tragen interne radiale Verläufe und feine Körnung; `#f7f8fa` als stille Abschnittsfläche; schwarze Streifen und Fußzeile als harte Gegenflächen.

## Bewegung
- Laut Datei: keine Zeiten dokumentiert (Known Gaps); empfohlen werden dort 150–200 ms ease für Zustandswechsel. Zustände: Pille gedrückt Charcoal, Feld fokussiert 2 px Blau.
- Empfehlung: Dauer klein 150 ms / Screenwechsel 220 ms, Easing `cubic-bezier(0.4, 0, 0.2, 1)`; Druck-Effekt: Fläche zu Charcoal plus 0,97-fache Skalierung; Einblenden: Farbkarten 12 px von unten, 60 ms gestaffelt; Unterstrich-Tab gleitet 180 ms zur neuen Position; Screenwechsel: Überblenden ohne Versatz; Fokus (TV): Ring in 150 ms.
- Compose: `tween(150, easing = FastOutSlowInEasing)`, `AnimatedVisibility(fadeIn(tween(220)) + slideInVertically { it / 16 })`, `animateDpAsState` für den Tab-Unterstrich; keine Federn, kein Überschwingen.

## Signatur-Elemente
1. Reinweiße Fläche mit sehr großer, eng gesetzter Display-Typo – fast ohne Farbe.
2. Vollfarbige Produktkarten mit 32-px-Radius neben weißen Karten mit 16 px: der Radius- und Farbsprung im selben Blick.
3. Schwarze Pillen-Buttons als einzige dominante Aktionsform – daneben eckige 8-px-Eingabefelder.
4. Unterstrich-Tabs und Datentabellen aus der Doku-Ebene, auch in der App.
5. Kennzahlen-Zeile aus großen Zahlen über kleinen Labels, getrennt durch Haarlinien; schwarzer Hinweisstreifen über der Kopfleiste.

## Übertragung auf eine App
- Startscreen: schwarzer Hinweisstreifen, zentrierte Begrüßung mit Kennzahlen-Zeile, Rückblick als große Farbkarte, darunter die waagerechte Produktmatrix „Zuletzt hinzugefügt“ mit einer Farbe je Eintrag.
- Liste und Übersicht: linksbündiger Titel, eckiges Suchfeld, Unterstrich-Tabs als Filter, danach eine Datentabelle mit Kopfzeile, Thumbnail, Art-Badge und rechtsbündiger Zahlenspalte; Quellen als Pillen-Tabs.
- Detail: Farbkarte als Kopf (Bild in Produktfarbe getönt, Titel riesig darin), darunter schwarze Pille als Hauptaktion mit Outline-Pille und rundem Icon-Button, Unterstrich-Tabs, Fotoraster 3-spaltig mit 12 px Radius, Musik als weiße Empfehlungskarte.
- Formulare und Einstellungen: weiße Karten mit Haarlinie, Felder 8 px Radius und 44 px Höhe, Labels 14 px/500, Hilfetext 13 px Steel, Aktion als schwarze Pille unten.
- Leere Zustände und Laden: Headline 32 px, ein Satz 14 px Steel, eine schwarze Pille; Laden als Flächen in `#f7f8fa` ohne Schimmer.
- TV: Farbkarten als Raster, Unterstrich-Tabs oben, Fokusring in Ink bzw. Weiß auf Farbe.
- Musterscreens: Start als Marketing-Ebene mit Hinweisstreifen, Kennzahlen und Farbkarten; Bibliothek als Plattform-Ebene mit Unterstrich-Tabs und Datentabelle; Album „Lissabon“ als Produktseite mit blauer Farbkarte, Pillen-Paar und Fotoraster.

## Vermeiden
- Markenfarben auf normalen Buttons, Fließtext, großen Flächen oder als Deko – sie gehören nur zur Identität eines Inhalts.
- Buttons mit weniger als vollem Radius; Eingabefelder vollrund machen (sie bleiben bei 8 px).
- Eine zweite Schriftfamilie, Kursive oder Gewichte über 700.
- Display-Zeilenhöhe unter 1,10, fehlende negative Laufweite bei großen Titeln.
- Schwere Schatten auf weißen Karten; Verläufe auf Buttons; bunte Icons.
- Farbkarten mit 16 px Radius oder weiße Karten mit 32 px – der Radius-Kontrast trägt das System.
