import turtle
import math


def polygon(t,length,n,angle):
    turn = 360/n
    for i in range(int(n*angle/360)):
        t.fd(length)
        t.lt(turn)
        
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
    
def arc2(t,r,angle):
    length = (2 * math.pi * r) / 100
    polygon(t,length,100,angle)
    
def petal(t,r,angle):
    """ draws two arcs with the given length and angle, turning back
        to the start after each one"""
    for i in range(2):
        arc(t,r,angle)
        t.lt(180-angle)
    
def flower(t,r,angle,no_petals):
    """ draws a flower with no_petals number of petals, each offset
        from the previous one by 360/no_petals """
    for i in range(no_petals):
        petal(t,r,angle)
        t.lt(360.0/no_petals)
        
bob = turtle.Turtle()

flower(bob,100,80,12)
#petal(bob,100,50)