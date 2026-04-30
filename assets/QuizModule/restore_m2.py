import os
import re

filepath = r"c:\Users\kj anand\Downloads\Quiz DD\Module-2.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Insertion 1: elif statements, logical operators
insertion_point_1 = """            <div class="quiz-cta">
                <h3>Module 2 Assessment</h3>"""

missing_content_part1 = """            <h3>elif Statement</h3>
            <p>The <code>elif</code> (else if) statement allows you to check multiple conditions sequentially.</p>
            <pre>
score = <span class="number">85</span>
<span class="keyword">if</span> score >= <span class="number">90</span>:
    <span class="function">print</span>(<span class="string">"Grade A"</span>)
<span class="keyword">elif</span> score >= <span class="number">80</span>:
    <span class="function">print</span>(<span class="string">"Grade B"</span>)
<span class="keyword">else</span>:
    <span class="function">print</span>(<span class="string">"Grade C"</span>)
</pre>

            <div class="practice-card coding-practice">
                <h3>Coding Practice: elif</h3>
                <p><strong>Challenge:</strong> Write a program that checks <code>temp = 25</code>. If temp is > 30, print <code>"Hot"</code>. Elif temp > 20, print <code>"Warm"</code>. Else print <code>"Cold"</code>.</p>
                <textarea id="coding-ans-elif" placeholder="# Write your code here..."></textarea>
                <div class="btn-group">
                    <button class="btn-run" onclick="runSkulpt('elif')">Run & Check</button>
                    <button class="btn-reset" onclick="resetCodingPractice('elif')">Reset</button>
                </div>
                <div id="coding-output-elif" class="live-output-box"></div>
                <div id="coding-feedback-elif" class="feedback"></div>
            </div>

            <div class="section-header">
                <h2>2. Logical Operators</h2>
            </div>
            <p>Logical operators combine multiple conditions together.</p>
            <ul class="content-list">
                <li><code>and</code>: True if BOTH conditions are true</li>
                <li><code>or</code>: True if AT LEAST ONE condition is true</li>
                <li><code>not</code>: Reverses the condition</li>
            </ul>

            <div class="interaction-box">
                <strong>Example:</strong>
                <pre style="margin: 10px 0; padding: 15px;">
<span class="keyword">if</span> age >= <span class="number">18</span> <span class="keyword">and</span> has_id:
    <span class="function">print</span>(<span class="string">"Entry allowed"</span>)</pre>
            </div>

            <div class="section-header">
                <h2>3. Loops</h2>
            </div>
            <p>Loops allow you to run the same block of code multiple times.</p>

            <h3>The for Loop</h3>
            <p>Used to iterate over a sequence (like a string, list, or range of numbers).</p>
            <pre>
<span class="keyword">for</span> i <span class="keyword">in</span> <span class="function">range</span>(<span class="number">3</span>):
    <span class="function">print</span>(<span class="string">"Iteration"</span>, i)
</pre>

            <div class="practice-card coding-practice">
                <h3>Coding Practice: for loop</h3>
                <p><strong>Challenge:</strong> Use a <code>for</code> loop and <code>range(5)</code> to print the word <code>"Python"</code> 5 times.</p>
                <textarea id="coding-ans-for" placeholder="# Write your code here..."></textarea>
                <div class="btn-group">
                    <button class="btn-run" onclick="runSkulpt('for')">Run & Check</button>
                    <button class="btn-reset" onclick="resetCodingPractice('for')">Reset</button>
                </div>
                <div id="coding-output-for" class="live-output-box"></div>
                <div id="coding-feedback-for" class="feedback"></div>
            </div>

            <h3>The while Loop</h3>
            <p>Used to repeat code as long as a condition remains True.</p>
            <pre>
count = <span class="number">0</span>
<span class="keyword">while</span> count < <span class="number">3</span>:
    <span class="function">print</span>(<span class="string">"Counting"</span>)
    count += <span class="number">1</span>
</pre>

            <div class="practice-card coding-practice">
                <h3>Coding Practice: while loop</h3>
                <p><strong>Challenge:</strong> Write a <code>while</code> loop that runs while <code>x < 2</code> and prints <code>x</code>. Assume <code>x = 0</code> initially and increment <code>x</code> by 1.</p>
                <textarea id="coding-ans-while" placeholder="# Write your code here..."></textarea>
                <div class="btn-group">
                    <button class="btn-run" onclick="runSkulpt('while')">Run & Check</button>
                    <button class="btn-reset" onclick="resetCodingPractice('while')">Reset</button>
                </div>
                <div id="coding-output-while" class="live-output-box"></div>
                <div id="coding-feedback-while" class="feedback"></div>
            </div>
            
            <div class="section-header">
                <h2>4. Break and Continue</h2>
            </div>
            <p><strong>Break:</strong> Exits the loop completely.</p>
            <p><strong>Continue:</strong> Skips the rest of the current iteration and moves to the next one.</p>

"""

if "<h2>2. Logical Operators</h2>" not in content:
    content = content.replace(insertion_point_1, missing_content_part1 + insertion_point_1)

# Update JS block
js_additions = """
                if (type === 'if' && result === 'Expensive') isCorrect = true;
                if (type === 'ifelse' && (result === 'Pass' || result === 'Fail')) isCorrect = true;
                if (type === 'elif' && result.includes('Warm')) isCorrect = true;
                if (type === 'for' && result.split('Python').length === 6) isCorrect = true;
                if (type === 'while' && result.includes('0') && result.includes('1')) isCorrect = true;"""

js_target = """
                if (type === 'if' && result === 'Expensive') isCorrect = true;
                if (type === 'ifelse' && (result === 'Pass' || result === 'Fail')) isCorrect = true;"""

if js_target in content:
    content = content.replace(js_target, js_additions)
else:
    print("WARNING: Could not find JS injection target in M2.")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Module-2.html successfully updated!")
