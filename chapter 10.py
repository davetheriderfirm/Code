def nested_sum(nestlist):
    total = 0
    for elmnt in nestlist:
        total += sum(elmnt)
    return(total)

t =  [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))