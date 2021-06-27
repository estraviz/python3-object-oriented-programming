import math


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance(self, p2) -> float:
        return math.sqrt((p2.x - self.x)**2 + (p2.y - self.y)**2)
