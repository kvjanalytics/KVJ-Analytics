import re

sync_html = """
    <div style="text-align: center; margin: 20px 0;">
        <button onclick="syncProgress()" id="syncBtn" style="background: #f8fafc; color: #64748b; border: 1.5px solid #e2e8f0; padding: 10px 20px; border-radius: 10px; font-weight: 600; font-size: 0.9rem; cursor: pointer; display: flex; align-items: center; justify-content: center; margin: 0 auto; gap: 8px; transition: all 0.2s;" onmouseover="this.style.background='#fff'; this.style.borderColor='#0284c7'; this.style.color='#0284c7'" onmouseout="this.style.background='#f8fafc'; this.style.borderColor='#e2e8f0'; this.style.color='#64748b'">
            <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
            Sync Progress from Server
        </button>
        <p id="syncStatus" style="font-size: 0.8rem; color: #94a3b8; margin-top: 8px; display: none;"></p>
    </div>
"""

sync_js_function = """
        const scriptURL = "https://script.google.com/macros/s/AKfycbxs8bcb1jw5qpazffbr1U5KvM_PzqAhb_9F3xOSjBQxuu1KaJYFC_DkUovfuloGCCq-/exec";

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
"""

def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Insert Button before Mock Assessments title
    content = content.replace('<h2 class="section-title">Mock Assessments</h2>', sync_html + '<h2 class="section-title">Mock Assessments</h2>')
    
    # Insert JS function into script block
    if '<script>' in content:
        content = content.replace('<script>', '<script>\n' + sync_js_function)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {path}")

update_file('c:/Users/kj anand/Downloads/Quiz DD/roadmap.html')
update_file('c:/Users/kj anand/Downloads/Quiz DD/data_roadmap.html')
