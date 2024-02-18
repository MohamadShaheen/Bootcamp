def main():
    users = [
        ['Mohamad', 'male', 23, 'high tech', 'prison break', 'pizza'],
        ['Lora', 'female', 26, 'doctor', 'la casa de papel', 'salad'],
        ['Peter', 'male', 50, 'professor', 'the black widow', 'pizza'],
        ['naya', 'female', 35, 'nurse', 'love story', 'salad']
    ]

    # Flag to check if a match is found or not
    match_found = False

    # Note that the name isn't important. That is, the user inserted can be a match if all of his
    # attributes are matched but the name

    while not match_found:
        input('Please enter the name: ')

        gender = input('Please enter the gender: ')
        while gender not in ['male', 'female']:
            print('Please enter valid gender: ', end="")
            gender = input()

        minimum_age = input('Please enter the minimum age: ')
        while True:
            try:
                minimum_age = int(minimum_age)
                break
            except ValueError:
                print('Please enter valid minimum age: ', end="")
                minimum_age = input()

        maximum_age = input('Please enter the maximum age: ')
        while True:
            try:
                maximum_age = int(maximum_age)
                break
            except ValueError:
                print('Please enter valid maximum age: ', end="")
                maximum_age = input()

        profession = input('Please enter profession: ')
        favorite_tv_show = input('Please enter favorite tv show: ')
        favorite_food = input('Please enter favorite food: ')

        for user in users:
            if user[1] == gender and minimum_age <= user[2] <= maximum_age and \
                    user[3] == profession and user[4] == favorite_tv_show and user[5] == favorite_food:
                print(f'\nThe user {user[0]} is a PERFECT match')
                match_found = True

        if not match_found:
            print('\nNo match found. Please try inserting another user information.')
            print()


if __name__ == '__main__':
    main()
