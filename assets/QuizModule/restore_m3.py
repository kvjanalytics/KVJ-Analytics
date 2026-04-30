import os
import re

filepath = r"c:\Users\kj anand\Downloads\Quiz DD\Module-3.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Insertion 1: read vs readlines, CSV module
insertion_point_1 = """            <h3>Writing to a File</h3>"""

missing_content_part1 = """            <h3>Reading from a File</h3>
            <p>You can read the entire file using <code>.read()</code>, or line-by-line using <code>.readlines()</code>.</p>
            <pre>
<span class="keyword">with</span> <span class="function">open</span>(<span class="string">"data.txt"</span>, <span class="string">"r"</span>) <span class="keyword">as</span> file:
    content = file.<span class="function">read</span>()
    <span class="function">print</span>(content)
</pre>

            <div class="practice-card coding-practice">
                <h3>Coding Practice: File Read</h3>
                <p><strong>Challenge:</strong> Write code to open <code>"log.txt"</code> in <strong>read</strong> mode using <code>with</code>, and print its contents using <code>.read()</code>. (Assume the file contains 'Error 404')</p>
                <textarea id="coding-ans-read" placeholder="# Write your code here..."></textarea>
                <div class="btn-group">
                    <button class="btn-run" onclick="runSkulpt('read')">Run & Check</button>
                    <button class="btn-reset" onclick="resetCodingPractice('read')">Reset</button>
                </div>
                <div id="coding-output-read" class="live-output-box"></div>
                <div id="coding-feedback-read" class="feedback"></div>
            </div>

"""

if "<h3>Reading from a File</h3>" not in content:
    content = content.replace(insertion_point_1, missing_content_part1 + insertion_point_1)


insertion_point_2 = """            <div class="quiz-cta">
                <h3>Module 3 Assessment</h3>"""

missing_content_part2 = """            <div class="section-header">
                <h2>3. Working with CSV Files</h2>
            </div>
            <p>CSV (Comma Separated Values) is a common format for storing tabular data. Python has a built-in <code>csv</code> module.</p>
            <pre>
<span class="keyword">import</span> csv

<span class="keyword">with</span> <span class="function">open</span>(<span class="string">"sales.csv"</span>, <span class="string">"r"</span>) <span class="keyword">as</span> file:
    reader = csv.<span class="function">reader</span>(file)
    <span class="keyword">for</span> row <span class="keyword">in</span> reader:
        <span class="function">print</span>(row)
</pre>

            <div class="practice-card coding-practice">
                <h3>Coding Practice: CSV Module</h3>
                <p><strong>Challenge:</strong> Import the <code>csv</code> module and print <code>csv.__name__</code> to confirm it's loaded.</p>
                <textarea id="coding-ans-csv" placeholder="# Write your code here..."></textarea>
                <div class="btn-group">
                    <button class="btn-run" onclick="runSkulpt('csv')">Run & Check</button>
                    <button class="btn-reset" onclick="resetCodingPractice('csv')">Reset</button>
                </div>
                <div id="coding-output-csv" class="live-output-box"></div>
                <div id="coding-feedback-csv" class="feedback"></div>
            </div>
"""

if "<h2>3. Working with CSV Files</h2>" not in content:
    content = content.replace(insertion_point_2, missing_content_part2 + insertion_point_2)

# Update JS block
js_additions = """
                if (type === 'input' && result.includes('Welcome to')) isCorrect = true;
                if (type === 'append' && result === 'a') isCorrect = true;
                if (type === 'read' && result.includes('Error 404')) isCorrect = true;
                if (type === 'csv' && result.includes('csv')) isCorrect = true;"""

js_target = """
                if (type === 'input' && result.includes('Welcome to')) isCorrect = true;
                if (type === 'append' && result === 'a') isCorrect = true;"""

# To support the fake file "log.txt", we need to inject it into Skulpt's builtinFiles
js_skulpt_setup = """        function builtinRead(x) {
            if (x === "log.txt") return "Error 404";
            if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
                throw "File not found: '" + x + "'";
            return Sk.builtinFiles["files"][x];
        }"""
        
js_skulpt_target = """        function builtinRead(x) {
            if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
                throw "File not found: '" + x + "'";
            return Sk.builtinFiles["files"][x];
        }"""

if js_target in content:
    content = content.replace(js_target, js_additions)
if js_skulpt_target in content:
    content = content.replace(js_skulpt_target, js_skulpt_setup)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Module-3.html successfully updated!")
