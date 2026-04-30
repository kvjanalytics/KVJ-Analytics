import os
import re

def clean_file(path, prefix):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the FULL CLEAN SCRIPT BLOCK
    # Note: I need to preserve the logout, openCertModal etc. functions if they exist.
    
    clean_js = f"""
    <script>
        const scriptURL = "https://script.google.com/macros/s/AKfycbw9mb2dsJ1SSheOcpdcdeE8eKNnuCjK2U9U9kIeHV_2yga8Ujiee1w_huTzc2w5BpWD/exec";
        
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

        function syncProgress() {{
            const phone = localStorage.getItem('strategist_phone');
            if (!phone) {{
                alert("Please log in first to sync your progress.");
                return;
            }}

            const btn = document.getElementById('syncBtn');
            const status = document.getElementById('syncStatus');
            btn.disabled = true;
            btn.innerHTML = 'Syncing...';
            status.style.display = 'block';
            status.innerText = "Connecting to server...";

            const callbackName = 'syncCallback_' + Date.now();
            const script = document.createElement('script');
            
            window[callbackName] = function(data) {{
                btn.disabled = false;
                btn.innerHTML = '<svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg> Sync Progress from Server';
                
                if (data.success && data.scores) {{
                    let count = 0;
                    for (let i = 1; i <= 6; i++) {{
                        localStorage.removeItem('score_' + i);
                        localStorage.removeItem('score_data' + i);
                    }}
                    for (const modId in data.scores) {{
                        localStorage.setItem('score_' + modId, data.scores[modId]);
                        count++;
                    }}
                    if (!isAutoUnlocked()) {{
                        ['PYMOCK1','PYMOCK2','PYMOCK3','DAMOCK1','DAMOCK2','DAMOCK3'].forEach(m => localStorage.removeItem('unlocked_' + m));
                    }}
                    status.innerText = "Successfully synced " + count + " module scores! Refreshing page...";
                    status.style.color = "#059669";
                    setTimeout(() => window.location.reload(), 1500);
                }} else {{
                    status.innerText = "Sync failed: " + (data.error || "No scores found.");
                    status.style.color = "#ef4444";
                }}
                document.body.removeChild(script);
                delete window[callbackName];
            }};

            script.src = `${{scriptURL}}?action=getScores&phone=${{encodeURIComponent(phone)}}&callback=${{callbackName}}&t=${{Date.now()}}`;
            document.body.appendChild(script);
        }}

        function checkMockCode(expectedCode, targetUrl) {{
            if (isAutoUnlocked() || localStorage.getItem('unlocked_' + expectedCode)) {{
                window.location.href = targetUrl;
                return;
            }}
            currentExpectedCode = expectedCode;
            currentTargetUrl = targetUrl;
            document.getElementById('mockCodeInput').value = '';
            document.getElementById('mockCodeError').style.display = 'none';
            document.getElementById('mockCodeModal').style.display = 'flex';
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

        function closeMockModal() {{ document.getElementById('mockCodeModal').style.display = 'none'; }}

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
            
            const phoneInput = document.getElementById('mockCodeInput');
            if (phoneInput) {{
                phoneInput.addEventListener('keypress', function (e) {{
                    if (e.key === 'Enter') submitMockCode();
                }});
            }}
        }});

        function logout() {{
            sessionStorage.clear();
            localStorage.removeItem('strategist_user');
            localStorage.removeItem('strategist_phone');
            localStorage.removeItem('gmail');
            localStorage.removeItem('class_code');
            window.location.href = 'login.html';
        }}

        function openCertModal() {{ document.getElementById('certModal').style.display = 'flex'; }}
        function closeCertModal() {{ document.getElementById('certModal').style.display = 'none'; }}
        window.onclick = function(event) {{
            const modal = document.getElementById('certModal');
            if (event.target == modal) modal.style.display = 'none';
            const mockModal = document.getElementById('mockCodeModal');
            if (event.target == mockModal) mockModal.style.display = 'none';
        }}
    </script>
"""

    # Find the start of the first script tag and the end of the last one
    # We want to replace EVERYTHING from the first <script> to the last </script> in that area.
    
    # Let's find the script block that contains our functions
    script_pattern = re.compile(r'<script>.*?</script>', re.DOTALL)
    
    # Find the FIRST occurrence of <script> after the modules section
    # Actually, let's just replace all script tags that look like they contain our logic.
    
    # BETTER: Just find the first <script> and the last </script> in the file and replace that range if it contains 'syncProgress'
    start_index = content.find('<script>')
    end_index = content.rfind('</script>') + 9
    
    if start_index != -1 and 'syncProgress' in content[start_index:end_index]:
        new_content = content[:start_index] + clean_js + content[end_index:]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned {path}")
    else:
        print(f"Could not find script block to clean in {path}")

clean_file('c:/Users/kj anand/Downloads/Quiz DD/roadmap.html', '')
clean_file('c:/Users/kj anand/Downloads/Quiz DD/data_roadmap.html', 'data')
