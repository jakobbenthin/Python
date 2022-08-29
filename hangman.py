from itertools import count
import random
from words import words

print(words)

word = random.choice(words)

print(word)

print(len(word))
blanks = []
for i in  range(0, len(word)):
    blanks.append('_')
    
print(*blanks, sep = " ")


print(blanks[3])


 
