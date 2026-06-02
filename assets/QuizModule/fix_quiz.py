import codecs
import os

path = r'data_quiz_data.js'
with codecs.open(path, 'r', 'utf-16le') as f:
    content = f.read()

# Finding the specific question 10 entry in data1
target = '"id": 10,\r\n            "marks": 4,\r\n            "type": "DND_PIVOT"'
replacement = '"id": 10,\r\n            "marks": 4,\r\n            "type": "MTF"'

if target in content:
    new_content = content.replace(target, replacement)
    with codecs.open(path, 'w', 'utf-16le') as f:
        f.write(new_content)
    print("Successfully updated Question 10 type.")
else:
    # Try different line endings just in case
    target_lf = '"id": 10,\n            "marks": 4,\n            "type": "DND_PIVOT"'
    replacement_lf = '"id": 10,\n            "marks": 4,\n            "type": "MTF"'
    if target_lf in content:
        new_content = content.replace(target_lf, replacement_lf)
        with codecs.open(path, 'w', 'utf-16le') as f:
            f.write(new_content)
        print("Successfully updated Question 10 type (LF).")
    else:
        print("Could not find the target string in the file.")
        # Search for a more flexible pattern
        import re
        pattern = r'"id":\s*10,\s*"marks":\s*4,\s*"type":\s*"DND_PIVOT"'
        if re.search(pattern, content):
            new_content = re.sub(pattern, '"id": 10,\n            "marks": 4,\n            "type": "MTF"', content)
            with codecs.open(path, 'w', 'utf-16le') as f:
                f.write(new_content)
            print("Successfully updated Question 10 type using Regex.")
        else:
            print("Regex search also failed.")
