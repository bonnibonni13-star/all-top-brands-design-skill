---
slug: ferrari
marke: Ferrari
website: https://www.ferrari.com
ansatz: buehne
ansatz2: editorial
modus: gemischt
aufbau: Kinoformat-Bild füllt das obere Drittel randlos, darunter ruhige Redaktionsbahnen auf Fast-Schwarz #181818, Listen als weiße Bahn
navigation: Unten feste Leiste, 4 Ziele, Versal-Mikrolabel 11px/1,1px, aktiv weiß + 2px Rosso-Strich; Profil zusätzlich über Avatar
komponenten: Randloses Kinobild, scharfe 0px-CTA in Rosso, Kennzahl-Zellen 34–44px/700, Haarlinien-Zeilen, weiße Listenbahn, Versal-Pillen
icons: Lucide-Linie, Strich 1,25px, runde Enden, 20–22px, nie gefüllt – fein und fließend neben schwerer Typo
bewegung: Langsam und filmisch; 160ms klein / 420ms Screen, cubic-bezier(.33,0,.1,1), Bild zoomt beim Auftritt, Text steigt gestaffelt
schrift: Eine Sans (Inter als FerrariSans-Ersatz); Display 500 mit -1,6px bis -0,36px, Versal-Labels 600/1,1px, Body 400
---
# Ferrari – Designsprache

**Kurz:** Eine Luxus-Magazinsprache für ein Automobil: das randlose Kinofoto trägt die Seite, die Typografie bleibt zurückhaltend (Display immer Gewicht 500, nie fett). Alles ist scharfkantig (0px Radius), Tiefe entsteht durch Foto und Helligkeitsstufe statt durch Schatten. Rosso Corsa `#da291c` ist der einzige Farbton und erscheint sparsam – Hauptaktion und Aktiv-Marke.

## Wirkung
- Charakter: filmisch, souverän, elegant fließend; Präzision ohne Lautstärke, Luxus durch Ruhe und Luft.
- Passt zu: Medien- und Foto-Apps, Reise, Mode, Fahrzeug- und Produktkataloge, Event- und Ergebnis-Apps.
- Passt weniger zu: datendichte Werkzeuge, verspielte Consumer-Apps, Apps ohne gutes Bildmaterial (ohne Foto bricht das System zusammen).
- Abgrenzung zur anderen Supersportwagen-Sprache in diesem Katalog (`lamborghini`): hier **elegant und fließend** – warmes Fast-Schwarz `#181818` statt reinem Schwarz, Display gemischt geschrieben in Gewicht 500 mit negativer Laufweite statt Versal-Geschrei, feine Linien-Icons mit runden Enden statt harter Gehrung, Haarlinien und eine helle Redaktionsbahn statt durchgehender Leere.

## Aufbau und Raster
- Seitenaufbau: randloses Kinobild oben (40–45 % der Höhe), Überschrift über dem unteren Bildrand oder in einer engen Bahn darunter; danach schmalere Redaktionsbahnen mit Haarlinien.
- Ausrichtung: links; nur Kennzahl-Zellen und Vorfußzeilen-Bahnen sind zentriert.
- Raster: Web 12 Spalten, Inhalt max. 1280px, Hero randlos. App: 1 Spalte, Seitenrand 24px (`sm`), Listen 2-spaltig mit 1px Haarlinien-Fuge.
- Dichte und Weißraum: 8px-Leiter `xxxs` 4 · `xxs` 8 · `xs` 16 · `sm` 24 · `md` 32 · `lg` 48 · `xl` 64 · `xxl` 96 · `super` 128. Bandabstand Web 96px; in der App 32px zwischen Bereichen, 16px innerhalb.
- Rhythmus: großes Bild → enge Textbahn → Kennzahlband → Haarlinien-Liste. Kein Element bekommt eine eigene Karte mit Schatten.

## Navigation
- Website: Kopfleiste 64px auf Canvas `#181818`, Marke links, Versal-Menü 13px/600/0,65px, Werkzeuge rechts; unter 768px Hamburger.
- App: feste untere Leiste, 4 Ziele (Start · Bibliothek · Suche · Profil), Höhe 68px, 1px Haarlinie `#303030` oben, Flächen bleiben eckig. Icon 22px Linie + Versal-Mikrolabel 11px/600/1,1px; inaktiv `#969696`, aktiv weiß **plus** 2px Rosso-Strich direkt über dem Icon (nie nur Farbe). Leiste bleibt beim Scrollen stehen; auf hellen Bahnen Variante Weiß mit Haarlinie `#d2d2d2`. Profil zusätzlich über das runde Avatar-Plättchen oben rechts (einziger Vollradius).
- TV: obere Versal-Menüzeile, Fokus als 2px Rosso-Unterstrich plus Helligkeitsstufe der Kachel (`#181818` → `#303030`), kein Vergrößern mit Schatten.

## Startscreen
- Randloses Kinobild mit leichter Körnung, Statusleiste liegt darüber; unten Verlauf zu `#181818`.
- Über dem Bildrand: Versal-Mikrolabel (z. B. „Vor einem Jahr“), darunter Display 44px/500/-1px gemischt geschrieben, danach Angaben 13px `#969696`.
- Direkt darunter die Aktionszeile: Rosso-CTA scharf 48px hoch, daneben ein 48px-Quadrat mit weißer 1px-Kontur.
- Danach ein Kennzahlband (drei Zellen, Zahl 34px/700/-0,8px, Label 11px Versal) zwischen zwei Haarlinien, dann eine horizontale Reihe scharfer Bildkarten, zuletzt die Quellen als Haarlinien-Zeilen.

## Komponenten
- Buttons: Hauptaktion `#da291c`, Text weiß 14px/700 Versal/1,4px Laufweite, Höhe 48px, Padding 14×32px, Radius 0. Druck `#b01e0a`. Sekundär transparent mit 1px weißer Kontur (auf Hell 1px `#181818`), gleiche Geometrie. Tertiär nur Versaltext.
- Karten und Kacheln: keine Karten im üblichen Sinn – Bildkacheln ohne Radius, Bild randlos bis zur Kante, Titel und Angaben eng darunter. Auf Dunkel hebt sich eine Fläche über `#303030` ab, nicht über Schatten.
- Listen: Haarlinien-Zeilen (`race-calendar-row`): links Datum oder Miniatur, Mitte Titel 16px/500 + Angaben 13px `#969696`, rechts Wert oder Chevron; 16px Abstand oben/unten, 1px `#303030` bzw. `#d2d2d2`.
- Suche und Eingabefelder: Höhe 48px, Radius 4px (einzige weiche Ecke neben Pillen), 1px Haarlinie, Text 14px, Platzhalter `#666`.
- Chips, Tabs, Filter: keine Pillen-Chips. Filter sind Versal-Textreiter 11px/600/1,1px nebeneinander, aktiv Vollton plus 2px Rosso-Strich darunter, inaktiv `#969696`; Trennlinie über die volle Breite.
- Dialoge und Sheets: scharfe Flächen `#303030` auf Dunkel bzw. Weiß auf Hell, 1px Haarlinie, Radius 0 (nur Modale dürfen `xl` 12px), Titel 26px/500.
- Signatur-Komponenten: `hero-band-cinema` (randloses Foto + schwebende Überschrift), `spec-cell` (riesige Zahl über Versal-Label), `livery-band` (volle Rosso-Fläche als Zäsur), `preowned-listing`-Raster (weiße Bahn, scharfe Kacheln, Haarlinien-Fugen), `badge-pill` (11px Versal auf `#303030`, Vollradius – die einzige runde Form).

## Icons
- Stil: feine Linie, offen, mit runden Enden – fließend als Gegengewicht zu den harten Kanten der Flächen. Nie gefüllt, nie zweifarbig.
- Größe und Strich: 20px in Zeilen, 22px in der Navigationsleiste, 24px über Bildern; Strichstärke 1,25px (Empfehlung, aus der schlanken Typo abgeleitet – die Datei beschreibt keinen Icon-Satz).
- Einsatz: sparsam, nur wo ein Wort fehlen würde; Icons bleiben weiß oder `#969696`, nie Rosso (Rot bleibt Aktionen und dem Aktiv-Strich vorbehalten).
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Rounded, Gewicht 200, Füllung 0, Grad 0; iOS SF Symbols `.ultraLight`/`.thin`, nicht gefüllt; Web Lucide `stroke-width: 1.25` mit `stroke-linecap: round`.

## Bildsprache
- Fotografie ist die Oberfläche: randlos, 16:9 oder breiter im Hero, 4:3 in Kacheln, 1:1 im Raster mit 1px Fuge – nie ein Radius auf dem Bild.
- Dunkler Verlauf (`linear-gradient(180deg, transparent, #181818)`) nur über dem unteren Drittel, damit Text trägt; keine farbigen Tönungen.
- Feine Körnung (`--grain: .10`) über großen Bildern für Kinowirkung; Atmosphäre-Verlauf `linear-gradient(180deg,#3c3c3c,#030303 64%)` an Abschnittswechseln.
- Menschen nur als rundes Avatar-Plättchen; sonst bleiben Motive unbeschnitten und bekommen Platz.

## Typografie-Stimme
- Eine Sans für alles. Größenkontrast ist groß (80/56/36/26 Web; 44/32/26 App) gegen ruhige 14px-Fließtexte.
- Display bleibt Gewicht 500 – nie fett – mit negativer Laufweite (-1,6px bei 80px, -0,36px bei 36px); Body 400, Laufweite 0; Komponententitel 18px/700.
- Versalien nur in kleinen Rollen: Buttons 14px/700/1,4px, Navigation 13px/600/0,65px, Labels 11px/600/1,1px. Zeilenhöhe 1,05 im Display, 1,5 im Text.
- Zahlen sind eine eigene Stimme: 80px/700/-1,6px (App 34–44px) über einem Versal-Label.
- Freier Ersatz: Inter (Gewicht 500, `letter-spacing: -1%`) – so auch in der Markendatei empfohlen; alternativ Archivo oder Manrope.

## Form, Tiefe und Material
- Radien: 0px überall (Buttons, Kacheln, Bilder, Bänder); 4px nur Eingabefelder, 12px nur Modale, Vollradius nur Pillen-Badges und Avatare.
- Linien und Rahmen: 1px Haarlinien `#303030` auf Dunkel, `#d2d2d2` auf Hell; sekundäre Buttons 1px weiß. Linien trennen – Flächen tun es nicht.
- Schatten und Ebenen: keine Schattenstufen. Ebene 0 `#181818`, Ebene 1 `#303030`, Lichtbahn `#ffffff`; höchstens `0 4px 8px rgba(0,0,0,.1)` auf angefasste Kacheln.
- Besondere Oberflächen: Rosso-Verlauf `linear-gradient(180deg,#a00c01,#da291c 64%)` in Akzentbändern; weiße Redaktionsbahn als bewusster Bruch mitten im dunklen Fluss.

## Bewegung
- Laut Datei: keine Angaben (Hero-Parallaxe, Band-Auftritt und Zähler ausdrücklich außerhalb des Umfangs); kein Hover-Zustand dokumentiert.
- Empfehlung: Dauer klein 160ms / Screenwechsel 420ms, Easing `cubic-bezier(.33, 0, .1, 1)` (langer, filmischer Auslauf). Druck-Effekt nur Farbwechsel auf `#b01e0a`, kein Skalieren. Einblenden: Bild von `scale(1.04)` auf 1 über 600ms, Text 16px von unten, Zeilen um 60ms gestaffelt. Screenwechsel: Bild bleibt stehen und wächst, Textbahn schiebt darüber. Fokus (TV): Rosso-Strich wächst in 160ms von der Mitte.
- Compose: `tween(420, easing = CubicBezierEasing(.33f, 0f, .1f, 1f))`, Bild `graphicsLayer` mit `animateFloatAsState` von 1.04f, `AnimatedVisibility` mit `slideInVertically`, Liste `animateItem()`, Hero zu Detail als Shared-Element über das Bild.

## Signatur-Elemente
1. Randloses Kinofoto mit schwebender Überschrift am unteren Bildrand – das Bild ist die Navigationsfläche, nicht ein Element darin.
2. Scharfe 0px-Flächen überall, dazu eine Rosso-Hauptaktion in Versalien mit 1,4px Laufweite.
3. Kennzahl-Zellen: sehr große Zahl in 700 über einem winzigen Versal-Label, getrennt durch Haarlinien.
4. Weiße Redaktionsbahn (Liste, Preise) als heller Einschnitt in einer sonst fast schwarzen App.
5. Display in Gewicht 500 mit negativer Laufweite – ruhig statt laut, obwohl groß.

## Übertragung auf eine App
- Startscreen: Kinobild des hervorgehobenen Inhalts oben, Überschrift darüber, direkt darunter Rosso-CTA; dann Kennzahlband, eine horizontale Bildreihe und Quellen als Haarlinien-Zeilen.
- Liste und Übersicht: helle Bahn (Weiß) mit Versal-Textreitern als Filter und einem 2-spaltigen Raster scharfer Bildkacheln mit 1px Fugen; Angaben 12px `#666` unter dem Titel.
- Detail: Bild randlos über die obere Hälfte, Titel darüber, Angaben als Haarlinien-Zeile, Rosso-Hauptaktion plus zwei konturierte Quadrate, Versal-Umschalter, Fotoraster mit 1px Fuge, feste Aktionsleiste unten statt Navigation.
- Formulare und Einstellungen: 48px-Felder mit 4px Radius und Haarlinie, Label als 11px-Versal darüber, Abschnitte durch Haarlinien statt Karten getrennt.
- Leere Zustände und Laden: Fläche `#181818` mit zentriertem Versal-Label und einer Zeile 14px `#969696`; Ladeplatzhalter als `#303030`-Rechtecke ohne Radius, kein Schimmer-Effekt.
- TV: Hero randlos über die ganze Fläche, Inhalte als Haarlinien-Zeilen rechts; Fokus über Rosso-Strich und Helligkeitsstufe.
- Musterscreens: Start mit Kino-Rückblick, Kennzahlband und Bildreihe; Bibliothek als helle Redaktionsbahn mit Versalfiltern und scharfem 2-spaltigen Raster; Detail mit randlosem Bild, Rosso-Hauptaktion und Fotoraster über einer festen Musikleiste.

## Vermeiden
- Keine zweite gesättigte Farbe neben Rosso Corsa; Rosso nie dekorativ oder flächig unter Text.
- Keine runden oder Pillen-Buttons – scharfe 0px-Kanten sind die Markenform; Vollradius nur für Badges und Avatare.
- Display nie fett setzen und nie in Versalien – die Lautstärke kommt vom Foto, nicht von der Schrift.
- Kein reines Schwarz als Fläche (`#181818`, leicht warm) und keine Schattenstufen; Tiefe nur über Foto und Helligkeitsstufe.
- Keine Ad-hoc-Abstände – nur die 8px-Leiter; keine eng gestapelten Kleinteile, die die Luft des Layouts auffressen.
- Gelb (Hypersail) nicht außerhalb seines Kontextes verwenden.
