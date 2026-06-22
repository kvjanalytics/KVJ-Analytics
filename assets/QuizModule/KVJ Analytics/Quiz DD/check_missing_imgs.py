import re, os

files = ['data_quiz_data.js', 'quiz_data.js']

for fname in files:
    print(f"\n=== {fname} — optionImages ===")
    with open(fname, encoding='utf-8', errors='ignore') as f:
        js = f.read()
    # Match all strings inside optionImages arrays
    blocks = re.findall(r'optionImages\s*:\s*\[([^\]]+)\]', js, re.DOTALL)
    imgs = []
    for block in blocks:
        imgs += re.findall(r'"([^"]+\.png)"', block)
        imgs += re.findall(r"'([^']+\.png)'", block)
    imgs = sorted(set(imgs))
    missing = []
    for img in imgs:
        if img.startswith('data:'):
            continue
        if os.path.exists(img):
            print(f"  OK      {img}")
        else:
            print(f"  MISSING {img}")
            missing.append(img)
    print(f"\n  Total optionImages: {len(imgs)}, Missing: {len(missing)}")
