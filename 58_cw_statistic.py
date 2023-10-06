class Class:
    _value = 0

    @staticmethod
    def get_number():
        Class._value = 1 if Class._value == 0 else Class._value * 2
        return Class._value

print(Class.get_number())
print(Class.get_number())
print(Class.get_number())
print(Class.get_number())
print(Class.get_number())
print(Class.get_number())