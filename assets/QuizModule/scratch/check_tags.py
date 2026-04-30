import re

def check_tags(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove script and style content for tag counting
    content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style.*?>.*?</style>', '', content, flags=re.DOTALL)
    
    tags_to_check = ['div', 'main', 'header', 'nav', 'footer', 'aside']
    
    for tag in tags_to_check:
        opens = len(re.findall(rf'<{tag}\b', content, re.IGNORECASE))
        closes = len(re.findall(rf'</{tag}\b', content, re.IGNORECASE))
        print(f"Tag <{tag}>: {opens} open, {closes} close")

if __name__ == "__main__":
    check_tags(r'c:\Users\kj anand\Downloads\Quiz DD\Module-5.html')
