import random

def comp_guess(x):
    low = 1
    high = x
    feedback = '' 
    while feedback != 'C':
        guess = random.randint(low, high)
        #print(f'{low}, {high}')
        feedback = input(f'Är {guess} för högt (H) eller för lågt (L), eller rätt (C)??').upper()

        if feedback == 'L':
            low = guess + 1
        elif feedback == 'H':
            high = guess - 1

    print(f'du tänkte på {guess}')

comp_guess(int(input("ange ett nummer:")))
