
import re
import json

def process_file(filename):
    print(f"Processing {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to find all "q": "..." values and transform them.
    # However, some might be in single quotes, etc.
    # We will use a regex to find all q: "..." or q: '...'
    
    def transform_q(match):
        full_match = match.group(0)
        q_text = match.group(2)
        quote_char = match.group(1)
        
        # 1. Remove <strong> and <b> tags
        q_text = re.sub(r'<(/?strong|/?b)>', '', q_text)
        
        # 2. Extract Marks
        # Pattern 1: (X Mark[s]) at start
        marks_match = re.match(r'^\s*\(\d+\s*Marks?\)\s*', q_text)
        marks_str = ""
        if marks_match:
            marks_str = marks_match.group(0).strip()
            q_text = q_text[marks_match.end():].strip()
        
        # Pattern 2: <span ...>X point[s]</span>
        span_match = re.search(r'<span[^>]*>\s*\d+\s*points?\s*</span>', q_text, re.IGNORECASE)
        if span_match:
            # If we didn't get marks from Pattern 1, try to extract from this
            if not marks_str:
                m = re.search(r'(\d+)\s*points?', span_match.group(0), re.IGNORECASE)
                if m:
                    val = m.group(1)
                    marks_str = f"({val} {'Marks' if int(val) > 1 else 'Mark'})"
            q_text = q_text[:span_match.start()] + q_text[span_match.end():]
            q_text = q_text.strip()

        # 3. Handle cases where marks might be mentioned in the text differently or not at all
        # If we have marks_str, append it to the end.
        # But where to append? Before or after <br>?
        # The user example: "...once, more than once.(4 Marks)"
        # So right at the end of the text.
        
        if marks_str:
            # Clean up trailing <br> tags before appending
            q_text = re.sub(r'(<br\s*/?>\s*)+$', '', q_text).strip()
            q_text = f"{q_text}{marks_str}"
            
        return f'q: {quote_char}{q_text}{quote_char}'

    # Use a regex that captures q: "..." or q: '...'
    # We look for q: followed by optional whitespace, then a quote.
    new_content = re.sub(r'q:\s*(["\'])(.*?)\1', transform_q, content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Finished {filename}")

process_file('data_quiz_data.js')
process_file('quiz_data.js')
