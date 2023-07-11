import math

def check_solution(a,b):
    c = 1000 - a - b
    if c == (a**2 + b**2)**0.5:
        print(a, b, c)
        print(a*b*c)
        return True
    return False

for i in range(1,501):
    for j in range(i+1,1000-i):
        if check_solution(i,j):
            break