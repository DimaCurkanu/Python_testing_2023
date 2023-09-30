import re

def is_lock_ness_monster(string):
    pattern = r"(tree fiddy|3\.50|three fifty)"
    x = re.findall(pattern, string)
    return len(x) > 0

print(is_lock_ness_monster("I'm from Scottland. I moved here to be with my family sir. Please, $3.50 would go a long way to help me find them"))