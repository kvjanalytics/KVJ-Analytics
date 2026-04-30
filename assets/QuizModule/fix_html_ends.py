import os

def fix_end(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove literal \n and any extra </body></html>
    content = content.replace('\\\\n', '')
    content = content.replace('\\n', '')
    
    # Ensure it ends cleanly
    content = content.strip()
    if not content.endswith('</html>'):
        content += '\\n</body>\\n</html>'
    
    # Actually, let's just do a clean replace of the footer
    content = content.split('</script>')[0] + '</script>\\n</body>\\n</html>'

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed end of {path}")

fix_end('c:/Users/kj anand/Downloads/Quiz DD/roadmap.html')
fix_end('c:/Users/kj anand/Downloads/Quiz DD/data_roadmap.html')
