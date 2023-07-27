import math

fin = open('words.txt')

''' see if the dictionary already has this index
    if it does not, add a tuple of the current word to the dictionary for this index
    if it does, add the current word to the existing tuple''' 
def check_dict(checkindex):
    if checkindex == None:
        anagramdict[wordsort] = (wordline,)
        return
    anagramdict[wordsort] = anagramdict[wordsort] + (wordline,)
    
def word_distance(word1, word2):
    
    assert len(word1) == len(word2)
    
    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1
            
    return count

anagramdict = {}

''' sort the letters and use the result as an index for a dictionary. The dictionary values for
    each index will be a list of all the words that are the same when sorted'''
for line in fin:
    wordline = line.strip()
    wordsort = ''.join(sorted(wordline))
    check_dict(anagramdict.get(wordsort))

anagram_list = []
'''read the dictionary and see which keys have more than one value'''
'''if more than one value, add the value tuple to a list'''
for key in anagramdict:
    #if len(key) == 8:
    val_len = len(anagramdict[key])
    if val_len > 1:
        anagram_list.insert(val_len, anagramdict[key])
        
anagram_sorted = sorted(anagram_list,key=len, reverse=True)
#for line in anagram_sorted:
#    if len(line) > 5:
#        print(line)
        
for anagrams in anagramdict.values():
    for word1 in anagrams:
        for word2 in anagrams:
            if word1 < word2 and word_distance(word1, word2) == 2:
                print(word1, word2)
    
        