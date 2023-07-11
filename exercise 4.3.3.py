import turtle

def polygon(t,length,n):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        
bob = turtle.Turtle()
polygon(bob,40,13)