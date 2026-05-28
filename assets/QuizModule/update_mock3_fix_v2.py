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

# We want to replace IDs 4, 5, 6
# Let's find the start of Question 4
q4_marker = '"id": 4,'
q4_index = content.find(q4_marker, start_index)
if q4_index == -1:
    print("Question 4 not found")
    exit(1)

# Find the start of the object containing id: 4
q4_obj_start = content.rfind('{', start_index, q4_index)

# Find the start of Question 7 (to know where to stop)
q7_marker = '"id": 7,'
q7_index = content.find(q7_marker, q4_index)
if q7_index == -1:
    print("Question 7 not found")
    exit(1)

# Find the start of the object containing id: 7
q7_obj_start = content.rfind('{', q4_index, q7_index)

prefix = content[:q4_obj_start]
suffix = content[q7_obj_start:]

new_questions = """{
                "id": 4,
                "type": "MCQ2",
                "q": "Which two chart types should you use to rank values in ascending or descending order? (choose 2)<br><br><span style='font-size:12px;font-style:italic;'>Note: You will receive partial credit for each correct selection.</span>",
                "options": [
                        "Bar chart",
                        "Column chart",
                        "Line chart",
                        "Bubble chart"
                ],
                "a": [0, 1],
                "marks": 1
        },
        {
                "id": 5,
                "type": "TF",
                "q": "For each statement about <b>data organization</b>, select True if the statement is correct or False if it is incorrect. <br><br><span style='font-size:12px;font-style:italic;'>Note: You will receive partial credit for each correct selection.</span>",
                "options": [
                        "Slicer can be used to filter the data",
                        "Sorts can be used to display a subset of data",
                        "Filter can be used to display a subset of data",
                        "Tables can be used to organize related data into rows and columns",
                        "Pivot Tables can be used to summarize large amounts of data"
                ],
                "a": [true, false, true, true, true],
                "marks": 5
        },
        {
                "id": 6,
                "type": "TF",
                "q": "You have a data set of 100,000 rows. The data values fall within a standard range. The data has been cleaned to remove outliers. Approximately 100 rows of the data set contain NULL values in a numeric data column. You need to determine a best practice for handling the NULL values.<br><br>For each statement about handling NULL, select <b>Yes</b> if it is a best practice or <b>No</b> if it is not. <br><br><span style='font-size:12px;font-style:italic;'>Note: You will receive partial credit for each correct selection.</span>",
                "options": [
                        "Remove the row that contains Null values",
                        "Remove each Null value with a random value",
                        "Use a statistic such as average to account for the Null values"
                ],
                "a": [false, false, true],
                "marks": 3
        },
        """

new_content = prefix + new_questions + suffix

with open(file_path, "w", encoding="utf-16-le") as f:
    f.write(new_content)

print("Update successful")
