def in_range(x,y,z):
    """ check if x is in the range y-z where y <= z """
    return x >= y and x <= z

print(in_range(-4.2,-5,-3))