"""Render the catalog page from the extracted brand profiles.

Usage: python3 -I build_catalog.py <profiles_json> <template_html> <out_html> <skill_name>
"""
import json
import pathlib
import sys

profiles = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
tpl = pathlib.Path(sys.argv[2]).read_text(encoding="utf-8")
out = pathlib.Path(sys.argv[3])
name = sys.argv[4]

keys = ["slug", "name", "cat", "blurb", "mode", "light", "dark", "inkLight", "inkDark", "primary",
        "onPrimary", "ghost", "radius", "swatches", "font", "generic", "weight", "tracking", "upper"]
data = [{k: p[k] for k in keys} for p in profiles]
payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

assert tpl.count("/*DATA*/[]") == 1
html = tpl.replace("/*DATA*/[]", payload).replace("__CMD__", name)
out.write_text(html, encoding="utf-8")
print(f"{out}: {len(data)} designs, {len(html.encode()) // 1024} KB")

# Standalone copy for opening locally (the artifact host adds this skeleton itself).
if len(sys.argv) > 5:
    standalone = pathlib.Path(sys.argv[5])
    standalone.write_text(
        '<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<style>:root{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
        '</head>\n<body>\n' + html + '\n</body>\n</html>\n', encoding="utf-8")
    print(f"{standalone}: standalone copy")
