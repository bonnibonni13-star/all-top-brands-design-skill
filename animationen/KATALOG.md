# Animations-Katalog

Benannte Bewegungs-Effekte zum Auswählen – für Schritt 7, Bereich 6 („Animationen“) des Skills. Jeder Eintrag sagt, was man sieht, zu welchem Ansatz er passt, mit welchen Werten er läuft und wie man ihn im Web, in React und in Jetpack Compose baut.

## Wie man auswählt

- **Ein Leit-Effekt je Screen.** Einer darf auffallen, alles andere bleibt ruhig (Einblenden, Druck-Zustand, Übergang). Zwei auffällige Effekte nebeneinander wirken billig und lenken vom Inhalt ab.
- **Zum Ansatz passend.** `leuchten`, `verspielt` und `plakativ` vertragen sichtbare Effekte; `werkzeug`, `minimal` und `editorial` wollen fast unsichtbare Bewegung – dort ist der richtige Effekt oft nur eine kürzere Dauer.
- **Bewegung hat eine Aufgabe:** zeigen, woher etwas kommt, was zusammengehört, dass etwas lädt oder geklappt hat. Dekoration ohne Aufgabe fliegt raus.
- **Dauer:** kleine Zustände 120–200 ms, Flächen und Karten 200–320 ms, Screenwechsel 300–420 ms. Längeres wirkt träge, Kürzeres wird übersehen.
- **Easing:** Hinein `cubic-bezier(.16,1,.3,1)` (schnell los, weich aus), Hinaus `cubic-bezier(.4,0,1,1)`. Dauerschleifen immer `linear`.

## Reduzierte Bewegung

Pflicht, nicht Kür. Wer Bewegung abgeschaltet hat, bekommt den Endzustand sofort – nie eine leere Seite.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; animation-iteration-count: 1 !important;
    transition-duration: .01ms !important; scroll-behavior: auto !important; }
}
```

Android: `Settings.Global.getFloat(resolver, Settings.Global.ANIMATOR_DURATION_SCALE, 1f)` bzw. `TRANSITION_ANIMATION_SCALE`; ist der Wert `0f`, Effekte überspringen und den Endzustand setzen. In Compose den Wert einmal in einem `CompositionLocal` ablegen und Dauern damit multiplizieren.

## Leistung

Nur `transform` und `opacity` animieren – sie laufen auf der Grafikkarte. `width`, `height`, `top`, `left`, `margin`, `box-shadow` und `filter` auf großen Flächen lösen Neuberechnung des Layouts aus und ruckeln. In Compose entsprechend `graphicsLayer` (Skalierung, Alpha, Verschiebung) statt geänderter Maße. Dauerschleifen nur, solange sie sichtbar sind (`IntersectionObserver` bzw. `LaunchedEffect` am Sichtbarkeitszustand).

---

## Text

### Weich einblenden (blur-fade)
Text erscheint, während Unschärfe und Versatz verschwinden.
`Passt zu:` editorial, minimal, buehne, galerie
`Dosierung:` für Überschriften und erste Absätze; nicht auf jedem Listeneintrag.
`Werte:` 400 ms, `cubic-bezier(.16,1,.3,1)`, `blur(6px) → 0`, 8 px von unten, Staffel 60 ms.
`Web:` `@keyframes` auf `opacity`, `filter: blur()`, `translateY`; Start per `IntersectionObserver`.
`React:` `npx shadcn@latest add @magicui/blur-fade`
`Compose:` `AnimatedVisibility(enter = fadeIn(tween(400)) + slideInVertically { it / 8 })`; Unschärfe über `Modifier.blur()` (ab API 31) oder weglassen.
`Barrierefreiheit:` ohne Bewegung sofort scharf und sichtbar.

### Zeichenweise schreiben (typing-animation)
Der Text tippt sich Zeichen für Zeichen, mit blinkendem Strich.
`Passt zu:` werkzeug, retro, leuchten
`Dosierung:` genau eine Stelle je App, meist der Begrüßungssatz. Nie bei Text, den man lesen muss, bevor man handelt.
`Werte:` 35–55 ms je Zeichen, Strich blinkt 1 s `step-end`, Pause 1,2 s vor dem Neustart.
`Web:` Zeichen in `<span>` zerlegen und per `animation-delay` staffeln, oder `steps()` auf der Breite bei Monospace.
`React:` `npx shadcn@latest add @magicui/typing-animation`
`Compose:` `LaunchedEffect` mit `delay()` und wachsendem `substring`; Strich als blinkendes `Text("|")` über `rememberInfiniteTransition`.
`Barrierefreiheit:` ganzer Text im `aria-label`, damit Vorlesewerkzeuge ihn am Stück lesen.

### Wort wechseln (word-rotate)
Ein Wort im Satz tauscht sich gegen das nächste aus, der Rest steht still.
`Passt zu:` plakativ, verspielt, buehne
`Dosierung:` für ein Versprechen mit mehreren Facetten („Fotos · Videos · Musik“). Höchstens vier Wörter.
`Werte:` 2,2 s Standzeit, 320 ms Wechsel, hoch hinaus und von unten herein, 12 px.
`Web:` zwei übereinanderliegende Spans, `overflow: hidden`, `transform: translateY`.
`React:` `npx shadcn@latest add @magicui/word-rotate`
`Compose:` `AnimatedContent` mit `slideInVertically { it } togetherWith slideOutVertically { -it }`.
`Barrierefreiheit:` ohne Bewegung das erste Wort stehen lassen.

### Buchstabensalat (hyper-text)
Buchstaben würfeln kurz durch, bevor sich das Wort setzt.
`Passt zu:` werkzeug, leuchten, retro
`Dosierung:` einmalig beim Erscheinen, nie in Dauerschleife; wirkt schnell nach Spielerei.
`Werte:` 30 ms je Schritt, 8–12 Schritte je Buchstabe, versetzt um 40 ms.
`Web:` Timer, der je Buchstabe zufällige Zeichen setzt, bis der Zielbuchstabe erreicht ist.
`React:` `npx shadcn@latest add @magicui/hyper-text`
`Compose:` `produceState` mit zufälligen Zeichen je Position.
`Barrierefreiheit:` Endtext im `aria-label`; ohne Bewegung direkt setzen.

### Wörter formen sich um (morphing-text)
Ein Wort schmilzt unscharf in das nächste.
`Passt zu:` leuchten, buehne
`Dosierung:` einmal je Screen, am besten in einem großen Kopfbereich.
`Werte:` 1,5 s Standzeit, 600 ms Übergang, `blur(8px)` in der Mitte, Kontrastfilter.
`Web:` zwei Texte übereinander, gegenläufige `opacity` plus `filter: blur()`, Elternteil mit `filter: contrast(20)`.
`React:` `npx shadcn@latest add @magicui/morphing-text`
`Compose:` zwei `Text` übereinander mit gegenläufigem `alpha`; echtes Verschmelzen ist aufwendig, meist genügt das Überblenden.
`Barrierefreiheit:` starker Kontrastfilter kann flimmern – bei reduzierter Bewegung ganz aus.

### Zeile für Zeile aufdecken (text-reveal)
Beim Scrollen färbt sich der Text Wort für Wort von blass zu kräftig.
`Passt zu:` editorial, buehne, plakativ
`Dosierung:` für genau einen Absatz, der die Aussage trägt.
`Werte:` an die Scrollstrecke gekoppelt, blass `opacity .2` → 1.
`Web:` Wörter in Spans, `opacity` aus dem Scrollfortschritt, `IntersectionObserver` plus `scroll`-Ereignis.
`React:` `npx shadcn@latest add @magicui/text-reveal`
`Compose:` Scrollposition aus `LazyListState`/`rememberScrollState` auf die Wort-Alphas abbilden.
`Barrierefreiheit:` Mindestkontrast auch im blassen Zustand; ohne Bewegung alles kräftig.

### Schimmernder Text (animated-shiny-text)
Ein heller Streifen wandert langsam durch die Schrift.
`Passt zu:` leuchten, minimal, werkzeug
`Dosierung:` für kleine Hinweise („Neu“, „Jetzt verfügbar“), nicht für Fließtext.
`Werte:` 4 s `linear`, Dauerschleife, Streifen 40 % breit.
`Web:` `background: linear-gradient(...)` mit `background-size: 200%`, `background-clip: text`, `color: transparent`, Position animieren.
`React:` `npx shadcn@latest add @magicui/animated-shiny-text`
`Compose:` `Brush.linearGradient` mit wanderndem Offset aus `rememberInfiniteTransition`, auf `TextStyle(brush = …)`.
`Barrierefreiheit:` Grundfarbe muss allein schon lesbar sein.

### Farbverlauf-Text (animated-gradient-text)
Die Schrift trägt einen langsam wandernden Farbverlauf.
`Passt zu:` leuchten, verspielt, plakativ
`Dosierung:` eine Überschrift je Screen.
`Werte:` 6–8 s `linear`, Dauerschleife, zwei bis drei Farben.
`Web:` wie oben mit `background-clip: text`.
`React:` `npx shadcn@latest add @magicui/animated-gradient-text`
`Compose:` `TextStyle(brush = Brush.linearGradient(...))` mit animiertem Offset.
`Barrierefreiheit:` alle Verlaufsfarben gegen den Hintergrund prüfen, nicht nur eine.

### Nordlicht-Text (aurora-text)
Weiche, wabernde Farbflächen hinter der Schrift, wie Polarlicht.
`Passt zu:` leuchten, buehne
`Dosierung:` nur im Kopfbereich, nie über Lesetext.
`Werte:` 10 s `linear`, zwei bis drei Flächen mit `blur(40px)`, gegenläufig.
`Web:` unscharfe Farbkreise hinter dem Text, `background-clip: text` auf dem Elternteil.
`React:` `npx shadcn@latest add @magicui/aurora-text`
`Compose:` `Brush.radialGradient` mit animiertem Mittelpunkt; `Modifier.blur()` ab API 31, sonst vorbereitete Verlaufsgrafik.
`Barrierefreiheit:` ohne Bewegung ein ruhiges Standbild statt Abschalten ins Nichts.

### Funken im Text (sparkles-text)
Kleine Sternchen blitzen rund um ein Wort auf.
`Passt zu:` verspielt, leuchten
`Dosierung:` ein Wort, kein Satz.
`Werte:` 6–10 Funken, je 700 ms Lebensdauer, zufällig versetzt, Skalierung 0 → 1 → 0.
`Web:` absolut gesetzte SVG-Sterne mit zufälliger Position und `animation-delay`.
`React:` `npx shadcn@latest add @magicui/sparkles-text`
`Compose:` `Canvas` mit einer Liste animierter Punkte.
`Barrierefreiheit:` kein Blitzen schneller als dreimal je Sekunde.

### Schlagschatten-Schrift (line-shadow-text)
Ein versetzter Linienschatten wandert langsam hinter der Schrift.
`Passt zu:` plakativ, retro
`Dosierung:` nur für sehr große Versalien.
`Werte:` Schatten 2–4 px versetzt, 3 s `linear`.
`Web:` Streifenmuster als `background` hinter dem Text, Position animieren.
`React:` `npx shadcn@latest add @magicui/line-shadow-text`
`Compose:` zweiter, versetzter `Text` mit Streifen-Brush darunter.
`Barrierefreiheit:` Schatten darf die Form nicht verwischen.

### Buchstaben kippen (text-3d-flip)
Buchstaben drehen sich einzeln um die eigene Achse.
`Passt zu:` verspielt, plakativ
`Dosierung:` kurze Wörter, einmalig.
`Werte:` 500 ms je Buchstabe, Staffel 40 ms, `rotateX(90deg) → 0`.
`Web:` `perspective` auf dem Elternteil, `transform: rotateX` je Span.
`React:` `npx shadcn@latest add @magicui/text-3d-flip`
`Compose:` `graphicsLayer { rotationX = … }` je Buchstabe.
`Barrierefreiheit:` ohne Bewegung flach anzeigen.

### Zahlen hochzählen (number-ticker)
Eine Zahl zählt von null auf ihren Wert.
`Passt zu:` daten, plakativ, werkzeug
`Dosierung:` für Kennzahlen, die etwas bedeuten („1.248 Fotos“), nicht für Preise im Warenkorb.
`Werte:` 1,2 s, `cubic-bezier(.16,1,.3,1)`, Tausendertrennzeichen mitführen, Tabellenziffern (`font-variant-numeric: tabular-nums`).
`Web:` `requestAnimationFrame` mit eigener Easing-Kurve.
`React:` `npx shadcn@latest add @magicui/number-ticker`
`Compose:` `animateIntAsState(target, tween(1200))`.
`Barrierefreiheit:` Endwert im `aria-label`, damit nicht jede Zwischenzahl vorgelesen wird.

---

## Knöpfe und Aktionen

### Druck-Zustand (press)
Der Knopf sinkt beim Antippen leicht ein.
`Passt zu:` alle
`Dosierung:` auf jedem tippbaren Element – das ist die wichtigste Animation der ganzen App.
`Werte:` Skalierung 0,97, 120 ms hinein, 180 ms zurück; bei flachen Marken stattdessen Flächenstufe statt Skalierung.
`Web:` `transition: transform .12s` plus `:active { transform: scale(.97) }`.
`React:` —
`Compose:` `interactionSource.collectIsPressedAsState()` → `animateFloatAsState` auf `graphicsLayer { scaleX = …; scaleY = … }`.
`Barrierefreiheit:` Tastaturfokus braucht einen eigenen, sichtbaren Zustand – Druck allein genügt nicht.

### Schimmer-Knopf (shimmer-button)
Ein Lichtstreifen läuft dauerhaft am Rand oder über die Fläche.
`Passt zu:` leuchten, plakativ, buehne
`Dosierung:` genau ein Knopf je Screen – die Hauptaktion.
`Werte:` 2,5–3 s `linear`, Dauerschleife, Streifen 25 % breit, weiß bei 20 % Deckkraft.
`Web:` rotierender `conic-gradient` hinter dem Knopf, Inhalt auf einer Innenfläche; oder wandernder `linear-gradient` mit `background-size: 200%`.
`React:` `npx shadcn@latest add @magicui/shimmer-button`
`Compose:` `rememberInfiniteTransition` auf den Offset eines `Brush.linearGradient`, gezeichnet in `Modifier.drawBehind`.
`Barrierefreiheit:` Beschriftung muss ohne den Schimmer genug Kontrast haben.

### Glanz-Knopf (shiny-button)
Beim Zeigen oder Antippen huscht ein Glanz über die Fläche.
`Passt zu:` minimal, werkzeug, galerie
`Dosierung:` zurückhaltender als der Schimmer-Knopf, auch mehrfach einsetzbar.
`Werte:` 600 ms, `ease-out`, nur beim Zeigen oder Drücken.
`Web:` Pseudo-Element mit schrägem Verlauf, `transform: translateX(-100% → 200%)`.
`React:` `npx shadcn@latest add @magicui/shiny-button`
`Compose:` beim Druck ein `animateFloatAsState` auf die Position eines Verlaufs in `drawWithContent`.
`Barrierefreiheit:` unauffällig genug, um niemanden zu stören.

### Regenbogen-Knopf (rainbow-button)
Ein Farbkranz wandert um den Knopfrand.
`Passt zu:` verspielt, leuchten
`Dosierung:` höchstens einer je App – sehr laut.
`Werte:` 2 s `linear`, Dauerschleife, vier bis sechs Farben.
`Web:` `conic-gradient` als Rahmen über `background-origin: border-box` und Maske.
`React:` `npx shadcn@latest add @magicui/rainbow-button`
`Compose:` `Brush.sweepGradient` mit animiertem Winkel in `drawBehind`.
`Barrierefreiheit:` Farbe darf keine Bedeutung tragen.

### Welle beim Tippen (ripple-button)
Vom Berührpunkt läuft ein Kreis nach außen.
`Passt zu:` verspielt, galerie, daten
`Dosierung:` Standard für Android; auf Marken mit sehr flachem Stil besser den Druck-Zustand nehmen.
`Werte:` 450 ms, `ease-out`, Deckkraft 0,25 → 0.
`Web:` Kreis am Klickpunkt einfügen, `scale(0 → 2.5)` plus `opacity`.
`React:` `npx shadcn@latest add @magicui/ripple-button`
`Compose:` eingebaut über `indication = ripple(color = …)`; Farbe an die Marke anpassen.
`Barrierefreiheit:` bei reduzierter Bewegung durch eine kurze Flächenänderung ersetzen.

### Pulsieren (pulsating-button)
Ein weicher Ring atmet um den Knopf.
`Passt zu:` verspielt, leuchten, daten
`Dosierung:` nur, wenn etwas wirklich Aufmerksamkeit braucht (Aufnahme läuft, Live). Dauerhaftes Pulsieren ohne Grund nervt.
`Werte:` 2 s, `ease-in-out`, Skalierung 1 → 1,25, Deckkraft 0,5 → 0.
`Web:` Pseudo-Element mit `@keyframes` auf `transform` und `opacity`.
`React:` `npx shadcn@latest add @magicui/pulsating-button`
`Compose:` `rememberInfiniteTransition` auf Skalierung und Alpha eines Kreises darunter.
`Barrierefreiheit:` nach einiger Zeit anhalten; nicht endlos blinken lassen.

### Knopf wird zur Bestätigung (animated-subscribe-button)
Der Knopf wechselt nach dem Tippen Beschriftung und Farbe, mit Häkchen.
`Passt zu:` galerie, verspielt, daten
`Dosierung:` für Aktionen mit Ergebnis (gespeichert, abonniert, hinzugefügt).
`Werte:` 300 ms Wechsel, Häkchen zeichnet sich in 250 ms.
`Web:` `AnimatedContent`-Muster: zwei Zustände übereinander, Breite per `transition`.
`React:` `npx shadcn@latest add @magicui/animated-subscribe-button`
`Compose:` `AnimatedContent` auf den Zustand, `Modifier.animateContentSize()` für die Breite.
`Barrierefreiheit:` Zustandswechsel auch als Text melden (`aria-live` bzw. `stateDescription`).

### Knopf öffnet sich (interactive-hover-button)
Beim Zeigen schiebt sich ein Pfeil heraus und die Fläche färbt sich von einer Seite ein.
`Passt zu:` minimal, editorial, werkzeug
`Dosierung:` gut für Textlinks mit Aktionscharakter.
`Werte:` 300 ms, `ease-out`, Pfeil 6 px, Fläche von links.
`Web:` Pseudo-Element mit `transform: scaleX`, Ursprung links; Pfeil per `translateX`.
`React:` `npx shadcn@latest add @magicui/interactive-hover-button`
`Compose:` Hover gibt es auf dem Handy nicht – als Druck-Zustand umsetzen.
`Barrierefreiheit:` muss auch ohne Zeigegerät erreichbar bleiben.

### Konfetti (confetti)
Papierschnipsel regnen einmalig über den Screen.
`Passt zu:` verspielt
`Dosierung:` einmal, nach einem echten Erfolg. Zweimal ist zu viel.
`Werte:` 1,5–2,5 s, 60–120 Teilchen, Schwerkraft, zufällige Drehung.
`Web:` `<canvas>` mit eigener kleiner Physik.
`React:` `npx shadcn@latest add @magicui/confetti`
`Compose:` `Canvas` mit einer Liste von Teilchen, bewegt über `withFrameNanos`.
`Barrierefreiheit:` bei reduzierter Bewegung ganz weglassen, Erfolg nur als Text und Häkchen.

---

## Listen und Karten

### Gestaffeltes Einblenden (stagger)
Einträge erscheinen kurz nacheinander statt alle auf einmal.
`Passt zu:` alle
`Dosierung:` beim ersten Laden eines Screens; nicht bei jedem Scrollen neu.
`Werte:` je Eintrag 260 ms, Staffel 40–60 ms, 8–12 px von unten, nach dem achten Eintrag nicht weiter staffeln.
`Web:` `animation-delay: calc(var(--i) * 50ms)`.
`React:` `npx shadcn@latest add @magicui/blur-fade` (mit `delay`)
`Compose:` Index in `itemsIndexed` → `LaunchedEffect` mit `delay(index * 50L)` auf ein `animateFloatAsState`.
`Barrierefreiheit:` ohne Bewegung alles sofort da.

### Liste wächst von oben (animated-list)
Neue Einträge schieben sich oben hinein, die anderen rücken nach.
`Passt zu:` daten, werkzeug, verspielt
`Dosierung:` für Ströme, die wirklich laufen (Meldungen, Aktivität). Nicht für statische Listen.
`Werte:` 400 ms, `cubic-bezier(.16,1,.3,1)`, Höhe und Deckkraft gemeinsam.
`Web:` FLIP-Technik oder `@starting-style` plus `transition`.
`React:` `npx shadcn@latest add @magicui/animated-list`
`Compose:` `Modifier.animateItem()` in `LazyColumn` – macht Einfügen, Entfernen und Umsortieren von allein.
`Barrierefreiheit:` neue Einträge höflich melden (`aria-live="polite"`).

### Laufband (marquee)
Eine Reihe zieht endlos seitwärts vorbei.
`Passt zu:` plakativ, regale, verspielt
`Dosierung:` für Logo-Reihen, Stichwörter, Cover. Nie für Text, den man lesen soll.
`Werte:` 25–40 s `linear` für eine Runde, Inhalt zweimal hintereinander, an den Rändern weich ausblenden.
`Web:` Inhalt verdoppeln, `transform: translateX(0 → -50%)`, Ränder per `mask-image`.
`React:` `npx shadcn@latest add @magicui/marquee`
`Compose:` `LazyRow` mit endlosem Index und `LaunchedEffect`, das `scrollBy` aufruft.
`Barrierefreiheit:` beim Zeigen anhalten; bei reduzierter Bewegung stehen lassen.

### Karte folgt dem Zeiger (magic-card)
Ein Lichtschein auf der Karte wandert mit dem Zeiger mit.
`Passt zu:` leuchten, werkzeug
`Dosierung:` auf Karten-Rastern am Rechner; auf dem Handy wirkungslos.
`Werte:` Schein 300 px, Deckkraft 0,15, folgt mit 120 ms Verzögerung.
`Web:` Mausposition in CSS-Variablen schreiben, `radial-gradient` daraus.
`React:` `npx shadcn@latest add @magicui/magic-card`
`Compose:` entfällt – stattdessen einen Druck- oder Fokus-Zustand verwenden.
`Barrierefreiheit:` reine Zierde, darf fehlen.

### Lichtkante (border-beam)
Ein Lichtpunkt läuft einmal um den Rand der Karte.
`Passt zu:` leuchten, werkzeug, daten
`Dosierung:` für genau ein hervorgehobenes Element (empfohlener Plan, laufender Vorgang).
`Werte:` 6 s `linear`, Dauerschleife, Punkt 20 % der Kantenlänge, Rahmen 1–2 px.
`Web:` `conic-gradient` als Rahmen, über `mask` auf die Kante begrenzt.
`React:` `npx shadcn@latest add @magicui/border-beam`
`Compose:` `Brush.sweepGradient` mit animiertem Winkel in `drawBehind`, innen die Fläche überzeichnen.
`Barrierefreiheit:` darf kein Zustand sein, den nur die Animation zeigt.

### Leuchtender Rahmen (shine-border)
Der Rahmen schimmert langsam in zwei bis drei Farben.
`Passt zu:` leuchten, verspielt
`Dosierung:` ruhiger als die Lichtkante, auch für mehrere Karten.
`Werte:` 8–14 s `linear`, Rahmen 1 px.
`Web:` wie Lichtkante, aber mit weichem Verlauf statt Punkt.
`React:` `npx shadcn@latest add @magicui/shine-border`
`Compose:` wie Lichtkante mit breiterem Verlauf.
`Barrierefreiheit:` unkritisch.

### Neon-Karte (neon-gradient-card)
Ein weiches Neonlicht liegt hinter der Karte.
`Passt zu:` leuchten
`Dosierung:` eine Karte je Screen.
`Werte:` `blur(24px)`, Deckkraft 0,5, Farbwechsel über 10 s.
`Web:` Kopie der Karte dahinter, unscharf, Verlauf animiert.
`React:` `npx shadcn@latest add @magicui/neon-gradient-card`
`Compose:` unscharfe Fläche hinter der Karte; `Modifier.blur()` ab API 31, sonst vorbereitete Grafik.
`Barrierefreiheit:` Inhalt der Karte bleibt auf eigener, deckender Fläche.

### Glanz beim Überfahren (glare-hover)
Ein harter Lichtbalken huscht schräg über eine Kachel.
`Passt zu:` buehne, galerie, plakativ
`Dosierung:` auf Bildkacheln, nicht auf Text.
`Werte:` 700 ms, `ease-out`, Balken 20° schräg.
`Web:` Pseudo-Element mit schrägem Verlauf und `translateX`.
`React:` `npx shadcn@latest add @magicui/glare-hover`
`Compose:` als Druck-Zustand umsetzen.
`Barrierefreiheit:` unkritisch.

### Lupe (lens)
Ein runder Ausschnitt vergrößert den Bereich unter dem Zeiger.
`Passt zu:` galerie, buehne
`Dosierung:` für Produkt- und Detailfotos.
`Werte:` Faktor 1,8–2,5, Kreis 140 px, folgt ohne Verzögerung.
`Web:` zweites, größeres Hintergrundbild in einem runden Element, Position aus der Mausposition.
`React:` `npx shadcn@latest add @magicui/lens`
`Compose:` auf dem Handy als Doppeltipp-Zoom mit `graphicsLayer` und `TransformableState`.
`Barrierefreiheit:` Zoom auch über Tastatur oder eine Schaltfläche anbieten.

### Dock mit Vergrößerung (dock)
Symbole in einer Leiste wachsen, wenn der Zeiger sie streift.
`Passt zu:` verspielt, galerie, minimal
`Dosierung:` für kleine Werkzeugleisten am Rechner.
`Werte:` Faktor bis 1,6, Umfeld bis 140 px, Feder statt fester Dauer.
`Web:` Abstand zum Zeiger je Symbol berechnen, daraus die Skalierung.
`React:` `npx shadcn@latest add @magicui/dock`
`Compose:` auf dem Handy entfällt es; auf dem TV ersetzt der Fokus-Zustand den Effekt.
`Barrierefreiheit:` Beschriftungen nicht nur beim Vergrößern zeigen.

### Kreisende Symbole (orbiting-circles)
Kleine Symbole kreisen um eine Mitte.
`Passt zu:` leuchten, verspielt, daten
`Dosierung:` als Bild für „alles verbindet sich“ – ein Mal, im Kopfbereich.
`Werte:` 20–30 s je Umlauf, zwei Bahnen gegenläufig.
`Web:` `@keyframes rotate` auf der Bahn, Gegenrotation auf dem Symbol.
`React:` `npx shadcn@latest add @magicui/orbiting-circles`
`Compose:` Winkel aus `rememberInfiniteTransition`, Position per Sinus und Kosinus im `Canvas` oder über `offset`.
`Barrierefreiheit:` reine Illustration, mit `aria-hidden` ausblenden.

### Verbindungsstrahl (animated-beam)
Ein Licht wandert auf einer Linie von einem Element zum anderen.
`Passt zu:` daten, werkzeug, leuchten
`Dosierung:` für Abläufe und Verbindungen (Quelle → App), zwei bis vier Linien.
`Werte:` 2–3 s `linear`, versetzt starten, Linie 1,5 px.
`Web:` SVG-Pfad zwischen zwei Elementen, `stroke-dasharray` plus wanderndes `stroke-dashoffset`.
`React:` `npx shadcn@latest add @magicui/animated-beam`
`Compose:` `Canvas` mit `drawPath` und `PathEffect.dashPathEffect`, Phase animiert.
`Barrierefreiheit:` die Verbindung muss auch ohne Bewegung erkennbar sein.

---

## Hintergrund und Atmosphäre

Höchstens **ein** Hintergrundeffekt je Screen, immer hinter einer deckenden Inhaltsfläche, nie unter Lesetext.

### Punktraster (dot-pattern)
Feines Punktraster, das sanft atmet oder beim Zeiger aufhellt.
`Passt zu:` werkzeug, minimal, daten
`Dosierung:` sehr ruhig halten, Deckkraft unter 0,15.
`Werte:` Abstand 16–24 px, Punkt 1 px.
`Web:` `radial-gradient` als sich wiederholender Hintergrund.
`React:` `npx shadcn@latest add @magicui/dot-pattern`
`Compose:` `drawBehind` mit zwei Schleifen und `drawCircle`.
`Barrierefreiheit:` unkritisch.

### Linienraster (grid-pattern)
Dünnes Gitternetz, einzelne Felder leuchten kurz auf.
`Passt zu:` werkzeug, daten, retro
`Dosierung:` wie Punktraster.
`Werte:` Feld 40 px, Linie 1 px, Aufleuchten 1,2 s versetzt.
`Web:` zwei `repeating-linear-gradient`; einzelne Felder als absolute Kacheln.
`React:` `npx shadcn@latest add @magicui/grid-pattern` bzw. `animated-grid-pattern`
`Compose:` `drawBehind` mit `drawLine`.
`Barrierefreiheit:` unkritisch.

### Flackerndes Raster (flickering-grid)
Kacheln blinken zufällig auf und ab.
`Passt zu:` retro, leuchten, werkzeug
`Dosierung:` sparsam – das Flackern zieht Blicke.
`Werte:` Kachel 4–8 px, Wechsel alle 300–600 ms, Deckkraft bis 0,3.
`Web:` `<canvas>` mit zufälligen Kacheln.
`React:` `npx shadcn@latest add @magicui/flickering-grid`
`Compose:` `Canvas` mit zufälligen Rechtecken, in Schritten statt je Bild erneuert.
`Barrierefreiheit:` nicht schneller als dreimal je Sekunde; bei reduzierter Bewegung aus.

### Retro-Gitter (retro-grid)
Ein perspektivisches Gitter läuft zum Horizont, wie Synthwave.
`Passt zu:` retro, leuchten, verspielt
`Dosierung:` ein Kopfbereich, nie ganzflächig.
`Werte:` 15 s `linear`, Neigung 60°, oben weich ausblenden.
`Web:` `transform: rotateX(60deg)` auf einem Linienraster, Position animiert, `mask-image` nach oben.
`React:` `npx shadcn@latest add @magicui/retro-grid`
`Compose:` `Canvas` mit perspektivisch verdichteten Linien.
`Barrierefreiheit:` unkritisch.

### Meteoriten (meteors)
Lichtstreifen fallen schräg durchs Bild.
`Passt zu:` leuchten, buehne
`Dosierung:` 8–20 Stück, nur im Kopfbereich.
`Werte:` 3–8 s je Streifen, zufälliger Start, Schweif 50–120 px.
`Web:` absolute Elemente mit Schweif-Verlauf und `translate` plus `rotate`.
`React:` `npx shadcn@latest add @magicui/meteors`
`Compose:` `Canvas` mit wenigen Linien; viele bewegte Teilchen kosten auf dem Handy Akku.
`Barrierefreiheit:` ohne Bewegung ein ruhiges Standbild.

### Teilchen (particles)
Punkte schweben langsam und weichen dem Zeiger aus.
`Passt zu:` leuchten, buehne, minimal
`Dosierung:` Dichte niedrig halten; auf dem Handy höchstens 40 Teilchen.
`Werte:` 30–80 Teilchen, Geschwindigkeit 0,2–0,6 px je Bild.
`Web:` `<canvas>` mit kleiner Eigenbewegung.
`React:` `npx shadcn@latest add @magicui/particles`
`Compose:` möglich, aber teuer – auf Android lieber ein vorbereiteter Verlauf mit leichter Bewegung.
`Barrierefreiheit:` bei reduzierter Bewegung einfrieren.

### Lichtstrahlen (light-rays)
Weiche Strahlen fallen von oben ins Bild.
`Passt zu:` buehne, leuchten, editorial
`Dosierung:` sehr ruhig, Deckkraft unter 0,25.
`Werte:` 12–20 s `linear`, zwei bis drei Strahlen, `blur(30px)`.
`Web:` schräge, unscharfe Verlaufsflächen mit wanderndem Winkel.
`React:` `npx shadcn@latest add @magicui/light-rays`
`Compose:` `Brush.linearGradient` in `drawBehind`, Winkel animiert.
`Barrierefreiheit:` unkritisch.

### Wellenwand (warp-background)
Gekrümmte Linien strömen in die Tiefe.
`Passt zu:` leuchten, verspielt
`Dosierung:` ein Kopfbereich je App.
`Werte:` 8–12 s `linear`, 12–20 Bahnen.
`Web:` CSS-Perspektive mit versetzten Kacheln.
`React:` `npx shadcn@latest add @magicui/warp-background`
`Compose:` `Canvas` mit Bézier-Pfaden; aufwendig, meist verzichtbar.
`Barrierefreiheit:` kann Unwohlsein auslösen – bei reduzierter Bewegung immer aus.

### Ringwellen (ripple)
Konzentrische Ringe gehen ruhig von einem Punkt aus.
`Passt zu:` minimal, leuchten, daten
`Dosierung:` gut hinter einem Symbol in der Mitte (Verbindung, Suche, Aufnahme).
`Werte:` 3 Ringe, je 3 s, Versatz 1 s, Skalierung 1 → 2, Deckkraft 0,4 → 0.
`Web:` drei Kreise mit `@keyframes` und `animation-delay`.
`React:` `npx shadcn@latest add @magicui/ripple`
`Compose:` `rememberInfiniteTransition` auf Radius und Alpha im `Canvas`.
`Barrierefreiheit:` unkritisch.

### Körnung (noise-texture)
Feines, ruhiges Rauschen über der Fläche.
`Passt zu:` editorial, buehne, retro, plakativ
`Dosierung:` statisch lassen – bewegtes Rauschen flimmert und kostet Rechenzeit.
`Werte:` Deckkraft 0,04–0,12, `mix-blend-mode: overlay`, Kachel 160 px.
`Web:` SVG-`feTurbulence` als Hintergrundkachel.
`React:` `npx shadcn@latest add @magicui/noise-texture`
`Compose:` kleines, gekacheltes Rausch-Bild mit `TileMode.Repeated`.
`Barrierefreiheit:` Textkontrast nach dem Auflegen erneut prüfen.

### Verlaufende Unschärfe (progressive-blur)
Der Rand einer Fläche wird nach außen immer unschärfer.
`Passt zu:` buehne, galerie, minimal
`Dosierung:` an Kanten von Bildbereichen und über festen Leisten.
`Werte:` mehrere Stufen `blur(2px)` bis `blur(16px)`, je mit eigener Maske.
`Web:` gestapelte Schichten mit `backdrop-filter` und `mask-image`.
`React:` `npx shadcn@latest add @magicui/progressive-blur`
`Compose:` Verlaufsfläche statt echter Unschärfe (billiger und genauso wirksam).
`Barrierefreiheit:` Text darf nicht in der unscharfen Zone liegen.

### Drehende Schrift im Kreis (spinning-text)
Text läuft auf einer Kreisbahn, der Kreis dreht sich.
`Passt zu:` verspielt, editorial, plakativ
`Dosierung:` als Siegel oder Abzeichen, eines je Screen.
`Werte:` 12–20 s `linear`.
`Web:` SVG `textPath` auf einem Kreis, `@keyframes rotate`.
`React:` `npx shadcn@latest add @magicui/spinning-text`
`Compose:` `Canvas` mit `drawTextOnPath` über `nativeCanvas`.
`Barrierefreiheit:` Text zusätzlich als Beschriftung hinterlegen.

---

## Übergänge und Navigation

### Gemeinsames Element (shared element)
Ein Bild wächst beim Öffnen aus der Kachel in die Detailansicht.
`Passt zu:` galerie, regale, buehne
`Dosierung:` für den Weg Liste → Detail; der wirksamste Übergang überhaupt.
`Werte:` 320–400 ms, `cubic-bezier(.2,0,0,1)`, Bild und Titel gemeinsam.
`Web:` View Transitions API mit `view-transition-name` auf beiden Seiten.
`React:` —
`Compose:` `SharedTransitionLayout` mit `Modifier.sharedElement(...)` je Paar.
`Barrierefreiheit:` ohne Bewegung einfach überblenden.

### Screenwechsel (navigation transition)
Der neue Screen kommt von der Seite oder blendet auf.
`Passt zu:` alle
`Dosierung:` eine Regel für die ganze App, nicht je Screen eine andere.
`Werte:` hinein 300 ms von rechts, hinaus 250 ms nach links um 30 %; Modal von unten 350 ms.
`Web:` View Transitions oder `@keyframes` beim Routenwechsel.
`React:` —
`Compose:` `enterTransition`/`exitTransition` in `NavHost`, oder `AnimatedContent`.
`Barrierefreiheit:` ohne Bewegung hart schneiden.

### Blatt von unten (bottom sheet)
Eine Fläche fährt von unten herein, der Hintergrund verdunkelt sich.
`Passt zu:` alle (App-Standard)
`Dosierung:` für Auswahl und Nebenaktionen statt eines Dialogs.
`Werte:` 300 ms hinein `cubic-bezier(.16,1,.3,1)`, 220 ms hinaus, Abdunklung bis 40 %.
`Web:` `translateY(100% → 0)` plus Abdunklungsfläche.
`Compose:` `ModalBottomSheet`; eigene Form und Griffleiste nach Profil.
`Barrierefreiheit:` Fokus hineinführen, mit Esc bzw. Zurück schließbar.

### Fortschritt beim Scrollen (scroll-progress)
Ein dünner Balken oben zeigt, wie weit man ist.
`Passt zu:` editorial, daten, werkzeug
`Dosierung:` für lange Lesetexte, nicht für kurze Screens.
`Werte:` 2–3 px, Akzentfarbe, ohne Verzögerung.
`Web:` `scroll-timeline`/`animation-timeline: scroll()` oder `scroll`-Ereignis.
`React:` `npx shadcn@latest add @magicui/scroll-progress`
`Compose:` `LinearProgressIndicator` aus `LazyListState`.
`Barrierefreiheit:` keine Bedeutung allein über Farbe.

### Tempo aus dem Scrollen (scroll-based-velocity)
Eine Reihe läuft schneller, je schneller man scrollt, und kehrt die Richtung um.
`Passt zu:` plakativ, verspielt, editorial
`Dosierung:` ein Band je Seite.
`Werte:` Grundtempo 20 s, Faktor bis 3, Richtung aus dem Vorzeichen.
`Web:` Scrollgeschwindigkeit messen, auf die Bandposition legen.
`React:` `npx shadcn@latest add @magicui/scroll-based-velocity`
`Compose:` `LazyListState.firstVisibleItemScrollOffset` ableiten und auf ein `LazyRow` legen.
`Barrierefreiheit:` bei reduzierter Bewegung stehen lassen.

### Fokus auf dem Fernseher (tv focus)
Die ausgewählte Karte hebt sich deutlich hervor.
`Passt zu:` regale, buehne, galerie
`Dosierung:` Pflicht auf Android TV – ohne klaren Fokus ist die App unbedienbar.
`Werte:` Skalierung 1,08, 150 ms, zusätzlich Rahmen 2 px oder Leuchten; Nachbarn leicht abdunkeln.
`Web:` `:focus-visible` mit `transform` und `outline`.
`Compose (TV):` `Modifier.onFocusChanged` → `animateFloatAsState` auf `graphicsLayer`; `androidx.tv.material3` nutzt `border`/`borderVariant` statt `outline`.
`Barrierefreiheit:` nie nur über Farbe – immer auch Größe oder Rahmen.

### Zum Aktualisieren ziehen (pull to refresh)
Oben erscheint ein Anzeiger, der sich beim Ziehen aufbaut.
`Passt zu:` alle
`Dosierung:` auf Listen, die sich von außen ändern.
`Werte:` Auslösung bei 80 dp, Anzeiger dreht sich mit dem Zug, Rücklauf 250 ms.
`Web:` `touchmove` abgreifen, Anzeiger an die Strecke koppeln.
`Compose:` `PullToRefreshBox`; Anzeiger an die Marke anpassen.
`Barrierefreiheit:` zusätzlich eine Schaltfläche zum Aktualisieren anbieten.

---

## Zustände: Laden, Leer, Fehler, Erfolg

### Skelett mit Schimmer (skeleton)
Graue Platzhalter in der Form des späteren Inhalts, ein Lichtstreifen läuft darüber.
`Passt zu:` alle
`Dosierung:` ab etwa 300 ms Wartezeit; darunter gar nichts zeigen, sonst blitzt es.
`Werte:` 1,4 s `linear`, Dauerschleife, Streifen 30 %, Grundfläche eine Stufe heller als der Hintergrund.
`Web:` `linear-gradient` mit `background-size: 200%`, Position animiert.
`React:` —
`Compose:` `rememberInfiniteTransition` auf den Offset eines `Brush.linearGradient` in `Modifier.background`.
`Barrierefreiheit:` Ladezustand melden (`aria-busy` bzw. `stateDescription`).

### Kreisfortschritt (animated-circular-progress-bar)
Ein Ring füllt sich auf den Prozentwert.
`Passt zu:` daten, werkzeug, verspielt
`Dosierung:` für Speicher, Fortschritt, Anteile.
`Werte:` 800 ms, `cubic-bezier(.16,1,.3,1)`, Ring 6–10 px, Zahl zählt mit.
`Web:` SVG-Kreis mit `stroke-dasharray` und animiertem `stroke-dashoffset`.
`React:` `npx shadcn@latest add @magicui/animated-circular-progress-bar`
`Compose:` `animateFloatAsState` auf den Winkel, `drawArc`.
`Barrierefreiheit:` Prozentwert auch als Text.

### Unbestimmtes Laden
Ein Balken oder Ring läuft, solange die Dauer unbekannt ist.
`Passt zu:` alle
`Dosierung:` nur, wenn der Fortschritt wirklich unbekannt ist – sonst den echten Wert zeigen.
`Werte:` Balken 1,8 s `cubic-bezier(.65,.05,.36,1)`, Dauerschleife.
`Web:` `@keyframes` auf `transform: translateX` und `scaleX`.
`Compose:` `LinearProgressIndicator()` ohne Wert.
`Barrierefreiheit:` nach langer Zeit erklären, worauf gewartet wird.

### Leerer Zustand, der ankommt
Symbol und Text blenden sanft ein, das Symbol bewegt sich einmal leicht.
`Passt zu:` alle
`Dosierung:` zurückhaltend; der leere Zustand soll weiterhelfen, nicht unterhalten.
`Werte:` 400 ms einblenden, Symbol 600 ms mit 4 px Hub.
`Web:` `@keyframes` auf `opacity` und `translateY`.
`Compose:` `AnimatedVisibility` plus einmalige `animateFloatAsState`-Bewegung.
`Barrierefreiheit:` der Text erklärt den Zustand, nicht die Bewegung.

### Fehler: kurzes Rütteln
Das Feld wackelt einmal seitlich.
`Passt zu:` alle
`Dosierung:` einmal je Fehler, nur bei Eingaben.
`Werte:` 300 ms, ±6 px, drei Ausschläge.
`Web:` `@keyframes` auf `translateX`.
`Compose:` `animateFloatAsState` mit `keyframes { … }` auf den Versatz.
`Barrierefreiheit:` Fehler immer zusätzlich als Text; Bewegung allein genügt nicht. Bei reduzierter Bewegung nur Farbe und Text.

### Erfolg: Häkchen zeichnet sich
Ein Häkchen wird in einem Zug gezeichnet, der Kreis schließt sich.
`Passt zu:` alle
`Dosierung:` für abgeschlossene Vorgänge; danach wieder in den Ruhezustand.
`Werte:` Kreis 300 ms, Häkchen 250 ms mit 100 ms Versatz, `ease-out`.
`Web:` SVG-Pfad mit `stroke-dasharray`/`stroke-dashoffset`.
`Compose:` `animateFloatAsState` auf den Pfadanteil, `drawPath` mit `PathMeasure`.
`Barrierefreiheit:` Erfolg auch melden (`aria-live`), nicht nur zeigen.

### Meldung von unten (snackbar)
Eine kurze Meldung fährt unten herein und geht von allein wieder.
`Passt zu:` alle
`Dosierung:` für Rückmeldungen mit Rückgängig-Möglichkeit.
`Werte:` 250 ms herein, 4 s stehen, 200 ms hinaus.
`Web:` `translateY` plus `opacity`, Zeitgeber.
`Compose:` `SnackbarHost`; Form und Farben nach Profil.
`Barrierefreiheit:` lange genug stehen lassen; mit Aktion nicht automatisch schließen.

---

## Nicht enthalten

Einige Magic-UI-Bausteine sind keine Animationen, sondern fertige Bauteile: Globus, Geräte-Rahmen (iPhone, Android, Safari), Dateibaum, Tweet-Karte, Landkarte, Code-Vergleich, Terminal, Symbol-Wolke. Wer so etwas braucht, baut es als eigenen Baustein in der Designsprache der gewählten Marke – die Bewegung darin kommt dann aus diesem Katalog.
