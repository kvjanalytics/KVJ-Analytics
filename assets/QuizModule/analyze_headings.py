import re

def analyze_headings():
    file_path = 'Data-Module-4.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    headings = []
    for i, line in enumerate(lines):
        # Look for h1-h6
        match = re.search(r'<(h[1-6]).*?>(.*?)</\1>', line, re.IGNORECASE)
        if match:
            tag = match.group(1).lower()
            text = match.group(2).strip()
            # Clean HTML tags from text
            text = re.sub(r'<.*?>', '', text)
            headings.append({
                'line': i + 1,
                'tag': tag,
                'text': text
            })

    for h in headings:
        print(f"L{h['line']}: {h['tag']} - {h['text']}")

analyze_headings()
