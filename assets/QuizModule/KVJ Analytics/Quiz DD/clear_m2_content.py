import re

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\Data-Module-2.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'(<main class="main-content">).*?(</main>)', re.DOTALL)

new_content = pattern.sub(r'\1\n            <div class="section-header">\n                <h2>New Content Coming Soon</h2>\n            </div>\n            <p>Please provide the new content for this module, and I will integrate it into this premium layout for you.</p>\n        \2', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully cleared content.")
