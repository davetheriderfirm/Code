import math
import random

"""Birthday paradox - generates random sets of 23 birthdays (actually days numbered 1 to 366)"""
"""Displays what percentage of sets have at least one duplicate"""
"""input variable 'sample' controls how many sets to generate"""

"""create set of setsize birthdays"""
def birthday_list(dayarray,setsize):
    for j in range(setsize):
        dayarray.append(random.randint(1,365))
    dayarray.sort()

def has_duplicates(inlist):
    t = list(inlist)
    t.sort()    
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False 

def birthday_paradox(samplesize):
    match = 0    
    for i in range(samplesize):
        t = []
        birthday_list(t,setsize)
        if has_duplicates(t):
            match += 1       
    print(match, ' matches')
    print(100*match/samplesize, '%')
    
setsize = 23
sample = 10000
birthday_paradox(sample)
            
            