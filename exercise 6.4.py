def is_power(a,b):
    if a == 0:
        return False
    if a == b:
        return True
    if a % b == 0:
        return is_power(a/b,b)
    return False

print(is_power(2,4))