def main():
    # Define plants and their preferences
    plants = [
        ['Monstera', 'sun', '1', 'not wind'],
        ['Calathea', 'rain', '20', 'wind'],
        ['Dracaena', 'sun', '5', 'not wind']
    ]

    # Ask the user to input a weather
    weather = input('Please enter the weather (sun or rain): ')
    while weather not in ['sun', 'rain']:
        print('Please enter valid weather (sun or rain): ', end="")
        weather = input()

    # Ask the user to input water precipitation
    water_precipitation = input('Please enter the water precipitation (integer number): ')
    while True:
        try:
            int(water_precipitation)
            break
        except ValueError:
            print('Please enter valid water precipitation (integer number): ', end="")
        water_precipitation = input()

    # Ask the user to enter wind condition
    wind = input('Please enter the weather (wind or not wind): ')
    while wind not in ['wind', 'not wind']:
        print('Please enter valid input (wind or not wind): ', end="")
        wind = input()

    print()
    for plant in plants:
        if plant[1] == weather:
            print(f'{plant[0]} likes {weather}')

    print()
    for plant in plants:
        if plant[2] == water_precipitation:
            print(f'{plant[0]} likes {water_precipitation} liters of water')

    print()
    for plant in plants:
        if plant[3] == wind:
            if wind == 'not wind':
                print(f'{plant[0]} doesn\'t like wind')
            else:
                print(f'{plant[0]} likes {wind}')

    plants[0].append(3)
    plants[1].append(24)
    plants[2].append(7)

    # Ask the user to input snow value
    snow_value = input('\nPlease enter the snow value (integer number): ')
    while True:
        try:
            snow_value = int(snow_value)
            break
        except ValueError:
            print('Please enter valid snow value (integer number): ', end="")
        snow_value = input()

    print()
    for plant in plants:
        if plant[4] <= snow_value:
            print(f'{plant[0]} will die because of the snow value')


if __name__ == '__main__':
    main()