# Task

# Given a point in a Euclidean plane (x and y), return the quadrant the point exists in: 1, 2, 3 or 4 (integer). x and y are non-zero integers, therefore the given point never lies on the axes.

# Examples

# (1, 2)     => 1
# (3, 5)     => 1
# (-10, 100) => 2
# (-1, -9)   => 3
# (19, -56)  => 4

def quadrant(x, y):
    if x >=1 and y >= 1:
        return 1
    if x < 0 and y < 0:
        return 3
    if x < 0 and y >= 1:
        return 2
    if x > 0 and y < 0:
        return 4
print(quadrant(3, 7))
print(quadrant(-10, 100))
print(quadrant(-1, -9))
print(quadrant(19, -56))
print(quadrant(0, 0))


def quadrant2(x, y):
    if x > 0:
        if y >0:
            return 1
        else:
            return 4
    if x < 0:
        if y < 0:
            return 3
        else:
            return 2
print(quadrant2(3, 7))
print(quadrant2(-10, 100))
print(quadrant2(-1, -9))
print(quadrant2(19, -56))       
print(quadrant(0, 0))

