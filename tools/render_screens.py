"""Musterscreens rendern: Icons einsetzen, Basis-CSS einfügen, prüfen und als PNG fotografieren.

Aufruf (aus dem Arbeitsordner):
  python3 -I render_screens.py <slug|datei.html> [...] [--src work/mock] [--profiles work/sprache]
                               [--out work/out] [--icons DIR] [--scale 1] [--no-png]

Eingabe: HTML mit <main class="stage"> und drei <section class="phone"> (siehe screens/ANLEITUNG.md).
Icons als <i data-icon="lucide:house"></i> oder <i data-icon="ph-bold:house"></i>
(Phosphor-Stärken: ph-thin, ph-light, ph-regular, ph-bold, ph-fill, ph-duotone).
Ausgabe: <out>/<slug>.html (eigenständig, ohne externe Dateien) und <out>/<slug>.png.
Bereits gerenderte Dateien können erneut gerendert werden (Basis-CSS wird ersetzt).

Icon-Sammlungen (Lucide, ISC; Phosphor, MIT) werden in --icons erwartet:
  git clone --depth 1 https://github.com/lucide-icons/lucide <DIR>/lucide
  git clone --depth 1 https://github.com/phosphor-icons/core <DIR>/phosphor
Braucht Python 3 und Playwright (pip install playwright; playwright install chromium).
"""
import argparse
import contextlib
import fcntl
import html
import pathlib
import re
import sys
import tempfile
import urllib.parse

HERE = pathlib.Path(__file__).resolve().parent
BASE_CSS = HERE / "screens" / "base.css"
SCENES = HERE / "screens" / "scenes"

ANSAETZE = {
    "buehne": "Große Bühne", "regale": "Medien-Regale", "galerie": "Bild-Karten",
    "werkzeug": "Präzises Werkzeug", "editorial": "Editorial", "daten": "Daten und Zahlen",
    "verspielt": "Verspielt", "plakativ": "Plakativ", "minimal": "Stilles Minimal",
    "leuchten": "Verlauf und Leuchten", "retro": "Retro",
}
PH_WEIGHTS = {"ph-thin": "thin", "ph-light": "light", "ph-regular": "regular",
              "ph-bold": "bold", "ph-fill": "fill", "ph-duotone": "duotone"}
ICON_RE = re.compile(r'<i\b([^>]*?)\bdata-icon\s*=\s*"([^"]+)"([^>]*)>\s*</i>', re.S)
ATTR_RE = re.compile(r'([\w:-]+)\s*=\s*"([^"]*)"')
EXTERNAL_RE = re.compile(r'''(?:\b(?:src|href)\s*=\s*["']?\s*(?:https?:)?//|url\(\s*["']?\s*(?:https?:)?//|@import)''', re.I)


def front_matter(path):
    data = {}
    if path and path.exists():
        m = re.match(r"---\n(.*?)\n---", path.read_text(encoding="utf-8"), re.S)
        if m:
            for line in m.group(1).splitlines():
                k, sep, v = line.partition(":")
                if sep:
                    data[k.strip()] = v.strip()
    return data


def scene_uri(name):
    svg = (SCENES / f"{name}.svg").read_text(encoding="utf-8")
    svg = re.sub(r">\s+<", "><", re.sub(r"\s+", " ", svg)).strip().replace('"', "'")
    return "data:image/svg+xml," + urllib.parse.quote(svg, safe=" '/:=,.-()")


def base_css():
    css = BASE_CSS.read_text(encoding="utf-8")
    return re.sub(r"\{\{scene:([\w-]+)\}\}", lambda m: scene_uri(m.group(1)), css)


class Icons:
    def __init__(self, root):
        self.root = root
        self.cache = {}
        self.missing = set()
        self.used = set()

    def load(self, spec):
        if spec in self.cache:
            return self.cache[spec]
        kind, _, name = spec.partition(":")
        result = None
        if kind == "lucide":
            p = self.root / "lucide" / "icons" / f"{name}.svg"
            attrs = ('viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
                     'stroke-linecap="round" stroke-linejoin="round"')
            cls = "ic ic-l"
        elif kind in PH_WEIGHTS:
            w = PH_WEIGHTS[kind]
            p = self.root / "phosphor" / "assets" / w / (f"{name}.svg" if w == "regular" else f"{name}-{w}.svg")
            attrs = 'viewBox="0 0 256 256" fill="currentColor"'
            cls = f"ic ic-p ic-{kind}"
        else:
            p = None
        if p is not None and p.exists():
            inner = re.search(r"<svg[^>]*>(.*)</svg>", p.read_text(encoding="utf-8"), re.S).group(1)
            result = (attrs, cls, re.sub(r">\s+<", "><", re.sub(r"\s+", " ", inner)).strip())
        self.cache[spec] = result
        return result

    def replace(self, m):
        spec = m.group(2).strip()
        extra = dict(ATTR_RE.findall(m.group(1) + " " + m.group(3)))
        extra.pop("data-icon", None)
        icon = self.load(spec)
        if icon is None:
            self.missing.add(spec)
            return ('<svg class="ic ic-missing" viewBox="0 0 24 24" aria-hidden="true">'
                    '<rect width="24" height="24" fill="red" opacity=".45"/></svg>')
        self.used.add(spec)
        attrs, cls, inner = icon
        cls = (cls + " " + extra.pop("class", "")).strip()
        rest = "".join(f' {k}="{html.escape(v, quote=True)}"' for k, v in extra.items())
        return f'<svg class="{cls}" {attrs} aria-hidden="true" data-i="{spec}"{rest}>{inner}</svg>'


def process(src_text, slug, meta, icons):
    problems = []
    text = ICON_RE.sub(icons.replace, src_text)
    text = re.sub(r'<style id="ms-base">.*?</style>\s*', "", text, flags=re.S)
    style = f'<style id="ms-base">\n{base_css()}\n</style>\n'
    if re.search(r"<head[^>]*>", text):
        text = re.sub(r"(<head[^>]*>\s*(?:<meta charset[^>]*>\s*)?)", lambda m: m.group(1) + style, text, count=1)
    else:
        problems.append("kein <head>")
    if 'class="ms-wrap"' not in text:
        start = text.find('<main class="stage"')
        end = text.rfind("</main>")
        if start < 0 or end < 0:
            problems.append('kein <main class="stage">…</main>')
        else:
            marke = meta.get("marke", slug)
            ansatz = " + ".join(ANSAETZE.get(k, k) for k in (meta.get("ansatz", "?"), meta.get("ansatz2", "")) if k)
            foot = (f'<footer class="ms-foot"><b>{html.escape(marke)}-Stil</b> · Ansatz: {html.escape(ansatz)} · '
                    'eigene Musterscreens mit Beispielinhalten, keine Originalscreens der Marke</footer>')
            end += len("</main>")
            text = text[:start] + '<div class="ms-wrap">' + text[start:end] + foot + "</div>" + text[end:]
    if len(re.findall(r'<section class="phone\b', text)) != 3:
        problems.append('nicht genau drei <section class="phone">')
    if EXTERNAL_RE.search(text):
        problems.append("externe Adresse gefunden (nur lokale Inhalte erlaubt)")
    if re.search(r"<script\b", text, re.I):
        problems.append("<script> ist nicht erlaubt")
    if re.search(r"<img\b", text, re.I):
        problems.append("<img> ist nicht erlaubt (Bilder nur über .scene-*)")
    if "prefers-reduced-motion" not in text and re.search(r"@keyframes|animation\s*:", text):
        problems.append("Animationen nicht in @media (prefers-reduced-motion: no-preference) gekapselt")
    return text, problems


@contextlib.contextmanager
def render_lock():
    with open(pathlib.Path(tempfile.gettempdir()) / "render_screens.lock", "w") as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)


FONT_PROBE = r"""
() => {
  const out = [];
  for (const ph of document.querySelectorAll('.phone')) {
    const pr = ph.getBoundingClientRect();
    const res = {id: ph.id, w: Math.round(pr.width), h: Math.round(pr.height), overflow: [], clipped: []};
    const label = el => (el.id ? '#' + el.id : '') + (typeof el.className === 'string' && el.className ? '.' + el.className.trim().split(/\s+/).join('.') : (el.className && el.className.baseVal ? '.' + el.className.baseVal.trim().split(/\s+/).join('.') : '')) || el.tagName.toLowerCase();
    const clippedByAncestor = el => {
      for (let a = el.parentElement; a && a !== ph; a = a.parentElement) {
        const cs = getComputedStyle(a);
        if (cs.overflowX !== 'visible' || a.classList.contains('row-x')) return true;
      }
      return false;
    };
    for (const el of ph.querySelectorAll('*')) {
      const r = el.getBoundingClientRect();
      if (!r.width || !r.height || el.classList.contains('hi')) continue;
      if ((r.right > pr.right + 0.5 || r.left < pr.left - 0.5) && !clippedByAncestor(el) && r.top < pr.bottom)
        res.overflow.push(label(el) + ' (x ' + Math.round(r.left - pr.left) + '…' + Math.round(r.right - pr.left) + ')');
      const cs = getComputedStyle(el);
      const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
      if (hasText && cs.overflow !== 'visible' && cs.textOverflow !== 'ellipsis' && cs.webkitLineClamp === 'none'
          && (el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1) && r.top < pr.bottom)
        res.clipped.push(label(el) + ': "' + el.textContent.trim().slice(0, 40) + '"');
    }
    res.overflow = res.overflow.slice(0, 8); res.clipped = res.clipped.slice(0, 8);
    out.push(res);
  }
  return out;
}
"""


def shoot(pairs, scale, qa=False):
    from playwright.sync_api import sync_playwright
    report = {}
    with render_lock(), sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width": 1400, "height": 1000}, device_scale_factor=scale,
                                  reduced_motion="reduce")
        for html_path, png_path in pairs:
            page = ctx.new_page()
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.goto(html_path.resolve().as_uri())
            page.evaluate("document.fonts.ready.then(() => true)")
            page.wait_for_timeout(120)
            phones = page.evaluate(FONT_PROBE)
            cdp = ctx.new_cdp_session(page)
            cdp.send("DOM.enable")
            cdp.send("CSS.enable")
            root = cdp.send("DOM.getDocument", {"depth": -1})["root"]["nodeId"]
            ids = cdp.send("DOM.querySelectorAll", {"nodeId": root, "selector": ".phone *"})["nodeIds"]
            fonts = {}
            for nid in ids[:700]:
                try:
                    for f in cdp.send("CSS.getPlatformFontsForNode", {"nodeId": nid})["fonts"]:
                        fonts[f["familyName"]] = fonts.get(f["familyName"], 0) + f["glyphCount"]
                except Exception:
                    pass
            page.locator(".ms-wrap").screenshot(path=str(png_path))
            if qa:
                qdir = png_path.parent / "qa"
                qdir.mkdir(exist_ok=True)
                page.add_style_tag(content=".ms-wrap{filter:grayscale(1)}")
                page.locator(".ms-wrap").screenshot(path=str(qdir / f"{html_path.stem}-grau.png"))
                page.add_style_tag(content=".ms-wrap{filter:none}")
                big = ctx.browser.new_context(viewport={"width": 1400, "height": 1000}, device_scale_factor=2,
                                              reduced_motion="reduce")
                bp = big.new_page()
                bp.goto(html_path.resolve().as_uri())
                bp.evaluate("document.fonts.ready.then(() => true)")
                bp.wait_for_timeout(120)
                for i, ph in enumerate(bp.locator(".phone").all()):
                    ph.screenshot(path=str(qdir / f"{html_path.stem}-{i + 1}@2x.png"))
                big.close()
            report[html_path.stem] = {"phones": phones, "fonts": fonts, "errors": errors}
            page.close()
        browser.close()
    return report


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("items", nargs="+")
    ap.add_argument("--src", default="work/mock")
    ap.add_argument("--profiles", default="work/sprache")
    ap.add_argument("--out", default="work/out")
    ap.add_argument("--icons", default="/home/claude/src/icons")
    ap.add_argument("--scale", type=float, default=1)
    ap.add_argument("--no-png", action="store_true")
    ap.add_argument("--qa", action="store_true",
                    help="zusätzlich <out>/qa/<slug>-grau.png und je Phone eine 2x-Aufnahme <slug>-N@2x.png")
    a = ap.parse_args()
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    icons = Icons(pathlib.Path(a.icons))
    if not (icons.root / "lucide" / "icons").is_dir() or not (icons.root / "phosphor" / "assets").is_dir():
        sys.exit(f"Icon-Sammlungen fehlen in {icons.root} (siehe Hilfe: --help)")
    pairs, ok = [], True
    for item in a.items:
        src = pathlib.Path(item) if item.endswith(".html") else pathlib.Path(a.src) / f"{item}.html"
        slug = src.stem
        meta = front_matter(pathlib.Path(a.profiles) / f"{slug}.md")
        icons.missing.clear()
        text, problems = process(src.read_text(encoding="utf-8"), slug, meta, icons)
        if icons.missing:
            problems.append("fehlende Icons: " + ", ".join(sorted(icons.missing)))
        if not meta:
            problems.append(f"kein Profil mit Kopfdaten in {a.profiles}/{slug}.md (Fußzeile unvollständig)")
        dst = out / f"{slug}.html"
        dst.write_text(text, encoding="utf-8")
        print(f"{slug}: {dst} ({len(text) // 1024} KB)")
        for pr in problems:
            print(f"  PROBLEM: {pr}")
            ok = False
        pairs.append((dst, out / f"{slug}.png"))
    if not a.no_png:
        for slug, r in shoot(pairs, a.scale, a.qa).items():
            sizes = ", ".join(f"{ph['id'] or '?'} {ph['w']}×{ph['h']}" for ph in r["phones"])
            fonts = ", ".join(f"{k} ({v})" for k, v in sorted(r["fonts"].items(), key=lambda kv: -kv[1]))
            print(f"{slug}: PNG {out / (slug + '.png')} | Phones: {sizes}\n  Schriften gerendert: {fonts}")
            if any((ph["w"], ph["h"]) != (390, 844) for ph in r["phones"]):
                print("  PROBLEM: Phone-Größe muss 390×844 sein")
                ok = False
            for e in r["errors"]:
                print(f"  PROBLEM (Seite): {e}")
                ok = False
            for ph in r["phones"]:
                for o in ph["overflow"]:
                    print(f"  HINWEIS {ph['id']}: ragt seitlich aus dem Phone: {o}")
                for c in ph["clipped"]:
                    print(f"  HINWEIS {ph['id']}: Text abgeschnitten: {c}")
            if a.qa:
                print(f"  QA-Bilder: {out / 'qa'}/{slug}-grau.png, {slug}-1@2x.png … {slug}-3@2x.png")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
