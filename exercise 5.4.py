def recurse(n, s):
    """Takes two numbers n and s, and adds the nth triangular number to s.
    Only works if n is a non-negative integer"""
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
        
recurse(3,0)