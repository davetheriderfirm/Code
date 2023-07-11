import math

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

k = 0
p = 1
while k < 10001:
    p += 1
    if isPrime(p):
        k += 1
#        print(k," ",p)

print(p)