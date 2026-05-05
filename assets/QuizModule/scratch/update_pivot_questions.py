import re

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Question pattern for the pivot table question
# It can be type MCQ, MATRIX, or MTF
pattern = re.compile(r'\{\s+id:\s+(\d+),\s+type:\s+"(?:MCQ|MATRIX|MTF|DND_PIVOT)",\s+q:\s+"From the data in the table below, you create a [Pp]ivot[Tt]able to show the combined number of certified virtual and in-person teachers for each class at each school\..*?".*?\s+a:\s+(?:\[1, 0, 4, 5\]|\{\s+"Label 1": "Networking",\s+"Label 2": "Data Analytics",\s+"Label 3": "School A",\s+"Label 4": "School B"\s+\})\s+\},', re.DOTALL)

# Replacement HTML and structure
replacement_html = """<table style='width:100%; border-collapse: collapse; margin: 15px 0; font-size: 13px; text-align: center;'><thead><tr style='background: #000; color: #fff;'><th style='padding: 8px; border: 1px solid #ddd;'>School</th><th style='padding: 8px; border: 1px solid #ddd;'>Class</th><th style='padding: 8px; border: 1px solid #ddd;'>Format</th><th style='padding: 8px; border: 1px solid #ddd;'>Certified teacher</th></tr></thead><tbody><tr><td>School A</td><td>Networking</td><td>In Person</td><td>6</td></tr><tr><td>School A</td><td>Networking</td><td>Virtual</td><td>5</td></tr><tr><td>School A</td><td>Data Analytics</td><td>In Person</td><td>2</td></tr><tr><td>School A</td><td>Data Analytics</td><td>Virtual</td><td>3</td></tr><tr><td>School B</td><td>Networking</td><td>In Person</td><td>9</td></tr><tr><td>School B</td><td>Networking</td><td>Virtual</td><td>7</td></tr><tr><td>School B</td><td>Data Analytics</td><td>In Person</td><td>2</td></tr><tr><td>School B</td><td>Data Analytics</td><td>Virtual</td><td>4</td></tr></tbody></table><br>Move the appropriate labels to the correct locations in the Pivot table structure below.<br><br><table style='border-collapse: collapse; margin: 10px 0; text-align: center;'><tr><td style='border: 1px solid #000; padding: 10px; background: #eee;'></td><td style='border: 1px solid #000; padding: 10px; font-weight: bold;'>Label 1</td><td style='border: 1px solid #000; padding: 10px; font-weight: bold;'>Label 2</td></tr><tr><td style='border: 1px solid #000; padding: 10px; font-weight: bold;'>Label 3</td><td style='border: 1px solid #000; padding: 10px;'>11</td><td style='border: 1px solid #000; padding: 10px;'>5</td></tr><tr><td style='border: 1px solid #000; padding: 10px; font-weight: bold;'>Label 4</td><td style='border: 1px solid #000; padding: 10px;'>16</td><td style='border: 1px solid #000; padding: 10px;'>6</td></tr></table>"""

def replace_fn(match):
    qid = match.group(1)
    return f'''{{ 
            id: {qid}, 
            type: "DND_PIVOT", 
            q: "{replacement_html}", 
            options: ["Label 1", "Label 2", "Label 3", "Label 4"],
            labels: ["Data Analytics", "Networking", "In-Person", "Virtual", "School A", "School B"],
            a: {{
                "Label 1": "Networking",
                "Label 2": "Data Analytics",
                "Label 3": "School A",
                "Label 4": "School B"
            }},
            marks: 4
        }},'''

new_content = pattern.sub(replace_fn, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated all occurrences of the pivot table question.")
