import glob
import re

for filepath in glob.glob('Data-Module-*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig_content = content
    
    # Fix Module 1 links
    content = re.sub(r'(<a href="Data-Module-1\.html#s[^"]*" class="sidebar-content-link">)(\d+)\.\s', r'\g<1>1.\g<2> ', content)
    
    # Fix Module 2 links
    content = re.sub(r'(<a href="Data-Module-2\.html#s[^"]*" class="sidebar-content-link">)(\d+)\.\s', r'\g<1>2.\g<2> ', content)
    
    # Fix Module 3 links (Only the first one)
    content = re.sub(r'(<a href="Data-Module-3\.html#s1-analysis" class="sidebar-content-link">)1\. Data Analysis', r'\g<1>3.0 Data Analysis', content)

    if content != orig_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated sidebar in {filepath}")
    else:
        print(f"No changes needed for {filepath}")
