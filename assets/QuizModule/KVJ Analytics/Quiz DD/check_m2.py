import re
with open('Data-Module-2.html', 'r', encoding='utf-8') as f:
    text = f.read()

links = re.findall(r'<a href="Data-Module-2\.html#s[^"]+" class="sidebar-content-link">([^<]+)</a>', text)
print("Sidebar Links:", links)

h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', text)
print("H2s:", h2s)
