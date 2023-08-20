import math
import copy

class Circle:
    """ Attributes Centre and Radius.
        Centre is a Point object, Radius is a number"""
    
class Point:
    """Represents a point in 2-D space."""

class Rectangle:
    """ Represents a rectangle.
    attribures: width, height, corner.
    """

def point_in_circle(circ, p):
    """Return True if p lies within or on the boundary of circ"""
    if distance_between_points(p, circ.centre) <= circ.radius:
        return True
    return False

def rect_in_circle(circ,rect):
    """Return True if rectangle rect lies entirely within circ.
       It is enough to check all four corners lie within."""
    if distance_between_points(rect.corner, circ.centre) > circ.radius:
        return False
    rect.corner2 = copy.copy(rect.corner)
    rect.corner2.x += rect.width
    if distance_between_points(rect.corner2, circ.centre) > circ.radius:
        return False
    rect.corner2.y += rect.height
    if distance_between_points(rect.corner2, circ.centre) > circ.radius:
        return False
    rect.corner2.x += (-rect.width)
    if distance_between_points(rect.corner2, circ.centre) > circ.radius:
        return False
    return True

def rect_circle_overlap(circ,rect):
    """Return True if any corner of the rectangle is within the circle."""
    if distance_between_points(rect.corner, circ.centre) <= circ.radius:
        return True
    rect.corner2 = copy.copy(rect.corner)
    rect.corner2.x += rect.width
    if distance_between_points(rect.corner2, circ.centre) <= circ.radius:
        return True
    rect.corner2.y += rect.height
    if distance_between_points(rect.corner2, circ.centre) <= circ.radius:
        return True
    rect.corner2.x += (-rect.width)
    if distance_between_points(rect.corner2, circ.centre) <= circ.radius:
        return True
    return False
    

def distance_between_points(p1,p2):
    distance = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    print('distance = ', distance)
    return(distance)

circ = Circle()
circ.centre = Point()
circ.centre.x = 0
circ.centre.y = 0
circ.radius = 5

#point = Point()
#point.x = 19
#point.y = 11

#print(point_in_circle(circ,point))

box = Rectangle()
box.corner = Point()
box.corner.x = 4.5
box.corner.y = -3
box.width = 4
box.height = 3

print(rect_in_circle(circ,box))
print(rect_circle_overlap(circ,box))