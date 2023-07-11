import turtle
import math
bob = turtle.Turtle()

def square(t,length):
    """Draw 4 line segments with the given length and a 90 degree turn in between each.
    t is a turtle."""
    for i in range(4):
        t.fd(length)
        t.lt(90)
        
def polygon(t,length,sides):
    """Calculate the internal angle for a polygon of 'sides' sides, then pass it to polygonline to draw."""
    angle = 360.0/sides
    polygonline(t,length,sides,angle)
        
def polygonline(t,length,sides,angle):
    """Draw the number of line segments in 'sides', with the given length and angle between each.
    Again, t is a turtle."""
    for i in range(sides):
        t.fd(length)
        t.lt(angle)
        
def circle(t,radius):
    """Draws an arc of 360 degrees, i.e. a circle."""
    arc(t,radius,360)
    
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
    
        
square(bob,247)
polygon(bob,60,7)
circle(bob,90)
arc(bob,120,235)
    
turtle.mainloop()