import math

def check_palindrome(n):
    """ convert n to a string and then check if it is the same in reverse."""
    n_char = str(n)
    if n_char == n_char[::-1]:
        return True
    return False

highpal = 0
for i in range(999,1,-1):
    for j in range(999,i,-1):
        if check_palindrome(i*j):
            if i*j > highpal:
                print(i,'*',j,'=',i*j)
                highpal = i*j