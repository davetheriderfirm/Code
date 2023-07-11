import math

def get_abcn():
    a_in = input('give me an a\n')
    a = int(a_in)
    b_in = input('give me an b\n')
    b = int(b_in)
    c_in = input('give me an c\n')
    c = int(c_in)
    n_in = input('give me an n\n')
    n = int(n_in)
    check_fermat(a,b,c,n)
    
def check_fermat(a,b,c,n):
    if (a**n + b**n == c**n) and n > 2:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work.")
        
get_abcn()