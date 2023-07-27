import math
import time

fin = open('words.txt')

# use in_bisect (comments for that are in exercise 10.10)

def in_bisect(bisectlist,findword):
    
    if len(bisectlist) == 0:     
        return False
    
    i = len(bisectlist) // 2
    if bisectlist[i] == findword:
        return True
    if bisectlist[i] > findword:
        return in_bisect(bisectlist[:i],findword)
    else:
        return in_bisect(bisectlist[i+1:],findword)
    
wordlist = []
for wordline in fin:
    word = wordline.strip()
    wordlist.append(word)
    
for word in wordlist:
    if in_bisect(wordlist,word[::-1]):
        print(word, word[::-1])

