import codecs
import re

with codecs.open('quiz_data.js', 'r', 'utf-8') as f:
    text = f.read()

idx = text.find('"da_mock2"')
if idx != -1:
    print("Found 'da_mock2' at index", idx)
    print(text[max(0, idx-100):min(len(text), idx+500)])
    
    # We will remove the existing da_mock2 block and replace it since it broke.
    # We assume 'da_mock2' array is the last one in the file because that's what add_da_mock2 did
    # Let's replace it properly.
    start_idx = text.rfind('"da_mock2"')
    # keep everything before "da_mock2" up to the preceding comma
    comma_idx = text.rfind(',', 0, start_idx)
    new_text = text[:comma_idx] + '\n'
else:
    # Remove the closing brace to append
    idx2 = text.rfind('}')
    new_text = text[:idx2].rstrip()
    if not new_text.endswith(','):
        new_text += ',\n'

question_data = """    "da_mock2": [
        {
            "id": 1,
            "type": "MCQ2",
            "q": "You have a comma-delimited file with 100,000 rows and 200 columns of phone sales data. One column represents the phone manufacturer. You need to analyze all sales data for one manufacturer. Which two techniques should you use? (Choose 2.)<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
            "options": ["Filtering", "Transposing", "Slicing", "Deleting", "Truncating"],
            "a": [0, 2]
        }
    ]
}"""

with codecs.open('quiz_data.js', 'w', 'utf-8') as out:
    out.write(new_text + question_data)
    
print("Replaced/Added da_mock2 at the bottom of the file.")
