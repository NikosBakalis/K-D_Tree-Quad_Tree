points = [[-3, 1], [1, 1], [-1, -5], [1, -1]]


class QuadTree:
    def __init__(self):
        self.max_width = 0
        self.max_height = 0
        self.mid_point = []


def boundaries(max_width, max_height):
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


def insert(minimum, mid, maximum):
    for point in points:
        print(point)
        if -minimum <= point[0] <= mid[0] and mid[1] <= point[1] <= maximum:
            print("Top Left")
        if mid[0] <= point[0] <= maximum and mid[1] <= point[1] <= maximum:
            print("Top Right")
        if -minimum <= point[0] <= mid[0] and -minimum <= point[1] <= mid[1]:
            print("Bottom Left")
        if mid[0] <= point[0] <= maximum and -minimum <= point[1] <= mid[1]:
            print("Bottom Right")
    print(points)


# qt = QuadTree()
boundaries(0, 0)
insert(5, [0, 0], 5)  # TODO: parse the actual numbers
