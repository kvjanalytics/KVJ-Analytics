import os
import re

files = [
    r'c:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html',
    r'c:\Users\kj anand\Downloads\Quiz DD\Data-Module-2.html',
    r'c:\Users\kj anand\Downloads\Quiz DD\Data-Module-3.html',
    r'c:\Users\kj anand\Downloads\Quiz DD\Data-Module-4.html'
]

for file_path in files:
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generic pattern to find the banner div
    # It usually has "Ready for the Module X Assessment?" and "START FINAL ASSESSMENT"
    # We'll search for the div that contains these strings.
    
    # We find the start of a div that eventually contains the target text.
    # This is tricky with regex in HTML.
    
    # Let's try to find the specific heading and then go outwards to the parent div.
    # Or just use the fact that they all have a similar structure: a div with style and a heading.
    
    # Module 1 & 2 often have: <div style="margin-top: 100px; padding: 60px; background: linear-gradient...
    # Module 3 has: <div class="quiz-cta" style="margin-top: 100px; ...
    # Module 4 has: <div class="conclusion-box" ...
    
    # Let's use a very broad pattern for the banner.
    pattern = r'<(div|section)[^>]*?>\s*?.*?Ready for the Module \d Assessment?.*?START FINAL ASSESSMENT.*?</\1>'
    
    new_content = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Also clean up the comments around it if they exist
    comments = [
        r'<!-- Final Assessment CTA Banner -->',
        r'<!-- Module \d Assessment CTA -->',
        r'<!-- Conclusion Box -->'
    ]
    for c in comments:
        new_content = re.sub(c, '', new_content, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned banner from {os.path.basename(file_path)}")
    else:
        print(f"No banner found in {os.path.basename(file_path)}")
