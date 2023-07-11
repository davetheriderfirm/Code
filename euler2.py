import math

def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return(fib(n-1)+fib(n-2))

total = 0

for i in range(33):
    current_fib = fib(i)
    print(i, fib(i))
    if fib(i)%2 == 0:
        total += current_fib
        
print(total)