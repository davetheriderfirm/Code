import math
import time

# use smallwords for debug purposes 

fin = open('words.txt')
#fin = open('smallwords.txt')


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
    
def interlock_general(wordlist,word,nnn):
    for i in range(nnn):
        inter = word[i::nnn]
        if not in_bisect(wordlist,inter):
            return False
    return True
    
wordlist = []
for wordline in fin:
    word = wordline.strip()
    wordlist.append(word)
    
nnn = 5    
    
for word in wordlist:
    wordprint = word
    if interlock_general(wordlist, word, nnn):
        for i in range(nnn):
            wordprint += ' '
            wordprint += word[i::nnn]
        print(wordprint)
        

