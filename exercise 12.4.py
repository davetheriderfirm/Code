import math

fin = open('words.txt')

def build_worddict():
    for line in fin:
        wordline = line.strip()
        worddict[wordline] = True

def is_reducible(inword):
    '''Base case - empty string is reducible'''
    if len(inword) == 0:
        return True
        '''Maybe we already checked this word's reducibility as a child of a previous
        word - if so then we are done'''
    if inword in reducdict:
        return True
        '''Try removing every letter in turn and see if the resulting child word
        is reducible.
        Note - we only need to find a single reducible child so we can return True and
        stop checking at the first success'''
    for i in range(len(inword)):
        childword = inword[:i]+inword[i+1:]
        '''Check whether we already know that this child word is reducible'''
        if childword in reducdict:
            return True
        '''Check whether this child word is a valid word'''
        if childword in worddict:
            '''Check whether this child word is reducible. If it is, then add it
            to the reducible dictionary (we know that it isn't in there yet
            because we already checked)'''
            if is_reducible(childword):
                reducdict[childword] = True
                return True
            '''Child word was either not a word or not reducible, so continue
            round the loop and try the next child word'''
            
    return False
    '''No reducible child words exist so the parent word is not reducible'''

worddict  = {}
reducdict = {}

'''build a dictionary of valid words from the text file to allow faster searching'''
build_worddict()

'''We have read through the whole file to build the word dictionary, but now we need to
read through it again to check reducibility, so open the file again'''
fin = open('words.txt')

maxlength = 0

for line in fin:
    wordline = line.strip()
    if is_reducible(wordline):
        '''if the word is reducible then add it to the reducible dictionary'''
        if wordline not in reducdict:
            reducdict[wordline] = True
        #print(wordline)
        '''If this is the longest reducible word yet, then print it out'''
        if len(wordline) >= maxlength:
            maxlength = len(wordline)
            maxword = wordline
            print(maxword,maxlength)
            
#print(maxword, maxlength)