class Block:
    def __init__(self, a):
        self.width = a[0]
        self.length = a[1]
        self.heigth = a[2]

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.heigth

    def get_volume(self):
        return self.width * self.length * self.heigth

    def get_surface_area(self):
        return 2 * (self.length * self.width + self.width * self.heigth + self.heigth * self.length)