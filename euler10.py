from math import sqrt
def primes(n):
    total = 0
    primeslist = [2]
    limit = sqrt(n)
    for i in range (2,n):
        p = 1
        for j in primeslist:
            if j>limit:
                break
            if (i%j) == 0:
                p = 0
        if p == 1:
            primeslist.append(i)
            total += i
    print(total)
    return primeslist

primeslist = primes(20)
print(len(primeslist))