var quizData = {
    "1": [
        { id: 1, type: "MTF", q: "You are reviewing several Python expressions and must determine the data type each expression evaluates to.<br>Move the appropriate data type from the list on the left to the correct expression on the right.<br>You may use each data type once, more than once, or not at all.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["type(25 // 4)", "type(25 / 4)", "type(\"25\")", "type(25 > 4)"], labels: ["int", "float", "str", "bool"], a: { "type(25 // 4)": "int", "type(25 / 4)": "float", "type(\"25\")": "str", "type(25 > 4)": "bool" } },
        { id: 2, type: "MCQ", q: "You are evaluating the following expression:<br><br>What is the value of result?<br><span style='font-size: 15px; font-style: italic;'>Select the correct answer.</span>", code: "result = 5 + 3 * 2 ** 2", options: ["64", "17", "29", "19"], a: 1 },
        { id: 3, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "a = [10, 20, 30]\nb = [10, 20, 30]\nc = a", options: ["a == b evaluates to True.", "a is b evaluates to True.", "a is c evaluates to True.", "b is not c evaluates to True."], a: [true, false, true, true] },
        { id: 4, type: "DD", q: "You are developing a program that manages a list of product prices. The program must: • Add a new price (150) • Sort the list • Reverse the list <br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "prices = [300, 200, 400]\n# Add new price\n[b1]\n# Sort prices\n[b2]\n# Reverse prices\n[b3]", options: ["prices.append(150)", "prices.sort()", "prices.reverse()", "prices.add(150)", "prices.sorted()"], a: ["prices.append(150)", "prices.sort()", "prices.reverse()"] },
        { id: 5, type: "SHORT", q: "Evaluate the following expression:<br><br>What value is printed?<br><span style='font-size: 15px; font-style: italic;'>Enter the number as an integer.</span>", code: "value = (10 % 4 * 3) + 2 ** 2\nprint(value)", a: "10" },
        { id: 6, type: "MTF", q: "You are working with the following string:<br><br>Match each slicing expression to its result.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", code: "word = \"programming\"", options: ["word[:4]", "word[3:7]", "word[7:]"], labels: ["prog", "gram", "ming", "program"], a: { "word[:4]": "prog", "word[3:7]": "gram", "word[7:]": "ming" } },
        { id: 7, type: "MCQ", q: "You are evaluating the following code:<br><br>What is printed?", code: "nums = [5, 10, 15, 20]\nprint(10 in nums)", options: ["True", "False", "10", "Error"], a: 0 },
        { id: 8, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "x = -5\ny = +x\nz = not (x > 0)", options: ["y will store -5.", "z will store True.", "The unary + operator changes the value of x.", "The not operator returns a boolean value."], a: [true, true, false, true] },
        { id: 9, type: "MCQ", q: "You are reviewing the following code:<br><br>What happens when this code executes?", code: "data = [10, 20, 30]\nprint(data[3])", options: ["30 is printed", "None is printed", "IndexError occurs", "0 is printed"], a: 2 },
        { id: 10, type: "MCQ2", q: "You are designing a condition that must evaluate to True only if: • x is greater than 5 AND • y is less than 10 <br><br>Which two expressions meet the requirement?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)<br>Note: You will receive partial credit for each correct answer.</span>", options: ["x > 5 and y < 10", "x > 5 or y < 10", "(x > 5) and (y < 10)", "x >= 5 and y <= 10"], a: [0, 2] }
    ],
    "2": [
        { id: 1, type: "MCQ", q: "You are writing a program that determines whether a number is positive, negative, or zero. Review the following code:<br><br>What is printed?", code: "num = -5\nif num > 0:\n    print(\"Positive\")\nelif num < 0:\n    print(\"Negative\")\nelse:\n    print(\"Zero\")", options: ["Positive", "Negative", "Zero", "Nothing"], a: 1 },
        { id: 2, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "score = 85\nif score >= 50:\n    if score >= 75:\n        print(\"Distinction\")\n    else:\n        print(\"Pass\")\nelse:\n    print(\"Fail\")", options: ["If score = 60, the output will be \"Pass\".", "If score = 40, the output will be \"Fail\".", "If score = 90, the output will be \"Distinction\".", "If score = 75, the output will be \"Pass\"."], a: [true, true, true, false] },
        { id: 3, type: "SHORT", q: "Review the following code:<br><br>How many lines of output are printed?<br><span style='font-size: 15px; font-style: italic;'>Enter the number as an integer.</span>", code: "count = 1\nwhile count <= 4:\n    print(count)\n    count += 1", a: "4" },
        { id: 4, type: "DD", q: "You are building a program that searches for a value in a list. The program must: • Loop through numbers • Stop immediately once the value 7 is found <br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "numbers = [2, 4, 6, 7, 8]\nfor n in numbers:\n    if n == 7:\n        print(\"Found\")\n        [b1]", options: ["break", "continue", "pass"], a: ["break"] },
        { id: 5, type: "MCQ", q: "Review the following code:<br><br>What is printed?", code: "for i in range(1, 6):\n    if i == 3:\n        continue\n    print(i)", options: ["1 2 3 4 5", "1 2 4 5", "3", "1 2 3"], a: 1 },
        { id: 6, type: "MTF", q: "You are analyzing different range() expressions.<br>Match each expression with the correct sequence produced.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["range(4)", "range(1,5)", "range(0,6,2)"], labels: ["0 1 2 3", "1 2 3 4", "0 2 4"], a: { "range(4)": "0 1 2 3", "range(1,5)": "1 2 3 4", "range(0,6,2)": "0 2 4" } },
        { id: 7, type: "MCQ2", q: "You are designing a login validation rule. The program must allow access only if: • age is 18 or older AND • has_id is True <br><br>Which two expressions meet the requirement?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", options: ["age >= 18 and has_id", "age > 18 or has_id", "(age >= 18) and (has_id == True)", "age >= 18 or has_id == True"], a: [0, 2] },
        { id: 8, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "for i in range(3):\n    print(i)\nelse:\n    print(\"Done\")", options: ["The loop prints 0 1 2.", "\"Done\" is printed after the loop completes normally.", "The else block executes only if break is used.", "The else block is optional in a for loop."], a: [true, true, false, true] },
        { id: 9, type: "MCQ", q: "You are reviewing the following code:<br><br>What happens when this code runs?", code: "x = 1\nwhile x < 5:\n    print(x)", options: ["Prints 1 2 3 4", "Prints 1 only", "Infinite loop", "Syntax Error"], a: 2 },
        { id: 10, type: "SHORT", q: "Review the following code:<br><br>How many lines of output are printed?<br><span style='font-size: 15px; font-style: italic;'>Enter the number as an integer.</span>", code: "for i in range(2):\n    for j in range(2):\n        print(i, j)", a: "4" }
    ],
    "3": [
        { id: 1, type: "MCQ", q: "You are creating a console-based application that asks a user to enter their age.<br>Which statement correctly reads input from the console and stores it in a variable named age?", options: ["age = console.read()", "age = input()", "read(age)", "age.input()"], a: 1 },
        { id: 2, type: "DD", q: "You are writing a program that must: • Accept a number from the user • Convert it to an integer • Multiply it by 2 <br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "num = [b1](\"Enter a number: \")\nresult = num * 2\nprint(result)", options: ["int(input)", "int(input())", "input(int)", "float(input())"], a: ["int(input())"] },
        { id: 3, type: "MCQ2", q: "You are writing a billing program. The program must: • Display customer name • Display total amount • Format output as: Name: John, Total: 500 <br><br>Which two code segments correctly meet the requirement?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", options: ["print(\"Name:\", name, \"Total:\", total)", "print(f\"Name: {name}, Total: {total}\")", "print(\"Name: {0}, Total: {1}\".format(name, total))", "print(name + total)"], a: [1, 2] },
        { id: 4, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "f = open(\"data.txt\", \"w\")\nf.write(\"Hello\")\nf.close()", options: ["If the file does not exist, it will be created.", "If the file exists, its previous contents will be overwritten.", "The file must be manually closed.", "\"w\" mode allows reading the file."], a: [true, true, true, false] },
        { id: 5, type: "MCQ", q: "You are writing a logging program.<br>Which file mode allows you to add new content to the end of a file without deleting existing content?", options: ["\"r\"", "\"w\"", "\"a\"", "\"rw\""], a: 2 },
        { id: 6, type: "DD", q: "You are developing a program that: • Opens a file in read mode • Reads all contents • Prints the contents <br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "file = open(\"info.txt\", \"[b1]\")\ndata = file.[b2]()\nprint(data)\nfile.close()", options: [["r", "w", "a"], ["read", "write", "append"]], a: ["r", "read"] },
        { id: 7, type: "MCQ", q: "You are reviewing the following code:<br><br>What is the advantage of using with in this context?", code: "with open(\"data.txt\", \"r\") as f:\n    content = f.read()", options: ["It makes the file read faster", "It automatically closes the file", "It prevents file overwriting", "It allows writing only"], a: 1 },
        { id: 8, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "import os\nif os.path.exists(\"report.txt\"):\n    print(\"File exists\")", options: ["The os module must be imported before using os.path.exists().", "The function returns True if the file exists.", "os.path.exists() deletes the file if found.", "The function can check for directories as well."], a: [true, true, false, true] },
        { id: 9, type: "SHORT", q: "Review the following script:<br>The program is executed using:<br><code>python script.py Red Blue Green</code><br><br>What is printed?", code: "import sys\nprint(sys.argv[1])", a: "Red" },
        { id: 10, type: "MCQ2", q: "You are designing a program that opens a file. The program must: • Avoid crashing if the file does not exist • Handle the error gracefully <br><br>Which two approaches meet the requirement?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", code: "A.\ntry:\n    f = open(\"data.txt\", \"r\")\nexcept FileNotFoundError:\n    print(\"File not found\")\n\nB.\nopen(\"data.txt\")\n\nC.\nimport os\nif os.path.exists(\"data.txt\"):\n    f = open(\"data.txt\", \"r\")\n\nD.\nf = open(\"data.txt\", \"w\")", options: ["A", "B", "C", "D"], a: [0, 2] }
    ],
    "4": [
        { id: 1, type: "MCQ", q: "<strong>Objective:</strong> Design a utility to calculate the area of floor plans for an architectural firm.<br><br>Which syntax correctly defines the function to achieve this?", options: ["function area(length, width):", "def area(length, width):", "define area(length, width):", "area(length, width):"], a: 1 },
        { id: 2, type: "SHORT", q: "<strong>Logic Check:</strong> A basic arithmetic helper is required in an internal math module.<br><br>What is the output of the following function?<br><span style='font-size: 15px; font-style: italic;'>Enter the number as an integer.</span>", code: "def multiply(a, b):\n    return a * b\n\nresult = multiply(4, 5)\nprint(result)", a: "20" },
        { id: 3, type: "TF", q: "<strong>Code Review:</strong> Evaluate a greeting routine within an automated customer support bot.<br><br>Select True or False for each statement regarding the <code>greet</code> implementation below.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "def greet(name, message=\"Hello\"):\n    print(message, name)", options: ["Calling greet(\"John\") prints \"Hello John\".", "Calling greet(\"John\", \"Hi\") prints \"Hi John\".", "Default parameters must always be the first parameter.", "The function can be called using keyword arguments."], a: [true, true, false, true] },
        { id: 4, type: "DD", q: "<strong>Task:</strong> Finalize a tax calculation utility by completing the function call below for a price of 100 and a tax of 20.<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "def calculate_price(price, tax):\n    return price + tax\n\n# Answer Area\ntotal = calculate_price([b1])", options: ["100, 20", "price=100, tax=20", "tax=20, price=100", "20, 100"], a: ["price=100, tax=20"] },
        { id: 5, type: "MCQ", q: "<strong>Scope Analysis:</strong> Investigate a variable-lifecycle issue in a data processing routine.<br><br>What is the value of 'x' when this code completes?", code: "x = 10\ndef update():\n    x = 5\nupdate()\nprint(x)", options: ["5", "10", "None", "Error"], a: 1 },
        { id: 6, type: "DD", q: "<strong>Requirement:</strong> Standardize the documentation for an internal math library to ensure long-term maintainability.<br><br>Select the correct docstring format.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "def add(a, b):\n    [b1]\n    return a + b", options: ["\"\"\"This function adds two numbers\"\"\"", "// This function adds two numbers", "This function adds two numbers", "/* This function adds two numbers */"], a: ["\"\"\"This function adds two numbers\"\"\""] },
        { id: 7, type: "TF", q: "<strong>Validation Trace:</strong> Analyze the behavior of a user-input parity filter within a registration form.<br><br>Determine the truth of each operational statement for the <code>check_even</code> function.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "def check_even(num):\n    if num % 2 == 0:\n        return \"Even\"\n    return \"Odd\"", options: ["The function always returns a value.", "If num = 4, the function returns \"Even\".", "If num = 3, the function returns \"Odd\".", "Both return statements will execute for the same input."], a: [true, true, true, false] },
        { id: 8, type: "MCQ", q: "<strong>Diagnostics:</strong> Inspect a simple display function for unexpected return behaviors.<br><br>What result is assigned after this code executes?", code: "def show():\n    print(\"Hello\")\nresult = show()\nprint(result)", options: ["Hello", "Hello None", "None", "Error"], a: 2 },
        { id: 9, type: "MCQ2", q: "<strong>Architecture:</strong> Implement an aggregation tool capable of processing a dynamic list of price entries.<br><br>Which two function definitions meet this flexibility requirement?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", options: ["def total(*numbers):", "def total(numbers):", "def total(**numbers):", "def total(a, b, *numbers):"], a: [0, 3] },
        { id: 10, type: "SHORT", q: "<strong>Finalization:</strong> Verify the discount-logic integrity for a premium user loyalty formula.<br><br>Calculate the final output for a price of 120.<br><span style='font-size: 15px; font-style: italic;'>Enter the value as a number.</span>", code: "def calculate_discount(price):\n    if price > 100:\n        return price * 0.9\n    return price\nprint(calculate_discount(120))", a: "108.0" }
    ],
    "5": [
        { id: 1, type: "MCQ", q: "You are writing a program that converts user input to an integer.<br>Which code correctly handles invalid input without crashing?", code: "A.\nx = int(input())\n\nB.\ntry:\n    x = int(input())\nexcept:\n    print(\"Invalid input\")\n\nC.\nhandle:\n    x = int(input())\n\nD.\ncatch ValueError:\n    print(\"Invalid\")", options: ["A", "B", "C", "D"], a: 1 },
        { id: 2, type: "DD", q: "You are writing a program that divides two numbers entered by the user. The program must: • Catch division by zero errors • Display \"Cannot divide by zero\" <br><br>Complete the code by selecting the correct exception type.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "try:\n    result = 10 / 0\nexcept [b1]:\n    print(\"Cannot divide by zero\")", options: ["ValueError", "ZeroDivisionError", "TypeError", "FileNotFoundError"], a: ["ZeroDivisionError"] },
        { id: 3, type: "TF", q: "<strong>Data Engineering:</strong> You are troubleshooting a data ingestion script. The script must safely attempt to open a required data file and guarantee that cleanup operations run regardless of success or failure.<br><br>Analyze the following code block. For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "try:\n    f = open(\"data.txt\")\nexcept FileNotFoundError:\n    print(\"File not found\")\nfinally:\n    print(\"Execution completed\")", options: ["The finally block always executes.", "The finally block runs only if an exception occurs.", "The finally block runs even if no exception occurs.", "The except block runs if the file does not exist."], a: [true, false, true, true] },
        { id: 4, type: "MTF", q: "You are designing a program that handles different types of exceptions.<br>Match each exception with the scenario that causes it.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["Dividing a number by zero", "Converting \"abc\" to int", "Adding string and integer"], labels: ["ValueError", "TypeError", "ZeroDivisionError"], a: { "Dividing a number by zero": "ZeroDivisionError", "Converting \"abc\" to int": "ValueError", "Adding string and integer": "TypeError" } },
        { id: 5, type: "MCQ", q: "You are writing a function that must: • Raise an error if the age entered is negative. <br><br>Which code correctly raises an exception?", code: "A.\nif age < 0:\n    print(\"Invalid age\")\n\nB.\nif age < 0:\n    raise ValueError(\"Invalid age\")\n\nC.\nif age < 0:\n    except ValueError\n\nD.\nif age < 0:\n    error(\"Invalid age\")", options: ["A", "B", "C", "D"], a: 1 },
        { id: 6, type: "TF", q: "<strong>Inventory Management:</strong> You are testing an e-commerce platform's checkout system. The system must verify that sufficient stock exists before processing an order.<br><br>Analyze the behavior of the following assertion check where <code>x</code> represents the current stock level of an item. For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "x = 10\nassert x > 5", options: ["The assertion passes.", "An AssertionError is raised.", "If x = 3, the assertion would fail.", "assert is commonly used in testing."], a: [true, false, true, true] },
        { id: 7, type: "DD", q: "You are writing a unit test to verify that two values are equal.<br>Complete the test method by selecting the correct assertion method.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "import unittest\nclass TestMath(unittest.TestCase):\n    def test_add(self):\n        self.[b1](5, 2 + 3)", options: ["assertEqual", "assertTrue", "assertIs", "assertIn"], a: ["assertEqual"] },
        { id: 8, type: "MCQ", q: "<strong>Financial Analytics:</strong> You are reviewing a risk assessment module. The <code>divide</code> function calculates a financial ratio based on user-submitted data.<br><br>What is a potential issue with this implementation?", code: "def divide(a, b):\n    try:\n        return a / b\n    except:\n        return 0", options: ["It handles only ZeroDivisionError", "It hides all types of errors", "It causes syntax error", "It does not handle division"], a: 1 },
        { id: 9, type: "MCQ2", q: "You are designing a program that opens a file safely. The program must: • Prevent crash if file does not exist • Display an error message <br><br>Which two code segments meet the requirement? (Choose 2.)", code: "A.\ntry:\n    f = open(\"data.txt\", \"r\")\nexcept FileNotFoundError:\n    print(\"File not found\")\n\nB.\nf = open(\"data.txt\", \"r\")\n\nC.\nimport os\nif os.path.exists(\"data.txt\"):\n    f = open(\"data.txt\", \"r\")\nelse:\n    print(\"File not found\")\n\nD.\nf = open(\"data.txt\", \"w\")", options: ["A", "B", "C", "D"], a: [0, 2] },
        { id: 10, type: "SHORT", q: "Review the following code:<br><br>What is missing from this code?", code: "try\n    x = int(\"abc\")\nexcept ValueError\n    print(\"Error\")", a: ":" }
    ],
    "6": [
        { id: 1, type: "MCQ", q: "You are writing a program that uses functions from the random module.<br>Which statement correctly imports the module?", options: ["include random", "using random", "import random", "random.import()"], a: 2 },
        { id: 2, type: "DD", q: "You are developing a game that must generate a random number between 1 and 10 (inclusive).<br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "import random\nnumber = random.[b1](1, 10)\nprint(number)", options: ["randint", "randrange", "random", "choice"], a: ["randint"] },
        { id: 3, type: "MCQ", q: "Review the following code:<br><br>Which values can be printed?", code: "import random\nprint(random.randrange(0, 10, 2))", options: ["1, 3, 5, 7, 9", "0, 2, 4, 6, 8", "2, 4, 6, 8, 10", "0 to 10 inclusive"], a: 1 },
        { id: 4, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "import os\nif os.path.exists(\"data.txt\"):\n    print(\"File exists\")", options: ["os must be imported before using os.path.exists().", "os.path.exists() returns a boolean value.", "os.path.exists() deletes the file after checking.", "This function can check for directories as well."], a: [true, true, false, true] },
        { id: 5, type: "DD", q: "You are writing a script that must read the first command-line argument provided by the user.<br>Complete the code by selecting the correct option.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "import sys\nvalue = sys.argv[[b1]]\nprint(value)", options: ["0", "1", "2", "-1"], a: ["1"] },
        { id: 6, type: "MCQ", q: "You are writing a program that must calculate the square root of a number.<br>Which code correctly performs this operation?", code: "A.\nimport math\nprint(math.sqrt(16))\n\nB.\nimport math\nprint(math.square(16))\n\nC.\nsqrt(16)\n\nD.\nmath.root(16)", options: ["A", "B", "C", "D"], a: 0 },
        { id: 7, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "import random as r\nprint(r.randint(1,5))", options: ["random is imported with alias r.", "r.randint(1,5) generates a random integer.", "The alias changes how the module works internally.", "Using an alias is optional."], a: [true, true, false, true] },
        { id: 8, type: "MCQ2", q: "You are building a system utility script. The script must: • Check whether a file exists • Generate a random number <br><br>Which two modules must be imported? (Choose 2.)", options: ["sys", "os", "random", "math"], a: [1, 2] },
        { id: 9, type: "MCQ", q: "You are writing a program that lists all files in the current directory.<br>Which code correctly performs this task?", code: "A.\nimport os\nprint(os.listdir())\n\nB.\nprint(list.files())\n\nC.\nimport sys\nprint(sys.files())\n\nD.\nos.files()", options: ["A", "B", "C", "D"], a: 0 },
        { id: 10, type: "SHORT", q: "Review the following code:<br><br>What is printed?", code: "import random\nimport sys\nnumbers = [10, 20, 30, 40]\nindex = random.randint(0, 3)\nprint(numbers[index])", a: "4" }
    ],
    "mock1": [
        { id: 1, type: "DD", q: "<strong>Unit Testing:</strong> You are developing a Python application that requires unit testing. You need to:<br>• Import the correct module.<br>• Verify that a value is an instance of a specific class.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "[b1] unittest\nclass TestExample(unittest.TestCase):\n    def test_instance(self):\n        self.[b2](5, int)\n\nif __name__ == \"__main__\":\n    unittest.main()", options: [["define", "import", "include", "using"], ["assertEqual", "assertTrue", "assertIsInstance", "assertIn"]], a: ["import", "assertIsInstance"] },
        { id: 2, type: "MCQ", q: "<strong>Code Documentation:</strong> You are part of a development team maintaining a large Python project. You need to add notes in your code so other developers can understand its purpose and logic.<br><br>What is the correct way to add a single-line comment in Python?", options: ["Use /* comment */", "Use <!-- comment -->", "Use # comment", "Use // comment"], a: 2 },
        { id: 3, type: "DD", q: "<strong>Random Assignment Logic:</strong> You are writing a program that assigns a random room number. The program must:<br>• Ensure that the room number is not already assigned.<br>• Generate a new random number if it is already in use.<br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "import random\nroomsAssigned = []\nroom_number = 1\nwhile room_number in roomsAssigned:\n    [b1]\nroomsAssigned.append(room_number)", options: ["room_number = random.randint(1, 50)", "room_number += 1", "random.choice(room_number)"], a: ["room_number = random.randint(1, 50)"] },
        { id: 4, type: "DD", q: "<strong>File Creation and Writing:</strong> A company requires a program that:<br>• Opens a file named report.txt.<br>• Writes the text \"End of listing\" into the file.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "file = open(\"report.txt\", \"[b1]\")\nfile.[b2](\"End of listing\")\nfile.close()", options: [["r", "w", "a"], ["write", "read", "append"]], a: ["w", "write"] },
        { id: 5, type: "DD", q: "<strong>Exception Handling:</strong> You are writing a program that:<br>• Prompts the user for a number.<br>• Converts the input to an integer.<br>• Handles invalid input without crashing.<br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "while True:\n    try:\n        x = int(input(\"Enter a number: \"))\n        break\n    [b1] ValueError:\n        print(\"Invalid number.\")", options: ["except", "catch", "error", "handle"], a: ["except"] },
        { id: 6, type: "DD", q: "<strong>File Existence Check:</strong> You are developing a file-processing program. Before opening a file, the program must:<br>• Verify that the file exists.<br>• Read and display its contents if it exists.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "import os\nif [b1](\"data.txt\"):\n    file = open(\"data.txt\", \"r\")\n    print(file.[b2]())\n    file.close()", options: [["os.path.exists", "os.exists", "os.path.check"], ["read", "write", "open"]], a: ["os.path.exists", "read"] },
        { id: 7, type: "DND", q: "<strong>Prime Number Logic:</strong> You are building a program that prints all prime numbers between 2 and 20. The program must:<br>• Loop through numbers from 2 to 20.<br>• Determine whether each number is prime.<br>• Stop checking a number once a divisor is found.<br><br>Complete the code by moving the appropriate code segment into the correct location.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct placement.</span>", code: "for p in range(2, 21):\n    is_prime = True\n    for i in range(2, p):\n        if p % i == 0:\n            is_prime = False\n            [target1]\n    if is_prime:\n        print(p)", options: ["break", "continue", "pass", "elif"], a: ["break"] },
        { id: 8, type: "DD", q: "<strong>List Comparison:</strong> You are comparing two lists to determine whether they contain the same values in the same order.<br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "numList = [1, 2, 3]\nalphaList = [\"a\", \"b\", \"c\"]\nif [b1]:\n    print(\"Equal\")\nelse:\n    print(\"Not Equal\")", options: ["numList == alphaList", "numList is alphaList", "numList != alphaList", "numList in alphaList"], a: ["numList == alphaList"] },
        { id: 9, type: "MCQ", q: "<strong>input() Function:</strong> You are creating a console-based application. You use the following statement:<br><br>What does this statement do?", code: "data = input()", options: ["Creates an HTML input field", "Prompts the user to enter text in the console", "Displays system input devices", "Opens a message dialog"], a: 1 },
        { id: 10, type: "TF", q: "<strong>Function Logic:</strong> You are reviewing the following function.<br><br>For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "def grosspay(hours=40, rate=25, pieces=0, piecerate=0, salary=0):\n    if pieces > 0:\n        return pieces * piecerate\n    if salary > 0:\n        pass\n    if hours > 40:\n        overtime = (hours - 40) * (1.5 * rate)\n        return overtime + (40 * rate)\n    else:\n        return hours * rate", options: ["Calling grosspay() results in a syntax error.", "Calling grosspay(salary=50000) returns None.", "Calling grosspay(pieces=500, piecerate=4) returns 2000."], a: [false, false, true] },
        { id: 11, type: "DD", q: "<strong>Loop Until Exit:</strong> You are writing a program that repeatedly accepts user input. The program must:<br>• Prompt the user to enter a word.<br>• Display the number of characters in the word.<br>• Continue until the user enters \"QUIT\".<br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "word = input(\"Enter a word (or QUIT to exit): \")\n[b1] word != \"QUIT\":\n    print(len(word))\n    word = input(\"Enter a word (or QUIT to exit): \")", options: ["if", "for", "while"], a: ["while"] },
        { id: 12, type: "TF", q: "<strong>Comparison Logic:</strong> You are reviewing the following conditional statements.<br><br>For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "if num1 == num2:\n    print(\"Equal\")\nif num1 < num2:\n    print(\"Less\")\nif num1 > num2:\n    print(\"Greater\")\nif num2 == num1:\n    print(\"Same\")", options: ["The first print statement executes only when the values are equal.", "The second print statement executes only when num1 is less than num2.", "The third print statement executes only when num1 is greater than num2.", "The final condition is logically redundant."], a: [true, true, true, true] },
        { id: 13, type: "DD", q: "<strong>Counting Items in a List:</strong> You are developing a function that counts how many words in a list contain a specific letter.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "def count_letter(letter, word_list):\n    count = 0\n    for [b1]:\n        if [b2]:\n            count += 1\n    return count", options: [["word in word_list", "letter in word", "word_list in letter", "word == letter"], ["word in word_list", "letter in word", "word_list in letter", "word == letter"]], a: ["word in word_list", "letter in word"] },
        { id: 14, type: "DND", q: "<strong>Guessing Game:</strong> You are creating a guessing game. The program must:<br>• Generate a random number between 1 and 10.<br>• Allow the user up to three guesses.<br>• Stop immediately if the correct guess is entered.<br><br>Complete the code by moving the appropriate code segments into the correct locations.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct placement.</span>", code: "from random import randint\ntarget = randint(1, 10)\nchance = 1\n[target1]\n    guess = int(input(\"Guess: \"))\n    if guess == target:\n        print(\"Correct!\")\n        [target2]\n    [target3]", options: ["break", "chance += 1", "while chance <= 3:"], a: ["while chance <= 3:", "break", "chance += 1"] },
        { id: 15, type: "DD", q: "<strong>Admission Fee Calculation:</strong> You are developing a function to calculate admission fees. The program must:<br>• Assign a free rate for children under 5.<br>• Assign a discounted rate for students aged 5 to 17.<br>• Assign a higher rate for non-students aged 5 to 17.<br>• Assign a standard adult rate otherwise.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "elif age >= 5 and age <= 17 and not school:\n    rate = [b1]\nelse:\n    rate = [b2]", options: [["20", "50", "10"], ["20", "50", "10"]], a: ["20", "50"] },
        { id: 16, type: "MCQ", q: "<strong>Command-Line Arguments:</strong> You are reviewing the following script.<br>The program is executed using the following command:<br><code>python script.py Apple Banana Mango</code><br><br>What is the output?", code: "import sys\nprint(sys.argv[2])", options: ["script.py", "Apple", "Banana", "Mango"], a: 2 },
        { id: 17, type: "DD", q: "<strong>Reverse String Function:</strong> You are creating a function that reverses a string.<br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "def reverse_name(backward_name):\n    forward_name = \"\"\n    length = len(backward_name) - 1\n    while length >= 0:\n        forward_name += [b1]\n        length -= 1\n    return forward_name", options: ["backward_name[length]", "backward_name", "forward_name[length]"], a: ["backward_name[length]"] },
        { id: 18, type: "TF", q: "<strong>Comments and Execution:</strong> You are reviewing the following function.<br><br>For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "def calc_power(x, y):\n    comment = \"# return the value\"\n    return x ** y  # exponent", options: ["The string in line 2 is treated as a comment.", "The function returns x raised to the power y.", "The inline comment does not affect execution.", "Removing the comment changes the output."], a: [false, true, true, false] },
        { id: 19, type: "MCQ", q: "<strong>Operator Precedence:</strong> You are evaluating the following expression.<br><br>What is the value of answer?", code: "answer = (9 % 4 * 10) // 2 ** 3 + 4", options: ["5", "6", "4", "3"], a: 0 },
        { id: 20, type: "MCQ", q: "<strong>File Handling Error:</strong> You are reviewing the following function.<br><br>An error occurs when executing this code. What is the most likely cause?", code: "def read_file(file):\n    if os.path.isfile(file):\n        data = open(file, 'r')\n        for line in data:\n            print(line)", options: ["isfile requires two parameters", "os module is not imported", "The path must be absolute", "open requires a different mode"], a: 1 },
        { id: 21, type: "MCQ2", q: "<strong>Random Number Generation:</strong> You work on a team that is developing a game. You need to write code that generates a random number that meets the following requirements:<br>• The number must be a multiple of 5.<br>• The lowest number must be 5.<br>• The highest number must be 100.<br><br>Which two code segments meet the requirements?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", code: "A.\nfrom random import randint\nprint(randint(1, 20) * 5)\n\nB.\nfrom random import randint\nprint(randint(0, 20) * 5)\n\nC.\nfrom random import randrange\nprint(randrange(0, 100, 5))\n\nD.\nfrom random import randrange\nprint(randrange(5, 105, 5))", options: ["A", "B", "C", "D"], a: [0, 3] },
        { id: 22, type: "DD", q: "<strong>Digit Classification:</strong> You are writing a program to determine if a number entered by the user contains:<br>• One digit<br>• Two digits<br>• More than two digits<br><br>Complete the code by selecting the correct code segment from each drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "num = int(input(\"Enter a number with 1 or 2 digits: \"))\ndigits = \"0\"\nif [b1]:\n    digits = \"1\"\nelif [b2]:\n    digits = \"2\"\nelse:\n    digits = \">2\"\nprint(digits + \" digits.\")", options: [["num < 10", "len(str(num)) == 1", "num >= 100", "num >= 10 and num < 100"], ["num < 10", "len(str(num)) == 1", "num >= 100", "num >= 10 and num < 100"]], a: ["num < 10", "num >= 10 and num < 100"] },
        { id: 23, type: "MCQ", q: "<strong>Conditional Grade Logic:</strong> You write the following code to determine a student's final grade based on their current grade and class rank.<br><br>What value will print?", code: "grade = 76\nrank = 3\nif grade > 80 and rank >= 3:\n    grade += 10\nelif grade >= 70 and rank > 3:\n    grade += 5\nelse:\n    grade -= 5\nprint(grade)", options: ["71", "76", "81", "86"], a: 0 },
        { id: 24, type: "MTF", q: "<strong>Data Type Identification:</strong> You need to identify the data types of various expressions.<br>Move the appropriate data types from the list on the left to the correct type operations on the right.<br>You may use each data type once, more than once, or not at all.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["type(+1E10)", "type(5.0)", "type(\"True\")", "type(False)"], labels: ["int", "float", "str", "bool"], a: { "type(+1E10)": "float", "type(5.0)": "float", "type(\"True\")": "str", "type(False)": "bool" } },
        { id: 25, type: "MCQ2", q: "<strong>Function Definitions:</strong> A bicycle company is creating a program that allows customers to log the number of miles biked. The program will:<br>• Ask the user for their name.<br>• Ask how many miles they biked.<br>• Calculate calories burned.<br><br>You must define two required functions. Which two code segments should you use?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", code: "A.\ndef get_name():\n\nB.\ndef get_name(biker):\n\nC.\ndef get_name(name):\n\nD.\ndef calc_calories():\n\nE.\ndef calc_calories(miles, burn_rate):\n\nF.\ndef calc_calories(miles, calories_per_mile):", options: ["A", "B", "C", "D", "E", "F"], a: [0, 5] },
        { id: 26, type: "TF", q: "<strong>Exponent Function:</strong> Review the following code.<br><br>For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "def calc_power(a, b):\n    return a**b\n\nbase = input(\"Enter the number for the base: \")\nexponent = input(\"Enter the number for the exponent: \")\nresult = calc_power(base, exponent)\nprint(\"The result is \" + result)", options: ["The code will generate an error in the input lines.", "The function will correctly compute exponentiation.", "The print statement will generate an error."], a: [false, false, true] },
        { id: 27, type: "TF", q: "<strong>Try Statements:</strong> For each statement about <code>try</code> statements, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", options: ["A try statement can have one or more except clauses.", "A try statement can have a finally clause without an except clause.", "A try statement can have both except and finally clauses.", "A try statement can have more than one finally clause."], a: [true, true, true, false] },
        { id: 28, type: "TF", q: "<strong>File Handling Behavior:</strong> Review the following code segment.<br><br>For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "f = open(\"python.txt\", \"a\")\nf.write(\"This is a line of text.\")\nf.close()", options: ["A file named python.txt is created if it does not exist.", "The existing data in the file will be overwritten.", "The file can be opened again after this code runs."], a: [true, false, true] },
        { id: 29, type: "MCQ2", q: "<strong>Formatted Output:</strong> You are creating an eCommerce script that:<br>• Accepts item name and quantity.<br>• Outputs the data in comma-delimited format.<br>• Encloses strings in double quotes.<br>• Does not enclose numbers in quotes.<br><br>Which two code segments meet the requirements?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", code: "A.\nprint('\"' + item + '\",' + str(sales))\n\nB.\nprint('\"{0}\",{1}'.format(item, sales))\n\nC.\nprint(item + \",\" + sales)\n\nD.\nprint(f'\"{item}\",{sales}')", options: ["A", "B", "C", "D"], a: [1, 3] },
        { id: 30, type: "MCQ", q: "<strong>Expression Evaluation:</strong> Evaluate the following expression.<br><br>What is the result?", code: "value1 = 9\nvalue2 = 4\nanswer = (value1 % value2 * 10) / 2.0 ** 3.0 + value2\nprint(answer)", options: ["5.667", "5.25", "129", "Syntax Error"], a: 1 },
        { id: 31, type: "DND", q: "<strong>Operator Precedence:</strong> You are writing a Python application that includes multiple operations on the same line of code. You need to determine the correct order of operations.<br>Move the type of operation from the list on the left to the correct locations on the right, with the operation performed first at the top and the operation performed last at the bottom.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", code: "<div class='dnd-grid'><div>1st Operation:</div> [target1]<div>2nd Operation:</div> [target2]<div>3rd Operation:</div> [target3]<div>4th Operation:</div> [target4]<div>5th Operation:</div> [target5]<div>6th Operation:</div> [target6]</div>", options: ["Addition and Subtraction", "And", "Exponents", "Multiplication and Division", "Parentheses", "Unary positive, negative, not"], a: ["Parentheses", "Exponents", "Unary positive, negative, not", "Multiplication and Division", "Addition and Subtraction", "And"] },
        { id: 32, type: "TF", q: "<strong>Function with Default Parameters:</strong> You are writing a function that increments the player score in a game. The function has the following requirements:<br>• If no value is specified for points, then points should start at 1.<br>• If bonus is True, then points must be doubled.<br><br>For each statement, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "01 def increment_score(score, bonus, points):\n02     if bonus == True:\n03         points = points * 2\n04     score = score + points\n05     return score\n06 points = 5\n07 score = 10\n08 new_score = increment_score(score, True, points)", options: ["To meet the requirements, you must change line 01 to: def increment_score(score, bonus, points = 1):", "If you do not change line 01 and the function is called with only two parameters, an error occurs.", "Line 03 will modify the value of the variable points declared at line 06."], a: [true, true, false] },
        { id: 33, type: "MTF", q: "<strong>String Slicing:</strong> You need to identify the results of performing slicing operations on the following sequence.<br>Move the appropriate results from the list on the left to the correct slicing operations on the right.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", code: "alph = \"abcdefghijklmnopqrstuvwxyz\"", options: ["alph[3:6]", "alph[:6]"], labels: ["def", "abcdef", "cde", "defg", "cdef", "abcde"], a: { "alph[3:6]": "def", "alph[:6]": "abcdef" } },
        { id: 34, type: "SHORT", q: "<strong>Loop Execution Analysis:</strong> Review the following code segment.<br><br>How many lines of output does the code print?<br><span style='font-size: 15px; font-style: italic;'>Enter the number as an integer.</span>", code: "product = 2\nn = 5\nwhile (n != 0):\n    product *= n\n    print(product)\n    n -= 1\n    if n == 3:\n        break", a: "2" },
        { id: 35, type: "DD", q: "<strong>Code Correction:</strong> You find errors while evaluating the following code.<br>You need to correct the code regarding the <code>while</code> loop statement and the <code>if</code> condition statement.<br><br>Evaluate the code and answer the questions by selecting the correct option from each drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "numbers = [0,1,2,3,4,5,6,7,8,9]\nindex = 0\n[b1]\n    print(numbers[index])\n    [b2]\n        break\n    else:\n        index += 1", options: [["while (index < 10)", "while (index < 10):", "while index < 10", "while index = 10:"], ["if numbers[index] == 6:", "if numbers[index] = 6:", "if numbers(index) == 6:", "if numbers(index) = 6"]], a: ["while (index < 10):", "if numbers[index] == 6:"] },
        { id: 36, type: "DD", q: "<strong>List Operations:</strong> You are developing a program that manages a list of student scores. The program must:<br>• Add a new score to the list<br>• Sort the list in ascending order<br>• Remove the lowest score<br><br>Complete the code by selecting the correct code segment from each drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "scores = [78, 85, 62, 90]\n# Add new score 88\n[b1]\n# Sort the list\n[b2]\n# Remove the lowest score\n[b3]\nprint(scores)", options: [["scores.append(88)", "scores.add(88)"], ["scores.sort()", "scores.sorted()"], ["scores.pop(0)", "scores.remove(min(scores))"]], a: ["scores.append(88)", "scores.sort()", "scores.pop(0)"] },
        { id: 37, type: "TF", q: "<strong>Identity vs Equality:</strong> You are reviewing code written by a junior developer.<br><br>For each statement, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "a = [1, 2, 3]\nb = [1, 2, 3]\nc = a", options: ["a == b evaluates to True.", "a is b evaluates to True.", "a is c evaluates to True.", "b is not c evaluates to True."], a: [true, false, true, true] },
        { id: 38, type: "MCQ", q: "<strong>Logical Condition Evaluation:</strong> You are designing a system that validates login attempts. Review the following code:<br><br>What will be printed?", code: "attempts = 3\nlocked = False\nif attempts >= 3 and not locked:\n    print(\"Warning\")\nelse:\n    print(\"Access Allowed\")", options: ["Access Allowed", "Warning", "Syntax Error", "Nothing"], a: 1 },
        { id: 39, type: "MCQ2", q: "<strong>File Read Operation:</strong> You are writing a program that reads all lines from a file named data.txt. The program must:<br>• Open the file safely<br>• Read all contents<br>• Automatically close the file<br><br>Which two code segments meet the requirements?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", code: "A.\nwith open(\"data.txt\", \"r\") as f:\n    data = f.read()\n\nB.\nf = open(\"data.txt\", \"r\")\ndata = f.read()\n\nC.\nf = open(\"data.txt\", \"r\")\ndata = f.read()\nf.close()\n\nD.\nopen(\"data.txt\").read()", options: ["A", "B", "C", "D"], a: [0, 2] },
        { id: 40, type: "SHORT", q: "<strong>Loop with Continue:</strong> Review the following code segment:<br><br>What value is printed?<br><span style='font-size: 15px; font-style: italic;'>Enter the number as an integer.</span>", code: "total = 0\nfor i in range(1, 6):\n    if i == 3:\n        continue\n    total += i\nprint(total)", a: "12" }
    ],
    "mock2": [
    {
        "id": 1,
        "type": "DD",
        "q": "You are developing a Python application that requires unit testing. You need to:<br>\u2022 Import the correct module.<br>\u2022 Verify that a value is an instance of a specific class.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "[b1] unittest\nclass TestExample(unittest.TestCase):\n    def test_instance(self):\n        self.[b2](5, int)\n\nif __name__ == \"__main__\":\n    unittest.main()",
        "options": [
            [
                "define",
                "import",
                "include",
                "using"
            ],
            [
                "assertEqual",
                "assertTrue",
                "assertIsInstance",
                "assertIn"
            ]
        ],
        "a": [
            "import",
            "assertIsInstance"
        ]
    },
    {
        "id": 2,
        "type": "MCQ",
        "q": "You are part of a development team maintaining a large Python project. You need to add notes in your code so other developers can understand its purpose and logic.<br><br>What is the correct way to add a single-line comment in Python?",
        "options": [
            "Use /* comment */",
            "Use <!-- comment -->",
            "Use # comment",
            "Use // comment"
        ],
        "a": 2
    },
    {
        "id": 3,
        "type": "DD",
        "q": "You are writing a program that assigns a random room number. The program must:<br>\u2022 Ensure that the room number is not already assigned.<br>\u2022 Generate a new random number if it is already in use.<br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>",
        "code": "import random\nroomsAssigned = []\nroom_number = 1\nwhile room_number in roomsAssigned:\n    [b1]\nroomsAssigned.append(room_number)",
        "options": [
            "room_number = random.randint(1, 50)",
            "room_number += 1",
            "random.choice(room_number)"
        ],
        "a": [
            "room_number = random.randint(1, 50)"
        ]
    },
    {
        "id": 4,
        "type": "DD",
        "q": "A company requires a program that:<br>\u2022 Opens a file named report.txt.<br>\u2022 Writes the text \"End of listing\" into the file.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "file = open(\"report.txt\", \"[b1]\")\nfile.[b2](\"End of listing\")\nfile.close()",
        "options": [
            [
                "r",
                "w",
                "a"
            ],
            [
                "write",
                "read",
                "append"
            ]
        ],
        "a": [
            "w",
            "write"
        ]
    },
    {
        "id": 5,
        "type": "DD",
        "q": "You are writing a program that:<br>\u2022 Prompts the user for a number.<br>\u2022 Converts the input to an integer.<br>\u2022 Handles invalid input without crashing.<br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>",
        "code": "while True:\n    try:\n        x = int(input(\"Enter a number: \"))\n        break\n    [b1] ValueError:\n        print(\"Invalid number.\")",
        "options": [
            "except",
            "catch",
            "error",
            "handle"
        ],
        "a": [
            "except"
        ]
    },
    {
        "id": 6,
        "type": "DD",
        "q": "You are developing a file-processing program. Before opening a file, the program must:<br>\u2022 Verify that the file exists.<br>\u2022 Read and display its contents if it exists.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "import os\nif [b1](\"data.txt\"):\n    file = open(\"data.txt\", \"r\")\n    print(file.[b2]())\n    file.close()",
        "options": [
            [
                "os.path.exists",
                "os.exists",
                "os.path.check"
            ],
            [
                "read",
                "write",
                "open"
            ]
        ],
        "a": [
            "os.path.exists",
            "read"
        ]
    },
    {
        "id": 7,
        "type": "DND",
        "q": "You are building a program that prints all prime numbers between 2 and 20. The program must:<br>\u2022 Loop through numbers from 2 to 20.<br>\u2022 Determine whether each number is prime.<br>\u2022 Stop checking a number once a divisor is found.<br><br>Complete the code by moving the appropriate code segment into the correct location.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct placement.</span>",
        "code": "for p in range(2, 21):\n    is_prime = True\n    for i in range(2, p):\n        if p % i == 0:\n            is_prime = False\n            [target1]\n    if is_prime:\n        print(p)",
        "options": [
            "break",
            "continue",
            "pass"
        ],
        "a": [
            "break"
        ]
    },
    {
        "id": 8,
        "type": "DD",
        "q": "You are comparing two lists to determine whether they contain the same values in the same order.<br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>",
        "code": "numList = [1, 2, 3]\nalphaList = [\"a\", \"b\", \"c\"]\nif [b1]:\n    print(\"Equal\")\nelse:\n    print(\"Not Equal\")",
        "options": [
            "numList == alphaList",
            "numList is alphaList",
            "numList != alphaList",
            "numList in alphaList"
        ],
        "a": [
            "numList == alphaList"
        ]
    },
    {
        "id": 9,
        "type": "MCQ",
        "q": "You are creating a console-based application. You use the following statement:<br><br><div class='code-snippet' style='margin:0;'>data = input()</div><br>What does this statement do?",
        "options": [
            "Creates an HTML input field",
            "Prompts the user to enter text in the console",
            "Displays system input devices",
            "Opens a message dialog"
        ],
        "a": 1
    },
    {
        "id": 10,
        "type": "TF",
        "q": "You are reviewing the following function.<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>",
        "code": "def grosspay(hours=40, rate=25, pieces=0, piecerate=0, salary=0):\n    if pieces > 0:\n        return pieces * piecerate\n    if salary > 0:\n        pass\n    if hours > 40:\n        overtime = (hours - 40) * (1.5 * rate)\n        return overtime + (40 * rate)\n    else:\n        return hours * rate",
        "options": [
            "Calling grosspay() results in a syntax error.",
            "Calling grosspay(salary=50000) returns None.",
            "Calling grosspay(pieces=500, piecerate=4) returns 2000."
        ],
        "a": [
            false,
            false,
            true
        ]
    },
    {
        "id": 11,
        "type": "DD",
        "q": "You are writing a program that repeatedly accepts user input. The program must:<br>\u2022 Prompt the user to enter a word.<br>\u2022 Display the number of characters in the word.<br>\u2022 Continue until the user enters \"QUIT\".<br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>",
        "code": "word = input(\"Enter a word (or QUIT to exit): \")\n[b1] word != \"QUIT\":\n    print(len(word))\n    word = input(\"Enter a word (or QUIT to exit): \")",
        "options": [
            "if",
            "for",
            "while"
        ],
        "a": [
            "while"
        ]
    },
    {
        "id": 12,
        "type": "TF",
        "q": "You are reviewing the following conditional statements.<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>",
        "code": "if num1 == num2:\n    print(\"Equal\")\nif num1 < num2:\n    print(\"Less\")\nif num1 > num2:\n    print(\"Greater\")\nif num2 == num1:\n    print(\"Same\")",
        "options": [
            "The first print statement executes only when the values are equal.",
            "The second print statement executes only when num1 is less than num2.",
            "The third print statement executes only when num1 is greater than num2.",
            "The final condition is logically redundant."
        ],
        "a": [
            true,
            true,
            true,
            true
        ]
    },
    {
        "id": 13,
        "type": "DD",
        "q": "You are developing a function that counts how many words in a list contain a specific letter.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "def count_letter(letter, word_list):\n    count = 0\n    for [b1]:\n        if [b2]:\n            count += 1\n    return count",
        "options": [
            [
                "word in word_list",
                "letter in word",
                "word_list in letter",
                "word == letter"
            ],
            [
                "word in word_list",
                "letter in word",
                "word_list in letter",
                "word == letter"
            ]
        ],
        "a": [
            "word in word_list",
            "letter in word"
        ]
    },
    {
        "id": 14,
        "type": "DND",
        "q": "You are creating a guessing game. The program must:<br>\u2022 Generate a random number between 1 and 10.<br>\u2022 Allow the user up to three guesses.<br>\u2022 Stop immediately if the correct guess is entered.<br><br>Complete the code by moving the appropriate code segments into the correct locations.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct placement.</span>",
        "code": "from random import randint\ntarget = randint(1, 10)\nchance = 1\n[target1]\n    guess = int(input(\"Guess: \"))\n    if guess == target:\n        print(\"Correct!\")\n        [target2]\n    [target3]",
        "options": [
            "break",
            "chance += 1",
            "while chance <= 3:"
        ],
        "a": [
            "while chance <= 3:",
            "break",
            "chance += 1"
        ]
    },
    {
        "id": 15,
        "type": "DD",
        "q": "You are developing a function to calculate admission fees. The program must:<br>\u2022 Assign a free rate for children under 5.<br>\u2022 Assign a discounted rate for students aged 5 to 17.<br>\u2022 Assign a higher rate for non-students aged 5 to 17.<br>\u2022 Assign a standard adult rate otherwise.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "elif age >= 5 and age <= 17 and not school:\n    rate = [b1]\nelse:\n    rate = [b2]",
        "options": [
            [
                "20",
                "50",
                "10"
            ],
            [
                "20",
                "50",
                "10"
            ]
        ],
        "a": [
            "20",
            "50"
        ]
    },
    {
        "id": 16,
        "type": "MCQ",
        "q": "You are reviewing the following script.<br>The program is executed using the following command:<br><code>python script.py Apple Banana Mango</code><br><br>What is the output?",
        "code": "import sys\nprint(sys.argv[2])",
        "options": [
            "script.py",
            "Apple",
            "Banana",
            "Mango"
        ],
        "a": 2
    },
    {
        "id": 17,
        "type": "DD",
        "q": "You are creating a function that reverses a string.<br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>",
        "code": "def reverse_name(backward_name):\n    forward_name = \"\"\n    length = len(backward_name) - 1\n    while length >= 0:\n        forward_name += [b1]\n        length -= 1\n    return forward_name",
        "options": [
            "backward_name[length]",
            "backward_name",
            "forward_name[length]"
        ],
        "a": [
            "backward_name[length]"
        ]
    },
    {
        "id": 18,
        "type": "TF",
        "q": "You are reviewing the following function.<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>",
        "code": "def calc_power(x, y):\n    comment = \"# return the value\"\n    return x ** y  # exponent",
        "options": [
            "The string in line 2 is treated as a comment.",
            "The function returns x raised to the power y.",
            "The inline comment does not affect execution.",
            "Removing the comment changes the output."
        ],
        "a": [
            false,
            true,
            true,
            false
        ]
    },
    {
        "id": 19,
        "type": "MCQ",
        "q": "You are evaluating the following expression.<br><br>What is the value of answer?",
        "code": "answer = (9 % 4 * 10) // 2 ** 3 + 4",
        "options": [
            "5",
            "6",
            "4",
            "3"
        ],
        "a": 0
    },
    {
        "id": 20,
        "type": "MCQ",
        "q": "You are reviewing the following function.<br><br>An error occurs when executing this code. What is the most likely cause?",
        "code": "def read_file(file):\n    if os.path.isfile(file):\n        data = open(file, 'r')\n        for line in data:\n            print(line)",
        "options": [
            "isfile requires two parameters",
            "os module is not imported",
            "The path must be absolute",
            "open requires a different mode"
        ],
        "a": 1
    },
    {
        "id": 21,
        "type": "DD",
        "q": "You are developing a Python program that stores log information in a file. The program must:<br>\u2022 Open a file named log.txt<br>\u2022 Append new messages without deleting existing data<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "file = open(\"log.txt\", \"[b1]\")\nfile.[b2](\"System started\")\nfile.close()",
        "options": [
            [
                "r",
                "w",
                "a"
            ],
            [
                "read",
                "write",
                "append"
            ]
        ],
        "a": [
            "a",
            "write"
        ]
    },
    {
        "id": 22,
        "type": "MCQ",
        "q": "You are reviewing code written by a developer that checks whether a number exists in a list.<br><br>What will the program output?",
        "code": "numbers = [10, 20, 30, 40]\nprint(20 in numbers)",
        "options": [
            "False",
            "True",
            "20",
            "Error"
        ],
        "a": 1
    },
    {
        "id": 23,
        "type": "DND",
        "q": "You are developing a program that processes numbers from 1 to 10. The program must:<br>\u2022 Stop the loop immediately when the number 7 is encountered.<br><br>Complete the code by moving the correct code segment into the blank.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct placement.</span>",
        "code": "for i in range(1, 11):\n    if i == 7:\n        [target1]\n    print(i)",
        "options": [
            "break",
            "continue",
            "pass"
        ],
        "a": [
            "break"
        ]
    },
    {
        "id": 24,
        "type": "DD",
        "q": "You are creating a program that stores student marks. The program must:<br>\u2022 Add a new mark to the list<br>\u2022 Sort the list<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "marks = [70, 85, 60]\nmarks.[b1](90)\nmarks.[b2]()\nprint(marks)",
        "options": [
            [
                "append",
                "insert",
                "sort",
                "sorted"
            ],
            [
                "append",
                "insert",
                "sort",
                "sorted"
            ]
        ],
        "a": [
            "append",
            "sort"
        ]
    },
    {
        "id": 25,
        "type": "TF",
        "q": "You are reviewing the following Python code:<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>",
        "code": "score = 75\nif score >= 50:\n    print(\"Pass\")\nelse:\n    print(\"Fail\")",
        "options": [
            "The program prints Pass when score is 75.",
            "The program prints Fail when score is below 50.",
            "The else block executes when the condition is False."
        ],
        "a": [
            true,
            true,
            true
        ]
    },
    {
        "id": 26,
        "type": "DD",
        "q": "You are developing a Python program that reads data from a file. The program must:<br>\u2022 Check if the file records.txt exists.<br>\u2022 Read and print its contents if it exists.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "import os\nif [b1](\"records.txt\"):\n    file = open(\"records.txt\",\"r\")\n    print(file.[b2]())\n    file.close()",
        "options": [
            [
                "os.path.exists",
                "os.exists",
                "os.path.check"
            ],
            [
                "read",
                "write",
                "open"
            ]
        ],
        "a": [
            "os.path.exists",
            "read"
        ]
    },
    {
        "id": 27,
        "type": "DD",
        "q": "You are creating a program that generates a random number between 1 and 100.<br><br>Complete the code by selecting the correct option.",
        "code": "import random\nnum = random.[b1](1,100)\nprint(num)",
        "options": [
            "randint",
            "rand",
            "range",
            "random"
        ],
        "a": [
            "randint"
        ]
    },
    {
        "id": 28,
        "type": "MCQ",
        "q": "You are reviewing the following code:<br><br>What is the output?",
        "code": "for i in range(3):\n    print(i)",
        "options": [
            "1 2 3",
            "0 1 2",
            "0 1 2 3",
            "1 2"
        ],
        "a": 1
    },
    {
        "id": 29,
        "type": "TF",
        "q": "You are reviewing the following code:<br><br>Select True or False.",
        "code": "x = 10\nif x > 5:\n    print(\"High\")\nelse:\n    print(\"Low\")",
        "options": [
            "The program prints High.",
            "The program prints Low when x = 10.",
            "The if block runs when the condition is True."
        ],
        "a": [
            true,
            false,
            true
        ]
    },
    {
        "id": 30,
        "type": "DD",
        "q": "You are writing a program that checks whether a number exists in a list.<br><br>Complete the code.",
        "code": "numbers = [5,10,15]\nif 10 [b1] numbers:\n    print(\"Found\")",
        "options": [
            "in",
            "is",
            "==",
            "not"
        ],
        "a": [
            "in"
        ]
    },
    {
        "id": 31,
        "type": "SHORT",
        "q": "Review the following code:<br><br>How many lines of output will be printed?<br><span style='font-size: 12px; font-style: italic;'>Enter the number as an integer.</span>",
        "code": "for i in range(2):\n    for j in range(2):\n        print(i,j)",
        "a": "4"
    },
    {
        "id": 32,
        "type": "DD",
        "q": "You are creating a loop that prints numbers until 5.<br><br>Complete the code.",
        "code": "x = 1\n[b1] x <= 5:\n    print(x)\n    x += 1",
        "options": [
            "if",
            "for",
            "while"
        ],
        "a": [
            "while"
        ]
    },
    {
        "id": 33,
        "type": "MCQ",
        "q": "You are teaching a new colleague how to build reusable components in Python.<br><br>Which keyword defines a function?",
        "options": [
            "function",
            "define",
            "def",
            "func"
        ],
        "a": 2
    },
    {
        "id": 34,
        "type": "SHORT",
        "q": "You are reviewing a basic math utility function in a financial application.<br><br>What is the output of this code?",
        "code": "def add(a,b):\n    return a+b\nprint(add(3,7))",
        "a": "10"
    },
    {
        "id": 35,
        "type": "TF",
        "q": "You are implementing a default greeting for a user profile system.<br><br>Review the following code and select True or False for each statement.",
        "code": "def greet(name=\"Student\"):\n    print(\"Hello\",name)",
        "options": [
            "greet() prints Hello Student",
            "greet(\"Ana\") prints Hello Ana",
            "Default parameters must be declared first."
        ],
        "a": [
            true,
            true,
            false
        ]
    },
    {
        "id": 36,
        "type": "MCQ",
        "q": "You are developing a script that processes color themes from the command line.<br>Program execution:<br><code>python script.py Red Blue</code><br><br>What is the output?",
        "code": "import sys\nprint(sys.argv[1])",
        "options": [
            "script.py",
            "Red",
            "Blue",
            "Error"
        ],
        "a": 1
    },
    {
        "id": 37,
        "type": "DD",
        "q": "You are building a text parser that needs to extract the first letter of a company name.<br><br>Complete the code that prints the first character of a string.",
        "code": "text = \"Python\"\nprint(text[[b1]])",
        "options": [
            "0",
            "1",
            "-1",
            "2"
        ],
        "a": [
            "0"
        ]
    },
    {
        "id": 38,
        "type": "TF",
        "q": "You are reviewing the coding standards for a new team project regarding code documentation.<br><br>Select True or False for each statement.",
        "code": "# calculate total\ntotal = 10 + 5",
        "options": [
            "Comments are ignored during execution.",
            "Comments improve code readability.",
            "Comments change program output."
        ],
        "a": [
            true,
            true,
            false
        ]
    },
    {
        "id": 39,
        "type": "MCQ",
        "q": "You are debugging an automated billing formula that calculates a total including flat fees and multipliers.<br><br>Evaluate the following expression. What is the output?",
        "code": "print(10 + 5 * 2)",
        "options": [
            "30",
            "20",
            "25",
            "15"
        ],
        "a": 1
    },
    {
        "id": 40,
        "type": "DD",
        "q": "You are updating a data export tool that must overwrite previous export files with new data.<br><br>Complete the code to overwrite file contents.",
        "code": "file = open(\"data.txt\",\"[b1]\")\nfile.write(\"Hello\")\nfile.close()",
        "options": [
            "r",
            "a",
            "w"
        ],
        "a": [
            "w"
        ]
    }
],
    "mock3": [
    {
        "id": 1,
        "type": "DD",
        "q": "You are developing a Python program that stores log information in a file. The program must:<br>\u2022 Open a file named log.txt<br>\u2022 Append new messages without deleting existing data<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "file = open(\"log.txt\", \"[b1]\")\nfile.[b2](\"System started\")\nfile.close()",
        "options": [
            [
                "r",
                "w",
                "a"
            ],
            [
                "read",
                "write",
                "append"
            ]
        ],
        "a": [
            "a",
            "write"
        ]
    },
    {
        "id": 2,
        "type": "MCQ",
        "q": "You are reviewing code written by a developer that checks whether a number exists in a list.<br><br>What will the program output?",
        "code": "numbers = [10, 20, 30, 40]\nprint(20 in numbers)",
        "options": [
            "False",
            "True",
            "20",
            "Error"
        ],
        "a": 1
    },
    {
        "id": 3,
        "type": "DND",
        "q": "You are developing a program that processes numbers from 1 to 10. The program must:<br>\u2022 Stop the loop immediately when the number 7 is encountered.<br><br>Complete the code by moving the correct code segment into the blank.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct placement.</span>",
        "code": "for i in range(1, 11):\n    if i == 7:\n        [target1]\n    print(i)",
        "options": [
            "break",
            "continue",
            "pass"
        ],
        "a": [
            "break"
        ]
    },
    {
        "id": 4,
        "type": "DD",
        "q": "You are creating a program that stores student marks. The program must:<br>\u2022 Add a new mark to the list<br>\u2022 Sort the list<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "marks = [70, 85, 60]\nmarks.[b1](90)\nmarks.[b2]()\nprint(marks)",
        "options": [
            [
                "append",
                "insert",
                "sort",
                "sorted"
            ],
            [
                "append",
                "insert",
                "sort",
                "sorted"
            ]
        ],
        "a": [
            "append",
            "sort"
        ]
    },
    {
        "id": 5,
        "type": "TF",
        "q": "You are reviewing the following Python code:<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>",
        "code": "score = 75\nif score >= 50:\n    print(\"Pass\")\nelse:\n    print(\"Fail\")",
        "options": [
            "The program prints Pass when score is 75.",
            "The program prints Fail when score is below 50.",
            "The else block executes when the condition is False."
        ],
        "a": [
            true,
            true,
            true
        ]
    },
    {
        "id": 6,
        "type": "DD",
        "q": "You are developing a Python program that reads data from a file. The program must:<br>\u2022 Check if the file records.txt exists.<br>\u2022 Read and print its contents if it exists.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "import os\nif [b1](\"records.txt\"):\n    file = open(\"records.txt\",\"r\")\n    print(file.[b2]())\n    file.close()",
        "options": [
            [
                "os.path.exists",
                "os.exists",
                "os.path.check"
            ],
            [
                "read",
                "write",
                "open"
            ]
        ],
        "a": [
            "os.path.exists",
            "read"
        ]
    },
    {
        "id": 7,
        "type": "DD",
        "q": "You are creating a program that generates a random number between 1 and 100.<br><br>Complete the code by selecting the correct option.",
        "code": "import random\nnum = random.[b1](1,100)\nprint(num)",
        "options": [
            "randint",
            "rand",
            "range",
            "random"
        ],
        "a": [
            "randint"
        ]
    },
    {
        "id": 8,
        "type": "MCQ",
        "q": "You are reviewing the following code:<br><br>What is the output?",
        "code": "for i in range(3):\n    print(i)",
        "options": [
            "1 2 3",
            "0 1 2",
            "0 1 2 3",
            "1 2"
        ],
        "a": 1
    },
    {
        "id": 9,
        "type": "TF",
        "q": "You are reviewing the following code:<br><br>Select True or False.",
        "code": "x = 10\nif x > 5:\n    print(\"High\")\nelse:\n    print(\"Low\")",
        "options": [
            "The program prints High.",
            "The program prints Low when x = 10.",
            "The if block runs when the condition is True."
        ],
        "a": [
            true,
            false,
            true
        ]
    },
    {
        "id": 10,
        "type": "DD",
        "q": "You are writing a program that checks whether a number exists in a list.<br><br>Complete the code.",
        "code": "numbers = [5,10,15]\nif 10 [b1] numbers:\n    print(\"Found\")",
        "options": [
            "in",
            "is",
            "==",
            "not"
        ],
        "a": [
            "in"
        ]
    },
    {
        "id": 11,
        "type": "SHORT",
        "q": "Review the following code:<br><br>How many lines of output will be printed?<br><span style='font-size: 12px; font-style: italic;'>Enter the number as an integer.</span>",
        "code": "for i in range(2):\n    for j in range(2):\n        print(i,j)",
        "a": "4"
    },
    {
        "id": 12,
        "type": "DD",
        "q": "You are creating a loop that prints numbers until 5.<br><br>Complete the code.",
        "code": "x = 1\n[b1] x <= 5:\n    print(x)\n    x += 1",
        "options": [
            "if",
            "for",
            "while"
        ],
        "a": [
            "while"
        ]
    },
    {
        "id": 13,
        "type": "MCQ",
        "q": "You are teaching a new colleague how to build reusable components in Python.<br><br>Which keyword defines a function?",
        "options": [
            "function",
            "define",
            "def",
            "func"
        ],
        "a": 2
    },
    {
        "id": 14,
        "type": "SHORT",
        "q": "You are reviewing a basic math utility function in a financial application.<br><br>What is the output of this code?",
        "code": "def add(a,b):\n    return a+b\nprint(add(3,7))",
        "a": "10"
    },
    {
        "id": 15,
        "type": "TF",
        "q": "You are implementing a default greeting for a user profile system.<br><br>Review the following code and select True or False for each statement.",
        "code": "def greet(name=\"Student\"):\n    print(\"Hello\",name)",
        "options": [
            "greet() prints Hello Student",
            "greet(\"Ana\") prints Hello Ana",
            "Default parameters must be declared first."
        ],
        "a": [
            true,
            true,
            false
        ]
    },
    {
        "id": 16,
        "type": "MCQ",
        "q": "You are developing a script that processes color themes from the command line.<br>Program execution:<br><code>python script.py Red Blue</code><br><br>What is the output?",
        "code": "import sys\nprint(sys.argv[1])",
        "options": [
            "script.py",
            "Red",
            "Blue",
            "Error"
        ],
        "a": 1
    },
    {
        "id": 17,
        "type": "DD",
        "q": "You are building a text parser that needs to extract the first letter of a company name.<br><br>Complete the code that prints the first character of a string.",
        "code": "text = \"Python\"\nprint(text[[b1]])",
        "options": [
            "0",
            "1",
            "-1",
            "2"
        ],
        "a": [
            "0"
        ]
    },
    {
        "id": 18,
        "type": "TF",
        "q": "You are reviewing the coding standards for a new team project regarding code documentation.<br><br>Select True or False for each statement.",
        "code": "# calculate total\ntotal = 10 + 5",
        "options": [
            "Comments are ignored during execution.",
            "Comments improve code readability.",
            "Comments change program output."
        ],
        "a": [
            true,
            true,
            false
        ]
    },
    {
        "id": 19,
        "type": "MCQ",
        "q": "You are debugging an automated billing formula that calculates a total including flat fees and multipliers.<br><br>Evaluate the following expression. What is the output?",
        "code": "print(10 + 5 * 2)",
        "options": [
            "30",
            "20",
            "25",
            "15"
        ],
        "a": 1
    },
    {
        "id": 20,
        "type": "DD",
        "q": "You are updating a data export tool that must overwrite previous export files with new data.<br><br>Complete the code to overwrite file contents.",
        "code": "file = open(\"data.txt\",\"[b1]\")\nfile.write(\"Hello\")\nfile.close()",
        "options": [
            "r",
            "a",
            "w"
        ],
        "a": [
            "w"
        ]
    },
    {
        "id": 21,
        "type": "MCQ",
        "q": "You are developing a lottery application that selects a winner from a list of predefined grades.<br><br>What does this program do?",
        "code": "import random\nprint(random.choice([\"A\",\"B\",\"C\"]))",
        "options": [
            "Prints entire list",
            "Prints random element from list",
            "Sorts list",
            "Removes element"
        ],
        "a": 1
    },
    {
        "id": 22,
        "type": "TF",
        "q": "You are working on a logic controller that compares sensor threshold values.<br><br>Select True or False for each statement.",
        "code": "print(10 > 5)",
        "options": [
            "Output is True",
            "Result type is Boolean",
            "Comparison operators produce numbers."
        ],
        "a": [
            true,
            true,
            false
        ]
    },
    {
        "id": 23,
        "type": "SHORT",
        "q": "You are developing an inventory system and need to determine the total number of items currently in stock.<br><br>What is the printed answer?",
        "code": "nums = [1,2,3,4,5]\nprint(len(nums))",
        "a": "5"
    },
    {
        "id": 24,
        "type": "DD",
        "q": "You are writing a program to extract the name from a JSON payload containing student records.<br><br>Complete the code.",
        "code": "student = {\"name\":\"Rahul\",\"age\":20}\nprint(student[\"[b1]\"])",
        "options": [
            "name",
            "Rahul",
            "age",
            "student"
        ],
        "a": [
            "name"
        ]
    },
    {
        "id": 25,
        "type": "TF",
        "q": "You are designing a data deduplication routine and have decided to use Sets.<br><br>Select True or False for each statement concerning Sets.",
        "options": [
            "Sets allow duplicate values.",
            "Sets store unique elements.",
            "Sets are unordered."
        ],
        "a": [
            false,
            true,
            true
        ]
    },
    {
        "id": 26,
        "type": "MCQ",
        "q": "You are storing fixed configuration coordinates that must not be changed during execution. You choose to use a tuple.<br><br>Which statement describes tuples?",
        "options": [
            "Mutable sequence",
            "Immutable sequence",
            "Unordered structure",
            "Dynamic list"
        ],
        "a": 1
    },
    {
        "id": 27,
        "type": "TF",
        "q": "You are investigating memory optimization techniques and reviewing variable assignments.<br><br>Select True or False for each statement.",
        "code": "a = 10\nb = 10\nprint(a is b)",
        "options": [
            "Output may be True",
            "is checks memory identity",
            "== checks value equality."
        ],
        "a": [
            true,
            true,
            true
        ]
    },
    {
        "id": 28,
        "type": "DD",
        "q": "You are building a robust calculation engine that must safely handle unexpected mathematical operations without crashing.<br><br>Complete the code.",
        "code": "try:\n    print(10/0)\n[b1] ZeroDivisionError:\n    print(\"Cannot divide\")",
        "options": [
            "except",
            "catch",
            "handle"
        ],
        "a": [
            "except"
        ]
    },
    {
        "id": 29,
        "type": "TF",
        "q": "You are finalizing a database connection script that must guarantee cleanup processes execute.<br><br>Select True or False concerning the finally block.",
        "options": [
            "finally always executes",
            "finally runs only when error occurs",
            "finally runs even if no exception happens."
        ],
        "a": [
            true,
            false,
            true
        ]
    },
    {
        "id": 30,
        "type": "DD",
        "q": "You are writing automated tests for a data processing pipeline to strictly ensure variable types.<br><br>Complete the test statement.",
        "code": "self.[b1](5, int)",
        "options": [
            "assertTrue",
            "assertEqual",
            "assertIsInstance",
            "assertIn"
        ],
        "a": [
            "assertIsInstance"
        ]
    },
    {
        "id": 31,
        "type": "MCQ",
        "q": "You are auditing a complex pricing algorithm to ensure operations are calculated in the correct order.<br><br>What is the output?",
        "code": "print((10+5)*2)",
        "options": [
            "20",
            "30",
            "25",
            "15"
        ],
        "a": 1
    },
    {
        "id": 32,
        "type": "MTF",
        "q": "You are developing a string sanitizer that extracts specific substrings from a filename.<br><br>Match the sliced outputs:",
        "code": "text = \"pythonprogram\"",
        "options": [
            "text[:6]",
            "text[6:]"
        ],
        "labels": [
            "python",
            "program",
            "prog",
            "pythonp"
        ],
        "a": {
            "text[:6]": "python",
            "text[6:]": "program"
        }
    },
    {
        "id": 33,
        "type": "SHORT",
        "q": "You are writing a task scheduler that stops processing tasks early if a certain threshold is met.<br><br>How many numbers are printed?",
        "code": "for i in range(5):\n    if i == 3:\n        break\n    print(i)",
        "a": "3"
    },
    {
        "id": 34,
        "type": "DD",
        "q": "You are conducting a code review and spot an assignment inside a conditional check.<br><br>Correct the operator.",
        "code": "if x [b1] 5:\n    print(\"Hello\")",
        "options": [
            "==",
            "=",
            "!=",
            "="
        ],
        "a": [
            "=="
        ]
    },
    {
        "id": 35,
        "type": "DD",
        "q": "You are building a queue management system and need to add a new customer ID to the end of a list.<br><br>Complete the code.",
        "code": "numbers = [1,2,3]\nnumbers.[b1](4)",
        "options": [
            "append",
            "add",
            "insert",
            "extend"
        ],
        "a": [
            "append"
        ]
    },
    {
        "id": 36,
        "type": "MCQ2",
        "q": "You are developing a log reading utility that extracts historical data safely.<br><br>Which two code segments correctly read file content? (Choose 2.)",
        "options": [
            "with open(\"data.txt\",\"r\") as f:\n    print(f.read())",
            "f=open(\"data.txt\",\"r\")\nprint(f.read())\nf.close()",
            "open(\"data.txt\").write()",
            "open(\"data.txt\").append()"
        ],
        "a": [
            0,
            1
        ]
    },
    {
        "id": 37,
        "type": "MCQ",
        "q": "You are verifying a complex gate condition in a security access script.<br><br>What is the output?",
        "code": "print(True or False)",
        "options": [
            "True",
            "False",
            "None",
            "Error"
        ],
        "a": 0
    },
    {
        "id": 38,
        "type": "DD",
        "q": "You are creating a game mechanic that spawns an item between specific coordinate limits.<br><br>Complete the code.",
        "code": "import random\nprint(random.[b1](1,10))",
        "options": [
            "randrange",
            "rand",
            "random",
            "choose"
        ],
        "a": [
            "randrange"
        ]
    },
    {
        "id": 39,
        "type": "MCQ",
        "q": "You are developing an automated maintenance script that removes temporary files.<br><br>Which function deletes a file?",
        "options": [
            "os.delete()",
            "os.remove()",
            "os.erase()",
            "os.clean()"
        ],
        "a": 1
    },
    {
        "id": 40,
        "type": "SHORT",
        "q": "You are calculating a running total of scores but must skip the calculation for a specific round.<br><br>What is the output?",
        "code": "total = 0\nfor i in range(1,6):\n    if i == 3:\n        continue\n    total += i\nprint(total)",
        "a": "12"
    }
],
    "d1": [
        { id: 1, type: "MCQ", q: "Which statement best describes data?", options: ["Processed information ready for decision making", "Raw facts and figures collected for analysis", "A business strategy", "A summarized report"], a: 1 },
        { id: 2, type: "MCQ", q: "<b>True or False:</b> Data becomes meaningful only after processing and analysis.", options: ["True", "False"], a: 0 },
        { id: 3, type: "MCQ", q: "Which data type can store a sentence or phrase?", options: ["Integer", "Boolean", "String", "Float"], a: 2 },
        { id: 4, type: "MCQ", q: "Select the correct data type for the value below.<br><br><div class='code-snippet' style='margin:0;'>is_logged_in = True</div>", options: ["Integer", "Boolean", "String", "Float"], a: 1 },
        { id: 5, type: "MTF", q: "Match the data structure with the description.", options: ["Table", "Row", "Column", "List"], labels: ["Multiple rows and columns", "Single record in a dataset", "Attribute or field", "Collection of items"], a: { "Table": "Multiple rows and columns", "Row": "Single record in a dataset", "Column": "Attribute or field", "List": "Collection of items" } },
        { id: 6, type: "MCQ", q: 'Which data structure describes this data?<br><br><div class=\'code-snippet\' style=\'margin:0;\'>["Aabid", "Jesenia", "Mark"]</div>', options: ["Table", "List", "Graph", "Matrix"], a: 1 },
        { id: 7, type: "MCQ", q: "Which of the following is quantitative data?", options: ["Eye color", "Age", "Country name", "Product category"], a: 1 },
        { id: 8, type: "MCQ", q: "<b>True or False:</b> Qualitative data describes categories rather than numeric values.", options: ["True", "False"], a: 0 }
    ],
    "d2": [
        { id: 1, type: "MCQ", q: "What is an example of data cleaning?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", options: ["Arranging Excel data rows in an order that is easy for a user to read", "Ensuring that the data in a Word table uses a consistent font", "Adding quotation marks to the beginning and end of a tab-delimited file", "Removing non-printable characters from a comma-delimited file"], a: 3 },
        { id: 2, type: "MTF", q: "You are performing descriptive analytics on quarterly sales data. Match the metric with the description.", options: ["Average", "Max", "Min", "Sum"], labels: ["Mean value of sales", "Largest value", "Smallest value", "Total of all values"], a: { "Average": "Mean value of sales", "Max": "Largest value", "Min": "Smallest value", "Sum": "Total of all values" } },
        { id: 3, type: "MCQ2", q: "You need to create a data view based on aggregations for sales data from the last five years. Which two aggregation methods should you use?", options: ["Filtering", "Pivoting", "Merging", "Grouping"], a: [1, 3] },
        { id: 4, type: "MCQ", q: "Your company summarized a large dataset for your region. You need to compare results from urban and rural communities. What is the fastest way to obtain this information?", options: ["Review data from neighboring regions", "Aggregate the data", "Disaggregate the data", "Collect a new data sample"], a: 2 },
        { id: 5, type: "DND", q: "Complete the data organization scenarios by dragging the correct method to each situation.", code: "<div style='display:grid; grid-template-columns: 1fr auto; gap:15px; align-items:center;'><div>Arrange distributed items from highest to lowest</div> [target1]<div>Display only items greater than 500</div> [target2]<div>Extract a subset of the dataset containing only the 'Sales' column</div> [target3]</div>", options: ["Sorting", "Filtering", "Slicing", "Truncating", "Transposing", "Appending"], a: ["Sorting", "Filtering", "Slicing"] },
        { id: 6, type: "MCQ", q: "As part of an ETL process, which action represents Transformation?", options: ["Changing data from summary level to detailed level", "Converting data from one data type or structure to another", "Retrieving data from multiple sources into one destination", "Importing a percentage of rows from the source data"], a: 1 },
        { id: 8, type: "MCQ", q: "A file named coursesdata contains structured data. Which programming language could be used to read this data and import it into a database?", options: ["SQL", "Python", "HTML", "CSS"], a: 1 }
    ],
    "data3": [
        { id: 1, type: "MCQ", q: "A retail manager notices a sudden 20% spike in weekend umbrella sales. Which analysis should the manager use to find the <b>root cause</b> for this unexpected increase?", options: ["Predictive Analysis", "Diagnostic Analysis", "Descriptive Analysis", "Prescriptive Analysis"], a: 1 },
        { id: 2, type: "TF", q: "A hospital uses historical patient records to forecast how many beds will be needed on Friday nights.<br><br><b>True or False:</b> This is an example of Predictive Analysis.", options: ["This is an example of Predictive Analysis."], a: [true] },
        { id: 3, type: "DD", q: "A travel app processes millions of raw GPS coordinates to suggest nearby hotels to tourists.<br><br>The process of converting these raw coordinates into <b>meaningful suggestions</b> is called generating ______.<br><br>Select the correct answer from the dropdown.", code: "Raw GPS Data → [b1]", options: ["Noise", "Insights", "Errors", "Files"], a: ["Insights"] },
        { id: 4, type: "MCQ", q: "Which of the following activities is <b>NOT</b> an example of data analysis?", options: ["Identifying patterns in student test scores", "Predicting customer churn based on usage", "Manually changing the font color of a final report", "Summarizing monthly sales by region"], a: 2 },
        { id: 5, type: "MTF", q: "Match the type of analysis with the <b>real-world scenario</b> it represents.<br><span style='font-size:12px;font-style:italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["Descriptive", "Diagnostic", "Predictive", "Prescriptive"], labels: ["Calculating last month's revenue", "Finding why profit dropped in June", "Estimating next year's market growth", "Recommending an automated budget cut"], a: { "Descriptive": "Calculating last month's revenue", "Diagnostic": "Finding out why profit dropped in June", "Predictive": "Estimating next year's market growth", "Prescriptive": "Recommending an automated budget cut" } },
        { id: 6, type: "MCQ", q: "An e-commerce manager prints a weekly report showing exactly how many laptops were sold in every city.<br><br>Which type of analysis does this report represent?", options: ["Predictive", "Prescriptive", "Descriptive", "Diagnostic"], a: 2 },
        { id: 7, type: "TF", q: "<b>True or False:</b> Diagnostic analysis is primarily used to forecast whether a company's stock price will rise next month.", options: ["Diagnostic analysis forecasts future outcomes."], a: [false] },
        { id: 8, type: "DD", q: "A logistics company uses historical traffic trends to <b>estimate</b> exactly when a package will arrive at its destination.<br><br>Predictive analysis is used here to ______ the arrival time.", code: "Predictive Analysis → [b1] delivery times", options: ["Ignore", "Predict", "Delete", "Store"], a: ["Predict"] }
    ],
    "ex1": [
        { id: 1, type: "MCQ", q: "<strong>Strategic Analysis:</strong> What is a manager's primary objective when overseeing a business data model?", options: ["Maximizing Variance to increase risk-taking", "Maintaining the Pulse (Mean) and minimizing Variance (Risk)", "Hiding raw data from stakeholders", "Building the most complex formulas possible"], a: 1 },
        { id: 2, type: "MCQ", q: "<strong>Data Pulses:</strong> Which function is most appropriate for understanding a 'typical' customer's spend when the dataset contains extreme outliers?", options: ["AVERAGE", "SUM", "MEDIAN", "STDEV.P"], a: 2 },
        { id: 3, type: "TF", q: "<strong>Inventory Intelligence:</strong> Analyze the following statements regarding statistical inventory management.<br><br>For each statement, select True or False.", options: ["High Standard Deviation (STDEV.P) indicates a need for 'Safety Stock'.", "Low Standard Deviation allows for 'Just-in-Time' (JIT) stock management.", "The MAX function is used exclusively to find 'Dead Stock'.", "The MIN function identifies products that are candidates for liquidation."], a: [true, true, false, true] },
        { id: 4, type: "MTF", q: "<strong>Model Engineering:</strong> Match each layer of the Three-Layer Architecture to its primary function.", options: ["Data Lake (Raw)", "The Engine (Logic)", "The Dashboard (Front)", "Assumptions"], labels: ["Untouched CSV/SQL imports", "Formula-heavy calculation layer", "Final reports and KPI tables", "Hardcoded inputs and tax rates"], a: { "Data Lake (Raw)": "Untouched CSV/SQL imports", "The Engine (Logic)": "Formula-heavy calculation layer", "The Dashboard (Front)": "Final reports and KPI tables", "Assumptions": "Hardcoded inputs and tax rates" } },
        { id: 5, type: "MCQ", q: "<strong>Architecture:</strong> Why is the Kerala Boutique naming convention (e.g., ST-0001-K) essential for model scalability?", options: ["It reduces file size significantly", "It creates predictable patterns for extraction logic", "It prevents Excel from crashing", "It automatically formats cells"], a: 1 },
        { id: 6, type: "DD", q: "<strong>Structured Logic:</strong> Identify the correct function to count all 'Hero Product' items that exceed a revenue threshold in a dynamic table.<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "[b1](Table_Kerala[Revenue], \">50000\")", options: ["COUNTIFS", "SUMIFS", "VLOOKUP", "AVERAGEIFS"], a: ["COUNTIFS"] },
        { id: 7, type: "MCQ", q: "<strong>Hierarchy:</strong> In our architectural framework, which unit represents an entire geographic region (e.g., South India)?", options: ["A single cell", "A worksheet", "An entire workbook", "A table row"], a: 2 },
        { id: 8, type: "MCQ", q: "<strong>The 'Esc' Rule:</strong> According to professional standards, where should 'Report_OUTPUT' sheets pull their data from?", options: ["Directly from the Data_Raw sheet", "From external web sources", "Through the Logic_CALC (Engine) layer", "From the Home tab"], a: 2 }
    ],
    "ex2": [
        { id: 1, type: "MCQ", q: "Which XLOOKUP argument defines the value to return if no match is found, eliminating the need for nested IFERROR functions?", options: ["lookup_value", "return_array", "if_not_found", "match_mode"], a: 2 },
        { id: 2, type: "MCQ", q: "Analyze the formula <code>=INDEX(A1:C10, 5, 2)</code>. What specific coordinate is this formula targeting?", options: ["Row 5, Column 2", "Column 5, Row 2", "Total columns count", "Range height"], a: 0 },
        { id: 3, type: "TF", q: "<strong>Logic Advantage:</strong> Determine if the following statements about INDEX-MATCH vs. VLOOKUP are True or False.", options: ["INDEX-MATCH can look up values to the LEFT of the key column.", "VLOOKUP is faster than INDEX-MATCH for datasets with 50+ columns.", "INDEX-MATCH remains intact when new columns are inserted in the middle."], a: [true, false, true] },
        { id: 4, type: "MCQ", q: "Which Boolean function returns TRUE only if EVERY single logic test within the parenthesis is passed?", options: ["OR()", "IF()", "AND()", "NOT()"], a: 2 },
        { id: 5, type: "SHORT", q: "In binary strategic logic, if we multiply two Boolean results (Criteria1 * Criteria2), what numerical result do we get if both criteria are TRUE?", a: "1" },
        { id: 6, type: "DD", q: "Construct a 2D Lookup formula to find the 'Tax Rate' where the Row is 'Product' and the Column is 'Region'.", code: "=INDEX(Tax_Matrix, MATCH(\"Saree\", Rows, 0), [b1](\"Kerala\", Columns, 0))", options: ["MATCH", "XLOOKUP", "VLOOKUP", "HLOOKUP"], a: ["MATCH"] },
        { id: 7, type: "MTF", q: "Match the logic gate with its business requirement.", options: ["AND", "OR", "XOR", "NOT"], labels: ["Must meet all eligibility rules", "Meet either the age OR the income rule", "Exclude a specific category from a list", "Targeting users who chose A or B, but not both"], a: { "AND": "Must meet all eligibility rules", "OR": "Meet either the age OR the income rule", "XOR": "Targeting users who chose A or B, but not both", "NOT": "Exclude a specific category from a list" } },
        { id: 8, type: "MCQ", q: "When using XLOOKUP, setting the <code>match_mode</code> to <b>-1</b> tells Excel to perform which action if an exact match is missing?", options: ["Return next larger item", "Return next smaller item", "Return wildcards", "Return a #DIV/0! error"], a: 1 }
    ],
    "ex3": [
        { id: 1, type: "MCQ", q: "Which shortcut represents the 'Gold Standard' for toggling between relative, absolute, and mixed cell references?", options: ["F2", "F4", "F10", "Alt+Shift+R"], a: 1 },
        { id: 2, type: "MCQ", q: "In the mixed reference <b>$A1</b>, which axis is explicitly 'locked' during a formula drag operation?", options: ["The Row axis (1)", "The Column axis (A)", "The entire Workbook", "Neither"], a: 1 },
        { id: 3, type: "SHORT", q: "You have the formula <code>=A$1 + B1</code> in cell C1. If you drag this formula DOWN to cell C2, what will the resulting formula in C2 be?", a: "=A$1 + B2" },
        { id: 4, type: "MCQ2", q: "Identify TWO primary reasons for using Absolute References ($C$2) in a financial model.", options: ["To prevent references from shifting when copying formulas", "To lock external tax rates or assumption variables", "To reduce the file size of the calculations", "To ensure formulas only work on hidden sheets"], a: [0, 1] },
        { id: 5, type: "SHORT", q: "If you copy the formula <code>=$B$5</code> from cell D10 and paste it into cell Z500, what will the formula in Z500 look like?", a: "=$B$5" },
        { id: 6, type: "MCQ", q: "What does the <b>!</b> symbol signify in the reference <code>'Q3_Sales'!C10</code>?", options: ["A logical negation (NOT)", "A worksheet boundary identifier", "A broken link warning", "An important formula tag"], a: 1 },
        { id: 7, type: "MCQ", q: "When building a 10x10 multiplication table, which referencing style should be applied to the column headers in Row 1 to allow for horizontal and vertical dragging?", options: ["A1 (Relative)", "$A$1 (Absolute)", "A$1 (Mixed Row-locked)", "$A1 (Mixed Column-locked)"], a: 2 },
        { id: 8, type: "MCQ", q: "If you drag the formula <code>=$C5</code> to the RIGHT through 5 columns, what stays fixed in the reference?", options: ["The Row (5)", "The Column (C)", "The Worksheet name", "The Cell value"], a: 1 }
    ],
    "ex4": [
        { id: 1, type: "MCQ", q: "Which shortcut key is the universal standard for converting a raw data range into a 'Smart Table'?", options: ["Ctrl + S", "Ctrl + T", "Ctrl + L", "Alt + T"], a: 1 },
        { id: 2, type: "MCQ", q: "What is the primary advantage of using a Table instead of a normal range for an inventory list?", options: ["It uses colors automatically", "It automatically expands when new rows are added at the bottom", "It prevents users from deleting data", "It hides the formula bar"], a: 1 },
        { id: 3, type: "SHORT", q: "In a Table named 'Sales', what character is used to refer to 'this row' in a formula like <code>=Sales[[b1]Amount] * 0.1</code>?", a: "@" },
        { id: 4, type: "MTF", q: "<strong>Strategic Matching:</strong> Match the Excel Table nomenclature to its respective component.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["Table1[#All]", "Table1[#Data]", "Table1[#Headers]", "Table1[#Totals]"], labels: ["Entire table (headers, data, totals)", "Rows of data only", "Top column names row", "Final calculation row at the bottom"], a: { "Table1[#All]": "Entire table (headers, data, totals)", "Table1[#Data]": "Rows of data only", "Table1[#Headers]": "Top column names row", "Table1[#Totals]": "Final calculation row at the bottom" } },
        { id: 5, type: "TF", q: "<strong>Data Integrity:</strong> Select True or False for each statement regarding Data Validation.", options: ["A 'Stop' alert prevents users from entering invalid data.", "A 'Warning' alert allows invalid data but shows a message.", "Drop-down lists can only be created from numbers."], a: [true, true, false] },
        { id: 6, type: "MCQ", q: "You need to ensure that a 'Quantity' column only accepts whole numbers between 1 and 500. Which tool should you use?", options: ["Conditional Formatting", "Data Validation", "Goal Seek", "AutoSum"], a: 1 },
        { id: 7, type: "SHORT", q: "What is the result of <code>Table1[[#Totals],[Revenue]]</code> if the Revenue column total is 5000?", a: "5000" },
        { id: 8, type: "MCQ", q: "Which tool provides a visual, button-based way to filter a Table without using the standard filter arrows?", options: ["Slicers", "Filters", "Macros", "Sparklines"], a: 0 }
    ],
    "ex5": [
        { id: 1, type: "MCQ", q: "What is the 'Strategic Logic' behind using Heat Maps in an inventory aging report?", options: ["To make the sheet look colorful", "To identify business 'Exceptions' without reading every row", "To sort the data automatically", "To reduce file size"], a: 1 },
        { id: 2, type: "MCQ", q: "Using Icon Sets (Traffic Lights) for Sales Reps, what would a 'Red' light typically signify in a trend analysis?", options: ["Top performance", "A downward trend or performance drop", "Pending data entry", "Data error"], a: 1 },
        { id: 3, type: "TF", q: "<strong>Conditional Rules:</strong> Select True or False for each statement.", options: ["Formula-based rules allow you to format an entire row based on one cell value.", "You can apply multiple conditional rules to the same range.", "Heat Maps only work with text values."], a: [true, true, false] },
        { id: 4, type: "DND", q: "<strong>Visualizing Metrics:</strong> You are setting up a dashboard. Move the formatting technique to the most appropriate business scenario.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct placement.</span>", code: "<div class='dnd-grid'><div>Show inventory levels as bars:</div> [target1]<div>Flag low performers with Red icons:</div> [target2]<div>Color cells based on profit %:</div> [target3]</div>", options: ["Data Bars", "Icon Sets", "Color Scales"], a: ["Data Bars", "Icon Sets", "Color Scales"] },
        { id: 5, type: "MCQ", q: "Which feature would you use to show a 'Gradient' fill in a cell based on how close it is to the monthly target?", options: ["Icon Sets", "Color Scales", "Highlight Cells Rules", "Data Bars"], a: 3 },
        { id: 6, type: "SHORT", q: "In a Heat Map for 'Inventory Age', what color would you strategically assign to fabric sitting for 180+ days?", a: "Red" },
        { id: 7, type: "MCQ2", q: "Identify TWO business benefits of using Strategic Conditional Formatting.", options: ["Faster identification of profit leakage", "Automated sorting of spreadsheets", "Visual triggers for immediate investigation", "Permanent deletion of outdated records"], a: [0, 2] },
        { id: 8, type: "TF", q: "<strong>Visual Triggers:</strong> Are the following statements True or False?", options: ["Color Scales show a transition between two or three colors.", "Conditional Formatting changes the actual value of the cell.", "Rules are re-calculated automatically whenever data changes."], a: [true, false, true] }
    ],
    "ex6": [
        { id: 1, type: "MTF", q: "<strong>Function Logic:</strong> Match the formula to its analytical purpose.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["=SUMIFS(Revenue, ...)", "=COUNTIFS(EmployeeID, ...)", "=AVERAGEIFS(Sales, ...)", "=MAXIFS(Price, ...)"], labels: ["Total earnings across multiple branches", "Counting employees meeting a specific target", "Benchmarking typical performance of a group", "Finding the peak pricing within a segment"], a: { "=SUMIFS(Revenue, ...)": "Total earnings across multiple branches", "=COUNTIFS(EmployeeID, ...)": "Counting employees meeting a specific target", "=AVERAGEIFS(Sales, ...)": "Benchmarking typical performance of a group", "=MAXIFS(Price, ...)": "Finding the peak pricing within a segment" } },
        { id: 2, type: "MCQ", q: "Why is <code>AVERAGEIFS</code> used for 'Strategic Benchmarking'?", options: ["To find the total revenue of a branch", "To compare subset performance (e.g., Manager A vs Manager B)", "To count how many items were sold", "To find the highest sale value"], a: 1 },
        { id: 3, type: "SHORT", q: "In the <code>SUMIFS</code> function, which argument must ALWAYS be specified first?", a: "sum_range" },
        { id: 4, type: "MCQ2", q: "You need to calculate the Total Sales of 'Linen' in 'Mumbai' during 'Q1'. Which TWO arguments are mandatory for this SUMIFS?", options: ["The range containing 'Linen/Silk' names", "The range containing 'Branch' names", "The range containing 'Employee ID'", "The range containing 'Stock Count'"], a: [0, 1] },
        { id: 5, type: "TF", q: "<strong>Criteria Logic:</strong> Select True or False for each statement.", options: ["SUMIFS can handle more than 100 different criteria.", "Wildcards (*) can be used in criteria to find partial matches.", "SUMIFS works even if the criteria_ranges are different sizes."], a: [true, true, false] },
        { id: 6, type: "MCQ", q: "What does 'Filter while Calculating' refer to in advanced analytics?", options: ["Using the filter button and then manually summing", "Performing a conditional aggregation (like SUMIFS) to isolate segments", "Deleting rows that don't match criteria", "Sorting data before calculating totals"], a: 1 },
        { id: 7, type: "SHORT", q: "What is the numerical output of <code>COUNTIFS(A:A, \"*\")</code> if Column A has 5 text entries?", a: "5" },
        { id: 8, type: "MCQ", q: "If Manager A has an average discount of 15% and Manager B has 5%, what business insight is detected using <code>AVERAGEIFS</code>?", options: ["Branch growth", "Potential profit leakage", "Inventory shortage", "Marketing success"], a: 1 }
    ],
    "ex7": [
        { id: 1, type: "MCQ", q: "Which function is the 'Modern Standard' for retrieving data, replacing the need for VLOOKUP?", options: ["HLOOKUP", "XLOOKUP", "MATCH", "INDEX"], a: 1 },
        { id: 2, type: "MCQ", q: "What is the primary risk of using VLOOKUP in a long-term business model?", options: ["It makes the file too large", "It breaks when you insert or delete columns", "It cannot find exact matches", "It only works with numbers"], a: 1 },
        { id: 3, type: "DND", q: "<strong>Retrieval Strategies:</strong> Move the lookup function to its primary strategic advantage.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct placement.</span>", code: "<div class='dnd-grid'><div>Retrieve values to the LEFT of the key:</div> [target1]<div>Legacy support for small, static lists:</div> [target2]<div>Return the position of an item:</div> [target3]</div>", options: ["XLOOKUP", "VLOOKUP", "MATCH"], a: ["XLOOKUP", "VLOOKUP", "MATCH"] },
        { id: 4, type: "MCQ2", q: "Identify TWO advantages of using <code>INDEX & MATCH</code> over VLOOKUP.", options: ["Ability to look to the LEFT of the key column", "Immunity to column insertion/deletion", "Faster calculation for 1 million rows", "Automatic translation of text"], a: [0, 1] },
        { id: 5, type: "TF", q: "<strong>Error Handling:</strong> Select True or False for each statement.", options: ["IFERROR replaces #N/A with custom text like 'Check ID'.", "Reports with visible #N/A codes are considered professional.", "XLOOKUP has a built-in 'if_not_found' argument."], a: [true, false, true] },
        { id: 6, type: "MCQ", q: "What is a 'Common Key' in data relationship logic?", options: ["A cell with a green background", "A shared identifier (like Employee ID) used to link two different tables", "A password to open the file", "The most expensive product in a list"], a: 1 },
        { id: 7, type: "SHORT", q: "In <code>INDEX(A1:A10, 5)</code>, what is the value of the 5th item in the range if A1 is 100, A2 is 200... A5 is 500?", a: "500" },
        { id: 8, type: "MCQ", q: "Which XLOOKUP argument allows you to pull multiple columns at once by selecting a wide range?", options: ["lookup_value", "return_array", "match_mode", "search_mode"], a: 1 }
    ],
    "ex8": [
        { id: 1, type: "MCQ", q: "What does the 'ETL' process in Power Query stand for?", options: ["Extract, Transform, Load", "Evaluate, Total, Link", "Export, Transfer, List", "Excel, Table, Logic"], a: 0 },
        { id: 2, type: "MCQ", q: "Why would a professional use Power Query instead of manual copy-pasting for monthly reports?", options: ["It provides better colors", "It records and automates the cleaning steps for future data", "Manual pasting is more accurate", "Power Query requires a special license"], a: 1 },
        { id: 3, type: "MTF", q: "<strong>BI Infrastructure:</strong> Match the tool to its primary functional domain.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["Power Query", "Power Pivot", "DAX", "Relationships"], labels: ["Extracting and Cleaning data", "Modeling complex datasets", "Creating advanced measures/formulas", "Linking two tables via a Key ID"], a: { "Power Query": "Extracting and Cleaning data", "Power Pivot": "Modeling complex datasets", "DAX": "Creating advanced measures/formulas", "Relationships": "Linking two tables via a Key ID" } },
        { id: 4, type: "MCQ2", q: "Identify TWO characteristics of 'Big Data' handling in Excel BI tools.", options: ["Processing millions of rows without crashing", "Using DAX to calculate cross-table metrics", "Replacing all formulas with VBA macros", "Hiding columns permanently"], a: [0, 1] },
        { id: 5, type: "TF", q: "<strong>Automation Logic:</strong> Select True or False for each statement.", options: ["Power Query repeats cleaning steps with a single click (Refresh).", "Power Pivot is like a mini-SQL database inside Excel.", "VLOOKUP is faster than Power Pivot for 1 million rows."], a: [true, true, false] },
        { id: 6, type: "MCQ", q: "Which language is used in Power Pivot to create advanced measures like 'Revenue per Rupee of Salary'?", options: ["Python", "SQL", "DAX", "VBA"], a: 2 },
        { id: 7, type: "SHORT", q: "What is the maximum number of rows a standard Excel worksheet can hold?", a: "1048576" },
        { id: 8, type: "MCQ", q: "You need to combine 12 monthly CSV files into one master Table. Which Power Query feature should you use?", options: ["Pivot Column", "Merge Queries", "Append Queries", "Group By"], a: 2 }
    ],
    "ex9": [
        { id: 1, type: "MCQ", q: "What does a 'Correlation' coefficient of +0.9 between Marketing and Sales indicate?", options: ["No relationship", "A very strong positive relationship", "Marketing causes sales to drop", "Error in the data"], a: 1 },
        { id: 2, type: "DND", q: "<strong>Predictive Analytics:</strong> Move the statistical term to its correct definition.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct placement.</span>", code: "<div class='dnd-grid'><div>Measures relationship strength (-1 to +1):</div> [target1]<div>Projects future values based on history:</div> [target2]<div>Determines the 'line of best fit':</div> [target3]</div>", options: ["Correlation", "Forecasting", "Regression"], a: ["Correlation", "Forecasting", "Regression"] },
        { id: 3, type: "SHORT", q: "Which function is used to project future sales based on a linear trend and historical data?", a: "FORECAST.LINEAR" },
        { id: 4, type: "MCQ2", q: "Identify TWO metrics found in 'Descriptive Statistics' used for business audits.", options: ["Standard Deviation (Risk)", "Skewness (Outlier detection)", "VLOOKUP (Retrieval)", "SUMIFS (Counting)"], a: [0, 1] },
        { id: 5, type: "TF", q: "<strong>Trend Analysis:</strong> Select True or False for each statement.", options: ["A linear trendline assumes data moves in a straight path.", "Seasonality accounts for recurring peaks like festive seasons.", "Forecasting is only useful if you have 1 week of data."], a: [true, true, false] },
        { id: 6, type: "MCQ", q: "Which toolpak must be enabled in Excel to access advanced Regression and Descriptive Statistics?", options: ["Macro Pak", "Data Analysis Toolpak", "Power Map", "Solver"], a: 1 },
        { id: 7, type: "SHORT", q: "What is the term for a data point that is significantly higher or lower than the rest of the group?", a: "Outlier" },
        { id: 8, type: "MCQ", q: "Why is 'Skewness' important in a finance budget audit?", options: ["To find the average spend", "To detect if a few massive expenses are inflating the total", "To calculate taxes", "To sort employee names"], a: 1 }
    ],
    "ex10": [
        { id: 1, type: "MCQ", q: "What is the '30-Second Insight' rule in visual storytelling?", options: ["The chart must take 30 seconds to load", "If a manager can't understand the insight in 30 seconds, the chart has failed", "Every chart must have 30 different colors", "A chart must be updated every 30 seconds"], a: 1 },
        { id: 2, type: "MTF", q: "<strong>Chart Selection:</strong> Match the chart type to its high-impact use case.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["Waterfall Chart", "Pareto (80/20)", "Scatter Plot", "Bar Chart"], labels: ["Visualizing profit/cost leakage", "Identifying top assets generating most wealth", "Detecting correlation between variables", "Comparing simple categorical revenue"], a: { "Waterfall Chart": "Visualizing profit/cost leakage", "Pareto (80/20)": "Identifying top assets generating most wealth", "Scatter Plot": "Detecting correlation between variables", "Bar Chart": "Comparing simple categorical revenue" } },
        { id: 3, type: "SHORT", q: "Which chart is based on the 80/20 rule, identifying the 'Vital Few' assets that generate most of the wealth?", a: "Pareto" },
        { id: 4, type: "MCQ2", q: "Identify TWO use cases for a 'Stacked Column Chart'.", options: ["Comparing total revenue across branches", "Showing the product mix (categories) within each branch", "Visualizing individual transaction logs", "Calculating the square root of sales"], a: [0, 1] },
        { id: 5, type: "TF", q: "<strong>Clarity Logic:</strong> Select True or False for each statement.", options: ["3D effects and shadows generally improve chart clarity.", "A Pareto chart combines a bar chart and a cumulative line.", "Visualizing 'Profit Leakage' is a key goal of a Waterfall chart."], a: [false, true, true] },
        { id: 6, type: "MCQ", q: "In a Pareto analysis of 100 products, what does the '80/20' principle suggest?", options: ["80% of products generate 80% of sales", "20% of products generate 80% of the sales", "80% of effort yields 100% result", "20 products are always defective"], a: 1 },
        { id: 7, type: "SHORT", q: "In a '100% Stacked Column Chart', what is the total percentage height of every individual column?", a: "100" },
        { id: 8, type: "MCQ", q: "Why are 'Floating Bars' used in a Waterfall chart?", options: ["To show where values decrease or increase relative to the previous point", "To make the chart look like a bridge", "To hide negative values", "To save space"], a: 0 }
    ]
,

    "data1": [
        { id: 1, type: "MCQ", q: "<strong>Data Fundamentals:</strong> What is raw data that has been processed and turned into something meaningful called?", options: ["Information", "Metadata", "Storage", "Draft"], a: 0 },
        { id: 2, type: "TF", q: "<strong>Data Types:</strong> Consider the nature of qualitative and quantitative data.<br><br>For each statement below, select True or False by dragging.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", options: ["Qualitative data focuses on numbers and measurements.", "Blood type represents categorical qualitative data.", "Quantitative data can be discrete or continuous.", "The number of children in a household is continuous data."], a: [false, true, true, false] },
        { id: 3, type: "DROPDOWN", q: "<strong>Structured vs Unstructured:</strong> You are evaluating different data sources for an enterprise data warehouse.<br><br>Complete the classification by selecting the correct option from the drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "An email body text is [b1] data, while a SQL database table containing customer names is [b2] data.", options: [["Structured", "Semi-structured", "Unstructured"], ["Structured", "Semi-structured", "Unstructured"]], a: ["Unstructured", "Structured"] },
        { id: 4, type: "MTF", q: "<strong>Data Attributes:</strong> Match the numeric data type scale with its correct example.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["Nominal Data", "Ordinal Data", "Interval Data", "Ratio Data"], labels: ["Hair Color", "Customer Satisfaction (1-5)", "Temperature in Celsius", "Annual Salary"], a: { "Nominal Data": "Hair Color", "Ordinal Data": "Customer Satisfaction (1-5)", "Interval Data": "Temperature in Celsius", "Ratio Data": "Annual Salary" } },
        { id: 5, type: "MCQ2", q: "<strong>Big Data:</strong> Which two of the following statements accurately describe the defining characteristics (the 'V's) of Big Data?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", options: ["Volume refers to the massive scale of data generated.", "Variety means Big Data only consists of numerical records.", "Velocity refers to the speed at which data is generated and processed.", "Veracity indicates that all Big Data is 100% accurate and clean."], a: [0, 2] },
        { id: 6, type: "MCQ", q: "<strong>Metadata Definition:</strong> Which term is commonly defined as 'data about other data'?", options: ["Microdata", "Metadata", "Masterdata", "Megadata"], a: 1 },
        { id: 7, type: "TF", q: "<strong>Reviewing Data Formats:</strong> Evaluate the following statements regarding data formats.<br><br>Select True or False for each statement.", options: ["Audio files are examples of unstructured data.", "A spreadsheet with rows and columns is unstructured data.", "Metadata helps organize and locate data without opening the file itself."], a: [true, false, true] },
        { id: 8, type: "MCQ", q: "<strong>Data Categories:</strong> Which of the following is an example of Discrete Quantitative data?", options: ["The exact weight of an apple (e.g., 152.4g)", "The number of employees in a company", "The eye color of the employees", "The temperature recorded in an office"], a: 1 }
    ],
    "data2": [
        { id: 1, type: "MCQ", q: "<strong>Data Preparation:</strong> Which process involves identifying and removing errors, duplicates, and inconsistencies from a dataset?", options: ["Data Mining", "Data Cleaning", "Data Storage", "Data Visualization"], a: 1 },
        { id: 2, type: "DROPDOWN", q: "<strong>Data Life Cycle:</strong> You are organizing the phases of the Data Analytics Life Cycle. The typical first step after defining the objective is to [b1] the data, and after cleaning, the next immediate step is to [b2] the data.<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", options: [["Collect", "Analyze", "Visualize", "Archive"], ["Collect", "Analyze", "Visualize", "Archive"]], a: ["Collect", "Analyze"] },
        { id: 3, type: "MTF", q: "<strong>Life Cycle Phases:</strong> Match each action to the correct phase of the Data Life Cycle.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["Data Collection", "Data Wrangling", "Data Analysis", "Data Visualization"], labels: ["Gathering records from an API", "Converting date formats and merging tables", "Applying statistical models", "Creating a dashboard chart"], a: {"Data Collection": "Gathering records from an API", "Data Wrangling": "Converting date formats and merging tables", "Data Analysis": "Applying statistical models", "Data Visualization": "Creating a dashboard chart"} },
        { id: 4, type: "TF", q: "<strong>Data Quality:</strong> You are reviewing a newly acquired dataset.<br><br>For each statement below, select True or False by dragging.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", options: ["Missing values can skew analysis results if not handled.", "Data visualization should always precede data cleaning.", "ETL stands for Extract, Transform, Load."], a: [true, false, true] },
        { id: 5, type: "MCQ2", q: "<strong>Wrangling Techniques:</strong> What are two common activities performed during Data Wrangling?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", options: ["Filtering out unwanted rows", "Presenting findings to executives", "Joining multiple datasets together", "Publishing data to the public internet"], a: [0, 2] },
        { id: 6, type: "MCQ", q: "<strong>Exploratory Analysis:</strong> What does the acronym EDA stand for in the context of the data life cycle?", options: ["Executive Data Assessment", "Exploratory Data Analysis", "Electronic Data Automation", "External Data Algorithm"], a: 1 },
        { id: 7, type: "MCQ", q: "<strong>Phase Priorities:</strong> Why is data cleaning considered one of the most critical steps in the data life cycle?", options: ["It is the fastest step in the process.", "It ensures that the insights generated are accurate and reliable.", "It automatically generates predictive dashboards.", "It replaces the need for data collection."], a: 1 },
        { id: 8, type: "TF", q: "<strong>Analysis Flow:</strong> Evaluate standard practices in a professional data environment.<br><br>Select True or False for each statement.", options: ["Data visualization is primarily used to store data efficiently.", "Deploying models is often the final actionable step of advanced predictive life cycles.", "Data governance policies dictate how data is managed throughout its life cycle."], a: [false, true, true] },
        { id: 9, type: "MCQ", q: "<strong>File Formats:</strong> Which data file format uses key-value pairs to store data?", options: ["CSV", "XML", "JSON", "SQL"], a: 2 },
        { id: 10, type: "MCQ", q: "<strong>Data Handling:</strong> A dataset contains a row where the city is 'new york' instead of 'New York'. What type of data issue does this represent?", options: ["Duplicate record", "Missing value", "Inconsistent formatting", "Special characters"], a: 2 },
        { id: 11, type: "MTF", q: "<strong>Data Formats:</strong> Match the common data file format to its description.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["CSV", "XML", "JSON"], labels: ["Data separated by commas", "Data structured with tags", "Data stored in key-value pairs"], a: {"CSV": "Data separated by commas", "XML": "Data structured with tags", "JSON": "Data stored in key-value pairs"} },
        { id: 12, type: "DROPDOWN", q: "<strong>ETL Architecture:</strong> You are setting up an automated pipeline. The stage where data is collected from an external database is the [b1] phase, and where it is cleaned and converted is the [b2] phase.", options: [["Extract", "Transform", "Load"], ["Extract", "Transform", "Load"]], a: ["Extract", "Transform"] },
        { id: 13, type: "MTF", q: "<strong>Data Cleaning:</strong> Match the dirty data example to its correct issue type.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["Duplicate", "Missing", "Formatting", "Special Chars"], labels: ["Two identical rows for Arjun", "Age column showing 'NULL'", "City listed as 'kOCHi'", "Name entered as 'M@ike'"], a: {"Duplicate": "Two identical rows for Arjun", "Missing": "Age column showing 'NULL'", "Formatting": "City listed as 'kOCHi'", "Special Chars": "Name entered as 'M@ike'"} },
        { id: 14, type: "TF", q: "<strong>Data Systems:</strong> Evaluate the following statements regarding the ETL process.", options: ["The 'Extract' phase can pull data from multiple different sources at once.", "The 'Load' phase modifies the structure of the data.", "'Transform' involves removing duplicates and correcting errors."], a: [true, false, true] },
        { id: 15, type: "MCQ2", q: "<strong>Data Manipulation Goals:</strong> Identify TWO primary reasons why data manipulation is an essential step before analysis.", options: ["To ensure the dataset is accurate and consistent", "To generate automatic predictive forecasts", "To identify and remove errors or missing values", "To permanently delete historical company records"], a: [0, 2] }
    ],
    "data3": [
        { id: 1, type: "MCQ", q: "<strong>Data Analysis Goals:</strong> What is the primary goal of data analysis?", options: ["Collecting data", "Storing data", "Extracting useful insights from data", "Deleting data"], a: 2 },
        { id: 2, type: "TF", q: "<strong>Analytical Maturity:</strong> Evaluate the levels of depth in data analytics.<br><br>For each statement below, select True or False by dragging.", options: ["Descriptive analytics explains 'What happened?'", "Predictive analytics answers the question 'Why did it happen?'", "Prescriptive analytics suggests 'What should we do about it?'"], a: [true, false, true] },
        { id: 3, type: "MCQ", q: "<strong>Historical Data:</strong> Which type of analytics summarizes past data?", options: ["Diagnostic", "Descriptive", "Predictive", "Prescriptive"], a: 1 },
        { id: 4, type: "TF", q: "<strong>Diagnostic Logic:</strong> Analyze the purpose of diagnostic analytics.<br><br>Select True or False for each statement.", options: ["It is used to uncover the root cause of an unexpected dip in sales.", "It primarily focuses on predicting next month's weather patterns.", "It often involves drilling down into specific data segments to find patterns."], a: [true, false, true] },
        { id: 5, type: "MCQ", q: "<strong>Forecasting:</strong> Predicting next year's sales using past sales data is an example of:", options: ["Diagnostic analysis", "Predictive analysis", "Descriptive analysis", "Prescriptive analysis"], a: 1 },
        { id: 6, type: "MCQ", q: "<strong>Recommendations:</strong> Which type of analysis recommends business actions?", options: ["Prescriptive", "Diagnostic", "Descriptive", "Historical"], a: 0 },
        { id: 7, type: "MTF", q: "<strong>Data Metrics:</strong> Match the metric with its correct description.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["Sum", "Max", "Min", "Count"], labels: ["Total of values", "Largest value", "Smallest value", "Number of values"], a: { "Sum": "Total of values", "Max": "Largest value", "Min": "Smallest value", "Count": "Number of values" } },
        { id: 8, type: "MCQ", q: "<strong>Exploratory Data Analysis:</strong> Which of the following is a key goal of Exploratory Data Analysis (EDA)?", options: ["Deleting data", "Discovering patterns and relationships", "Writing programs", "Creating databases"], a: 1 },
        { id: 9, type: "TF", q: "<strong>Analysis Integrity:</strong> Consider the relationship between variables.<br><br>For each statement below, select True or False by dragging.", options: ["Correlation always means that one variable is the direct cause of another.", "Visualizing data with scatter plots can help detect potential correlations.", "Identifying causation usually requires controlled experiments or deeper domain context."], a: [false, true, true] },
        { id: 10, type: "MCQ", q: "<strong>Advanced Analytics:</strong> Machine learning in analytics is commonly used to:", options: ["Delete data", "Predict patterns in data", "Format spreadsheets", "Create documents"], a: 1 }
    ],
    "data4": [
        { id: 1, type: "MCQ", q: "<strong>Chart Selection:</strong> You need to visualize the growth of monthly sales over the last 12 months. Which chart is most effective for showing this trend?", options: ["Bar Chart", "Line Chart", "Pie Chart", "Histogram"], a: 1 },
        { id: 2, type: "MTF", q: "<strong>Visualization Match:</strong> Match each visualization type to its primary purpose.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["Comparison", "Trend", "Distribution", "Correlation"], labels: ["Comparing categories (e.g., Sales by Region)", "Changes over time (e.g., Monthly Growth)", "How data is spread (e.g., Age ranges)", "Relationship between variables (e.g., Price vs Sales)"], a: {"Comparison": "Comparing categories (e.g., Sales by Region)", "Trend": "Changes over time (e.g., Monthly Growth)", "Distribution": "How data is spread (e.g., Age ranges)", "Correlation": "Relationship between variables (e.g., Price vs Sales)"} },
        { id: 3, type: "DROPDOWN", q: "<strong>Visual Integrity:</strong> You are evaluating a dashboard with a Y-axis that starts at 1,000 instead of 0 for a dataset ranging from 1,000 to 1,200. This is an example of [b1] bias. To show the spread of salaries in a company, use a [b2].", options: [["Visual/Scaling", "Sampling", "Confirmation"], ["Histogram", "Line Chart", "Scatter Plot"]], a: ["Visual/Scaling", "Histogram"] },
        { id: 4, type: "TF", q: "<strong>Effective Communication:</strong> Evaluate the following statements on data storytelling.<br><br>Select True or False for each statement.", options: ["A good report should emphasize key insights over raw data.", "Correlation between two variables always confirms causation.", "Using simple language helps stakeholders understand complex findings."], a: [true, false, true] },
        { id: 5, type: "MCQ2", q: "<strong>Visual Clarity:</strong> Which two practices help improve the clarity of a data report?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", options: ["Using clear, descriptive titles", "Adding as many gridlines as possible", "Focusing on the 30-second insight rule", "Hiding the axes to make the report look minimalist"], a: [0, 2] },
        { id: 6, type: "MCQ", q: "<strong>Insight Communication:</strong> Which is the most effective way to explain a data finding to a business stakeholder?", options: ["Provide the raw database logs", "Use clear visuals and concise explanations", "Use as many technical terms as possible", "Keep findings vague to avoid questions"], a: 1 },
        { id: 7, type: "MCQ", q: "<strong>Chart Types:</strong> Which chart is specifically designed to show the frequency of data within certain ranges (distribution)?", options: ["Line Chart", "Bar Chart", "Histogram", "Scatter Plot"], a: 2 },
        { id: 8, type: "TF", q: "<strong>Accuracy & Bias:</strong> Evaluate the following regarding visual interpretation.", options: ["Interpreting a visualization correctly is as important as creating it.", "Changing the axis scale can distort the perceived magnitude of change.", "Scatter plots are used to compare categorical totals."], a: [true, true, false] },
        { id: 9, type: "MCQ", q: "<strong>Interpret Patterns:</strong> Look at the chart below. What does this visualization indicate about the relationship between Advertising Spend and Sales?", chart: { type: 'scatter', data: 'correlation' }, options: ["No relationship", "Strong Positive Correlation", "Negative Correlation", "Cyclical Pattern"], a: 1 },
        { id: 10, type: "MCQ", q: "<strong>Trend Analysis:</strong> In the trend chart below, which month experienced the most significant growth recovery after a dip?", chart: { type: 'line', data: 'recovery_trend' }, options: ["Month 2", "Month 4", "Month 6", "Month 8"], a: 2 },
        { id: 11, type: "DROPDOWN", q: "<strong>Visual Selection:</strong> You need to present the [b1] of age groups in your customer base. The most effective chart for this is a [b2].", options: [["Trend", "Comparison", "Distribution", "Correlation"], ["Histogram", "Line Chart", "Scatter Plot", "Heatmap"]], a: ["Distribution", "Histogram"] },
        { id: 12, type: "MCQ", q: "<strong>Comparative Insights:</strong> Which of the following visual representations is most appropriate for identifying the <b>underperforming</b> outlier in a regional sales dataset?", options: ["Region A", "Region B", "Region C (Outlier)", "Region D"], optionsCharts: [{data: 'regional_sales'}, {data: 'market_share'}, {data: 'correlation'}, {type: 'bar', data: {labels:['X','Y','Z'], datasets:[{data:[10,12,50], backgroundColor:'#0ea5e9'}]} }], a: 0 },
        { id: 16, type: "MCQ", q: "<strong>Visual Storytelling:</strong> Which chart is better suited for a stakeholder who wants to see the <b>cumulative share</b> of different product lines over a year?", chart: {data: 'recovery_trend'}, options: ["Grouped Bar", "Stacked Area", "Simple Line", "Pie Map"], a: 1 },
        { id: 13, type: "TF", q: "<strong>Data Storytelling:</strong> Evaluate these advanced communication principles.", options: ["The '30-second rule' means a stakeholder should grasp the main insight within 30 seconds.", "Static tables are always superior to interactive dashboards for live presentations.", "Adding 'Chart Junk' (unnecessary decorations) improves the professional look of a report."], a: [true, false, false] },
        { id: 14, type: "MCQ", q: "<strong>Composition:</strong> Looking at the Donut chart below, which product category holds the <b>majority</b> share (>50%) of total revenue?", chart: { type: 'doughnut', data: 'market_share' }, options: ["Electronics", "Apparel", "Home Decor", "Furniture"], a: 0 },
        { id: 15, type: "DROPDOWN", q: "<strong>Bias Detection:</strong> A line chart showing 'Global Temperature' uses a Y-axis that only starts at 20°C, making a 0.5°C change look like a huge spike. This is a form of [b1] bias. If a surveyor only asks happy customers for feedback, that is [b2] bias.", options: [["Visual Scaling", "Sampling", "Confirmation"], ["Sampling", "Visual Scaling", "Measurement"]], a: ["Visual Scaling", "Sampling"] }
    ],
    "data5": [
        { id: 1, type: "MCQ", q: "<strong>Data Applications:</strong> Which of the following is an example of an algorithm applying Predictive Analysis in the real world?", options: ["A thermostat that adjusts temperature based on the current time.", "A streaming service recommending movies based on your viewing history.", "A car dashboard displaying the current tire pressure.", "A cash register printing a receipt."], a: 1 },
        { id: 2, type: "TF", q: "<strong>Data Ethics:</strong> Evaluate the following statements on data ethics and security.<br><br>Select True or False for each statement.", options: ["Data bias in training sets can lead to discriminatory AI models.", "Anonymizing data means to attach a person's explicit name to their records.", "Transparency involves hiding how user data is collected and processed."], a: [true, false, false] },
        { id: 3, type: "MTF", q: "<strong>Ethics Principles:</strong> Match the data governance concept with its correct definition.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["Privacy", "Security", "Compliance", "Bias Mitigation"], labels: ["Respecting user consent and data rights", "Protecting data from unauthorized access or breaches", "Adhering to legal standards like GDPR or CCPA", "Ensuring models represent diverse populations fairly"], a: {"Privacy": "Respecting user consent and data rights", "Security": "Protecting data from unauthorized access or breaches", "Compliance": "Adhering to legal standards like GDPR or CCPA", "Bias Mitigation": "Ensuring models represent diverse populations fairly"} },
        { id: 4, type: "DROPDOWN", q: "<strong>Regulations:</strong> You are setting up user data policies for a European application.<br><br>You must ensure strict adherence to the [b1] framework, which protects consumer privacy and data rights in the EU. For California residents, you would reference [b2].", options: [["GDPR", "HIPAA", "SOX"], ["CCPA", "HIPAA", "PCI-DSS"]], a: ["GDPR", "CCPA"] },
        { id: 5, type: "MCQ2", q: "<strong>Data Security:</strong> Which two practices are standard methods for protecting sensitive data?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", options: ["Data Encryption", "Posting data to a public GitHub repo", "Role-Based Access Control (RBAC)", "Storing passwords in plain text"], a: [0, 2] },
        { id: 6, type: "MCQ", q: "<strong>Algorithmic Impact:</strong> What is a potential negative consequence of using historical data that contains human prejudices to train a machine learning model?", options: ["Algorithmic Bias", "Data Encryption", "Data Normalization", "Increased Data Velocity"], a: 0 },
        { id: 7, type: "TF", q: "<strong>Ethics in Action:</strong> Review the scenarios concerning data rights.<br><br>Select True or False for each statement.", options: ["Users generally have the right to request deletion of their personal data under GDPR.", "Data Security and Data Privacy are exactly the same concept.", "A company is ethically bound to protect user data even if it has no legal obligation."], a: [true, false, true] },
        { id: 8, type: "MCQ", q: "<strong>Acronym Check:</strong> What does the European privacy regulation acronym GDPR stand for?", options: ["General Data Processing Rule", "Group Data Protection Resource", "General Data Protection Regulation", "Global Data Privacy Routine"], a: 2 },
        { id: 9, type: "MCQ", q: "<strong>PII Handling:</strong> If a data analyst discovers a customer's clear phone number in a public dataset, what is the most responsible action?", options: ["Publish the dataset immediately", "Delete the specific record before sharing", "Mask the phone number (e.g., +91 XXX-XXX)", "Rename the file to 'Confidential'"], a: 2 },
        { id: 10, type: "DROPDOWN", q: "<strong>Anonymization & Bias:</strong> You are preparing a database report. To protect individual identity, you [b1] the user names. To ensure the results are representative and fair, you actively work on [b2] mitigation.", options: [["Mask/Anonymize", "Encrypt", "Delete"], ["Bias", "Privacy", "Security"]], a: ["Mask/Anonymize", "Bias"] }
    ],
    "ex1": [
        { id: 1, type: "MCQ", q: "<strong>Strategic Analysis:</strong> What is a manager's primary objective when overseeing a business data model?", options: ["Maximizing Variance to increase risk-taking", "Maintaining the Pulse (Mean) and minimizing Variance (Risk)", "Hiding raw data from stakeholders", "Building the most complex formulas possible"], a: 1 },
        { id: 2, type: "MCQ", q: "<strong>Data Pulses:</strong> Which function is most appropriate for understanding a 'typical' customer's spend when the dataset contains extreme outliers?", options: ["AVERAGE", "SUM", "MEDIAN", "STDEV.P"], a: 2 },
        { id: 3, type: "TF", q: "<strong>Inventory Intelligence:</strong> Analyze the following statements regarding statistical inventory management.<br><br>For each statement, select True or False by dragging.", options: ["High Standard Deviation (STDEV.P) indicates a need for 'Safety Stock'.", "Low Standard Deviation allows for 'Just-in-Time' (JIT) stock management.", "The MAX function is used exclusively to find 'Dead Stock'.", "The MIN function identifies products that are candidates for liquidation."], a: [true, true, false, true] },
        { id: 4, type: "MTF", q: "<strong>Model Engineering:</strong> Match each layer of the Three-Layer Architecture to its primary function.", options: ["Data Lake (Raw)", "The Engine (Logic)", "The Dashboard (Front)", "Assumptions"], labels: ["Untouched CSV/SQL imports", "Formula-heavy calculation layer", "Final reports and KPI tables", "Hardcoded inputs and tax rates"], a: { "Data Lake (Raw)": "Untouched CSV/SQL imports", "The Engine (Logic)": "Formula-heavy calculation layer", "The Dashboard (Front)": "Final reports and KPI tables", "Assumptions": "Hardcoded inputs and tax rates" } },
        { id: 5, type: "MCQ", q: "<strong>Architecture:</strong> Why is the Kerala Boutique naming convention (e.g., ST-0001-K) essential for model scalability?", options: ["It reduces file size significantly", "It creates predictable patterns for extraction logic", "It prevents Excel from crashing", "It automatically formats cells"], a: 1 },
        { id: 6, type: "DROPDOWN", q: "<strong>Structured Logic:</strong> Identify the correct function to count all 'Hero Product' items that exceed a revenue threshold in a dynamic table.<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "[b1](Table_Kerala[Revenue], \">50000\")", options: [["COUNTIFS", "SUMIFS", "VLOOKUP", "AVERAGEIFS"]], a: ["COUNTIFS"] },
        { id: 7, type: "MCQ", q: "<strong>Hierarchy:</strong> In our architectural framework, which unit represents an entire geographic region (e.g., South India)?", options: ["A single cell", "A worksheet", "An entire workbook", "A table row"], a: 2 },
        { id: 8, type: "MCQ", q: "<strong>The 'Esc' Rule:</strong> According to professional standards, where should 'Report_OUTPUT' sheets pull their data from?", options: ["Directly from the Data_Raw sheet", "From external web sources", "Through the Logic_CALC (Engine) layer", "From the Home tab"], a: 2 }
    ],
    "ex2": [
        { id: 1, type: "MCQ", q: "Which XLOOKUP argument defines the value to return if no match is found, eliminating the need for nested IFERROR functions?", options: ["lookup_value", "return_array", "if_not_found", "match_mode"], a: 2 },
        { id: 2, type: "MCQ", q: "Analyze the formula <code>=INDEX(A1:C10, 5, 2)</code>. What specific coordinate is this formula targeting?", options: ["Row 5, Column 2", "Column 5, Row 2", "Total columns count", "Range height"], a: 0 },
        { id: 3, type: "TF", q: "<strong>Logic Advantage:</strong> Determine if the following statements about INDEX-MATCH vs. VLOOKUP are True or False.", options: ["INDEX-MATCH can look up values to the LEFT of the key column.", "VLOOKUP is faster than INDEX-MATCH for datasets with 50+ columns.", "INDEX-MATCH remains intact when new columns are inserted in the middle."], a: [true, false, true] },
        { id: 4, type: "MCQ", q: "Which Boolean function returns TRUE only if EVERY single logic test within the parenthesis is passed?", options: ["OR()", "IF()", "AND()", "NOT()"], a: 2 },
        { id: 5, type: "MCQ", q: "In binary strategic logic, if we multiply two Boolean results (Criteria1 * Criteria2), what numerical result do we get if both criteria are TRUE?", options: ["0", "1", "2", "-1"], a: 1 },
        { id: 6, type: "DROPDOWN", q: "Construct a 2D Lookup formula to find the 'Tax Rate' where the Row is 'Product' and the Column is 'Region'.", code: "=INDEX(Tax_Matrix, MATCH(\"Saree\", Rows, 0), [b1](\"Kerala\", Columns, 0))", options: [["MATCH", "XLOOKUP", "VLOOKUP", "HLOOKUP"]], a: ["MATCH"] },
        { id: 7, type: "MTF", q: "Match the logic gate with its business requirement.", options: ["AND", "OR", "XOR", "NOT"], labels: ["Must meet all eligibility rules", "Meet either the age OR the income rule", "Exclude a specific category from a list", "Targeting users who chose A or B, but not both"], a: { "AND": "Must meet all eligibility rules", "OR": "Meet either the age OR the income rule", "XOR": "Targeting users who chose A or B, but not both", "NOT": "Exclude a specific category from a list" } },
        { id: 8, type: "MCQ", q: "When using XLOOKUP, setting the <code>match_mode</code> to <b>-1</b> tells Excel to perform which action if an exact match is missing?", options: ["Return next larger item", "Return next smaller item", "Return wildcards", "Return a #DIV/0! error"], a: 1 }
    ],
    "da_mock1": [
        { 
            id: 1, 
            type: "MCQ", 
            q: "What is the direction of correlation between variable X and variable Y based on the scatter plot below?", 
            img: "correlation_scatter.png", 
            options: ["Positive", "Negative", "Zero"], 
            a: 0 
        },
        { 
            id: 2, 
            type: "MCQ", 
            q: "Which correlation range most likely describes the relationship between Variable X and Variable Y based on the plot provided?", 
            img: "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQwMCIgdmlld0JveD0iMCAwIDYwMCA0MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cmVjdCB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQwMCIgZmlsbD0iI2ZjZmNmYyIgc3Ryb2tlPSIjZTJlOGYwIiBzdHJva2Utd2lkdGg9IjEiLz4KICAgIDxsaW5lIHgxPSI1MCIgeTE9IjUwIiB4Mj0iNTUwIiB5Mj0iNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNTAiIHkxPSIxMDAiIHgyPSI1NTAiIHkyPSIxMDAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNTAiIHkxPSIxNTAiIHgyPSI1NTAiIHkyPSIxNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNTAiIHkxPSIyMDAiIHgyPSI1NTAiIHkyPSIyMDAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNTAiIHkxPSIyNTAiIHgyPSI1NTAiIHkyPSIyNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNTAiIHkxPSIzMDAiIHgyPSI1NTAiIHkyPSIzMDAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iMTAwIiB5MT0iNTAiIHgyPSIxMDAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iMTUwIiB5MT0iNTAiIHgyPSIxMTUwIiB5Mj0iMzUwIiBzdHJva2U9IiNmMmY1ZjkiIHN0cm9rZS13aWR0aD0iMSIvPgogICAgPGxpbmUgeD0iMjAwIiB5MT0iNTAiIHgyPSIyMDAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iMjUwIiB5MT0iNTAiIHgyPSIyNTAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iMzAwIiB5MT0iNTAiIHgyPSIzMDAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iMzUwIiB5MT0iNTAiIHgyPSIzNTAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNDAwIiB5MT0iNTAiIHgyPSI0MDAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNDUwIiB5MT0iNTAiIHgyPSI0NTAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNTAwIiB5MT0iNTAiIHgyPSI1MDAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNTAiIHkxPSIzNTAiIHgyPSI1NTAiIHkyPSIzNTAiIHN0cm9rZT0iIzQ3NTU2OSIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgICA8bGluZSB4MT0iNTAiIHkxPSI1MCIgeDI9IjUwIiB5Mj0iMzUwIiBzdHJva2U9IiM0NzU1NjkiIHN0cm9rZS13aWR0aD0iMiIvPgogICAgPHRleHQgeD0iMzAwIiB5PSIzODAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iIzQ3NTU2OSI+VmFyaWFibGUgWDwvdGV4dD4KICAgIDx0ZXh0IHg9IjE1IiB5PSIyMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iIzQ3NTU2OSIgdHJhbnNmb3JtPSJyb3RhdGUoLTkwLCAxNSwgMjAwKSI+VmFyaWFibGUgWTwvdGV4dD4KICAgIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjI1MCIgcj0iNSIgZmlsbD0iIzQ0NzJjNCIgLz4KICAgIDxjaXJjbGUgY3g9IjE1MCIgY3k9IjMwMCIgcj0iNSIgZmlsbD0iIzQ0NzJjNCIgLz4KICAgIDxjaXJjbGUgY3g9IjIwMCIgY3k9IjE5MCIgcj0iNSIgZmlsbD0iIzQ0NzJjNCIgLz4KICAgIDxjaXJjbGUgY3g9IjIwMCIgY3k9IjIwMCIgcj0iNSIgZmlsbD0iIzQ0NzJjNCIgLz4KICAgIDxjaXJjbGUgY3g9IjMwMCIgY3k9IjE2MCIgcj0iNSIgZmlsbD0iIzQ0NzJjNCIgLz4KICAgIDxjaXJjbGUgY3g9IjM1MCIgY3k9IjI1NSIgcj0iNSIgZmlsbD0iIzQ0NzJjNCIgLz4KICAgIDxjaXJjbGUgY3g9IjQwMCIgY3k9IjEzMCIgcj0iNSIgZmlsbD0iIzQ0NzJjNCIgLz4KICAgIDxjaXJjbGUgY3g9IjQ1MCIgY3k9Ijc1IiAgcj0iNSIgZmlsbD0iIzQ0NzJjNCIgLz4KPC9zdmc+", 
            options: ["No correlation (r=0.00)", "Some correlation (0.00 < r < 0.99)", "Perfect correlation (r=1.00)"], 
            a: 1 
        },
        { 
            id: 3, 
            type: "MCQ", 
            q: "An analyst claims the visualization implies that Variable X causes Variable Y. Is the analyst correct in this assertion?", 
            img: "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQwMCIgdmlld0JveD0iMCAwIDYwMCA0MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cmVjdCB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQwMCIgZmlsbD0iI2ZjZmNmYyIgc3Ryb2tlPSIjZTJlOGYwIiBzdHJva2Utd2lkdGg9IjEiLz4KICAgIDxsaW5lIHgxPSI1MCIgeTE9IjUwIiB4Mj0iNTUwIiB5Mj0iNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNTAiIHkxPSIxMDAiIHgyPSI1NTAiIHkyPSIxMDAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNTAiIHkxPSIxNTAiIHgyPSI1NTAiIHkyPSIxNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNTAiIHkxPSIyMDAiIHgyPSI1NTAiIHkyPSIyMDAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNTAiIHkxPSIyNTAiIHgyPSI1NTAiIHkyPSIyNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNTAiIHkxPSIzMDAiIHgyPSI1NTAiIHkyPSIzMDAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iMTAwIiB5MT0iNTAiIHgyPSIxMDAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iMTUwIiB5MT0iNTAiIHgyPSIxNTAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iMjAwIiB5MT0iNTAiIHgyPSIyMDAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iMjUwIiB5MT0iNTAiIHgyPSIyNTAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iMzAwIiB5MT0iNTAiIHgyPSIzMDAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iMzUwIiB5MT0iNTAiIHgyPSIzNTAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNDAwIiB5MT0iNTAiIHgyPSI0MDAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNDUwIiB5MT0iNTAiIHgyPSI0NTAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNTAwIiB5MT0iNTAiIHgyPSI1MDAiIHkyPSIzNTAiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8bGluZSB4MT0iNTAiIHkxPSIzNTAiIHgyPSI1NTAiIHkyPSIzNTAiIHN0cm9rZT0iIzQ3NTU2OSIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgICA8bGluZSB4MT0iNTAiIHkxPSI1MCIgeDI9IjUwIiB5Mj0iMzUwIiBzdHJva2U9IiM0NzU1NjkiIHN0cm9rZS13aWR0aD0iMiIvPgogICAgPHRleHQgeD0iMzAwIiB5PSIzODAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iIzQ3NTU2OSI+VmFyaWFibGUgWDwvdGV4dD4KICAgIDx0ZXh0IHg9IjE1IiB5PSIyMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iIzQ3NTU2OSIgdHJhbnNmb3JtPSJyb3RhdGUoLTkwLCAxNSwgMjAwKSI+VmFyaWFibGUgWTwvdGV4dD4KICAgIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjI1MCIgcj0iNSIgZmlsbD0iIzQ0NzJjNCIgLz4KICAgIDxjaXJjbGUgY3g9IjE1MCIgY3k9IjMwMCIgcj0iNSIgZmlsbD0iIzQ0NzJjNCIgLz4KICAgIDxjaXJjbGUgY3g9IjIwMCIgY3k9IjE5MCIgcj0iNSIgZmlsbD0iIzQ0NzJjNCIgLz4KICAgIDxjaXJjbGUgY3g9IjI1MCIgY3k9IjIwMCIgcj0iNSIgZmlsbD0iIzQ0NzJjNCIgLz4KICAgIDxjaXJjbGUgY3g9IjMwMCIgY3k9IjE2MCIgcj0iNSIgZmlsbD0iIzQ0NzJjNCIgLz4KICAgIDxjaXJjbGUgY3g9IjM1MCIgY3k9IjI1NSIgcj0iNSIgZmlsbD0iIzQ0NzJjNCIgLz4KICAgIDxjaXJjbGUgY3g9IjQwMCIgY3k9IjEzMCIgcj0iNSIgZmlsbD0iIzQ0NzJjNCIgLz4KICAgIDxjaXJjbGUgY3g9IjQ1MCIgY3k9Ijc1IiAgcj0iNSIgZmlsbD0iIzQ0NzJjNCIgLz4KPC9zdmc+", 
            options: ["Yes", "No"], 
            a: 1 
        },
        { 
            id: 4, 
            type: "MCQ", 
            q: "Which visualization type is commonly used to display the distribution of a continuous variable, with variable values on the x-axis and corresponding frequencies on the Y-axis?", 
            options: ["Option A: Column Chart", "Option B: Bar Chart", "Option C: Histogram", "Option D: Line Chart"], 
            optionImages: [
                "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDMwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cmVjdCB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgZmlsbD0iI2Y4ZmFmYyIgcng9IjgiLz4KICAgIDxsaW5lIHgxPSI0MCIgeTE9IjE2MCIgeDI9IjI2MCIgeTI9IjE2MCIgc3Ryb2tlPSIjNDc1NTY5IiBzdHJva2Utd2lkdGg9IjIiLz4KICAgIDxsaW5lIHgxPSI0MCIgeTE9IjMwIiB4Mj0iNDAiIHkyPSIxNjAiIHN0cm9rZT0iIzQ3NTU2OSIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgICA8cmVjdCB4PSI2MCIgeT0iMTEwIiB3aWR0aD0iMjAiIGhlaWdodD0iNTAiIGZpbGw9IiM0NDcyYzQiLz4KICAgIDxyZWN0IHg9IjEwMCIgeT0iNjAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMDAiIGZpbGw9IiM0NDcyYzQiLz4KICAgIDxyZWN0IHg9IjE0MCIgeT0iOTAiIHdpZHRoPSIyMCIgaGVpZ2h0PSI3MCIgZmlsbD0iIzQ0NzJjNCIvPgogICAgPHJlY3QgeD0iMTgwIiB5PSI1MCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjExMCIgZmlsbD0iIzQ0NzJjNCIvPgogICAgPHJlY3QgeD0iMjIwIiB5PSI4MCIgd2lkdGg9IjIwIiBoZWlnaHQ9IjgwIiBmaWxsPSIjNDQ3MmM0Ii8+Cjwvc3ZnPg==",
                "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDMwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cmVjdCB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgZmlsbD0iI2Y4ZmFmYyIgcng9IjgiLz4KICAgIDxsaW5lIHgxPSI1MCIgeTE9IjE3MCIgeDI9IjI3MCIgeTI9IjE3MCIgc3Ryb2tlPSIjNDc1NTY5IiBzdHJva2Utd2lkdGg9IjIiLz4KICAgIDxsaW5lIHgxPSI1MCIgeTE9IjMwIiB4Mj0iNTAiIHkyPSIxNzAiIHN0cm9rZT0iIzQ3NTU2OSIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgICA8cmVjdCB4PSI1MCIgeT0iNTAiIHdpZHRoPSIxODAiIGhlaWdodD0iMTUiIGZpbGw9IiM0NDcyYzQiLz4KICAgIDxyZWN0IHg9IjUwIiB5PSI4MCIgd2lkdGg9IjEyMCIgaGVpZ2h0PSIxNSIgZmlsbD0iIzQ0NzJjNCIvPgogICAgPHJlY3QgeD0iNzAiIHk9IjExMCIgd2lkdGg9IjIwMCIgaGVpZ2h0PSIxNSIgZmlsbD0iIzQ0NzJjNCIvPgogICAgPHJlY3QgeD0iNzAiIHk9IjE0MCIgd2lkdGg9IjE1MCIgaGVpZ2h0PSIxNSIgZmlsbD0iIzQ0NzJjNCIvPgo8L3N2Zz4=",
                "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDMwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cmVjdCB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgZmlsbD0iI2Y4ZmFmYyIgcng9IjgiLz4KICAgIDxsaW5lIHgxPSI0MCIgeTE9IjE2MCIgeDI9IjI2MCIgeTI9IjE2MCIgc3Ryb2tlPSIjNDc1NTY5IiBzdHJva2Utd2lkdGg9IjIiLz4KICAgIDxsaW5lIHgxPSI0MCIgeTE9IjMwIiB4Mj0iNDAiIHkyPSIxNjAiIHN0cm9rZT0iIzQ3NTU2OSIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgICA8cmVjdCB4PSI2MCIgeT0iNzAiIHdpZHRoPSI0MCIgaGVpZ2h0PSI5MCIgZmlsbD0iIzQ0NzJjNCIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjEiLz4KICAgIDxyZWN0IHg9IjEwMCIgeT0iMTEwIiB3aWR0aD0iNDAiIGhlaWdodD0iNTAiIGZpbGw9IiM0NDcyYzQiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8cmVjdCB4PSIxNDAiIHk9IjkwIiB3aWR0aD0iNDAiIGhlaWdodD0iNzAiIGZpbGw9IiM0NDcyYzQiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8cmVjdCB4PSIxODAiIHk9IjEzMCIgd2lkdGg9IjQwIiBoZWlnaHQ9IjMwIiBmaWxsPSIjNDQ3MmM0IiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMSIvPgogICAgPHRleHQgeD0iMTUwIiB5PSIxODAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjEwIiBmaWxsPSIjNjQ3NDhiIj5Db250aW51b3VzIEJpbnM8L3RleHQ+Cjwvc3ZnPg==",
                "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDMwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cmVjdCB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgZmlsbD0iI2Y4ZmFmYyIgcng9IjgiLz4KICAgIDxsaW5lIHgxPSI0MCIgeTE9IjE2MCIgeDI9IjI2MCIgeTI9IjE2MCIgc3Ryb2tlPSIjNDc1NTY5IiBzdHJva2Utd2lkdGg9IjIiLz4KICAgIDxsaW5lIHgxPSI0MCIgeTE9IjMwIiB4Mj0iNDAiIHkyPSIxNjAiIHN0cm9rZT0iIzQ3NTU2OSIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgICA8cG9seWxpbmUgcG9pbnRzPSI2MCwxMzAgMTAwLDgwIDE0MCwxMTAgMTgwLDUwIDIyMCw3MCAyNDAsMzAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzQ0NzJjNCIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSI2MCIgY3k9IjEzMCIgcj0iMyIgZmlsbD0iIzFlM2E1ZiIgLz4KICAgIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjgwIiByPSIzIiBmaWxsPSIjMWUzYTVmIiAvPgogICAgPGNpcmNsZSBjeD0iMTQwIiBjeT0iMTEwIiByPSIzIiBmaWxsPSIjMWUzYTVmIiAvPgogICAgPGNpcmNsZSBjeD0iMTgwIiBjeT0iNTAiIHI9IjMiIGZpbGw9IiMxZTNhNWYiIC8+CiAgICA8Y2lyY2xlIGN4PSIyMjAiIGN5PSI3MCIgcj0iMyIgZmlsbD0iIzFlM2E1ZiIgLz4KICAgIDxjaXJjbGUgY3g9IjI0MCIgY3k9IjMwIiByPSIzIiBmaWxsPSIjMWUzYTVmIiAvPgo8L3N2Zz4="
            ], 
            a: 2 
        },
        { 
            id: 5, 
            type: "MCQ", 
            q: "What data structure describes the following data?<br><strong>[“Aabid”, “Jesenia”, “Mark”]</strong>", 
            options: ["List", "Multi-dimensional", "Table", "Graph"], 
            a: 0 
        },
        { 
            id: 6, 
            type: "MCQ2", 
            q: "You need to create a data view based on aggregations for further visual analysis. Your data includes sales information for the past five years for food products at your company’s stores. Each product belongs to one category. For example milk belongs to dairy category. <br><br>The data view must meet the following requirements:<br>• Include all products and their associated categories<br>• Include sales sub-total for each category and year<br>• Display grand total of sales for each category<br>• Create a summary of each category for every year<br><br>Which <b>two</b> aggregation methods should you use to create the data view? (Choose 2)<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", 
            options: ["Pivoting", "Filtering", "Merging", "Grouping"], 
            a: [0, 3] 
        },
        { 
            id: 7, 
            type: "MTF", 
            q: "<strong>Statistical Metrics:</strong> You are performing descriptive analysis on quarterly sales data. <br><br>Move the appropriate statistical metrics from the list on the left to the correct row numbers (1-4) shown in the summary area of the table provided below.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", 
            img: "statistical_metrics_v2.png", 
            options: ["Row 1", "Row 2", "Row 3", "Row 4"], 
            labels: ["Sum", "Max", "Min", "Mode", "Average", "Median"], 
            a: { "Row 1": "Sum", "Row 2": "Max", "Row 3": "Min", "Row 4": "Mode" } 
        },
        { 
            id: 8, 
            type: "MCQ", 
            q: "Which data type can store a phrase or sentence?", 
            options: ["Integer", "Character", "String", "Boolean"], 
            a: 2 
        },
        { 
            id: 9, 
            type: "MCQ2", 
            q: "A coworker is having trouble joining two database tables, Table A and Table B, that were imported from CSV files. They say the tables have no common values.<br><br>You troubleshoot the problem and find that the <b>RowKey</b> values in TableA and the <b>RowID</b> values in TableB look identical (e.g., three numbers, a dash, and two letters).<br><br>Which <b>two</b> actions should you complete next? (Choose 2)<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", 
            options: [
                "Verify that the data in the database was imported as a numeric data type", 
                "Trim empty spaces from both of the valid characters", 
                "Visually compare the database values to the CSV values", 
                "Trim empty spaces from only the right side of the valid characters"
            ], 
            a: [1, 2] 
        },
        { 
            id: 10, 
            type: "MCQ2", 
            q: "Each month you need to automatically transform the data from two XML documents into a single flat file with columns and rows that Excel can open and interpret. The document names and structure remain constant. You know the relationship between the two XML documents.<br><br>Which <b>two</b> resources can you use? (Choose 2)<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", 
            options: ["Json", "Power Query for Excel (M)", "Microsoft Excel", "Python"], 
            a: [1, 3] 
        },
        { 
            id: 11, 
            type: "MCQ", 
            q: "What is the goal of data privacy and protection laws such as GDPR, FERPA, and HIPAA?", 
            options: [
                "To hold violators accountable for mishandling data", 
                "To tax companies that use private data", 
                "To ensure that companies openly share industry data", 
                "To protect companies from liability related to private data"
            ], 
            a: 0 
        },
        { 
            id: 12, 
            type: "MCQ", 
            q: "You have a small dataset that contains personally identifiable information (PII). You need to provide the data to an outside source for additional processing.<br><br>What could you do to protect the PII but still allow you to eventually relate the additional analysis to your original data?", 
            options: [
                "Employ pseudonymization on the PII and use the pseudonym as the key between the new and original datasets", 
                "Retain every text based PII in the original dataset but convert them to number-based features in the new dataset", 
                "Randomly shuffle the original dataset so that each given piece of PII is no longer associated with a particular user", 
                "Remove every instance of PII in the original dataset and add them back after the new dataset is retrieved"
            ], 
            a: 0 
        },
        { 
            id: 13, 
            type: "TF", 
            q: "The visualization and the data table depict housing prices in a region. For each statement about the visualization, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", 
            img: "housing_prices_color_final.png", 
            options: [
                "The visualization uses scaling manipulation", 
                "An annual increase of $25,000 occurs between 2016 and 2025", 
                "The visualization accurately depicts the housing prices shown"
            ], 
            a: [false, false, true] 
        },
        { 
            id: 14, 
            type: "MCQ", 
            q: "What is a raw data?", 
            options: ["Unprocessed Data", "Purely numerical Data", "Summarized Data", "Visualized Data"], 
            a: 0 
        },
        { 
            id: 15, 
            type: "MCQ", 
            q: "You are analyzing sales activity that occurs on national holidays.<br><br>What level of data granularity will enable you to perform the most precise analysis?", 
            options: ["Years", "Months", "Weeks", "Days", "Hours"], 
            a: 4 
        },
        { 
            id: 16, 
            type: "MCQ", 
            q: "What is an example of data cleaning?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Arranging Excel data rows in an order that is easy for a user to read", 
                "Ensuring that the data in a Word table uses a consistent font", 
                "Adding quotation marks to the beginning and end of a tab-delimited file", 
                "Removing non-printable characters from a comma-delimited file"
            ], 
            a: 3 
        },
        { 
            id: 17, 
            type: "MCQ", 
            q: "A popular social media site records and counts clicks, likes, and dislikes and other user interactions.<br><br>What type of data is collected?", 
            options: ["Continuous data", "Qualitative data", "Imputed data", "Big data"], 
            a: 3 
        },
        { 
            id: 18, 
            type: "MCQ", 
            q: "You work for a recreational sports company. The table shows the company's recreational vehicle sales.<br><br>You need to show how each vehicle type contributes to the company's total sales.<br><br>Which visualization should you use? Select the correct visualization in the answer area.", 
            img: "recreational_sales_table.png", 
            options: ["Option A", "Option B", "Option C", "Option D"], 
            optionImages: [
                "recreational_pie_chart.png", 
                "recreational_combo_chart.png", 
                "recreational_scatter_plot.png", 
                "recreational_bar_chart.png"
            ], 
            a: 0 
        },
        { 
            id: 19, 
            type: "MATRIX", 
            q: "From the data in the table below, you create a pivot table to show the combined number of certified virtual and in-person teachers for each class at each school.<br><br>Move the appropriate labels from the list on the left to the correct locations in the Pivot tables on the right. You may use each label once or not at all.", 
            img: "pivot_table_question.png",
            rows: ["Label 1", "Label 2", "Label 3", "Label 4"],
            cols: ["Data Analytics", "Networking", "In-Person", "Virtual", "School A", "School B"],
            a: [1, 0, 4, 5] 
        },
        { 
            id: 20, 
            type: "MCQ", 
            q: "Your company has summarized a large data set for the region you live in. You need to compare results from urban and rural communities within your region.<br><br>What is the fastest way to obtain the information?", 
            options: ["Collect a new Data Sample", "Review data from neighbouring regions", "Disaggregate the data", "Aggregate the data"], 
            a: 2 
        },
        { 
            id: 21, 
            type: "MCQ", 
            q: "What concept allows analysts to drill down into data and examine different levels of information that may be crucial in diagnostic analytics?", 
            options: ["Granularity", "Completeness", "Interpretability", "Transparency"], 
            a: 0 
        },
        { 
            id: 22, 
            type: "TF", 
            q: "For each statement about the machine learning select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", 
            options: [
                "Machine learning can predict the probability of Rain in a region by examining known weather patterns",
                "Machine learning can help determine whether a candidate will pass an exam without looking at historical scores",
                "Machine Learning can be used to automatically decline financial purchases based on previous purchase activity"
            ], 
            a: [true, false, true] 
        },
        { 
            id: 23, 
            type: "MCQ", 
            q: "Which Data structure have multiple rows and columns?", 
            options: ["Series", "Table", "One-dimensional Array", "List"], 
            a: 1 
        },
        { 
            id: 24, 
            type: "MCQ", 
            q: "In which scenario will artificial intelligence (AI) provide the greatest benefit?", 
            options: [
                "Predicting maintenance requirements for a international rental car company's fleet vehicles",
                "Determining the statistical mean, mode, and standard deviation of the grades for a class",
                "Recording daily sales for the three stores owned by one franchise owner",
                "Interpreting fundraising sales data for a college soccer team"
            ], 
            a: 0 
        },
        { 
            id: 25, 
            type: "MTF", 
            q: "Move each function from the list on the left to the correct description on the right.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", 
            options: ["Returns the largest value", "Returns the smallest value", "Returns the number of Values", "Returns the total of the values"], 
            labels: ["Max()", "Min()", "Count()", "Sum()"], 
            a: {
                "Returns the largest value": "Max()",
                "Returns the smallest value": "Min()",
                "Returns the number of Values": "Count()",
                "Returns the total of the values": "Sum()"
            }
        },
        { 
            id: 26, 
            type: "MCQ", 
            q: "Person A has 5 coins and person B has 10 coins.<br><br>Which type of data does the number of coins represent?", 
            options: ["Ordinal Data", "Metadata", "Qualitative data", "Quantitative data"], 
            a: 3 
        },
        { 
            id: 27, 
            type: "MCQ", 
            q: "You have a dataset that includes product review scores and demographic information about the reviewers. There are no subcategories associated with the demographic answers. The table shows a selection of the data.<br><br>Which Scenario is an example of disaggregating the dataset?", 
            img: "disaggregation_dataset_v3.png",
            options: [
                "By average and mode of the scores for each product grouped by the ethnicity of the reviewers",
                "Display the overall average and mode of all scores on a per-products basis",
                "Display a list of ethnicities that are included in the other option",
                "Display the overall average and mode of all scores and a count of all reviews"
            ], 
            a: 0 
        },
        { 
            id: 28, 
            type: "MCQ2", 
            q: "Which two concepts are commonly associated with artificial intelligence (AI) in data analytics?<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection. (Choose 2.)</span>", 
            options: ["Cost-Benefit Analysis", "Stakeholder Mapping", "Automation", "Machine Learning"], 
            a: [2, 3] 
        },
        { 
            id: 29, 
            type: "MCQ2", 
            q: "For which two reasons is it risky to make generalizations from limited sample data?<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection. (Choose 2.)</span>", 
            options: [
                "Limited data Samples are easier to collect",
                "A limited sample may not represent a larger population",
                "Findings from a smaller sample size may not be as precise",
                "Analyzing data from a smaller sample size is faster"
            ], 
            a: [1, 2] 
        },
        { 
            id: 30, 
            type: "MCQ", 
            q: "You are reviewing a database of restaurant menu items. The table below shows a selection of the data.<br>You need to display only items on the dessert menu with a type of cake.<br><br>What should you do to nondestructively limit the data display?", 
            img: "restaurant_menu_dataset.png",
            options: [
                "Group the data by menu and then group the data on the desert menu by type",
                "Delete all data that has a menu other than desert. Then delete all data that has a type other than cake",
                "Add two slicers, one for menu and one for type. Set the menu slicer to desert and the type slicer to cake",
                "Sort the data by menu and within each menu, Sort by type"
            ], 
            a: 2 
        },
        { 
            id: 31, 
            type: "MCQ", 
            q: "You want to show a friend your monthly budget breakdown to prove that most of your expenditure is food costs. You create a table that shows the flow of money as it moves one budget category to the next.<br><br>Which visualization type should you use to display your analysis based on the table shown?", 
            img: "budget_flow_dataset_v2.png",
            options: ["Time Series Chart", "Correlation Chart", "Sankey Chart", "Classification Chart"], 
            a: 2 
        },
        { 
            id: 32, 
            type: "MCQ", 
            q: "The Marketing team wants to know which market segment have the highest sales in the last year.<br><br>Which type of data analysis should they use?", 
            options: ["Perspective analytics", "Diagnostic Analytics", "Predictive Analytics", "Descriptive Analytics"], 
            a: 3 
        },
        { 
            id: 33, 
            type: "MCQ", 
            q: "You Believe Playing video game's increases the chance of man getting heart attack. In your research you notice equal evidences in favouring your hypothesis and opposed to it. You tried hours trying to identify the problems with the evidence opposed to your hypothesis, but readily accept the evidence in favor.<br><br>Which type of bias are you demonstrating?", 
            options: ["Motivated Reasoning", "Confirmation Bias", "Anchoring Bias", "Sampling Bias"], 
            a: 1 
        },
        { 
            id: 34, 
            type: "TF", 
            q: "<strong>Data Disaggregation:</strong> For each statement about data disaggregation, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", 
            options: [
                "Data disaggregation provides a summary of the data",
                "Data disaggregation combines data from different sources",
                "Data Disaggregation can clarify trends and patterns among subgroups"
            ], 
            a: [false, false, true] 
        },
        { 
            id: 35, 
            type: "MCQ", 
            q: "A college shows you the chart below to indicate that group A has performed significantly better than group B on a recent assignment. You don't know the sample size and the result of the statistical testing.<br><br>Which chart element creates the impression of a significant score difference?", 
            img: "scaling_manipulation_chart.png",
            options: [
                "The X-axis unit of Measurement", 
                "The Y-Axis unit of measurement", 
                "The Z-Axis Unit of Measurement", 
                "The Color differentiation"
            ], 
            a: 1 
        },
        { 
            id: 36, 
            type: "MCQ", 
            q: "You conduct a study to identify how much people exercise daily. You recruit all the study participants at the gyms.<br><br>Which type of bias are you demonstrating?", 
            options: ["Anchoring bias", "Confirmation Bias", "Motivated Bias", "Sampling bias"], 
            a: 3 
        },
        { 
            id: 37, 
            type: "MCQ", 
            q: "Which Statement correctly assigns a string to the variable that is name score?", 
            options: ["Score=true", "Score=String[7]", "Score=\"&\"", "Score= 7\""], 
            a: 2 
        },
        { 
            id: 38, 
            type: "MTF", 
            q: "You are using data analytics to help answer business questions about a new product your company released.<br><br>Move each type of data analytics from the list on the left to the correct question on the right.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", 
            options: [
                "Descriptive Analysis",
                "Diagnostic Analysis",
                "Predictive Analysis",
                "Perspective Analysis"
            ], 
            labels: [
                "What happened in the initial product release?",
                "Why did it happens?",
                "What might happen in future?",
                "What action should we take next?"
            ], 
            a: {
                "Descriptive Analysis": "What happened in the initial product release?",
                "Diagnostic Analysis": "Why did it happens?",
                "Predictive Analysis": "What might happen in future?",
                "Perspective Analysis": "What action should we take next?"
            }
        },
        { 
            id: 39, 
            type: "MCQ", 
            q: "You run a t-test with alpha value of 5% (a= 0.05) in order to test an alternative hypothesis (H1). You finish the analysis and discover the P-value is 0.017.<br><br>What can you conclude about the null hypothesis (H0)?", 
            options: [
                "You modify the null hypothesis (H0)",
                "You accept the null hypothesis (H0)",
                "You fail to reject the null Hypothesis (H0)",
                "You reject the null hypothesis (H0)"
            ], 
            a: 3 
        },
        { 
            id: 40, 
            type: "MCQ", 
            q: "You have a comma-delimited file with 100,000 rows and 200 columns of phone sales data. One column represents the Phone manufacturer.<br><br>You need to analyze all sales data for a specific manufacturer.<br><br>Which technique should you use?", 
            options: ["Deleting", "Transposing", "Truncating", "Filtering"], 
            a: 3 
        }
    ],
    "da_mock2": [
        { 
            id: 1, 
            type: "MCQ", 
            q: "What is an example of data cleaning?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Arranging Excel data rows in an order that is easy for a user to read", 
                "Ensuring that the data in a Word table uses a consistent font", 
                "Adding quotation marks to the beginning and end of a tab-delimited file", 
                "Removing non-printable characters from a comma-delimited file"
            ], 
            a: 3 
        },
        { 
            id: 2, 
            type: "MCQ", 
            q: "You believe playing video games increases a person's chance of having a heart attack. In your research. you notice equal evidence in favor of this hypothesis and opposed to it. You spend hours trying to identify the problems with the evidence opposed to your hypothesis, but readily accept the evidence in favor.<br><br>Which type of bias are you demonstrating?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Motivated Reasoning", 
                "Anchoring bias", 
                "Sampling bias", 
                "Confirmation Bias"
            ], 
            a: 3 
        },
        { 
            id: 3, 
            type: "MCQ", 
            q: "What is metadata?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Statistics", 
                "The text content of a message", 
                "Numerical facts", 
                "The context that give data meaning"
            ], 
            a: 3 
        },
        { 
            id: 4, 
            type: "TF", 
            q: "The visualization and data table depict housing price in a region. For each statement about the visualization, select True or False.<br><span style='font-size: 13px; color: #64748b;'>1 point</span><br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection</span>", 
            img: "housing_prices_color_final.png", 
            options: [
                "The visualization accurately depict the housing prices shown in the table", 
                "The scaling of the graph is misleading", 
                "An increase of $25000 occurs Each year"
            ], 
            a: [true, false, false] 
        },
        { 
            id: 5, 
            type: "MCQ", 
            q: "Person A has 5 coins and person B has 10 coins.<br><br>Which type of data does the number of coins represent?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Qualitative data", 
                "Quantitative data", 
                "Ordinal data", 
                "Metadata"
            ], 
            a: 1 
        },
        { 
            id: 6, 
            type: "MCQ", 
            q: "Which data structure describes the following data<br><br><div class='code-snippet' style='margin:0;'>[\"Aabid\",\"jesenia\",\"Mark\"]</div><br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Graph", 
                "Table", 
                "List", 
                "Multi-dimensional array"
            ], 
            a: 2 
        },
        { 
            id: 7, 
            type: "MCQ", 
            q: "A popular social media site records and count clicks, likes, and dislikes, and other user interactions<br><br>What type of data is collected?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Continuous data", 
                "Imputed Data", 
                "Qualitative Data", 
                "Big Data"
            ], 
            a: 3 
        },
        { 
            id: 8, 
            type: "MCQ", 
            q: "Which data type can store a phrase or sentence?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Integer", 
                "String", 
                "Boolean", 
                "Character"
            ], 
            a: 1 
        },
        { 
            id: 9, 
            type: "MTF", 
            q: "You are using data analytics to help answer business questions about a new product your company released. Move each type of data analytics from the list on the left to the correct question on the right.<br><span style='font-size: 13px; color: #64748b;'>4 points</span><br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", 
            options: ["Descriptive analytics", "Diagnostic analytics", "Predictive analytics", "Prescriptive analytics"], 
            labels: [
                "Why did this happen?", 
                "What action should we take next", 
                "What might happen in the future", 
                "What happened in the initial product relese"
            ], 
            a: {
                "Descriptive analytics": "What happened in the initial product relese",
                "Diagnostic analytics": "Why did this happen?",
                "Predictive analytics": "What might happen in the future?",
                "Prescriptive analytics": "What action should we take next"
            } 
        },
        { 
            id: 10, 
            type: "MCQ", 
            q: "You have a small dataset that contains personally identifiable information (PII). You need to provide the data to an outside source for additional processing. What could you do to protect the Pll but still allow you to eventually relate the additional analysis to your original data?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Remove every instance of Pll in the original dataset and add them back after the new dataset is retrieved.", 
                "Retain every text-based Pll in the original dataset but convert them to number-based features in the new dataset.", 
                "Employ pseudonymization on the Pll and use the pseudonym as the key between the new and original datasets.", 
                "Randomly shuffle the original dataset so that each given piece of Pll is no longer associated. with a particular user"
            ], 
            a: 2 
        },
        { 
            id: 11, 
            type: "MCQ", 
            q: "You are reviewing a database of restaurant menu items. The table below shows a selection of the data. You need to display only items on the Dessert menu With a Type of Cake. What should you do to nondestructively limit the data display?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            img: "restaurant_menu_dataset.png",
            options: [
                "Group the data by Menu and then group data on the Dessert menu by Type", 
                "Add two slicers, one for Menu and one for Type. Set the Menu slicer to Dessert and the Type slicer to Cake.", 
                "Sort the data by Menu and within each Menu, sort by Type.", 
                "Delete all data that has a Menu other than Dessert. Then delete all data that has a Type other than Cake."
            ], 
            a: 1 
        },
        { 
            id: 12, 
            type: "MCQ2", 
            q: "You need to create a data view based on aggregations for further visual analysis. Your data includes sales information for the past five years for food products at your company's stores. Each product belongs to one category. For example, milk belongs to the Dairy category<br><br> The data view must meet the following requirements:<br> * Include all products and their associated categories.<br> * Include sales subtotals for each category and year. <br> * Display a grand total of sales for each category.<br> * Create a summary of each category for every year.<br><br>Which <strong>two</strong> aggregation method should you use to create the data view (choose 2)<br><span style='font-size: 13px; color: #64748b;'>1 point</span><br><br><span style='font-size: 15px; font-style: italic;'>Note : You will receive partial credit for each correct selection</span>", 
            options: ["Filtering", "Pivoting", "Merging", "Grouping"], 
            a: [1, 3] 
        },
        { 
            id: 13, 
            type: "MCQ", 
            q: "What concept allow analytics to drill down into data and examine level of information that maybe crucial in diagnostic analytics?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Completeness", 
                "Interpretability", 
                "Granularity", 
                "Transparency"
            ], 
            a: 2 
        },
        { 
            id: 14, 
            type: "MCQ", 
            q: "You work for a recreational sports company. The table shows the company's recreational vehicle sales. You need to show how each vehicle type contributes to the company's total sales.<br><br> Which visualization should you use? Select the correct visualization in the answer area.<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            img: "recreational_sales_table.png", 
            options: ["Option A", "Option B", "Option C", "Option D"], 
            optionImages: [
                "recreational_pie_chart.png", 
                "recreational_combo_chart.png", 
                "recreational_scatter_plot.png", 
                "recreational_bar_chart.png"
            ], 
            a: 0 
        },
        { 
            id: 15, 
            type: "MCQ", 
            q: "Which visualization type is commonly used to display the distribution of a continuous variable. with variable values on the x-axis and corresponding frequencies on the y-axis? Select the correct visualization type in the answer area.<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: ["Option 1", "Option 2", "Option 3", "Option 4"], 
            optionImages: [
                "dist_column_chart.png", 
                "dist_line_chart.png", 
                "dist_histogram.png", 
                "dist_bar_chart.png"
            ], 
            a: 2 
        },
        { 
            id: 16, 
            type: "TF", 
            q: "For each statement about data disaggregation ,Select True or False<br><span style='font-size: 15px; font-style: italic;'>Note: You will Receive partial credit for each correct selection</span><br><span style='font-size: 13px; color: #64748b;'>3 points</span>", 
            options: [
                "Data disaggregation provides a summary of data",
                "Data disaggregation combines data from multiple sources",
                "Data disaggregation can clarify trends and pattern among subgroups"
            ], 
            a: {
                "Data disaggregation provides a summary of data": "False",
                "Data disaggregation combines data from multiple sources": "False",
                "Data disaggregation can clarify trends and pattern among subgroups": "True"
            } 
        },
        { 
            id: 17, 
            type: "MCQ", 
            q: "The marketing team want to know which market segment had the highest sales last year. Which type of data analytics should they use?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Diagnostic analytics", 
                "Descriptive analytics", 
                "Predictive analytics", 
                "Prescriptive analytics"
            ], 
            a: 1 
        },
        { 
            id: 18, 
            type: "MCQ", 
            q: "You have a dataset that includes product review scores and demographic information about the reviewers_ There are no subcategories associated with the demographic answers, The table shows a selection of the data, Which scenario is an example of disaggregating the dataset?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            img: "disaggregation_dataset_v4.png",
            options: [
                "Display the overall average and mode of all scores on a PW-product basis.",
                "Display a list of ethnicities that are included in the Other option.",
                "Display average and mode of the scores for each product grouped by the ethnicity of the reviewers.",
                "Display the overall average and mode of all scores and a count of all reviews."
            ], 
            a: 2 
        },
        { 
            id: 19, 
            type: "MCQ", 
            q: "A colleague shows you the chart below to indicate that Group A has performed significantly better than Group B on a recent assignment. You do not know the sample size or the results of statistical testing. Which chart element creates the impression Of a significant score difference?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            img: "q19_misleading_chart.png", 
            options: [
                "The x-axis units of measurement", 
                "The y-axis units of measurement", 
                "The z-axis units of measurement", 
                "The color differentiation"
            ], 
            a: 1 
        },
        { 
            id: 20, 
            type: "MCQ", 
            q: "You have produced a linear regression model which calculates house prices based on area taken up by the house, the number of bedrooms, and the number of bathrooms:<br><br><b>House price = (100 + 0.5 * square meters + 8 * bedrooms + 10 * bathrooms) * 1,000</b><br><br>What would the model predict for the price of a house with 800 square meters, 4 bedrooms and 3 bathrooms?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "538,000",
                "552,000",
                "562,000",
                "572,000"
            ], 
            a: 2 
        },
        { 
            id: 21, 
            type: "MCQ", 
            q: "You want to show a friend your monthly budget breakdown to prove that most of your expenditure is food costs. You create a table that shows the flow of money as it moves one budget category to the next.<br><br>Which visualization type should you use to display your analysis based on the table shown?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            img: "budget_sankey_table.png",
            options: [
                "Time Series Chart",
                "Classification tree",
                "Correlation matrix",
                "Sankey Diagram"
            ], 
            a: 3 
        },
        { 
            id: 22, 
            type: "DROPDOWN", 
            q: "You are analyzing customer satisfaction scores between on-line purchases and in-store purchases. Satisfaction scores are entered on a scale from 1 (extremely unsatisfied) to 10 (extremely satisfied).<br><br>Select the correct metric from the drop-down list for each statement.<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span><br><span style='font-size: 13px; color: #64748b;'>4 points</span>", 
            code: "The most frequent satisfaction score was 5 for online customer and 9 for in-store customers: [b1]<br><br>The average score for online customers was 6.4 and the average score for in-store customers was 7.0: [b2]<br><br>The score at the midpoint between the lowest and the highest scores was 6 for online customers and 7 for in-store customers: [b3]<br><br>The online scores vary from the average by 2.3 and the in-store variance is 1.9: [b4]",
            options: [
                ["Count", "Mean", "Median", "Mode", "Std Dev", "Max", "Min"],
                ["Count", "Mean", "Median", "Mode", "Std Dev", "Max", "Min"],
                ["Count", "Mean", "Median", "Mode", "Std Dev", "Max", "Min"],
                ["Count", "Mean", "Median", "Mode", "Std Dev", "Max", "Min"]
            ], 
            a: ["Mode", "Mean", "Median", "Std Dev"]
        },
        { 
            id: 23, 
            type: "MCQ2", 
            q: "You have a comma-delimited file with 100,000 rows and 200 columns of phone sales data. One column represents the phone manufacturer. You need to analyze all sales data for one manufacturer. Which two techniques should you use? (Choose 2.)<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Filtering",
                "Transposing",
                "Slicing",
                "Deleting",
                "Truncating"
            ], 
            a: [0, 2] 
        },
        { 
            id: 24, 
            type: "DROPDOWN", 
            q: "You are analyzing statistics for online and in-store purchases with data collected over the past year. Data collected includes surveys from 300 instore customers and 300 online customers. Based on the data visualization below, identify which statements about customer purchases over the last year are correct and which statements are incorrect.<br><br>For each statement about online and in-store purchases, select True if the statement is correct or False if the statement is incorrect.<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span><br><span style='font-size: 13px; color: #64748b;'>4 points</span>", 
            img: "purchase_stats_chart.png",
            code: "In-store customers spent more money than online customers: [b1]<br><br>Online customers have a larger variance in how much they spend: [b2]<br><br>The difference between the largest amount spent and the smallest amount spent is higher for in-store customers: [b3]<br><br>The amount spent the most often is the same for online and in-store customers: [b4]",
            options: [
                ["True", "False"],
                ["True", "False"],
                ["True", "False"],
                ["True", "False"]
            ], 
            a: ["False", "True", "False", "True"]
        },
        { 
            id: 25, 
            type: "MCQ2", 
            q: "Each month, you need to automatically transform the data from two XML documents into a single flat file with columns and rows that Excel can open and interpret. The document names and structure remain constant. You know the relationships between the two XML documents.<br><br>Which two resources can you use? (Choose 2.)<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each Correct selection.</span><br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Python",
                "Microsoft Word",
                "Power Query for Excel (M)",
                "JSON"
            ], 
            a: [0, 2] 
        },
        { 
            id: 26, 
            type: "MCQ2", 
            q: "For which two reason is risky to make generalization from limited sample data?<br><span style='font-size: 13px; color: #64748b;'>2 points</span>", 
            options: [
                "Findings from a smaller sample size may not be as precise",
                "Analyzing data from a smaller sample size is faster",
                "A limited sample may not represent a larger population",
                "Limited data samples are easier to collect."
            ], 
            a: [0, 2] 
        },
        { 
            id: 27, 
            type: "MCQ2", 
            q: "A coworker is having trouble joining two database tables, TableA and TableB, that were imported from CSV files. They say the tables have no common values.<br><br>You need to troubleshoot the problem. You look at the data in the original CSV files and find that the RowKey values in the TableA file and the RowID values in the TableB file look identical. Both have three numbers followed by a dash (-) and two letters.<br><br>Which two actions should you complete next? (Choose 2.)<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span><br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Visually compare the database values to the CSV values.",
                "Trim empty spaces from only the right side of the valid characters",
                "Verify that the data in the database was imported as a numeric data type",
                "Trim empty spaces from both Sides of the valid characters."
            ], 
            a: [0, 3] 
        },
        { 
            id: 28, 
            type: "MCQ", 
            q: "Your company has summarized a large set for the region you live in. You need to compare the result from Urban and Rural communities Within your region.<br><br>What is the fastest way to obtain this information?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Review data from neighboring regions",
                "Aggregate the data",
                "Disaggregate the data",
                "Collect new data sample"
            ], 
            a: 2 
        },
        { 
            id: 29, 
            type: "MATRIX", 
            q: "From the data in the table below, you create a PivotTable to show the combined number of certified virtual and in-person teachers for each class at each school.<br><br>Move the appropriate labels from the list on the left to the correct locations in the PivotTable on the right. You may use each label once or not at all.<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span><br><span style='font-size: 13px; color: #64748b;'>4 points</span>", 
            img: "pivot_table_matching.png",
            rows: ["Label 1", "Label 2", "Label 3", "Label 4"],
            cols: ["Data Analytics", "Networking", "In-Person", "Virtual", "School A", "School B"],
            a: [1, 0, 4, 5] 
        },
        { 
            id: 30, 
            type: "MCQ3", 
            q: "Select three ways that machine learning algorithms are used in data analysis. (Choose 3)<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span><br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Time series Analysis",
                "Anomaly Detection",
                "Regulated Data Analysis",
                "Small Data Set Analysis",
                "Singular Historical Events",
                "Data Classification"
            ], 
            a: [0, 1, 5] 
        },
        { 
            id: 31, 
            type: "MCQ", 
            q: "What is one goal of data privacy and protection laws such as GDPR, FERPA, and HIPAA?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "To hold violators accountable for mishandling data",
                "To ensure that companies openly share industry data",
                "To protect companies from liability related to private data",
                "To tax companies that use private data"
            ], 
            a: 0 
        },
        { 
            id: 32, 
            type: "MCQ", 
            q: "What is a raw data<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Visualized data",
                "Purely numeric data",
                "Summarized data",
                "Unprocessed data"
            ], 
            a: 3 
        },
        { 
            id: 33, 
            type: "MCQ", 
            q: "The data structure has multiple rows and multiple column<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "One-dimensional array",
                "Series",
                "Table",
                "List"
            ], 
            a: 2 
        },
        { 
            id: 34, 
            type: "MCQ", 
            q: "A conduct of study identify how many people exercise daily. You recruit all the study participants at gyms. Which types of bias are you demonstrating?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Anchoring bias", 
                "Motivated reasoning", 
                "Sampling bias", 
                "Confirmation bias"
            ], 
            a: 2 
        },
        { 
            id: 35, 
            type: "MCQ", 
            q: "You run a t-test with an alpha value of 5% (α = 0.05) in order to test an alternative hypothesis (H₁). You finish the analysis and discover that the p-value is 0.017. What can you conclude about the null hypothesis (H₀)?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "You reject the null hypothesis (H₀)", 
                "You Fail to reject the null hypothesis (H₀)", 
                "You modify the null hypothesis (H₀)", 
                "You accept the null hypothesis (H₀)"
            ], 
            a: 0 
        },
        { 
            id: 36, 
            type: "MCQ", 
            q: "In which scenario will artificial Intelligence (AI) Provides the greatest benefit?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Interpreting fundraising sales data for a college team",
                "Recording daily sales for three stores owned by one franchise owner",
                "Determining the statistical mean, median, mode, and standard deviation of the grade for a class",
                "Predicting maintenance requirement for an international rental car's companies fleet vehicles"
            ], 
            a: 3 
        },
        { 
            id: 37, 
            type: "MCQ", 
            q: "You are analyzing sales that occurs on a national holiday.<br>What level of data granularity will enable you to perform the most precise analysis?<br><span style='font-size: 13px; color: #64748b;'>1 point</span>", 
            options: [
                "Years",
                "Months",
                "Weeks",
                "Days",
                "Hours"
            ], 
            a: 4 
        },
        { 
            id: 38, 
            type: "MATRIX", 
            q: "You are performing descriptive analytics on quarterly sales data. Move the appropriate statistical metrics from the list on the left to the correct locations on the right.<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct response.</span><br><span style='font-size: 13px; color: #64748b;'>4 points</span>", 
            img: "quarterly_sales_metrics.png",
            rows: ["Metric 1", "Metric 2", "Metric 3", "Metric 4"],
            cols: ["Average", "Max", "Median", "Mode", "Sum", "Min"],
            a: [4, 1, 5, 3] 
        }
    ],
    "da_mock3": [
        {
                "id": 1,
                "type": "MCQ",
                "q": "You are analyzing customer ice cream preferences across different regions. Based on the following pie chart, which flavor is the most preferred by the sample population?",
                "img": "ice_cream_preference_chart.png",
                "options": [
                        "Vanilla",
                        "Chocolate",
                        "Strawberry",
                        "Mango"
                ],
                "a": 1
        },
        {
                "id": 2,
                "type": "MCQ",
                "q": "What is the primary reason for performing data disaggregation on a summarized sales report?",
                "options": [
                        "To hide seasonal fluctuations",
                        "To identify underlying trends at a granular level (e.g., specific stores)",
                        "To increase the security of the data",
                        "To reduce the file size of the report"
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
                "a": [
                        0,
                        1,
                        2
                ]
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
                "a": [
                        true,
                        false,
                        true
                ]
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
                "a": [
                        2,
                        3
                ]
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
                "a": [
                        0,
                        2
                ]
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
                "q": "What is a primary characteristic of Big Data that makes it difficult to manage with traditional database systems?",
                "options": [
                        "It only contains text",
                        "It has low velocity and volume",
                        "It has extreme volume, velocity, and variety",
                        "It is only collected via paper surveys"
                ],
                "a": 2
        },
        {
                "id": 22,
                "type": "MCQ",
                "q": "You run a t-test with a significance level of \u03b1 = 0.01. Which p-value would allow you to reject the null hypothesis?",
                "options": [
                        "0.05",
                        "0.011",
                        "0.008",
                        "0.10"
                ],
                "a": 2
        },
        {
                "id": 23,
                "type": "MCQ",
                "q": "Based on the Lead-to-Sale Rate chart, which channel has the highest conversion efficiency despite having lower total volume?",
                "img": "lead_conversion_efficiency.png",
                "options": [
                        "Organic Search",
                        "Direct Marketing",
                        "Social Media",
                        "Referrals"
                ],
                "a": 3
        },
        {
                "id": 24,
                "type": "MCQ",
                "q": "In the context of data analysis, how is 'Information' defined?",
                "options": [
                        "Any collection of numbers",
                        "Interpreted and processed data that provides meaning or context",
                        "Raw signals collected from hardware",
                        "A database that has not been queried yet"
                ],
                "a": 1
        },
        {
                "id": 25,
                "type": "MCQ",
                "q": "Which of the following is a classic example of Machine Learning in Predictive Analysis?",
                "options": [
                        "A calculator showing the result of 1+1",
                        "A streaming service recommending music based on your listening history",
                        "A computer shutting down on a timer",
                        "A printer showing a 'Low Ink' warning"
                ],
                "a": 1
        },
        {
                "id": 26,
                "type": "DD",
                "q": "Complete the data organization description by choosing the correct operations.<br><br>First, we [b1] the data to hide irrelevant categories. Then, we [b2] the list alphabetically. Finally, we [b3] a specific slice of the data for investigation.",
                "options": [
                        "Filter",
                        "Sort",
                        "Slicing"
                ],
                "a": [
                        "Filter",
                        "Sort",
                        "Slicing"
                ]
        },
        {
                "id": 27,
                "type": "MCQ",
                "q": "When writing a logical statement like <code>IF(Sales > 5000)</code>, what is the resulting data type for that specific output?",
                "options": [
                        "Integer",
                        "String",
                        "Boolean",
                        "Float"
                ],
                "a": 2
        },
        {
                "id": 28,
                "type": "TF",
                "q": "Evaluate these statements about Data Mining.",
                "options": [
                        "Data mining is used to identify anomalies and pattern correlations in large datasets.",
                        "Data mining requires an analyst to manually read every single record.",
                        "Data mining helps in summarizing complex data into actionable insights."
                ],
                "a": [
                        true,
                        false,
                        true
                ]
        }
]
};
