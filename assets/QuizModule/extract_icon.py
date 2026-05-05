import re

with open('pearson_logo.svg', 'rb') as f:
    content = f.read().decode('utf-16')

# remove the wordmark path
content = re.sub(r'<path\s+id="wordmark".*?/>', '', content, flags=re.DOTALL)

# Now we need to update the viewBox to ONLY wrap the icon.
# Let's extract thumbprint and interrobang to find bounding box roughly
thumb = re.search(r'id="thumbprint"\s*d="(.*?)"', content, re.DOTALL).group(1)
inter = re.search(r'id="interrobang"\s*d="(.*?)"', content, re.DOTALL).group(1)

coords = re.findall(r'[-+]?\d*\.\d+|[-+]?\d+', thumb + ' ' + inter)
xs = [float(coords[i]) for i in range(0, len(coords), 2)]
ys = [float(coords[i+1]) for i in range(0, len(coords), 2)]

minx, maxx = min(xs), max(xs)
miny, maxy = min(ys), max(ys)

# Replace the original viewBox
new_viewbox = f'viewBox="{minx-1} {miny-1} {maxx-minx+2} {maxy-miny+2}"'
content = re.sub(r'viewBox=".*?"', new_viewbox, content)
# remove width and height so it scales
content = re.sub(r'width=".*?"', '', content, count=1)
content = re.sub(r'height=".*?"', '', content, count=1)

with open('pearson_icon_only.svg', 'w', encoding='utf-8') as f:
    f.write(content)
