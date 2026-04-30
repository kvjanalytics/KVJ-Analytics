import re

# We will modify the syncProgress function to clear manual unlocks if sync is clicked
# and also ensure the lock check is aggressive.

sync_fix_js = """
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
                    // Clear old scores first to ensure a clean sync
                    for (let i = 1; i <= 6; i++) {
                        localStorage.removeItem('score_' + i);
                        localStorage.removeItem('score_data' + i);
                    }
                    
                    for (const modId in data.scores) {
                        localStorage.setItem('score_' + modId, data.scores[modId]);
                        count++;
                    }

                    // Strict: If sync is clicked and they no longer meet the criteria, clear manual overrides too
                    // This ensures that if a teacher lowers a score, clicking sync will re-lock the test.
                    if (!isAutoUnlocked()) {
                        ['PYMOCK1','PYMOCK2','PYMOCK3','DAMOCK1','DAMOCK2','DAMOCK3'].forEach(m => localStorage.removeItem('unlocked_' + m));
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

def update_sync(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the existing syncProgress function
    pattern = re.compile(r'function syncProgress\(\) \{.*?setTimeout\(\(\) => window\.location\.reload\(\), 1500\);.*?\}', re.DOTALL)
    if pattern.search(content):
        content = pattern.sub(sync_fix_js, content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated sync logic in {path}")
    else:
        print(f"Could not find syncProgress function in {path}")

update_sync('c:/Users/kj anand/Downloads/Quiz DD/roadmap.html')
update_sync('c:/Users/kj anand/Downloads/Quiz DD/data_roadmap.html')
