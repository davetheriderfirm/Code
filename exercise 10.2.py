def cumsum(sumlist):
    newlist = []
    for i in range(len(sumlist)):
        newlist.append(sum(sumlist[:i+1]))
    return newlist

t = [1,2,3]
print(cumsum(t))