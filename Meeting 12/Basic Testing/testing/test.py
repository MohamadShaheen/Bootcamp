import os


def check_str_type(value) -> bool:
    if not isinstance(value, str):
        print(f'The value {value} is not a string')
        return False

    return True


def check_list_is_strs(list_of_values: list) -> bool:
    for value in list_of_values:
        if not check_str_type(value):
            print(f'The value {value} is not a string')
            return False

    return True


def check_value_in_list(value, list_of_values) -> bool:
    if value in list_of_values:
        print(f'The value {value} is already the list {list_of_values}')
        return False

    return True


def check_existed_file(file_location):
    if not os.path.exists(file_location):
        raise FileNotFoundError(f'The file {file_location} does not exist')


def check_key_in_dictionary(key, dictionary: dict):
    if key not in dictionary.keys():
        print(f'The key {key} does not exist in the dictionary')
        return False

    return True


def check_value_bigger_than_list_len(value, list_of_values: list) -> bool:
    if value >= len(list_of_values):
        print(f'The value {value} is bigger than the list length')
        return False

    return True
