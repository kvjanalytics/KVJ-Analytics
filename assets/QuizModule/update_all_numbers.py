import re
import glob

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig_content = content
    if 'Data-Module-1.html' in filepath:
        content = orig_content
        # Replace sidebar links: >1. Data -> >1.1 Data
        content = re.sub(r'(<a href="Data-Module-1\.html#s\d+[^"]*" class="sidebar-content-link">)(\d+)\.\s', r'\g<1>1.\g<2> ', content)
        # Replace H2 tags: <h2>1. Data -> <h2>1.1 Data
        content = re.sub(r'(<h2[^>]*>)(\d+)\.\s', r'\g<1>1.\g<2> ', content)

    elif 'Data-Module-2.html' in filepath:
        content = orig_content
        # Sidebar links: >1. ETL -> >2.1 ETL
        content = re.sub(r'(<a href="Data-Module-2\.html#s\d+[^"]*" class="sidebar-content-link">)(\d+)\.\s', r'\g<1>2.\g<2> ', content)
        
        # H2 tags can be "1. " or "1.1 "
        # We replace <h2>1.  with <h2>2.1 
        content = re.sub(r'(<h2[^>]*>)(\d+)\.\s', r'\g<1>2.\g<2> ', content)
        # We replace <h2>1.1  with <h2>2.1.1 
        content = re.sub(r'(<h2[^>]*>)(\d+)\.(\d+)\s', r'\g<1>2.\g<2>.\g<3> ', content)
        # Wait, the subheadings in Module 2 are actually H3? No, in the previous script check we saw they were H2. Wait, let me check again.
        # Data-Module-2.html: ['Data Manipulation', '1. Extract Transform and Load (ETL)', '1.1 Extract']
        # The previous script extracted them using `<h2[^>]*>(.*?)</h2>`, so they ARE H2 tags!

    elif 'Data-Module-3.html' in filepath:
        content = orig_content
        # Just replace "1. Data Analysis" to "3.0 Data Analysis"
        content = content.replace('>1. Data Analysis<', '>3.0 Data Analysis<')

    if content != orig_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for f in glob.glob('Data-Module-*.html'):
    process_file(f)
