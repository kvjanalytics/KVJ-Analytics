import os

path = r'Quiz DD/data_quiz_data.js'

# The questions 21-33 content based on my previous successful updates.
# I'll rebuild the sequence 21-33.

questions_21_31 = """{
                "id": 21,
                "type": "MCQ",
                "q": "You want to know whether there is significant difference between the average test scores of male and female students in the same class You check that the data is approximately normally distributed for each group has similar variance How would you decide whether the difference in the test score between male and female students is significant ?",
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
                "q": "An analyst is comparing the weekly sales performance of two different stores. They calculate the average weekly sales for each store and then perform a t-test to determine if the difference in average sales is statistically significant. The resulting p-value is 0.038. Assuming an alpha of 0.05, what should the analyst conclude?",
                "options": [
                        "Fail to reject the null hypothesis; the difference is not statistically significant.",
                        "Reject the null hypothesis; the difference is statistically significant.",
                        "The data is insufficient to make a conclusion.",
                        "The t-test was the wrong statistical method for this analysis."
                ],
                "a": 1,
                "marks": 1
        },
        {
                "id": 23,
                "type": "MCQ",
                "q": "You are analyzing quarterly sales across multiple years. Based on the table below, which year had the highest total sales and in which quarter did it occur?",
                "img": "quarterly_sales_table.png",
                "options": [
                        "2024, Quarter 4",
                        "2025, Quarter 1",
                        "2021, Quarter 3",
                        "2023, Quarter 3"
                ],
                "a": 0,
                "marks": 1
        },
        {
                "id": 24,
                "type": "MCQ",
                "q": "As part of an ETL process, Which process represents transformation ?",
                "options": [
                        "Changing data from summary level to detailed level",
                        "Converting data from one data type to another data type or structure",
                        "Retrieving data from many sources into a single destination",
                        "Importing a percentage of row from the source data"
                ],
                "a": 1,
                "marks": 1
        },
        {
                "id": 25,
                "type": "MCQ",
                "q": "You need to compare three (3) values of each data point in a series which data type should you use?",
                "options": [
                        "Bubble chart",
                        "Area chart",
                        "Scatter chart",
                        "Waterfall chart"
                ],
                "a": 0,
                "marks": 1
        },
        {
                "id": 26,
                "type": "MCQ",
                "q": "You ran a t-test with an alpha value of 1% (a=0.01) which p-value would cause you to reject the null hypothesis ?",
                "options": [
                        "0.001",
                        "0.011",
                        "0.09",
                        "0.10"
                ],
                "a": 0,
                "marks": 1
        },
        {
                "id": 27,
                "type": "MCQ",
                "q": "The visualization below displays sales data for two salespeople. A conclusion indicates that Salesperson 1 has a higher lead to sale rate than salesperson 2.<br><br>(A lead to sales rate is the number of actual sales divided by the number of attempted sales )<br><br>You need to determine the accuracy of this conclusion What should you conclude?",
                "img": "sales_lead_comparison.png",
                "options": [
                        "The conclusin is accurate",
                        "The conclusion is inaccurate because the visualization is missing sales and lead data",
                        "The conclusion is inaccurate because the visualization uses size manipulation",
                        "The conclusion is inaccurate because the visualization uses scale manipulation"
                ],
                "a": 3,
                "marks": 1
        },
        {
                "id": 28,
                "type": "MCQ",
                "q": "A group of students asked about their favorite flavor of ice cream the pie chart below illustrate the proportion of each response. What can you conclude from the visualization about below about ice cream preference for this group of students?",
                "img": "q28_ice_cream.png",
                "options": [
                        "The fewest students chose strawberry",
                        "The most students chose chocolate",
                        "The most students chose strawberry",
                        "Exactly half of the students chose vanilla"
                ],
                "a": 2,
                "marks": 1
        },
        {
                "id": 29,
                "type": "MCQ",
                "q": "You are exporting a dataset to a CSV file. One of the text columns contains commas within the data values. Which character should you use as a text qualifier to ensure the file can be opened correctly in Excel?",
                "options": [
                        "Semicolon (;)",
                        "Tab (\\t)",
                        "Double quote (\")",
                        "Single quote (\')"
                ],
                "a": 2,
                "marks": 1
        },
        {
                "id": 30,
                "type": "MCQ3",
                "q": "A domestic flight company wants to forecast flight delays and cancellations to provide the best experience to their customers Which three approaches would a data scientist use for this task? (Choose 3) Note. You will receive partial credit for each correct selection",
                "options": [
                        "Determining the most efficient flight paths to reduce fuel consumption",
                        "Building a model that predicts flight delays based on weather data",
                        "Proposing when a flight might be delayed without using data mining",
                        "Creating a visualization that shows the frequency of flight delays by airline",
                        "Developing a system that automatically notifies customers of flight cancellations"
                ],
                "a": [0, 1, 4],
                "marks": 1
        },
        {
                "id": 31,
                "type": "MTF",
                "q": "You are a data analytics auditor for a large public company. You need to categorize the data. Match each of the four data descriptions to the category of data it represents.<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>",
                "options": [
                        "An archive called 'Spring Sales Campaign' that contains .svg documents, retouched images and the company style guide as .pdf file",
                        "SQL database with calendar-year sales data",
                        "Results of a company-wide survey measuring feelings about the company's direction and future outlook",
                        "Information about the writer of each knowledge-base article and when it was last revised"
                ],
                "labels": [
                        "Qualitative Data",
                        "Unstructured Data",
                        "Metadata",
                        "Structured Data"
                ],
                "a": {
                        "An archive called 'Spring Sales Campaign' that contains .svg documents, retouched images and the company style guide as .pdf file": "Unstructured Data",
                        "SQL database with calendar-year sales data": "Structured Data",
                        "Results of a company-wide survey measuring feelings about the company's direction and future outlook": "Qualitative Data",
                        "Information about the writer of each knowledge-base article and when it was last revised": "Metadata"
                }
        },
        {
                "id": 32,
                "type": "MCQ",
                "q": "You want to know whether there is significant difference between the average test scores of male and female students in the same class. You check that the data is approximately normally distributed for each group, and that each group has similar variance. How would you decide whether the difference in test scores between male and female students is significant?",
                "options": [
                        "Perform a t-test using the means and variances for male and female students and if the p-value is greater than 0.05, decide that the difference is significant.",
                        "Perform a t-test using the means and variances for male and female students and if the p-value is less than 0.05, decide that the difference is significant.",
                        "Perform a t-test using the medians and variances for male and female students and if the p-value is less than 0.05, decide that the difference is significant.",
                        "Perform a t-test using the medians and variances for male and female students and if the p-value is greater than 0.05, decide that the difference is significant."
                ],
                "a": 1,
                "marks": 1
        },
        {
                "id": 33,
                "type": "MTF",
                "q": "You are a data analyst for a healthcare provider. You are designing a solution that must meet these requirements:<br><br><ul><li>Medical records must not be readable by unauthorized staff.</li><li>Patient names must be converted to cartoon character names.</li><li>However, doctors must be able to associate the cartoon names to the actual patient when providing health care</li><li>Statisticians must be able to access healthcare visits but only be able to refer to patients as their cartoon character names</li></ul><br>Choose the correct option from each drop down list.<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
                "options": [
                        "Medical records must not be readable by unauthorized staff",
                        "Patient names converted to cartoon names (reversible by doctors)",
                        "Statisticians referring to patients only by cartoon character names"
                ],
                "labels": [
                        "Encryption",
                        "Anonymization",
                        "Pseudonymization"
                ],
                "a": {
                        "Medical records must not be readable by unauthorized staff": "Encryption",
                        "Patient names converted to cartoon names (reversible by doctors)": "Pseudonymization",
                        "Statisticians referring to patients only by cartoon character names": "Pseudonymization"
                }
        }"""
# NO TRAILING COMMA because I want to close the array properly after ID 33.

# Re-insert da_mock3 section from ID 1 to 33.
# ID 1 to 20 should be preserved if possible, but I don't have them in my recent context.
# Wait! I updated 1-20 in the *previous* conversation (Conversation fa7849f1-d0c1-4f83-8535-351c4a3f31dd).
# I'll check that conversation's artifacts or logs.
# Actually, I'll just check if 1-20 are still in the file.
