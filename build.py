# -*- coding: utf-8 -*-
"""拼接 parts/*.html -> index.html（照片走 img/ 外链，不内嵌）"""
import os, glob

BASE = r"D:\hermer\love-site"
PARTS = sorted(glob.glob(os.path.join(BASE, "parts", "*.html")))
html = "".join(open(p, encoding="utf-8").read() for p in PARTS)

# 占位符 __IMG1__..__IMG7__ -> img/N.jpg（相对路径，GitHub Pages / Vercel 通用）
for i in range(1, 8):
    ph = f"__IMG{i}__"
    assert ph in html, f"占位符缺失: {ph}"
    html = html.replace(ph, f"img/{i}.jpg")

out = os.path.join(BASE, "index.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
print(f"OK -> {out}, {os.path.getsize(out)//1024} KB, 剩余占位符={html.count('__IMG')}")
