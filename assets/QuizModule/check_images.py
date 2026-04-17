from PIL import Image
import os

def check_images():
    paths = [
        r"C:\Users\kj anand\.gemini\antigravity\brain\1b442fb8-cfad-47c4-9d32-7c32b4995ec3\media__1776161873014.png",
        r"C:\Users\kj anand\.gemini\antigravity\brain\1b442fb8-cfad-47c4-9d32-7c32b4995ec3\media__1776161994679.png"
    ]
    for p in paths:
        if os.path.exists(p):
            img = Image.open(p)
            print(f"{os.path.basename(p)}: {img.size}")
        else:
            print(f"{os.path.basename(p)}: MISSING")

if __name__ == "__main__":
    check_images()
