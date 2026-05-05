import re

def update_module_5():
    with open('Data-Module-5.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 5.2 Privacy Laws
    laws = [
        'General Data Protection Regulation (GDPR)',
        'California Consumer Privacy Act (CCPA)',
        'Health Insurance Portability and Accountability Act (HIPAA)',
        'Family Educational Rights and Privacy Act (FERPA)',
        'Personal Information Protection and Electronic Documents Act (PIPEDA)',
        'Institutional Review Board (IRB)',
        'PCI DSS (Payment Card Industry Data Security Standard)'
    ]
    
    # GDPR and CCPA both have "1. " in front in the current file
    content = content.replace('<h3>1. General Data Protection Regulation (GDPR)</h3>', '<h3>5.2.1 General Data Protection Regulation (GDPR)</h3>')
    content = content.replace('<h3>1. California Consumer Privacy Act (CCPA)</h3>', '<h3>5.2.2 California Consumer Privacy Act (CCPA)</h3>')
    
    # Others
    content = content.replace('<h3>Health Insurance Portability and Accountability Act (HIPAA)</h3>', '<h3>5.2.3 Health Insurance Portability and Accountability Act (HIPAA)</h3>')
    content = content.replace('<h3>Family Educational Rights and Privacy Act (FERPA)</h3>', '<h3>5.2.4 Family Educational Rights and Privacy Act (FERPA)</h3>')
    content = content.replace('<h3>Personal Information Protection and Electronic Documents Act (PIPEDA)</h3>', '<h3>5.2.5 Personal Information Protection and Electronic Documents Act (PIPEDA)</h3>')
    content = content.replace('<h3>Institutional Review Board (IRB)</h3>', '<h3>5.2.6 Institutional Review Board (IRB)</h3>')
    content = content.replace('<h3>PCI DSS (Payment Card Industry Data Security Standard)</h3>', '<h3>5.2.7 PCI DSS (Payment Card Industry Data Security Standard)</h3>')
    
    # 5.3 Best Practices
    for i in range(1, 16):
        content = content.replace(f'<h4>{i}. ', f'<h4>5.3.{i} ')
    
    # 5.4 Types of Bias
    bias_types = [
        'Sampling Bias', 'Measurement Bias', 'Confirmation Bias', 'Non-response Bias',
        'Selection Bias', 'Data Processing Bias', 'Survivorship Bias', 'Recall Bias',
        'Observer Bias', 'Algorithmic Bias'
    ]
    for i, bias in enumerate(bias_types, 1):
        content = content.replace(f'<h4>{i}. {bias}</h4>', f'<h4>5.4.{i} {bias}</h4>')

    with open('Data-Module-5.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated Data-Module-5.html")

update_module_5()
