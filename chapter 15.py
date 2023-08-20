import math
import copy

class Point:
    """Represents a point in 2-D space."""

class Rectangle:
    """ Represents a rectangle.
    attribures: width, height, corner.
    """

def distance_between_points(p1,p2):
    distance = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    return(distance)

def move_rectangle(rect, dx, dy):
    rect2 = copy.deepcopy(rect)
    rect2.corner.x += dx
    rect2.corner.y += dy
    return(rect2)

point1 = Point()
point2 = Point()

point1.x = 6
point1.y = 2
point2.x = 18
point2.y = -3

print(distance_between_points(point1, point2))

box = Rectangle()
box.width = 20
box.height = 50
box.corner = Point()
box.corner.x = 12
box.corner.y = 19
print(box.width, box.height, box.corner.x, box.corner.y)

box2 = move_rectangle(box, 5, 11)

print(box.width, box.height, box.corner.x, box.corner.y)
print(box2.width, box2.height, box2.corner.x, box2.corner.y)
