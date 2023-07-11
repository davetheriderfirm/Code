import math

def find_factor(n):
    i = 2
    if n == 1:
        return
    while i <= n:
        if i == n:
            print(n)
            return
        if n % i == 0:
            print(i)
            find_factor(n/i)
            return
        i +=1
        
    
            
find_factor(600851475143)