class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __contains__(self, point):
        x, y = point
        if not self.x <= x <= self.x + self.w:
            return False
        if not self.y <= y <= self.y + self.h:
            return False
        return True

    def split(self):


class QuadTree:
    def __init__(self, width, height):