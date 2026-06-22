from PIL import Image
import os

def crop_ice_cream_chart():
    img_path = r"C:\Users\kj anand\.gemini\antigravity\brain\9f3730f5-ca81-43c4-8845-03df554b14dc\media__1779780737420.png"
    output_path = r"C:\Users\kj anand\Downloads\Quiz DD (13) 6\Quiz DD\q28_ice_cream.png"
    
    with Image.open(img_path) as img:
        # Based on visual inspection, the pie chart and legend are in the center.
        # The prompt text at the top should be removed.
        # Width: approx 1000, Height: approx 750
        # Let's crop from top=150 to bottom=720, and trim sides.
        left = 50
        top = 200
        right = 950
        bottom = 720
        
        cropped = img.crop((left, top, right, bottom))
        
        # Trim white space
        from PIL import ImageChops
        bg = Image.new(cropped.mode, cropped.size, cropped.getpixel((0,0)))
        diff = ImageChops.difference(cropped, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
            cropped = cropped.crop(bbox)
            
        cropped.save(output_path)
        print(f"Saved cropped image to {output_path}")

if __name__ == "__main__":
    crop_ice_cream_chart()
