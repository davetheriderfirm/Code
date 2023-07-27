def chop(inlist):
    listlen = len(inlist)
    del inlist[listlen - 1]
    del inlist[0]

t = [1,2,3,4]
print(chop(t))
print(t)