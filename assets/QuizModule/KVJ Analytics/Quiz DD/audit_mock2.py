import re
import json

path = r'Quiz DD/data_quiz_data.js'
with open(path, 'rb') as f:
    content = f.read().decode('utf-16')

# Extract da_mock2
match = re.search(r'["\']da_mock2["\']\s*:\s*\[(.*?)(?=\s*\]\s*[,}])', content, re.DOTALL)
if match:
    da_mock2_content = match.group(1)
    # Finding ids
    ids = re.findall(r'id:\s*(\d+)', da_mock2_content)
    print("IDs in da_mock2:", ids)
    # Print the last question
    questions = re.findall(r'\{\s*id:\s*\d+.*?\}', da_mock2_content, re.DOTALL)
    if questions:
        print("Last question in da_mock2:", questions[-1])
else:
    print("da_mock2 not found or empty")
