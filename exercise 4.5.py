import turtle
import math

def arch_spiral(t,n,length,a,b):
    theta = 0
    for i in range(n):
        t.fd(length)
        angle = 