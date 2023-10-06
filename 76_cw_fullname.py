import re

def initials(name):
    full = name.split()
    fio = ''
    for el in range(len(full) - 1):
        fio += full[el][0].upper() + '.'
    return fio + full[-1].capitalize()

'''
Vadim Trefilov solution:
'''
def initials2(name):
    name = name.title().split(' ')
    x = [re.findall(r'\w', elem)[0] for elem in name[:-1]]
    return '.'.join(x) + '.' + name[-1]