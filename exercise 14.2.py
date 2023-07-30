import anagram_sets
import dbm
import pickle
import shelve

def store_anagrams(filename, anag_map):
    shelf = shelve.open(filename, 'c')
    for key, value in anagram_map.items():
        shelf[key] = value

    shelf.close()

def read_anagrams(filename, inword):
    shelf = shelve.open(filename)
    sig = anagram_sets.signature(inword)
    try:
        return shelf[sig]
    except KeyError:
        return (inword + ' is not in the wordlist.')
        
#db = dbm.open('myanagrams', 'c')
#anagram_map = anagram_sets.all_anagrams('words.txt')
#store_anagrams('myanagrams.db', anagram_map)

print(read_anagrams('myanagrams.db', 'xraral'))
