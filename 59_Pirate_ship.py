class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        weight = self.draft - self.crew * 1.5
        return weight > 20

our_ship = Ship(80,10)
print(our_ship.is_worth_it())

