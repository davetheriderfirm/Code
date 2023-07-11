def gcd(a,b):
    if b == 0:
        return a
    return(gcd(b, a%b))
           
print(gcd((5**6 * 3**4 * 2**11),(5**4 * 3**7 * 2**2)))