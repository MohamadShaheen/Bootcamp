import csv

from users.user import User
from users.admin import Admin


def ask_user_for_numeric_input(input_text: str, error_text: str, lower_bound: int, upper_bound: int):
    while True:
        try:
            number = int(input(input_text))
            if lower_bound > number > upper_bound:
                raise ValueError
            break
        except ValueError:
            print(error_text)


def print_list_numbered(list_to_be_printed: list):
    for i, element in enumerate(list_to_be_printed):
        print(f'{i + 1}: {element}')

def check_if_csv_file_exists(csv_file_location: str):
    try:
        with open(csv_file_location, 'r'):
            csv_file = csv.reader(csv_file_location)
            return csv_file
    except FileNotFoundError:
        print('CSV file with specified location not found')

def main():



if __name__ == '__main__':
    main()
