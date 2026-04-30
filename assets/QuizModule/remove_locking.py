import os
import re

def remove_locking(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Restore buttons to direct links
    # Find <a href="javascript:void(0)" onclick="checkMockCode('PYMOCK1', 'module_quiz.html?mock=1')" class="btn-mock">Take Mock</a>
    # Replace with <a href="module_quiz.html?mock=1" class="btn-mock">Take Mock</a>
    content = re.sub(r'onclick="checkMockCode\(\'[^\\\']+\', \'([^\\\']+)\'\)" class="btn-mock"', r'href="\1" class="btn-mock"', content)
    
    # Also handle ones with 🔒 Take Mock (though we'll just set the text to "Take Mock")
    content = content.replace('🔒 Take Mock', 'Take Mock')
    
    # 2. Remove the Mock Code Modal HTML
    # It was a large div with id="mockCodeModal"
    modal_pattern = re.compile(r'<div id="mockCodeModal".*?</div>\s*</div>\s*</div>', re.DOTALL)
    content = modal_pattern.sub('', content)
    
    # 3. Clean up the script
    # We'll remove the functions: checkMockCode, isAutoUnlocked, submitMockCode, closeMockModal
    # and the DOMContentLoaded listener that adds locks.
    
    # Let's find the script block and replace it with a simpler one that just has sync and logout
    script_start = content.find('<script>')
    script_end = content.find('</script>', script_start) + 9
    
    # We want to preserve scriptURL and syncProgress (it's useful for scores) but remove the auto-unlock logic
    # Actually, I'll just keep syncProgress but remove the isAutoUnlocked check inside it.
    
    clean_js = """
    <script>
        const scriptURL = "https://script.google.com/macros/s/AKfycbw9mb2dsJ1SSheOcpdcdeE8eKNnuCjK2U9U9kIeHV_2yga8Ujiee1w_huTzc2w5BpWD/exec";

        function syncProgress() {
            const phone = localStorage.getItem('strategist_phone');
            if (!phone) {
                alert("Please log in first to sync your progress.");
                return;
            }

            const btn = document.getElementById('syncBtn');
            const status = document.getElementById('syncStatus');
            btn.disabled = true;
            btn.innerHTML = 'Syncing...';
            status.style.display = 'block';
            status.innerText = "Connecting to server...";

            const callbackName = 'syncCallback_' + Date.now();
            const script = document.createElement('script');
            
            window[callbackName] = function(data) {
                btn.disabled = false;
                btn.innerHTML = '<svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg> Sync Progress from Server';
                
                if (data.success && data.scores) {
                    let count = 0;
                    for (const modId in data.scores) {
                        localStorage.setItem('score_' + modId, data.scores[modId]);
                        count++;
                    }
                    status.innerText = "Successfully synced " + count + " module scores! Refreshing page...";
                    status.style.color = "#059669";
                    setTimeout(() => window.location.reload(), 1500);
                } else {
                    status.innerText = "Sync failed: " + (data.error || "No scores found.");
                    status.style.color = "#ef4444";
                }
                document.body.removeChild(script);
                delete window[callbackName];
            };

            script.src = `${scriptURL}?action=getScores&phone=${encodeURIComponent(phone)}&callback=${callbackName}&t=${Date.now()}`;
            document.body.appendChild(script);
        }

        function logout() {
            sessionStorage.clear();
            localStorage.removeItem('strategist_user');
            localStorage.removeItem('strategist_phone');
            localStorage.removeItem('gmail');
            localStorage.removeItem('class_code');
            window.location.href = 'login.html';
        }

        function openCertModal() { document.getElementById('certModal').style.display = 'flex'; }
        function closeCertModal() { document.getElementById('certModal').style.display = 'none'; }
        window.onclick = function(event) {
            const modal = document.getElementById('certModal');
            if (event.target == modal) modal.style.display = 'none';
        }
    </script>
    """
    
    content = content[:script_start] + clean_js + content[script_end:]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Removed locking from {path}")

remove_locking('c:/Users/kj anand/Downloads/Quiz DD/roadmap.html')
remove_locking('c:/Users/kj anand/Downloads/Quiz DD/data_roadmap.html')
