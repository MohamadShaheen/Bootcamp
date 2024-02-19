def main():
    # Define the available conversion types
    conversion_types = ['F -> C', 'C -> F',
                        'MPH -> KPH', 'KPH -> MPH',
                        'kg -> stone', 'stone -> kg',
                        'kg -> lbs', 'lbs -> kg',
                        'stone -> lbs', 'lbs -> stone']

    # Ask the user to input a specific conversion type
    print('\nPlease enter one of the following conversion types:')
    print(conversion_types)
    type_of_conversion = input('Please enter the type of conversion you would like to implement: ')

    # Make sure the conversion type is on of the available types
    while type_of_conversion not in conversion_types:
        print('You entered invalid conversion type. Please enter one of the provided above: ', end="")
        type_of_conversion = input()

    if type_of_conversion == 'F -> C':
        while True:
            try:
                source_value = float(input('Please enter the temperature in Fahrenheit: '))
                break
            except ValueError:
                print('Please enter a valid value.')
        converted_value = (5 / 9) * (source_value - 32)
        print(f'Temperature in Celsius: {converted_value}')

    elif type_of_conversion == 'C -> F':
        while True:
            try:
                source_value = float(input('Please enter the temperature in Celsius: '))
                break
            except ValueError:
                print('Please enter a valid value.')
        converted_value = source_value * (9 / 5) + 32
        print(f'Temperature in Fahrenheit: {converted_value}')

    elif type_of_conversion == 'MPH -> KPH':
        while True:
            try:
                source_value = float(input('Please enter the speed in MPH: '))
                break
            except ValueError:
                print('Please enter a valid value.')
        converted_value = source_value / 1.60934
        print(f'Speed in KPH: {converted_value}')

    elif type_of_conversion == 'KPH -> MPH':
        while True:
            try:
                source_value = float(input('Please enter the speed in KPH: '))
                break
            except ValueError:
                print('Please enter a valid value.')
        converted_value = source_value * 1.60934
        print(f'Speed in MPH: {converted_value}')

    elif type_of_conversion == 'kg -> stone':
        while True:
            try:
                source_value = float(input('Please enter the weight in kg: '))
                break
            except ValueError:
                print('Please enter a valid value.')
        converted_value = source_value / 6.35029318
        print(f'Weight in stone: {converted_value}')

    elif type_of_conversion == 'stone -> kg':
        while True:
            try:
                source_value = float(input('Please enter the weight in stone: '))
                break
            except ValueError:
                print('Please enter a valid value.')
        converted_value = source_value * 6.35029318
        print(f'Weight in kg: {converted_value}')

    elif type_of_conversion == 'kg -> lbs':
        while True:
            try:
                source_value = float(input('Please enter the weight in kg: '))
                break
            except ValueError:
                print('Please enter a valid value.')
        converted_value = source_value * 2.20462
        print(f'Weight in lbs: {converted_value}')

    elif type_of_conversion == 'lbs -> kg':
        while True:
            try:
                source_value = float(input('Please enter the weight in lbs: '))
                break
            except ValueError:
                print('Please enter a valid value.')
        converted_value = source_value / 2.20462
        print(f'Weight in kg: {converted_value}')

    elif type_of_conversion == 'stone -> lbs':
        while True:
            try:
                source_value = float(input('Please enter the weight in stone: '))
                break
            except ValueError:
                print('Please enter a valid value.')
        converted_value = source_value * 14
        print(f'Weight in lbs: {converted_value}')

    elif type_of_conversion == 'lbs -> stone':
        while True:
            try:
                source_value = float(input('Please enter the weight in lbs: '))
                break
            except ValueError:
                print('Please enter a valid value.')
        converted_value = source_value / 14
        print(f'Weight in stone: {converted_value}')


if __name__ == '__main__':
    main()
