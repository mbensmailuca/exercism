def equilateral(sides):
    return is_triangle(sides) and sides[0] == sides[1] and sides[1] == sides[2]


def isosceles(sides):
    return is_triangle(sides) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])
    


def scalene(sides):
    return is_triangle(sides) and not equilateral(sides) and not isosceles(sides)

def is_triangle(sides):
    is_sum_greater = sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]
    is_greater_zero = sides[0] > 0 and sides[1] > 0 and sides[2] > 0
    return is_greater_zero and is_sum_greater
