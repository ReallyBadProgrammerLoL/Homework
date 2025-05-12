from math import pi, pow
class Cuboid:
    def __init__(self, a, b, c):
        self.length = a
        self.width = b
        self.height = c
        self.__sq_sur = 2 * (a * b + a * c + b * c)
        self.__volume = a * b * c

    def S(self):
        return round(self.__sq_sur, 2)

    def V(self):
        return round(self.__volume, 2)

class Ball:
    def __init__(self, radius):
        self.r = radius

    def S(self):
        s = 4 * pi * pow(self.r, 2)
        return round(s, 2)

    def V(self):
        v = (4 / 3) * pi * pow(self.r, 3)
        return round(v, 2)