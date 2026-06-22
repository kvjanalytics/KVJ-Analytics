import re

def update_roadmap(path, prefix, mock_codes):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the new script and modal logic
    auto_unlock_js = f"""
    <script>
        let currentExpectedCode = "";
        let currentTargetUrl = "";

        const modulesCount = 6;
        const requiredScore = 85;

        function isAutoUnlocked() {{
            for (let i = 1; i <= modulesCount; i++) {{
                const score = localStorage.getItem('score_{prefix}' + i);
                if (!score || parseFloat(score) < requiredScore) return false;
            }}
            return true;
        }}

        function checkMockCode(expectedCode, targetUrl) {{
            // Bypass if auto-unlocked OR manual code already entered
            if (isAutoUnlocked() || localStorage.getItem('unlocked_' + expectedCode)) {{
                window.location.href = targetUrl;
                return;
            }}

            currentExpectedCode = expectedCode;
            currentTargetUrl = targetUrl;
            document.getElementById('mockCodeInput').value = '';
            document.getElementById('mockCodeError').style.display = 'none';
            document.getElementById('mockCodeModal').style.display = 'flex';
            
            // Add progress note to modal
            const progressNote = document.getElementById('mockProgressNote');
            if (progressNote) {{
                let missing = [];
                for (let i = 1; i <= modulesCount; i++) {{
                    const s = localStorage.getItem('score_{prefix}' + i);
                    if (!s || parseFloat(s) < requiredScore) missing.push(i);
                }}
                if (missing.length > 0) {{
                    progressNote.innerText = "Locked: Complete Modules " + missing.join(", ") + " with 85%+ to unlock automatically.";
                    progressNote.style.display = 'block';
                }} else {{
                    progressNote.style.display = 'none';
                }}
            }}

            setTimeout(() => document.getElementById('mockCodeInput').focus(), 100);
        }}

        function closeMockModal() {{
            document.getElementById('mockCodeModal').style.display = 'none';
        }}

        function submitMockCode() {{
            const code = document.getElementById('mockCodeInput').value.trim().toUpperCase();
            if (code === currentExpectedCode) {{
                localStorage.setItem('unlocked_' + currentExpectedCode, 'true');
                window.location.href = currentTargetUrl;
            }} else {{
                document.getElementById('mockCodeError').style.display = 'block';
                document.getElementById('mockCodeInput').style.borderColor = '#ef4444';
            }}
        }}
        
        document.getElementById('mockCodeInput').addEventListener('keypress', function (e) {{
            if (e.key === 'Enter') submitMockCode();
        }});

        // Initialize locks on page load
        document.addEventListener('DOMContentLoaded', () => {{
            const buttons = document.querySelectorAll('.btn-mock');
            const unlockedAutomatically = isAutoUnlocked();
            
            buttons.forEach(btn => {{
                const onclick = btn.getAttribute('onclick');
                if (onclick && onclick.includes('checkMockCode')) {{
                    const match = onclick.match(/'([^']+)'/);
                    if (match && match[1]) {{
                        const code = match[1];
                        if (unlockedAutomatically || localStorage.getItem('unlocked_' + code)) {{
                            btn.innerHTML = 'Take Mock'; 
                        }} else {{
                            btn.innerHTML = '🔒 Take Mock';
                        }}
                    }}
                }}
            }});
        }});
    </script>
"""

    # Add the progress note div to the modal
    modal_body_pattern = r'(<p style="color:#64748b; font-size:0.95rem; margin-bottom:24px; font-family:\'Inter\', sans-serif;">.*?</p>)'
    content = re.sub(modal_body_pattern, r'\1\n            <div id="mockProgressNote" style="font-size: 0.8rem; color: #f59e0b; background: #fffbeb; padding: 10px; border-radius: 8px; margin-bottom: 20px; display: none; font-weight: 500;"></div>', content)

    # Replace the old script block
    script_pattern = re.compile(r'<script>\s*let currentExpectedCode.*?</script>', re.DOTALL)
    content = script_pattern.sub(auto_unlock_js, content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {path}")

# Python prefix is empty because IDs are just 1, 2, 3...
update_roadmap('c:/Users/kj anand/Downloads/Quiz DD/roadmap.html', '', ['PYMOCK1', 'PYMOCK2', 'PYMOCK3'])
# Data prefix is 'data' because IDs are data1, data2...
update_roadmap('c:/Users/kj anand/Downloads/Quiz DD/data_roadmap.html', 'data', ['DAMOCK1', 'DAMOCK2', 'DAMOCK3'])
