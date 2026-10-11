---
slug: composio
marke: Composio
website: https://composio.dev
ansatz: leuchten
ansatz2: daten
modus: dunkel
aufbau: Monolithisch dunkle Fläche, Tiefe nur über Helligkeitsstufen, ein blauer Spotlight-Schein hinter dem Einstieg
navigation: Schwebende Dock-Leiste (4 Ziele, 12 px Radius, aktiv = blau gefüllte 8-px-Kachel)
komponenten: 2x2-Panel-Raster (Kennzahlen), gefüllte Karten ohne Rahmen, schwarze Mono-Panels, Versal-Pillen
icons: Phosphor Fill, 18-22 px, massiv gefüllt, nie Linie
bewegung: Empfehlung - sachlich, 160/240 ms, cubic-bezier(.2,0,0,1), Schein atmet, Karten heben Helligkeit
schrift: Inter/Inter Display 500 mit enger Laufweite, 11-px-Versallabels, Mono für alle Zahlen
---
# Composio – Designsprache

**Kurz:** Eine fast schwarze Fläche von oben bis unten, auf der Tiefe ausschließlich über Helligkeitsstufen entsteht (#0f0f0f → #181818 → #222222, tiefer gelegt #000000) – keine Schatten, keine Rahmen. Ein einziges tiefes Elektroblau trägt Hauptaktionen und einen radialen Lichtschein hinter dem Einstieg. Das Erkennungszeichen ist ein Raster aus vier Terminal-Panels mit Mono-Zahlen.

## Wirkung
- Charakter: technisch, konzentriert, ruhig-dunkel; Werkzeugkasten statt Schaufenster.
- Passt zu: Entwickler- und Infrastruktur-Apps, Dashboards, Medien-Verwaltung mit vielen Zahlen, Monitoring.
- Passt weniger zu: verspielte Consumer-Apps, Kinder, Lifestyle, alles Helle mit Pastell.

## Aufbau und Raster
- Seitenaufbau: durchgehend dunkle Bahnen; jede Bahn beginnt mit einem 11-px-Versallabel, darunter der Inhalt.
- Ausrichtung: links; nur der Einstiegs-Block (Schein + Panel-Raster) wirkt zentriert durch sein symmetrisches 2x2.
- Raster: 12 Spalten im Web (max. 1200 px); Toolkit-Raster 4-up Desktop → 2-up Tablet → 1-up Handy; Panel-Raster immer 2x2.
- Dichte und Weißraum: Basiseinheit 4 px; Abstände 4/8/12/16/20/24/32/48, Bahnabstand 96 px (App: 28–32 px). Seitenrand 20 px, Kartenpolster 20–28 px, Panelpolster 20 px bei 16 px Lücke.
- Rhythmus: Label (11 px Versal) → Block → 28 px Luft. Dunkel darf dicht sein; die Fläche trägt die Ruhe.

## Navigation
- Website: 64 px hohe dunkle Kopfleiste, Zeichen links, horizontale Menüpunkte 14 px/500, rechts blaue Hauptaktion.
- App: schwebendes Dock unten, 12 px vom Rand abgesetzt, Fläche #181818, Radius 12 px, vier Ziele (Start, Bibliothek, Suche, Profil). Aktiv = blau gefüllte 8-px-Kachel hinter dem gefüllten Icon plus Label in Weiß/600; inaktiv Icon #666, Label #888. Beim Scrollen bleibt das Dock stehen; Inhalt läuft darunter aus.
- TV: linke Spalte mit denselben vier Zielen; Fokus = blau gefüllte Kachel, zusätzlich 2 px heller Rand.

## Startscreen
- Begrüßung als Display 32 px/500 mit −0.96 px Laufweite, darunter eine Mono-Zeile mit den Bestandszahlen.
- Darunter der Einstiegsanker: 2x2-Panel-Raster in schwarzem Container (#000, Radius 16 px) mit radialem Blauschein dahinter – vier Kennzahlen (Fotos, Videos, Titel, Speicher) als Versallabel + Mono-Zahl.
- Dann eine Spotlight-Karte (Rückblick) und ein 2-up-Raster „Zuletzt hinzugefügt“, unten angeschnitten.

## Komponenten
- Buttons: Hauptaktion blau #0007cd, Weiß, 14 px/500, Polster 10×18 px, Höhe 40 px, Radius 8 px (nie Pille); Nebenaktion Fläche #222222; Umriss = transparent mit 1 px #333; Text-Button in #a8a8a8.
- Karten und Kacheln: gefüllte Flächen #181818, Radius 12–16 px, Polster 20–28 px, **kein** Rahmen, **kein** Schatten. Hervorgehobene Karte bekommt einen radialen Blauschein im Inneren.
- Listen: Zeilen als eigene gefüllte Karten (Radius 12 px) mit 48-px-Bildplatte (Radius 8 px) links, Titel 16 px/600, Mono-Angaben 13 px #888 darunter; 8 px Abstand zwischen den Zeilen statt Trennlinien.
- Suche und Eingabefelder: Fläche #181818, Radius 8 px, Höhe 40–44 px, Polster 10–12 px × 16 px, Platzhalter #666, Lupe gefüllt links.
- Chips, Tabs, Filter: Versal-Pillen 11 px/600 mit 0.88 px Laufweite, Polster 4×10 px (App: 6×12), inaktiv #222222 auf #888, aktiv blau gefüllt mit weißem 600-Text.
- Dialoge und Sheets: Fläche #2a2a2a, Radius 16 px oben, 24 px Polster, kein Schatten – Abgrenzung über die hellere Stufe.
- Signatur-Komponenten: `terminal-grid` (2x2 Panels im schwarzen Rahmen), `code-pane` (schwarzes Panel mit Mono-Zeile und blauem Prompt-Balken), `spotlight-card`, Versal-Pille.

## Icons
- Stil: Phosphor **Fill** – massiv gefüllte, geometrische Glyphen, nie Linienversion; eine einzige Stärke im ganzen Produkt.
- Größe und Strich: 18 px in Listen und Chips, 20–22 px im Dock und in quadratischen Aktionsknöpfen (36–40 px, Radius 8 px).
- Einsatz: sparsam und funktional – Navigation, Aktionsknöpfe, Quellen, Medienart. Keine dekorativen Icons in Fließtext.
- Umsetzung: Compose `Icons.Filled` bzw. Material Symbols Rounded, Fill 1, Gewicht 500; iOS SF Symbols `.fill`, Gewicht Medium; Web Phosphor `weight="fill"`.

## Bildsprache
- Bilder sind Material, nicht Dekoration: dunkel abgestimmt, leicht abgesenkt (`filter: brightness(.92) saturate(.95)`), Radius 8–12 px.
- Im Detail vollflächig oben, nach unten per Verlauf in #0f0f0f auslaufend; darunter darf der Blauschein durchscheinen.
- Kleine Vorschauen als quadratische Platten (48 px, Radius 8 px) – gleiche Form wie die Icon-Platten des Toolkit-Rasters.
- Raster aus Ausschnitten mit 6 px Lücke und 8 px Radius; keine weißen Rahmen, keine Schlagschatten.

## Typografie-Stimme
- Eine Familie für alles außer Code: abcDiatype (Ersatz Inter / Inter Display). Display 24–72 px immer Gewicht **500** mit negativer Laufweite (−0.5 px bei 24 px bis −2.16 px bei 72 px); Titel 16–18 px/600; Fließtext 16 px/400 in #a8a8a8; Label 11 px/600 Versal mit +0.88 px.
- Alle Zahlen, Pfade, Dauern und Befehle in Mono 13 px (JetBrains Mono, Ersatz DejaVu Sans Mono) – das ist der zweite Stimmenträger.
- Zeilenhöhe: Display 1.05–1.25, Text 1.5.
- Freier Ersatz: Inter (500 für Display, −1.5 % Laufweite) + JetBrains Mono.

## Form, Tiefe und Material
- Radien: 4 px Inline-Tags, 6 px kompakte Zeilen, 8 px Buttons/Eingaben/Bildplatten, 12 px Karten und Panels, 16 px große Container, Pille nur für Versal-Label.
- Linien und Rahmen: 1 px #222222 nur als Trennlinie, 1 px #333333 für Umriss-Buttons – Karten bekommen keinen Rahmen.
- Schatten und Ebenen: keine Schlagschatten. Helligkeitsleiter #0f0f0f → #181818 → #222222 → #2a2a2a, tiefergelegt #000000 für Terminal- und Code-Flächen.
- Besondere Oberflächen: radialer Blauschein (#1a26ff, 10–22 % Deckkraft, 60–70 % Radius) hinter Einstieg und Spotlight-Karten; Mono-Panels auf reinem Schwarz; schmaler blauer Prompt-Balken als Akzentmarke.

## Bewegung
- Laut Datei: keine Angaben (Animationszeiten ausdrücklich außerhalb des Umfangs).
- Empfehlung: klein 160 ms / Screenwechsel 240 ms, Easing `cubic-bezier(.2,0,0,1)`; Druck = Fläche eine Helligkeitsstufe hoch (#181818 → #222222) plus `scale(.985)`; Einblenden 12 px von unten mit 40 ms Staffel je Panel; Screenwechsel als weiches Überblenden ohne Verschieben; der Spotlight-Schein atmet langsam (8 s, 0.85 ↔ 1.0 Deckkraft); Fokus (TV) = blaue Kachel wächst auf 1.04.
- Compose: `tween(160, easing = CubicBezierEasing(.2f,0f,0f,1f))`, `AnimatedVisibility` mit `fadeIn() + slideInVertically { it / 8 }`, `animateItem()` für Listen, `Crossfade` für Screenwechsel.

## Signatur-Elemente
1. 2x2-Panel-Raster auf reinem Schwarz mit Mono-Kennzahlen – der Einstiegsanker.
2. Radialer tiefblauer Lichtschein hinter Einstieg und hervorgehobener Karte.
3. Helligkeitsleiter statt Schatten: gefüllte, rahmenlose Karten in vier Graustufen.
4. 11-px-Versallabel mit 0.88 px Laufweite über jedem Abschnitt, als Pille oder als Zeile.
5. Mono-Zeile mit blauem Prompt-Balken für Zahlen, Pfade und den Musik-Hinweis.

## Übertragung auf eine App
- Startscreen: Begrüßung (Display 32/500) + Mono-Bestandszeile, darunter das 2x2-Kennzahlraster mit Schein, dann Spotlight-Karte „Rückblick“ und ein 2-up-Raster neuer Inhalte.
- Liste und Übersicht: Suchfeld (8 px), Versal-Pillen als Filter, danach **ein**spaltige gefüllte Kartenzeilen mit quadratischer Bildplatte, Titel und Mono-Angaben – das Toolkit-Raster im 1-up-Zustand.
- Detail: Vollbild oben mit Verlauf und Schein, quadratischer Zurück-Knopf (36 px, Radius 8 px), Versal-Pille für die Art, Display-Titel, Mono-Angaben, blaue Hauptaktion plus drei quadratische Nebenknöpfe, schwarzes Mono-Panel für die Diashow-Musik, Versal-Pillen als Umschalter, Fotoraster 3-up.
- Formulare und Einstellungen: Felder #181818 mit 8 px Radius und 11-px-Versallabel darüber; Gruppen als gefüllte Karten ohne Rahmen; Schalter blau gefüllt.
- Leere Zustände und Laden: schwarzes Panel mit Mono-Zeile und blauem Prompt-Balken („keine Einträge“); Laden als Helligkeits-Puls der Platzhalterflächen, kein Spinner-Zirkus.
- TV: linke Zielspalte, Inhalt als 2x2- bzw. 4x2-Panelraster, Fokus über blau gefüllte Kachel.
- Musterscreens: Start mit Kennzahl-Panels unter blauem Schein, Bibliothek als einspaltige gefüllte Kartenliste mit Versal-Filtern, Detail mit Vollbild, blauer Hauptaktion und Mono-Panel für die Diashow-Musik.

## Vermeiden
- Keine zweite Markenfarbe; Cyan und Violett bleiben Illustration.
- Keine Pillen-Buttons für Aktionen (8 px Radius) und kein Display-Gewicht 400.
- Keine Schlagschatten und keine Rahmen um Karten – Tiefe nur über Helligkeit.
- Reines Schwarz nur für Terminal-/Code-Flächen, nie als Seitenfläche.
- Blau nicht großflächig fluten: Hauptaktion, Aktivzustand, Schein – mehr nicht.
- Zahlen nicht in der Textschrift setzen; die Mono-Stimme geht sonst verloren.
