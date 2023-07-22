import math

def is_palindrome(word):
    return word[::-1] == word    

for odom in range (0,999996):
    odomstr0 = str(odom).zfill(6)[2:6]
    odomstr1 = str(odom + 1).zfill(6)[1:6]
    odomstr2 = str(odom + 2).zfill(6)[1:5]
    odomstr3 = str(odom + 3).zfill(6)            
    
    if odom == 198888:
        print('debug')
    if 0 < odom:
        if is_palindrome(odomstr0) and is_palindrome(odomstr1) and is_palindrome(odomstr2) and is_palindrome(odomstr3):
            print(odom)

print('finished')
                