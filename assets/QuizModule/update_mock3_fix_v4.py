import json

file_path = "c:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/data_quiz_data.js"

with open(file_path, "r", encoding="utf-16-le") as f:
    content = f.read()

# Find the start of "da_mock3"
start_marker = '"da_mock3": ['
start_index = content.find(start_marker)
if start_index == -1:
    print("da_mock3 not found")
    exit(1)

# Find the start of Question 9
q9_marker = '"id": 9,'
q9_index = content.find(q9_marker, start_index)
if q9_index == -1:
    print("Question 9 not found")
    exit(1)

# Find the start of the object containing id: 9
q9_obj_start = content.rfind('{', start_index, q9_index)

# Find the start of Question 11 (to know where to stop)
q11_marker = '"id": 11,'
q11_index = content.find(q11_marker, q9_index)
if q11_index == -1:
    print("Question 11 not found")
    exit(1)

# Find the start of the object containing id: 11
q11_obj_start = content.rfind('{', q9_index, q11_index)

prefix = content[:q9_obj_start]
suffix = content[q11_obj_start:]

new_questions = """{
                "id": 9,
                "type": "MCQ",
                "q": "You create the column chart below, which shows sales for different years. Management asks for a way to see demographic information associated with the individual sales records for each year.<br><br>You decide to create tables for each year that show the demographic information for the sales in that year. When someone clicks, the associated table will open.<br><br>Which reporting technique does this represent?",
                "img": "sales_by_year_column.png",
                "options": [
                        "Disaggregating",
                        "Unpivoting",
                        "Pivoting",
                        "Distributing"
                ],
                "a": 1,
                "marks": 1
        },
        {
                "id": 10,
                "type": "MTF",
                "q": "Match the type of data analysis on the left to the analysis question it answers on the right. You may use each item once or not at all.<br><br><span style='font-size:12px;font-style:italic;'>Note: You will receive partial credit for each correct match.</span>",
                "options": [
                        "Descriptive analysis",
                        "Diagnostic analysis",
                        "Predictive analysis",
                        "Prescriptive analysis",
                        "Hypothesis Testing"
                ],
                "labels": [
                        "What happened?",
                        "why did it happened?",
                        "What should we do next?",
                        "Is there enough evidence to draw conclusin"
                ],
                "a": {
                        "Descriptive analysis": "What happened?",
                        "Diagnostic analysis": "why did it happened?",
                        "Prescriptive analysis": "What should we do next?",
                        "Hypothesis Testing": "Is there enough evidence to draw conclusin"
                },
                "marks": 4
        },
        """

new_content = prefix + new_questions + suffix

with open(file_path, "w", encoding="utf-16-le") as f:
    f.write(new_content)

print("Update successful")
