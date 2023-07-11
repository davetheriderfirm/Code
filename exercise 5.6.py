import turtle

def koch(t,length,angle):
    if length < 3:
        t.fd(length)
    else:
        koch(t,length/3,angle)
        t.lt(angle)
        koch(t,length/3,angle)
        t.rt(2*angle)
        koch(t,length/3,angle)
        t.lt(angle)
        koch(t,length/3,angle)
        
def snowflake(t,length,angle):
    for i in range(3):
        koch(t,length,angle)
        t.rt(angle)
        
bob = turtle.Turtle()
bob.speed(1000)
snowflake(bob,200,85)