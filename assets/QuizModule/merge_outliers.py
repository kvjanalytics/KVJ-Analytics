import re

def merge_and_renumber():
    file_path = 'Data-Module-3.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Merge 3.12 and 3.13
    # Find the start of 3.12 and end of 3.13
    start_312 = content.find('<div id="s3-12-anomaly"')
    end_313 = content.find('<div id="s3-14-evaluate"')
    
    if start_312 == -1 or end_313 == -1:
        print("Markers not found for merge")
        return

    combined_section = """
            <div id="s3-12-anomaly-outliers" class="slide-header" style="margin-top: 80px;">
                <h3>3.12 Anomaly Detection & Outliers</h3>
            </div>

            <div class="concept-visual-container" style="align-items: flex-start; gap: 40px; background: white; padding: 40px; border-radius: 24px; border: 1px solid #f1f5f9;">
                <div class="comparison-side" style="text-align: left; flex: 1.2;">
                    <p style="font-size: 18px; line-height: 1.8; color: #334155;">
                        <strong>Anomaly detection</strong>, also known as <strong>outlier analysis</strong>, aims to identify rare or unusual data objects that deviate significantly from the rest of the dataset.
                    </p>
                    
                    <div style="margin-top: 25px; padding: 20px; background: #fff1f2; border-left: 4px solid #e11d48; border-radius: 8px; margin-bottom: 25px;">
                        <h5 style="margin: 0 0 10px 0; color: #9f1239; font-size: 16px;">Common Applications:</h5>
                        <ul style="margin: 0; padding-left: 20px; font-size: 15px; color: #9f1239; line-height: 1.6;">
                            <li>Detecting fraudulent credit card transactions</li>
                            <li>Identifying network intrusions (Cybersecurity)</li>
                            <li>Spotting manufacturing defects</li>
                            <li>Monitoring abnormal behavior in healthcare data</li>
                        </ul>
                    </div>

                    <div style="padding: 25px; background: #f0f9ff; border-left: 5px solid #0ea5e9; border-radius: 8px;">
                        <h5 style="margin-top: 0; color: #0369a1; font-size: 16px;">What causes outliers?</h5>
                        <p style="font-size: 15px; color: #0c4a6e; line-height: 1.7; margin-bottom: 0;">
                            Outliers can be caused by <strong>measurement errors</strong> (faulty equipment) or <strong>execution errors</strong> (incorrect data entry). Identifying them is a crucial part of data mining and preprocessing.
                        </p>
                    </div>
                </div>
                <div class="comparison-side" style="flex: 1; display: flex; flex-direction: column; align-items: center;">
                    <div style="background: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; width: 100%;">
                        <svg viewBox="0 0 300 220" style="width: 100%; height: auto;">
                            <path d="M40 20 L40 180 L280 180" fill="none" stroke="#333" stroke-width="3" stroke-linecap="round"/>
                            <path d="M35 30 L40 20 L45 30" fill="none" stroke="#333" stroke-width="3"/>
                            <path d="M270 175 L280 180 L270 185" fill="none" stroke="#333" stroke-width="3"/>
                            <circle cx="80" cy="150" r="6" fill="#10b981"/><circle cx="100" cy="140" r="6" fill="#10b981"/><circle cx="120" cy="160" r="6" fill="#10b981"/><circle cx="140" cy="130" r="6" fill="#10b981"/><circle cx="160" cy="150" r="6" fill="#10b981"/><circle cx="180" cy="120" r="6" fill="#10b981"/><circle cx="200" cy="140" r="6" fill="#10b981"/><circle cx="220" cy="110" r="6" fill="#10b981"/><circle cx="240" cy="130" r="6" fill="#10b981"/><circle cx="130" cy="100" r="6" fill="#10b981"/><circle cx="170" cy="90" r="6" fill="#10b981"/><circle cx="210" cy="80" r="6" fill="#10b981"/><circle cx="250" cy="100" r="6" fill="#10b981"/>
                            <circle cx="100" cy="60" r="8" fill="#e11d48"/>
                            <text x="115" y="55" font-size="12" font-weight="bold" fill="#e11d48">OUTLIER</text>
                        </svg>
                    </div>
                    <p style="font-size: 14px; color: #1e293b; font-weight: 600; margin-top: 15px; font-style: italic;">Visual representation of a statistical outlier.</p>
                </div>
            </div>
"""
    
    content = content[:start_312] + combined_section + content[end_313:]

    # 2. Re-number subsequent sections
    # 3.14 -> 3.13, etc.
    # We need to find "3.14", "3.15", ..., "3.22" and decrement them.
    for i in range(14, 23):
        old_num = f"3.{i}"
        new_num = f"3.{i-1}"
        content = content.replace(f"<h3>{old_num}", f"<h3>{new_num}")
        # Also in IDs? 
        # Actually s3-14-evaluate -> s3-13-evaluate
        old_id = f"s3-{i}"
        new_id = f"s3-{i-1}"
        content = content.replace(f'id="{old_id}', f'id="{new_id}')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully merged 3.12/3.13 and re-numbered")

merge_and_renumber()
