import turtle
import math

class Point:
    """Represents a point in 2-D space."""

class Circle:
    """ Attributes Centre and Radius.
        Centre is a Point object, Radius is a number"""
    
class Rectangle:
    """ Represents a rectangle.
    attribures: width, height, corner.
    Corner is a Point object, width and height are numbers.
    """
def move_to_start(t,p):
    """Move the turtle to the start point"""
    t.up()
    t.fd(p.x)
    t.lt(90)
    t.fd(p.y)
    t.rt(90)
    t.down()

def draw_rect(t, rect):
    """First move the turtle to the corner of the rectangle"""
    move_to_start(t,rect.corner)
    """Now draw the sides in turn"""
    t.fd(rect.width)
    t.lt(90)
    t.fd(rect.height)
    t.lt(90)
    t.fd(rect.width)
    t.lt(90)
    t.fd(rect.height)

def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        
def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def draw_circle(t,circ):
    """The circle will start drawing at the bottom point so
    subtract radius from the y co-ordinate of the centre before drawing"""
    circ.centre.y += -circ.radius
    move_to_start(t,circ.centre)
    arc(t,circ.radius,360)

box = Rectangle()
box.corner = Point()
box.corner.x = -100
box.corner.y = 50
box.height = 200
box.width = 100

bob = turtle.Turtle()
draw_rect(bob,box)

circ = Circle()
circ.centre = Point()
circ.centre.x = -100
circ.centre.y = 50
circ.radius = 40

bob.up()
bob.home()
bob.down()
draw_circle(bob,circ)
