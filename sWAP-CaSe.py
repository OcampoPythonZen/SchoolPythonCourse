_string = 'HackerRank.com presents "Pythonist 2"'
newString = []
for word in _string:
    if word == word.upper():
        newString.append(word.lower())
    elif word == word.lower():
        newString.append(word.upper())
print('before:', _string)
print('after:', ''.join(newString))

secString = 'this is a string'
print(secString.replace(' ', '-'))

ts = 'abracadabra'
print(len(ts))

def mutable(string, position, char):
    l = list(string)
    l[position] = char
    string = ''.join(l)
    return string

print(mutable(ts, 5, 'k'))

l = list(ts)
print(l, l[5])

