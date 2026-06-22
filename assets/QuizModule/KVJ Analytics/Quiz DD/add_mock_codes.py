import re

# Update roadmap.html
with open('c:/Users/kj anand/Downloads/Quiz DD/roadmap.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace mock links
text = re.sub(r'<a href="module_quiz\.html\?mock=1" class="btn-mock">Take Mock</a>', r'<a href="javascript:void(0)" onclick="checkMockCode(\'PYMOCK1\', \'module_quiz.html?mock=1\')" class="btn-mock">Take Mock</a>', text)
text = re.sub(r'<a href="module_quiz\.html\?mock=2" class="btn-mock">Take Mock</a>', r'<a href="javascript:void(0)" onclick="checkMockCode(\'PYMOCK2\', \'module_quiz.html?mock=2\')" class="btn-mock">Take Mock</a>', text)
text = re.sub(r'<a href="module_quiz\.html\?mock=3" class="btn-mock">Take Mock</a>', r'<a href="javascript:void(0)" onclick="checkMockCode(\'PYMOCK3\', \'module_quiz.html?mock=3\')" class="btn-mock">Take Mock</a>', text)

# Add script
script = """
    <script>
        function checkMockCode(expectedCode, targetUrl) {
            var code = prompt("Please enter the access code to take this Mock Test:");
            if (code === null) return; 
            if (code.trim().toUpperCase() === expectedCode) {
                window.location.href = targetUrl;
            } else {
                alert("Incorrect Access Code. Registration blocked.");
            }
        }
    </script>
</body>
"""
text = text.replace('</body>', script)

with open('c:/Users/kj anand/Downloads/Quiz DD/roadmap.html', 'w', encoding='utf-8') as f:
    f.write(text)


# Update data_roadmap.html
with open('c:/Users/kj anand/Downloads/Quiz DD/data_roadmap.html', 'r', encoding='utf-8') as f:
    text2 = f.read()

# Replace mock links
text2 = re.sub(r'<a href="module_quiz\.html\?mock=da_mock1" class="btn-mock">Take Mock</a>', r'<a href="javascript:void(0)" onclick="checkMockCode(\'DAMOCK1\', \'module_quiz.html?mock=da_mock1\')" class="btn-mock">Take Mock</a>', text2)
text2 = re.sub(r'<a href="module_quiz\.html\?mock=da_mock2" class="btn-mock">Take Mock</a>', r'<a href="javascript:void(0)" onclick="checkMockCode(\'DAMOCK2\', \'module_quiz.html?mock=da_mock2\')" class="btn-mock">Take Mock</a>', text2)
text2 = re.sub(r'<a href="module_quiz\.html\?mock=da_mock3" class="btn-mock">Take Mock</a>', r'<a href="javascript:void(0)" onclick="checkMockCode(\'DAMOCK3\', \'module_quiz.html?mock=da_mock3\')" class="btn-mock">Take Mock</a>', text2)

# Add script
text2 = text2.replace('</body>', script)

with open('c:/Users/kj anand/Downloads/Quiz DD/data_roadmap.html', 'w', encoding='utf-8') as f:
    f.write(text2)
    
print("Updated roadmaps successfully.")
