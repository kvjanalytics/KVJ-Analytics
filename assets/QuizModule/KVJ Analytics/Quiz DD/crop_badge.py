from PIL import Image

def crop_to_square(image_path, output_path):
    img = Image.open(image_path)
    width, height = img.size
    new_size = min(width, height)
    left = (width - new_size) / 2
    top = (height - new_size) / 2
    right = (width + new_size) / 2
    bottom = (height + new_size) / 2
    
    img_cropped = img.crop((left, top, right, bottom))
    img_cropped.save(output_path, "PNG")

crop_to_square("d2a1327f-1e69-46e6-9efd-b54d0086d85c.jpg", "pearson_python_badge_proper.png")
print("Cropped Python badge to a perfect square.")
