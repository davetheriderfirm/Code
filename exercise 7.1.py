import math

def mysqrt(a):
    x = a/2
    while True:
        y = (x + a/x) / 2
        if y == x:
            return(y)
        x = y
        
def test_square_root():
    print('a   mysqrt(a)     math.sqrt(a)  diff')
    print('-   ---------     ------------  ----')
    i = 1.0
    while i < 10:
        myval = mysqrt(i)
        mathval = math.sqrt(i)
        print(i, str(myval)[:13].ljust(13), str(mathval)[:13].ljust(13), abs(myval - mathval)) 
        i += 1
        
test_square_root()