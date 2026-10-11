"""Vorschau-Werkzeuge bauen: tools/vorschau/icons.js und tools/vorschau/vorlage.html.

Beide Dateien werden von Schritt 3 und Schritt 7 des Skills benutzt: `vorlage.html` wird als
`<Projekt>/design-vorschau/index.html` ins Projekt kopiert, `icons.js` daneben gelegt. Die Seite
läuft dann ohne Internet direkt aus `file://` und lädt nur `./icons.js`.

Aufruf (aus dem Ordner dieses Skills):
  python3 -I tools/build_vorschau.py
  python3 -I tools/build_vorschau.py --icons /home/claude/src/icons --out tools/vorschau

Optionen:
  --icons DIR   Ordner mit den Icon-Sammlungen (Standard: /home/claude/src/icons)
                DIR/lucide/icons/<name>.svg und DIR/phosphor/assets/<stärke>/<name>[-<stärke>].svg
                  git clone --depth 1 https://github.com/lucide-icons/lucide   DIR/lucide
                  git clone --depth 1 https://github.com/phosphor-icons/core   DIR/phosphor
  --out DIR     Zielordner (Standard: <Ordner dieses Skripts>/vorschau)
  --renderer F  Pfad zu render_screens.py (Standard: <Ordner dieses Skripts>/render_screens.py);
                daraus kommen `base_css()` (Basis-CSS mit eingebetteten Motiven) und die Icon-
                Erzeugung, damit die Vorschau genau dasselbe Markup wie die Musterscreens hat.

Das Ergebnis ist bei gleicher Eingabe Byte für Byte gleich (keine Zeitstempel, feste Reihenfolge).
Fehlt ein Icon in den Sammlungen, bricht der Lauf mit einer Liste ab.

Icon-Lizenzen: Lucide (ISC), Phosphor Icons (MIT) – beide erlauben die Weitergabe mit Lizenzhinweis.
Der Hinweis steht im Kopf von icons.js.
"""

import argparse
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent

PH_WEIGHTS = ["thin", "light", "regular", "bold", "fill", "duotone"]

# Icon-Satz: (Bereich, [(logischer Name, Lucide-Name, Phosphor-Name), …]).
# Logische Namen sind deutsch, damit man im Kopf von icons.js nach dem Bedarf suchen kann;
# Schlüssel in der Datei sind die echten Namen der Sammlungen (lucide:… / ph-<stärke>:…).
ICONS = [
    ("Navigation", [
        ("haus", "house", "house"),
        ("suchen", "search", "magnifying-glass"),
        ("entdecken", "compass", "compass"),
        ("menue", "menu", "list"),
        ("schliessen", "x", "x"),
        ("zurueck", "chevron-left", "caret-left"),
        ("weiter", "chevron-right", "caret-right"),
        ("hoch", "chevron-up", "caret-up"),
        ("runter", "chevron-down", "caret-down"),
        ("pfeil-links", "arrow-left", "arrow-left"),
        ("pfeil-rechts", "arrow-right", "arrow-right"),
        ("mehr", "ellipsis", "dots-three"),
        ("mehr-vertikal", "ellipsis-vertical", "dots-three-vertical"),
        ("anheften", "pin", "push-pin"),
        ("raster", "layout-grid", "squares-four"),
        ("liste", "list", "list-dashes"),
        ("filter", "funnel", "funnel"),
        ("sortieren", "arrow-up-down", "sort-ascending"),
    ]),
    ("Medien", [
        ("abspielen", "play", "play"),
        ("pause", "pause", "pause"),
        ("naechster", "skip-forward", "skip-forward"),
        ("vorheriger", "skip-back", "skip-back"),
        ("zufall", "shuffle", "shuffle"),
        ("wiederholen", "repeat", "repeat"),
        ("lauter", "volume-2", "speaker-high"),
        ("stumm", "volume-x", "speaker-x"),
        ("mikrofon", "mic", "microphone"),
        ("kopfhoerer", "headphones", "headphones"),
        ("musik", "music", "music-note"),
        ("noten", "music-4", "music-notes"),
        ("podcast", "audio-lines", "microphone-stage"),
        ("warteschlange", "list-music", "playlist"),
    ]),
    ("Aktionen", [
        ("plus", "plus", "plus"),
        ("plus-kreis", "circle-plus", "plus-circle"),
        ("minus", "minus", "minus"),
        ("haken", "check", "check"),
        ("bearbeiten", "pencil", "pencil-simple"),
        ("loeschen", "trash", "trash"),
        ("kopieren", "copy", "copy"),
        ("teilen", "share-2", "share-network"),
        ("herunterladen", "download", "download-simple"),
        ("hochladen", "upload", "upload-simple"),
        ("merken", "bookmark", "bookmark-simple"),
        ("gefaellt-mir", "heart", "heart"),
        ("stern", "star", "star"),
        ("daumen-hoch", "thumbs-up", "thumbs-up"),
        ("neu-laden", "refresh-cw", "arrows-clockwise"),
        ("senden", "send", "paper-plane-tilt"),
        ("verknuepfung", "link", "link-simple"),
        ("qr-code", "qr-code", "qr-code"),
    ]),
    ("Status", [
        ("info", "info", "info"),
        ("warnung", "triangle-alert", "warning"),
        ("fehler", "circle-x", "x-circle"),
        ("erfolg", "circle-check", "check-circle"),
        ("hilfe", "circle-question-mark", "question"),
        ("glocke", "bell", "bell"),
        ("signal", "signal", "cell-signal-full"),
        ("laden", "loader-circle", "spinner"),
        ("gesperrt", "lock", "lock"),
        ("schild", "shield", "shield-check"),
        ("sichtbar", "eye", "eye"),
        ("unsichtbar", "eye-off", "eye-slash"),
    ]),
    ("Einstellungen und Konto", [
        ("einstellungen", "settings", "gear"),
        ("regler", "sliders-horizontal", "sliders-horizontal"),
        ("person", "user", "user"),
        ("person-kreis", "circle-user-round", "user-circle"),
        ("personen", "users", "users"),
        ("abmelden", "log-out", "sign-out"),
        ("schluessel", "key", "key"),
        ("farben", "palette", "palette"),
        ("mond", "moon", "moon"),
        ("sonne", "sun", "sun"),
    ]),
    ("Dateien und Speicher", [
        ("datei", "file", "file"),
        ("textdatei", "file-text", "file-text"),
        ("ordner", "folder", "folder"),
        ("ordner-offen", "folder-open", "folder-open"),
        ("archiv", "archive", "archive"),
        ("festplatte", "hard-drive", "hard-drives"),
        ("datenbank", "database", "database"),
        ("server", "server", "hard-drive"),
        ("wolke", "cloud", "cloud"),
        ("wolke-hoch", "cloud-upload", "cloud-arrow-up"),
        ("wolke-runter", "cloud-download", "cloud-arrow-down"),
        ("usb", "usb", "usb"),
        ("bild", "image", "image"),
        ("galerie", "images", "images-square"),
        ("bibliothek", "library", "books"),
        ("video", "video", "video-camera"),
        ("clip", "paperclip", "paperclip"),
    ]),
    ("Geräte", [
        ("fernseher", "tv", "television"),
        ("bildschirm", "monitor", "monitor"),
        ("geraete", "monitor-smartphone", "devices"),
        ("handy", "smartphone", "device-mobile"),
        ("laptop", "laptop", "laptop"),
        ("lautsprecher", "speaker", "speaker-hifi"),
        ("streamen", "cast", "screencast"),
        ("wlan", "wifi", "wifi-high"),
        ("bluetooth", "bluetooth", "bluetooth"),
        ("akku", "battery-full", "battery-full"),
        ("kamera", "camera", "camera"),
    ]),
    ("Kommunikation", [
        ("mail", "mail", "envelope"),
        ("nachricht", "message-circle", "chat-circle"),
        ("telefon", "phone", "phone"),
        ("eingang", "inbox", "tray"),
    ]),
    ("Handel", [
        ("einkaufswagen", "shopping-cart", "shopping-cart"),
        ("einkaufstasche", "shopping-bag", "shopping-bag"),
        ("karte-kredit", "credit-card", "credit-card"),
        ("geldbeutel", "wallet", "wallet"),
        ("etikett", "tag", "tag"),
        ("beleg", "receipt", "receipt"),
        ("geschenk", "gift", "gift"),
        ("lieferung", "truck", "truck"),
        ("paket", "package", "package"),
        ("euro", "euro", "currency-eur"),
    ]),
    ("Essen und Kochen", [
        ("besteck", "utensils", "fork-knife"),
        ("kochmuetze", "chef-hat", "chef-hat"),
        ("topf", "cooking-pot", "cooking-pot"),
        ("kaffee", "coffee", "coffee"),
        ("wein", "wine", "wine"),
    ]),
    ("Gesundheit und Sport", [
        ("puls", "activity", "pulse"),
        ("herz-puls", "heart-pulse", "heartbeat"),
        ("schritte", "footprints", "footprints"),
        ("hantel", "dumbbell", "barbell"),
        ("fahrrad", "bike", "person-simple-bike"),
        ("bett", "bed-single", "bed"),
        ("tropfen", "droplet", "drop"),
        ("flamme", "flame", "flame"),
    ]),
    ("Reise und Karten", [
        ("landkarte", "map", "map-trifold"),
        ("ort", "map-pin", "map-pin"),
        ("navigation", "navigation", "navigation-arrow"),
        ("globus", "globe", "globe"),
        ("flugzeug", "plane", "airplane-tilt"),
        ("auto", "car", "car"),
        ("zug", "train-front", "train"),
        ("bus", "bus", "bus"),
        ("koffer", "briefcase", "suitcase-rolling"),
        ("ticket", "ticket", "ticket"),
        ("route", "route", "path"),
    ]),
    ("Bearbeiten", [
        ("schrift", "type", "text-aa"),
        ("pinsel", "brush", "paint-brush"),
        ("zuschneiden", "crop", "crop"),
        ("ebenen", "layers", "stack"),
    ]),
    ("Diagramme", [
        ("balken", "chart-column", "chart-bar"),
        ("linie", "chart-line", "chart-line"),
        ("kreis-diagramm", "chart-pie", "chart-pie-slice"),
        ("trend-hoch", "trending-up", "trend-up"),
        ("trend-runter", "trending-down", "trend-down"),
        ("ziel", "target", "target"),
        ("tacho", "gauge", "gauge"),
        ("tabelle", "table", "table"),
    ]),
    ("Wetter", [
        ("regen", "cloud-rain", "cloud-rain"),
        ("schnee", "cloud-snow", "cloud-snow"),
        ("wind", "wind", "wind"),
        ("thermometer", "thermometer", "thermometer"),
        ("regenschirm", "umbrella", "umbrella"),
    ]),
    ("Zeit", [
        ("uhr", "clock", "clock"),
        ("kalender", "calendar", "calendar-blank"),
        ("wecker", "alarm-clock", "alarm"),
        ("stoppuhr", "timer", "timer"),
        ("verlauf", "rotate-ccw", "clock-counter-clockwise"),
    ]),
]


def lade_renderer(pfad):
    """render_screens.py als Modul laden (für base_css() und die Icon-Klasse)."""
    pfad = pathlib.Path(pfad).resolve()
    if not pfad.exists():
        sys.exit(f"render_screens.py nicht gefunden: {pfad}")
    spec = importlib.util.spec_from_file_location("render_screens_fuer_vorschau", pfad)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def js_text(s):
    """Inneres SVG-Markup als JS-Zeichenkette (doppelte Anführungszeichen)."""
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("</", '<\\/') + '"'


def aus_musterscreens(screens_dir):
    """Jeden Icon-Namen sammeln, den die Musterscreens verwenden (data-i="satz:name").

    Die Musterscreens entstehen mit dem vollen Lucide- und Phosphor-Vorrat, der
    Vorschau-Satz ist eine Auswahl. Ohne diesen Abgleich fehlen beim Übernehmen
    von Bausteinen aus screens/<slug>.html genau die Icons der Marke.
    """
    namen = set()
    d = pathlib.Path(screens_dir)
    if not d.is_dir():
        return namen
    for f in sorted(d.glob("*.html")):
        namen |= set(re.findall(r'data-i="([a-z-]+:[a-z0-9-]+)"', f.read_text(encoding="utf-8")))
    return namen


def icons_js(renderer, icons_root, screens_dir=None):
    """icons.js erzeugen: je Icon eine Zeile, Schlüssel sind die echten Namen der Sammlungen."""
    lader = renderer.Icons(pathlib.Path(icons_root))
    fehlt, zeilen, tabelle = [], [], []
    gesetzt = set()

    def aufnehmen(spec):
        if spec in gesetzt:
            return True
        icon = lader.load(spec)
        if icon is None:
            return False
        gesetzt.add(spec)
        zeilen.append(f'"{spec}":{js_text(icon[2])},')
        return True

    for bereich, eintraege in ICONS:
        tabelle.append(f"   {bereich}")
        for logisch, lu, ph in eintraege:
            tabelle.append(f"     {logisch:<20} lucide:{lu:<24} ph-*:{ph}")
            for spec in [f"lucide:{lu}"] + [f"ph-{w}:{ph}" for w in PH_WEIGHTS]:
                if not aufnehmen(spec):
                    fehlt.append(spec)
    if fehlt:
        sys.exit("Icons fehlen in den Sammlungen:\n  " + "\n  ".join(fehlt))

    # Alles ergänzen, was die Musterscreens brauchen – jeweils die ganze Familie,
    # damit sich die Strichstärke in der Vorschau noch wechseln lässt.
    dazu = []
    for spec in sorted(aus_musterscreens(screens_dir) if screens_dir else ()):
        satz, _, name = spec.partition(":")
        familie = [f"lucide:{name}"] + [f"ph-{w}:{name}" for w in PH_WEIGHTS]
        neu = [x for x in familie if x not in gesetzt and aufnehmen(x)]
        if spec not in gesetzt:
            sys.exit(f"Musterscreens nutzen {spec}, das es in den Sammlungen nicht gibt")
        if neu:
            dazu.append(name)
    if dazu:
        tabelle.append("   Aus den Musterscreens ergänzt")
        for name in sorted(set(dazu)):
            tabelle.append(f"     {name}")

    anzahl = sum(len(e) for _, e in ICONS) + len(set(dazu))
    kopf = [
        "/* icons.js – Icon-Vorrat für die Designvorschau des All Top Brands Design Skills.",
        "   Erzeugt von tools/build_vorschau.py – nicht von Hand ändern.",
        "",
        f"   {anzahl} Icons, jedes als Lucide-Strichvariante und in allen sechs Phosphor-Stärken",
        f"   (thin, light, regular, bold, fill, duotone) = {len(zeilen)} Einträge.",
        "",
        "   Benutzung in der Seite:  <i data-icon=\"lucide:house\"></i>",
        "                            <i data-icon=\"ph-bold:house\" class=\"gross\"></i>",
        "   VorschauIcons.ersetzen(wurzel) tauscht alle <i data-icon=\"…\"> gegen Inline-SVG mit",
        "   genau dem Markup der Musterscreens (Klassen \"ic ic-l\" bzw. \"ic ic-p ic-ph-<stärke>\",",
        "   data-i=\"<satz>:<name>\"), damit aus screens/<slug>.html übernommenes CSS unverändert greift.",
        "   Fehlt ein Name, erscheint ein kleines rot gestricheltes Kästchen (.ic-missing) und eine",
        "   Warnung in der Konsole.",
        "",
        "   Lizenzen (beide erlauben Weitergabe mit Lizenzhinweis):",
        "     Lucide – ISC-Lizenz – https://lucide.dev – © Lucide Contributors",
        "       (abgeleitet von Feather Icons, MIT, © Cole Bemis)",
        "     Phosphor Icons – MIT-Lizenz – https://phosphoricons.com – © Phosphor Icons",
        "   Das sind freie Icon-Sammlungen, keine Markenzeichen der nachgebildeten Marken.",
        "",
        "   Namensliste zum Durchsuchen – logischer Name, Lucide-Name, Phosphor-Name:",
        "",
    ] + tabelle + ["*/", ""]

    api = """
window.VorschauIcons = (function () {
  "use strict";
  // Wurzel-Attribute und Klassen je Satz – identisch zu class Icons in tools/render_screens.py
  var SATZ = {
    "lucide": ["ic ic-l", 'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'],
    "ph-thin": ["ic ic-p ic-ph-thin", 'viewBox="0 0 256 256" fill="currentColor"'],
    "ph-light": ["ic ic-p ic-ph-light", 'viewBox="0 0 256 256" fill="currentColor"'],
    "ph-regular": ["ic ic-p ic-ph-regular", 'viewBox="0 0 256 256" fill="currentColor"'],
    "ph-bold": ["ic ic-p ic-ph-bold", 'viewBox="0 0 256 256" fill="currentColor"'],
    "ph-fill": ["ic ic-p ic-ph-fill", 'viewBox="0 0 256 256" fill="currentColor"'],
    "ph-duotone": ["ic ic-p ic-ph-duotone", 'viewBox="0 0 256 256" fill="currentColor"']
  };
  var FEHLT = '<svg class="ic ic-missing" viewBox="0 0 24 24" aria-hidden="true">'
            + '<rect width="24" height="24" fill="red" opacity=".45"/></svg>';

  function schutz(s) {
    return String(s).replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;");
  }

  // Markup eines Icons. zusatzKlasse: zusätzliche Klassen, restAttribute: fertige Attribut-Zeichenkette.
  function markup(spec, zusatzKlasse, restAttribute) {
    spec = String(spec || "").trim();
    var i = spec.indexOf(":");
    var satz = i < 0 ? "" : spec.slice(0, i);
    var s = SATZ[satz], inner = DATEN[spec];
    if (!s || inner === undefined) {
      console.warn("Icon fehlt: \\"" + spec + "\\" – in icons.js nicht vorhanden. "
                 + "Verfügbare Namen stehen im Kopf von icons.js.");
      return FEHLT;
    }
    var klasse = (s[0] + " " + (zusatzKlasse || "")).trim();
    return '<svg class="' + schutz(klasse) + '" ' + s[1] + ' aria-hidden="true" data-i="'
         + schutz(spec) + '"' + (restAttribute || "") + ">" + inner + "</svg>";
  }

  // Alle <i data-icon="…"> unter wurzel ersetzen. Gibt die Zahl der fehlenden Icons zurück.
  function ersetzen(wurzel) {
    var liste = (wurzel || document).querySelectorAll("i[data-icon]");
    var fehlend = 0;
    for (var n = 0; n < liste.length; n++) {
      var el = liste[n], klasse = "", rest = "";
      for (var k = 0; k < el.attributes.length; k++) {
        var at = el.attributes[k];
        if (at.name === "data-icon") continue;
        if (at.name === "class") { klasse = at.value; continue; }
        rest += " " + at.name + '="' + schutz(at.value) + '"';
      }
      var m = markup(el.getAttribute("data-icon"), klasse, rest);
      if (m === FEHLT) fehlend++;
      el.outerHTML = m;
    }
    return fehlend;
  }

  function namen(satz) {
    var out = [];
    for (var k in DATEN) if (!satz || k.indexOf(satz + ":") === 0) out.push(k);
    return out.sort();
  }

  return { markup: markup, ersetzen: ersetzen, namen: namen, daten: DATEN, saetze: Object.keys(SATZ) };
})();
"""
    # DATEN steht vor dem Abschluss und im gleichen Skript-Gültigkeitsbereich; die Funktionen
    # darin greifen darauf zu. Je Icon eine Zeile – gut zum Durchsuchen mit grep.
    return "\n".join(kopf) + "var DATEN = {\n" + "\n".join(zeilen).rstrip(",") + "\n};\n" + api


def vorlage_html(renderer):
    """vorlage.html erzeugen: Basis-CSS eingebettet, Seitenstile, Beispielkarte, kleines Skript."""
    css = renderer.base_css()
    if re.search(r"\{\{scene:[\w-]+\}\}", css):
        sys.exit("Basis-CSS enthält noch {{scene:…}}-Platzhalter – tools/screens/scenes/ prüfen.")
    return VORLAGE.replace("/*{{BASIS_CSS}}*/", css)


VORLAGE = r"""<!doctype html>
<!-- ===========================================================================================
     Designvorschau – Vorlage des All Top Brands Design Skills
     Erzeugt von tools/build_vorschau.py. Nicht die Vorlage im Skill-Ordner bearbeiten, sondern
     die Kopie im Projekt:
         cp tools/vorschau/vorlage.html <Projekt>/design-vorschau/index.html
         cp tools/vorschau/icons.js    <Projekt>/design-vorschau/icons.js

     Die Seite ist eigenständig (Basis-CSS und Bildmotive sind eingebettet) und lädt nur ./icons.js.
     Sie läuft offline direkt aus file:// – `open`/`xdg-open` genügt, kein Server.

     Ohne Desktop (Sitzung ohne Bildschirm, kein `open`/`xdg-open`): die Seite mit Playwright
     fotografieren (Chromium, file://-Adresse, einmal 1440 px und einmal 390 px breit, full_page)
     und die Bilder SELBST ansehen, bevor die Seite dem Nutzer gezeigt wird. Dabei die Konsole
     mitlesen (`page.on("console", …)`, `page.on("pageerror", …)`): Meldungen „Icon fehlt: …“
     bedeuten einen falschen Icon-Namen – gültige Namen stehen im Kopf von icons.js –, und Fehler
     darf es keine geben.

     Wofür:
       Schritt 3 – je Designvorschlag eine Karte mit dem Hauptscreen der eigenen App in der
                   Designsprache einer Marke, jede Karte mit drei umschaltbaren Farbvarianten.
       Schritt 7 – dieselbe Seite für kleine Vergleiche: zwei bis drei Ausschnitte nebeneinander
                   (z. B. nur die Navigationsleiste) über <section class="phone ausschnitt">,
                   immer INNERHALB der Karte #dN des Entwurfs (siehe „HIER 3“).

     Zu tun sind genau drei Stellen, alle unten mit „HIER“ gekennzeichnet:
       1. Style-Block mit der Id "entwuerfe" – Tokens, die drei Variantenblöcke, die Bausteine
       2. App-Name in der Kopfzeile
       3. Der <main>-Bereich mit der Klasse "vs-entwuerfe" – je Entwurf eine Karte

     Alle Klassen und Variablen der Seite selbst beginnen mit „vs-“ bzw. „--vs-“. Übernommene
     Bausteine aus screens/<slug>.html können daher nie versehentlich das Drumherum verändern.
     Frei verwendbar bleiben: .phone, .sb, .sb-icons, .hi, .scene-*, .crop-N, .grain, .row-x, .ic.
     =========================================================================================== -->
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Designvorschläge</title>

<!-- Basis-CSS der Musterscreens (Phone 390×844, .sb, .hi, .scene-*, .crop-N, .grain, :where-Resets).
     Eingebettet samt Bildmotiven als data-URI – dadurch ist die Seite offline vollständig. -->
<style id="ms-base">
/*{{BASIS_CSS}}*/
</style>

<!-- Stile der Vorschau-Seite selbst. Betreffen nur das Drumherum, nie den Inhalt der Phones:
     die Phones behalten immer ihre eigenen Farben aus dem Entwurf. -->
<style id="seite">
:root {
  --vs-bg: #f3f3f6; --vs-flaeche: #ffffff; --vs-flaeche-2: #ececf1;
  --vs-text: #17171c; --vs-leise: #6a6a76; --vs-linie: #dededf;
  --vs-akzent: #2f5bd0; --vs-auf-akzent: #ffffff;
  --vs-r: 16px;
  --vs-zoom: 1;        /* Verkleinerung der Phones auf schmalen Fenstern */
  --vs-zoom-vgl: .82;  /* Verkleinerung im Vergleichsmodus */
  color-scheme: light dark;
}
@media (prefers-color-scheme: dark) {
  :root {
    --vs-bg: #121216; --vs-flaeche: #1b1b21; --vs-flaeche-2: #24242c;
    --vs-text: #f2f2f5; --vs-leise: #9a9aa6; --vs-linie: #31313a;
    --vs-akzent: #8aa6ff; --vs-auf-akzent: #10121a;
  }
}
body { background: var(--vs-bg); color: var(--vs-text);
  font-family: Inter, system-ui, "Segoe UI", "DejaVu Sans", sans-serif; }
html, body { max-width: 100%; overflow-x: hidden; }

/* Hüllen des Musterscreen-Renderers abschalten, falls Bausteine samt Hülle kopiert werden. */
.ms-wrap, .stage, .shot { display: block; width: auto; padding: 0; margin: 0; gap: 0; background: none; }
.ms-foot, .shot > figcaption { display: none; }

/* ---------- Kopfzeile ---------- */
.vs-top { padding: 28px 20px 18px; border-bottom: 1px solid var(--vs-linie); background: var(--vs-flaeche); }
.vs-top-in { max-width: 1680px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: 10px 20px; align-items: flex-end; }
.vs-top h1 { margin: 0; font-size: clamp(22px, 3vw, 30px); font-weight: 700; letter-spacing: -.01em; }
.vs-sub { margin: 4px 0 0; color: var(--vs-leise); font-size: 14px; line-height: 1.5; }
.vs-sub b { color: var(--vs-text); font-weight: 600; }
.vs-top-rechts { margin-left: auto; display: flex; gap: 10px; align-items: center; flex-wrap: wrap; }
.vs-schalter { display: inline-flex; gap: 8px; align-items: center; padding: 8px 13px; font: 500 13px/1.2 inherit;
  cursor: pointer; border: 1px solid var(--vs-linie); border-radius: 999px;
  background: var(--vs-flaeche-2); color: var(--vs-text); }
.vs-schalter[aria-pressed="true"] { background: var(--vs-akzent); color: var(--vs-auf-akzent); border-color: transparent; }
.vs-warnung { margin: 14px auto 0; max-width: 1648px; padding: 10px 14px; border-radius: 10px; font-size: 13px;
  background: #ffe8e8; color: #7a1414; border: 1px solid #f3b4b4; }
@media (prefers-color-scheme: dark) { .vs-warnung { background: #3a1616; color: #ffd4d4; border-color: #6d2323; } }
.vs-warnung[hidden] { display: none; }

/* ---------- Fläche der Entwürfe ---------- */
.vs-entwuerfe { max-width: 1680px; margin: 0 auto; padding: 24px 16px 72px;
  display: flex; flex-wrap: wrap; gap: 26px; align-items: flex-start; justify-content: center; }
.vs-design { width: calc(390px * var(--vs-zoom) + 34px); flex: none;
  background: var(--vs-flaeche); border: 1px solid var(--vs-linie); border-radius: var(--vs-r);
  padding: 16px 16px 18px; display: flex; flex-direction: column; gap: 12px; outline-offset: 3px; }
.vs-design:focus-visible { outline: 2px solid var(--vs-akzent); }

.vs-zeile-nr { margin: 0; font-size: 12px; font-weight: 700; letter-spacing: .1em; text-transform: uppercase;
  color: var(--vs-leise); }
.vs-name { margin: 2px 0 0; font-size: 20px; font-weight: 700; letter-spacing: -.01em; }
.vs-kopfdaten { margin: 7px 0 0; display: flex; flex-wrap: wrap; gap: 7px; align-items: center; font-size: 12.5px; }
.vs-chip { padding: 3px 9px; border-radius: 999px; background: var(--vs-flaeche-2);
  border: 1px solid var(--vs-linie); font-weight: 600; }
.vs-inspiriert { color: var(--vs-leise); }

.vs-zeilen { margin: 0; display: grid; gap: 3px; font-size: 12.5px; line-height: 1.45; }
.vs-zeilen > div { display: grid; grid-template-columns: 94px 1fr; gap: 8px; }
.vs-zeilen dt { color: var(--vs-leise); }
.vs-zeilen dd { margin: 0; }

/* ---------- Variantenumschalter ---------- */
.vs-schalterreihe { display: flex; flex-wrap: wrap; gap: 6px; }
.vs-knopf { flex: 1 1 auto; display: flex; gap: 6px; align-items: center; justify-content: center;
  padding: 7px 7px; font: 600 11.5px/1.2 inherit; cursor: pointer; white-space: nowrap;
  border: 1px solid var(--vs-linie); border-radius: 10px; background: var(--vs-flaeche); color: var(--vs-text); }
.vs-knopf:hover { background: var(--vs-flaeche-2); }
.vs-knopf[aria-pressed="true"] { border-color: var(--vs-akzent); box-shadow: inset 0 0 0 1px var(--vs-akzent); }
.vs-farben { display: inline-flex; flex: none; }
.vs-farben i { display: block; width: 10px; height: 10px; border-radius: 50%; border: 1px solid rgba(128,128,128,.45); }
.vs-farben i + i { margin-left: -3px; }

/* ---------- Bühne mit dem Phone ---------- */
.vs-screen { display: flex; justify-content: center; }
.phone { zoom: var(--vs-zoom); }

/* ---------- Ausschnitte für die Vergleiche aus Schritt 7 ----------
   Ein Ausschnitt zeigt nur den fraglichen Teil eines Screens (nur die Leiste, nur eine Karte …).
   Die Klassen gehören auf das Phone selbst:
     <section class="phone ausschnitt ende" style="--vs-hoehe:190px"> … nur die Leiste … </section>
   Eine Hülle mit denselben Klassen um ein unverändertes Phone wirkt genauso:
     <figure class="ausschnitt ende" style="--vs-hoehe:190px"><section class="phone"> … </section></figure>
   --vs-hoehe = sichtbare Höhe (Standard 220px)
   .ende      = Inhalt am unteren Rand (für Leisten unten), ohne .ende am oberen Rand.

   WICHTIG: Ein Ausschnitt muss INNERHALB der Entwurfs-Karte #dN liegen, zu deren Entwurf er
   gehört – nur dort gelten die Tokens von #dN und die Regeln #dN .phone, #dN .leiste … (die
   Entwurfs-Stile sind durchweg auf #dN gebunden, siehe „HIER 1 c)“). Liegt ein Ausschnitt
   außerhalb, fehlen ihm alle Farben des Entwurfs. Die beiden Rückfallwerte unten (var(--bg, …),
   var(--text, …)) machen ihn dann grau statt weiß auf weiß, und das Skript schreibt eine Warnung
   in die Konsole und in das rote Band oben – gemeint ist das als Hinweis, nicht als Lösung. */
.phone.ausschnitt, .ausschnitt > .phone {
  height: var(--vs-hoehe, 220px); border-radius: 22px; overflow: hidden;
  background: var(--bg, var(--vs-flaeche-2)); color: var(--text, var(--vs-text)); }
.phone.ausschnitt.ende, .ausschnitt.ende > .phone {
  display: flex; flex-direction: column; justify-content: flex-end; }
/* Zwei bis drei Ausschnitte nebeneinander in einer Karte. Eine Karte mit einer .vs-reihe wird
   dafür so breit wie nötig – sonst stünden die Ausschnitte untereinander. Browser ohne :has()
   erreichen dasselbe über class="vs-design vs-breit" an der Karte. */
.vs-design.vs-breit, .vs-design:has(.vs-reihe) { width: min(100%, 1280px); }
.vs-reihe { display: flex; flex-wrap: wrap; gap: 14px; justify-content: center; align-items: flex-end; }
.vs-reihe > figure { margin: 0; display: flex; flex-direction: column; gap: 7px; align-items: center; }
.vs-reihe figcaption { font-size: 12px; font-weight: 600; color: var(--vs-leise); text-align: center; }
.vs-reihe .phone { zoom: var(--vs-zoom-vgl); }

.vs-waehlen { margin-top: 2px; padding: 11px 14px; font: 600 14px/1.2 inherit; cursor: pointer;
  border: 0; border-radius: 12px; background: var(--vs-akzent); color: var(--vs-auf-akzent); }
.vs-waehlen:hover { filter: brightness(1.08); }
.vs-waehlen:active { transform: translateY(1px); }

/* ---------- Vergleichsmodus „Alle Varianten nebeneinander“ ---------- */
body.vs-alle .vs-design { width: min(100%, 1240px); }
body.vs-alle .vs-screen { display: none; }
body.vs-alle .vs-schalterreihe { display: none; }
.vs-vergleich { display: flex; flex-wrap: wrap; gap: 16px; justify-content: center; }
.vs-vergleich > figure { margin: 0; display: flex; flex-direction: column; gap: 8px; align-items: center; }
.vs-vergleich figcaption { font-size: 12px; font-weight: 600; color: var(--vs-leise); }
.vs-vergleich .phone { zoom: var(--vs-zoom-vgl); }
body:not(.vs-alle) .vs-vergleich { display: none; }

/* ---------- Kopieren: Rückmeldung ---------- */
.vs-toast { position: fixed; left: 50%; bottom: 24px; transform: translate(-50%, 12px);
  padding: 11px 16px; border-radius: 12px; font-size: 13.5px; font-weight: 600; z-index: 100;
  background: #17171c; color: #ffffff; box-shadow: 0 10px 30px rgba(0,0,0,.28);
  opacity: 0; pointer-events: none; transition: opacity .18s ease, transform .18s ease; }
.vs-toast.vs-an { opacity: 1; transform: translate(-50%, 0); }
@media (prefers-color-scheme: dark) { .vs-toast { background: #f2f2f5; color: #17171c; } }
.vs-feld { position: fixed; left: 50%; bottom: 24px; transform: translateX(-50%); z-index: 101;
  display: flex; gap: 8px; align-items: center; padding: 10px 12px; border-radius: 12px;
  background: var(--vs-flaeche); border: 1px solid var(--vs-linie); box-shadow: 0 10px 30px rgba(0,0,0,.22);
  font-size: 13px; max-width: calc(100vw - 32px); flex-wrap: wrap; }
.vs-feld[hidden] { display: none; }
.vs-feld input { width: min(46vw, 300px); padding: 7px 9px; font: inherit; color: var(--vs-text);
  background: var(--vs-flaeche-2); border: 1px solid var(--vs-linie); border-radius: 8px; }
.vs-feld button { padding: 6px 10px; font: 600 12px/1 inherit; cursor: pointer; color: var(--vs-text);
  background: none; border: 1px solid var(--vs-linie); border-radius: 8px; }

/* ---------- Schmale Fenster: Phones verkleinern, nie seitlich scrollen ---------- */
@media (max-width: 900px) { :root { --vs-zoom-vgl: .46; } }
@media (max-width: 520px) { :root { --vs-zoom: .86; --vs-zoom-vgl: .5; }
  .vs-entwuerfe { gap: 18px; padding: 18px 12px 60px; } }
@media (max-width: 430px) { :root { --vs-zoom: .82; } .vs-top { padding: 20px 14px 14px; } }
@media (max-width: 380px) { :root { --vs-zoom: .74; --vs-zoom-vgl: .46; } }
</style>

<!-- ===========================================================================================
     HIER 1 – Stile der Entwürfe
     ===========================================================================================
     Pro Entwurf drei Teile, alle unter der Karten-Id (#d1, #d2, …) – so stoßen sich die Entwürfe
     nicht gegenseitig:

     a) Tokens auf #dN. Immer diese sieben Namen belegen; daraus liest das Skript die Farbpunkte
        der Umschalter:
            --bg         Hintergrund des Screens
            --surface    Flächen darüber (Karten, Leisten)
            --text       Textfarbe
            --muted      zweite Textstufe
            --line       Linien und Rahmen
            --accent     Akzent
            --on-accent  Text und Icons auf dem Akzent
        Weitere Werte des Entwurfs (Radien, Schatten, Dauern, Schriftstapel …) gern dazu. Werden
        Tokens aus screens/<slug>.html übernommen, deren Namen behalten UND zusätzlich die sieben
        Namen oben belegen.

     b) Die beiden weiteren Varianten als eigene Blöcke, die NUR Tokens umschreiben:
            #dN[data-variante="2"] { … }   Gegenmodus hell ↔ dunkel, Akzent bleibt
            #dN[data-variante="3"] { … }   eigene Akzentfarbe passend zum Zweck der App
        Nur Tokens, keine Bausteinregeln – daran hängt auch „Alle Varianten nebeneinander“.
        Feste Farbwerte in Bausteinen (z. B. ein Verlauf) vorher in ein Token auslagern, sonst
        wandert sie beim Umschalten nicht mit.
        Welche Variante eine Karte zeigt, steht allein in data-variante="…" auf der Karte selbst
        (siehe „HIER 3“); die Knöpfe richten sich beim Laden danach.

     c) Bausteine aus screens/<slug>.html übernehmen (Leisten, Karten, Listen, Buttons, Animationen)
        und jede Regel mit der Karten-Id beginnen:
            :root { … }       ->  #dN { … }          (nur Tokens, siehe a)
            .phone { … }      ->  #dN .phone { … }
            .nav { … }        ->  #dN .nav { … }
            #start { … }      ->  #dN .phone { … }   (Id-Regeln der Musterscreens auflösen)
            @keyframes auf    ->  @keyframes dN-auf  (Namen eindeutig machen, auch in animation:)
        Animationen wie dort in @media (prefers-reduced-motion: no-preference) kapseln.

        Diese Bindung an #dN gilt genauso für die Vergleichs-Ausschnitte aus Schritt 7: auch sie
        bekommen Tokens und Bausteine nur, wenn sie IM Element #dN stehen. Ein Ausschnitt gehört
        deshalb in die Karte #dN seines Entwurfs. Die Unterschiede der drei Vorschläge über je
        eine zusätzliche Klasse, ebenfalls unter der Karten-Id:
            #dN .vgl-a .leiste { … }   #dN .vgl-b .leiste { … }   #dN .vgl-c .leiste { … }
        Soll ein Vergleich in einer eigenen Karte stehen, braucht diese eine eigene Id (#v1 …)
        UND den Tokenblock des Entwurfs unter dieser Id – sonst bleibt der Ausschnitt farblos.
     =========================================================================================== -->
<style id="entwuerfe">
/* ====== Design 1 · Beispiel – ersetzen ====== */
/* a) Tokens */
#d1 {
  --bg: #0f1116; --surface: #171a21; --text: #f3f4f7; --muted: #9aa1ae; --line: #262b34;
  --accent: #ffc84d; --on-accent: #1b1403;
  /* weitere Werte dieses Entwurfs */
  --schleier: #2b2416;   /* Farbschleier hinter dem Bühnenbild, wandert mit der Variante mit */
  --r: 20px; --r-klein: 13px; --r-pille: 999px;
  --dur: 220ms; --ease: cubic-bezier(.2, .7, .2, 1);
  --schrift: Inter, system-ui, "DejaVu Sans", sans-serif;
}
/* b) Variante 2 – Gegenmodus hell, Akzent bleibt */
#d1[data-variante="2"] {
  --bg: #fbfaf6; --surface: #ffffff; --text: #16181d; --muted: #6b7280; --line: #e6e3da;
  --accent: #ffc84d; --on-accent: #1b1403;
  --schleier: #fdf3dd;
}
/* b) Variante 3 – eigene Akzentfarbe */
#d1[data-variante="3"] {
  --bg: #0b1317; --surface: #121e23; --text: #ecf5f6; --muted: #8fa5ac; --line: #1d2d34;
  --accent: #35d6a4; --on-accent: #04241a;
  --schleier: #0f2a26;
}

/* c) Bausteine */
#d1 .phone { background: linear-gradient(180deg, var(--schleier) 0, var(--bg) 320px);
  color: var(--text); font-family: var(--schrift); font-size: 16px; display: flex; flex-direction: column; }
#d1 .sb, #d1 .hi { color: var(--text); }

#d1 .kopf-zeile { display: flex; align-items: center; gap: 12px; padding: 6px 20px 10px; }
#d1 .kopf-zeile h3 { font: 700 26px/1.15 var(--schrift); letter-spacing: -.02em; flex: 1; }
#d1 .rund { width: 38px; height: 38px; flex: none; display: grid; place-items: center; font-size: 19px;
  border-radius: var(--r-pille); background: var(--surface); border: 1px solid var(--line); }

#d1 .suche { display: flex; align-items: center; gap: 10px; margin: 0 20px 14px; padding: 11px 14px;
  border-radius: var(--r-pille); background: var(--surface); border: 1px solid var(--line);
  color: var(--muted); font-size: 14px; }
#d1 .suche .ic { font-size: 18px; }

#d1 .gross-bild { position: relative; margin: 0 20px; height: 232px; border-radius: var(--r); overflow: hidden;
  display: flex; flex-direction: column; justify-content: flex-end; padding: 16px; }
#d1 .gross-bild::before { content: ""; position: absolute; inset: 0;
  background: linear-gradient(180deg, rgba(0,0,0,0) 35%, rgba(0,0,0,.72) 100%); }
#d1 .gross-bild > * { position: relative; }
#d1 .einwurf { align-self: flex-start; margin-bottom: 10px; padding: 4px 10px; border-radius: var(--r-pille);
  font: 700 11px/1.4 var(--schrift); letter-spacing: .08em; text-transform: uppercase;
  background: var(--accent); color: var(--on-accent); }
#d1 .gross-titel { font: 700 23px/1.2 var(--schrift); color: #ffffff; letter-spacing: -.015em; }
#d1 .gross-unter { margin-top: 5px; font: 500 13px/1.4 var(--schrift); color: rgba(255,255,255,.78); }

#d1 .abschnitt { display: flex; align-items: baseline; gap: 10px; padding: 24px 20px 10px; }
#d1 .abschnitt h4 { font: 700 15px/1.2 var(--schrift); letter-spacing: -.01em; }
#d1 .abschnitt span { margin-left: auto; font: 600 12.5px/1 var(--schrift); color: var(--accent); }

#d1 .kacheln { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; padding: 0 20px; }
#d1 .kachel { border-radius: var(--r-klein); overflow: hidden; background: var(--surface);
  border: 1px solid var(--line); transition: transform var(--dur) var(--ease); }
#d1 .kachel .bild { height: 92px; }
#d1 .kachel .text { padding: 9px 11px 11px; }
#d1 .kachel b { display: block; font: 600 13.5px/1.3 var(--schrift); }
#d1 .kachel small { display: block; margin-top: 3px; font: 500 11.5px/1.3 var(--schrift); color: var(--muted); }
#d1 .kachel:active { transform: scale(.975); }

#d1 .leiste { margin-top: auto; display: flex; padding: 10px 14px 26px;
  background: var(--surface); border-top: 1px solid var(--line); }
#d1 .leiste a { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 4px;
  font: 600 10.5px/1.2 var(--schrift); color: var(--muted); }
#d1 .leiste a .ic { font-size: 23px; }
#d1 .leiste a.aktiv { color: var(--text); }
#d1 .leiste a.aktiv .ic { color: var(--accent); }

@media (prefers-reduced-motion: no-preference) {
  #d1 .kachel { animation: d1-auf var(--dur) var(--ease) both; }
  #d1 .kachel:nth-child(2) { animation-delay: 50ms; }
  #d1 .kachel:nth-child(3) { animation-delay: 100ms; }
  #d1 .kachel:nth-child(4) { animation-delay: 150ms; }
  @keyframes d1-auf { from { opacity: 0; transform: translateY(8px); } }
}

/* ====== Design 2 · hier die nächste Karte ergänzen ====== */
</style>
</head>

<body>

<header class="vs-top">
  <div class="vs-top-in">
    <div>
      <h1>Designvorschläge</h1>
      <!-- HIER 2 – App-Name eintragen -->
      <p class="vs-sub">für <b data-app>«App-Name»</b> · Hauptscreen in jeder Designsprache ·
        Farbvariante umschalten mit den Tasten <b>1</b>, <b>2</b>, <b>3</b></p>
    </div>
    <div class="vs-top-rechts">
      <button type="button" class="vs-schalter" id="vs-alle-knopf" aria-pressed="false">
        <i data-icon="lucide:layout-grid"></i> Alle Varianten nebeneinander
      </button>
    </div>
  </div>
  <p class="vs-warnung" id="vs-warnung" hidden></p>
</header>

<!-- ===========================================================================================
     HIER 3 – die Karten
     ===========================================================================================
     Eine <article class="vs-design"> je Vorschlag. Neue Karte = diese Karte kopieren, id auf d2,
     d3 … setzen, data-variante="1" lassen und oben im Style-Block den gleichen Satz Regeln für
     #d2 anlegen. Die Nummer in .vs-zeile-nr und der Name in .vs-name wandern in den Text, den
     „Dieses Design wählen“ kopiert.

     Vorauswahl einer Farbvariante: data-variante auf der Karte ist der einzige Schalter – steht
     dort data-variante="2" oder "3" (z. B. nach der Wahl in Schritt 4 oder beim Zeigen des
     Hauptscreens in Schritt 6), zeigt die Karte beim Laden diese Variante UND der Umschalter
     stellt sich selbst darauf ein. Die aria-pressed-Werte der Knöpfe bleiben also unverändert
     wie unten (Knopf 1 auf "true"); sie werden beim Laden überschrieben. Nichts von Hand
     umhängen, keine Inline-Farben in die Karte schreiben.

     In das <section class="phone"> gehört der HAUPTSCREEN DER EIGENEN APP: echte Bezeichnungen,
     echte Inhalte, echte Navigationsziele der App – nur Anordnung, Navigation, Komponenten,
     Icon-Stil, Bildbehandlung, Typografie und Abstände kommen aus der Designsprache der Marke.
     Keine Platzhalter wie „Titel 1“, keine Logos und keine Markennamen der Vorlage.

     Bilder nur über die Motive der Musterscreens: class="scene-see | scene-lissabon | scene-konzert |
     scene-nacht | scene-herbst | scene-studio | scene-wien | scene-film | scene-person",
     weitere Ausschnitte desselben Motivs mit crop-1 … crop-12, Körnung mit class="grain".
     Icons als <i data-icon="lucide:house"></i> oder <i data-icon="ph-fill:house"></i>;
     alle Namen stehen im Kopf von icons.js (dort nach dem Bedarf suchen, z. B. „fernseher“).

     Vergleiche aus Schritt 7 (zwei bis drei Varianten eines Bereichs nebeneinander, z. B. drei
     Navigationsleisten): statt des ganzen Screens nur Ausschnitte zeigen – und zwar INNERHALB
     der Karte #dN des Entwurfs, zu dem sie gehören, weil alle Entwurfs-Stile an #dN hängen.
     Die Klassen „ausschnitt“ und „ende“ sowie --vs-hoehe gehören auf dasselbe Element wie die
     Klasse „phone“; alternativ auf eine Hülle direkt um das Phone (.ausschnitt > .phone). Nicht
     auf das <figure> der Reihe, wenn dazwischen noch etwas steht.
     Was die Vorschläge unterscheidet, kommt in je eine eigene Klasse (hier .vgl-a/-b/-c), deren
     Regeln oben im Style-Block unter der Karten-Id stehen: #dN .vgl-a .leiste { … }

       <article class="vs-design" id="d1" data-variante="1" tabindex="0">
         … Kopf, Angaben und (wenn noch gewünscht) der ganze Screen …
         <div class="vs-reihe">
           <figure>
             <section class="phone ausschnitt ende vgl-a" style="--vs-hoehe:170px">
               <nav class="leiste"> … vier Ziele … </nav>
               <div class="hi"></div>
             </section>
             <figcaption>1 · flache Leiste</figcaption>
           </figure>
           <figure>
             <section class="phone ausschnitt ende vgl-b" style="--vs-hoehe:170px"> … </section>
             <figcaption>2 · schwebende Pille</figcaption>
           </figure>
           <figure>
             <section class="phone ausschnitt ende vgl-c" style="--vs-hoehe:170px"> … </section>
             <figcaption>3 · Leiste mit Beschriftung</figcaption>
           </figure>
         </div>
       </article>

     Die Karte mit der .vs-reihe wird von selbst breit genug für zwei bis drei Ausschnitte
     nebeneinander (in alten Browsern ohne :has() zusätzlich class="vs-design vs-breit").
     Rutscht ein Ausschnitt aus der Karte heraus, erscheint er grau und die Seite warnt oben im
     roten Band sowie in der Konsole („Ausschnitt ohne Entwurfs-Stile“) – dann die Karten-Id
     ergänzen, nicht die Farben von Hand setzen.
     =========================================================================================== -->
<main class="vs-entwuerfe">

  <!-- ===== Beispiel – ersetzen ===== -->
  <article class="vs-design" id="d1" data-variante="1" tabindex="0">
    <header>
      <p class="vs-zeile-nr">Design <span class="vs-nummer">1</span> · Beispiel – ersetzen</p>
      <h2 class="vs-name">Ruhige Bühne</h2>
      <p class="vs-kopfdaten">
        <span class="vs-chip">Große Bühne</span>
        <span class="vs-inspiriert">Inspiriert von: Beispielmarke</span>
      </p>
    </header>

    <dl class="vs-zeilen">
      <div><dt>Aufbau</dt><dd>Ein großes Bild oben, darunter ein Raster aus zwei Spalten.</dd></div>
      <div><dt>Navigation</dt><dd>Flache Leiste unten mit vier Zielen, aktives Ziel am Akzent.</dd></div>
      <div><dt>Komponenten</dt><dd>Weiche Karten mit feinem Rahmen, Pillen für Suche und Einwurf.</dd></div>
      <div><dt>Icons</dt><dd>Lucide, 2 px Strich, 23 px in der Leiste.</dd></div>
      <div><dt>Bewegung</dt><dd>Kacheln blenden gestaffelt ein, Druck verkleinert auf 97,5 %.</dd></div>
    </dl>

    <div class="vs-schalterreihe" role="group" aria-label="Farbvariante">
      <button type="button" class="vs-knopf" data-v="1" aria-pressed="true"><span class="vs-farben"></span>1 Original</button>
      <button type="button" class="vs-knopf" data-v="2" aria-pressed="false"><span class="vs-farben"></span>2 Hell/Dunkel</button>
      <button type="button" class="vs-knopf" data-v="3" aria-pressed="false"><span class="vs-farben"></span>3 Eigene Farbe</button>
    </div>

    <div class="vs-screen">
      <section class="phone">
        <div class="sb"><span>9:41</span>
          <span class="sb-icons"><i data-icon="lucide:wifi"></i><i data-icon="lucide:battery-full"></i></span></div>

        <div class="kopf-zeile">
          <h3>Guten Abend</h3>
          <span class="rund"><i data-icon="lucide:bell"></i></span>
          <span class="rund"><i data-icon="lucide:user"></i></span>
        </div>

        <div class="suche"><i data-icon="lucide:search"></i> Suchen …</div>

        <div class="gross-bild scene-see grain" style="--grain:.14">
          <span class="einwurf">Heute</span>
          <div class="gross-titel">Abendlicht am See</div>
          <div class="gross-unter">Gesammelt · 24 Aufnahmen</div>
        </div>

        <div class="abschnitt"><h4>Zuletzt geöffnet</h4><span>Alle</span></div>
        <div class="kacheln">
          <div class="kachel"><div class="bild scene-lissabon crop-1"></div>
            <div class="text"><b>Lissabon</b><small>82 Aufnahmen</small></div></div>
          <div class="kachel"><div class="bild scene-herbst crop-4"></div>
            <div class="text"><b>Herbstwoche</b><small>31 Aufnahmen</small></div></div>
          <div class="kachel"><div class="bild scene-konzert crop-2"></div>
            <div class="text"><b>Konzertabend</b><small>17 Aufnahmen</small></div></div>
          <div class="kachel"><div class="bild scene-studio crop-6"></div>
            <div class="text"><b>Werkstatt</b><small>9 Aufnahmen</small></div></div>
        </div>

        <nav class="leiste">
          <a class="aktiv"><i data-icon="lucide:house"></i>Start</a>
          <a><i data-icon="lucide:search"></i>Suchen</a>
          <a><i data-icon="lucide:folder"></i>Alben</a>
          <a><i data-icon="lucide:settings"></i>Mehr</a>
        </nav>
        <div class="hi"></div>
      </section>
    </div>

    <button type="button" class="vs-waehlen">Dieses Design wählen</button>
  </article>

  <!-- ===== Weitere Karten hier anfügen (diese Karte kopieren, id d2, d3 … ) ===== -->

</main>

<div class="vs-toast" id="vs-toast" role="status" aria-live="polite"></div>
<div class="vs-feld" id="vs-feld" hidden>
  <span>Text markiert – mit Strg/Cmd + C kopieren:</span>
  <input id="vs-feld-text" readonly>
  <button type="button" id="vs-feld-zu">Schließen</button>
</div>

<script src="./icons.js"></script>
<script>
/* Kleines Skript der Vorschau: Icons einsetzen, Varianten umschalten, Auswahl kopieren.
   Es liest nur vorhandene Werte – an den Entwürfen ist hier nichts zu ändern. */
(function () {
  "use strict";
  var TOKENS = ["--bg", "--surface", "--text", "--muted", "--line", "--accent", "--on-accent"];
  var VARIANTEN = ["1", "2", "3"];
  var karten = [].slice.call(document.querySelectorAll(".vs-design"));
  var werte = {};          /* Karten-Id -> { "1": {Token: Wert}, "2": …, "3": … } */
  var ueberKarte = null;   /* Karte unter dem Mauszeiger */
  var warnungen = [];      /* Texte für das rote Band in der Kopfzeile */

  function warnungenZeigen() {
    var w = document.getElementById("vs-warnung");
    if (!w || !warnungen.length) return;
    w.hidden = false;
    w.textContent = warnungen.join(" ");
  }

  /* ---------- Icons ---------- */
  if (window.VorschauIcons) {
    var fehlend = VorschauIcons.ersetzen(document);
    if (fehlend) {
      warnungen.push(fehlend + " Icon-Name" + (fehlend === 1 ? "" : "n") + " nicht gefunden "
        + "(rot gestrichelte Kästchen). Die gültigen Namen stehen im Kopf von icons.js; "
        + "Einzelheiten in der Konsole.");
    }
  } else {
    console.warn("icons.js wurde nicht geladen – liegt die Datei neben dieser Seite?");
  }

  /* ---------- Tokens der drei Varianten einlesen ---------- */
  /* Neben den sieben Standard-Tokens alles, was die Blöcke dieser Karte zusätzlich setzen. */
  function tokenListe(karte) {
    var satz = {}, i;
    for (i = 0; i < TOKENS.length; i++) satz[TOKENS[i]] = 1;
    var id = "#" + karte.id;
    try {
      var blaetter = document.styleSheets;
      for (var b = 0; b < blaetter.length; b++) {
        var regeln;
        try { regeln = blaetter[b].cssRules; } catch (e) { continue; }
        if (!regeln) continue;
        for (var r = 0; r < regeln.length; r++) {
          var regel = regeln[r];
          if (!regel.selectorText || !regel.style) continue;
          var teile = regel.selectorText.split(","), trifft = false;
          for (var t = 0; t < teile.length; t++) {
            var s = teile[t].trim();
            if (s === id || s.indexOf(id + "[data-variante") === 0) trifft = true;
          }
          if (!trifft) continue;
          for (var p = 0; p < regel.style.length; p++) {
            var name = regel.style[p];
            if (name.indexOf("--") === 0) satz[name] = 1;
          }
        }
      }
    } catch (e) { /* ohne CSSOM bleiben die sieben Standard-Tokens */ }
    return Object.keys(satz);
  }

  function werteLesen(karte) {
    var liste = tokenListe(karte);
    var vorher = karte.getAttribute("data-variante") || "1";
    var out = {};
    ["1", "2", "3"].forEach(function (v) {
      karte.setAttribute("data-variante", v);
      var cs = getComputedStyle(karte), o = {};
      liste.forEach(function (t) { o[t] = cs.getPropertyValue(t).trim(); });
      out[v] = o;
    });
    karte.setAttribute("data-variante", vorher);
    return out;
  }

  /* ---------- Farbpunkte der Umschalter (live aus den Variablen der Variante) ---------- */
  function farbenFuellen(karte) {
    var w = werte[karte.id];
    [].forEach.call(karte.querySelectorAll(".vs-knopf"), function (knopf) {
      var v = knopf.getAttribute("data-v"), p = knopf.querySelector(".vs-farben");
      if (!p || !w[v]) return;
      p.textContent = "";
      ["--bg", "--surface", "--accent"].forEach(function (t) {
        var punkt = document.createElement("i");
        punkt.style.background = w[v][t] || "transparent";
        p.appendChild(punkt);
      });
      knopf.title = "Variante " + v + ": Fläche " + (w[v]["--bg"] || "?")
        + ", Akzent " + (w[v]["--accent"] || "?");
    });
  }

  /* ---------- Variante setzen ---------- */
  /* Maßgeblich ist immer data-variante auf der Karte: so lässt sich eine Karte mit
     data-variante="2" oder "3" ausliefern (Vorauswahl nach Schritt 4/6). umschalterSyncen()
     bringt die Knopfreihe auf genau diesen Stand und läuft deshalb auch beim Laden, nicht nur
     beim Klick. Alles, was den aktuellen Stand anzeigt, gehört in diese Funktion. */
  function umschalterSyncen(karte) {
    var v = String(karte.getAttribute("data-variante") || "1");
    if (VARIANTEN.indexOf(v) < 0) {
      console.warn("Karte #" + karte.id + ": data-variante=\"" + v + "\" gibt es nicht – "
                 + "erlaubt sind 1, 2 und 3. Es gilt wieder 1.");
      v = "1";
    }
    karte.setAttribute("data-variante", v);
    var reihe = karte.querySelector(".vs-schalterreihe");
    if (reihe) reihe.setAttribute("data-aktiv", v);
    [].forEach.call(karte.querySelectorAll(".vs-knopf"), function (knopf) {
      knopf.setAttribute("aria-pressed", knopf.getAttribute("data-v") === v ? "true" : "false");
    });
  }
  function setzen(karte, v) {
    karte.setAttribute("data-variante", String(v));
    umschalterSyncen(karte);
  }

  /* ---------- Vergleich: alle drei Varianten nebeneinander ---------- */
  /* Kopien des Phones, auf die die Tokens der jeweiligen Variante direkt geschrieben werden.
     Das klappt, weil die Variantenblöcke ausschließlich Tokens umschreiben. */
  var NAMEN = { "1": "1 Original", "2": "2 Hell/Dunkel", "3": "3 Eigene Farbe" };
  function vergleichBauen(karte) {
    if (karte.querySelector(".vs-vergleich")) return;
    var buehne = karte.querySelector(".vs-screen");
    var phone = buehne && buehne.querySelector(".phone");
    if (!phone) return;
    var reihe = document.createElement("div");
    reihe.className = "vs-vergleich";
    ["1", "2", "3"].forEach(function (v) {
      var fig = document.createElement("figure");
      var klon = phone.cloneNode(true);
      klon.removeAttribute("id");
      [].forEach.call(klon.querySelectorAll("[id]"), function (el) { el.removeAttribute("id"); });
      var w = werte[karte.id][v] || {};
      Object.keys(w).forEach(function (t) { if (w[t]) klon.style.setProperty(t, w[t]); });
      var cap = document.createElement("figcaption");
      cap.textContent = NAMEN[v];
      fig.appendChild(klon);
      fig.appendChild(cap);
      reihe.appendChild(fig);
    });
    buehne.parentNode.insertBefore(reihe, buehne.nextSibling);
  }

  var alleKnopf = document.getElementById("vs-alle-knopf");
  if (alleKnopf) {
    alleKnopf.addEventListener("click", function () {
      var an = alleKnopf.getAttribute("aria-pressed") !== "true";
      alleKnopf.setAttribute("aria-pressed", an ? "true" : "false");
      document.body.classList.toggle("vs-alle", an);
      if (an) karten.forEach(vergleichBauen);
    });
  }

  /* ---------- Auswahl kopieren ---------- */
  var toast = document.getElementById("vs-toast"), toastZeit = null;
  function melden(text) {
    if (!toast) return;
    toast.textContent = text;
    toast.classList.add("vs-an");
    clearTimeout(toastZeit);
    toastZeit = setTimeout(function () { toast.classList.remove("vs-an"); }, 2400);
  }
  var feld = document.getElementById("vs-feld"), eingabe = document.getElementById("vs-feld-text");
  var zu = document.getElementById("vs-feld-zu");
  if (zu) zu.addEventListener("click", function () { feld.hidden = true; });
  function notloesung(text) {
    if (!feld || !eingabe) { melden(text); return; }
    feld.hidden = false;
    eingabe.value = text;
    eingabe.focus();
    eingabe.select();
  }
  function altKopieren(text) {
    var tmp = document.createElement("textarea");
    tmp.value = text;
    tmp.setAttribute("readonly", "");
    tmp.style.cssText = "position:fixed;top:-1000px;opacity:0";
    document.body.appendChild(tmp);
    tmp.select();
    var ok = false;
    try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
    document.body.removeChild(tmp);
    if (ok) melden("Kopiert: " + text); else notloesung(text);
  }
  function kopieren(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        melden("Kopiert: " + text);
      }, function () { altKopieren(text); });
    } else {
      altKopieren(text);
    }
  }
  function auswahlText(karte) {
    var nr = karte.querySelector(".vs-nummer");
    nr = nr ? nr.textContent.trim() : (karte.id || "").replace(/^d/, "");
    var name = karte.querySelector(".vs-name");
    name = name ? name.textContent.trim() : "Entwurf";
    return "Design " + nr + " · " + name + " · Variante " + (karte.getAttribute("data-variante") || "1");
  }

  /* ---------- Karten verdrahten ---------- */
  karten.forEach(function (karte) {
    if (!karte.id) {
      console.warn("Karte ohne id – die Entwurfs-Stile greifen nur über eine id (#d1, #d2 …).");
      return;
    }
    werte[karte.id] = werteLesen(karte);
    farbenFuellen(karte);
    umschalterSyncen(karte);   /* Knöpfe auf das data-variante der Karte stellen */
    [].forEach.call(karte.querySelectorAll(".vs-knopf"), function (knopf) {
      knopf.addEventListener("click", function () { setzen(karte, knopf.getAttribute("data-v")); });
    });
    var waehlen = karte.querySelector(".vs-waehlen");
    if (waehlen) waehlen.addEventListener("click", function () { kopieren(auswahlText(karte)); });
    karte.addEventListener("pointerover", function () { ueberKarte = karte; });
  });

  /* ---------- Ausschnitte aus Schritt 7 prüfen ---------- */
  /* Ein Ausschnitt außerhalb der Karte #dN bekommt keine Tokens und keine Bausteinregeln des
     Entwurfs. Das CSS fängt ihn grau auf, hier kommt die Erklärung dazu. */
  function ausschnittePruefen() {
    var liste = document.querySelectorAll(".phone.ausschnitt, .ausschnitt > .phone");
    var ohne = 0;
    [].forEach.call(liste, function (el) {
      var karte = el.closest ? el.closest(".vs-design[id]") : null;
      var tokens = getComputedStyle(el).getPropertyValue("--bg").trim();
      if (karte && tokens) return;
      ohne++;
      console.warn("Ausschnitt ohne Entwurfs-Stile: "
        + (karte ? "die Karte #" + karte.id + " setzt kein --bg."
                 : "der Ausschnitt liegt in keiner Karte <article class=\"vs-design\" id=\"dN\">.")
        + " Die Entwurfs-Stile hängen alle an #dN – Ausschnitt dorthin verschieben "
        + "oder die Tokens des Entwurfs für die Id dieser Karte anlegen.", el);
    });
    if (ohne) {
      warnungen.push(ohne + " Vergleichs-Ausschnitt" + (ohne === 1 ? "" : "e") + " ohne "
        + "Entwurfs-Stile (grau dargestellt): Ausschnitte gehören in die Karte #dN ihres "
        + "Entwurfs. Einzelheiten in der Konsole.");
    }
  }
  ausschnittePruefen();
  warnungenZeigen();

  /* ---------- Tasten 1 / 2 / 3 für die Karte unter dem Zeiger oder im Fokus ---------- */
  document.addEventListener("keydown", function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.key !== "1" && e.key !== "2" && e.key !== "3") return;
    var z = e.target;
    if (z && (z.tagName === "INPUT" || z.tagName === "TEXTAREA" || z.isContentEditable)) return;
    var aktiv = document.activeElement;
    var karte = (aktiv && aktiv.closest) ? aktiv.closest(".vs-design") : null;
    if (!karte) karte = ueberKarte;
    if (!karte) return;
    setzen(karte, e.key);
    e.preventDefault();
  });
})();
</script>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--icons", default="/home/claude/src/icons",
                    help="Ordner mit lucide/ und phosphor/ (Standard: %(default)s)")
    ap.add_argument("--out", default=str(HERE / "vorschau"),
                    help="Zielordner (Standard: %(default)s)")
    ap.add_argument("--screens", default=str(HERE.parent / "screens"),
                    help="Ordner mit den Musterscreens; die dort benutzten Icons kommen mit in icons.js")
    ap.add_argument("--renderer", default=str(HERE / "render_screens.py"),
                    help="Pfad zu render_screens.py (Standard: %(default)s)")
    a = ap.parse_args()

    icons_root = pathlib.Path(a.icons)
    if not (icons_root / "lucide" / "icons").is_dir() or not (icons_root / "phosphor" / "assets").is_dir():
        sys.exit(f"Icon-Sammlungen fehlen in {icons_root} (siehe --help)")

    renderer = lade_renderer(a.renderer)
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    js = icons_js(renderer, icons_root, a.screens)
    html_text = vorlage_html(renderer)

    # Kurze Eigenprüfung, damit Fehler hier und nicht erst im Browser auffallen.
    for spec in re.findall(r'data-icon="([^"]+)"', html_text):
        if f'"{spec}":' not in js:
            sys.exit(f"Die Vorlage benutzt {spec}, das nicht in icons.js steht.")
    if "./icons.js" not in html_text:
        sys.exit("Die Vorlage lädt icons.js nicht.")

    # Jedes Icon, das die Musterscreens benutzen, muss in der Vorschau verfügbar sein.
    fehlend = sorted(s for s in aus_musterscreens(a.screens) if f'"{s}":' not in js)
    if fehlend:
        sys.exit("Musterscreens benutzen Icons, die nicht in icons.js stehen:\n  " + "\n  ".join(fehlend))

    (out / "icons.js").write_text(js, encoding="utf-8")
    (out / "vorlage.html").write_text(html_text, encoding="utf-8")
    eintraege = js.count('":"')
    print(f"{out / 'icons.js'} ({len((out / 'icons.js').read_bytes()) // 1024} KB, {eintraege} Einträge; "
          f"Musterscreens geprüft: {len(aus_musterscreens(a.screens))} Namen)")
    print(f"{out / 'vorlage.html'} ({len((out / 'vorlage.html').read_bytes()) // 1024} KB)")


if __name__ == "__main__":
    main()
