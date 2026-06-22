import glob
import re

for filepath in glob.glob('Data-Module-*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig_content = content

    # Replace 3.0 with 3. in the text
    content = content.replace('>3.0 Data Analysis<', '>3. Data Analysis<')

    # If it's module 3, replace h2 with h3 for 3.1, 3.2, etc.
    if 'Data-Module-3.html' in filepath:
        content = re.sub(r'<h2([^>]*)>(3\.[1-9]\d*.*?)</h2>', r'<h3\1>\2</h3>', content)

    if content != orig_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes needed for {filepath}")
