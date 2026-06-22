import codecs

path = r"C:\Users\kj anand\Downloads\Quiz DD\quiz_data.js"
with codecs.open(path, 'r', 'utf-8') as f:
    text = f.read()

# Fix the missing comma if it's there
# We saw:
#         }
#     ]
#     "da_mock2": [
# 
# We need to change "    ]\n    \"da_mock2\"" to "    ],\n    \"da_mock2\""

# First, find the end of the previous block
# Since we know it's right before da_mock2
target_str = ']\n    "da_mock2": ['
if target_str in text:
    new_text = text.replace(target_str, '],\n    "da_mock2": [')
    print("Added missing comma before da_mock2")
else:
    # try with different whitespace
    new_text = text.replace(']\n    "da_mock2":', '],\n    "da_mock2":')
    if new_text != text:
        print("Added missing comma before da_mock2 (version 2)")
    else:
        print("Missing comma not found or already fixed. Continuing...")
        new_text = text

# Now ensure the question is correct
question_obj = """        {
            "id": 1,
            "type": "MCQ2",
            "q": "You have a comma-delimited file with 100,000 rows and 200 columns of phone sales data. One column represents the phone manufacturer. You need to analyze all sales data for one manufacturer. Which two techniques should you use? (Choose 2.)<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
            "options": ["Filtering", "Transposing", "Slicing", "Deleting", "Truncating"],
            "a": [0, 2]
        }"""

# Find the da_mock2 array and replace its first question
import re
match = re.search(r'"da_mock2":\s*\[\s*\{.*?\}', new_text, re.DOTALL)
if match:
    new_text = new_text[:match.start()] + '"da_mock2": [\n' + question_obj + new_text[match.end():]
    print("Updated da_mock2 question 1")
else:
    print("Could not find da_mock2 question structure to replace. Checking if it's empty...")
    if '"da_mock2": []' in new_text:
        new_text = new_text.replace('"da_mock2": []', '"da_mock2": [\n' + question_obj + '\n    ]')
        print("Populated empty da_mock2")

# Lastly, add da_mock3 if missing
if '"da_mock3"' not in new_text:
    # Need to insert it before the last }
    idx = new_text.rfind('}')
    if idx != -1:
        # Check for comma
        insertion = ',\n    "da_mock3": []\n'
        new_text = new_text[:idx].rstrip()
        if not new_text.endswith(','):
            new_text += insertion
        else:
            new_text += '\n    "da_mock3": []\n'
        new_text += '}'
        print("Added da_mock3 as empty holder")

with codecs.open(path, 'w', 'utf-8') as out:
    out.write(new_text)

print("Final update applied to quiz_data.js")
