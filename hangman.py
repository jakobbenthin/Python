import random, os, string
from words import words



def check_letter(word, input, tmp_word):
    if(input in word):
        print(word.find(input))
        print(f'{input}, finns i {word}')
    else:
        print(f'{input}, finns inte i {word}')
    

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_wrong(wrong):
    
    if wrong == 0:
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
    elif wrong == 1:
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
    x = 0
    word = get_random_word(words)
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    

    while len(word_letters) > 0:
        cls()
        print_wrong(x)
        print('You have used these letters: \n', ' '.join(used_letters))
        
        #överkurs,,, show word and guess
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: \n', ' '.join(word_list))

        user_letter = input('Guess a letter:').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                x += 1
                if x == 10:
                    cls()
                    print_wrong(x)
                    print(f'You died, right answer: {word}')
                    return False
        elif user_letter in used_letters:
            print('You have already used this character...')

        else:
            print('Invalid character...')

    print(f'Correct word!! \n{word}')
    return True

    # when len(world_letters) == 0






    #blanks = []
    #for i in  range(0, len(word)):
    #    blanks.append('-')
    #print("\n\n\n\n\n\n\n")
    #print(*blanks)
    







#print(len(word))


tmp_word = ''

#check_letter(word, input(), tmp_word)

#print_wrong(8)
if hangman_game() == True:
    print('You won!')
else:
    print('You lose...')
 
