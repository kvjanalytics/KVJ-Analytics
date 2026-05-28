import os
import re

path = r'Quiz DD/data_quiz_data.js'

with open(path, 'rb') as f:
    content = f.read().decode('utf-16')

# Remove Questions 41-44 using regex
# We find everything from the start of ID 41 to the end of the array (ID 44 is the last one).
# The regex looks for { "id": 41, ... } up to the last } of ID 44.
q41_44_pattern = re.compile(r'\{\s*"id":\s*41,.*\}\s*\]\s*\}\s*;', re.DOTALL)

# Let's refine the regex to just remove the objects 41-44
# ID 41 starts at { "id": 41, ...
# ID 44 ends at ... "a": 3 } 
# Then ] };
q_rem_pattern = re.compile(r'\{\s*"id":\s*41,.*\}\s*(?=\s*\]\s*\}\s*;)', re.DOTALL)

if q_rem_pattern.search(content):
    print("Found Q41-44, removing...")
    content = q_rem_pattern.sub('', content)
else:
    print("Q41-44 not found with regex.")

# Also remove any trailing comma if id 40 is now the last one.
content = re.sub(r'\},\s*(\s*\]\s*\}\s*;)', r'}\1', content)

with open(path, 'wb') as f:
    f.write(content.encode('utf-16'))

print("Removal complete.")
