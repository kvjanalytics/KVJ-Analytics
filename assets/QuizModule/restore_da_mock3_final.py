import os
import re

path = r'Quiz DD/data_quiz_data.js'

with open(path, 'rb') as f:
    content = f.read().decode('utf-16')

# Check if it ends with da_mock2 array
if '"da_mock2": [' in content and 'da_mock3' not in content:
    print("da_mock3 missing, preparing to restore...")
    
    # We need to find the closing bracket of da_mock2 array and the object.
    # The file ends with:
    #         }]
    # };
    
    # We want to replace the final `}]` with `}],\n    "da_mock3": [`
    
    # Using regex to find the end points
    end_pattern = re.compile(r'\]\s*\}\s*;$', re.DOTALL)
    
    da_mock3_content = """\n    "da_mock3": [
        {
                "id": 1,
                "type": "MCQ",
                "q": "You have been given a large data set that includes location, income, and age.<br>Why should you disaggregate the data?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>",
                "options": [
                        "To hide difference among subgroups",
                        "To combine data sets and present a summary of your findings",
                        "To form generalization about the entire data set",
                        "To analyze income within different age groups or locations"
                ],
                "a": 3
        },
        {
                "id": 2,
                "type": "MCQ",
                "q": "As part of an ETL process, Which process represents transformation?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>",
                "options": [
                        "Changing data from summary level to detailed level",
                        "Converting data from one data type to another data type or structure",
                        "Retrieving data from many sources into a single destination",
                        "Importing a percentage of row from the source data"
                ],
                "a": 1
        },
        {
                "id": 3,
                "type": "MCQ",
                "q": "How is machine learning typically used in a modern recruitment (hiring) process?",
                "options": [
                        "To manually call every candidate",
                        "To predict applicant performance using historical data patterns",
                        "To convert resumes from PDF to Word format",
                        "To write job descriptions for managers"
                ],
                "a": 1
        },
        {
                "id": 4,
                "type": "MCQ",
                "q": "A dataset contains a column labeled 'Phone Number' with values formatted like '(555) 123-4567'. Which data type is most appropriate for storing this information?",
                "options": [
                        "Integer",
                        "String",
                        "Float",
                        "Boolean"
                ],
                "a": 1
        },
        {
                "id": 5,
                "type": "MCQ",
                "q": "Which of the following is an example of Unstructured Data?",
                "options": [
                        "A relational database table",
                        "An Excel spreadsheet of sales records",
                        "A collection of customer review audio files",
                        "A library of books sorted by ISBN"
                ],
                "a": 2
        },
        {
                "id": 6,
                "type": "MCQ",
                "q": "Which scenario is the most appropriate use case for a Line Chart?",
                "options": [
                        "Comparing the market share of five different companies",
                        "Showing the relationship between employee height and weight",
                        "Tracking the stock price of a company over 30 days",
                        "Comparing the number of pets owned by different households"
                ],
                "a": 2
        },
        {
                "id": 7,
                "type": "MCQ",
                "q": "Which reporting technique allows users to break down a total value (e.g., Total Revenue) into its component parts (e.g., Revenue by City)?",
                "options": [
                        "Data Truncation",
                        "Data Disaggregation",
                        "Data Masking",
                        "Data Appending"
                ],
                "a": 1
        },
        {
                "id": 8,
                "type": "MCQ",
                "q": "You need to identify outliers in a delivery time dataset. Which visualization would most clearly display these anomalies?",
                "img": "outlier_detection_visual.png",
                "options": [
                        "Pie Chart",
                        "Scatter Plot",
                        "Heatmap",
                        "Sankey Diagram"
                ],
                "a": 1
        },
        {
                "id": 9,
                "type": "MTF",
                "q": "Match each analysis type with the core question it seeks to answer.<br><span style='font-size:12px;font-style:italic;'>Note: You will receive partial credit for each correct match.</span>",
                "options": [
                        "Descriptive",
                        "Diagnostic",
                        "Predictive",
                        "Prescriptive",
                        "Inferential"
                ],
                "labels": [
                        "What happened?",
                        "Why did it happen?",
                        "What will happen?",
                        "What should we do?",
                        "Does this sample represent the population?"
                ],
                "a": {
                        "Descriptive": "What happened?",
                        "Diagnostic": "Why did it happen?",
                        "Predictive": "What will happen?",
                        "Prescriptive": "What should we do?",
                        "Inferential": "Does this sample represent the population?"
                }
        },
        {
                "id": 10,
                "type": "MCQ",
                "q": "Which chart type is specifically designed to compare three variables at once using the X-axis, Y-axis, and the size of the marker?",
                "options": [
                        "Bar Chart",
                        "Bubble Chart",
                        "Area Chart",
                        "Waterfall Chart"
                ],
                "a": 1
        },
        {
                "id": 11,
                "type": "MCQ",
                "q": "In the ETL (Extract, Transform, Load) process, which of the following is an example of 'Transformation'?",
                "options": [
                        "Importing a CSV into a data warehouse",
                        "Converting currency values from USD to INR",
                        "Running a SQL query to see data",
                        "Backing up a database"
                ],
                "a": 1
        },
        {
                "id": 12,
                "type": "MCQ3",
                "q": "While handling Personally Identifiable Information (PII) during a project, which THREE principles should you follow? (Choose 3.)",
                "options": [
                        "Limit PII usage to only necessary data",
                        "Remove PII immediately after analysis is complete",
                        "Track and audit who accesses PII",
                        "Store PII in public cloud folders",
                        "Share PII via email for quick reviews"
                ],
                "a": [0, 1, 2]
        },
        {
                "id": 13,
                "type": "MCQ",
                "q": "What is the primary relationship between Data and Statistics?",
                "options": [
                        "They are completely unrelated fields",
                        "Statistics is the tool used to interpret and summarize data",
                        "Data is created by statistics",
                        "Statistics is only used for small datasets"
                ],
                "a": 1
        },
        {
                "id": 14,
                "type": "TF",
                "q": "Determine if the following statements about data organization are True or False.",
                "options": [
                        "Slicers are a visual way to filter data in a dashboard.",
                        "Sorting changes the actual values within the dataset.",
                        "Filters allow you to hide rows that do not meet certain criteria."
                ],
                "a": [true, false, true]
        },
        {
                "id": 15,
                "type": "MCQ2",
                "q": "Which TWO of the following are generally considered NON-sensitive PII? (Choose 2.)",
                "options": [
                        "Bank account number",
                        "Medical diagnosis",
                        "Job title",
                        "General city of residence",
                        "Social Security Number"
                ],
                "a": [2, 3]
        },
        {
                "id": 16,
                "type": "MCQ2",
                "q": "Which TWO chart types are most effective for ranking items from highest to lowest? (Choose 2.)",
                "options": [
                        "Bar Chart",
                        "Pie Chart",
                        "Column Chart",
                        "Scatter Plot"
                ],
                "a": [0, 2]
        },
        {
                "id": 17,
                "type": "MCQ",
                "q": "What is the main goal of Data Validation before beginning analysis?",
                "options": [
                        "To make the report look visually appealing",
                        "To verify that values fall within logical ranges (e.g., age is not negative)",
                        "To convert all data into visualizations",
                        "To delete all outliers from the dataset"
                ],
                "a": 1
        },
        {
                "id": 18,
                "type": "MTF",
                "q": "Match the NULL value handling technique with the situation it is best suited for.",
                "options": [
                        "Row Removal",
                        "Mean Imputation",
                        "Keep as NULL"
                ],
                "labels": [
                        "When only a tiny % of rows are missing data",
                        "When you want to maintain the sample size by using averages",
                        "When the absence of data is itself a meaningful insight"
                ],
                "a": {
                        "Row Removal": "When only a tiny % of rows are missing data",
                        "Mean Imputation": "When you want to maintain the sample size by using averages",
                        "Keep as NULL": "When the absence of data is itself a meaningful insight"
                }
        },
        {
                "id": 19,
                "type": "MCQ",
                "q": "In a comma-delimited file (.csv), why are 'Text Qualifiers' (like double quotes) sometimes used?",
                "options": [
                        "To make the file look more professional",
                        "To allow data containing actual commas to stay in one column",
                        "To encrypt the information",
                        "To reduce the file size"
                ],
                "a": 1
        },
        {
                "id": 20,
                "type": "MCQ",
                "q": "You are creating a visualization to compare sales against a target. Which of the following is the most UNBIASED way to present this?",
                "options": [
                        "A 3D Pie chart with the 'Sales' slice exploded",
                        "A Grouped Bar Chart including a clear Benchmark Line for the target",
                        "A Line chart that starts the Y-axis at 50% of the target",
                        "A Bar chart where only the 'Sales' bar is colored brightly"
                ],
                "a": 1
        },
        {
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
                        "Tab (\\\\t)",
                        "Double quote (\\\")",
                        "Single quote (\\\')"
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
        }
    ]
};"""
    
    # Prepend a comma to start of da_mock3 line if needed, but here I'll replace the closing part carefully.
    content = end_pattern.sub('],' + da_mock3_content, content)
    
    with open(path, 'wb') as f:
        f.write(content.encode('utf-16'))
    print("Restoration complete.")
else:
    print("Conditions for restoration not met. Check if da_mock3 already exists or da_mock2 is missing.")
