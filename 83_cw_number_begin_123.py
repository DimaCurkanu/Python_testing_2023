def validate_code(code):
    return str(code)[0] == '1' or str(code)[0] == '2' or str(code)[0] == '3'

'''
more solutions
'''
def validate_code1(code):
    return str(code).startswith(('1', '2', '3'))

'''
one more + regular expressions
'''
def validate_code2(code):
    import re
    return bool(re.match(r"^[123]\d*$",str(code)))

'''
simple solution:
'''
def validate_code3(code):
    return str(code)[0] in '123'