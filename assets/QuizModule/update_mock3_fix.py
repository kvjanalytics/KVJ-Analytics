import json

file_path = "c:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/data_quiz_data.js"

with open(file_path, "r", encoding="utf-16-le") as f:
    content = f.read()

# I will replace the block from the start of "da_mock3" up to where it makes sense
# Let's find "da_mock3": [
start_marker = '"da_mock3": ['
start_index = content.find(start_marker)
if start_index == -1:
    print("da_mock3 not found")
    exit(1)

# Find the end of Question 3
# Currently Question 3 ends around line 2059
# Let's use string matching or index searching

# I'll construct the new block for the first 3 questions
new_questions = """
        {
                "id": 1,
                "type": "TF",
                "q": "For each statement about <b>data mining</b>, select True if the statement is correct or False if it is incorrect. <br><br><span style='font-size:12px;font-style:italic;'>Note: You will receive partial credit for each correct selection.</span> (2 Marks)",
                "options": [
                        "Data mining is used to summarize raw data from large data sets",
                        "Data mining is used to review underlying details in a given table"
                ],
                "a": [true, false],
                "marks": 2
        },
        {
                "id": 2,
                "type": "MCQ",
                "q": "You have been given a large data set that includes location, income, and age. Why should you disaggregate the data?",
                "options": [
                        "To hide difference among subgroups",
                        "To combine data sets and present a summary of your findings",
                        "To form generalization about the entire data set",
                        "To analyze income within different age groups or locations"
                ],
                "a": 3,
                "marks": 1
        },
        {
                "id": 3,
                "type": "MCQ",
                "q": "For which scenario should you use a line chart to represent the data?",
                "options": [
                        "The weekly average stock price during a one-year period",
                        "The proportion of yes and no answer to a survey question",
                        "The binned distribution for the height of different students",
                        "The maximum, minimum, and average value for a set of data"
                ],
                "a": 0,
                "marks": 1
        },"""

# Now find where Question 4 starts to know where to stop the replacement
q4_marker = '"id": 4,'
q4_index = content.find(q4_marker, start_index)
if q4_index == -1:
    print("Question 4 not found")
    exit(1)

# We want to replace from after the [ bracket up to before the Question 4 start
# The bracket is at start_index + len(start_marker)
prefix = content[:start_index + len(start_marker)]
# Find the start of the object containing id: 4
q4_obj_start = content.rfind('{', start_index, q4_index)
suffix = content[q4_obj_start:]

new_content = prefix + new_questions + suffix

with open(file_path, "w", encoding="utf-16-le") as f:
    f.write(new_content)

print("Update successful")
