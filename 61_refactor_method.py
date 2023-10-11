# TODO: This method needs to be called multiple times for the same person (my_name).
# It would be nice if we didnt have to always pass in my_name every time we needed to great someone.
class Person:
    def __init__(self, name):
        self.name = name

    def get_my_name(self):
        return self.name

    def greet(self, your_name):
        return f'Hello {your_name}, my name is {self.get_my_name()}'