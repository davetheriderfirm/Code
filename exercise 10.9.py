import math
import time

fin = open('words.txt')

starttime = time.time()
wordlist = []
for wordline in fin:
    word = wordline.strip()
    wordlist.append(word)
    
endtime = time.time()
print("Execution time is :",(starttime - endtime)*10000000)

starttime = time.time()
wordlist2 = []
for wordline2 in fin:
    word2 = wordline2.strip()
    wordlist2 = wordlist2 + [word2]
    
endtime = time.time()
print("Execution time is :",(starttime - endtime)*10000000)