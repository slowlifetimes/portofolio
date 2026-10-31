import glob
from html.parser import HTMLParser

class TagValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        self.void_tags = {
            'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
            'link', 'meta', 'param', 'source', 'track', 'wbr'
        }

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_tags:
            self.stack.append((tag.lower(), self.getpos()))

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in self.void_tags:
            return
        if not self.stack:
            self.errors.append(f"Unexpected closing tag </{tag}> at line {self.getpos()[0]}")
            return
        last_tag, pos = self.stack.pop()
        if last_tag != tag:
            self.errors.append(f"Mismatched tag: expected </{last_tag}> (opened at line {pos[0]}), found </{tag}> at line {self.getpos()[0]}")

def check_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    parser = TagValidator()
    parser.feed(content)
    if parser.errors:
        print(f"[{filepath}] ERRORS ({len(parser.errors)}):")
        for err in parser.errors[:5]:
            print(f"  {err}")
    elif parser.stack:
        print(f"[{filepath}] UNCLOSED TAGS ({len(parser.stack)}):")
        for tag, pos in parser.stack[-5:]:
            print(f"  <{tag}> opened at line {pos[0]}")
    else:
        print(f"[{filepath}] OK! All tags balanced.")

check_file("berkas.html")
check_file("ppl-mandiri-siklus4.html")
check_file("ppl-mandiri-siklus3.html")
check_file("ppl-mandiri-siklus2.html")
check_file("ppl-mandiri-siklus1.html")
check_file("ppl-mandiri.html")

check_file("model-guru.html")
check_file("profil.html")
check_file("index.html")
