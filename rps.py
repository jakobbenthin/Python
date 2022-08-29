import random

print('###############################################')
print("#######Låt oss spela STEN, SAX, PÅSE! #########")
print('#############Jakethesnake######################')


def print_func(winner, user1, user2, u1_in, u2_in, u1_p, u2_p):
    print('###############################################')
    print(f'{winner} vann omgågnen! {user1} valde {u1_in}, {user2} valde {u2_in}')
    print(f'Ställning, {user1}: {u1_p} - {user2}: {u2_p}')
    print('###############################################')


def play():
    user_point = 0
    computer_point = 0
    user1_name = input('Ange ditt namn: ')
    user2_name = 'Datorn'
    check = False
    turn = 0
    while check != True:

        turn +=1
        print(f'Omgång {turn}')
        user1_in = input("'r', för sten, 'p' för papper, 's' för sax")
        user2_in = random.choice(['r', 'p', 's'])

        if user1_in == 'r' and user2_in == 'p':
            computer_point +=1
            print_func(user2_name, user1_name, user2_name, user1_in, user2_in, user_point, computer_point)
        elif user1_in == 'r' and user2_in == 's':
            user_point +=1
            print_func(user1_name, user1_name, user2_name, user1_in, user2_in, user_point, computer_point)
        elif user1_in == 'p' and user2_in == 's':
            computer_point +=1
            print_func(user2_name, user1_name, user2_name, user1_in, user2_in, user_point, computer_point)
        elif user1_in == 'p' and user2_in == 'r':
            user_point +=1
            print_func(user1_name, user1_name, user2_name, user1_in, user2_in, user_point, computer_point)
        elif user1_in == 's' and user2_in == 'p':
            user_point +=1
            print_func(user1_name, user1_name, user2_name, user1_in, user2_in, user_point, computer_point)
        elif user1_in == 's' and user2_in == 'r':
            computer_point +=1
            print_func(user2_name, user1_name, user2_name, user1_in, user2_in, user_point, computer_point)
        elif user1_in == user2_in:
            print_func('Ingen', user1_name, user2_name, user1_in, user2_in, user_point, computer_point)
        
        if user_point == 3 or computer_point == 3:
            print()
            print(f'Matchen slut!, resultat {user1_name} fick {user_point} -- {user2_name} fick {computer_point}')
            check = True

play()

