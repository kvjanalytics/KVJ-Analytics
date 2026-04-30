var dataQuizData = {
    "data1": [
        {
            id: 1,
            type: "MCQ",
            q: "What is metadata?",
            options: ["Statistics", "The text content of a message", "Numerical facts", "The context that give data meaning"],
            a: 3,
            marks: 2
        },
        {
            id: 2,
            type: "MCQ",
            q: "A popular social media site records and count clicks, likes, and dislikes, and other user interactions. What type of data is collected?",
            options: ["Continuous data", "Imputed Data", "Qualitative Data", "Big Data"],
            a: 3,
            marks: 2
        },
        {
            id: 3,
            type: "MCQ",
            q: "Which data type can store a phrase or sentence?",
            options: ["Integer", "String", "Boolean", "Character"],
            a: 1,
            marks: 2
        },
        {
            id: 4,
            type: "MCQ",
            q: "Which data structure describes the following data [\"Aabid\", \"jesenia\", \"Mark\"]?",
            options: ["Graph", "Table", "List", "Multi-dimensional array"],
            a: 2,
            marks: 2
        },
        {
            id: 5,
            type: "MCQ",
            q: "What is a raw data?",
            options: ["Unprocessed Data", "Purely numerical Data", "Summarized Data", "Visualized Data"],
            a: 0,
            marks: 2
        },
        {
            id: 6,
            type: "MCQ",
            q: "Which Data structure have multiple rows and columns?",
            options: ["Series", "Table", "One-dimensional Array", "List"],
            a: 1,
            marks: 2
        },
        {
            id: 7,
            type: "MCQ",
            q: "Person A has 5 coins and person B has 10 coins. Which type of data does the number of coins represent?",
            options: ["Ordinal Data", "Metadata", "Qualitative data", "Quantitative data"],
            a: 3,
            marks: 2
        },
        {
            id: 8,
            type: "MCQ",
            q: "What is the main characteristic of 'Ratio' data that distinguishes it from 'Interval' data?",
            options: ["It has no specific order", "It has a true absolute zero", "It only uses text labels", "It is always unstructured"],
            a: 1,
            marks: 2
        },
        {
            id: 9,
            type: "MCQ",
            q: "Which data type is used to store only two possible values, typically True and False?",
            options: ["Integer", "String", "Boolean", "Character"],
            a: 2,
            marks: 2
        },
        {
            id: 10,
            type: "MCQ",
            q: "Which of the following terms describes raw facts and figures that have not yet been processed?",
            options: ["Knowledge", "Information", "Data", "Metadata"],
            a: 2,
            marks: 2
        }
    ],
    "data2": [
        {
            id: 1,
            type: "MCQ",
            q: "What is an example of data cleaning?",
            options: [
                "Arranging Excel data rows in an order that is easy for a user to read",
                "Ensuring that the data in a Word table uses a consistent font",
                "Adding quotation marks to the beginning and end of a tab-delimited file",
                "Removing non-printable characters from a comma-delimited file"
            ],
            a: 3,
            marks: 2
        },
        {
            id: 2,
            type: "MCQ2",
            q: "You need to create a data view based on aggregations for further visual analysis. Your data includes sales information for the past five years for food products at your company's stores. Each product belongs to one category. For example, milk belongs to the Dairy category.<br><br>The data view must meet the following requirements:<br>• Include all products and their associated categories.<br>• Include sales subtotals for each category and year.<br>• Display a grand total of sales for each category.<br>• Create a summary of each category for every year.<br><br>Which two aggregation methods should you use to create the data view? (Choose 2)<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection</span>",
            options: [
                "Filtering",
                "Pivoting",
                "Merging",
                "Grouping"
            ],
            a: [1, 3],
            marks: 2
        },
        {
            id: 3,
            type: "MCQ",
            q: "Your company has summarized a large set for the region you live in. You need to compare the result from Urban and Rural communities within your region.<br><br>What is the fastest way to obtain this information?",
            options: [
                "Review data from neighboring regions",
                "Aggregate the data",
                "Disaggregate the data",
                "Collect new data sample"
            ],
            a: 2,
            marks: 2
        },
        {
            id: 4,
            type: "MTF",
            q: "Your marketing department attends a variety of events each year and distributes promotional items to event participants. The table below shows the quantity distributed of each promotional item.<br><br><table style='width:100%; border-collapse: collapse; margin: 20px 0; font-size: 14px; text-align: center;'><thead><tr style='background: #f1f5f9;'><th style='padding: 10px; border: 1px solid #cbd5e1;'>Promotional item</th><th style='padding: 10px; border: 1px solid #cbd5e1;'>Quantity Distributed</th></tr></thead><tbody><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>T-shirt</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>600</td></tr><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>Shuffled Animal</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>425</td></tr><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>Drinkware</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>550</td></tr><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>Backpacks</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>100</td></tr><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>Blankets</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>55</td></tr><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>Magnets</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>250</td></tr><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>Gift cards</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>50</td></tr><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>Candy</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>500</td></tr><tr><td style='padding: 8px; border: 1px solid #cbd5e1;'>Notebooks</td><td style='padding: 8px; border: 1px solid #cbd5e1;'>450</td></tr></tbody></table>You are performing analysis on the data. Complete the sentence about the data organization by selecting the correct option from the list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>",
            options: [
                "Can arrange distributed items from highest to lowest",
                "Can limit the display of distributed items to greater than 500",
                "Can limit the display of promotional items to shuffled animals and T-shirt"
            ],
            labels: ["Appending", "Filtering", "Sorting", "Truncating", "Transposing", "Slicing"],
            a: {
                "Can arrange distributed items from highest to lowest": "Sorting",
                "Can limit the display of distributed items to greater than 500": "Filtering",
                "Can limit the display of promotional items to shuffled animals and T-shirt": "Filtering"
            },
            marks: 2
        },
        {
            id: 5,
            type: "MCQ",
            q: "As part of an ETL process, which process represents transformation?",
            options: [
                "Changing data from summary level to detailed level",
                "Converting data from one data type to another data type or structure",
                "Retrieving data from many sources into a single destination",
                "Importing a percentage of row from the source data"
            ],
            a: 1,
            marks: 2
        },
        {
            id: 6,
            type: "MCQ",
            q: "The marketing team wants to know which market segment had the highest sales last year. Which type of data analytics should they use?",
            options: [
                "Diagnostic analytics",
                "Descriptive analytics",
                "Predictive analytics",
                "Prescriptive analytics"
            ],
            a: 1,
            marks: 2
        },
        {
            id: 7,
            type: "SHORT",
            q: "A file named <strong>courses data</strong> contains the following content:<br><br><pre>Title|Number|Hours\nAlgebra|MT101|3\nHistory|HS201|3\nPhysics|PS302|4\nMusic|MS101|2\nArt|AR201|2</pre><br>You need to use Python to read the data from the file so that you can import it into a database file. What parameter should you specify in the <code>read_csv</code> function to correctly handle this file format?",
            a: "sep='|'",
            marks: 2
        },
        {
            id: 8,
            type: "MCQ2",
            q: "A coworker is having trouble joining two database tables, Table A and Table B, that were imported from CSV files. They say the tables have no common values.<br><br>You look at the data in the original CSV file and find that the RowKey values in the TableA file and the RowID values in the TableB file look identical. Both have three numbers followed by a dash(-) and two letters.<br><br>Which two actions should you complete next? (Choose 2)<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection</span>",
            options: [
                "Verify that the data in the database was imported as a numeric data type",
                "Trim empty spaces from both of the valid characters",
                "Visually compare the database values to the CSV values",
                "Trim empty spaces from only the right side of the valid characters"
            ],
            a: [1, 2],
            marks: 2
        },
        {
            id: 9,
            type: "MCQ2",
            q: "Each month you need to automatically transform the data from two XML documents into a single flat file with columns and rows that excel can open and interpret. The document names and structure remain constant. You know the relationship between the two XML documents.<br><br>Which two resources can you use? (Choose 2)<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection</span>",
            options: [
                "Json",
                "Power Query for Excel (M)",
                "Microsoft Excel",
                "Python"
            ],
            a: [1, 3],
            marks: 2
        },
        {
            id: 10,
            type: "MCQ",
            q: "You have a comma-delimited file with 100,000 rows and 200 columns of phone sales data. One column represents the Phone manufacturer.<br><br>You need to analyze all sales data for a specific manufacturer. Which technique should you use?",
            options: [
                "Deleting",
                "Transposing",
                "Truncating",
                "Filtering"
            ],
            a: 3,
            marks: 2
        },
        {
            id: 11,
            type: "TF",
            q: "For each statement about data disaggregation, select whether it is True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection</span>",
            options: [
                "Data disaggregation provides a summary of the data",
                "Data disaggregation combines data from different sources",
                "Data disaggregation can clarify trends and patterns among subgroups"
            ],
            a: [false, false, true],
            marks: 2
        },
        {
            id: 12,
            type: "MTF",
            q: "From the data in the table below, you create a pivot table to show the combined number of certified virtual and in-person teachers for each class at each school.<br><br><table style='width:100%; border-collapse: collapse; margin: 15px 0; font-size: 13px; text-align: center;'><thead><tr style='background: #000; color: #fff;'><th style='padding: 8px; border: 1px solid #ddd;'>School</th><th style='padding: 8px; border: 1px solid #ddd;'>Class</th><th style='padding: 8px; border: 1px solid #ddd;'>Format</th><th style='padding: 8px; border: 1px solid #ddd;'>Certified teacher</th></tr></thead><tbody><tr><td>School A</td><td>Networking</td><td>In Person</td><td>6</td></tr><tr><td>School A</td><td>Networking</td><td>Virtual</td><td>5</td></tr><tr><td>School A</td><td>Data Analytics</td><td>In Person</td><td>2</td></tr><tr><td>School A</td><td>Data Analytics</td><td>Virtual</td><td>3</td></tr><tr><td>School B</td><td>Networking</td><td>In Person</td><td>9</td></tr><tr><td>School B</td><td>Networking</td><td>Virtual</td><td>7</td></tr><tr><td>School B</td><td>Data Analytics</td><td>In Person</td><td>2</td></tr><tr><td>School B</td><td>Data Analytics</td><td>Virtual</td><td>4</td></tr></tbody></table><br>Move the appropriate labels to the correct locations in the Pivot table structure below.<br><br><table style='border-collapse: collapse; margin: 10px 0; text-align: center;'><tr><td style='border: 1px solid #000; padding: 10px; background: #eee;'></td><td style='border: 1px solid #000; padding: 10px; font-weight: bold;'>Label 1</td><td style='border: 1px solid #000; padding: 10px; font-weight: bold;'>Label 2</td></tr><tr><td style='border: 1px solid #000; padding: 10px; font-weight: bold;'>Label 3</td><td style='border: 1px solid #000; padding: 10px;'>11</td><td style='border: 1px solid #000; padding: 10px;'>5</td></tr><tr><td style='border: 1px solid #000; padding: 10px; font-weight: bold;'>Label 4</td><td style='border: 1px solid #000; padding: 10px;'>16</td><td style='border: 1px solid #000; padding: 10px;'>6</td></tr></table><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>",
            options: ["Label 1", "Label 2", "Label 3", "Label 4"],
            labels: ["Data Analytics", "Networking", "In-Person", "Virtual", "School A", "School B"],
            a: {
                "Label 1": "Networking",
                "Label 2": "Data Analytics",
                "Label 3": "School A",
                "Label 4": "School B"
            },
            marks: 2
        },
        {
            id: 13,
            type: "MCQ",
            q: "What concept allows analysts to drill down into data and examine different levels of information that may be crucial in diagnostic analytics?",
            options: [
                "Granularity",
                "Completeness",
                "Interpretability",
                "Transparency"
            ],
            a: 0,
            marks: 2
        },
        {
            id: 14,
            type: "MCQ",
            q: "You have a dataset that includes product review scores and demographic information about the reviewers. There are no subcategories associated with the demographic answers. The table below shows a selection of the data.<br><br><table style='width:100%; border-collapse: collapse; margin: 15px 0; font-size: 13px; text-align: center;'><thead><tr style='background: #f1f5f9;'><th style='padding: 8px; border: 1px solid #cbd5e1;'>Product</th><th style='padding: 8px; border: 1px solid #cbd5e1;'>Review Score</th><th style='padding: 8px; border: 1px solid #cbd5e1;'>Review id</th><th style='padding: 8px; border: 1px solid #cbd5e1;'>Industry</th><th style='padding: 8px; border: 1px solid #cbd5e1;'>Ethnicity</th></tr></thead><tbody><tr><td>AX-150</td><td>74</td><td>123</td><td>Education</td><td>Asian</td></tr><tr><td>BK-330</td><td>82</td><td>124</td><td>Finance</td><td>Latino or Hispanic</td></tr><tr><td>BK-315</td><td>79</td><td>125</td><td>Health Care</td><td>Native Hawaiian...</td></tr><tr><td>CX-290</td><td>86</td><td>126</td><td>Other</td><td>African-American</td></tr><tr><td>BD-250</td><td>61</td><td>127</td><td>Finance</td><td>Other</td></tr><tr><td>CD-140</td><td>35</td><td>128</td><td>Food Services</td><td>Caucasian</td></tr><tr><td>AX-310</td><td>84</td><td>129</td><td>Education</td><td>Caucasian</td></tr></tbody></table><br>Which scenario is an example of <strong>disaggregating</strong> the dataset?",
            options: [
                "By average and mode of the scores for each product grouped by the ethnicity of the reviewers",
                "Display the overall average and mode of all scores on a per-product basis",
                "Display a list of ethnicities that are included in the other option",
                "Display the overall average and mode of all scores and a count of all reviews"
            ],
            a: 0,
            marks: 2
        },
        {
            id: 15,
            type: "MCQ",
            q: "You are reviewing a database of restaurant menu items. The table below shows a selection of the data.<br><br><table style='width:100%; border-collapse: collapse; margin: 15px 0; font-size: 13px; text-align: center;'><thead><tr style='background: #f1f5f9;'><th style='padding: 8px; border: 1px solid #cbd5e1;'>Item</th><th style='padding: 8px; border: 1px solid #cbd5e1;'>Type</th><th style='padding: 8px; border: 1px solid #cbd5e1;'>Menu</th><th style='padding: 8px; border: 1px solid #cbd5e1;'>Gluten-free</th><th style='padding: 8px; border: 1px solid #cbd5e1;'>Vegan</th></tr></thead><tbody><tr><td>Croque Monsieur</td><td>Sandwich</td><td>Lunch</td><td>Optional</td><td>No</td></tr><tr><td>Lemon Meringue Pie</td><td>Pie</td><td>Dessert</td><td>No</td><td>No</td></tr><tr><td>Matcha Slice</td><td>Cake</td><td>Dessert</td><td>No</td><td>No</td></tr><tr><td>Shrimp and crab Louie</td><td>Salad</td><td>Lunch; Dinner</td><td>Yes</td><td>No</td></tr><tr><td>Vegan Chocolate...</td><td>Cake</td><td>Dessert</td><td>Yes</td><td>Yes</td></tr></tbody></table><br>You need to display only items on the <strong>dessert</strong> menu with a type of <strong>cake</strong>. What should you do to nondestructively limit the data display?",
            options: [
                "Group the data by menu and then group the data on the dessert menu by type",
                "Delete all data that has a menu other than dessert, then delete all data that has a type other than cake",
                "Add two slicers, one for menu and one for type. Set the menu slicer to dessert and the type slicer to cake",
                "Sort the data by menu and within each menu, sort by type"
            ],
            a: 2,
            marks: 2
        },
        {
            id: 16,
            type: "MCQ",
            q: "Which of the following is a common task in data cleaning?",
            options: [
                "Removing duplicate rows from a dataset",
                "Creating a pie chart of the data",
                "Collecting new data through interviews",
                "Publishing the data to a public website"
            ],
            a: 0,
            marks: 2
        },
        {
            id: 17,
            type: "MCQ",
            q: "Which technique is used to rearrange data rows based on a specific column, such as Alphabetical order or Date?",
            options: [
                "Filtering",
                "Sorting",
                "Aggregation",
                "Pivoting"
            ],
            a: 1,
            marks: 2
        },
        {
            id: 18,
            type: "MCQ",
            q: "Which aggregation function should be used to find the most frequently occurring value in a dataset?",
            options: [
                "SUM",
                "AVG",
                "COUNT",
                "MODE"
            ],
            a: 3,
            marks: 2
        },
        {
            id: 19,
            type: "MCQ",
            q: "What does the 'L' stand for in the data management process known as ETL?",
            options: [
                "Label",
                "Link",
                "Load",
                "List"
            ],
            a: 2,
            marks: 2
        },
        {
            id: 20,
            type: "MCQ",
            q: "Which file format is specifically designed to store data in a plain text format where values are separated by commas?",
            options: [
                "XML",
                "JSON",
                "CSV",
                "HTML"
            ],
            a: 2,
            marks: 2
        }
    ],
    "data3": [
        {
            id: 1,
            type: "MTF",
            q: "You are performing descriptive analytics on quarterly sales data. Move the appropriate statistical metrics from the list on the left to the correct locations on the right.<br><br><img src='recreated_table.png' style='max-width:100%; border:1px solid #e5e7eb; border-radius:6px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 14px;'><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct response.</span>",
            options: ["Metric 1", "Metric 2", "Metric 3", "Metric 4"],
            labels: ["Average", "Max", "Median", "Mode", "Sum", "Min"],
            a: {
                "Metric 1": "Sum",
                "Metric 2": "Max",
                "Metric 3": "Min",
                "Metric 4": "Mode"
            },
            marks: 2
        },
        {
            id: 2,
            type: "MTF",
            q: "You are using data analytics to help answer business questions about a new product your company released.<br><br>Move each type of data analytics from the list on the left to the correct question on the right.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>",
            options: ["Why did it happen?", "What action should be taken?", "What might happen?", "What happened in the past?"],
            labels: ["Descriptive Analysis", "Diagnostic Analysis", "Predictive Analysis", "Prescriptive Analysis"],
            a: {
                "Why did it happen?": "Diagnostic Analysis",
                "What action should be taken?": "Prescriptive Analysis",
                "What might happen?": "Predictive Analysis",
                "What happened in the past?": "Descriptive Analysis"
            },
            marks: 2
        },
        {
            id: 3,
            type: "MCQ",
            q: "What is an example of machine learning in predictive analysis?",
            options: [
                "Your thermostat adjusts to a higher temperature because you programmed it based on the time of day.",
                "Your streaming service suggests a category of movies based on the last ten movies you watched.",
                "Your vehicle turns on a warning sensor because one of its components requires maintenance.",
                "Your computer automatically goes into sleep mode because the battery has less than ten percent power."
            ],
            a: 1,
            marks: 2
        },
        {
            id: 4,
            type: "TF",
            q: "For each statement about data mining, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
            options: [
                "Data mining is used to find anomalies.",
                "Data mining is used to summarize raw data from large data sets.",
                "Data mining is used to review underlying details in a given table."
            ],
            a: [true, true, false],
            marks: 2
        },
        {
            id: 5,
            type: "MTF",
            q: "Match the type of data analysis on the left to the analysis question it answers on the right. You may use each item once or not at all.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct response.</span>",
            options: [
                "What happened?",
                "Why did it happen?",
                "What should we do next?",
                "Is there enough evidence to draw a conclusion?"
            ],
            labels: [
                "Descriptive analysis",
                "Diagnostic analysis",
                "Predictive analysis",
                "Prescriptive analysis",
                "Hypothesis Testing"
            ],
            a: {
                "What happened?": "Descriptive analysis",
                "Why did it happen?": "Diagnostic analysis",
                "What should we do next?": "Prescriptive analysis",
                "Is there enough evidence to draw a conclusion?": "Hypothesis Testing"
            },
            marks: 2
        },
        {
            id: 6,
            type: "MCQ",
            q: "You will be analyzing sales and determining trends based on a very large dataset that includes the following columns:<ul style='margin-top: 10px; margin-bottom: 15px; padding-left: 20px; line-height: 1.6;'><li>CustomerName</li><li>CustomerEmail</li><li>Birthdate</li><li>FirstPurchaseDate</li><li>MostRecentPurchaseDate</li><li>TotalQuantityPurchased</li><li>TotalsalesAmount</li></ul>You need to validate the data before you start analysis.<br><br>What should you do?",
            options: [
                "Analyze firstPurchaseDates to determine purchasing trends",
                "Calculate statistics TotalQuantityPurchased",
                "Verify date ranges and value for all dates column",
                "Create aggregation of all new column"
            ],
            a: 2,
            marks: 2
        },
        {
            id: 7,
            type: "MCQ",
            q: "A data scientist at your company creates a machine learning model to help the hiring manager select candidates from thousands of job applicants. Which statement best describes how machine learning is used in this scenario?",
            options: [
                "A machine learning model defines the qualifications necessary for a given job or role",
                "The machine learning model uses historical data and algorithms to predict future applicant performance",
                "The machine learning system converts applicant information into a common format",
                "The hiring manager queries the machine learning database for qualified applicants"
            ],
            a: 1,
            marks: 2
        },
        {
            id: 8,
            type: "MCQ",
            q: "You ran a t-test with an alpha value of 1% (&alpha;=0.01). Which p-value would cause you to reject the null hypothesis?",
            options: [
                "0.001",
                "0.011",
                "0.09",
                "0.10"
            ],
            a: 0,
            marks: 2
        },
        {
            id: 9,
            type: "MCQ",
            q: "You want to know whether there is a significant difference between the average test scores of male and female students in the same class. You check that the data is approximately normally distributed for each group and has similar variance.<br><br>How would you decide whether the difference in the test scores between male and female students is significant?",
            options: [
                "Perform a t-test using the means and variance for male and female students and if p-value is greater than 0.05 decide that the difference is significant.",
                "Perform a t-test using the medians and variance for male and female students and if p-value is less than 0.05 decide that the difference is significant.",
                "Perform a t-test using the medians and variance for male and female students and if p-value is greater than 0.05 decide that the difference is significant.",
                "Perform a t-test using the means and variance for male and female students and if p-value is less than 0.05 decide that the difference is significant."
            ],
            a: 3,
            marks: 2
        },
        {
            id: 10,
            type: "MCQ",
            q: "You are analyzing sales activity that occurs on national holidays.<br><br>What level of data granularity will enable you to perform the most precise analysis?",
            options: [
                "Years",
                "Months",
                "Weeks",
                "Days",
                "Hours"
            ],
            a: 4,
            marks: 2
        },
        {
            id: 11,
            type: "MCQ",
            q: "What concept allows analysts to drill down into data and examine different levels of information that may be crucial in diagnostic analytics?",
            options: [
                "Granularity",
                "Completeness",
                "Interpretability",
                "Transparency"
            ],
            a: 0,
            marks: 2
        },
        {
            id: 12,
            type: "TF",
            q: "For each statement about machine learning, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
            options: [
                "Machine learning can predict the probability of rain in a region by examining known weather patterns.",
                "Machine learning can help determine whether a candidate will pass an exam without looking at historical scores.",
                "Machine learning can be used to automatically decline financial purchases based on previous purchase activity."
            ],
            a: [true, false, true],
            marks: 2
        },
        {
            id: 13,
            type: "MCQ",
            q: "In which scenario will artificial intelligence (AI) provide the greatest benefit?",
            options: [
                "Predicting maintenance requirements for an international rental car company's fleet vehicles",
                "Determining the statistical mean, mode, and standard deviation of the grades for a class",
                "Recording daily sales for the three stores owned by one franchise owner",
                "Interpreting fundraising sales data for a college soccer team"
            ],
            a: 0,
            marks: 2
        },
        {
            id: 14,
            type: "MCQ2",
            q: "Which two concepts are commonly associated with artificial intelligence (AI) in data analytics? (Choose 2)",
            options: [
                "Cost-Benefit Analysis",
                "Stakeholder Mapping",
                "Automation",
                "Machine Learning"
            ],
            a: [2, 3],
            marks: 2
        },
        {
            id: 15,
            type: "MCQ2",
            q: "For which two reasons is it risky to make generalizations from limited sample data? (Choose 2)",
            options: [
                "Limited data samples are easier to collect",
                "A limited sample may not represent a larger population",
                "Findings from a smaller sample size may not be as precise",
                "Analyzing data from a smaller sample size is faster"
            ],
            a: [1, 2],
            marks: 2
        },
        {
            id: 16,
            type: "MCQ",
            q: "You believe playing video games increases the chance of a man getting a heart attack. In your research you notice equal evidence favouring your hypothesis and opposed to it. You tried hours trying to identify the problems with the evidence opposed to your hypothesis, but readily accept the evidence in favor.<br><br>Which type of bias are you demonstrating?",
            options: [
                "Motivated Reasoning",
                "Confirmation Bias",
                "Anchoring Bias",
                "Sampling Bias"
            ],
            a: 1,
            marks: 2
        },
        {
            id: 17,
            type: "MCQ",
            q: "You conduct a study to identify how much people exercise daily. You recruit all the study participants at the gyms.<br><br>Which type of bias are you demonstrating?",
            options: [
                "Anchoring Bias",
                "Confirmation Bias",
                "Motivated Bias",
                "Sampling Bias"
            ],
            a: 3,
            marks: 2
        },
        {
            id: 18,
            type: "MCQ2",
            q: "For which two reasons is it risky to make generalizations from limited sample data? (Choose 2)",
            options: [
                "Findings from a smaller sample size may not be as precise",
                "Analyzing data from a smaller sample size is faster",
                "A limited sample may not represent a larger population",
                "Limited data samples are easier to collect"
            ],
            a: [0, 2],
            marks: 2
        },
        {
            id: 19,
            type: "MCQ",
            q: "In which scenario will artificial intelligence (AI) provide the greatest benefit?",
            options: [
                "Interpreting fundraising sales data for a college team",
                "Recording daily sales for three stores owned by one franchise owner",
                "Determining the statistical mean, median, mode, and standard deviation of the grades for a class",
                "Predicting maintenance requirements for an international rental car company's fleet vehicles"
            ],
            a: 3,
            marks: 2
        },
        {
            id: 20,
            type: "MCQ2",
            q: "Each month, you need to automatically transform the data from two XML documents into a single flat file with columns and rows that Excel can open and interpret. The document names and structure remain constant. You know the relationships between the two XML documents.<br><br>Which two resources can you use? (Choose 2)<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
            options: [
                "Python",
                "Microsoft Word",
                "Power Query for Excel (M)",
                "JSON"
            ],
            a: [0, 2],
            marks: 2
        }
    ],
    "data4": [
    ],
    "data_mod4": [
        {
            "id": 1,
            "marks": 2,
            "type": "MCQ",
            "q": "You are responsible for e-commerce sales at your company. You need to present the quarterly data shown in the table to upper management using the most accurate unbiased visualization.<br><br>Which visualization should you choose? Select the correct visualization in the answer area.",
            "img": "quarterly_sales_table.png",
            "optionImages": [
                "v3_q21_opt1.png",
                "v3_q21_opt2.png",
                "v3_q21_opt3.png",
                "v3_q21_opt4.png"
            ],
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "a": 0
        },
        {
            "id": 2,
            "marks": 2,
            "type": "MCQ",
            "q": "For which scenario should you use a line chart to represent the data?",
            "options": [
                "The weekly average stock price during a one-year period",
                "The proportion of yes and no answer to a survey question",
                "The binned distribution for the height of different students",
                "The maximum, minimum, and average value for a set of data"
            ],
            "a": 0
        },
        {
            "id": 3,
            "marks": 2,
            "type": "MCQ",
            "q": "A college shows you the chart below to indicate that group A has performed significantly better than group B on a recent assignment. You don't know the sample size and the result of the statistical testing.<br><br>Which chart element creates the impression of a significant score difference?",
            "img": "group_comparison_3d_bias.png",
            "options": [
                "The X-axis unit of Measurement",
                "The Y-Axis unit of measurement",
                "The Z-Axis Unit of Measurement",
                "The Color differentiation"
            ],
            "a": 1
        },
        {
            "id": 4,
            "marks": 2,
            "type": "MCQ",
            "q": "Which visualization type is commonly used to display the distribution of a continuous variable, with variable values on the x-axis and corresponding frequencies on the y-axis?<br><br>Select the correct visualization type in the answer area.",
            "optionImages": [
                "v3_q13_opt1.png",
                "v3_q13_opt2.png",
                "v3_q13_opt3.png",
                "v3_q13_opt4.png"
            ],
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "a": 2
        },
        {
            "id": 5,
            "marks": 2,
            "type": "MCQ",
            "q": "What is the direction of correlation between variable X and variable Y?",
            "img": "correlation_direction.png",
            "options": ["Positive", "Negative", "Zero"],
            "a": 0
        },
        {
            "id": 6,
            "marks": 2,
            "type": "TF",
            "q": "You are analyzing statistics for online and in-store purchases with data collected over the past year. Data collected includes surveys from 300 instore customers and 300 online customers.<br><br>Based on the data visualization below, identify which statements about customer purchases over the last year are correct and which statements are incorrect. Select <strong>True</strong> if the statement is correct or <strong>False</strong> if the statement is incorrect.<br><br><span style='font-size:15px; font-style:italic;'>Note: You will receive partial credit for each correct selection.</span>",
            "img": "purchase_stats_comparison.png",
            "options": [
                "In-store customers spent more money than online customers.",
                "Online customers have a larger variance in how much they spend.",
                "The difference between the largest amount spent and the smallest amount spent is higher for in-store customers.",
                "The amount spent the most often is the same for online and in-store customers."
            ],
            "a": [false, true, false, true]
        },
        {
            "id": 7,
            "marks": 2,
            "type": "MCQ",
            "q": "An analyst claims the visualization implies the variable X causes variable Y. Is the analyst correct in the assertion?",
            "img": "correlation_direction.png",
            "options": ["Yes", "No"],
            "a": 1
        },
        {
            "id": 8,
            "marks": 2,
            "type": "MCQ",
            "q": "Which visualization type is commonly used to display the distribution of a continuous variable, with variable values on the x-axis and corresponding frequencies on the Y axis?<br><br>Select the correct visualization type in the answer area.",
            "optionImages": [
                "v3_q1_optA.png",
                "v3_q1_optB.png",
                "v3_q1_optC.png",
                "v3_q1_optD.png"
            ],
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "a": 2
        },
        {
            "id": 9,
            "marks": 2,
            "type": "MCQ2",
            "q": "Which two chart types should you use to rank values in ascending or descending order? (Choose 2)<br><br><span style='font-size:15px; font-style:italic;'>Note: You will receive partial credit for each correct selection.</span>",
            "options": [
                "Bar chart",
                "Column chart",
                "Line chart",
                "Bubble chart"
            ],
            "a": [0, 1]
        },
        {
            "id": 10,
            "marks": 2,
            "type": "MCQ",
            "q": "You want to show a friend your monthly budget breakdown to prove that most of your expenditure is food costs. You create a table that shows the flow of money as it moves one budget category to the next.<br><br>Which visualization type should you use to display your analysis based on the table shown?",
            "img": "budget_flow_table.png",
            "options": [
                "Time Series Chart",
                "Correlation Chart",
                "Sankey Chart",
                "Classification Chart"
            ],
            "a": 2
        },
        {
            "id": 11,
            "marks": 2,
            "type": "MCQ",
            "q": "You need to compare three (3) values of each data point in a series which data type should you use?",
            "options": [
                "Bubble chart",
                "Area chart",
                "Scatter chart",
                "Waterfall chart"
            ],
            "a": 0
        },
        {
            "id": 12,
            "marks": 2,
            "type": "MCQ",
            "q": "You create the column chart below. which shows sales for different years. Management asks for a way to see demographic information associated with the individual sales records for each year<br><br>You decide to create tables for each year that show the demographic information for the sales in that year. When someone clicks associated table will open.<br><br>Which reporting technique does this represent?",
            "img": "sales_by_year_column.png",
            "options": [
                "Disaggregating",
                "Unpivoting",
                "Pivoting",
                "Distributing"
            ],
            "a": 0
        },
        {
            "id": 13,
            "marks": 2,
            "type": "MCQ",
            "q": "You work for a recreational sports company. The table shows the company's recreational vehicle sales. You need to show how each vehicle type contributes to the company's total sales.<br><br>Which visualization should you use?<br>Select the correct visualization in the answer area.",
            "img": "vehicle_sales_table.png",
            "optionImages": [
                "recreational_pie_chart.png",
                "recreational_combo_chart.png",
                "recreational_bar_chart.png",
                "recreational_scatter_plot.png"
            ],
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "a": 0
        },
        {
            "id": 14,
            "marks": 2,
            "type": "MCQ",
            "q": "You want to show a friend your monthly budget breakdown to prove that most of your expenditure is food costs. You create a table that shows the flow of money as it moves one budget category to the next.<br><br>Which visualization type should you use to display your analysis based on the table shown?",
            "img": "budget_sankey_table.png",
            "options": [
                "Time Series Chart",
                "Classification tree",
                "Correlation matrix",
                "Sankey Diagram"
            ],
            "a": 3
        },
        {
            "id": 15,
            "marks": 2,
            "type": "MCQ",
            "q": "The visualization below displays sales data for two salespeople. A conclusion indicates that Salesperson 1 has a higher lead to sale rate than salesperson 2.<br>(A lead to sales rate is the number of actual sales divided by the number of attempted sales)<br><br>You need to determine the accuracy of this conclusion.<br>What should you conclude?",
            "img": "sales_lead_comparison.png",
            "options": [
                "The conclusion is accurate",
                "The conclusion is inaccurate because the visualization is missing sales and lead data",
                "The conclusion is inaccurate because the visualization uses size manipulation",
                "The conclusion is inaccurate because the visualization uses scale manipulation"
            ],
            "a": 1
        },
        {
            "id": 16,
            "marks": 2,
            "type": "MATRIX",
            "q": "The visualization and the data table depict housing prices in a region *<br>for each statement about the visualization, select True or False<br>Note:- you will receive partial credit for each correct selection",
            "img": "housing_prices_wide.png",
            "labels": ["True", "False"],
            "options": [
                "The visualization accurately depict the housing prices shown in the table",
                "The scaling of the graph is misleading",
                "An increase of $25000 occurs Each yea"
            ],
            "a": {
                "The visualization accurately depict the housing prices shown in the table": "True",
                "The scaling of the graph is misleading": "False",
                "An increase of $25000 occurs Each yea": "False"
            }
        },
        {
            "id": 17,
            "marks": 2,
            "type": "MCQ",
            "q": "A colleague shows you the chart below to indicate that Group A has performed significantly better than Group B on a recent assignment. You do not know the sample size or the results of statistical testing. Which chart element creates the impression Of a significant score difference?",
            "img": "q19_misleading_chart.png",
            "options": [
                "The x-axis units of measurement",
                "The y-axis units of measurement",
                "The z-axis units of measurement",
                "The color differentiation"
            ],
            "a": 1
        },
        {
            "id": 18,
            "marks": 2,
            "type": "MCQ",
            "q": "Which correlation range most likely describe relationship between the variable X and Y",
            "img": "scatter_correlation_v2.png",
            "options": [
                "No correlation(r=0.00)",
                "Some correlation(0.00<r<0.99)",
                "Perfect correlation(r=1.00)"
            ],
            "a": 1
        },
        {
            "id": 19,
            "marks": 2,
            "type": "MCQ",
            "q": "You are given a data set displaying the time of day and number of minutes customers waited in line for service. You need to remove bias from the results eliminating outliers. Which visualization illustrates outliers in your dataset? Select the correct Visualization in the answer area",
            "options": [
                "Option 1",
                "Option 2",
                "Option 3",
                "Option 4"
            ],
            "optionImages": [
                "outlier_line_chart.png",
                "outlier_error_bar.png",
                "outlier_grouped_bar.png",
                "outlier_scatter_plot.png"
            ],
            "a": 3
        },
        {
            "id": 20,
            "marks": 2,
            "type": "MCQ",
            "q": "A group of students asked about their favorite flavor of ice cream the pie chart below illustrate the proportion of each response. What can you conclude from the visualization about below about ice cream preference for this group of students?",
            "img": "ice_cream_preference_chart.png",
            "options": [
                "The fewest students chose strawberry",
                "The most students chose vanilla",
                "The most students chose chocolate",
                "Fewest students chose chocolate"
            ],
            "a": 2
        }
    ],
    "data_mod5": [
    ]
};
