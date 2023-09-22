import math    # решение от Nata mas
class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4 / 3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface = 4 * math.pi * (self.radius ** 2)
        return round(surface, 5)

    def get_density(self):
        density = self.mass / ((4 / 3) * math.pi * (self.radius ** 3))
        return round(density, 5)


ball = Sphere(2, 50)
print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())

