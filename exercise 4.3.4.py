import turtle
import math


def polygon(t,length,n):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        
def circle(t,r):
    length = (2 * math.pi * r) / 100
    polygon(t,length,100)
        
bob = turtle.Turtle()
circle(bob,50)