import os

def fix_double_href(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace <a href="javascript:void(0)" href=" with <a href="
    content = content.replace('<a href="javascript:void(0)" href="', '<a href="')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed double href in {path}")

fix_double_href('c:/Users/kj anand/Downloads/Quiz DD/roadmap.html')
fix_double_href('c:/Users/kj anand/Downloads/Quiz DD/data_roadmap.html')
