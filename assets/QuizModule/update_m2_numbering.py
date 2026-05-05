import re

def update_module_2():
    with open('Data-Module-2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Change h2 to h3 for 2.X.Y sub-sections
    # Match <h2 ...>2.X.Y ...</h2>
    content = re.sub(
        r'<h2([^>]*)>(2\.\d+\.\d+\s+.*?)</h2>',
        r'<h3\1>\2</h3>',
        content,
        flags=re.IGNORECASE
    )
    
    # Fix 2. Grouping (COUNT) to 2.5.1
    content = content.replace('<h3>2. Grouping (COUNT)</h3>', '<h3>2.5.1 Grouping (COUNT)</h3>')

    with open('Data-Module-2.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated Data-Module-2.html header levels and numbering")

update_module_2()
