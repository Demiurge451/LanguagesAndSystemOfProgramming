import math
import re


class Circle:
    def __init__(self, x0: float, y0: float, radius: float):
        self.x0 = x0
        self.y0 = y0
        self.radius = radius


VectorOfCircles = list[Circle]


def find_disjoint_circles(arr: VectorOfCircles) -> VectorOfCircles:
    s = set()
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            dis = distance(arr[i].x0, arr[j].x0, arr[i].y0, arr[j].y0)
            if dis < arr[i].radius + arr[j].radius:
                s.add(i)
                s.add(j)

    res = []
    for i in range(0, len(arr)):
        if i not in s:
            res.append(arr[i])

    return res


def distance(x1: float, x2: float, y1: float, y2: float) -> float:
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def read_from_file() -> VectorOfCircles:
    with open("test1.txt", "r") as f:
        arr = []
        for s in f.readlines():
            pattern = re.compile("[\d\.]+")
            match = re.findall(pattern, s)
            x = float(match[0])
            y = float(match[1])
            r = float(match[2])
            arr.append(Circle(x, y, r))

    return arr


def write_to_file(arr: VectorOfCircles):
    with open("output.txt", "w") as f:
        for i in range(0, len(arr)):
            f.write("%g %g %g\n" % (arr[i].x0, arr[i].y0, arr[i].radius))


def main():
    arr = read_from_file()
    write_to_file(find_disjoint_circles(arr))


main()
