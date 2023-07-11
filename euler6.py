def sumsq(n):
    total = 0
    for i in range(n+1):
        total += i**2
    return total

def sqsum(n):
    total = 0
    for i in range(n+1):
        total += i
    return total**2

a = 100
print(sqsum(a)-sumsq(a))