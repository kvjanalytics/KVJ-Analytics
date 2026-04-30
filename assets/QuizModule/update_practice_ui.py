import re

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html'

html_content = """
            <div class="section-header" style="margin-top: 60px;">
                <h2>Practice Check</h2>
            </div>

            <style>
            .practice-light-card {
                background: white; border: 1px solid #e2e8f0; border-radius: 16px; padding: 35px; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.04); position: relative; overflow: hidden;
            }
            .practice-light-card::before {
                content: ''; position: absolute; top: 0; left: 0; right: 0; height: 5px; background: linear-gradient(90deg, #3b82f6, #8b5cf6);
            }
            .mcq-light-option {
                border: 2px solid #e2e8f0; border-radius: 12px; padding: 16px 20px; display: flex; align-items: center; cursor: pointer; transition: all 0.2s; color: #334155; font-size: 15px; font-weight: 500; background: white;
            }
            .mcq-light-option:hover {
                border-color: #cbd5e1; background: #f8fafc; transform: translateY(-2px);
            }
            .mcq-light-option.selected {
                border-color: #3b82f6; background: #eff6ff; box-shadow: 0 4px 12px rgba(59,130,246,0.15);
            }
            .mcq-light-option.correct {
                border-color: #10b981; background: #f0fdf4; color: #047857;
            }
            .mcq-light-option.wrong {
                border-color: #ef4444; background: #fef2f2; color: #b91c1c;
            }
            .mcq-light-prefix {
                background: #f1f5f9; color: #64748b; width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: 800; margin-right: 15px; flex-shrink: 0; transition: all 0.2s; font-family: 'Montserrat', sans-serif;
            }
            .mcq-light-option.selected .mcq-light-prefix {
                background: #3b82f6; color: white;
            }
            .mcq-light-option.correct .mcq-light-prefix {
                background: #10b981; color: white;
            }
            .mcq-light-option.wrong .mcq-light-prefix {
                background: #ef4444; color: white;
            }

            .tf-light-row {
                display: flex; justify-content: space-between; align-items: center; padding: 16px; border: 2px solid #e2e8f0; border-radius: 12px; margin-bottom: 12px; transition: all 0.2s; background: white;
            }
            .tf-light-row:hover { border-color: #cbd5e1; background: #f8fafc; }
            .tf-light-statement { color: #334155; font-size: 15px; font-weight: 500; padding-right: 20px; line-height: 1.5; }
            .tf-light-btn {
                padding: 8px 24px; border: 2px solid #e2e8f0; background: white; color: #64748b; border-radius: 8px; cursor: pointer; font-weight: 700; font-size: 14px; transition: all 0.2s; font-family: 'Montserrat', sans-serif;
            }
            .tf-light-btn:hover { border-color: #cbd5e1; color: #334155; background: #f8fafc; }
            .tf-light-btn.selected { background: #3b82f6; color: white; border-color: #3b82f6; box-shadow: 0 4px 10px rgba(59,130,246,0.2); }
            .tf-light-btn.correct { background: #10b981 !important; border-color: #10b981 !important; color: white !important; }
            .tf-light-btn.wrong { background: #ef4444 !important; border-color: #ef4444 !important; color: white !important; }

            .btn-light-check {
                background: #1e293b; color: white; border: none; padding: 14px 32px; border-radius: 8px; font-weight: 700; font-size: 15px; cursor: pointer; transition: all 0.2s; margin-top: 15px; font-family: 'Montserrat', sans-serif; letter-spacing: 0.5px;
            }
            .btn-light-check:hover { background: #0f172a; transform: translateY(-2px); box-shadow: 0 6px 15px rgba(0,0,0,0.1); }

            .feedback-light {
                margin-top: 20px; padding: 16px 20px; border-radius: 10px; font-weight: 500; font-size: 14.5px; display: none; line-height: 1.5;
            }
            .feedback-light.correct { background: #f0fdf4; color: #047857; border: 1px solid #bbf7d0; display: block; }
            .feedback-light.wrong { background: #fef2f2; color: #b91c1c; border: 1px solid #fecaca; display: block; }
            </style>

            <script>
                let lightSelections = {};

                function selectLightMCQ(el, qid) {
                    const parent = document.getElementById(qid);
                    if (!parent) return;
                    parent.querySelectorAll('.mcq-light-option').forEach(o => o.classList.remove('selected', 'correct', 'wrong'));
                    el.classList.add('selected');
                    lightSelections[qid] = el.querySelector('.mcq-light-prefix').innerText;
                }

                function checkLightMCQ(qid, correct, msg) {
                    const parent = document.getElementById(qid);
                    const feedback = document.getElementById('feedback-' + qid);
                    if (!parent || !feedback) return;
                    const sel = parent.querySelector('.selected');
                    if (!sel) return;

                    if (lightSelections[qid] === correct) {
                        sel.classList.add('correct');
                        feedback.innerHTML = '<strong style="display:block; margin-bottom:5px; font-size: 16px;">✅ Correct!</strong>' + msg;
                        feedback.className = 'feedback-light correct';
                        triggerConfetti();
                    } else {
                        sel.classList.add('wrong');
                        feedback.innerHTML = '<strong style="display:block; margin-bottom:5px; font-size: 16px;">❌ Incorrect</strong>Try again!';
                        feedback.className = 'feedback-light wrong';
                    }
                }

                function selectLightTF(el, qid, val) {
                    const row = document.getElementById('tf-light-row-' + qid);
                    if (!row) return;
                    row.querySelectorAll('.tf-light-btn').forEach(b => b.classList.remove('selected', 'correct', 'wrong'));
                    el.classList.add('selected');
                    lightSelections[qid] = val;
                }

                function checkLightTFGroup(qids, corrects, fbid) {
                    const feedback = document.getElementById(fbid);
                    if (!feedback) return;
                    
                    let allRight = true;
                    qids.forEach((q, idx) => {
                        const row = document.getElementById('tf-light-row-' + q);
                        if (!row) { allRight = false; return; }
                        const sel = row.querySelector('.selected');
                        if (!sel || lightSelections[q] !== corrects[idx]) {
                            allRight = false;
                            if (sel) sel.classList.add('wrong');
                        } else {
                            sel.classList.add('correct');
                        }
                    });

                    if (allRight) {
                        feedback.innerHTML = '<strong style="display:block; margin-bottom:5px; font-size: 16px;">✅ Outstanding!</strong> All answers are correct. You have a solid grasp of this concept!';
                        feedback.className = 'feedback-light correct';
                        triggerConfetti();
                    } else {
                        feedback.innerHTML = '<strong style="display:block; margin-bottom:5px; font-size: 16px;">❌ Almost there</strong> One or more answers are incorrect. Please review the statements and try again.';
                        feedback.className = 'feedback-light wrong';
                    }
                }
            </script>
            
            <!-- Question 1 -->
            <div class="practice-light-card">
                <div style="display: flex; align-items: center; margin-bottom: 20px;">
                    <div style="background: #f0f9ff; color: #0284c7; font-weight: 800; font-size: 14px; padding: 6px 12px; border-radius: 6px; margin-right: 15px; font-family: 'Montserrat', sans-serif;">Q1</div>
                    <h3 style="margin: 0; color: #1e293b; font-size: 19px; font-weight: 700; font-family: 'Montserrat', sans-serif;">Data vs Information</h3>
                </div>
                <p style="color: #475569; font-size: 15.5px; margin-bottom: 25px; font-weight: 500;">Which of the following scenarios best illustrates the difference between data and information?</p>
                
                <div id="q1_light" style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 20px;">
                    <div class="mcq-light-option" onclick="selectLightMCQ(this, 'q1_light')">
                        <div class="mcq-light-prefix">A</div>
                        <div>A list of temperatures is information, while a chart showing them is data.</div>
                    </div>
                    <div class="mcq-light-option" onclick="selectLightMCQ(this, 'q1_light')">
                        <div class="mcq-light-prefix">B</div>
                        <div>Random numbers are data, while knowing these represent daily sales is information.</div>
                    </div>
                    <div class="mcq-light-option" onclick="selectLightMCQ(this, 'q1_light')">
                        <div class="mcq-light-prefix">C</div>
                        <div>A printed textbook is data, while a digital ebook is information.</div>
                    </div>
                    <div class="mcq-light-option" onclick="selectLightMCQ(this, 'q1_light')">
                        <div class="mcq-light-prefix">D</div>
                        <div>Data is always numbers, while information is always words.</div>
                    </div>
                </div>
                <button class="btn-light-check" onclick="checkLightMCQ('q1_light', 'B', 'Processing raw numbers into daily sales adds the necessary context, successfully turning meaningless data into actionable information.')">Check Answer</button>
                <div id="feedback-q1_light" class="feedback-light"></div>
            </div>

            <!-- Question 2 -->
            <div class="practice-light-card">
                <div style="display: flex; align-items: center; margin-bottom: 20px;">
                    <div style="background: #fdf4ff; color: #c026d3; font-weight: 800; font-size: 14px; padding: 6px 12px; border-radius: 6px; margin-right: 15px; font-family: 'Montserrat', sans-serif;">Q2</div>
                    <h3 style="margin: 0; color: #1e293b; font-size: 19px; font-weight: 700; font-family: 'Montserrat', sans-serif;">Hierarchy Levels</h3>
                </div>
                <p style="color: #475569; font-size: 15.5px; margin-bottom: 25px; font-weight: 500;">Which level of the hierarchy is characterized by being 'action-oriented' and built through experience and reflection?</p>
                
                <div id="q2_light" style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 20px;">
                    <div class="mcq-light-option" onclick="selectLightMCQ(this, 'q2_light')"><div class="mcq-light-prefix">A</div><div>Metadata</div></div>
                    <div class="mcq-light-option" onclick="selectLightMCQ(this, 'q2_light')"><div class="mcq-light-prefix">B</div><div>Information</div></div>
                    <div class="mcq-light-option" onclick="selectLightMCQ(this, 'q2_light')"><div class="mcq-light-prefix">C</div><div>Knowledge</div></div>
                    <div class="mcq-light-option" onclick="selectLightMCQ(this, 'q2_light')"><div class="mcq-light-prefix">D</div><div>Data</div></div>
                </div>
                <button class="btn-light-check" onclick="checkLightMCQ('q2_light', 'C', 'Knowledge represents the application of information to make decisions and solve problems based on experience.')">Check Answer</button>
                <div id="feedback-q2_light" class="feedback-light"></div>
            </div>

            <!-- Question 3 -->
            <div class="practice-light-card">
                <div style="display: flex; align-items: center; margin-bottom: 20px;">
                    <div style="background: #f0fdf4; color: #16a34a; font-weight: 800; font-size: 14px; padding: 6px 12px; border-radius: 6px; margin-right: 15px; font-family: 'Montserrat', sans-serif;">Q3</div>
                    <h3 style="margin: 0; color: #1e293b; font-size: 19px; font-weight: 700; font-family: 'Montserrat', sans-serif;">True or False Assessment</h3>
                </div>
                <p style="color: #475569; font-size: 15.5px; margin-bottom: 25px; font-weight: 500;">Evaluate the following statements based on what you've learned:</p>
                
                <div style="display: flex; flex-direction: column; gap: 15px; margin-bottom: 20px;">
                    <div class="tf-light-row" id="tf-light-row-q3a_light">
                        <span class="tf-light-statement">Raw data is often meaningless on its own because it lacks context and organization.</span>
                        <div style="display:flex; gap:10px; flex-shrink: 0;">
                            <button class="tf-light-btn" onclick="selectLightTF(this, 'q3a_light', true)">True</button>
                            <button class="tf-light-btn" onclick="selectLightTF(this, 'q3a_light', false)">False</button>
                        </div>
                    </div>

                    <div class="tf-light-row" id="tf-light-row-q3b_light">
                        <span class="tf-light-statement">Information is the highest level of the hierarchy and represents the final stage of understanding.</span>
                        <div style="display:flex; gap:10px; flex-shrink: 0;">
                            <button class="tf-light-btn" onclick="selectLightTF(this, 'q3b_light', true)">True</button>
                            <button class="tf-light-btn" onclick="selectLightTF(this, 'q3b_light', false)">False</button>
                        </div>
                    </div>

                    <div class="tf-light-row" id="tf-light-row-q3c_light">
                        <span class="tf-light-statement">Summarizing a large spreadsheet of sales figures into a monthly growth chart is an example of creating knowledge.</span>
                        <div style="display:flex; gap:10px; flex-shrink: 0;">
                            <button class="tf-light-btn" onclick="selectLightTF(this, 'q3c_light', true)">True</button>
                            <button class="tf-light-btn" onclick="selectLightTF(this, 'q3c_light', false)">False</button>
                        </div>
                    </div>
                </div>

                <button class="btn-light-check" onclick="checkLightTFGroup(['q3a_light', 'q3b_light', 'q3c_light'], [true, false, false], 'feedback-q3_light')">Check Answers</button>
                <div id="feedback-q3_light" class="feedback-light"></div>
            </div>
"""

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the previously inserted block
pattern = re.compile(r'<div class="section-header" style="margin-top: 60px;">\s*<h2>Practice Check</h2>\s*</div>.*?<div style="margin-top: 60px; text-align: center;">\s*<div class="quiz-cta">', re.DOTALL)
new_content = pattern.sub(html_content + '\n            <div style="margin-top: 60px; text-align: center;">\n                <div class="quiz-cta">', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated practice UI")
