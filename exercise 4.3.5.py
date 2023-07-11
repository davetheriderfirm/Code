import turtle
import math


def polygon(t,length,n,angle):
    turn = 360/n
    for i in range(int(n*angle/360)):
        t.fd(length)
        t.lt(turn)
        
def arc(t,r,angle):
    length = (2 * math.pi * r) / 100
    polygon(t,length,100,angle)
        
bob = turtle.Turtle()
arc(bob,95,270)