import re
import glob

def fix_m3():
    with open('Data-Module-3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 3.11 Pattern Recognition
    content = re.sub(r'<(h[4-5])[^>]*>\s*Sequential Patterns\s*</\1>', r'<\1 style="margin: 0 0 5px 0; color: #1e40af; font-size: 17px;">3.11.1 Sequential Patterns</\1>', content)
    content = re.sub(r'<(h[4-5])[^>]*>\s*Frequent Patterns\s*</\1>', r'<\1 style="margin: 0 0 5px 0; color: #059669; font-size: 17px;">3.11.2 Frequent Patterns</\1>', content)
    content = re.sub(r'<(h[4-5])[^>]*>\s*Temporal Patterns\s*</\1>', r'<\1 style="margin: 0 0 5px 0; color: #92400e; font-size: 17px;">3.11.3 Temporal Patterns</\1>', content)
    
    # 3.14 Evaluate and Explain
    content = re.sub(r'<(h[2-3])[^>]*>\s*Trend and Expected Value\s*</\1>', r'<\1>3.14.1 Trend and Expected Value</\1>', content)
    content = re.sub(r'<(h[2-3])[^>]*>\s*Python Lab: Trend Analysis\s*</\1>', r'<\1>3.14.2 Python Lab: Trend Analysis</\1>', content)
    
    # 3.16 Probability/Errors
    content = re.sub(r'<(h[4-5])[^>]*>\s*Type I Error\s*</\1>', r'<\1>3.16.1 Type I Error</\1>', content)
    content = re.sub(r'<(h[4-5])[^>]*>\s*Type II Error\s*</\1>', r'<\1>3.16.2 Type II Error</\1>', content)
    
    # 3.17 Statistical Techniques
    # They are numbered as "1. ", "2. ", etc.
    techniques = [
        ('1. Correlation Analysis', '3.17.1 Correlation Analysis'),
        ('2. Multiple Regression', '3.17.2 Multiple Regression'),
        ('3. t-Tests', '3.17.3 t-Tests'),
        ('4. ANOVA \(Analysis of Variance\)', '3.17.4 ANOVA (Analysis of Variance)'),
        ('5. Chi-square test for independence', '3.17.5 Chi-square test for independence'),
        ('6. Hypothesis Testing', '3.17.6 Practical Hypothesis Testing (Python)')
    ]
    for old, new in techniques:
        content = re.sub(f'<(h[2-3])[^>]*>\\s*{old}\\s*</\\1>', f'<\\1>{new}</\\1>', content)
    
    # 3.18 Predictive Models
    content = re.sub(r'<(h[2-3])[^>]*>\s*Machine Learning: Simple Linear Regression\s*</\1>', r'<\1>3.18.1 Machine Learning: Simple Linear Regression</\1>', content)

    with open('Data-Module-3.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed Module 3 with robust regex")

def fix_m4():
    with open('Data-Module-4.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 4.3 Apple
    content = re.sub(r'<(h[4-5])[^>]*>\s*Financial Reports\s*</\1>', r'<\1>4.3.1 Financial Reports</\1>', content)
    content = re.sub(r'<(h[4-5])[^>]*>\s*Sales Reports\s*</\1>', r'<\1>4.3.2 Sales Reports</\1>', content)
    content = re.sub(r'<(h[4-5])[^>]*>\s*Performance Reports\s*</\1>', r'<\1>4.3.3 Performance Reports</\1>', content)
    
    # 4.4
    content = re.sub(r'<(h[2-3])[^>]*>\s*Importance of Reporting\s*</\1>', r'<\1>4.4.1 Importance of Reporting</\1>', content)
    content = re.sub(r'<(h[2-3])[^>]*>\s*Who Uses Reports\?\s*</\1>', r'<\1>4.4.2 Who Uses Reports?</\1>', content)
    
    # 4.9 Charts
    charts = [
        'Column Chart', 'Bar Chart', 'Line Chart', 'Scatter Plot', 
        'Pie Chart', 'Donut Chart', 'Tree Map', 'Area Chart', 
        'Ribbon Chart', 'Funnel Chart', 'Waterfall Chart', 'Sankey Diagram'
    ]
    for i, chart in enumerate(charts, 1):
        content = re.sub(f'<(h[2-3])[^>]*>\\s*{chart}\\s*</\\1>', f'<\\1>4.9.{i} {chart}</\\1>', content)
        
    with open('Data-Module-4.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed Module 4 with robust regex")

fix_m3()
fix_m4()
