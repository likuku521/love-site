# -*- coding: utf-8 -*-
"""压缩照片 -> img/ 目录（外链文件，不再 base64 内嵌）"""
import os
from PIL import Image

SRC = r"C:\Users\28215\.hermes-web-ui\upload\default"
OUT_DIR = r"D:\hermer\love-site\img"
os.makedirs(OUT_DIR, exist_ok=True)

# 照片叙事顺序（与之前一致）
FILES = [
    ("a048532f438b5c2f.jpg", "1.jpg"),
    ("3ff09604d9cd1ae5.jpg", "2.jpg"),
    ("ebf35d80c9cd1dcc.jpeg", "3.jpg"),
    ("1f830ff005d6780b.jpeg", "4.jpg"),
    ("897c2e4742f6abaf.jpeg", "5.jpg"),
    ("e65f22a6124fd26f.jpeg", "6.jpg"),
    ("e905738a105ad2cd.jpeg", "7.jpg"),
]

total = 0
for fname, out_name in FILES:
    im = Image.open(os.path.join(SRC, fname)).convert("RGB")
    # 手机优先：宽度压到 800px（2x 屏足够清晰，体积减半）
    if im.width > 800:
        h = int(im.height * 800 / im.width)
        im = im.resize((800, h), Image.LANCZOS)
    im.save(os.path.join(OUT_DIR, out_name), "JPEG", quality=78, optimize=True)
    size = os.path.getsize(os.path.join(OUT_DIR, out_name))
    total += size
    print(f"{out_name}: {im.size} -> {size//1024} KB")
print(f"总计 {total//1024} KB")
