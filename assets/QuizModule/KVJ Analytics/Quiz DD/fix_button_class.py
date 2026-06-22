import os
import re

target_dir = r"C:\Users\kj anand\Downloads\Quiz DD"
modules = [f"Module-{i}.html" for i in range(1, 7)]

for mod in modules:
    filepath = os.path.join(target_dir, mod)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The issue: CSS has `.btn-quiz-start` but HTML has `class="btn-start-quiz"`
    content = content.replace(".btn-quiz-start {", ".btn-start-quiz {")
    content = content.replace(".btn-quiz-start:hover {", ".btn-start-quiz:hover {")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed quiz button class for {mod}")
