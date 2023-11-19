def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

def capitalise_all(t):
    return [s.capitalize() for s in t]

def only_upper(t):
    return [s for s in t if s.isupper()]

def get_squares(n):
    return (x**2 for x in range(n))

def uses_all(word, letters):
    return all(letter in word for letter in letters)

def avoids(word, forbidden):
    return len(set(word) - set(forbidden)) == len(set(word))

#print(capitalise_all(['sausages', 'pancakes', 'yousuck']))
#print(only_upper(['Table', 'TWAT', 'undercarriage']))

#for val in get_squares(13):
#    print(val)

#print(uses_all('sausages', 'sage'))
#print(uses_all('sausages', 'stag'))

print(avoids('sausages', 'riot'))
print(avoids('sausages', 'riet'))
print(set('sausages') - set('riet'))