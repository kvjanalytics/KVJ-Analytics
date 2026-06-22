import re

modal_and_script = """
    <!-- Mock Access Modal -->
    <div id="mockCodeModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(15, 23, 42, 0.6); z-index:9999; align-items:center; justify-content:center; backdrop-filter: blur(4px);">
        <div style="background:#ffffff; padding:32px; border-radius:20px; width:90%; max-width:400px; text-align:center; box-shadow:0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04);">
            <div style="width:50px; height:50px; background:#e0f2fe; color:#0284c7; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 20px auto;">
                <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
            </div>
            <h3 style="margin:0 0 10px 0; color:#0f172a; font-size:1.3rem; font-weight:700; font-family:'Inter', sans-serif;">Mock Test Access</h3>
            <p style="color:#64748b; font-size:0.95rem; margin-bottom:24px; font-family:'Inter', sans-serif;">Please enter your secure access code to begin the assessment.</p>
            <input type="text" id="mockCodeInput" placeholder="Enter Access Code" style="width:100%; padding:14px; border:2px solid #e2e8f0; border-radius:12px; margin-bottom:12px; font-size:1rem; text-align:center; text-transform:uppercase; font-family:'Inter', sans-serif; outline:none;">
            <div id="mockCodeError" style="color:#ef4444; font-size:0.85rem; margin-bottom:20px; display:none; font-weight:600;">❌ Incorrect code. Please try again.</div>
            <div style="display:flex; gap:12px;">
                <button onclick="closeMockModal()" style="flex:1; padding:12px; border:none; background:#f1f5f9; color:#475569; border-radius:10px; cursor:pointer; font-weight:600; font-family:'Inter', sans-serif;">Cancel</button>
                <button onclick="submitMockCode()" style="flex:1; padding:12px; border:none; background:#0284c7; color:#ffffff; border-radius:10px; cursor:pointer; font-weight:600; font-family:'Inter', sans-serif;">Access Mock</button>
            </div>
        </div>
    </div>

    <script>
        let currentExpectedCode = "";
        let currentTargetUrl = "";

        function checkMockCode(expectedCode, targetUrl) {
            // Check if already unlocked
            if (localStorage.getItem('unlocked_' + expectedCode)) {
                window.location.href = targetUrl;
                return;
            }

            currentExpectedCode = expectedCode;
            currentTargetUrl = targetUrl;
            document.getElementById('mockCodeInput').value = '';
            document.getElementById('mockCodeError').style.display = 'none';
            document.getElementById('mockCodeModal').style.display = 'flex';
            setTimeout(() => document.getElementById('mockCodeInput').focus(), 100);
        }

        function closeMockModal() {
            document.getElementById('mockCodeModal').style.display = 'none';
        }

        function submitMockCode() {
            const code = document.getElementById('mockCodeInput').value.trim().toUpperCase();
            if (code === currentExpectedCode) {
                // Save to localStorage
                localStorage.setItem('unlocked_' + currentExpectedCode, 'true');
                window.location.href = currentTargetUrl;
            } else {
                document.getElementById('mockCodeError').style.display = 'block';
                document.getElementById('mockCodeInput').style.borderColor = '#ef4444';
            }
        }
        
        document.getElementById('mockCodeInput').addEventListener('keypress', function (e) {
            if (e.key === 'Enter') submitMockCode();
        });

        // Initialize locks on page load
        document.addEventListener('DOMContentLoaded', () => {
            const buttons = document.querySelectorAll('.btn-mock');
            buttons.forEach(btn => {
                const onclick = btn.getAttribute('onclick');
                if (onclick && onclick.includes('checkMockCode')) {
                    const match = onclick.match(/'([^']+)'/);
                    if (match && match[1]) {
                        const code = match[1];
                        if (localStorage.getItem('unlocked_' + code)) {
                            btn.innerHTML = 'Take Mock'; // Remove lock if unlocked
                        } else {
                            btn.innerHTML = '🔒 Take Mock'; // Add lock if locked
                        }
                    }
                }
            });
        });
    </script>
</body>
"""

def process_file(path, codes):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix the broken links (remove the extra backslashes)
    # The current links look like onclick="checkMockCode(\'PYMOCK1\', ...)"
    content = re.sub(r"onclick=\"checkMockCode\(\\'([^']+)\\', \\'([^']+)\\'\)\"", r"onclick=\"checkMockCode('\1', '\2')\"", content)
    
    # 2. Add the lock icon if not there (it will be updated by script anyway, but good for initial state)
    # But actually the script handles it on DOMContentLoaded, so we just need valid links.
    
    # 3. Replace the old modal/script block
    # My previous script block pattern:
    # <div id="mockCodeModal" ... </div>\n\n    <script>\n        let currentExpectedCode ... </script>\n</body>
    
    pattern = re.compile(r'<div id=\"mockCodeModal\".*?</script>\s*</body>', re.DOTALL)
    if pattern.search(content):
        content = pattern.sub(modal_and_script, content)
    else:
        # Fallback if the previous block wasn't exactly that
        content = content.replace('</body>', modal_and_script)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {path}")

process_file('c:/Users/kj anand/Downloads/Quiz DD/roadmap.html', ['PYMOCK1', 'PYMOCK2', 'PYMOCK3'])
process_file('c:/Users/kj anand/Downloads/Quiz DD/data_roadmap.html', ['DAMOCK1', 'DAMOCK2', 'DAMOCK3'])
