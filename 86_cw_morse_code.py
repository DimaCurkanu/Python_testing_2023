from preloaded import MORSE_CODE

def decode_morse(morse_code):
    res = morse_code.split(' ')
    s = ''
    for i in res:
        if i == '':
            s += ' '
        else:
            s += MORSE_CODE[i]
    return s.replace('  ', ' ').strip()

    # Remember - you can use the preloaded MORSE_CODE dictionary:
    # For example:
    # MORSE_CODE['.-'] = 'A'
    # MORSE_CODE['--...'] = '7'
    # MORSE_CODE['...-..-'] = '$'
