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

def final_restore(path, modules_html):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The file currently has a broken body structure.
    # We want to put modules_html into the page-body > left column.
    
    # Let's find the end of the style tag
    style_end = content.find('</style>') + 8
    
    # Reconstruct the middle part
    middle = f"""
</head>
<body>
    <nav class="navbar">
        <div class="navbar-left">
            <a href="index.html" class="nav-back">← Dashboard</a>
            <img src="Kvj logo.jpeg" alt="Logo" class="nav-logo">
        </div>
        <a href="javascript:void(0)" onclick="logout()" class="nav-logout">LOGOUT</a>
    </nav>

    <div class="course-banner">
        <div class="banner-inner">
            <div class="course-icon"><img src="pearson_python_badge_transparent.png"></div>
            <h1 class="course-title">Curriculum Roadmap</h1>
            <div class="rating-row">
                <span class="stars">★★★★★</span>
                <span class="rating-score">4.8</span>
                <span class="rating-count">(12,450 ratings) • 85,000 students</span>
            </div>
            <ul class="meta-list">
                <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> <strong>Professional Certification</strong> track</li>
                <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg> <strong>40+ hours</strong> of hands-on content</li>
            </ul>
        </div>
    </div>

    <div class="page-body">
        <div> <!-- left column -->
            {modules_html}
    """

    # Now find where the mock section starts in the CURRENT broken file
    mock_start = content.find('<div class="modules-section">')
    if mock_start == -1: mock_start = content.find('<div style="text-align: center; margin: 20px 0;">')
    
    # Keep the rest of the file (Mock section + Sidebar + Script)
    footer_part = content[mock_start:]
    
    final_html = content[:style_end] + middle + footer_part
    
    # Fix the literal \\n
    final_html = final_html.replace('\\\\n', '\\n')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"Restored {path}")

final_restore('c:/Users/kj anand/Downloads/Quiz DD/roadmap.html', modules_py)
final_restore('c:/Users/kj anand/Downloads/Quiz DD/data_roadmap.html', modules_da)
