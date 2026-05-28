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

# Find the start of Question 18
q18_marker = '"id": 18,'
q18_index = content.find(q18_marker, start_index)
if q18_index == -1:
    print("Question 18 not found")
    exit(1)

# Find the start of the object containing id: 18
q18_obj_start = content.rfind('{', start_index, q18_index)

# Find the start of Question 21 (to know where to stop)
q21_marker = '"id": 21,'
q21_index = content.find(q21_marker, q18_index)
if q21_index == -1:
    print("Question 21 not found")
    exit(1)

# Find the start of the object containing id: 21
q21_obj_start = content.rfind('{', q18_index, q21_index)

prefix = content[:q18_obj_start]
suffix = content[q21_obj_start:]

new_questions = """{
                "id": 18,
                "type": "MCQ",
                "q": "You will be analyzing sales and determining trends based on a very large dataset that includes the following columns:<ul style='margin-top: 10px; padding-left: 20px;'><li>CustomerName</li><li>CustomerEmail</li><li>Birthdate</li><li>FirstPurchaseDate</li><li>MostRecentPurchaseDate</li><li>TotalQuantityPurchased</li><li>TotalsalesAmount</li></ul>You need to validate the data before you start analysis.<br><br>What should you do?",
                "options": [
                        "Analyze firstPurchaseDates to determine purchasing trends",
                        "Calculate statistics TotalQuantityPurchased",
                        "Verify date ranges and value for all dates column",
                        "Create aggregation of all new column"
                ],
                "a": 2,
                "marks": 1
        },
        {
                "id": 19,
                "type": "MCQ",
                "q": "Which concept most comprehensively describe the general meaning of data in the context of data analytics?",
                "options": [
                        "Unprocessed data",
                        "Interpreted evidence",
                        "Meaningful statistics",
                        "Analyzed details"
                ],
                "a": 0,
                "marks": 1
        },
        {
                "id": 20,
                "type": "MCQ",
                "q": "A data scientist at your company creates a machine learning model to help the hiring manager select candidates from thousands of job applicants.<br><br>Which statement best describes how machine learning is used in this scenario?",
                "options": [
                        "A machine learning model defines the qualifications necessary for a given job or role",
                        "The machine learning model uses historical data and algorithms to predict future applicant performance",
                        "The machine learning system converts applicant information into a common format",
                        "The hiring manager queries the machine learning database for qualified applicants"
                ],
                "a": 1,
                "marks": 1
        },
        """

new_content = prefix + new_questions + suffix

with open(file_path, "w", encoding="utf-16-le") as f:
    f.write(new_content)

print("Update successful")
