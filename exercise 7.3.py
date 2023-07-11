import math

def estimate_pi():
    k = 0
    sum = 0
    term = 1
    while abs(term) >= 1e-15:
        term = (math.factorial(4 * k) * ((26390 * k) + 1103)) / ((math.factorial(k)**4) * (396**(4 * k)))
        sum += 8**0.5 * term / 9801
        print(1/sum, term)
        k += 1
    return(1/sum)

estimate = estimate_pi()
print(math.pi, ' - ',estimate, ' = ', math.pi-estimate)