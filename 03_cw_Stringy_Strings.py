
def stringy(size):
    str = '1'
    str_1 = '0'
    str_2 = str + str_1
    if size % 2 == 0:
        return(str_2 * (size//2))
    else:
        return(str_2 * (size//2) + str)