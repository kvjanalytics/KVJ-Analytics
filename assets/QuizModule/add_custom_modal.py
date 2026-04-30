import re

modal_code = """
    <!-- Mock Access Modal -->
    <div id="mockCodeModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(15, 23, 42, 0.6); z-index:9999; align-items:center; justify-content:center; backdrop-filter: blur(4px);">
        <div style="background:#ffffff; padding:32px; border-radius:20px; width:90%; max-width:400px; text-align:center; box-shadow:0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04); transform: translateY(0); transition: transform 0.3s ease-out;">
            <div style="width:50px; height:50px; background:#e0f2fe; color:#0284c7; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 20px auto;">
                <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
            </div>
            <h3 style="margin:0 0 10px 0; color:#0f172a; font-size:1.3rem; font-weight:700; font-family:'Inter', sans-serif;">Mock Test Access</h3>
            <p style="color:#64748b; font-size:0.95rem; margin-bottom:24px; font-family:'Inter', sans-serif;">Please enter your secure access code to begin the assessment.</p>
            <input type="text" id="mockCodeInput" placeholder="Enter Access Code" style="width:100%; padding:14px; border:2px solid #e2e8f0; border-radius:12px; margin-bottom:12px; font-size:1rem; text-align:center; text-transform:uppercase; font-family:'Inter', sans-serif; outline:none; transition:border-color 0.2s;" onfocus="this.style.borderColor='#0284c7'" onblur="this.style.borderColor='#e2e8f0'">
            <div id="mockCodeError" style="color:#ef4444; font-size:0.85rem; margin-bottom:20px; display:none; font-weight:600;">❌ Incorrect code. Please try again.</div>
            <div style="display:flex; gap:12px;">
                <button onclick="closeMockModal()" style="flex:1; padding:12px; border:none; background:#f1f5f9; color:#475569; border-radius:10px; cursor:pointer; font-weight:600; font-family:'Inter', sans-serif; font-size:0.95rem; transition:background 0.2s;" onmouseover="this.style.background='#e2e8f0'" onmouseout="this.style.background='#f1f5f9'">Cancel</button>
                <button onclick="submitMockCode()" style="flex:1; padding:12px; border:none; background:#0284c7; color:#ffffff; border-radius:10px; cursor:pointer; font-weight:600; font-family:'Inter', sans-serif; font-size:0.95rem; transition:background 0.2s;" onmouseover="this.style.background='#0369a1'" onmouseout="this.style.background='#0284c7'">Access Mock</button>
            </div>
        </div>
    </div>

    <script>
        let currentExpectedCode = "";
        let currentTargetUrl = "";

        function checkMockCode(expectedCode, targetUrl) {
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
                window.location.href = currentTargetUrl;
            } else {
                document.getElementById('mockCodeError').style.display = 'block';
                document.getElementById('mockCodeInput').style.borderColor = '#ef4444';
            }
        }
        
        // Enter key support
        document.getElementById('mockCodeInput').addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                submitMockCode();
            }
        });
    </script>
</body>
"""

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find the old script block I just added
    old_script_pattern = re.compile(r'<script>\s*function checkMockCode.*?</script>\s*</body>', re.DOTALL)
    
    if old_script_pattern.search(text):
        new_text = old_script_pattern.sub(modal_code.replace('\\', '\\\\'), text)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f"Updated {filename}")
    else:
        print(f"Could not find old script block in {filename}")

update_file('c:/Users/kj anand/Downloads/Quiz DD/roadmap.html')
update_file('c:/Users/kj anand/Downloads/Quiz DD/data_roadmap.html')
