from PIL import Image
from collections import Counter

def get_major_colors(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = list(img.getdata())
    # Filter out white and very light colors
    pixels = [p for p in pixels if sum(p) < 700 and sum(p) > 50]
    counts = Counter(pixels)
    for color, count in counts.most_common(5):
        print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}: {count}")

print("Colors from pearson_badge.png:")
get_major_colors("pearson_badge.png")
