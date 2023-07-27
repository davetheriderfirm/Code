def most_frequent(instring):
    
    hist = make_histogram(instring)
    
    t = []
    for x, freq in hist.items():
        t.append((freq, x))
        
    t.sort(reverse=True)
    
    #res = []
    for freq, x in t:
        print(x, freq)
        #res.append(x)
        
    #return res
    
    
def make_histogram(s):
    
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist
    
string = 'The left side is a tuple of variables; the right side is a tuple of expressions. Each value is assigned to its respective variable. All the expressions on the right side are evaluated before any of the assignments.'
letter_seq = most_frequent(string.lower())
