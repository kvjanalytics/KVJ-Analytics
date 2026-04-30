import os

filepath = r"c:\Users\kj anand\Downloads\Quiz DD\Module-5.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Insertion: finally block
insertion_point = """            <div class="quiz-cta">
                <h3>Module 5 Assessment</h3>"""

missing_content = """            <h3>The finally Block</h3>
            <p>The <code>finally</code> block executes regardless of whether an error occurred or not. It's often used for cleanup tasks like closing files.</p>
            <pre>
<span class="keyword">try</span>:
    <span class="function">print</span>(x)
<span class="keyword">except</span>:
    <span class="function">print</span>(<span class="string">"Variable not found"</span>)
<span class="keyword">finally</span>:
    <span class="function">print</span>(<span class="string">"Execution complete"</span>)
</pre>

            <div class="practice-card coding-practice">
                <h3>Coding Practice: Finally</h3>
                <p><strong>Challenge:</strong> Add a <code>finally</code> block that prints <code>"Done"</code>.</p>
                <div class="partial-fix-box">
                    <pre>try:
    print(10/0)
except:
    print("Error")</pre>
                    <span class="partial-fix-line"><input type="text" id="coding-ans-finally" style="width: 80px;" placeholder="finally:"></span>
                    <pre>    print("Done")</pre>
                </div>
                <div class="btn-group">
                    <button class="btn-run" onclick="runSkulpt('finally')">Run & Check</button>
                    <button class="btn-reset" onclick="resetCodingPractice('finally')">Reset</button>
                </div>
                <div id="coding-output-finally" class="live-output-box"></div>
                <div id="coding-feedback-finally" class="feedback"></div>
            </div>

"""

if "<h3>The finally Block</h3>" not in content:
    content = content.replace(insertion_point, missing_content + insertion_point)

# Update JS block
js_additions = """
        const CHALLENGE_DATA = {
            'syntax': { expected: "Fixed", isPartialFix: true, template: (val) => `if 10 > 5${val}\\n    print('Fixed')` },
            'except': { expected: "Caught" },
            'finally': { expected: "Error\\nDone", isPartialFix: true, template: (val) => `try:\\n    print(10/0)\\nexcept:\\n    print("Error")\\n${val}\\n    print("Done")` }
        };"""

js_target = """
        const CHALLENGE_DATA = {
            'syntax': { expected: "Fixed", isPartialFix: true, template: (val) => `if 10 > 5${val}\\n    print('Fixed')` },
            'except': { expected: "Caught" }
        };"""

if js_target in content:
    content = content.replace(js_target, js_additions)
else:
    print("WARNING: Could not find JS injection target in M5.")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Module-5.html successfully updated!")
