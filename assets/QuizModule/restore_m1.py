import os
import re

filepath = r"c:\Users\kj anand\Downloads\Quiz DD\Module-1.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add missing content before "1. Understanding Data Types"
insertion_point = "<h2>1. Understanding Data Types</h2>"

missing_content_part1 = """<h2>Introduction to Variables</h2>
            </div>
            <p>A variable is a container for storing data values. In Python, variables are created the moment you first assign a value to them.</p>
            <pre>
name = <span class="string">"Alice"</span>
age = <span class="number">25</span>
<span class="function">print</span>(name, age)
</pre>
            <div class="interaction-box">
                <strong>Naming Rules:</strong> Variable names must start with a letter or underscore, can contain numbers, and are case-sensitive. Use <code>snake_case</code> for readability.
            </div>

            <div class="practice-card coding-practice">
                <h3>Coding Practice: Variables</h3>
                <p><strong>Challenge:</strong> Create a variable called <code>company_name</code> and assign it the string <code>"Google"</code>. Then print it.</p>
                <textarea id="coding-ans-var" placeholder="# Write your code here..."></textarea>
                <div class="btn-group">
                    <button class="btn-run" onclick="runSkulpt('var')">Run & Check</button>
                    <button class="btn-reset" onclick="resetCodingPractice('var')">Reset</button>
                </div>
                <div id="coding-output-var" class="live-output-box"></div>
                <div id="coding-feedback-var" class="feedback"></div>
            </div>

            <div class="section-header">
                <h2>Basic Output</h2>
            </div>
            <p>The <code>print()</code> function is used to output text and variables to the screen.</p>
            <pre>
<span class="function">print</span>(<span class="string">"Hello, World!"</span>)
</pre>

            <div class="practice-card coding-practice">
                <h3>Coding Practice: Print</h3>
                <p><strong>Challenge:</strong> Print the phrase <code>"Learning Python"</code> exactly as shown.</p>
                <textarea id="coding-ans-print" placeholder="# Write your code here..."></textarea>
                <div class="btn-group">
                    <button class="btn-run" onclick="runSkulpt('print')">Run & Check</button>
                    <button class="btn-reset" onclick="resetCodingPractice('print')">Reset</button>
                </div>
                <div id="coding-output-print" class="live-output-box"></div>
                <div id="coding-feedback-print" class="feedback"></div>
            </div>

            <div class="section-header">
                <h2>Arithmetic Operators</h2>
            </div>
            <p>Python supports common math operations like addition <code>+</code>, subtraction <code>-</code>, multiplication <code>*</code>, division <code>/</code>, and exponentiation <code>**</code>.</p>
            <pre>
total = <span class="number">10</span> + <span class="number">5</span>
<span class="function">print</span>(total)
</pre>

            <div class="practice-card coding-practice">
                <h3>Coding Practice: Arithmetic</h3>
                <p><strong>Challenge:</strong> Calculate <code>50 * 3</code> and print the result.</p>
                <textarea id="coding-ans-math" placeholder="# Write your code here..."></textarea>
                <div class="btn-group">
                    <button class="btn-run" onclick="runSkulpt('math')">Run & Check</button>
                    <button class="btn-reset" onclick="resetCodingPractice('math')">Reset</button>
                </div>
                <div id="coding-output-math" class="live-output-box"></div>
                <div id="coding-feedback-math" class="feedback"></div>
            </div>

            <div class="section-header">
                """

if "<h2>Introduction to Variables</h2>" not in content:
    content = content.replace(insertion_point, missing_content_part1 + insertion_point)

# Now we need to update the JavaScript to handle 'var', 'print', 'math'
js_additions = """
                if (type === 'int' && result.includes("<class 'int'>") && code.includes('250')) isCorrect = true;
                if (type === 'float' && result.includes("<class 'float'>") && code.includes('0.15')) isCorrect = true;
                if (type === 'str' && result.includes("<class 'str'>")) isCorrect = true;
                if (type === 'bool' && result.includes("<class 'bool'>") && code.includes('False')) isCorrect = true;
                if (type === 'var' && result.includes('Google') && code.includes('company_name')) isCorrect = true;
                if (type === 'print' && result.includes('Learning Python')) isCorrect = true;
                if (type === 'math' && result.includes('150') && code.includes('*')) isCorrect = true;"""

js_target = """
                if (type === 'int' && result.includes("<class 'int'>") && code.includes('250')) isCorrect = true;
                if (type === 'float' && result.includes("<class 'float'>") && code.includes('0.15')) isCorrect = true;
                if (type === 'str' && result.includes("<class 'str'>")) isCorrect = true;
                if (type === 'bool' && result.includes("<class 'bool'>") && code.includes('False')) isCorrect = true;"""

if js_target in content:
    content = content.replace(js_target, js_additions)
else:
    print("WARNING: Could not find JS injection target in M1.")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Module-1.html successfully updated!")
