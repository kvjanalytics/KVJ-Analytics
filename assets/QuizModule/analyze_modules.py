import re

# Analyze each module HTML for image references and sections
modules_html = {
    1: 'Module-1.html',
    2: 'Module-2.html',
    3: 'Module-3.html',
    4: 'Module-4.html',
}

# Read docx structure
with open('docx_structure.txt', 'r', encoding='utf-8') as f:
    docx_lines = f.readlines()

# Module boundaries in docx (line indices, 0-based)
docx_modules = {
    1: (0, 675),
    2: (675, 923),
    3: (923, 1205),
    4: (1205, 1547),
}

print("=== DOCX Image counts per Module ===")
for mod_num, (start, end) in docx_modules.items():
    mod_lines = docx_lines[start:end]
    images = [l.strip() for l in mod_lines if l.strip().startswith('[IMAGE:')]
    print(f"Module {mod_num}: {len(images)} images in docx")

print()
print("=== HTML Image counts per Module ===")
for mod_num, fname in modules_html.items():
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
        print(f"Module {mod_num} ({fname}): {len(imgs)} img tags")
        for img in imgs[:5]:
            print(f"  {img}")
    except Exception as e:
        print(f"Error reading {fname}: {e}")

print()
print("=== Module 1 HTML headings ===")
with open('Module-1.html', 'r', encoding='utf-8') as f:
    content = f.read()
headings = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', content, re.DOTALL)
for h in headings[:60]:
    clean = re.sub(r'<[^>]+>', '', h).strip()
    if clean:
        print(clean[:100])
