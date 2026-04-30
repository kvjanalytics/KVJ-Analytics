import os
import re

filepath = r"c:\Users\kj anand\Downloads\Quiz DD\Module-4.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Insertion: Arguments and Return Values
insertion_point = """            <div class="quiz-cta">
                <h3>Module 4 Assessment</h3>"""

missing_content = """            <h3>Arguments and Parameters</h3>
            <p>Parameters allow you to pass data into a function. Arguments are the actual values passed.</p>
            <pre>
<span class="keyword">def</span> <span class="function">greet_user</span>(name):
    <span class="function">print</span>(<span class="string">"Hello, "</span> + name)

greet_user(<span class="string">"Alice"</span>)
</pre>

            <div class="practice-card coding-practice">
                <h3>Coding Practice: Arguments</h3>
                <p><strong>Challenge:</strong> Define <code>multiply(a, b)</code> that prints <code>a * b</code>. Call it with <code>4</code> and <code>5</code>.</p>
                <textarea id="coding-ans-args" placeholder="# Write your code here..."></textarea>
                <div class="btn-group">
                    <button class="btn-run" onclick="runSkulpt('args')">Run & Check</button>
                    <button class="btn-reset" onclick="resetCodingPractice('args')">Reset</button>
                </div>
                <div id="coding-output-args" class="live-output-box"></div>
                <div id="coding-feedback-args" class="feedback"></div>
            </div>

            <h3>Return Values</h3>
            <p>Functions can output a result back to the caller using the <code>return</code> keyword.</p>
            <pre>
<span class="keyword">def</span> <span class="function">add</span>(x, y):
    <span class="keyword">return</span> x + y

result = add(<span class="number">10</span>, <span class="number">20</span>)
<span class="function">print</span>(result)
</pre>

            <div class="practice-card coding-practice">
                <h3>Coding Practice: Return</h3>
                <p><strong>Challenge:</strong> Define a function <code>get_ten()</code> that returns the number <code>10</code>. Print the function call.</p>
                <textarea id="coding-ans-return" placeholder="# Write your code here..."></textarea>
                <div class="btn-group">
                    <button class="btn-run" onclick="runSkulpt('return')">Run & Check</button>
                    <button class="btn-reset" onclick="resetCodingPractice('return')">Reset</button>
                </div>
                <div id="coding-output-return" class="live-output-box"></div>
                <div id="coding-feedback-return" class="feedback"></div>
            </div>

"""

if "<h3>Arguments and Parameters</h3>" not in content:
    content = content.replace(insertion_point, missing_content + insertion_point)

# Update JS block
js_additions = """
                if (type === 'comment' && code.includes('#')) isCorrect = true;
                if (type === 'def' && result === 'Visible') isCorrect = true;
                if (type === 'args' && result.includes('20') && code.includes('def multiply')) isCorrect = true;
                if (type === 'return' && result.includes('10') && code.includes('return 10')) isCorrect = true;"""

js_target = """
                if (type === 'comment' && code.includes('#')) isCorrect = true;
                if (type === 'def' && result === 'Visible') isCorrect = true;"""

if js_target in content:
    content = content.replace(js_target, js_additions)
else:
    print("WARNING: Could not find JS injection target in M4.")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Module-4.html successfully updated!")
