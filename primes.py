a = 2000000
marked = [0] * a
value = 3
s = 2
while value < a:
    if marked[value] == 0:
        s += value
        i = value
        while i < a:
            marked[i] = 1
            i += value
    value += 2
print(s)