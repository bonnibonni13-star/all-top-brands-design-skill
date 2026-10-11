---
slug: vercel
marke: Vercel
website: https://vercel.com
ansatz: minimal
ansatz2: werkzeug
modus: hell
aufbau: Fast weiße Fläche, weiße Karten mit Haarlinie und Stapelschatten; Mesh-Verlauf nur im zentrierten Start-Hero
navigation: Oben Bereichs-Schalter mit Schrägstrich, darunter Unterstrich-Tabs (3 Ziele), Profil als Avatar (Empfehlung)
komponenten: Schwarze Pill-CTAs (Hero) bzw. 6-px-Buttons, Tabelle mit Mono-Kopf, Schlüssel-Wert-Karte, runde Icon-Buttons
icons: Feine Linien-Icons (Lucide 1.5), 16 px, Tinte bzw. Grau #888, nie gefüllt (Empfehlung)
bewegung: Ruhig und schnell: 150 ms ease für Flächen, 300 ms Einblenden, Verlauf driftet langsam (Empfehlung)
schrift: Grotesk 600 mit starker negativer Laufweite, Satz-Titel mit Punkt; Mono 12 px nur für Labels und Zahlen
---
# Vercel – Designsprache

**Kurz:** Strenges Schwarz-Weiß-Duett auf fast weißer Fläche: Hierarchie entsteht aus Tintenschwarz, einer feinen Grautreppe, 1-px-Haarlinien und gestapelten Mini-Schatten. Die einzige Dekoration ist ein großer, weich verwischter Mesh-Verlauf (Blau–Türkis–Violett–Pink–Koralle–Amber) hinter dem Hero; alles Technische spricht in Mono.

## Wirkung
- Charakter: präzise, ruhig, ingenieurhaft; wirkt wie ein gut gebautes Entwickler-Dashboard mit einem einzigen leuchtenden Moment.
- Passt zu: Werkzeug-, Verwaltungs-, Status- und Bibliotheks-Apps, Dashboards, Pro-Medienverwaltung mit Tabellen und Zuständen.
- Passt weniger zu: warmen Lifestyle- und Kinder-Apps, bildlauten Feeds, dunklen Medien-Regalen.

## Aufbau und Raster
- Seitenaufbau: weiße Kopfleiste und Tab-Leiste über grauweißer Arbeitsfläche (#fafafa); darauf weiße Karten und Tabellen. Start beginnt mit einem zentrierten Hero (Abzeichen → Satz-Titel → Lead → zwei CTAs → Bildkarte), danach ein invertiertes Tintenband.
- Ausrichtung: Hero zentriert; Arbeitsflächen linksbündig, Zahlen rechtsbündig in Mono.
- Raster: 4-px-Basis (4/8/12/16/24/32/40/48/64/96 px), Gutter 16 px mobil, 24 px Desktop; Inhalt max. 1400 px. Thumbnails 16:9, Showcase 2:1 oder 16:9.
- Dichte und Weißraum: „große Lücken, enges Inneres“ – Titel/Text-Stapel 8 px, vor CTAs 20–24 px, zwischen Bändern 24–64 px; Tabellenzeilen 56 px, Karteninnenabstand 16–24 px.
- Rhythmus: Flächen wechseln canvas-soft → canvas → Tinte (#171717); das dunkle Band ist der Tiefenwechsel.

## Navigation
- Website: Kopfleiste 64 px weiß, Logo links, Links 14 px in #4d4d4d als Geister-Pills, rechts drei 28-px-Buttons mit 6 px Radius; mobil Hamburger mit Vollbild-Overlay.
- App (App-Muster der Marke, nicht in der Datei): Kopf 52 px mit neutralem Zeichen, grauem Schrägstrich und Bereichs-Schalter „Lenas Medien ⇕“; rechts runder Icon-Button (32 px, Haarlinie) und Avatar = Profil. Darunter Tab-Leiste 44 px mit Start · Bibliothek · Suche: Text 14 px, inaktiv #4d4d4d, aktiv Tinte + 500 + 2-px-Unterstrich in Tinte; Hover = graue Pill. Keine Leiste unten; Tabs bleiben beim Scrollen kleben, Kopf scrollt weg.
- Detail: runder Zurück-Button + Pfad „Bibliothek / Lissabon“ mit Schrägstrich, rechts Favorit und Mehr als runde Icon-Buttons.
- TV: linke Seitenleiste, aktive Zeile mit 2-px-Balken in Tinte links (ex-app-shell-row); Fokus = Haarlinien-Ring wird Tinte + Level-3-Schatten.

## Startscreen
- Zentrierter Hero auf Weiß, Mesh-Verlauf in der oberen Hälfte (verwischt, nach unten ausblendend): Abzeichen-Pill „NEU · Rückblick →“, Satz-Titel 40 px 600 mit Punkt („Vor einem Jahr: Herbstwald.“), Lead 18 px #4d4d4d, schwarze und weiße Pill, darunter Bildkarte 2:1 mit Level-4-Schatten.
- Danach ein invertiertes Band (#171717): Mono-Eyebrow „MUSIK“, Titel weiß, Titelliste wie ein Code-Editor (Zeilennummern grau, Dauern rechtsbündig).

## Komponenten
- Buttons: Hero/Marketing = Pill 100 px, 44–48 px hoch, 16 px 500 (Primär Tinte, Sekundär weiß mit Haarlinie). Arbeitsflächen = 6 px Radius, 36–40 px hoch, 14 px 500. Nie beide Formen auf einem Screen. Primär Hover #383838 (Empfehlung).
- Karten und Kacheln: weiß, 8 px (Standard) bzw. 12 px (Showcase, Detail), Ring 1 px #00000014 plus gestapelter Schatten (Level 2–4); Innenabstand 16–24 px. Invertierte Karte/Band in #171717 für den einen hervorgehobenen Bereich.
- Listen: als Tabelle in einer Karte – Kopfzeile 36 px auf #fafafa in Mono 12 px Versalien (#888), Zeilen 56 px mit 1-px-Linie #ebebeb, Thumbnail 36 px (6 px Radius), Titel 14/500 (−0,28 px), Unterzeile 12 px #4d4d4d, rechte Spalte Mono.
- Suche und Eingabefelder: 40 px hoch, weiß, 6 px Radius, 1 px #ebebeb, Text 14 px, Platzhalter #888; Fokus: Rahmen Tinte + 3-px-Ring rgba(0,0,0,.08) (Empfehlung). Klein 32 px, groß 48 px.
- Chips, Tabs, Filter: Navigation als Unterstrich-Tabs; Filter als Tab-Pills (64 px Radius, 32 px hoch, Padding 0 14 px): inaktiv transparent + #4d4d4d, aktiv weiß + Tinte + 500 + Ring + Level-2-Schatten. Abzeichen: Pill #fafafa/#f5f5f5, 12 px #4d4d4d.
- Dialoge und Sheets: weiß, 12 px Radius, Padding 32 px, Level-5-Schatten; Toasts 8 px Radius, Level 4.
- Signatur-Komponenten: Mesh-Hero; Schlüssel-Wert-Karte (Bild oben, darunter 2×2-Raster mit Mono-Labels wie STATUS ● Aktuell); Tabelle mit Mono-Kopf; Bereichs-Schalter mit Schrägstrich; Code-Liste im Tintenband.

## Icons
- Stil (Empfehlung, die Datei nennt keine Icons): feine, geometrische Linien-Icons mit runden Enden, einfarbig Tinte oder #888; nie gefüllt, nie bunt. Zustände als 8-px-Punkte (Blau #0070f3 = aktuell, Amber #f5a623 = läuft, Grau = getrennt), immer mit Text.
- Größe und Strich: 16 px in Buttons, Tabellen und Feldern, 14 px in Abzeichen, 18 px in runden Icon-Buttons; Strich 1,5 auf 24er-Raster.
- Einsatz: sparsam, fast immer mit Text; runde Icon-Buttons 32 px weiß mit Haarlinie (icon-button-circular).
- Umsetzung: Compose `Icons.Outlined` bzw. Material Symbols Outlined, Gewicht 300, Füllung 0; iOS SF Symbols `.regular`/`.light` ohne `.fill`; Web Lucide `stroke-width: 1.5`.

## Bildsprache
- Laut Datei: Der Mesh-Verlauf ist die einzige Atmosphäre – vollflächig, nie beschnitten auf ein Feld, nie als Icon oder Einzelfarbe; Paare in fester Reihenfolge (Develop #007cf0→#00dfd8, Preview #7928ca→#ff0080, Ship #ff4d4d→#f9cb28). Bilder 16:9 bzw. 2:1 in 8–16-px-Karten mit Stapelschatten; Platzhalter in Graustufen.
- Übertragung: Fotos ohne Filter, ohne Text darauf, Ring 1 px #00000014 statt Rahmen; Raster-Fotos 6 px Radius, 8 px Fuge. Avatare rund. Keine Verlauf-Overlays auf Fotos.

## Typografie-Stimme
- Eine geometrische Grotesk von Display bis Label: Display 600 (nie 700), Text 400, Buttons/Labels 500. Laufweite stark negativ: 48/−2,4 · 40/−1,8 · 32/−1,28 · 24/−0,96 · 20/−0,6 · 14/−0,28 px.
- Satz-Titel in Satzschreibung und mit Punkt („Vor einem Jahr: Herbstwald.“); Namen und Screen-Titel ohne Punkt. Nie Versalien außer in Mono-Labels.
- Mono 12–13 px nur für Eyebrows, Tabellenköpfe, Schlüssel, Zahlen, Code – nie für Fließtext.
- Größen App: Hero 40/44, Screen-Titel 32/40, Abschnitt 24/32, Liste 14/20, Meta 12/16.
- Freier Ersatz: Geist bzw. Inter (Inter Display für Titel) 400/500/600; Mono Geist Mono, JetBrains Mono (hier DejaVu Sans Mono).

## Form, Tiefe und Material
- Radien: 4 px Mini-Pills, 6 px Buttons/Felder/Thumbnails, 8 px Karten/Tabellen, 12 px Showcase/Dialoge, 64 px Tab-Pills, 100 px Hero-CTAs, rund für Icon-Buttons und Avatare.
- Linien und Rahmen: 1 px #ebebeb für Trennlinien und Felder; #a1a1a1 als stärkere Linie (Schrägstrich, Deaktiviert).
- Schatten und Ebenen: immer gestapelt plus Ring – L1 `0 0 0 1px #00000014`; L2 + `0 1px 1px #00000005, 0 2px 2px #0000000a`; L4 + `0 2px 2px #0000000a, 0 8px 16px -4px #0000000a`; L5 zusätzlich `0 24px 32px -8px #0000000f`. Nie ein einzelner weicher Schlagschatten.
- Besondere Oberflächen: Mesh-Verlauf (nur Hero-Maßstab), invertiertes Tintenband #171717 als Tiefenstufe; sonst kein Glas, keine Körnung.

## Bewegung
- Laut Datei: keine Angaben zu Animationen.
- Empfehlung: Dauer klein 150 ms / Screenwechsel 250 ms, Easing `cubic-bezier(0.25, 0.1, 0.25, 1)` (ease); Druck: Fläche #383838 bzw. #f5f5f5, kein Skalieren; Einblenden: Deckkraft + 8 px Anheben in 300 ms, Hero-Teile 60 ms gestaffelt; Mesh-Verlauf driftet in 16 s hin und her; Screenwechsel: Überblenden; Fokus (TV) Ring in 150 ms.
- Compose: `tween(150, easing = CubicBezierEasing(0.25f, 0.1f, 0.25f, 1f))`, `AnimatedVisibility(fadeIn(tween(300)) + slideInVertically { it / 12 })`, `rememberInfiniteTransition` für den Verlauf; kein Überschwingen.

## Signatur-Elemente
1. Mesh-Verlauf als einzige Dekoration – groß, verwischt, hinter zentriertem Satz-Titel mit Punkt.
2. Tintenschwarz als Hauptaktion (Pill im Hero, 6 px in Arbeitsflächen), Weiß als Partner.
3. Haarlinie + gestapelte Mini-Schatten statt Material-Schatten; invertiertes Tintenband als Tiefe.
4. Mono-Versal-Labels für Eyebrows, Tabellenköpfe und Schlüssel (STATUS, FOTOS) mit Zustandspunkten.
5. Display 600 mit starker negativer Laufweite gegen kleinen 12–14-px-Text.

## Übertragung auf eine App
- Startscreen: Kopf mit Bereichs-Schalter, Unterstrich-Tabs, zentrierter Mesh-Hero mit Rückblick und zwei Pills, Bildkarte, darunter Tintenband mit Musik als Code-Liste.
- Liste und Übersicht: Titel 32 px + schwarzer 6-px-Button, Suchfeld + Ansichts-Umschalter, Tab-Pills, Mono-Werkzeugzeile, Tabelle mit Mono-Kopf und Mono-Zahlenspalte.
- Detail: Pfad mit Schrägstrich, Mono-Eyebrow, Titel 32 px, Schlüssel-Wert-Karte (Bild + STATUS/FOTOS/VIDEOS/MUSIK), schwarzer Button „Diashow starten“ + weißer „Teilen“, Unterstrich-Tabs mit Zahl-Abzeichen, Fotoraster 3-spaltig.
- Formulare und Einstellungen: weiße Karten mit Titel 20/600, Feldern 40 px, Fußzeile auf #fafafa mit Hinweis links und schwarzem 6-px-Button rechts (Empfehlung).
- Leere Zustände und Laden: Karte auf #fafafa mit 48 px Innenabstand, Satz mit Punkt, ein Button; Laden als graue Skelett-Flächen (#ebebeb) mit sanftem Schimmer.
- TV: Seitenleiste links, Inhalte als Karten-Raster 16:9; der Mesh-Verlauf nur im obersten Hero.
- Musterscreens: Mesh-Hero mit Tintenband, Bibliothek als Mono-Tabelle, Album als Schlüssel-Wert-Detail mit Fotoraster.

## Vermeiden
- Verlauf als Icon, Button-Füllung, Einzelfarbe oder in jeder Karte; eine sechste Akzentfarbe; bunte Icons.
- Display in 700+, Versal-Überschriften, Titel ohne negative Laufweite; Mono für Fließtext.
- Einzelne schwere Schatten, Material-Elevation, harte schwarze Rahmen.
- 100-px-Pill und 6-px-Button auf demselben Screen; Leiste unten mit bunten Icons.
- Reines Weiß als Seitenfläche überall – die Arbeitsfläche ist #fafafa, Karten sind #fff.
- Abgrenzung zu The Verge: Mono hier klein, grau und ruhig (Labels, Zahlen), dort laut, versal und weit gesperrt auf Schwarz.
