import re

def update_module_1():
    with open('Data-Module-1.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1.7
    content = content.replace('7.1 Descriptive Statistics', '1.7.1 Descriptive Statistics')
    content = content.replace('7.2 Inferential Statistics', '1.7.2 Inferential Statistics')
    
    # 1.8
    content = content.replace('8.1 Qualitative Data', '1.8.1 Qualitative Data')
    content = content.replace('8.2 Quantitative Data', '1.8.2 Quantitative Data')
    
    # 1.10
    content = content.replace('10.1 Raw Data', '1.10.1 Raw Data')
    content = content.replace('10.2 Meta Data', '1.10.2 Meta Data')

    with open('Data-Module-1.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated Data-Module-1.html")

update_module_1()
