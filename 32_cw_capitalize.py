import re

def drop_cap(words):
    return re.sub(r'[A-z]{3,}', lambda m: m.group(0).capitalize(),words)
