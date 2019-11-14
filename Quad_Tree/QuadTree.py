class QT:
    def __init__(self, max_width, max_height):
        self.max_width = max_width
        self.max_height = max_height

        # def build():


def insert():
    points = [[-1, 1], [1, 1], [-1, -1], [1, -1]]
    for point in points.length:
        print(point)
        if -5 <= point[0] <= 0 and 0 <= point[1] <= 5:
            print("Top Left")
            points.remove(point)
        if 0 <= point[0] <= 5 and 0 <= point[1] <= 5:
            print("Top Right")
            points.remove(point)
        if -5 <= point[0] <= 0 and -5 <= point[1] <= 0:
            print("Bottom Left")
            points.remove(point)
        if 0 <= point[0] <= 5 and -5 <= point[1] <= 0:
            print("Bottom Right")
            points.remove(point)
    print(points)


insert()
