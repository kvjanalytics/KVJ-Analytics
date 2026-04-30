import json
import re

variants = [
    {
        "id": 21,
        "type": "MCQ2",
        "q": "You work on a team that is developing a lottery application.<br><br>You need to write code that generates a random number that meets the following requirements:<br>\u2022 The number is a multiple of 10.<br>\u2022 The lowest number is 10.<br>\u2022 The highest number is 200.<br><br>Which two code segments will meet the requirements? Each correct answer presents a complete solution. (Choose 2.)<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>",
        "options": [
            "from random import randint\nprint(randint(1, 20) * 10)",
            "from random import randint\nprint(randint(0, 20) * 10)",
            "from random import randrange\nprint(randrange(0, 200, 10))",
            "from random import randrange\nprint(randrange(10, 210, 10))"
        ],
        "a": [0, 3]
    },
    {
        "id": 22,
        "type": "DROPDOWN",
        "q": "You are writing a Python program for a weather app to determine if a temperature (temp) is Freezing, Cold, or Warm.<br><br>Complete the code by selecting the correct code segment from each drop-down list.<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "temp = int(input(\"Enter the temperature: \"))\nstatus = \"Unknown\"\n[b1]\n    status = \"Freezing\"\n[b2]\n    status = \"Cold\"\n[b3]\n    status = \"Warm\"\nprint(\"It is \" + status + \".\")",
        "options": [
            [
                "if temp < 0:",
                "if temp > 0:"
            ],
            [
                "elif temp < 30:",
                "if temp < 30:",
                "elif temp > 30:",
                "if temp > 30:"
            ],
            [
                "else:",
                "elif:"
            ]
        ],
        "a": [
            "if temp < 0:",
            "elif temp < 30:",
            "else:"
        ]
    },
    {
        "id": 23,
        "type": "MCQ",
        "q": "You write the following code to determine an employee's salary bonus based on their base salary and years of experience:<br><br>What value will print?",
        "code": "salary = 4000\nexperience = 5\n\nif salary > 5000 and experience >= 5:\n    salary += 1000\nelif salary >= 3000 and experience > 3:\n    salary += 500\nelse:\n    salary -= 200\n\nprint(salary)",
        "options": [
            "4500",
            "5000",
            "3800",
            "4000"
        ],
        "a": 0
    },
    {
        "id": 24,
        "type": "MTF",
        "q": "You need to identify the data types of various operations.<br><br>Move the appropriate data types from the list on the left to the correct operations on the right. You may use each data type once, more than once, or not at all.<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>",
        "labels": [
            "int",
            "float",
            "str",
            "bool"
        ],
        "options": [
            "type(3.14)",
            "type(-42)",
            "type(\"False\")",
            "type(True)"
        ],
        "a": {
            "type(3.14)": "float",
            "type(-42)": "int",
            "type(\"False\")": "str",
            "type(True)": "bool"
        }
    },
    {
        "id": 25,
        "type": "MCQ2",
        "q": "A fitness company is creating a program that allows runners to log their steps. The program will calculate the distance run based on stride length.<br><br>You write the following Python code. Line numbers are included for reference only.<br><br>You need to define the two required functions.<br><br>Which two code segments should you use for line 01 and line 04? Each correct answer presents part of the solution. (Choose 2.)<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "01\n02     name = input(\"What is your name? \")\n03     return name\n04\n05     distance = steps * stride_length\n06     return distance\n07 step_count = int(input(\"How many steps did you run? \"))\n08 stride = 2.5\n09 runner = get_runner()\n10 total_distance = calc_distance(step_count, stride)\n11 print(runner, \", you ran \", total_distance, \" feet.\")",
        "options": [
            "01 def get_runner():",
            "01 def get_runner(runner):",
            "01 def get_runner(name):",
            "04 def calc_distance():",
            "04 def calc_distance(steps, stride):",
            "04 def calc_distance(steps, stride_length):"
        ],
        "a": [
            0,
            5
        ]
    },
    {
        "id": 26,
        "type": "MCQ",
        "q": "Review the following code:<br><br>What is the output of the print statement?",
        "code": "x = \"truck\"\ny = \"suv\"\nz = \"sedan\"\n\ndata = \"{1} and {0} and {2}\"\nprint(data.format(z, y, x))",
        "options": [
            "sedan and truck and suv",
            "truck and suv and sedan",
            "suv and sedan and truck",
            "suv and truck and sedan"
        ],
        "a": 2
    },
    {
        "id": 27,
        "type": "TF",
        "q": "For each statement about try statements, select True or False.",
        "options": [
            "An else clause in a try statement only executes if no exceptions were raised.",
            "A try statement can have a finally clause without an except clause.",
            "A try statement can have a finally clause and an except clause.",
            "The finally clause is skipped if an exception is caught."
        ],
        "a": [
            True,
            True,
            True,
            False
        ]
    },
    {
        "id": 28,
        "type": "TF",
        "q": "The following function calculates a discounted price. Line numbers are included for reference only.<br><br>For each statement, select True or False.<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "01 def calc_discount(price, pct):\n02     return price - (price * pct)\n03 retail = input(\"Enter the retail price: \")\n04 discount = input(\"Enter the discount decimal: \")\n05 result = calc_discount(retail, discount)\n06 print(\"The final price is \" + str(result))",
        "options": [
            "The code will generate a TypeError in line 03 and line 04.",
            "The code will generate an error in line 02 and line 05 because strings cannot be multiplied like floats.",
            "The code will correctly output data to the console."
        ],
        "a": [
            False,
            True,
            False
        ]
    },
    {
        "id": 29,
        "type": "TF",
        "q": "Review the following code segment:<br><br><code>f = open(\"data.csv\", \"w\")<br>f.write(\"ID,Name,Role\\n\")<br>f.close()</code>",
        "options": [
            "A file named data.csv is created if it does not exist.",
            "The data in the file will be appended to existing data.",
            "Other code can open the file after this code runs."
        ],
        "a": [
            True,
            False,
            True
        ]
    },
    {
        "id": 30,
        "type": "MCQ2",
        "q": "You are creating an HR script that accepts input from the user and outputs the data in a comma-delimited format.<br><br>You write the following code to accept input:<br><br><code>name = input(\"Enter employee name: \")<br>age = int(input(\"Enter age: \"))</code><br><br>The output must meet the following requirements:<br>\u2022 Enclose strings in double quotes.<br>\u2022 Do not enclose numbers in quotes or other characters.<br>\u2022 Separate items by commas.<br><br>You need to complete the code to meet the requirements.<br><br>Which two code segments could you use? Each correct answer presents a complete solution. (Choose 2.)<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "options": [
            "print('\"' + name + '\",' , age)",
            "print('\"{0}\",{1}'.format(name, age))",
            "print(name + ',' + age)",
            "print(f'\"{name}\", {age}')"
        ],
        "a": [
            1,
            3
        ]
    },
    {
        "id": 31,
        "type": "MTF",
        "q": "You are writing a Python application that includes multiple operations on the same line of code. You need to determine the correct order of precedence.<br><br>Move the operations from the list on the left to the correct locations on the right, with highest precedence at the top and lowest precedence at the bottom.<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct response.</span>",
        "headers": [
            "Operations",
            "Operations in Order"
        ],
        "placeholder": "<span style='color: #64748b; font-size: 13px;'>Operation Type</span>",
        "labels": [
            "Addition and Subtraction",
            "Logical AND",
            "Exponents (**)",
            "Multiplication and Division",
            "Parentheses ()",
            "Unary positive, negative, bitwise NOT"
        ],
        "options": [
            "<span style='white-space:nowrap;'>Highest precedence</span>",
            "\u200b",
            "\u200b\u200b",
            "\u200b\u200b\u200b",
            "\u200b\u200b\u200b\u200b",
            "\u200b\u200b\u200b\u200b\u200b"
        ],
        "a": {
            "<span style='white-space:nowrap;'>Highest precedence</span>": "Parentheses ()",
            "\u200b": "Exponents (**)",
            "\u200b\u200b": "Unary positive, negative, bitwise NOT",
            "\u200b\u200b\u200b": "Multiplication and Division",
            "\u200b\u200b\u200b\u200b": "Addition and Subtraction",
            "\u200b\u200b\u200b\u200b\u200b": "Logical AND"
        }
    },
    {
        "id": 32,
        "type": "TF",
        "q": "You are writing a function that applies a discount to a retail price. The function has the following requirements:<br>\u2022 If no value is specified for the discount percentage, it starts at 10.<br>\u2022 If is_member is True, the discount percentage is doubled.<br><br>You write the following code. Line numbers are included for reference only.",
        "code": "01 def apply_discount(price, is_member, discount):\n02     if is_member == True:\n03         discount = discount * 2\n04     price = price - (price * discount / 100)\n05     return price\n06 discount = 5\n07 price = 100\n08 final_price = apply_discount(price, True, discount)",
        "options": [
            "To meet the requirements, you must change line 01 to: def apply_discount(price, is_member, discount = 10):",
            "If you do not change line 01 and the function is called with only two parameters, an error occurs.",
            "Line 03 will permanently modify the value of the variable discount declared at line 06."
        ],
        "a": [
            True,
            True,
            False
        ]
    },
    {
        "id": 33,
        "type": "MTF",
        "q": "You need to identify the results of performing various slicing operations on the following sequence structure:<br><br><code>digits = \"0123456789\"</code>",
        "options": [
            "digits[2:5]",
            "digits[:4]"
        ],
        "labels": [
            "345",
            "234",
            "1234",
            "0123",
            "2345",
            "01234"
        ],
        "a": {
            "digits[2:5]": "234",
            "digits[:4]": "0123"
        }
    },
    {
        "id": 34,
        "type": "SHORT",
        "q": "Review the following code segment:<br><br>How many lines of output does the code print?<br><span style='font-size: 12px; font-style: italic;'>Enter the number as an integer.</span>",
        "code": "total = 0\nn = 10\nwhile (n > 0):\n    total += n\n    print(total)\n    n -= 2\n    if n == 4:\n        break",
        "a": "3"
    },
    {
        "id": 35,
        "type": "DROPDOWN",
        "q": "You find errors while evaluating the following code. Line numbers are included for reference only. You need to correct the code at line 03 and line 06.",
        "code": "<div class='code-snippet'>01 chars = ['A', 'B', 'C', 'D', 'E']<br>02 index = 0<br>03 [b1]<br>04 &nbsp;&nbsp;&nbsp;&nbsp;print(chars[index])<br>05 <br>06 &nbsp;&nbsp;&nbsp;&nbsp;[b2]<br>07 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;break<br>08 &nbsp;&nbsp;&nbsp;&nbsp;else :<br>09 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index += 1</div>",
        "options": [
            [
                "while (index < 5) :",
                "while [index < 5]",
                "while (index < 6) :",
                "while [index < 6]"
            ],
            [
                "if chars[index] == 'D' :",
                "if chars[index] == 'D'",
                "if chars(index) = 'D' :",
                "if chars(index) != 'D'"
            ]
        ],
        "a": [
            "while (index < 5) :",
            "if chars[index] == 'D' :"
        ]
    },
    {
        "id": 36,
        "type": "MCQ",
        "q": "You are developing a script to calculate net profit. The formula utilizes exponents and floor division.<br><br>What is the final value of the <code>net_profit</code> variable?",
        "code": "revenue = 100\nexpenses = 4\n\nnet_profit = revenue - expenses * 2 ** 2 // 3 + (revenue % 9)",
        "options": [
            "96",
            "88",
            "110",
            "45"
        ],
        "a": 0
    },
    {
        "id": 37,
        "type": "MCQ",
        "q": "You are building a geometry application. You run the script and encounter a NameError on line 03.<br><br>What is causing the error?",
        "code": "01 \n02 def calculate_hypotenuse(a, b):\n03     c_squared = math.pow(a, 2) + math.pow(b, 2)\n04     return math.sqrt(c_squared)\n05 print(calculate_hypotenuse(3, 4))",
        "options": [
            "You need to import the math module.",
            "The math.pow function only accepts floating-point numbers.",
            "The c_squared variable must be globally declared.",
            "The calculate_hypotenuse function must return an integer."
        ],
        "a": 0
    },
    {
        "id": 38,
        "type": "MCQ",
        "q": "You are creating an automated email generation script for a real estate agency:<br><br>What is the output of the print statement?",
        "code": "city = \"Tokyo\"\nrooms = 2\nrent = 1200.50\n\nemail = \"The {1}-room apartment in {0} rents for ${2}.\"\nprint(email.format(city, rooms, rent))",
        "options": [
            "The 2-room apartment in Tokyo rents for $1200.50.",
            "The {rooms}-room apartment in {city} rents for ${rent}.",
            "A syntax error occurs because the variables are different data types.",
            "The Tokyo-room apartment in 2 rents for $1200.50."
        ],
        "a": 0
    },
    {
        "id": 39,
        "type": "TF",
        "q": "You are implementing a robust data pipeline that must handle errors properly. For each statement about exception handling, select True or False.",
        "options": [
            "You can use the 'raise' keyword to intentionally trigger an exception.",
            "A try block can be nested inside another try block or except block.",
            "Variables defined inside a try block are strictly local and cannot be accessed in the except block.",
            "If an exception is raised inside a try block, the program will always crash immediately."
        ],
        "a": [
            True,
            True,
            False,
            False
        ]
    },
    {
        "id": 40,
        "type": "TF",
        "q": "You are building an application that needs to securely log diagnostic data into a text file:<br><br><code>with open(\"server_logs.txt\", \"w\") as log_file:<br>&nbsp;&nbsp;&nbsp;&nbsp;log_file.write(\"System start\\n\")</code><br><br>For each statement, select True or False.",
        "options": [
            "Using the with statement ensures the file is automatically closed when the block ends.",
            "The mode \"w\" guarantees that existing data in the file will not be overwritten.",
            "If server_logs.txt does not exist, the code will throw a FileNotFoundError."
        ],
        "a": [
            True,
            False,
            False
        ]
    }
]

with open("c:/Users/kj anand/Downloads/Quiz DD/quiz_data.js", "r", encoding="utf-8") as f:
    text = f.read()

def get_array_block(key, text):
    start_match = re.search(r'"' + key + r'"\s*:\s*\[', text)
    if not start_match: return None, -1, -1
    start_idx = start_match.end() - 1
    bracket_count = 0
    in_string = False
    escape = False
    for i in range(start_idx, len(text)):
        char = text[i]
        if escape:
            escape = False
            continue
        if char == '\\':
            escape = True
            continue
        if char == '"' and not in_string:
            in_string = True
            continue
        elif char == '"' and in_string:
            in_string = False
            continue
        if not in_string:
            if char == '[':
                bracket_count += 1
            elif char == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    return text[start_idx:i+1], start_idx, i+1
    return None, -1, -1

mock3_text, _, _ = get_array_block("mock3", text)
mock3_list = json.loads(mock3_text)

# We know mock1 is comprised of mock3_list[:20] + variants
mock1_first_20 = mock3_list[:20]

# Ensure the mock1_first_20 IDs are exactly 1-20
for i, q in enumerate(mock1_first_20):
    q["id"] = i + 1

# Ensure variants IDs are exactly 21-40
for i, q in enumerate(variants):
    q["id"] = i + 21

full_mock1 = mock1_first_20 + variants

_, m1_start, m1_end = get_array_block("mock1", text)

# Re-serialize
new_mock1_text = json.dumps(full_mock1, indent=4)

# Indentation fix
new_mock1_inner = new_mock1_text.strip()[1:-1].strip()
new_mock1_text = "[\n" + "\n".join("        " + line if line.strip() else line for line in new_mock1_inner.split("\n")) + "\n    ]"

text = text[:m1_start] + new_mock1_text + text[m1_end:]

with open("c:/Users/kj anand/Downloads/Quiz DD/quiz_data.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully generated and injected mock1 full array!")
