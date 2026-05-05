import re

def update_module_3():
    with open('Data-Module-3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 3.11 Pattern Recognition
    content = content.replace('<h5>Sequential Patterns</h5>', '<h5>3.11.1 Sequential Patterns</h5>')
    content = content.replace('<h5>Frequent Patterns</h5>', '<h5>3.11.2 Frequent Patterns</h5>')
    content = content.replace('<h5>Temporal Patterns</h5>', '<h5>3.11.3 Temporal Patterns</h5>')
    
    # 3.14 Evaluate and Explain
    content = content.replace('<h3>Trend and Expected Value</h3>', '<h3>3.14.1 Trend and Expected Value</h3>')
    content = content.replace('<h3>Python Lab: Trend Analysis</h3>', '<h3>3.14.2 Python Lab: Trend Analysis</h3>')
    
    # 3.16 Probability/Errors
    content = content.replace('<h5>Type I Error</h5>', '<h5>3.16.1 Type I Error</h5>')
    content = content.replace('<h5>Type II Error</h5>', '<h5>3.16.2 Type II Error</h5>')
    
    # 3.17 Statistical Techniques
    content = content.replace('<h3>1. Correlation Analysis</h3>', '<h3>3.17.1 Correlation Analysis</h3>')
    content = content.replace('<h3>2. Multiple Regression</h3>', '<h3>3.17.2 Multiple Regression</h3>')
    content = content.replace('<h3>3. t-Tests</h3>', '<h3>3.17.3 t-Tests</h3>')
    content = content.replace('<h3>4. ANOVA (Analysis of Variance)</h3>', '<h3>3.17.4 ANOVA (Analysis of Variance)</h3>')
    content = content.replace('<h3>5. Chi-square test for independence</h3>', '<h3>3.17.5 Chi-square test for independence</h3>')
    content = content.replace('<h3>6. Hypothesis Testing</h3>', '<h3>3.17.6 Practical Hypothesis Testing (Python)</h3>')
    
    # 3.18 Predictive Models
    content = content.replace('<h3>Machine Learning: Simple Linear Regression</h3>', '<h3>3.18.1 Machine Learning: Simple Linear Regression</h3>')

    with open('Data-Module-3.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated Data-Module-3.html")

update_module_3()
