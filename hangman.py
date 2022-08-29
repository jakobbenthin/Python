import random, os
from words import words



def check_letter(word, input, tmp_word):
    if(input in word):
        print(word.find(input))
        print(f'{input}, finns i {word}')
    else:
        print(f'{input}, finns inte i {word}')
    







print(words)
word = random.choice(words)



print(word)

#print(len(word))
blanks = []
for i in  range(0, len(word)):
    blanks.append('_')
    
print(*blanks, sep = " ")


print(blanks[3])

tmp_word = ''

check_letter(word, input())

 
