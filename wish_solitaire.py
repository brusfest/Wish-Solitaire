from random import *
import pickle

deck = []

for i in range(7, 15):
    deck.append(f'\u2665 {i}')
    deck.append(f'\u2663 {i}')
    deck.append(f'\u2666 {i}')
    deck.append(f'\u2660 {i}')


def distribute(split):
    shuffle(split)
    split = [split[x:x + 4] for x in range(0, len(split), 4)]
    return split


def remove_pair(c1, c2):
    global stacks
    letters = list('ABCDEFGH')
    convert = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    if c1 != c2 and c1 in letters and c2 in letters and stacks[convert[c1]][0][2:] == stacks[convert[c2]][0][2:]:
        stacks[convert[c1]].pop(0)
        stacks[convert[c2]].pop(0)
    else:
        print('Invalid input. Try again.')


def loss(cards):
    copy = []
    for item in cards:
        try:  # throws error if stack is empty
            copy.append(int(item[0][2:]))
        except:
            continue

    copy_check = set(copy)
    if len(copy) == len(copy_check):
        return True


def win(cards):
    if sum([len(x) for x in cards]) == 0:  # if nothing is added, then there's no cards left
        return True


def save(cards):
    pickle.dump(cards, open('save.p', 'wb'))


def load():
    global stacks
    try:
        stacks = pickle.load(open('save.p', 'rb'))
        game(stacks)
    except FileNotFoundError:
        print('No saved state found.')


def game(cards):
    letters = list('ABCDEFGH')
    while True:
        if win(cards):
            print('Congratulations! You won.')
            break
        elif loss(cards):
            print('You lose.')
            break
        else:
            for index, stack in enumerate(cards):
                if len(stack) > 0:
                    print(f'{letters[index]}: {stack[0]} {" "* (len(stack[0])%2)}{"? "* len(stack[1:])}')
                else:
                    print(f'{letters[index]}: ')

            print('\n"save" to save state to file')
            print('"back" to go back to menu')
            user = input('Choose cards you want to remove (e.g. CF): ').upper()
            if user == 'SAVE': save(cards)
            elif user == 'BACK': menu()
            else:
                if len(user) == 2:
                    c1 = user[0]
                    c2 = user[1]
                    remove_pair(c1, c2)
                else: game(cards)


stacks = distribute(deck)


def menu():
    global stacks
    import sys

    menu_list = '''
    ---------------
    1 - new game
    2 - load state
    3 - exit
    ---------------
    '''

    print(menu_list)
    user_choice = input('Choose option: ')
    if user_choice == '1':
        stacks = distribute(deck)
        game(stacks)
    elif user_choice == '2':
        load()
    elif user_choice == '3':
        sys.exit()
    else:
        print('Invalid option.')

    menu()


menu()