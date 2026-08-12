# -*- coding: utf-8 -*-
"""拼接 parts/*.html + images.json -> index.html"""
import json, os, glob

BASE = r"D:\hermer\love-site"
PARTS = sorted(glob.glob(os.path.join(BASE, "parts", "*.html")))
html = "".join(open(p, encoding="utf-8").read() for p in PARTS)

with open(os.path.join(BASE, "images.json"), encoding="utf-8") as f:
    imgs = json.load(f)
for key, data in imgs.items():
    ph = f"__IMG{key[3:]}__"
    assert ph in html, f"占位符缺失: {ph}"
    html = html.replace(ph, data)

out = os.path.join(BASE, "index.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
print(f"OK -> {out}, {os.path.getsize(out)//1024} KB, parts={len(PARTS)}, 剩余占位符={html.count('__IMG')}, main标签={html.count('<main>')}")
