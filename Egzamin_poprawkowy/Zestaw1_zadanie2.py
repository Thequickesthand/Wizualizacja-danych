import math as m


class Kolo:

    def __init__(self, promien):
        self.promien = promien

    def pole(self):
        return m.pow(self.promien, 2) * m.pi


p1 = Kolo(3)
print(p1.pole())
