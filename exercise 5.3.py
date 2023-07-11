import math

def is_triangle(a,b,c):
    if a > b+c or b > a+c or c > a+b:
        print('No')
        return
    print('Yes')
    
def input_sticks():
    stick1 = input('Stick 1 length?\n')
    stick2 = input('Stick 2 length?\n')
    stick3 = input('Stick 3 length?\n')
    s1 = int(stick1)
    s2 = int(stick2)
    s3 = int(stick3)
    is_triangle(s1,s2,s3)
    
input_sticks()