import jsbeautifier
import os

file_path = 'Data-Module-3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the script content
script_pattern = r'<script>(.*?)</script>'
scripts = re.findall(script_pattern, content, re.DOTALL)

for i, script in enumerate(scripts):
    try:
        # Just try to parse it or something
        # Or better, just print the length and a snippet
        print(f"Script {i} length: {len(script)}")
    except Exception as e:
        print(f"Error in script {i}: {e}")

# Let's try to find potential syntax errors by running it through a simple parser
# Or just look for missing braces.
