# -*- coding: utf-8 -*-
"""压缩照片 -> base64 -> 生成 images.json，供 HTML 模板拼接"""
import os, base64, json, io
from PIL import Image

SRC = r"C:\Users\28215\.hermes-web-ui\upload\default"
OUT_DIR = r"D:\hermer\love-site"
os.makedirs(OUT_DIR, exist_ok=True)

# 照片叙事顺序：1封面色/开场 -> 2-3 日常 -> 4-5 特别时刻 -> 6-7 未来
FILES = [
    ("a048532f438b5c2f.jpg", "img1"),
    ("3ff09604d9cd1ae5.jpg", "img2"),
    ("ebf35d80c9cd1dcc.jpeg", "img3"),
    ("1f830ff005d6780b.jpeg", "img4"),
    ("897c2e4742f6abaf.jpeg", "img5"),
    ("e65f22a6124fd26f.jpeg", "img6"),
    ("e905738a105ad2cd.jpeg", "img7"),
]

result = {}
for fname, key in FILES:
    path = os.path.join(SRC, fname)
    im = Image.open(path).convert("RGB")
    # 统一缩到宽度 1000px 内（竖图高约 1333，手机/桌面都够）
    if im.width > 1000:
        h = int(im.height * 1000 / im.width)
        im = im.resize((1000, h), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=80, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode()
    result[key] = "data:image/jpeg;base64," + b64
    print(f"{key}: {im.size} -> {len(b64)//1024} KB(base64)")

with open(os.path.join(OUT_DIR, "images.json"), "w", encoding="utf-8") as f:
    json.dump(result, f)
print("OK -> images.json, total", sum(len(v) for v in result.values()) // 1024, "KB")
