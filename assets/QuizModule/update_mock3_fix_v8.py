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

# Find the start of Question 21
q21_marker = '"id": 21,'
q21_index = content.find(q21_marker, start_index)
if q21_index == -1:
    print("Question 21 not found")
    exit(1)

# Find the start of the object containing id: 21
q21_obj_start = content.rfind('{', start_index, q21_index)

# Find the start of Question 23 (to know where to stop)
q23_marker = '"id": 23,'
q23_index = content.find(q23_marker, q21_index)
if q23_index == -1:
    print("Question 23 not found")
    exit(1)

# Find the start of the object containing id: 23
q23_obj_start = content.rfind('{', q21_index, q23_index)

prefix = content[:q21_obj_start]
suffix = content[q23_obj_start:]

new_questions = """{
                "id": 21,
                "type": "MCQ",
                "q": "You want to know whether there is significant difference between the average test scores of male and female students in the same class. You check that the data is approximately normally distributed and that each group has similar variance.<br><br>How would you decide whether the difference in the test score between male and female students is significant?",
                "options": [
                        "Perform a t-test using the means and variance for male and female students and if p-value is greater than 0.05 decide that the difference is significant.",
                        "Perform a t-test using the medians and variance for male and female students and if p-value is less than 0.05 decide that the difference is significant.",
                        "Perform a t-test using the medians and variance for male and female students and if p-value is greater than 0.05 decide that the difference is significant.",
                        "Perform a t-test using the means and variance for male and female students and if p-value is less than 0.05 decide that the difference is significant."
                ],
                "a": 3,
                "marks": 1
        },
        {
                "id": 22,
                "type": "MCQ",
                "q": "Which sentence is most accurately describe the relationship between data and statistics?",
                "options": [
                        "All statistics are data, but not all data are statistics",
                        "All data are statics but no all statistics are data",
                        "Data and statistics are both purely quantitative in nature",
                        "Data and statistics are both purely qualitative in nature"
                ],
                "a": 0,
                "marks": 1
        },
        """

new_content = prefix + new_questions + suffix

with open(file_path, "w", encoding="utf-16-le") as f:
    f.write(new_content)

print("Update successful")
