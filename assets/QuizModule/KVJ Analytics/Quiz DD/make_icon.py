import re

with open('pearson_logo.svg', 'rb') as f:
    content = f.read().decode('utf-16')

# Remove the wordmark path
content = re.sub(r'<path\s+id="wordmark".*?/>', '', content, flags=re.DOTALL)

# Adjust the viewBox to be a square matching the height
content = re.sub(r'viewBox="[^"]*"', 'viewBox="0 0 16 16"', content)
content = re.sub(r'width="[^"]*"', 'width="16"', content, count=1)
content = re.sub(r'height="[^"]*"', 'height="16"', content, count=1)

with open('pearson_icon_only.svg', 'w', encoding='utf-8') as f:
    f.write(content)
