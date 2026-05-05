import glob
import re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to replace window.location.href = '...' inside function logout()
    # Let's find function logout() block
    if 'function logout()' in content:
        # It's safer to just look for the function block and do a replacement inside it
        def replace_href(match):
            block = match.group(0)
            new_block = re.sub(r'window\.location\.href\s*=\s*[\'"].*?[\'"]\s*;', "window.location.href = 'https://www.kvjanalytics.in/training.html';", block)
            return new_block
        
        new_content = re.sub(r'function\s+logout\(\)\s*\{.*?\}', replace_href, content, flags=re.DOTALL)
        
        if content != new_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated {f}")
