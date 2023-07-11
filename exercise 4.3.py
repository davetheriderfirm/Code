import turtle
import math

def triangle(t,r,sides):
    """ draw a triangle segment for a pie with sides number of segments and r radius """
    # calculate the centre angle
    centre_angle = 360.0 / sides
    # the 2 outer angles of the segment are equal so easy to calculate
    outer_angle = (180.0 - centre_angle) / 2
    # convert the outer angle to radians then calculate the outer length with basic trig
    outer_length = 2 * r * (math.cos(outer_angle * math.pi / 180))
    # draw the relevant side lengths, turning by 180 degrees minus the relevant
    # angle each time
    t.fd(r)
    t.lt(180 - outer_angle)
    t.fd(outer_length)
    t.lt(180 - outer_angle)
    t.fd(r)
    t.lt(180)
    
def pie(t,r,sides):
    """ draw a pie with sides number of segments """
    for i in range(sides):
        triangle(t,r,sides)
    
bob = turtle.Turtle()
pie(bob,100,17)
    