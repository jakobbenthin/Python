import random, os, string
from words import words



def check_letter(word, input, tmp_word):
    if(input in word):
        print(word.find(input))
        print(f'{input}, finns i {word}')
    else:
        print(f'{input}, finns inte i {word}')
    

def cls():
    os.system('clear')


def print_wrong(wrong):
    cls()
    if wrong == 1:
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('                 ---')
        print("                |   |")
    elif wrong == 2:
        print('')
        print('               \  |')
        print('                \ |')
        print('                 \|')
        print('                  |')
        print('                  |')
        print('                  |')
        print('                  |')
        print('                 ---')
        print("                |   |")
    elif wrong == 3:
        print('____________________')
        print('               \  |')
        print('                \ |')
        print('                 \|')
        print('                  |')
        print('                  |')
        print('                  |')
        print('                  |')
        print('                 ---')
        print("                |   |")
    elif wrong == 4:
        print('_____________________')
        print(' |             \  |')
        print(' |              \ |')
        print('                 \|')
        print('                  |')
        print('                  |')
        print('                  |')
        print('                  |')
        print('                 ---')
        print("                |   |")
    elif wrong == 5:
        print('_____________________')
        print(' |             \  |')
        print(' |              \ |')
        print(' 0               \|')
        print('                  |')
        print('                  |')
        print('                  |')
        print('                  |')
        print('                 ---')
        print("                |   |")
    elif wrong == 6:
        print('_____________________')
        print(' |             \  |')
        print(' |              \ |')
        print(' 0               \|')
        print(' |                |')
        print('                  |')
        print('                  |')
        print('                  |')
        print('                 ---')
        print("                |   |")
    elif wrong == 7:
        print('_____________________')
        print(' |             \  |')
        print(' |              \ |')
        print(' 0               \|')
        print('-|                |')
        print('                  |')
        print('                  |')
        print('                  |')
        print('                 ---')
        print("                |   |")
    elif wrong == 8:
        print('_____________________')
        print(' |             \  |')
        print(' |              \ |')
        print(' 0               \|')
        print('-|-               |')
        print('                  |')
        print('                  |')
        print('                  |')
        print('                 ---')
        print("                |   |")
    elif wrong == 9:
        print('_____________________')
        print(' |             \  |')
        print(' |              \ |')
        print(' 0               \|')
        print('-|-               |')
        print('/                 |')
        print('                  |')
        print('                  |')
        print('                 ---')
        print("                |   |")
    elif wrong == 10:
        print('_____________________')
        print(' |             \  |')
        print(' |              \ |')
        print(' 0               \|')
        print('-|-               |')
        print('/ \               |')
        print('                  |')
        print('                  |')
        print('                 ---')
        print("                |   |")

def get_random_word(words):
    word = random.choice(words)
    return word


def hangman_game():
    word = get_random_word(words)

    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()



    blanks = []
    for i in  range(0, len(word)):
        blanks.append('-')
    print("\n\n\n\n\n\n\n")
    print(*blanks)
    







#print(len(word))


tmp_word = ''

#check_letter(word, input(), tmp_word)

#print_wrong(8)
hangman_game()
 
