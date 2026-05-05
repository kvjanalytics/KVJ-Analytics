import html.parser

class HTMLValidator(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in ['br', 'img', 'hr', 'input', 'link', 'meta']:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag not in ['br', 'img', 'hr', 'input', 'link', 'meta']:
            if not self.stack:
                self.errors.append(f"Orphan closing tag: </{tag}>")
            else:
                last = self.stack.pop()
                if last != tag:
                    self.errors.append(f"Mismatched tag: expected </{last}>, found </{tag}>")

    def close(self):
        super().close()
        while self.stack:
            self.errors.append(f"Unclosed tag: <{self.stack.pop()}>")

with open(r'c:\Users\kj anand\Downloads\Quiz DD\Data-Module-5.html', 'r', encoding='utf-8') as f:
    content = f.read()

validator = HTMLValidator()
validator.feed(content)
validator.close()

if validator.errors:
    print("Errors found:")
    for err in validator.errors:
        print(err)
else:
    print("No HTML structural errors found.")
