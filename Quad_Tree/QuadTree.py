points = [[-3, 1], [1, 1], [-1, -5], [1, -1]]


class QuadTree:
    def __init__(self):
        self.max_width = 0
        self.max_height = 0
        self.mid_point = []

    def boundaries(self, max_width, max_height):
        for i in points:
            if i[0] < 0:
                i[0] = i[0] * (-1)
                if i[0] > max_width:
                    max_width = i[0] * 2
                else:
                    continue
        for i in points:
            if i[1] < 0:
                i[1] = i[1] * (-1)
                if i[1] > max_height:
                    max_height = i[1] * 2
                else:
                    continue
        print(max_width, max_height)
        mid_point = [max_width / 2, max_height / 2]
        print(mid_point)

        def build():
            print("He will be the build")


def insert():
    for point in points:
        print(point)
        if -5 <= point[0] <= 0 and 0 <= point[1] <= 5:
            print("Top Left")
        if 0 <= point[0] <= 5 and 0 <= point[1] <= 5:
            print("Top Right")
        if -5 <= point[0] <= 0 and -5 <= point[1] <= 0:
            print("Bottom Left")
        if 0 <= point[0] <= 5 and -5 <= point[1] <= 0:
            print("Bottom Right")
    print(points)


insert()
qt = QuadTree
qt.boundaries(qt, 0, 0)
