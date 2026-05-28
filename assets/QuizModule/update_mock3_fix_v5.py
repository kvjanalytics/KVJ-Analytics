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

# Find the start of Question 11
q11_marker = '"id": 11,'
q11_index = content.find(q11_marker, start_index)
if q11_index == -1:
    print("Question 11 not found")
    exit(1)

# Find the start of the object containing id: 11
q11_obj_start = content.rfind('{', start_index, q11_index)

# Find the start of Question 15 (to know where to stop)
q15_marker = '"id": 15,'
q15_index = content.find(q15_marker, q11_index)
if q15_index == -1:
    print("Question 15 not found")
    exit(1)

# Find the start of the object containing id: 15
q15_obj_start = content.rfind('{', q11_index, q15_index)

prefix = content[:q11_obj_start]
suffix = content[q15_obj_start:]

new_questions = """{
                "id": 11,
                "type": "MCQ",
                "q": "Which data type results from processing conditional statement?",
                "options": [
                        "Boolean",
                        "Integer",
                        "character",
                        "String"
                ],
                "a": 0,
                "marks": 1
        },
        {
                "id": 12,
                "type": "MCQ",
                "q": "What type of data is too complex to be sorted in traditional data base management system (DBMS)",
                "options": [
                        "Imputed data",
                        "Metadata",
                        "Qualitative data",
                        "Big data"
                ],
                "a": 3,
                "marks": 1
        },
        {
                "id": 13,
                "type": "MCQ",
                "q": "Which data type is appropriate for a phone number using the format (###) ### - ###-####?",
                "options": [
                        "Numeric",
                        "String",
                        "Boolean",
                        "Binary"
                ],
                "a": 1,
                "marks": 1
        },
        {
                "id": 14,
                "type": "MCQ2",
                "q": "In the United state and Europe which two data points are considered non-sensitive PII(personal identifiable information)? (choose 2 )<br><br><span style='font-size:12px;font-style:italic;'>Note: You will receive partial credit for each correct selection.</span>",
                "options": [
                        "Bank account number",
                        "Medical records",
                        "Date of birth",
                        "Job title"
                ],
                "a": [2, 3],
                "marks": 2
        },
        """

new_content = prefix + new_questions + suffix

with open(file_path, "w", encoding="utf-16-le") as f:
    f.write(new_content)

print("Update successful")
