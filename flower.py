import turtle
import math

def polygonline(t,length,sides,angle):
    """Draw the number of line segments in 'sides', with the given length and angle between each.
    Again, t is a turtle."""
    for i in range(sides):
        t.fd(length)
        t.lt(angle)

def arc(t,radius,angle):
    """Calculate the circumference of an arc of given angle and radius.
    Calculate a suitable number of subdivisions for the arc, then determine the length and angle of each subdivision.
    Then pass this to polygonline to draw the arc."""
    arc_length = 2*math.pi*radius*angle/360
    sides = int(arc_length / 4) + 3
    step_length = arc_length / sides
    step_angle = float(angle) / sides
    t.lt(step_angle/2)
    polygonline(t,step_length,sides,step_angle)
    t.rt(step_angle/2)

def petal(t, r, angle):
    """Draws a petal using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    """Draws a flower with n petals.
    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)


def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()
    
bob = turtle.Turtle()

move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 60.0, 60.0)

move(bob, 100)
flower(bob, 20, 60.0, 60.0)

bob.hideturtle()
turtle.mainloop()