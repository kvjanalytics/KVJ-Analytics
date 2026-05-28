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

# Find the start of Question 4
q4_marker = '"id": 4,'
q4_index = content.find(q4_marker, start_index)
if q4_index == -1:
    print("Question 4 not found")
    exit(1)

# Find the start of the object containing id: 4
q4_obj_start = content.rfind('{', start_index, q4_index)

# Find the start of Question 9 (to know where to stop)
q9_marker = '"id": 9,'
q9_index = content.find(q9_marker, q4_index)
if q9_index == -1:
    print("Question 9 not found")
    exit(1)

# Find the start of the object containing id: 9
q9_obj_start = content.rfind('{', q4_index, q9_index)

prefix = content[:q4_obj_start]
suffix = content[q9_obj_start:]

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
        {
                "id": 7,
                "type": "MCQ",
                "q": "You are given a data set displaying the time of day and number of minutes customers waited in line for service. You need to remove bias from the results eliminating outliers.<br><br>Which visualization illustrates outliers in your dataset?<br>Select the correct Visualization in the answer area.",
                "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                "optionImages": [
                        "q44_opt1.png",
                        "q44_opt2.png",
                        "q44_opt3.png",
                        "q44_opt4.png"
                ],
                "a": 3,
                "marks": 1
        },
        {
                "id": 8,
                "type": "DROPDOWN",
                "q": "Your marketing department attends a variety of events each year and distributes promotional items to event participants. The table below shows the quantity distributed of each promotional item.<br><br>You are performing analysis on the data. Complete the sentences about the data organization by selecting the correct option from each drop-down list.<br><br><table style='width:100%; border-collapse: collapse; margin: 20px 0; font-size: 14px; text-align: center;'><thead><tr style='background: #f1f5f9;'><th style='padding: 10px; border: 1px solid #cbd5e1;'>Promotional item</th><th style='padding: 10px; border: 1px solid #cbd5e1;'>Quantity Distributed</th></tr></thead><tbody><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>T-shirt</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>600</td></tr><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>Shuffled Animal</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>425</td></tr><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>Drinkware</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>550</td></tr><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>Backpacks</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>100</td></tr><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>Blankets</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>55</td></tr><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>Magnets</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>250</td></tr><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>Gift cards</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>50</td></tr><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>Candy</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>500</td></tr><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>Notebooks</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>450</td></tr></tbody></table>Can arrange distributed items from highest to lowest: [b1]<br><br>Can limit the display of distributed items to greater than 500: [b2]<br><br>Can limit the display of promotional items to shuffled animals and T-shirt: [b3]",
                "options": [
                        ["Appending", "Filtering", "Sorting", "Truncating", "Transposing", "Slicing"],
                        ["Appending", "Filtering", "Sorting", "Truncating", "Transposing", "Slicing"],
                        ["Appending", "Filtering", "Sorting", "Truncating", "Transposing", "Slicing"]
                ],
                "a": ["Sorting", "Filtering", "Slicing"],
                "marks": 3
        },
        """

new_content = prefix + new_questions + suffix

with open(file_path, "w", encoding="utf-16-le") as f:
    f.write(new_content)

print("Update successful")
