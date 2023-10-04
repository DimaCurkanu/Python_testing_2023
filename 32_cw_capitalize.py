import re

def drop_cap(words):
    return re.sub(r'[A-z]{3,}', lambda m: m.group(0).capitalize(),words)
'''
our solution: ---> Iryna Kolhanova
'''
def drop_cap2(words):
    upper_case_words = []
    words2 = words.split(' ')
    for word in words2:
        if len(word) > 2:
            upper_case_words.append(word.capitalize())
        else:
            upper_case_words.append(word)
    return ' '.join(upper_case_words)