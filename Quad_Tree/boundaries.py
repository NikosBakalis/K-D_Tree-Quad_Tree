def boundaries(points):
    points.sort(key=lambda tup: tup[0])
    mid_x = (points[0][0] + points[-1][0]) / 2
    points.sort(key=lambda tup: tup[1])
    mid_y = (points[0][1] + points[-1][1]) / 2
    return mid_x, mid_y
