import glob
import re

for f in sorted(glob.glob('Data-Module-*.html')):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    print(f'=== {f} ===')
    links = re.findall(r'<a href="[^"]+" class="sidebar-content-link">([^<]+)</a>', content)
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', content)
    
    print('Sidebar Links (first 5):', links[:5])
    print('H2 Headings (first 5):', h2s[:5])
    print()
