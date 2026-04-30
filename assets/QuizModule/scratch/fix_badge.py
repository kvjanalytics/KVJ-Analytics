from PIL import Image, ImageDraw

def fix_badge(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    
    # Get bounding box of the badge content (non-white pixels)
    min_x, min_y, max_x, max_y = width, height, 0, 0
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            # If not white/transparent
            if pixel[0] < 252 or pixel[1] < 252 or pixel[2] < 252:
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)
    
    # Add a tiny margin around the detected badge
    padding = 2
    min_x = max(0, min_x - padding)
    min_y = max(0, min_y - padding)
    max_x = min(width, max_x + padding)
    max_y = min(height, max_y + padding)
    
    badge = img.crop((min_x, min_y, max_x, max_y))
    
    # Find the target square size (max dimension)
    size = max(badge.width, badge.height)
    
    # Create the square canvas with white background
    canvas = Image.new("RGBA", (size, size), (255, 255, 255, 255))
    
    # Paste badge in center
    offset_x = (size - badge.width) // 2
    offset_y = (size - badge.height) // 2
    canvas.paste(badge, (offset_x, offset_y), badge)
    
    # Create the high-quality circular mask
    scale = 4
    mask_size = size * scale
    mask = Image.new("L", (mask_size, mask_size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, mask_size, mask_size), fill=255)
    
    # Downsample mask for anti-aliasing
    mask = mask.resize((size, size), Image.Resampling.LANCZOS)
    
    # Apply mask
    canvas.putalpha(mask)
    
    # Save as the final badge
    canvas.save(output_path, "PNG")

if __name__ == "__main__":
    fix_badge("pearson_python_badge_proper.png", "pearson_python_badge_transparent.png")
    print("Badge fixed to perfect circle.")
