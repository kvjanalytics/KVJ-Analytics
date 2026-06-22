from PIL import Image
import os
import shutil

# Paths
brain_dir = r"C:\Users\kj anand\.gemini\antigravity\brain\1b442fb8-cfad-47c4-9d32-7c32b4995ec3"
target_dir = r"c:\Users\kj anand\Downloads\Quiz DD"

table_src = os.path.join(brain_dir, "media__1776161873014.png")
charts_src = os.path.join(brain_dir, "media__1776161994679.png")

# Copy table
shutil.copy(table_src, os.path.join(target_dir, "pd_sales_table_q20.png"))

# Crop charts
img = Image.open(charts_src)
w, h = img.size
qw, qh = w // 2, h // 2

crops = [
    (0, 0, qw, qh, "q20_option_a.png"),
    (qw, 0, w, qh, "q20_option_b.png"),
    (0, qh, qw, h, "q20_option_c.png"),
    (qw, qh, w, h, "q20_option_d.png")
]

for x1, y1, x2, y2, name in crops:
    crop = img.crop((x1, y1, x2, y2))
    crop.save(os.path.join(target_dir, name))
    print(f"Saved {name}")
