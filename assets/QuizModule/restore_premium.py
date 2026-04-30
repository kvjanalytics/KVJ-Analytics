import os

modules_py = """
            <div class="modules-section" id="modules-list">
                <h2 class="section-title">Curriculum Roadmap</h2>
                <div class="module-list">
                    <div class="module-card">
                        <div class="module-num">M1</div>
                        <div class="module-info">
                            <div class="module-name">Module 1 — Foundation</div>
                            <div class="module-desc">Variables, data types, and basic operations.</div>
                        </div>
                        <div class="module-actions">
                            <a href="Module-1.html" class="btn-sm btn-study">Study</a>
                            <a href="module_quiz.html?mod=1" class="btn-sm btn-quiz">Quiz</a>
                        </div>
                    </div>
                    <div class="module-card">
                        <div class="module-num">M2</div>
                        <div class="module-info">
                            <div class="module-name">Module 2 — Flow Control</div>
                            <div class="module-desc">Conditionals, loops, and logic branches.</div>
                        </div>
                        <div class="module-actions">
                            <a href="Module-2.html" class="btn-sm btn-study">Study</a>
                            <a href="module_quiz.html?mod=2" class="btn-sm btn-quiz">Quiz</a>
                        </div>
                    </div>
                    <div class="module-card">
                        <div class="module-num">M3</div>
                        <div class="module-info">
                            <div class="module-name">Module 3 — I/O Operations</div>
                            <div class="module-desc">File handling and console input/output.</div>
                        </div>
                        <div class="module-actions">
                            <a href="Module-3.html" class="btn-sm btn-study">Study</a>
                            <a href="module_quiz.html?mod=3" class="btn-sm btn-quiz">Quiz</a>
                        </div>
                    </div>
                    <div class="module-card">
                        <div class="module-num">M4</div>
                        <div class="module-info">
                            <div class="module-name">Module 4 — Documentation</div>
                            <div class="module-desc">Comments, docstrings, and best practices.</div>
                        </div>
                        <div class="module-actions">
                            <a href="Module-4.html" class="btn-sm btn-study">Study</a>
                            <a href="module_quiz.html?mod=4" class="btn-sm btn-quiz">Quiz</a>
                        </div>
                    </div>
                    <div class="module-card">
                        <div class="module-num">M5</div>
                        <div class="module-info">
                            <div class="module-name">Module 5 — Error Handling</div>
                            <div class="module-desc">Try-except blocks and debugging.</div>
                        </div>
                        <div class="module-actions">
                            <a href="Module-5.html" class="btn-sm btn-study">Study</a>
                            <a href="module_quiz.html?mod=5" class="btn-sm btn-quiz">Quiz</a>
                        </div>
                    </div>
                    <div class="module-card">
                        <div class="module-num">M6</div>
                        <div class="module-info">
                            <div class="module-name">Module 6 — Built-in Modules</div>
                            <div class="module-desc">Standard libraries and os/math modules.</div>
                        </div>
                        <div class="module-actions">
                            <a href="Module-6.html" class="btn-sm btn-study">Study</a>
                            <a href="module_quiz.html?mod=6" class="btn-sm btn-quiz">Quiz</a>
                        </div>
                    </div>
                </div>
            </div>
"""

modules_da = """
            <div class="modules-section" id="modules-list">
                <h2 class="section-title">Data Analytics Roadmap</h2>
                <div class="module-list">
                    <div class="module-card">
                        <div class="module-num">M1</div>
                        <div class="module-info">
                            <div class="module-name">Module 1 — Intro to Data Analytics</div>
                            <div class="module-desc">Understanding the data lifecycle and analysis types.</div>
                        </div>
                        <div class="module-actions">
                            <a href="Data-Module-1.html" class="btn-sm btn-study">Study</a>
                            <a href="module_quiz.html?data_mod=1" class="btn-sm btn-quiz">Quiz</a>
                        </div>
                    </div>
                    <div class="module-card">
                        <div class="module-num">M2</div>
                        <div class="module-info">
                            <div class="module-name">Module 2 — Excel for Data Analytics</div>
                            <div class="module-desc">Pivot tables, VLOOKUP, and data cleaning in Excel.</div>
                        </div>
                        <div class="module-actions">
                            <a href="Data-Module-2.html" class="btn-sm btn-study">Study</a>
                            <a href="module_quiz.html?data_mod=2" class="btn-sm btn-quiz">Quiz</a>
                        </div>
                    </div>
                    <div class="module-card">
                        <div class="module-num">M3</div>
                        <div class="module-info">
                            <div class="module-name">Module 3 — SQL for Data Analytics</div>
                            <div class="module-desc">Querying databases with SELECT, JOIN, and GROUP BY.</div>
                        </div>
                        <div class="module-actions">
                            <a href="Data-Module-3.html" class="btn-sm btn-study">Study</a>
                            <a href="module_quiz.html?data_mod=3" class="btn-sm btn-quiz">Quiz</a>
                        </div>
                    </div>
                    <div class="module-card">
                        <div class="module-num">M4</div>
                        <div class="module-info">
                            <div class="module-name">Module 4 — Python for Data Analytics</div>
                            <div class="module-desc">Using Pandas and NumPy for data manipulation.</div>
                        </div>
                        <div class="module-actions">
                            <a href="Data-Module-4.html" class="btn-sm btn-study">Study</a>
                            <a href="module_quiz.html?data_mod=4" class="btn-sm btn-quiz">Quiz</a>
                        </div>
                    </div>
                    <div class="module-card">
                        <div class="module-num">M5</div>
                        <div class="module-info">
                            <div class="module-name">Module 5 — Data Visualization</div>
                            <div class="module-desc">Creating dashboards with Power BI and Matplotlib.</div>
                        </div>
                        <div class="module-actions">
                            <a href="Data-Module-5.html" class="btn-sm btn-study">Study</a>
                            <a href="module_quiz.html?data_mod=5" class="btn-sm btn-quiz">Quiz</a>
                        </div>
                    </div>
                    <div class="module-card">
                        <div class="module-num">M6</div>
                        <div class="module-info">
                            <div class="module-name">Module 6 — Capstone Project</div>
                            <div class="module-desc">Final real-world data analysis project.</div>
                        </div>
                        <div class="module-actions">
                            <a href="Data-Module-6.html" class="btn-sm btn-study">Study</a>
                            <a href="module_quiz.html?data_mod=6" class="btn-sm btn-quiz">Quiz</a>
                        </div>
                    </div>
                </div>
            </div>
"""

def restore_premium_ui(path, modules_html, prefix):
    mock_links = f"""
            <div class="mock-card">
                <div class="mock-badge">📝</div>
                <div class="mock-info">
                    <div class="mock-name">Mock Test 1</div>
                    <div class="mock-desc">Comprehensive assessment covering all fundamentals.</div>
                </div>
                <a href="module_quiz.html?mock=1" class="btn-mock">Take Mock</a>
            </div>
            <div class="mock-card">
                <div class="mock-badge">🏆</div>
                <div class="mock-info">
                    <div class="mock-name">Mock Test 2</div>
                    <div class="mock-desc">Advanced full-length practice exam simulation.</div>
                </div>
                <a href="module_quiz.html?mock=2" class="btn-mock">Take Mock</a>
            </div>
            <div class="mock-card">
                <div class="mock-badge">🏅</div>
                <div class="mock-info">
                    <div class="mock-name">Mock Test 3 — Full Simulation</div>
                    <div class="mock-desc">Final certification level assessment.</div>
                </div>
                <a href="module_quiz.html?mock=3" class="btn-mock">Take Mock</a>
            </div>
    """

    new_html = f\"\"\"<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roadmap | KVJ</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --py-blue-dark: #1e3a5f; --py-blue-brand: #3776ab; --py-yellow: #ffd43b; --bg-light: #f6f8fb; --text-main: #1d1d1f; --text-muted: #4b5563; }}
        *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Inter', -apple-system, sans-serif; background-color: var(--bg-light); color: var(--text-main); line-height: 1.6; overflow-x: hidden; }}
        .navbar {{ background: #fff; border-bottom: 1px solid #e5e7eb; display: flex; align-items: center; justify-content: space-between; padding: 0.85rem 2.5rem; position: sticky; top: 0; z-index: 100; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }}
        .navbar-left {{ display: flex; align-items: center; gap: 1.25rem; }}
        .nav-back {{ font-size: 0.85rem; font-weight: 600; color: #193855; text-decoration: none; background: #eef2ff; padding: 7px 18px; border-radius: 20px; transition: background 0.2s; }}
        .nav-back:hover {{ background: #dde5ff; }}
        .nav-logo {{ max-height: 38px; width: auto; display: block; }}
        .nav-logout {{ font-size: 0.85rem; font-weight: 700; color: #0066ff; text-decoration: none; cursor: pointer; transition: opacity 0.2s; }}
        .nav-logout:hover {{ opacity: 0.75; }}
        .course-banner {{ background: #1c1d1f; color: #ffffff; padding: 3.5rem 2.5rem 2.5rem; position: relative; overflow: hidden; }}
        .banner-inner {{ max-width: 820px; position: relative; z-index: 2; }}
        .course-icon {{ width: 52px; height: 52px; background: rgba(255,255,255,0.18); border: 2px solid rgba(255,255,255,0.35); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.1rem; backdrop-filter: blur(4px); overflow: hidden; }}
        .course-icon img {{ width: 100%; height: 100%; object-fit: contain; padding: 10px; }}
        .course-title {{ font-size: 2.5rem; font-weight: 800; line-height: 1.2; margin-bottom: 1rem; letter-spacing: -0.5px; }}
        .rating-row {{ display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.85rem; flex-wrap: wrap; }}
        .stars {{ color: #FFD700; font-size: 1rem; letter-spacing: 1px; }}
        .rating-score {{ font-weight: 700; font-size: 0.95rem; }}
        .rating-count {{ font-size: 0.88rem; color: rgba(255,255,255,0.8); text-decoration: underline; cursor: default; }}
        .meta-list {{ list-style: none; display: flex; flex-direction: column; gap: 0.6rem; margin-bottom: 1.7rem; }}
        .meta-list li {{ display: flex; align-items: center; gap: 0.55rem; font-size: 0.95rem; color: rgba(255,255,255,0.92); }}
        .page-body {{ max-width: 1200px; margin: 3.5rem auto; padding: 0 2.5rem 4rem; display: grid; grid-template-columns: 1fr 340px; gap: 3rem; align-items: start; }}
        .section-title {{ font-size: 1.5rem; font-weight: 800; color: #1a1a1a; margin-bottom: 1.5rem; padding-bottom: 0.8rem; border-bottom: 2px solid #f0f0f0; }}
        .module-list {{ display: flex; flex-direction: column; gap: 1rem; }}
        .module-card {{ background: #fff; border: 1px solid #e5e7eb; border-radius: 12px; padding: 1.25rem 1.5rem; display: flex; align-items: center; gap: 1.25rem; transition: all 0.2s ease; }}
        .module-card:hover {{ box-shadow: 0 8px 25px rgba(0,0,0,0.06); border-color: #cbd5e1; transform: translateY(-2px); }}
        .module-num {{ min-width: 44px; height: 44px; background: #f0f7ff; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 0.9rem; font-weight: 800; color: var(--py-blue-brand); }}
        .module-info {{ flex: 1; }}
        .module-name {{ font-size: 1rem; font-weight: 700; color: #1a1a1a; margin-bottom: 0.3rem; }}
        .module-desc {{ font-size: 0.85rem; color: #6b7280; line-height: 1.5; }}
        .module-actions {{ display: flex; gap: 0.6rem; flex-shrink: 0; }}
        .btn-sm {{ font-size: 0.8rem; font-weight: 700; padding: 0.5rem 1.1rem; border-radius: 8px; text-decoration: none; border: 1px solid; transition: all 0.2s; }}
        .btn-study {{ color: #0066ff; border-color: #dbeafe; background: #eff6ff; }}
        .btn-quiz {{ color: #059669; border-color: #d1fae5; background: #f0fdf4; }}
        .mock-card {{ background: #fff; border: 1px solid #e5e7eb; border-radius: 12px; padding: 1.25rem 1.5rem; display: flex; align-items: center; gap: 1.25rem; }}
        .mock-badge {{ min-width: 44px; height: 44px; background: #f0fdff; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; }}
        .btn-mock {{ font-size: 0.8rem; font-weight: 700; padding: 0.5rem 1.2rem; border-radius: 8px; text-decoration: none; color: #0891b2; border: 1px solid #cffafe; background: #f0fdff; flex-shrink: 0; transition: all 0.2s; }}
        .btn-mock:hover {{ background: #cffafe; }}
        .sidebar-card {{ background: #fff; border-radius: 16px; border: 1px solid #e5e7eb; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.08); position: sticky; top: 100px; }}
        .sidebar-thumb {{ background: #1e293b; color: white; padding: 40px 20px; text-align: center; }}
        .sidebar-thumb img {{ max-width: 120px; margin-bottom: 15px; }}
        .sidebar-body {{ padding: 20px; }}
        .btn-cta {{ display: inline-block; background: #a435f0; color: #ffffff; font-size: 0.95rem; font-weight: 800; padding: 0.85rem 2.5rem; border-radius: 8px; text-decoration: none; border: none; cursor: pointer; transition: all 0.2s; box-shadow: 0 4px 18px rgba(164, 53, 240, 0.4); width: 100%; text-align: center; }}
        #syncBtn {{ background: #f8fafc; color: #64748b; border: 1.5px solid #e2e8f0; padding: 10px 20px; border-radius: 10px; font-weight: 600; cursor: pointer; display: flex; align-items: center; justify-content: center; margin: 20px auto; gap: 8px; }}
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="navbar-left"><a href="index.html" class="nav-back">← Dashboard</a><img src="Kvj logo.jpeg" alt="Logo" class="nav-logo"></div>
        <a href="javascript:void(0)" onclick="logout()" class="nav-logout">LOGOUT</a>
    </nav>
    <div class="course-banner">
        <div class="banner-inner">
            <div class="course-icon"><img src="pearson_python_badge_transparent.png"></div>
            <h1 class="course-title">Curriculum Roadmap</h1>
            <div class="rating-row"><span class="stars">★★★★★</span><span class="rating-score">4.8</span><span class="rating-count">(12,450 ratings) • 85,000 students</span></div>
            <ul class="meta-list"><li>Professional Certification track</li><li>40+ hours of content</li></ul>
        </div>
    </div>
    <div class="page-body">
        <div>
            {modules_html}
            <div class="modules-section">
                <button onclick="syncProgress()" id="syncBtn">Sync Progress</button>
                <p id="syncStatus" style="text-align:center; font-size:0.8rem;"></p>
                <h2 class="section-title">Mock Assessments</h2>
                <div class="module-list">{mock_links}</div>
            </div>
        </div>
        <div class="sidebar">
            <div class="sidebar-card">
                <div class="sidebar-thumb"><img src="pearson_python_badge_transparent.png"><p>Professional Certification</p></div>
                <div class="sidebar-body"><h4>Industry Recognized</h4><p style="font-size:0.85rem; color:#64748b; margin-bottom:15px;">Earn certificates from Pearson and KVJ.</p><button class="btn-cta">View Certificate</button></div>
            </div>
        </div>
    </div>
    <script>
        const scriptURL = "https://script.google.com/macros/s/AKfycbw9mb2dsJ1SSheOcpdcdeE8eKNnuCjK2U9U9kIeHV_2yga8Ujiee1w_huTzc2w5BpWD/exec";
        function syncProgress() {{
            const phone = localStorage.getItem('strategist_phone');
            if (!phone) {{ alert("Log in first!"); return; }}
            const btn = document.getElementById('syncBtn');
            const status = document.getElementById('syncStatus');
            btn.disabled = true; status.innerText = "Syncing...";
            const callbackName = 'syncCallback_' + Date.now();
            const script = document.createElement('script');
            window[callbackName] = function(data) {{
                btn.disabled = false;
                if (data.success && data.scores) {{
                    for (const modId in data.scores) {{ localStorage.setItem('score_' + modId, data.scores[modId]); }}
                    status.innerText = "Synced!"; setTimeout(() => window.location.reload(), 1000);
                }} else {{ status.innerText = "Failed."; }}
                document.body.removeChild(script); delete window[callbackName];
            }};
            script.src = `${{scriptURL}}?action=getScores&phone=${{encodeURIComponent(phone)}}&callback=${{callbackName}}&t=${{Date.now()}}`;
            document.body.appendChild(script);
        }}
        function logout() {{ sessionStorage.clear(); localStorage.clear(); window.location.href = 'login.html'; }}
    </script>
</body>
</html>
\"\"\"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Restored Premium UI to {path}")

restore_premium_ui('c:/Users/kj anand/Downloads/Quiz DD/roadmap.html', modules_py, '')
restore_premium_ui('c:/Users/kj anand/Downloads/Quiz DD/data_roadmap.html', modules_da, 'data')
