import os
import re

files = ["Module-1.html", "Module-2.html", "Module-3.html", "Module-4.html", "Module-5.html", "Module-6.html"]
directory = r"c:\Users\kj anand\Downloads\Quiz DD"

new_run_skulpt = """        function runSkulpt(id, expected, checks = null) {
            const prog = document.getElementById(`coding-ans-${id}`).value;
            const outputDiv = document.getElementById(`coding-output-${id}`);
            const feedback = document.getElementById(`coding-feedback-${id}`);
            
            outputDiv.innerHTML = "";
            outputDiv.classList.add('active');
            feedback.style.display = "none";
            feedback.className = "feedback";

            let outputText = "";
            
            Sk.configure({
                output: function(text) { 
                    outputDiv.appendChild(document.createTextNode(text));
                    outputDiv.scrollTop = outputDiv.scrollHeight;
                    outputText += text; 
                },
                read: function(x) {
                    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
                        throw "File not found: '" + x + "'";
                    return Sk.builtinFiles["files"][x];
                }
            });

            const myPromise = Sk.misceval.asyncToPromise(function() {
                return Sk.importMainWithBody("<stdin>", false, prog, true);
            });

            myPromise.then(function(mod) {
                if (!outputDiv.innerHTML) outputDiv.innerText = outputText;
                
                const cleanOutput = outputText.trim().toLowerCase();
                const cleanExpected = expected ? expected.trim().toLowerCase() : "";

                let isCorrect = true;
                let errorMsg = "";

                // 1. Output Check
                if (cleanExpected && !cleanOutput.includes(cleanExpected)) {
                    isCorrect = false;
                    errorMsg = `Expected output "${expected}" not found.`;
                }

                // 2. Variable State Check
                if (isCorrect && checks) {
                    try {
                        const checkObj = typeof checks === 'string' ? JSON.parse(checks) : checks;
                        for (const [varName, expectedVal] of Object.entries(checkObj)) {
                            if (mod.$d[varName] === undefined) {
                                isCorrect = false;
                                errorMsg = `Variable "${varName}" is missing.`;
                                break;
                            }
                            const userVal = Sk.ffi.remapToJs(mod.$d[varName]);
                            if (JSON.stringify(userVal) !== JSON.stringify(expectedVal)) {
                                isCorrect = false;
                                errorMsg = `The value of "${varName}" is incorrect. Expected ${expectedVal}.`;
                                break;
                            }
                        }
                    } catch (e) {
                        console.error("Check Error:", e);
                    }
                }

                if (isCorrect) {
                    feedback.innerHTML = "✓ Correct! Your code works perfectly. 🎉";
                    feedback.className = "feedback correct";
                    if (typeof triggerConfetti === 'function') triggerConfetti();
                } else {
                    feedback.innerHTML = `✗ ${errorMsg || "Wrong! Try again."}`;
                    feedback.className = "feedback wrong";
                }
                feedback.style.display = "block";
            }, function(err) {
                outputDiv.innerText += "\\n" + err.toString();
                feedback.innerHTML = "✗ Error in your code!";
                feedback.className = "feedback wrong";
                feedback.style.display = "block";
            });
        }
"""

# Simple but effective regex to find the runSkulpt function block
pattern = re.compile(r"function runSkulpt\s*\(id, expected.*?\)\s*\{(?:[^{}]*|\{[^{}]*\})*\}", re.DOTALL)

for filename in files:
    path = os.path.join(directory, filename)
    if not os.path.exists(path):
        print(f"File {filename} not found.")
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the existing runSkulpt function
    new_content = pattern.sub(new_run_skulpt, content)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes made to {filename} (pattern might not have matched)")
