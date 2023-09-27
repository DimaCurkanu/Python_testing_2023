import re

def is_digit(n):
    x = re.fullmatch('^\d$', n)
    return bool(x)

'''
++++++ Solution in one string --------->
def is_digit(n):
    return n.isdigit() and len(n)==1
'''