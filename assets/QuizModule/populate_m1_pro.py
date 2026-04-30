import re

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html'

html_content = """
        <main class="main-content">
            <div class="section-header">
                <h2>1. Data, Information and Knowledge</h2>
            </div>

            <h3>Data</h3>
            <p>Data refers to raw facts, figures, or observations collected for analysis or reference. On its own, data is often meaningless because it lacks context.</p>
            
            <div class="interaction-box">
                <strong>Examples of Data:</strong>
                <ul class="content-list" style="margin-top: 10px;">
                    <li>The number 42.</li>
                    <li>A list of dates: 12/05, 14/05, 19/05.</li>
                    <li>The word "Cochin."</li>
                </ul>
            </div>

            <p>Data can appear in many forms such as:</p>
            <ul class="content-list">
                <li>Numbers</li>
                <li>Text</li>
                <li>Images</li>
                <li>Audio</li>
            </ul>

            <div class="section-header" style="margin-top: 60px;">
                <h2>2. Information: The Finished Product</h2>
            </div>
            <p>Information is data that has been processed, structured, or presented within a specific context to make it meaningful and useful. It is "data with a story."</p>
            
            <div class="interaction-box" style="border-left-color: #8b5cf6; background: #f5f3ff;">
                <strong>Characteristics:</strong>
                <p>Processed, organized, and relevant to a goal.</p>
            </div>

            <div class="interaction-box">
                <strong>Examples of Information:</strong>
                <ul class="content-list" style="margin-top: 10px;">
                    <li>"42" is the number of students who passed the AI exam.</li>
                    <li>The dates represent a schedule for upcoming Python training sessions.</li>
                    <li>"Cochin" is the current location for a regional education tour.</li>
                </ul>
            </div>

            <h3>Key Differences at a Glance</h3>
            <div class="data-table-container">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Feature</th>
                            <th>Data</th>
                            <th>Information</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Form</strong></td>
                            <td>Raw, unorganized facts.</td>
                            <td>Organized and processed facts.</td>
                        </tr>
                        <tr>
                            <td><strong>Level</strong></td>
                            <td>Low-level (the starting point).</td>
                            <td>High-level (the output).</td>
                        </tr>
                        <tr>
                            <td><strong>Dependence</strong></td>
                            <td>Independent of context.</td>
                            <td>Dependent on context.</td>
                        </tr>
                        <tr>
                            <td><strong>Meaning</strong></td>
                            <td>Meaningless on its own.</td>
                            <td>Meaningful and actionable.</td>
                        </tr>
                        <tr>
                            <td><strong>Example</strong></td>
                            <td>Individual test scores.</td>
                            <td>The average grade of a class.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="section-header" style="margin-top: 60px;">
                <h2>3. Knowledge: The Application of Information</h2>
            </div>
            <p>While information is data with context, knowledge is the next step in the hierarchy. It is the ability to use information to make decisions, solve problems, or predict future outcomes. Knowledge is gained through experience, study, and reflection.</p>
            
            <div class="interaction-box" style="border-left-color: #8b5cf6; background: #f5f3ff;">
                <strong>Characteristics:</strong>
                <p style="margin-bottom: 10px;">Action-oriented, subjective, and cumulative.</p>
                <strong>The Key Difference:</strong>
                <p style="margin-bottom: 0;">If information tells you what is happening, knowledge tells you how to use that information or why it matters.</p>
            </div>

            <h3>Example Scenario: Educational Planning</h3>
            <p>To see how these concepts build on one another, let's look at a practical scenario involving educational planning:</p>

            <div class="practice-card" style="background: #1e293b; color: #f8fafc; border: none; margin-bottom: 40px;">
                <h4 style="color: #38bdf8; font-size: 18px; margin-top: 0; margin-bottom: 10px; font-family: 'Montserrat', sans-serif;">1. Data (The Raw Input)</h4>
                <p style="color: #e2e8f0; margin-bottom: 25px; line-height: 1.5;">A list of numbers: 85, 40, 92, 38, 77. <br><span style="font-size: 14.5px; opacity: 0.75;">On their own, these are just digits without a purpose.</span></p>

                <h4 style="color: #38bdf8; font-size: 18px; margin-bottom: 10px; font-family: 'Montserrat', sans-serif;">2. Information (The Processed Output)</h4>
                <p style="color: #e2e8f0; margin-bottom: 25px; line-height: 1.5;">These numbers are the scores from a recent Python Mock Test for a group of 5 students. <br><span style="font-size: 14.5px; opacity: 0.75;">By adding context, we now know these are test results. We can see that two students scored below 50.</span></p>

                <h4 style="color: #38bdf8; font-size: 18px; margin-bottom: 10px; font-family: 'Montserrat', sans-serif;">3. Knowledge (The Insight and Action)</h4>
                <p style="color: #e2e8f0; margin-bottom: 0; line-height: 1.5;">Based on these scores and past teaching experience, the instructor realizes that the students who struggled are the ones who missed the session on "Loops." The instructor decides to schedule a remedial workshop specifically on that topic before the final exam. <br><span style="font-size: 14.5px; opacity: 0.75;">This is knowledge: using the information (the scores) to identify a pattern (the gap in learning) and taking a strategic action (scheduling a workshop).</span></p>
            </div>

            <h3>Summary Comparison</h3>
            <div class="data-table-container">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Concept</th>
                            <th>Simple Definition</th>
                            <th>Example</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Data</strong></td>
                            <td>Symbols/Facts</td>
                            <td>"32"</td>
                        </tr>
                        <tr>
                            <td><strong>Information</strong></td>
                            <td>Contextualized Data</td>
                            <td>"32°C is the current temperature."</td>
                        </tr>
                        <tr>
                            <td><strong>Knowledge</strong></td>
                            <td>Applied Information</td>
                            <td>"At 32°C, I should wear light clothing to stay comfortable."</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Assessment Button -->
            <div style="margin-top: 60px; text-align: center;">
                <div class="quiz-cta">
                    <h2 style="font-family: 'Montserrat', sans-serif; font-weight: 800; font-size: 28px; margin-bottom: 15px; border-bottom: none; color: white;">Ready to Test Your Knowledge?</h2>
                    <p style="font-size: 16px; color: #e2e8f0; max-width: 600px; margin: 0 auto 25px;">Take the module assessment to evaluate your understanding of Data, Information, and Knowledge.</p>
                    <a href="module_quiz.html?mod=data1" class="btn-start-quiz">Start Assessment &rarr;</a>
                </div>
            </div>
        </main>"""

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to replace everything inside main-content
pattern = re.compile(r'<main class="main-content">.*?</main>', re.DOTALL)
new_content = pattern.sub(html_content, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully injected new content.")
