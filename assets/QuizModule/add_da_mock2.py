import codecs
import re

with codecs.open('quiz_data.js', 'r', 'utf-8') as f:
    text = f.read()

# check if da_mock2 already exists
if '"da_mock2"' in text:
    print("da_mock2 already exists in quiz_data.js")
else:
    # replace the last } or }; 
    idx = text.rfind('}')
    if idx != -1:
        new_text = text[:idx].rstrip()
        
        # if the last character inside the object is not a comma, add one
        if not new_text.endswith(','):
            new_text += ',\n'
        else:
            new_text += '\n'
            
        mock2_data = """    "da_mock2": [
        {
            "id": 1,
            "type": "MCQ2",
            "q": "You have a comma-delimited file with 100,000 rows and 200 columns of phone sales data. One column represents the phone manufacturer. You need to analyze all sales data for one manufacturer. Which two techniques should you use? (Choose 2.)",
            "options": ["Filtering", "Transposing", "Slicing", "Deleting", "Truncating"],
            "a": [0, 2]
        }
    ]
};"""
        
        new_text += mock2_data
        
        with codecs.open('quiz_data.js', 'w', 'utf-8') as out:
            out.write(new_text)
        print("Successfully added da_mock2 to quiz_data.js")
    else:
        print("Could not find the end of quizData object")
