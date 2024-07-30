from math import pi


class Math:
    def __init__(self):
        self.pi = pi

    def calculate_circumference(self, radius):
        return 2 * self.pi * radius
