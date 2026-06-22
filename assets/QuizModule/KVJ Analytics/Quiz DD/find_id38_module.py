import re

path = r'Quiz DD/data_quiz_data.js'
with open(path, 'rb') as f:
    content = f.read().decode('utf-16')

# Splitting by module keys
parts = re.split(r'["\'](\w+)["\']\s*:\s*\[', content)
for i in range(1, len(parts), 2):
    module_name = parts[i]
    module_content = parts[i+1]
    if 'id: 38,' in module_content or '"id": 38' in module_content:
        print(f'ID 38 is in module: {module_name}')
        # Also check if da_mock3 is missing
        if 'da_mock3' in content:
             print('da_mock3 found in content')
        else:
             print('da_mock3 NOT found in content')
        break
else:
    print('ID 38 not found')
