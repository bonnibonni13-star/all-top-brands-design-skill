"""Echte Website-Screens und gemessene Design-Werte einer Marke holen.

Aufruf:
  python3 live_screens.py <slug|url> [--skill-dir DIR] [--out DIR] [--seiten 3]
                          [--kein-handy] [--max-hoehe 6000] [--timeout 30]

Fotografiert Startseite und bis zu N Unterseiten einer Marken-Website auf Desktop
(1440x900) und Handy (iPhone 13) und liest dabei echte Werte aus:
  bewegung.json      Transitions, Keyframes, Easings, Hover-Effekte je Seite
  layout.json        Kopfleiste, Containerbreite, Abstaende, Schrift, Radien, Buttons, Icons
  zusammenfassung.md kurzer deutscher Bericht fuer Claude

Exit-Codes:
  0  Erfolg: Startseite und alle gewaehlten Unterseiten erfasst
  3  Teilerfolg: Startseite erfasst, einzelne Seiten oder Bilder fehlgeschlagen
     (zusammenfassung.md nennt sie unter "Nicht erfasste Seiten")
  1  Totalfehler: nichts gemessen (kein Netz, Seite gesperrt oder nicht erreichbar,
     Profil oder website: fehlt). Dann entstehen keine Ergebnisdateien, nur eine
     kurze Fehlernotiz in zusammenfassung.md.
  2  Abhaengigkeit fehlt: Playwright nicht installiert oder kein Browser startbar.

Braucht Playwright fuer Python. Es wird nichts automatisch installiert.
Die Bilder dienen nur der Anschauung - nichts daraus kopieren, nichts veroeffentlichen.
"""
import argparse
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import urllib.parse
from datetime import date

HERE = pathlib.Path(__file__).resolve().parent

# Exit-Codes (siehe Modul-Dokumentation und --help)
EXIT_OK = 0
EXIT_TOTAL = 1
EXIT_ABHAENGIGKEIT = 2
EXIT_TEILWEISE = 3


class SeitenFehler(Exception):
    """Seite war erreichbar, aber nicht brauchbar (z. B. Fehlerseite statt Inhalt)."""


HTTP_GRUND = {
    401: "Anmeldung verlangt", 403: "Zugriff gesperrt", 404: "Seite nicht gefunden",
    410: "Seite entfernt", 429: "zu viele Anfragen", 451: "aus rechtlichen Gruenden gesperrt",
    500: "Serverfehler", 502: "Gateway-Fehler", 503: "Server nicht verfuegbar",
    504: "Gateway-Zeitgrenze",
}

# Erkennungsmarken in Fehlertexten -> deutsche Ursache im Klartext
URSACHEN = [
    ("ERR_NAME_NOT_RESOLVED", "Adresse nicht aufloesbar - Domain falsch geschrieben, "
                              "kein DNS oder keine Netzverbindung"),
    ("ERR_TUNNEL_CONNECTION_FAILED", "Verbindung von einem Proxy oder einer Firewall "
                                     "blockiert - hier gibt es keinen offenen Internetzugang"),
    ("ERR_PROXY_CONNECTION_FAILED", "Proxy nicht erreichbar - kein Netzzugang"),
    ("ERR_INTERNET_DISCONNECTED", "keine Netzverbindung"),
    ("ERR_CONNECTION_REFUSED", "Server nimmt keine Verbindung an - laeuft dort ein "
                               "Webserver, stimmen Host und Port?"),
    ("ERR_CONNECTION_RESET", "Verbindung abgebrochen - die Seite blockiert "
                             "moeglicherweise automatisierte Zugriffe"),
    ("ERR_CONNECTION_CLOSED", "Verbindung vom Server geschlossen"),
    ("ERR_CONNECTION_TIMED_OUT", "Zeitgrenze beim Verbinden - Seite nicht erreichbar"),
    ("ERR_ADDRESS_UNREACHABLE", "Adresse nicht erreichbar"),
    ("ERR_UNSAFE_PORT", "Der Browser verweigert diesen Port - anderen Port verwenden"),
    ("ERR_TOO_MANY_REDIRECTS", "Weiterleitungsschleife"),
    ("ERR_EMPTY_RESPONSE", "Server antwortet nicht"),
    ("ERR_CERT", "TLS-Zertifikat nicht akzeptiert"),
    ("ERR_SSL", "TLS-Fehler beim Verbindungsaufbau"),
    ("ERR_BLOCKED_BY", "Aufruf wurde blockiert"),
    ("HTTP 401", "Anmeldung verlangt (HTTP 401)"),
    ("HTTP 403", "Zugriff gesperrt (HTTP 403) - die Seite laesst automatisierte "
                 "Zugriffe nicht zu"),
    ("HTTP 404", "Seite nicht gefunden (HTTP 404) - URL pruefen"),
    ("HTTP 429", "zu viele Anfragen (HTTP 429) - spaeter erneut versuchen"),
    ("HTTP 5", "Serverfehler auf der Gegenseite"),
    ("Timeout", "Zeitgrenze ueberschritten - Seite zu langsam, blockiert oder nicht "
                "erreichbar (ggf. --timeout erhoehen)"),
]


UNKLAR = ("Grund unklar - meist kein Netzzugang, die Seite ist gesperrt oder "
          "nicht erreichbar")


def ursache_text(fehlertexte):
    """Wahrscheinliche Ursache als deutscher Satzteil, sonst None.

    None heisst: kein bekanntes Muster erkannt - dann lieber nichts behaupten.
    """
    zusammen = " ".join(str(f) for f in (fehlertexte or []))
    for marke, text in URSACHEN:
        if marke in zusammen:
            return text
    return None


def fehlergrund(exc):
    """Kurzer Grund fuer eine fehlgeschlagene Seite."""
    if isinstance(exc, SeitenFehler):
        return str(exc)
    text = f"{type(exc).__name__}: {exc}".replace("\n", " ")
    return re.sub(r"\s+", " ", text)[:180]

PLAYWRIGHT_HINWEIS = """Playwright fehlt (wird fuer echte Website-Screens gebraucht).

So nachinstallieren:
  python3 -m pip install --user playwright
  python3 -m playwright install chromium

Der zweite Schritt (rund 150 MB) ist nicht noetig, wenn Google Chrome
auf diesem Rechner installiert ist - dann wird Chrome verwendet.
Es wird nichts automatisch installiert."""

# ---------------------------------------------------------------- Consent

# Nur eindeutig ablehnende Beschriftungen werden geklickt. Niemals Zustimmung.
ABLEHNEN = [
    r"\balle[sn]? ablehnen\b", r"^ablehnen$", r"\bablehnen\b", r"\babweisen\b",
    r"nicht (?:zustimmen|einverstanden)", r"\bverweigern\b",
    r"nur (?:die |das )?(?:technisch |unbedingt |strikt )?"
    r"(?:notwendige|noetige|erforderliche|essenzielle|essentielle|funktionale)",
    r"(?:notwendige|erforderliche|essenzielle|essentielle)\s*(?:cookies)?\s*(?:nur|only)?$",
    r"\breject all\b", r"^reject\b", r"\breject\b", r"\brefuse\b",
    r"\bdecline\b", r"\bdeny\b", r"\bdisagree\b", r"\bopt out\b",
    r"(?:do not|don't|dont) (?:accept|agree|allow|consent)",
    r"only (?:use )?(?:strictly )?(?:necessary|essential|required)",
    r"(?:necessary|essential|required) (?:cookies )?only",
    r"continue without (?:accepting|agreeing)", r"ohne (?:zu )?akzeptieren weiter",
    r"weiter ohne (?:zu )?(?:akzeptieren|einwilligung)",
]
ZUSTIMMEN = [
    "akzeptieren", "accept", "zustimmen", "einverstanden", "agree", "allow",
    "erlauben", "annehmen", "verstanden", "got it", "einwilligen", "zulassen",
    "alle cookies", "alles erlauben", "i consent", "ja, ", "sure", "aktivieren",
]
# Beschriftungen, die ein Zustimmungs-Wort enthalten, aber ablehnen
# ("weiter ohne zu akzeptieren", "nicht einverstanden", "do not agree")
ZUSTIMMEN_AUSNAHME = re.compile(
    r"(?:ohne (?:zu )?akzeptieren|without accepting|without agreeing"
    r"|nicht (?:zustimmen|einverstanden|akzeptieren|erlauben|zulassen|einwilligen|annehmen)"
    r"|(?:do not|don't|dont) (?:accept|agree|allow|consent))")

CONSENT_KEYS = [
    "onetrust", "ot-sdk", "optanon", "didomi", "usercentrics", "uc-banner",
    "cookiebot", "cybotcookiebot", "cookielaw", "cmp", "consent", "cookie",
    "gdpr", "dsgvo", "sp_message", "sp-message", "qc-cmp", "truste", "trustarc",
    "klaro", "borlabs", "osano", "iubenda", "termly", "tarteaucitron",
    "privacy-banner", "cc-window", "cookie-banner", "cookienotice",
]

# ---------------------------------------------------------------- Unterseiten

UEBERSPRINGEN = [
    "login", "log-in", "signin", "sign-in", "anmelden", "einloggen", "logout",
    "signup", "sign-up", "register", "registrieren", "konto", "account", "profil",
    "profile", "dashboard", "cart", "warenkorb", "basket", "checkout", "bag",
    "impressum", "legal", "rechtliches", "terms", "agb", "tos", "privacy",
    "datenschutz", "cookies", "cookie", "licen", "trademark", "patents",
    "careers", "career", "jobs", "stellen", "karriere", "press", "presse",
    "newsroom", "media-kit", "support", "help", "hilfe", "faq", "kontakt",
    "contact", "download", "downloads", "app-store", "apps.apple", "play.google",
    "status", "sitemap", "search", "suche", "subscribe", "newsletter", "shop",
    "store", "basket", "donate", "spenden", "accessibility", "barrierefrei",
]
BEVORZUGT = [
    "pricing", "preise", "preis", "plans", "tarife", "product", "produkt",
    "products", "produkte", "features", "funktionen", "platform", "plattform", "solutions",
    "loesungen", "about", "ueber-uns", "about-us", "company", "unternehmen",
    "customers", "kunden", "enterprise", "business", "design", "technology",
    "technik", "models", "developers", "docs", "blog", "stories", "work",
]
DATEI_ENDUNGEN = (
    ".pdf", ".zip", ".dmg", ".exe", ".pkg", ".jpg", ".jpeg", ".png", ".gif",
    ".svg", ".webp", ".mp4", ".mov", ".webm", ".mp3", ".xml", ".json", ".txt",
    ".csv", ".ics", ".rss", ".apk", ".tar", ".gz",
)

# ---------------------------------------------------------------- JS-Bausteine

JS_HELFER = r"""
const _split = s => {               // Liste trennen, Klammern beachten
  const out = []; let cur = '', depth = 0;
  for (const ch of String(s || '')) {
    if (ch === '(') depth++;
    if (ch === ')') depth--;
    if (ch === ',' && depth === 0) { out.push(cur.trim()); cur = ''; }
    else cur += ch;
  }
  if (cur.trim()) out.push(cur.trim());
  return out;
};
const _ms = v => {
  const s = String(v || '').trim();
  if (s.endsWith('ms')) return parseFloat(s);
  if (s.endsWith('s')) return parseFloat(s) * 1000;
  const n = parseFloat(s);
  return isNaN(n) ? 0 : n;
};
const _sichtbar = el => {
  const r = el.getBoundingClientRect();
  if (r.width < 2 || r.height < 2) return false;
  const cs = getComputedStyle(el);
  return cs.visibility !== 'hidden' && cs.display !== 'none' && cs.opacity !== '0';
};
const _top = (counter, n) => Object.entries(counter)
  .sort((a, b) => b[1] - a[1]).slice(0, n).map(([wert, anzahl]) => ({ wert, anzahl }));
const _zaehl = (obj, key) => { if (key) obj[key] = (obj[key] || 0) + 1; };
const _text = el => (el.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 60);
"""

JS_BEWEGUNG = JS_HELFER + r"""
const alle = Array.from(document.querySelectorAll('*')).slice(0, 4000);
const trans = { eigenschaften: {}, dauern: {}, easings: {} };
const anim = { namen: {}, dauern: {}, easings: {}, wiederholungen: {} };
let mitTransition = 0, mitAnimation = 0, geprueft = 0;

for (const el of alle) {
  if (!_sichtbar(el)) continue;
  geprueft++;
  const cs = getComputedStyle(el);
  const dauern = _split(cs.transitionDuration).map(_ms);
  if (dauern.some(d => d > 0)) {
    mitTransition++;
    const props = _split(cs.transitionProperty);
    const eas = _split(cs.transitionTimingFunction);
    dauern.forEach((d, i) => {
      if (d <= 0) return;
      _zaehl(trans.eigenschaften, props[i] || props[0] || 'all');
      _zaehl(trans.dauern, String(Math.round(d / 10) * 10));
      _zaehl(trans.easings, eas[i] || eas[0] || 'ease');
    });
  }
  if (cs.animationName && cs.animationName !== 'none') {
    mitAnimation++;
    const namen = _split(cs.animationName);
    const ad = _split(cs.animationDuration).map(_ms);
    const ae = _split(cs.animationTimingFunction);
    const ai = _split(cs.animationIterationCount);
    namen.forEach((n, i) => {
      _zaehl(anim.namen, n);
      _zaehl(anim.dauern, String(Math.round((ad[i] ?? ad[0] ?? 0) / 10) * 10));
      _zaehl(anim.easings, ae[i] || ae[0] || 'ease');
      _zaehl(anim.wiederholungen, ai[i] || ai[0] || '1');
    });
  }
}

// @keyframes und prefers-reduced-motion aus lesbaren Stylesheets
const keyframes = new Set();
let reducedMotion = false, cssFehler = 0, regeln = 0;
const lauf = (rules, tiefe) => {
  if (tiefe > 6) return;
  for (const r of rules) {
    regeln++;
    try {
      if (r.type === CSSRule.KEYFRAMES_RULE || (r.name && r.cssRules && r.type === 7)) {
        keyframes.add(r.name);
        continue;
      }
      const bedingung = r.conditionText || (r.media && r.media.mediaText) || '';
      if (/prefers-reduced-motion/i.test(bedingung)) reducedMotion = true;
      if (r.cssRules) lauf(r.cssRules, tiefe + 1);
    } catch (e) { cssFehler++; }
  }
};
for (const sheet of Array.from(document.styleSheets)) {
  try { lauf(sheet.cssRules, 0); } catch (e) { cssFehler++; }   // CORS: stillschweigend
}

// Scroll-Reveal-Hinweise
const muster = {
  'data-aos': '[data-aos]', 'data-animate': '[data-animate],[data-animation]',
  'data-scroll': '[data-scroll],[data-sr]',
  'class*=reveal': '[class*="reveal" i]', 'class*=fade-in': '[class*="fade-in" i],[class*="fadein" i]',
  'class*=animate': '[class*="animate" i]', 'class*=in-view': '[class*="in-view" i],[class*="inview" i]',
  'class*=slide-up': '[class*="slide-up" i],[class*="slideup" i]',
};
const reveal = { treffer: {}, opacity0_mit_transform: 0, beispiel_klassen: [] };
for (const [name, sel] of Object.entries(muster)) {
  let n = 0;
  try { n = document.querySelectorAll(sel).length; } catch (e) { n = 0; }
  if (n) reveal.treffer[name] = n;
}
const klassen = new Set();
for (const el of alle) {
  const cs = getComputedStyle(el);
  if (parseFloat(cs.opacity) === 0 && cs.transform && cs.transform !== 'none') {
    reveal.opacity0_mit_transform++;
    if (klassen.size < 8 && el.className && typeof el.className === 'string') {
      klassen.add(el.className.split(/\s+/).slice(0, 3).join(' ').slice(0, 60));
    }
  }
}
reveal.beispiel_klassen = Array.from(klassen);

return {
  gepruefte_elemente: geprueft,
  css_regeln_gelesen: regeln,
  css_nicht_lesbar: cssFehler,
  transitions: {
    elemente: mitTransition,
    dauern_ms: _top(trans.dauern, 8),
    easings: _top(trans.easings, 6),
    eigenschaften: _top(trans.eigenschaften, 10),
  },
  animationen: {
    elemente: mitAnimation,
    namen: _top(anim.namen, 10),
    dauern_ms: _top(anim.dauern, 8),
    easings: _top(anim.easings, 6),
    wiederholungen: _top(anim.wiederholungen, 4),
  },
  keyframes: Array.from(keyframes).slice(0, 40),
  prefers_reduced_motion_regeln: reducedMotion,
  scroll_reveal: reveal,
};
"""

JS_LAYOUT = JS_HELFER + r"""
const vw = window.innerWidth, vh = window.innerHeight;

// --- Kopfleiste
let header = document.querySelector('header, [role="banner"]');
if (!header) {
  header = Array.from(document.querySelectorAll('body > *, body > * > *')).find(el => {
    const cs = getComputedStyle(el), r = el.getBoundingClientRect();
    return ['sticky', 'fixed'].includes(cs.position) && r.top <= 8 && r.height > 24 && r.height < 200
      && r.width > vw * 0.6;
  }) || null;
}
let kopf = null;
if (header) {
  const cs = getComputedStyle(header), r = header.getBoundingClientRect();
  kopf = {
    hoehe_px: Math.round(r.height),
    position: cs.position,
    klebend: ['sticky', 'fixed'].includes(cs.position),
    hintergrund: cs.backgroundColor,
    rahmen_unten: cs.borderBottomWidth === '0px' ? null : cs.borderBottomWidth + ' ' + cs.borderBottomColor,
    schatten: cs.boxShadow === 'none' ? null : cs.boxShadow,
    unscharf: /blur/.test(cs.backdropFilter || '') ? (cs.backdropFilter) : null,
  };
}

// --- Container-Breiten, Abschnitts-Abstaende, Schrift, Radien, Schatten
const maxBreiten = {}, padTop = {}, padBottom = {}, familien = {}, groessen = {},
      radien = {}, schatten = {}, hoehenZeile = {};
const alle = Array.from(document.querySelectorAll('*')).slice(0, 4000);
for (const el of alle) {
  if (!_sichtbar(el)) continue;
  const cs = getComputedStyle(el), r = el.getBoundingClientRect();
  if (r.width >= 400 && cs.maxWidth && cs.maxWidth !== 'none') {
    _zaehl(maxBreiten, cs.maxWidth);
  }
  const istAbschnitt = /^(section|main|article|footer)$/i.test(el.tagName)
    || /section|band|block|wrapper|row|panel/i.test(typeof el.className === 'string' ? el.className : '');
  if (istAbschnitt && r.width > vw * 0.5 && r.height > 120) {
    const pt = Math.round(parseFloat(cs.paddingTop)), pb = Math.round(parseFloat(cs.paddingBottom));
    if (pt >= 16) _zaehl(padTop, String(pt));
    if (pb >= 16) _zaehl(padBottom, String(pb));
  }
  const eigenerText = Array.from(el.childNodes)
    .some(n => n.nodeType === 3 && n.textContent.trim().length > 1);
  if (eigenerText) {
    _zaehl(familien, (cs.fontFamily || '').split(',')[0].replace(/["']/g, '').trim());
    _zaehl(groessen, String(Math.round(parseFloat(cs.fontSize))));
    const lh = cs.lineHeight === 'normal' ? 'normal' : String(Math.round(parseFloat(cs.lineHeight)));
    _zaehl(hoehenZeile, lh);
  }
  if (cs.borderRadius && cs.borderRadius !== '0px' && r.width > 8) _zaehl(radien, cs.borderRadius);
  if (cs.boxShadow && cs.boxShadow !== 'none') _zaehl(schatten, cs.boxShadow.slice(0, 120));
}

// --- Primaere Buttons (die ersten drei auffaelligen)
const istSichtbareFlaeche = cs => {
  const m = (cs.backgroundColor || '').match(/rgba?\(([^)]+)\)/);
  if (!m) return false;
  const teile = m[1].split(',').map(parseFloat);
  return (teile[3] === undefined ? 1 : teile[3]) > 0.1;
};
const buttons = [];
const kandidaten = document.querySelectorAll(
  'button, a[class*="btn" i], a[class*="button" i], [role="button"], input[type="submit"], .cta, [class*="cta" i]');
for (const el of kandidaten) {
  if (buttons.length >= 3) break;
  if (!_sichtbar(el)) continue;
  const cs = getComputedStyle(el), r = el.getBoundingClientRect();
  if (r.width < 60 || r.height < 24 || r.width > vw * 0.9) continue;
  if (!istSichtbareFlaeche(cs)) continue;
  const t = _text(el);
  if (!t) continue;
  buttons.push({
    text: t,
    hintergrund: cs.backgroundColor,
    textfarbe: cs.color,
    radius: cs.borderRadius,
    polster: cs.padding,
    groesse_px: Math.round(r.width) + 'x' + Math.round(r.height),
    schriftgroesse: cs.fontSize,
    schriftgewicht: cs.fontWeight,
    laufweite: cs.letterSpacing,
    versalien: cs.textTransform,
    rahmen: cs.borderWidth === '0px' ? null : cs.borderWidth + ' ' + cs.borderColor,
    schatten: cs.boxShadow === 'none' ? null : cs.boxShadow.slice(0, 100),
    transition: cs.transitionDuration === '0s' ? null
      : cs.transitionProperty + ' / ' + cs.transitionDuration + ' / ' + cs.transitionTimingFunction,
  });
}

// --- Icons
const svgs = Array.from(document.querySelectorAll('svg')).filter(_sichtbar);
let strich = 0, flaeche = 0;
const svgGroessen = {};
for (const s of svgs.slice(0, 60)) {
  const r = s.getBoundingClientRect();
  if (r.width > 4 && r.width < 80) _zaehl(svgGroessen, String(Math.round(r.width)));
  let hatStrich = false, hatFuellung = false;
  for (const k of [s, ...Array.from(s.querySelectorAll('*')).slice(0, 12)]) {
    const cs = getComputedStyle(k);
    const st = k.getAttribute && k.getAttribute('stroke');
    if ((cs.stroke && cs.stroke !== 'none') || (st && st !== 'none')) hatStrich = true;
    const f = k.getAttribute && k.getAttribute('fill');
    if ((cs.fill && cs.fill !== 'none' && cs.fill !== 'rgba(0, 0, 0, 0)') || (f && f !== 'none')) hatFuellung = true;
  }
  if (hatStrich) strich++; else if (hatFuellung) flaeche++;
}
const iconFonts = {};
const fontMuster = /material symbols|material icons|font ?awesome|ionicons|bootstrap-icons|remixicon|phosphor|feather|lucide|iconfont|glyphicons/i;
for (const el of alle) {
  const ff = getComputedStyle(el).fontFamily || '';
  const m = ff.match(fontMuster);
  if (m) _zaehl(iconFonts, m[0]);
}
const icons = {
  svg_gesamt: svgs.length,
  svg_in_kopfleiste: header ? header.querySelectorAll('svg').length : 0,
  svg_in_buttons: document.querySelectorAll('button svg, [role="button"] svg, a[class*="btn" i] svg').length,
  stil: strich > flaeche ? 'Linien-Icons (stroke)' : (flaeche ? 'gefuellte Icons (fill)' : 'unklar'),
  strich_basiert: strich,
  flaeche_basiert: flaeche,
  typische_groesse_px: _top(svgGroessen, 4),
  icon_fonts: _top(iconFonts, 4),
};

// --- Handy-Navigationsmuster
const burgerSel = '[class*="burger" i], [class*="hamburger" i], [class*="menu-toggle" i],'
  + ' [class*="nav-toggle" i], [aria-label*="menu" i], [aria-label*="menü" i],'
  + ' [aria-label*="navigation" i], button[aria-expanded]';
let burger = false, burgerInfo = null;
try {
  for (const el of document.querySelectorAll(burgerSel)) {
    if (!_sichtbar(el)) continue;
    const r = el.getBoundingClientRect();
    if (r.width > 120 || r.height > 120 || r.top > vh) continue;
    burger = true;
    burgerInfo = (el.getAttribute('aria-label') || _text(el) || el.tagName).slice(0, 40)
      + ' (' + Math.round(r.width) + 'x' + Math.round(r.height) + ')';
    break;
  }
} catch (e) {}
let untenFest = null, obenKlebend = null;
for (const el of alle) {
  const cs = getComputedStyle(el), r = el.getBoundingClientRect();
  if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
  if (!untenFest && cs.position === 'fixed' && r.height >= 36 && r.height <= 140
      && r.width >= vw * 0.8 && Math.abs(r.bottom - vh) < 6) {
    untenFest = {
      hoehe_px: Math.round(r.height),
      hintergrund: cs.backgroundColor,
      ziele: el.querySelectorAll('a, button, [role="tab"]').length,
    };
  }
  if (!obenKlebend && r.top <= 2 && r.height > 24 && r.height < 200 && r.width >= vw * 0.8) {
    obenKlebend = { hoehe_px: Math.round(r.height), position: cs.position };
  }
}

return {
  viewport: { breite: vw, hoehe: vh },
  seitenhoehe_px: Math.round(document.documentElement.scrollHeight),
  kopfleiste: kopf,
  container_max_breiten: _top(maxBreiten, 6),
  abschnitt_polster_oben_px: _top(padTop, 6),
  abschnitt_polster_unten_px: _top(padBottom, 6),
  schrift: {
    basis_groesse: getComputedStyle(document.body).fontSize,
    basis_zeilenhoehe: getComputedStyle(document.body).lineHeight,
    familien: _top(familien, 6),
    groessen_px: Object.keys(groessen).map(Number).sort((a, b) => b - a).slice(0, 12),
    groessen_haeufig_px: _top(groessen, 8),
    zeilenhoehen_px: _top(hoehenZeile, 6),
  },
  radien: _top(radien, 8),
  schatten: _top(schatten, 5),
  primaere_buttons: buttons,
  icons: icons,
  handy_navigation: {
    hamburger: burger,
    hamburger_element: burgerInfo,
    feste_leiste_unten: untenFest,
    klebend_oben: obenKlebend,
  },
};
"""

HOVER_PROPS = ["transform", "boxShadow", "backgroundColor", "color", "opacity",
               "borderColor", "textDecorationLine", "filter"]

JS_HOVER_KANDIDATEN = JS_HELFER + r"""
const vh = window.innerHeight;
const sel = 'a, button, [role="button"], [class*="card" i], [class*="tile" i],'
  + ' [class*="karte" i], [class*="kachel" i], [class*="panel" i],'
  + ' [class*="btn" i], [class*="button" i], [class*="cta" i]';
const gesehen = new Set();
const roh = [];
for (const el of document.querySelectorAll(sel)) {
  if (roh.length >= 40) break;
  if (!_sichtbar(el)) continue;
  const r = el.getBoundingClientRect();
  const oben = r.top + window.scrollY;          // Lage im Dokument, nicht im Fenster
  if (oben < 0 || oben > vh * 2.5) continue;
  if (r.width < 40 || r.height < 16) continue;
  const cs = getComputedStyle(el);
  const klasse = (typeof el.className === 'string' ? el.className : '').slice(0, 60);
  // Nur ein Beispiel je Bauart, damit nicht sechsmal dasselbe gemessen wird
  const signatur = el.tagName + '|' + klasse;
  if (gesehen.has(signatur)) continue;
  gesehen.add(signatur);
  let punkte = 1;
  if (/btn|button|cta/i.test(klasse) || el.tagName === 'BUTTON') punkte = 3;
  else if (/card|tile|kachel|karte/i.test(klasse)) punkte = 2;
  if (cs.transitionDuration !== '0s') punkte += 3;
  roh.push({
    el, punkte,
    tag: el.tagName.toLowerCase(),
    klasse: klasse,
    text: _text(el),
    dauer: cs.transitionDuration,
  });
}
roh.sort((a, b) => b.punkte - a.punkte);
const out = [];
roh.forEach((k, i) => {
  k.el.setAttribute('data-ls-hover', String(i));
  out.push({ i, tag: k.tag, klasse: k.klasse, text: k.text, dauer: k.dauer, punkte: k.punkte });
});
return out;
"""

JS_STIL = """([el, props]) => {
  const cs = getComputedStyle(el);
  const o = {};
  for (const p of props) o[p] = cs[p];
  o._transition = cs.transitionProperty + ' / ' + cs.transitionDuration + ' / ' + cs.transitionTimingFunction;
  return o;
}"""


# ---------------------------------------------------------------- Hilfen

CHROME_PFADE = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/opt/google/chrome/chrome", "/opt/google/chrome/google-chrome",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]


def browser_kennung(pfad):
    """Was das Programm selbst ueber sich sagt, z. B. 'Google Chrome 141.0.7390.37'."""
    try:
        lauf = subprocess.run([str(pfad), "--version"], capture_output=True,
                              text=True, timeout=15)
    except Exception:
        return None
    text = re.sub(r"\s+", " ", (lauf.stdout or "") + " " + (lauf.stderr or "")).strip()
    return text[:80] or None


def chrome_finden():
    """(Pfad, Kennung) eines wirklich installierten Google Chrome - sonst (None, None).

    `launch(channel="chrome")` meldet in manchen Umgebungen Erfolg und startet
    dabei das mitgelieferte Chromium; auch `/opt/google/chrome/chrome` kann ein
    Verweis darauf sein. Deshalb wird das Programm selbst gefragt, damit der
    Bericht nicht den falschen Browser nennt.
    """
    kandidaten = []
    for name in ("google-chrome", "google-chrome-stable", "chrome"):
        pfad = shutil.which(name)
        if pfad:
            kandidaten.append(pfad)
    kandidaten += CHROME_PFADE
    lokal = os.environ.get("LOCALAPPDATA")
    if lokal:
        kandidaten.append(str(pathlib.Path(lokal) / "Google/Chrome/Application/chrome.exe"))
    for pfad in kandidaten:
        if not pathlib.Path(pfad).exists():
            continue
        kennung = browser_kennung(pfad)
        if kennung and "google chrome" in kennung.lower():
            return pfad, kennung
    return None, None


def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")
    return s or "seite"


def front_matter_website(pfad):
    """`website:` aus dem YAML-Kopf eines Profils lesen."""
    text = pfad.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return None
    for line in m.group(1).splitlines():
        k, sep, v = line.partition(":")
        if sep and k.strip() == "website":
            return v.strip().strip("\"'") or None
    return None


def normtext(s):
    s = re.sub(r"\s+", " ", str(s or "")).strip().lower()
    return s


def ist_ablehnen(text):
    """True, wenn die Beschriftung eindeutig ablehnt (und nicht zustimmt)."""
    t = normtext(text)
    if not t or len(t) > 60:
        return False
    if not any(re.search(p, t) for p in ABLEHNEN):
        return False
    if not ZUSTIMMEN_AUSNAHME.search(t) and any(w in t for w in ZUSTIMMEN):
        return False
    return True


def consent_selektoren():
    teile = []
    for key in CONSENT_KEYS:
        for attr in ("id", "class"):
            teile.append(f'[{attr}*="{key}" i]')
    teile += ['[aria-label*="cookie" i]', '[aria-label*="consent" i]',
              '[data-testid*="cookie" i]']
    return ", ".join(teile)


JS_CONSENT_VERSTECKEN = """(sel) => {
  let versteckt = 0;
  let kandidaten = [];
  try { kandidaten = Array.from(document.querySelectorAll(sel)); } catch (e) { return -1; }
  for (const el of kandidaten) {
    if (el === document.body || el === document.documentElement) continue;
    // Seiten-Huellen nie verstecken: sie enthalten die Landmarken der Seite
    if (el.querySelector('main, header, [role="banner"], footer, article')) continue;
    if (el.tagName === 'MAIN' || el.tagName === 'ARTICLE') continue;
    el.style.setProperty('display', 'none', 'important');
    versteckt++;
  }
  // Scrollsperre der Consent-Schicht aufheben
  for (const el of [document.documentElement, document.body]) {
    for (const p of ['overflow', 'overflow-y', 'position', 'height', 'filter']) {
      el.style.removeProperty(p);
    }
    el.style.setProperty('overflow', 'auto', 'important');
    el.style.setProperty('position', 'static', 'important');
    el.style.setProperty('height', 'auto', 'important');
  }
  return versteckt;
}"""


def consent_wegklicken(page, fehler, protokoll, label=""):
    """Zuerst eindeutig ablehnende Buttons klicken, dann Reste verstecken."""
    geklickt = []
    sel = ('button, [role="button"], a, input[type="button"], input[type="submit"], '
           '[class*="button" i], [class*="btn" i]')
    for frame in list(page.frames)[:6]:
        try:
            elemente = frame.query_selector_all(sel)
        except Exception:
            continue
        for el in elemente[:200]:
            try:
                text = (el.inner_text() or "").strip() or el.get_attribute("aria-label") or ""
            except Exception:
                continue
            if not ist_ablehnen(text):
                continue
            try:
                if not el.is_visible():
                    continue
                el.click(timeout=2500)
                geklickt.append(normtext(text)[:40])
                page.wait_for_timeout(700)
            except Exception as exc:
                fehler.append(f"Consent-Klick '{normtext(text)[:30]}': {type(exc).__name__}")
            break
        if geklickt:
            break
    versteckt = 0
    try:
        versteckt = page.evaluate(JS_CONSENT_VERSTECKEN, consent_selektoren())
    except Exception as exc:
        fehler.append(f"Consent-Ausblenden: {type(exc).__name__}")
    protokoll.append(
        f"{label}: " + ("abgelehnt per Klick auf " + ", ".join(f'"{g}"' for g in geklickt)
                        if geklickt else "kein Ablehnen-Button gefunden")
        + f"; {max(versteckt, 0)} Consent-Element(e) ausgeblendet")
    return geklickt


def maus_parken(page):
    """Zeiger in den linken Seitenrand stellen - sonst bleibt nach einem Klick
    ein Hover-Zustand unter dem Zeiger stehen und landet im Screenshot."""
    try:
        hoehe = page.evaluate("window.innerHeight") or 600
        page.mouse.move(2, max(2, int(hoehe / 2)))
    except Exception:
        pass


def durchscrollen(page, timeout_ms, fehler):
    """In Schritten durchscrollen (Lazy Loading ausloesen), dann wieder nach oben."""
    try:
        # 'scroll-behavior: smooth' wuerde jedes scrollTo animieren - dann messen wir mittendrin
        page.add_style_tag(content="html, body, * { scroll-behavior: auto !important; }")
    except Exception:
        pass
    try:
        for _ in range(24):
            vorher = page.evaluate("window.scrollY")
            page.evaluate("window.scrollBy(0, Math.round(window.innerHeight * 0.8))")
            page.wait_for_timeout(260)
            nachher = page.evaluate("window.scrollY")
            if nachher - vorher < 10:
                break
        for _ in range(12):                     # wirklich oben ankommen
            page.evaluate("window.scrollTo(0, 0)")
            page.wait_for_timeout(120)
            if page.evaluate("window.scrollY") <= 1:
                break
        page.wait_for_timeout(300)
    except Exception as exc:
        fehler.append(f"Scrollen: {type(exc).__name__}")
    try:
        page.wait_for_load_state("networkidle", timeout=min(timeout_ms, 8000))
    except Exception:
        pass            # Seiten mit Dauerverbindungen werden nie "idle" - egal


JS_REVEAL_VOR_SCROLL = JS_HELFER + r"""
const alle = Array.from(document.querySelectorAll('*')).slice(0, 4000);
let n = 0;
const klassen = new Set(), dauern = {};
for (const el of alle) {
  const cs = getComputedStyle(el);
  if (parseFloat(cs.opacity) === 0 && cs.transform && cs.transform !== 'none') {
    n++;
    if (klassen.size < 8 && typeof el.className === 'string' && el.className.trim()) {
      klassen.add(el.className.trim().split(/\s+/).slice(0, 3).join(' ').slice(0, 60));
    }
    const d = _ms(_split(cs.transitionDuration)[0]);
    if (d > 0) _zaehl(dauern, String(Math.round(d / 10) * 10));
  }
}
return { anzahl: n, beispiel_klassen: Array.from(klassen), dauern_ms: _top(dauern, 4) };
"""


def seite_oeffnen(page, url, timeout_ms, fehler, protokoll, label=""):
    """Seite laden, Consent abwehren, durchscrollen. Gibt die Werte vor dem Scrollen zurueck."""
    antwort = page.goto(url, timeout=timeout_ms, wait_until="domcontentloaded")
    status = antwort.status if antwort is not None else None
    if status is not None and status >= 400:
        # Fehlerseite statt Inhalt: nicht fotografieren, nicht messen
        raise SeitenFehler(f"HTTP {status} ({HTTP_GRUND.get(status, 'Fehlerseite')})")
    try:
        page.wait_for_load_state("load", timeout=min(timeout_ms, 10000))
    except Exception:
        pass
    page.wait_for_timeout(700)
    consent_wegklicken(page, fehler, protokoll, label or url)
    maus_parken(page)
    vor_scroll = None
    try:                                   # vor dem Scrollen: noch versteckte Reveal-Elemente
        vor_scroll = page.evaluate(f"() => {{ {JS_REVEAL_VOR_SCROLL} }}")
    except Exception as exc:
        fehler.append(f"Reveal-Messung: {type(exc).__name__}")
    durchscrollen(page, timeout_ms, fehler)
    try:
        page.evaluate(JS_CONSENT_VERSTECKEN, consent_selektoren())   # nach Lazy Loading erneut
    except Exception:
        pass
    return vor_scroll


def bilder_machen(page, out, basis, max_hoehe, fehler, beschreibungen=("", "")):
    """Viewport-Bild und Vollbild (Hoehe begrenzt).

    Gibt (Dateiname, Beschreibung)-Paare nur fuer wirklich entstandene Bilder
    zurueck - ein fehlgeschlagenes Bild darf das andere nicht falsch beschriften.
    """
    gemacht = []
    maus_parken(page)
    try:
        page.screenshot(path=str(out / f"{basis}.png"))
        gemacht.append((f"{basis}.png", beschreibungen[0]))
    except Exception as exc:
        fehler.append(f"{basis}.png: {type(exc).__name__}: {exc}".replace("\n", " ")[:160])
    try:
        hoehe = page.evaluate("document.documentElement.scrollHeight")
        breite = page.evaluate("document.documentElement.clientWidth")
        if hoehe and hoehe > max_hoehe:
            page.screenshot(path=str(out / f"{basis}-voll.png"), full_page=True,
                            clip={"x": 0, "y": 0, "width": breite, "height": max_hoehe})
        else:
            page.screenshot(path=str(out / f"{basis}-voll.png"), full_page=True)
        gemacht.append((f"{basis}-voll.png", beschreibungen[1]))
    except Exception as exc:
        fehler.append(f"{basis}-voll.png: {type(exc).__name__}: {exc}".replace("\n", " ")[:160])
    return gemacht


def hover_messen(page, fehler, anzahl=6):
    """Bis zu `anzahl` Elemente anfahren und Stil-Aenderungen notieren."""
    ergebnis = []
    try:
        kandidaten = page.evaluate(f"() => {{ {JS_HOVER_KANDIDATEN} }}")
    except Exception as exc:
        fehler.append(f"Hover-Kandidaten: {type(exc).__name__}")
        return ergebnis
    for kand in kandidaten:
        if len(ergebnis) >= anzahl:
            break
        sel = f'[data-ls-hover="{kand["i"]}"]'
        try:
            el = page.query_selector(sel)
            if el is None or not el.is_visible():
                continue
            vorher = page.evaluate(JS_STIL, [el, HOVER_PROPS])
            el.scroll_into_view_if_needed(timeout=2000)
            el.hover(timeout=2500, force=True)
            dauer = max(260, min(1400, int(_max_ms(vorher.get("_transition", "")) + 120)))
            page.wait_for_timeout(dauer)
            nachher = page.evaluate(JS_STIL, [el, HOVER_PROPS])
        except Exception:
            continue
        aenderungen = {p: {"vorher": vorher.get(p), "nachher": nachher.get(p)}
                       for p in HOVER_PROPS
                       if vorher.get(p) != nachher.get(p)}
        if aenderungen:
            ergebnis.append({
                "element": f'{kand["tag"]}.{kand["klasse"]}'.strip("."),
                "text": kand["text"],
                "transition": nachher.get("_transition"),
                "aenderungen": aenderungen,
            })
    maus_parken(page)
    try:
        page.evaluate("() => document.querySelectorAll('[data-ls-hover]')"
                      ".forEach(e => e.removeAttribute('data-ls-hover'))")
    except Exception:
        pass
    return ergebnis


def _max_ms(transition_text):
    werte = re.findall(r"([\d.]+)(ms|s)\b", str(transition_text or ""))
    ms = [float(v) * (1000 if e == "s" else 1) for v, e in werte]
    return max(ms) if ms else 0


def unterseiten_finden(page, start_url, anzahl, fehler):
    """Bis zu `anzahl` Unterseiten aus Kopf- und Navigationslinks waehlen."""
    try:
        links = page.evaluate("""() => {
          const sel = 'header a[href], nav a[href], [role="navigation"] a[href],'
            + ' [class*="nav" i] a[href], [class*="header" i] a[href], [class*="menu" i] a[href]';
          const out = [];
          for (const a of document.querySelectorAll(sel)) {
            out.push({ href: a.href, text: (a.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 60) });
            if (out.length > 300) break;
          }
          return out;
        }""")
    except Exception as exc:
        fehler.append(f"Navigationslinks: {type(exc).__name__}")
        return []

    start = urllib.parse.urlsplit(start_url)
    host_start = start.netloc.lower().removeprefix("www.")
    gesehen, kandidaten = set(), []
    for link in links:
        href = link.get("href") or ""
        try:
            u = urllib.parse.urlsplit(href)
        except ValueError:
            continue
        if u.scheme not in ("http", "https"):
            continue                                   # mailto:, tel:, javascript:
        if u.netloc.lower().removeprefix("www.") != host_start:
            continue                                   # andere Domain
        pfad = u.path or "/"
        if pfad in ("", "/") or pfad.rstrip("/") == start.path.rstrip("/"):
            continue                                   # Startseite / nur Anker
        if pfad.lower().endswith(DATEI_ENDUNGEN):
            continue
        ganz = (pfad + "?" + u.query + " " + normtext(link.get("text"))).lower()
        if any(w in ganz for w in UEBERSPRINGEN):
            continue
        segmente = [s for s in pfad.split("/") if s]
        erst = segmente[0].lower() if segmente else ""
        if not erst or erst in gesehen:
            continue
        gesehen.add(erst)
        punkte = 0
        for i, wort in enumerate(BEVORZUGT):
            if erst == wort:
                punkte = 1000 - i
                break
            if wort in erst and punkte == 0:
                punkte = 500 - i
        if len(segmente) > 2:
            punkte -= 50
        kandidaten.append({
            "url": urllib.parse.urlunsplit((u.scheme, u.netloc, pfad, u.query, "")),
            "name": slugify(erst)[:28],
            "text": link.get("text") or erst,
            "punkte": punkte,
        })
    kandidaten.sort(key=lambda k: -k["punkte"])
    return kandidaten[:anzahl]


# ---------------------------------------------------------------- Bericht

def _liste(eintraege, einheit="", grenze=4):
    teile = [f'{e["wert"]}{einheit} ({e["anzahl"]}x)' for e in (eintraege or [])[:grenze]]
    return ", ".join(teile) if teile else "keine"


def bericht_schreiben(out, info, layout, bewegung, bilder, fehler, protokoll, teilfehler=()):
    teilfehler = list(teilfehler)
    z = []
    z.append(f'# Echte Website-Werte: {info["marke"]}')
    z.append("")
    z.append(f'- **Website:** {info["url"]}')
    z.append(f'- **Datum:** {info["datum"]}')
    z.append(f'- **Browser:** {info["browser"]}')
    z.append(f'- **Seiten:** ' + ", ".join(info["seiten"]))
    z.append(f'- **Ergebnis:** ' + (
        f"Teilerfolg - {len(teilfehler)} Seite(n)/Bild(er) nicht erfasst (siehe "
        f'"Nicht erfasste Seiten")' if teilfehler else "alle gewaehlten Seiten erfasst"))
    z.append("")
    z.append("> Nur zur Anschauung. Nichts aus den Bildern kopieren, nichts veroeffentlichen.")
    z.append("> Gemessene Werte haben Vorrang vor den Empfehlungen im Profil.")
    z.append('> Was hier "nicht gemessen" heisst, ist kein Messwert: dafuer gilt das Profil.')
    z.append("")

    if teilfehler:
        z.append("## Nicht erfasste Seiten")
        z.append("")
        for t in dict.fromkeys(teilfehler):
            z.append(f"- {t}")
        z.append("")
        grund = ursache_text(teilfehler)
        if grund:
            z.append(f"Wahrscheinliche Ursache: {grund}.")
        z.append("")

    z.append("## Bilder")
    z.append("")
    for datei, beschreibung in bilder:
        z.append(f"- `{datei}` – {beschreibung}")
    if not bilder:
        z.append("- keine Bilder entstanden")
    z.append("")

    z.append("## Layout (Desktop-Startseite, 1440x900)")
    z.append("")
    if layout:
        kopf = layout.get("kopfleiste")
        if kopf:
            z.append(f'- **Kopfleiste:** {kopf["hoehe_px"]} px hoch, `position: {kopf["position"]}`'
                     f' ({"klebt beim Scrollen" if kopf["klebend"] else "scrollt mit"}),'
                     f' Flaeche {kopf["hintergrund"]}'
                     + (f', Rahmen unten {kopf["rahmen_unten"]}' if kopf.get("rahmen_unten") else "")
                     + (f', Schatten {kopf["schatten"]}' if kopf.get("schatten") else "")
                     + (f', Backdrop {kopf["unscharf"]}' if kopf.get("unscharf") else ""))
        else:
            z.append("- **Kopfleiste:** nicht erkannt")
        z.append(f'- **Containerbreite:** {_liste(layout.get("container_max_breiten"))}')
        z.append(f'- **Abschnitts-Polster:** oben {_liste(layout.get("abschnitt_polster_oben_px"), " px", 3)}'
                 f' / unten {_liste(layout.get("abschnitt_polster_unten_px"), " px", 3)}')
        s = layout.get("schrift", {})
        z.append(f'- **Schrift:** Basis {s.get("basis_groesse")} / Zeilenhoehe {s.get("basis_zeilenhoehe")};'
                 f' Familien: {_liste(s.get("familien"), "", 3)}')
        z.append(f'- **Groessen-Skala (px):** {", ".join(str(g) for g in (s.get("groessen_px") or []))}')
        z.append(f'- **Radien:** {_liste(layout.get("radien"), "", 5)}')
        z.append(f'- **Schatten:** {_liste(layout.get("schatten"), "", 2)}')
        ic = layout.get("icons", {})
        z.append(f'- **Icons:** {ic.get("stil")}, {ic.get("svg_gesamt")} Inline-SVG'
                 f' ({ic.get("svg_in_kopfleiste")} in der Kopfleiste, {ic.get("svg_in_buttons")} in Buttons),'
                 f' typische Groesse {_liste(ic.get("typische_groesse_px"), " px", 2)}'
                 + (f', Icon-Font: {_liste(ic.get("icon_fonts"), "", 2)}' if ic.get("icon_fonts") else ", kein Icon-Font"))
        for i, b in enumerate(layout.get("primaere_buttons") or [], 1):
            z.append(f'- **Button {i} ("{b["text"]}"):** {b["hintergrund"]} auf {b["textfarbe"]},'
                     f' Radius {b["radius"]}, Polster {b["polster"]}, {b["schriftgroesse"]}/{b["schriftgewicht"]},'
                     f' Laufweite {b["laufweite"]}, Versalien {b["versalien"]}'
                     + (f', Transition {b["transition"]}' if b.get("transition") else ""))
        if not layout.get("primaere_buttons"):
            z.append("- **Buttons:** keine gefuellten Buttons erkannt")
        nav = layout.get("handy_navigation") or {}
        teile = []
        teile.append("Hamburger vorhanden" + (f' ({nav["hamburger_element"]})' if nav.get("hamburger_element") else "")
                     if nav.get("hamburger") else "kein Hamburger erkannt")
        if nav.get("feste_leiste_unten"):
            u = nav["feste_leiste_unten"]
            teile.append(f'feste Leiste unten ({u["hoehe_px"]} px, {u["ziele"]} Ziele, {u["hintergrund"]})')
        else:
            teile.append("keine feste Leiste unten")
        if nav.get("klebend_oben"):
            teile.append(f'oben klebend ({nav["klebend_oben"]["position"]}, {nav["klebend_oben"]["hoehe_px"]} px)')
        z.append(f'- **Handy-Navigation:** ' + "; ".join(teile))
    else:
        z.append("- **Nicht gemessen** - die Layoutwerte der Startseite konnten nicht"
                 " ausgelesen werden. Hier gelten die Empfehlungen im Profil.")
    z.append("")

    z.append("## Bewegung")
    z.append("")
    start = bewegung.get("desktop-start") or {}
    t = start.get("transitions", {})
    a = start.get("animationen", {})
    if start:
        z.append(f'- **Transitions:** {t.get("elemente", 0)} Elemente;'
                 f' Dauern {_liste(t.get("dauern_ms"), " ms", 5)}')
        z.append(f'- **Easings:** {_liste(t.get("easings"), "", 3)}')
        z.append(f'- **Animierte Eigenschaften:** {_liste(t.get("eigenschaften"), "", 5)}')
        z.append(f'- **Keyframe-Animationen:** {a.get("elemente", 0)} Elemente,'
                 f' Namen {_liste(a.get("namen"), "", 4)}, Dauern {_liste(a.get("dauern_ms"), " ms", 3)},'
                 f' Wiederholungen {_liste(a.get("wiederholungen"), "", 2)}')
        kf = start.get("keyframes") or []
        z.append(f'- **@keyframes im CSS:** {", ".join(kf[:12]) if kf else "keine lesbaren"}'
                 + (f' (+{len(kf) - 12} weitere)' if len(kf) > 12 else "")
                 + (f'; {start.get("css_nicht_lesbar")} Stylesheets nicht lesbar (CORS)'
                    if start.get("css_nicht_lesbar") else ""))
        z.append(f'- **prefers-reduced-motion:** '
                 + ("Regeln vorhanden - respektiert reduzierte Bewegung"
                    if start.get("prefers_reduced_motion_regeln") else "keine Regeln gefunden"))
        rev = start.get("scroll_reveal", {})
        vor = rev.get("vor_dem_scrollen")
        hinweise = ", ".join(f"{k}: {v}" for k, v in (rev.get("treffer") or {}).items())
        if vor:
            stand = (f'vor dem Scrollen {vor.get("anzahl", 0)} Elemente mit opacity 0 + transform'
                     + (f' (Dauer {_liste(vor.get("dauern_ms"), " ms", 2)})' if vor.get("dauern_ms") else "")
                     + (f', z. B. `{vor["beispiel_klassen"][0]}`' if vor.get("beispiel_klassen") else ""))
        else:
            # Die Zahl aus JS_BEWEGUNG entsteht nach dem Scrollen - nicht als "vorher" ausgeben
            stand = (f'Stand vor dem Scrollen nicht gemessen; nach dem Scrollen'
                     f' {rev.get("opacity0_mit_transform", 0)} Elemente mit opacity 0 + transform')
        z.append(f'- **Scroll-Reveal:** {hinweise or "keine Marker"}; {stand}')
        hovers = start.get("hover") or []
        if hovers:
            z.append(f'- **Hover-Effekte ({len(hovers)} gemessen):**')
            for h in hovers:
                aend = "; ".join(f'{p}: {v["vorher"]} → {v["nachher"]}'
                                 for p, v in h["aenderungen"].items())
                z.append(f'  - `{h["element"]}` ("{h["text"]}"): {aend} [Transition: {h["transition"]}]')
        else:
            z.append("- **Hover-Effekte:** keine Stil-Aenderungen messbar")
    else:
        z.append("- **Nicht gemessen** - die Bewegungswerte der Startseite konnten nicht"
                 " ausgelesen werden. Hier gelten die Empfehlungen im Profil.")
    weitere = [k for k in bewegung if k != "desktop-start"]
    if weitere:
        z.append("")
        z.append("Weitere Seiten (Werte in `bewegung.json`):")
        for k in weitere:
            w = bewegung[k]
            z.append(f'- `{k}`: {w.get("transitions", {}).get("elemente", 0)} Transition-Elemente,'
                     f' Dauern {_liste(w.get("transitions", {}).get("dauern_ms"), " ms", 3)},'
                     f' {len(w.get("hover") or [])} Hover-Effekte')
    z.append("")

    z.append("## Uebernehmen")
    z.append("")
    dauern = (t.get("dauern_ms") or [])
    easings = (t.get("easings") or [])
    if dauern:
        z.append(f'- Haeufigste Transition-Dauer: **{dauern[0]["wert"]} ms**.')
    else:
        z.append("- Transition-Dauer: nicht gemessen - Wert aus dem Profil nehmen.")
    if easings:
        z.append(f'- Haeufigstes Easing: **{easings[0]["wert"]}**.')
    else:
        z.append("- Easing: nicht gemessen - Wert aus dem Profil nehmen.")
    kurz = [d["wert"] for d in dauern if d["wert"].isdigit() and int(d["wert"]) <= 300]
    if kurz:
        z.append(f'- Kurze Interaktionen (Hover, Flaeche): **{kurz[0]} ms**.')
    hovers = start.get("hover") or []
    if hovers:
        z.append(f'- Hover-Muster: {", ".join(sorted({p for h in hovers for p in h["aenderungen"]}))}.')
    if layout and layout.get("container_max_breiten"):
        z.append(f'- Inhaltsbreite: **{layout["container_max_breiten"][0]["wert"]}**.')
    elif layout:
        z.append("- Inhaltsbreite: nicht gemessen.")
    if layout and layout.get("radien"):
        z.append(f'- Haupt-Radius: **{layout["radien"][0]["wert"]}**.')
    elif layout:
        z.append("- Haupt-Radius: nicht gemessen.")
    if not layout:
        z.append("- Layoutwerte: nicht gemessen - Abstaende, Breiten und Radien aus dem Profil nehmen.")
    z.append("")

    z.append("## Ablauf und Fehler")
    z.append("")
    for p in protokoll:
        z.append(f"- {p}")
    if fehler:
        z.append("")
        z.append("**Fehler:**")
        for f in dict.fromkeys(fehler):
            z.append(f"- {f}")
    else:
        z.append("- Keine Fehler.")
    z.append("")
    (out / "zusammenfassung.md").write_text("\n".join(z) + "\n", encoding="utf-8")


def fehlbericht_schreiben(out, info, fehler, protokoll, entfernt=()):
    """Kurze Notiz, wenn nichts gemessen wurde - ausdruecklich keine Messwerte."""
    z = []
    z.append(f'# Keine Messung: {info["marke"]}')
    z.append("")
    z.append(f'- **Website:** {info["url"]}')
    z.append(f'- **Datum:** {info["datum"]}')
    z.append(f'- **Browser:** {info["browser"]}')
    z.append("")
    z.append("## Es wurde nichts gemessen")
    z.append("")
    z.append("Die Startseite konnte nicht geladen oder nicht ausgelesen werden.")
    z.append(f"Wahrscheinliche Ursache: **{ursache_text(fehler) or UNKLAR}**.")
    z.append("")
    z.append("Dieser Lauf enthaelt **keine** Messwerte: keine Bilder, keine `layout.json`,")
    z.append("keine `bewegung.json`. Es gibt also nichts, was Vorrang vor dem Profil haette.")
    z.append("**Fuer das Design die Empfehlungen im Profil (`designsprache/<slug>.md`)**")
    z.append("**verwenden** und im Ergebnis nicht behaupten, Werte seien gemessen.")
    if entfernt:
        z.append("")
        z.append("Entfernt, um keine alten Werte als Ergebnis dieses Laufs auszugeben: "
                 + ", ".join(f"`{e}`" for e in entfernt) + ".")
    z.append("")
    z.append("## Was helfen kann")
    z.append("")
    z.append("- Netzzugang pruefen (in dieser Umgebung ist das Internet oft gesperrt).")
    z.append("- Die URL im normalen Browser oeffnen: stimmt sie, antwortet die Seite?")
    z.append("- Bei langsamen Seiten `--timeout 60` setzen.")
    z.append("- Seiten mit Bot-Sperre (HTTP 403) lassen sich so nicht fotografieren.")
    z.append("")
    z.append("## Ablauf und Fehler")
    z.append("")
    for p in protokoll:
        z.append(f"- {p}")
    if fehler:
        z.append("")
        z.append("**Fehler:**")
        for f in dict.fromkeys(fehler):
            z.append(f"- {f}")
    z.append("")
    (out / "zusammenfassung.md").write_text("\n".join(z) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- Hauptlauf

def main(argv=None):
    p = argparse.ArgumentParser(
        prog="live_screens.py",
        description="Echte Website-Screens einer Marke holen und Bewegungs- und Layoutwerte auslesen.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Beispiele:\n"
               "  python3 live_screens.py stripe\n"
               "  python3 live_screens.py https://stripe.com --seiten 2 --kein-handy\n"
               "\n"
               "Exit-Codes:\n"
               "  0  Erfolg: Startseite und alle gewaehlten Unterseiten erfasst\n"
               "  3  Teilerfolg: Startseite erfasst, einzelne Seiten oder Bilder\n"
               "     fehlgeschlagen; zusammenfassung.md nennt sie unter\n"
               "     'Nicht erfasste Seiten'\n"
               "  1  Totalfehler: nichts gemessen (kein Netz, Seite gesperrt oder nicht\n"
               "     erreichbar, Profil oder website: fehlt). Es entstehen keine\n"
               "     Ergebnisdateien, nur eine kurze Fehlernotiz in zusammenfassung.md\n"
               "  2  Abhaengigkeit fehlt: Playwright nicht installiert oder kein\n"
               "     Browser startbar\n"
               "\n"
               "Die Bilder dienen nur der Anschauung - nichts daraus kopieren, nichts veroeffentlichen.")
    p.add_argument("ziel", metavar="slug|url",
                   help="Marken-Slug (liest website: aus designsprache/<slug>.md) oder direkte URL")
    p.add_argument("--skill-dir", metavar="DIR", default=None,
                   help="Ordner des Skills (Standard: der uebergeordnete Ordner dieses Skripts)")
    p.add_argument("--out", metavar="DIR", default=None,
                   help="Ausgabeordner (Standard: ~/.cache/all-top-brands-design-skill/live/<slug>/)")
    p.add_argument("--seiten", metavar="N", type=int, default=3,
                   help="Anzahl der Unterseiten zusaetzlich zur Startseite (Standard: 3, 0 = keine)")
    p.add_argument("--kein-handy", action="store_true",
                   help="keine Handy-Bilder machen (nur Desktop)")
    p.add_argument("--max-hoehe", metavar="PX", type=int, default=6000,
                   help="maximale Hoehe der Vollbild-Aufnahmen in px (Standard: 6000)")
    p.add_argument("--timeout", metavar="S", type=int, default=30,
                   help="Zeitgrenze je Seite in Sekunden (Standard: 30)")
    args = p.parse_args(argv)

    try:
        from playwright.sync_api import sync_playwright
    except Exception:
        print(PLAYWRIGHT_HINWEIS, file=sys.stderr)
        return EXIT_ABHAENGIGKEIT

    # ---- Ziel bestimmen
    ziel = args.ziel.strip()
    skill_dir = pathlib.Path(args.skill_dir).expanduser() if args.skill_dir else HERE.parent
    if re.match(r"^https?://", ziel, re.I):
        url = ziel
        slug = slugify(urllib.parse.urlsplit(url).netloc.removeprefix("www.").rsplit(":", 1)[0])
        marke = urllib.parse.urlsplit(url).netloc
    else:
        slug = slugify(ziel)
        profil = skill_dir / "designsprache" / f"{ziel}.md"
        if not profil.exists():
            print(f"Profil nicht gefunden: {profil}\n"
                  f"Entweder --skill-dir auf den Skill-Ordner setzen oder direkt eine URL uebergeben.\n"
                  f"Nichts gemessen - es gelten die Empfehlungen im Profil.",
                  file=sys.stderr)
            return EXIT_TOTAL
        url = front_matter_website(profil)
        if not url:
            print(f"Kein 'website:' im YAML-Kopf von {profil}. Bitte URL direkt uebergeben.\n"
                  f"Nichts gemessen - es gelten die Empfehlungen im Profil.", file=sys.stderr)
            return EXIT_TOTAL
        if not re.match(r"^https?://", url, re.I):
            url = "https://" + url.lstrip("/")
        marke = ziel

    out = pathlib.Path(args.out).expanduser() if args.out else (
        pathlib.Path.home() / ".cache" / "all-top-brands-design-skill" / "live" / slug)
    out.mkdir(parents=True, exist_ok=True)
    timeout_ms = max(5, args.timeout) * 1000

    fehler, protokoll, bilder = [], [], []
    teilfehler = []            # Seiten oder Bilder, die nicht erfasst wurden
    bewegung, layout = {}, None
    seitennamen = []
    print(f"Website: {url}\nAusgabe: {out}")

    with sync_playwright() as pw:
        # ---- Browser: zuerst das installierte Google Chrome, dann Playwright-Chromium.
        # Es wird nur gemeldet, was wirklich gestartet wurde.
        browser, browser_name = None, "unbekannt"
        chrome_pfad, chrome_kennung = chrome_finden()
        if chrome_pfad:
            try:
                # Fester Pfad statt channel="chrome": so steht fest, was laeuft
                browser = pw.chromium.launch(executable_path=chrome_pfad)
                browser_name = f"{chrome_kennung} (installiert: {chrome_pfad})"
            except Exception as exc:
                protokoll.append(f"Google Chrome unter {chrome_pfad} nicht startbar "
                                 f"({type(exc).__name__}), nehme Playwright-Chromium")
        else:
            protokoll.append("Kein installiertes Google Chrome gefunden, nehme Playwright-Chromium")
        if browser is None:
            try:
                browser = pw.chromium.launch()
                try:
                    exe = pw.chromium.executable_path
                except Exception:
                    exe = None
                kennung = browser_kennung(exe) if exe else None
                browser_name = (f"{kennung or 'Chromium ' + browser.version}"
                                f" (von Playwright mitgeliefert: {exe or 'Pfad unbekannt'})")
            except Exception as exc2:
                print("Kein Browser startbar.\n", PLAYWRIGHT_HINWEIS, f"\n\nFehler: {exc2}", file=sys.stderr)
                return EXIT_ABHAENGIGKEIT
        print(f"Browser: {browser_name}")
        protokoll.append(f"Browser: {browser_name}")

        startseite_ok = False
        unterseiten = []
        try:
            # ---------------- Desktop
            ctx = browser.new_context(viewport={"width": 1440, "height": 900},
                                      device_scale_factor=1, locale="de-DE")
            ctx.set_default_timeout(timeout_ms)
            page = ctx.new_page()
            try:
                vor_scroll = seite_oeffnen(page, url, timeout_ms, fehler, protokoll,
                                           "Startseite (Desktop)")
                startseite_ok = True
                neu = bilder_machen(page, out, "desktop-start", args.max_hoehe, fehler,
                                    ("Startseite Desktop, erster Bildschirm (1440x900)",
                                     "Startseite Desktop, ganze Seite von oben bis unten"))
                bilder += neu
                if len(neu) < 2:
                    teilfehler.append(f"Startseite (Desktop) {url}: {2 - len(neu)} von 2 Bildern"
                                      f" nicht erstellt")
                seitennamen.append("Startseite (Desktop)")
                layout = page.evaluate(f"() => {{ {JS_LAYOUT} }}")
                mot = page.evaluate(f"() => {{ {JS_BEWEGUNG} }}")
                mot["scroll_reveal"]["vor_dem_scrollen"] = vor_scroll
                mot["hover"] = hover_messen(page, fehler)
                bewegung["desktop-start"] = mot
                if args.seiten > 0:
                    unterseiten = unterseiten_finden(page, url, args.seiten, fehler)
                    protokoll.append("Unterseiten gewaehlt: " + (
                        ", ".join(f'{u["name"]} ({u["url"]})' for u in unterseiten) or "keine gefunden"))
            except Exception as exc:
                grund = fehlergrund(exc)
                fehler.append(f"Startseite {url}: {grund}")
                teilfehler.append(f"Startseite (Desktop) {url}: {grund}")

            for u in unterseiten:                       # eine Seite nach der anderen
                try:
                    vor_scroll = seite_oeffnen(page, u["url"], timeout_ms, fehler, protokoll,
                                               f'{u["name"]} (Desktop)')
                    neu = bilder_machen(page, out, f'desktop-{u["name"]}', args.max_hoehe, fehler,
                                        (f'Unterseite "{u["text"]}" Desktop, erster Bildschirm',
                                         f'Unterseite "{u["text"]}" Desktop, ganze Seite'))
                    bilder += neu
                    if len(neu) < 2:
                        teilfehler.append(f'Unterseite {u["url"]}: {2 - len(neu)} von 2 Bildern'
                                          f' nicht erstellt')
                    seitennamen.append(f'{u["text"]} (Desktop)')
                    mot = page.evaluate(f"() => {{ {JS_BEWEGUNG} }}")
                    mot["url"] = u["url"]
                    mot["scroll_reveal"]["vor_dem_scrollen"] = vor_scroll
                    mot["hover"] = hover_messen(page, fehler, anzahl=4)
                    bewegung[f'desktop-{u["name"]}'] = mot
                except Exception as exc:
                    grund = fehlergrund(exc)
                    fehler.append(f'Unterseite {u["url"]}: {grund}')
                    teilfehler.append(f'Unterseite {u["url"]} ({u["text"]}, Desktop): {grund}')
            ctx.close()

            # ---------------- Handy
            if not args.kein_handy and startseite_ok:
                device = dict(pw.devices["iPhone 13"])
                device["device_scale_factor"] = 2       # 3x waere unnoetig gross
                ctx = browser.new_context(locale="de-DE", **device)
                ctx.set_default_timeout(timeout_ms)
                page = ctx.new_page()
                handy = [("start", url, "Startseite")]
                if unterseiten:
                    handy.append((unterseiten[0]["name"], unterseiten[0]["url"], unterseiten[0]["text"]))
                for name, hurl, text in handy:
                    try:
                        vor_scroll = seite_oeffnen(page, hurl, timeout_ms, fehler, protokoll,
                                                   f"{name} (Handy)")
                        neu = bilder_machen(page, out, f"handy-{name}", args.max_hoehe, fehler,
                                            (f'{text} Handy (iPhone 13), erster Bildschirm',
                                             f'{text} Handy (iPhone 13), ganze Seite'))
                        bilder += neu
                        if len(neu) < 2:
                            teilfehler.append(f"Handy {hurl}: {2 - len(neu)} von 2 Bildern"
                                              f" nicht erstellt")
                        seitennamen.append(f"{text} (Handy)")
                        mot = page.evaluate(f"() => {{ {JS_BEWEGUNG} }}")
                        mot["scroll_reveal"]["vor_dem_scrollen"] = vor_scroll
                        mot["hinweis"] = "Handy-Emulation, kein Hover gemessen"
                        bewegung[f"handy-{name}"] = mot
                        if name == "start":
                            handylayout = page.evaluate(f"() => {{ {JS_LAYOUT} }}")
                            if layout is not None:
                                layout["handy_navigation"] = handylayout.get("handy_navigation")
                                layout["handy_kopfleiste"] = handylayout.get("kopfleiste")
                                layout["handy_schrift_basis"] = handylayout.get("schrift", {}).get("basis_groesse")
                    except Exception as exc:
                        grund = fehlergrund(exc)
                        fehler.append(f"Handy {hurl}: {grund}")
                        teilfehler.append(f"{text} (Handy) {hurl}: {grund}")
                ctx.close()
        finally:
            browser.close()

    info = {"marke": marke, "url": url, "datum": date.today().isoformat(),
            "browser": browser_name, "seiten": seitennamen or ["keine"]}
    gemessen = bool(layout) or bool(bewegung) or bool(bilder)

    # ---- Totalfehler: keine Ergebnisdateien schreiben, die wie Messwerte aussehen
    if not gemessen:
        entfernt = []
        for name in ("bewegung.json", "layout.json"):
            alt = out / name
            if alt.exists():
                try:
                    alt.unlink()
                    entfernt.append(name)
                except OSError:
                    pass
        fehlbericht_schreiben(out, info, fehler, protokoll, entfernt)
        print("\n0 Bilder, 0 Seiten ausgelesen - es wurde nichts gemessen.", file=sys.stderr)
        print(f"Wahrscheinliche Ursache: {ursache_text(fehler) or UNKLAR}.", file=sys.stderr)
        if fehler:
            for f in list(dict.fromkeys(fehler))[:10]:
                print(f"  {f}", file=sys.stderr)
        if entfernt:
            print("Alte Ergebnisdateien entfernt: " + ", ".join(entfernt), file=sys.stderr)
        print("Keine layout.json und keine bewegung.json geschrieben. Es liegen keine"
              " gemessenen Werte vor -\nfuer das Design die Empfehlungen im Profil verwenden."
              f"\nNotiz: {out / 'zusammenfassung.md'}", file=sys.stderr)
        return EXIT_TOTAL

    # Leere JSON-Dateien waeren kein Ergebnis - nur schreiben, was Werte enthaelt
    dateien = []
    for name, daten in (("bewegung.json", bewegung), ("layout.json", layout)):
        ziel = out / name
        if daten:
            ziel.write_text(json.dumps(daten, indent=2, ensure_ascii=False), encoding="utf-8")
            dateien.append(name)
        elif ziel.exists():
            try:
                ziel.unlink()
                teilfehler.append(f"{name}: nicht gemessen (alte Datei entfernt)")
            except OSError:
                pass
        else:
            teilfehler.append(f"{name}: nicht gemessen, Datei nicht geschrieben")
    bericht_schreiben(out, info, layout, bewegung, bilder, fehler, protokoll, teilfehler)

    print(f"\n{len(bilder)} Bilder, {len(bewegung)} Seiten ausgelesen.")
    for datei, _ in bilder:
        print(f"  {datei}")
    for name in dateien:
        print(f"  {name}")
    print("  zusammenfassung.md")
    if fehler:
        print(f"\n{len(set(fehler))} Fehler (siehe zusammenfassung.md):", file=sys.stderr)
        for f in list(dict.fromkeys(fehler))[:10]:
            print(f"  {f}", file=sys.stderr)
    if teilfehler:
        print(f"\nTeilerfolg: {len(set(teilfehler))} Seite(n)/Bild(er) nicht erfasst:",
              file=sys.stderr)
        for t in list(dict.fromkeys(teilfehler))[:10]:
            print(f"  {t}", file=sys.stderr)
        grund = ursache_text(teilfehler)
        if grund:
            print(f"Wahrscheinliche Ursache: {grund}.", file=sys.stderr)
        print(f"Die erfassten Seiten sind brauchbar. Zusammenfassung lesen:"
              f" {out / 'zusammenfassung.md'}", file=sys.stderr)
        return EXIT_TEILWEISE
    print(f"\nFertig. Zusammenfassung lesen: {out / 'zusammenfassung.md'}")
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
