def replace_nth(text, n, old_value, new_value):
    new_str = ''
    count = 0
    for i in text:
        if i == old_value:
            count += 1
            if n <= 0:
                new_str += i
            elif count % n == 0:
                new_str += new_value
            else:
                new_str += old_value
        else:
            new_str += i
    return new_str
print(replace_nth("Vader said: No, I am your father!", 2, 'a', 'o'))git