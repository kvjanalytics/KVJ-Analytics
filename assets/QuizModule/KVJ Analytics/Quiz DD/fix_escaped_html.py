import os

def fix_roadmap(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the double escaping of quotes in onclick
    # Find onclick=\"checkMockCode('PYMOCK1', 'module_quiz.html?mock=1')\"
    content = content.replace('onclick=\\"', 'onclick="')
    content = content.replace(')\\"', ')"')
    
    # Also fix if there are any other escaped quotes
    content = content.replace('\\\'', "'")
    
    # Fix the double script URL issue if it happened
    content = content.replace('const scriptURL = "https://script.google.com/macros/s/AKfycbw9mb2dsJ1SSheOcpdcdeE8eKNnuCjK2U9U9kIeHV_2yga8Ujiee1w_huTzc2w5BpWD/exec";', '')
    # Put it back cleanly once in the script block
    if '<script>' in content and 'const scriptURL' not in content:
        content = content.replace('<script>', '<script>\n        const scriptURL = "https://script.google.com/macros/s/AKfycbw9mb2dsJ1SSheOcpdcdeE8eKNnuCjK2U9U9kIeHV_2yga8Ujiee1w_huTzc2w5BpWD/exec";')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed {path}")

fix_roadmap('c:/Users/kj anand/Downloads/Quiz DD/roadmap.html')
fix_roadmap('c:/Users/kj anand/Downloads/Quiz DD/data_roadmap.html')
