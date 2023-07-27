import random

def choose_from_hist(t):
    return random.choice(t)

hist = {'a':1, 'b':2}
t = []
for key, value in hist.items():
    for i in range(value):
        t.append(key)

tallyhist = {}
for j in range(1000):
    current_val = choose_from_hist(t)
    tallyhist[current_val] = tallyhist.get(current_val, 0) + 1

print(tallyhist)