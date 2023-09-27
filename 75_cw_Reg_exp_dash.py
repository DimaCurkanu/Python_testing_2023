import re


def insert_dash(num):
    x = str(num)
    return re.sub(r"([13579])(?=[13579])", r'\1-', x)

#  Solution from chat GPT

# import re

# def insert_dash(num):
#     # Convert the number to a string
#     num_str = str(num)

#     # Use regular expression to insert dashes between consecutive odd digits
#     result = re.sub(r'([13579])(?=[13579])', r'\1-', num_str)

#     return result