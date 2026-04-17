import json
import re

DA_MOCK3 = [
    {
        "id": 1,
        "type": "MCQ",
        "q": "You are analyzing customer ice cream preferences across different regions. Based on the following pie chart, which flavor is the most preferred by the sample population?",
        "img": "ice_cream_preference_chart.png",
        "options": ["Vanilla", "Chocolate", "Strawberry", "Mango"],
        "a": 1
    },
    {
        "id": 2,
        "type": "MCQ",
        "q": "What is the primary reason for performing data disaggregation on a summarized sales report?",
        "options": ["To hide seasonal fluctuations", "To identify underlying trends at a granular level (e.g., specific stores)", "To increase the security of the data", "To reduce the file size of the report"],
        "a": 1
    },
    {
        "id": 3,
        "type": "MCQ",
        "q": "How is machine learning typically used in a modern recruitment (hiring) process?",
        "options": ["To manually call every candidate", "To predict applicant performance using historical data patterns", "To convert resumes from PDF to Word format", "To write job descriptions for managers"],
        "a": 1
    },
    {
        "id": 4,
        "type": "MCQ",
        "q": "A dataset contains a column labeled 'Phone Number' with values formatted like '(555) 123-4567'. Which data type is most appropriate for storing this information?",
        "options": ["Integer", "String", "Float", "Boolean"],
        "a": 1
    },
    {
        "id": 5,
        "type": "MCQ",
        "q": "Which of the following is an example of Unstructured Data?",
        "options": ["A relational database table", "An Excel spreadsheet of sales records", "A collection of customer review audio files", "A library of books sorted by ISBN"],
        "a": 2
    },
    {
        "id": 6,
        "type": "MCQ",
        "q": "Which scenario is the most appropriate use case for a Line Chart?",
        "options": ["Comparing the market share of five different companies", "Showing the relationship between employee height and weight", "Tracking the stock price of a company over 30 days", "Comparing the number of pets owned by different households"],
        "a": 2
    },
    {
        "id": 7,
        "type": "MCQ",
        "q": "Which reporting technique allows users to break down a total value (e.g., Total Revenue) into its component parts (e.g., Revenue by City)?",
        "options": ["Data Truncation", "Data Disaggregation", "Data Masking", "Data Appending"],
        "a": 1
    },
    {
        "id": 8,
        "type": "MCQ",
        "q": "You need to identify outliers in a delivery time dataset. Which visualization would most clearly display these anomalies?",
        "img": "outlier_detection_visual.png",
        "options": ["Pie Chart", "Scatter Plot", "Heatmap", "Sankey Diagram"],
        "a": 1
    },
    {
        "id": 9,
        "type": "MTF",
        "q": "Match each analysis type with the core question it seeks to answer.<br><span style='font-size:12px;font-style:italic;'>Note: You will receive partial credit for each correct match.</span>",
        "options": ["Descriptive", "Diagnostic", "Predictive", "Prescriptive", "Inferential"],
        "labels": ["What happened?", "Why did it happen?", "What will happen?", "What should we do?", "Does this sample represent the population?"],
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
        "options": ["Bar Chart", "Bubble Chart", "Area Chart", "Waterfall Chart"],
        "a": 1
    },
    {
        "id": 11,
        "type": "MCQ",
        "q": "In the ETL (Extract, Transform, Load) process, which of the following is an example of 'Transformation'?",
        "options": ["Importing a CSV into a data warehouse", "Converting currency values from USD to INR", "Running a SQL query to see data", "Backing up a database"],
        "a": 1
    },
    {
        "id": 12,
        "type": "MCQ3",
        "q": "While handling Personally Identifiable Information (PII) during a project, which THREE principles should you follow? (Choose 3.)",
        "options": ["Limit PII usage to only necessary data", "Remove PII immediately after analysis is complete", "Track and audit who accesses PII", "Store PII in public cloud folders", "Share PII via email for quick reviews"],
        "a": [0, 1, 2]
    },
    {
        "id": 13,
        "type": "MCQ",
        "q": "What is the primary relationship between Data and Statistics?",
        "options": ["They are completely unrelated fields", "Statistics is the tool used to interpret and summarize data", "Data is created by statistics", "Statistics is only used for small datasets"],
        "a": 1
    },
    {
        "id": 14,
        "type": "TF",
        "q": "Determine if the following statements about data organization are True or False.",
        "options": ["Slicers are a visual way to filter data in a dashboard.", "Sorting changes the actual values within the dataset.", "Filters allow you to hide rows that do not meet certain criteria."],
        "a": [True, False, True]
    },
    {
        "id": 15,
        "type": "MCQ2",
        "q": "Which TWO of the following are generally considered NON-sensitive PII? (Choose 2.)",
        "options": ["Bank account number", "Medical diagnosis", "Job title", "General city of residence", "Social Security Number"],
        "a": [2, 3]
    },
    {
        "id": 16,
        "type": "MCQ2",
        "q": "Which TWO chart types are most effective for ranking items from highest to lowest? (Choose 2.)",
        "options": ["Bar Chart", "Pie Chart", "Column Chart", "Scatter Plot"],
        "a": [0, 2]
    },
    {
        "id": 17,
        "type": "MCQ",
        "q": "What is the main goal of Data Validation before beginning analysis?",
        "options": ["To make the report look visually appealing", "To verify that values fall within logical ranges (e.g., age is not negative)", "To convert all data into visualizations", "To delete all outliers from the dataset"],
        "a": 1
    },
    {
        "id": 18,
        "type": "MTF",
        "q": "Match the NULL value handling technique with the situation it is best suited for.",
        "options": ["Row Removal", "Mean Imputation", "Keep as NULL"],
        "labels": ["When only a tiny % of rows are missing data", "When you want to maintain the sample size by using averages", "When the absence of data is itself a meaningful insight"],
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
        "options": ["To make the file look more professional", "To allow data containing actual commas to stay in one column", "To encrypt the information", "To reduce the file size"],
        "a": 1
    },
    {
        "id": 20,
        "type": "MCQ",
        "q": "You are creating a visualization to compare sales against a target. Which of the following is the most UNBIASED way to present this?",
        "options": ["A 3D Pie chart with the 'Sales' slice exploded", "A Grouped Bar Chart including a clear Benchmark Line for the target", "A Line chart that starts the Y-axis at 50% of the target", "A Bar chart where only the 'Sales' bar is colored brightly"],
        "a": 1
    },
    {
        "id": 21,
        "type": "MCQ",
        "q": "What is a primary characteristic of Big Data that makes it difficult to manage with traditional database systems?",
        "options": ["It only contains text", "It has low velocity and volume", "It has extreme volume, velocity, and variety", "It is only collected via paper surveys"],
        "a": 2
    },
    {
        "id": 22,
        "type": "MCQ",
        "q": "You run a t-test with a significance level of \u03b1 = 0.01. Which p-value would allow you to reject the null hypothesis?",
        "options": ["0.05", "0.011", "0.008", "0.10"],
        "a": 2
    },
    {
        "id": 23,
        "type": "MCQ",
        "q": "Based on the Lead-to-Sale Rate chart, which channel has the highest conversion efficiency despite having lower total volume?",
        "img": "lead_conversion_efficiency.png",
        "options": ["Organic Search", "Direct Marketing", "Social Media", "Referrals"],
        "a": 3
    },
    {
        "id": 24,
        "type": "MCQ",
        "q": "In the context of data analysis, how is 'Information' defined?",
        "options": ["Any collection of numbers", "Interpreted and processed data that provides meaning or context", "Raw signals collected from hardware", "A database that has not been queried yet"],
        "a": 1
    },
    {
        "id": 25,
        "type": "MCQ",
        "q": "Which of the following is a classic example of Machine Learning in Predictive Analysis?",
        "options": ["A calculator showing the result of 1+1", "A streaming service recommending music based on your listening history", "A computer shutting down on a timer", "A printer showing a 'Low Ink' warning"],
        "a": 1
    },
    {
        "id": 26,
        "type": "DD",
        "q": "Complete the data organization description by choosing the correct operations.<br><br>First, we [b1] the data to hide irrelevant categories. Then, we [b2] the list alphabetically. Finally, we [b3] a specific slice of the data for investigation.",
        "options": ["Filter", "Sort", "Slicing"],
        "a": ["Filter", "Sort", "Slicing"]
    },
    {
        "id": 27,
        "type": "MCQ",
        "q": "When writing a logical statement like <code>IF(Sales > 5000)</code>, what is the resulting data type for that specific output?",
        "options": ["Integer", "String", "Boolean", "Float"],
        "a": 2
    },
    {
        "id": 28,
        "type": "TF",
        "q": "Evaluate these statements about Data Mining.",
        "options": ["Data mining is used to identify anomalies and pattern correlations in large datasets.", "Data mining requires an analyst to manually read every single record.", "Data mining helps in summarizing complex data into actionable insights."],
        "a": [True, False, True]
    }
]

def restore():
    path = r"c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Simple string replacement for the empty array we just created in repair
    target = '"da_mock3": []'
    replacement = f'"da_mock3": {json.dumps(DA_MOCK3, indent=8)}'
    
    if target in content:
        new_content = content.replace(target, replacement)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully injected Mock 3 questions.")
    else:
        print("Could not find Target in quiz_data.js")

if __name__ == "__main__":
    restore()
