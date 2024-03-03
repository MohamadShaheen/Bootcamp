import testing
import random


def main():
    for _ in range(10):
        first_number = random.randint(50, 100)
        second_number = random.randint(1, 49)
        print(f'First number: {first_number}\nSecond number: {second_number}\n')

        testing.bigger(first_number, second_number)

    print('#########################################################################################\n')
    print('First number is bigger than Second number - Pass\n')
    print('#########################################################################################\n')

    for _ in range(10):
        first_number = random.randint(1, 49)
        second_number = random.randint(50, 100)
        print(f'First number: {first_number}\nSecond number: {second_number}\n')

        testing.smaller(first_number, second_number)

    print('#########################################################################################\n')
    print('First number is smaller than Second number - Pass\n')
    print('#########################################################################################\n')

    for _ in range(10):
        first_number = random.randint(1, 49)
        second_number = first_number
        print(f'First number: {first_number}\nSecond number: {second_number}\n')

        testing.equals(first_number, second_number)

    print('#########################################################################################\n')
    print('First number equals Second number - Pass\n')
    print('#########################################################################################\n')

    numbers = [i for i in range(100)]

    print(numbers, '\n')

    for _ in range(10):
        number = random.randint(0, 99)
        print(f'Number: {number}\n')

        testing.value_in_list(number, numbers)

    print('#########################################################################################\n')
    print('All numbers are in the list - Pass\n')
    print('#########################################################################################\n')

    list_of_numbers_list = [[i for i in range(j, j + 10)] for j in range(0, 100, 10)]

    print(list_of_numbers_list, '\n')

    for _ in range(10):
        number = random.randint(0, 99)
        print(f'Number: {number}\n')

        testing.value_in_list_of_lists(number, list_of_numbers_list)

    print('#########################################################################################\n')
    print('All numbers are in the list of lists - Pass\n')
    print('#########################################################################################\n')

    dict = {}
    counter = 0
    for i in range(10):
        dict[i] = [j for j in range(counter, counter + 10)]
        counter += 10

    print(dict, '\n')

    for _ in range(10):
        key = random.randint(0, 9)
        print(f'Key: {key}\n')

        testing.key_in_dict_keys(key, dict)

    print('#########################################################################################\n')
    print('All keys are in the dictionary - Pass\n')
    print('#########################################################################################\n')

    print(dict, '\n')

    for _ in range(10):
        value = random.randint(0, 99)
        print(f'Value: {value}\n')

        testing.value_in_dict_values_of_lists(key, dict)

    print('#########################################################################################\n')
    print('All values are in the dictionary - Pass\n')
    print('#########################################################################################\n')

    print('We can test other functions but it will be ugly so we will refrain from this. '
          'It will work but we have to design dictionaries that are not the best looking.')

if __name__ == '__main__':
    main()
