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

# Find the start of Question 18 (to know where to stop)
q18_marker = '"id": 18,'
q18_index = content.find(q18_marker, q11_index)
if q18_index == -1:
    print("Question 18 not found")
    exit(1)

# Find the start of the object containing id: 18
q18_obj_start = content.rfind('{', q11_index, q18_index)

prefix = content[:q11_obj_start]
suffix = content[q18_obj_start:]

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
        {
                "id": 15,
                "type": "MCQ",
                "q": "What is an example of machine learning in predictive analysis?",
                "options": [
                        "Your thermostat adjusts to a higher temperature because you programmed it based on the time of day",
                        "Your streaming service suggests a category of movies based on the last ten movies you watched.",
                        "Your vehicle turns on a warning sensor because one of its components requires maintenance.",
                        "Your computer automatically goes into sleep mode because the battery has less than ten percent power."
                ],
                "a": 1,
                "marks": 1
        },
        {
                "id": 16,
                "type": "MCQ",
                "q": "How is an unstructured data set different from structured data set",
                "options": [
                        "An unstructured data set can be quickly searched without manipulation.",
                        "The data organization of an unstructured data set is explicitly defined",
                        "An unstructured data set has a predefined data model.",
                        "An unstructured data set can store large amounts of unrelated data."
                ],
                "a": 3,
                "marks": 1
        },
        {
                "id": 17,
                "type": "MCQ3",
                "q": "You are tasked with completing a data analysis project for a large organization. During the project, you must handle personally identifiable information (PII)<br><br>Throughout the project which three principle should you follow?(Choose 3)<br><br><span style='font-size:12px;font-style:italic;'>Note: You will receive partial credit for each correct selection.</span>",
                "options": [
                        "Limit your handling of the PII to only what is necessary for the current analysis.",
                        "Remove all PII from your computer after the analysis is complete",
                        "Retain only the PII that you might need for future analysis.",
                        "Request all data from the database that contains the POI.",
                        "Keep track of the PII that you have during the analysis."
                ],
                "a": [0, 1, 4],
                "marks": 3
        },
        """

new_content = prefix + new_questions + suffix

with open(file_path, "w", encoding="utf-16-le") as f:
    f.write(new_content)

print("Update successful")
