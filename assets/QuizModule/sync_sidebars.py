import glob
import re

sidebar_html = """
            <h3>Module Path</h3>
            
            <!-- Module 1 -->
            <div class="accordion-item">
                <div class="accordion-header" id="header-1" onclick="toggleAccordion(1)">
                    <span>01 Data Basics</span>
                    <span class="chevron"></span>
                </div>
                <div id="content-1" class="accordion-content">
                    <a href="Data-Module-1.html#s1-basics" class="sidebar-content-link">1.1 Data & Information</a>
                    <a href="Data-Module-1.html#s2-info" class="sidebar-content-link">1.2 Information</a>
                    <a href="Data-Module-1.html#s3-knowledge" class="sidebar-content-link">1.3 Knowledge</a>
                    <a href="Data-Module-1.html#s4-analysis" class="sidebar-content-link">1.4 Data Analysis</a>
                    <a href="Data-Module-1.html#s5-variables" class="sidebar-content-link">1.5 Variable Types</a>
                    <a href="Data-Module-1.html#s6-structures" class="sidebar-content-link">1.6 Basic Structures</a>
                    <a href="Data-Module-1.html#s7-stats" class="sidebar-content-link">1.7 Statistics</a>
                    <a href="Data-Module-1.html#s8-types" class="sidebar-content-link">1.8 Types of Data</a>
                    <a href="Data-Module-1.html#s9-structured" class="sidebar-content-link">1.9 Structured Data</a>
                    <a href="Data-Module-1.html#s10-raw" class="sidebar-content-link">1.10 Raw & Big Data</a>
                </div>
            </div>

            <!-- Module 2 -->
            <div class="accordion-item">
                <div class="accordion-header" id="header-2" onclick="toggleAccordion(2)">
                    <span>02 Data Manipulation</span>
                    <span class="chevron"></span>
                </div>
                <div id="content-2" class="accordion-content">
                    <a href="Data-Module-2.html#s1-etl" class="sidebar-content-link">2.1 ETL Process</a>
                    <a href="Data-Module-2.html#s2-formats" class="sidebar-content-link">2.2 File Formats</a>
                    <a href="Data-Module-2.html#s3-cleaning" class="sidebar-content-link">2.3 Data Cleaning</a>
                    <a href="Data-Module-2.html#s4-organizing" class="sidebar-content-link">2.4 Data Organizing</a>
                    <a href="Data-Module-2.html#s5-aggregation" class="sidebar-content-link">2.5 Data Aggregation</a>
                    <a href="Data-Module-2.html#s6-summarizing" class="sidebar-content-link">2.6 Summarizing</a>
                    <a href="Data-Module-2.html#s7-pivoting" class="sidebar-content-link">2.7 Pivoting</a>
                </div>
            </div>

            <!-- Module 3 -->
            <div class="accordion-item">
                <div class="accordion-header" id="header-3" onclick="toggleAccordion(3)">
                    <span>03 Data Analysis</span>
                    <span class="chevron"></span>
                </div>
                <div id="content-3" class="accordion-content">
                    <a href="Data-Module-3.html#s3-1-types" class="sidebar-content-link">3.1 Analysis Types</a>
                    <a href="Data-Module-3.html#s3-2-descriptive" class="sidebar-content-link">3.2 Descriptive</a>
                    <a href="Data-Module-3.html#s3-3-diagnostic" class="sidebar-content-link">3.3 Diagnostic</a>
                    <a href="Data-Module-3.html#s3-4-predictive" class="sidebar-content-link">3.4 Predictive</a>
                    <a href="Data-Module-3.html#s3-5-prescriptive" class="sidebar-content-link">3.5 Prescriptive</a>
                    <a href="Data-Module-3.html#s3-6-exploratory" class="sidebar-content-link">3.6 Exploratory (EDA)</a>
                    <a href="Data-Module-3.html#s3-7-drilling" class="sidebar-content-link">3.7 Data Drilling</a>
                    <a href="Data-Module-3.html#s3-8-granularity" class="sidebar-content-link">3.8 Data Granularity</a>
                    <a href="Data-Module-3.html#s3-9-mining" class="sidebar-content-link">3.9 Data Mining</a>
                    <a href="Data-Module-3.html#s3-10-corr" class="sidebar-content-link">3.10 Correlation</a>
                    <a href="Data-Module-3.html#s3-11-pattern" class="sidebar-content-link">3.11 Pattern Recognition</a>
                    <a href="Data-Module-3.html#s3-12-anomaly-outliers" class="sidebar-content-link">3.12 Anomaly & Outliers</a>
                    <a href="Data-Module-3.html#s3-13-evaluate" class="sidebar-content-link">3.13 Explain Results</a>
                    <a href="Data-Module-3.html#s3-14-hypothesis" class="sidebar-content-link">3.14 Hypothesis Testing</a>
                    <a href="Data-Module-3.html#s3-15-prob" class="sidebar-content-link">3.15 Probability/Errors</a>
                    <a href="Data-Module-3.html#s3-16-stats" class="sidebar-content-link">3.16 Statistical Techniques</a>
                    <a href="Data-Module-3.html#s3-17-predictive-models" class="sidebar-content-link">3.17 Predictive Models</a>
                    <a href="Data-Module-3.html#s3-20-ai-role" class="sidebar-content-link">3.20 Role of AI</a>
                    <a href="Data-Module-3.html#s3-21-ml-algo" class="sidebar-content-link">3.21 ML Algorithms</a>
                </div>
            </div>

            <!-- Module 4 -->
            <div class="accordion-item">
                <div class="accordion-header" id="header-4" onclick="toggleAccordion(4)">
                    <span>04 Data Visualization</span>
                    <span class="chevron"></span>
                </div>
                <div id="content-4" class="accordion-content">
                    <a href="Data-Module-4.html#s4-1-report-data" class="sidebar-content-link">4.1 Report Data</a>
                    <a href="Data-Module-4.html#s4-2-types-of-reports" class="sidebar-content-link">4.2 Types of Reports</a>
                    <a href="Data-Module-4.html#s4-3-apple-case" class="sidebar-content-link">4.3 Apple Case Study</a>
                    <a href="Data-Module-4.html#s4-4-importance" class="sidebar-content-link">4.4 Importance/Audience</a>
                    <a href="Data-Module-4.html#s4-5-banavil" class="sidebar-content-link">4.5 Banavil Case Study</a>
                    <a href="Data-Module-4.html#s4-7-tables" class="sidebar-content-link">4.7 Data Tables</a>
                    <a href="Data-Module-4.html#s4-8-conclusions" class="sidebar-content-link">4.8 Conclusions</a>
                    <a href="Data-Module-4.html#s4-9-chart-library" class="sidebar-content-link">4.9 Chart Library</a>
                    <a href="Data-Module-4.html#s4-10-dashboard" class="sidebar-content-link">4.10 Live Dashboard</a>
                </div>
            </div>

            <!-- Module 5 -->
            <div class="accordion-item">
                <div class="accordion-header" id="header-5" onclick="toggleAccordion(5)">
                    <span>05 Responsible Analytics</span>
                    <span class="chevron"></span>
                </div>
                <div id="content-5" class="accordion-content">
                    <a href="Data-Module-5.html#s5-1-concept" class="sidebar-content-link">5.1 Concept</a>
                    <a href="Data-Module-5.html#s5-2-laws" class="sidebar-content-link">5.2 Privacy Laws</a>
                    <a href="Data-Module-5.html#s5-3-best-practices" class="sidebar-content-link">5.3 Best Practices</a>
                    <a href="Data-Module-5.html#s5-4-bias" class="sidebar-content-link">5.4 Types of Bias</a>
                </div>
            </div>

            <h3 style="margin-top:35px;">Navigation</h3>
"""

for f in glob.glob('Data-Module-*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Replace the sidebar content
    pattern = re.compile(r'<h3>Module Path</h3>.*?<h3 style="margin-top:35px;">Navigation</h3>', re.DOTALL)
    if pattern.search(text):
        new_text = pattern.sub(sidebar_html, text)
        
        module_num = f.split('-')[-1].split('.')[0]
        new_text = new_text.replace(f'id="header-{module_num}" class="accordion-header"', f'id="header-{module_num}" class="accordion-header active expanded"')
        new_text = new_text.replace(f'id="content-{module_num}" class="accordion-content"', f'id="content-{module_num}" class="accordion-content expanded"')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_text)
        print(f"Synced sidebar in {f}")
    else:
        print(f"Could not find sidebar pattern in {f}")
