def transpose_two_strings(arr):
    s = ''
    n = max(len(arr[0]), len(arr[1]))
    if len(arr[0]) > len(arr[1]):
        arr[1] = arr[1].ljust(len(arr[0]), ' ')
    elif len(arr[1]) > len(arr[0]):
        arr[0] = arr[0].ljust(len(arr[1]), ' ')
    for i in range(n):
        s += ''.join(arr[0][i] + ' ' + arr[1][i])
        if i < n - 1:
            s += '\n'
    return s


  # 2-е решение -->
def transpose_two_strings1(arr):
    s = ''
    n = max(len(arr[0]), len(arr[1]))
    for i in range(n):
        char1 = arr[0][i] if i < len(arr[0]) else ' '
        char2 = arr[1][i] if i < len(arr[1]) else ' '
        s += ''.join(char1 + ' ' + char2)
        if i < n - 1:
            s += '\n'
    return s
