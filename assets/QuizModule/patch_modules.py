import os
import re

# THE DEFINITIVE SMART VALIDATION ENGINE
NEW_RUNSKULPT_LOGIC = """
        function runSkulpt(id) {
            const config = CHALLENGE_DATA[id] || {};
            const expected = config.expected || "";
            const checks = config.checks || null;

            let prog = "";
            if (config.isPartialFix) {
                const input = document.getElementById(`coding-ans-${id}`);
                const val = input ? input.value : "";
                prog = config.template(val);
            } else {
                prog = document.getElementById(`coding-ans-${id}`).value;
            }

            const outputDiv = document.getElementById(`coding-output-${id}`);
            const feedback = document.getElementById(`coding-feedback-${id}`);
            
            outputDiv.innerHTML = "";
            outputDiv.classList.add('active');
            feedback.style.display = "none";
            feedback.className = "feedback";

            // SPECIAL BYPASS FOR MODULE 6 (os/datetime)
            if (config.isSpecial) {
                let isValid = true;
                (config.modules || []).forEach(m => {
                    if (!prog.includes(`import ${m}`) && !prog.includes(`from ${m}`)) isValid = false;
                });
                const stripTags = (s) => s.replace(/[<>]/g, '').replace(/\\s+/g, ' ').trim().toLowerCase();
                if (!stripTags(prog).includes(stripTags(expected))) isValid = false;
                if (isValid) {
                    outputDiv.innerText = expected;
                    feedback.innerHTML = "✓ Correct! Your code works perfectly. 🎉";
                    feedback.className = "feedback correct";
                    if (typeof triggerConfetti === 'function') triggerConfetti();
                } else {
                    outputDiv.innerText = `Error: Please ensure you import ${config.modules.join(' and ')} and print "${expected}".`;
                    feedback.innerHTML = "✗ Wrong! Expected result not found.";
                    feedback.className = "feedback wrong";
                }
                feedback.style.display = "block";
                return;
            }

            let outputText = "";
            let userInputs = [];
            
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
                },
                inputfun: function(prompt) {
                    return new Promise((resolve) => {
                        const container = document.createElement('div');
                        container.className = 'colab-input-container';
                        container.innerHTML = `
                            <span class="colab-prompt">${prompt}</span>
                            <input type="text" class="colab-input" autocomplete="off">
                        `;
                        outputDiv.appendChild(container);
                        const inputField = container.querySelector('.colab-input');
                        inputField.focus();
                        inputField.addEventListener('keydown', (e) => {
                            if (e.key === 'Enter') {
                                const val = inputField.value;
                                userInputs.push(val);
                                container.remove();
                                outputDiv.appendChild(document.createTextNode(prompt + val + "\\n"));
                                outputText += prompt + val + "\\n";
                                resolve(val);
                            }
                        });
                    });
                }
            });

            const myPromise = Sk.misceval.asyncToPromise(function() {
                return Sk.importMainWithBody("<stdin>", false, prog, true);
            });

            myPromise.then(function(mod) {
                if (!outputDiv.innerHTML) outputDiv.innerText = outputText;
                
                let isCorrect = true;
                let errorMsg = "";

                // 1. Structural Checks
                if (config.isComment && !prog.includes('#')) {
                    isCorrect = false; errorMsg = "Missing Comment! Use the '#' symbol.";
                } else if (config.isDoc && (!prog.includes('\"\"\"') && !prog.includes("'''"))) {
                    isCorrect = false; errorMsg = "Missing Docstring! Use triple quotes.";
                } else if (config.isDef && !prog.includes('def ')) {
                    isCorrect = false; errorMsg = "Function definition missing.";
                }

                // 2. Resilient Output Check (Smart Logic)
                const stripTags = (s) => s.replace(/[<>]/g, '').replace(/\\s+/g, ' ').trim().toLowerCase();
                const strippedOutput = stripTags(outputText);
                const allowedExpected = Array.isArray(expected) ? expected : [expected];
                const isOutputCorrect = !expected || allowedExpected.some(exp => strippedOutput.includes(stripTags(exp)));

                if (isCorrect && expected && !isOutputCorrect) {
                    isCorrect = false;
                    errorMsg = `Expected output matching "${allowedExpected.join('" or "')}" not found.`;
                }

                // 3. Ultra-Robust Variable State Check
                if (isCorrect && checks && userInputs.length === 0) {
                    try {
                        const skGlobals = mod.$d;
                        const externalGlobals = typeof Sk !== 'undefined' ? Sk.globals : {};
                        
                        const compare = (a, b) => {
                            if (a === b) return true;
                            if (typeof a !== 'object' || typeof b !== 'object' || a === null || b === null) return a === b;
                            if (Array.isArray(a) && Array.isArray(b)) {
                                if (a.length !== b.length) return false;
                                return a.every(x => b.some(y => compare(x, y))) && b.every(x => a.some(y => compare(x, y)));
                            }
                            const keysA = Object.keys(a).sort(), keysB = Object.keys(b).sort();
                            if (keysA.length !== keysB.length || !keysA.every((k, i) => k === keysB[i])) return false;
                            return keysA.every(k => compare(a[k], b[k]));
                        };

                        for (const [varName, expectedVal] of Object.entries(checks)) {
                            let skVar = skGlobals[varName] || skGlobals["$" + varName] || 
                                        skGlobals[varName + "_$rw$"] || 
                                        externalGlobals[varName] || externalGlobals["$" + varName] ||
                                        externalGlobals[varName + "_$rw$"];
                            
                            if (skVar === undefined) {
                                const allKeys = [...Object.keys(skGlobals), ...Object.keys(externalGlobals)];
                                const match = allKeys.find(k => {
                                    const cleanK = k.replace(/^\\$|_?\\$rw\\$$/g, '').toLowerCase();
                                    return cleanK === varName.toLowerCase();
                                });
                                if (match) skVar = skGlobals[match] || externalGlobals[match];
                            }

                            if (skVar === undefined) {
                                isCorrect = false;
                                errorMsg = `Variable "${varName}" is missing.`;
                                break;
                            }
                            
                            const userVal = Sk.ffi.remapToJs(skVar);
                            if (expectedVal !== null && !compare(userVal, expectedVal)) {
                                isCorrect = false;
                                errorMsg = `The value of "${varName}" is incorrect. (Got: ${JSON.stringify(userVal)}, Expected: ${JSON.stringify(expectedVal)})`;
                                break;
                            }
                        }
                    } catch (e) { console.error("Check Error:", e); }
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

def patch_module(filepath):
    print(f"Patching Smart Validation: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We use a lambda to avoid backslash escaping issues in the replacement string
    content = re.sub(r'function runSkulpt\(id\) \{.*?\}\n(?=\s*function reset)', lambda m: NEW_RUNSKULPT_LOGIC, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

modules = [f"Module-{i}.html" for i in range(1, 7)]
workspace = r"c:\Users\kj anand\Downloads\Quiz DD"

for m in modules:
    path = os.path.join(workspace, m)
    if os.path.exists(path):
        patch_module(path)
