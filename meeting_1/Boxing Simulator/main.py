import random


def one_round(boxing_moves, moves_names):
    boxing_move = 0

    while boxing_move not in boxing_moves.keys():
        boxing_move = input('Please enter a boxing move: ')
        while True:
            try:
                boxing_move = int(boxing_move)
                break
            except ValueError:
                print('Please enter valid boxing move: ', end="")
                boxing_move = input()

    random_number = random.randint(1, 6)
    while random_number == boxing_move:
        random_number = random.randint(1, 6)

    print(f'{moves_names[boxing_move]} VS. {moves_names[random_number]}')
    if random_number in boxing_moves[boxing_move]:
        print(f'I beat. {moves_names[boxing_move]} beats {moves_names[random_number]}')
        return True
    else:
        print(f'I lose. {moves_names[random_number]} beats {moves_names[boxing_move]}')
        return False


def main():
    boxing_moves = {
        1: [2, 3, 4, 5],
        2: [3, 4, 5, 6],
        3: [4, 5, 6],
        4: [5, 6],
        5: [6],
        6: [1]
    }

    print('\nLegend:')

    moves_names = {
        1: 'Jab',
        2: 'Cross',
        3: 'Lead Hook',
        4: 'Rear Hook',
        5: 'Lead Uppercut',
        6: 'Rear Uppercut'
    }

    print(f'{moves_names}\n')
    print(f'Every move is followed by a list that describes which moves it beats:\n{boxing_moves}\n')

    # One Round
    one_round(boxing_moves, moves_names)

    print('\nMultiple Rounds\n')
    print('-------------------------------------------------------------------------------------------\n')

    for i in range(10):
        # Print round number
        print(f'round {i + 1}:\n')
        # Simulate single round
        one_round(boxing_moves, moves_names)
        print()

    print('\nChampionship\n')
    print('-------------------------------------------------------------------------------------------\n')
    for i in range(4):
        # Print round number
        print(f'round {i + 1}:\n')
        # Simulate single round and save its results
        result = one_round(boxing_moves, moves_names)
        print()
        if not result:
            # If I lost, then the championship ended
            print('I lost. Championship ended.')
            break

    if result:
        print('I won.')

    print('\nMore Than One Punch\n')
    print('-------------------------------------------------------------------------------------------\n')
    for i in range(4):
        counter = 0
        print(f'round {i + 1}:\n')
        # Every round consists of 3 punches, whoever wins more punches wins the round.
        for _ in range(3):
            result = one_round(boxing_moves, moves_names)
            if result:
                # Add the counter by 1 to signify that I won this round.
                counter += 1

        if counter in [2, 3]:

            print(f'\nThe result is {counter} - {3 - counter}: I won this round.\n')
        else:
            print(f'\nThe result is {counter} - {3 - counter}: I lost this round.\n')


if __name__ == '__main__':
    main()
