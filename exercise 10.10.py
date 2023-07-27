import math
import time

fin = open('words.txt')

# function that does a binary/bisection search of the list
# to find whether or not a word is in it
# precondition is that list is sorted
# arguments are the list to search and the word to search for
# Check the midpoint of the list, and if it doesn't match the search word
# then halve the list and recursively check until it either
# matches or the list is length zero

def in_bisect(bisectlist,findword):
    
    if len(bisectlist) == 0:
# if the list is empty then the search fails - sad times       
        return False
    
    i = len(bisectlist) // 2
    if bisectlist[i] == findword:
# if the mid-point happens to equal the word, then great, we found it!
        return True
    if bisectlist[i] > findword:
# too high - try again with the first half of the list
        print(i, ' too high')
        return in_bisect(bisectlist[:i],findword)
    else:
# too low - try again with the second half of the list
        print(i, ' too low')
        return in_bisect(bisectlist[i+1:],findword)
    
wordlist = []
for wordline in fin:
    word = wordline.strip()
    wordlist.append(word)
    
searchword = 'chinwag'

# do the search with in_bisect and then compare with using the 'in' function
# multiply times by 1000 for clarity
starttime = time.time()
print(in_bisect(wordlist,searchword))
endtime = time.time()
print((endtime-starttime)*1000)

starttime = time.time()
if searchword in wordlist:
    print('true')
else:
    print('false')
endtime = time.time()
print((endtime-starttime)*1000)