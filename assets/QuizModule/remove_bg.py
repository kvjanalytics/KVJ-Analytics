from PIL import Image, ImageDraw

def remove_background(image_path, output_path):
    # Open the image and ensure it has an alpha channel
    img = Image.open(image_path).convert("RGBA")
    width, height = img.size
    
    # Create a circular mask
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    
    # Draw a white circle on the black mask
    # We leave a tiny margin to avoid any edge artifacts
    margin = 5
    draw.ellipse((margin, margin, width - margin, height - margin), fill=255)
    
    # Apply mask as alpha channel
    result = img.copy()
    result.putalpha(mask)
    
    # Optional: Make specifically white pixels transparent outside the badge if mask isn't enough
    # But for a circular badge, the mask is usually much cleaner.
    
    result.save(output_path, "PNG")

remove_background("pearson_python_badge_proper.png", "pearson_python_badge_transparent.png")
print("Removed white background and created a transparent circular badge.")
