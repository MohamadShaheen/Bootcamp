import json
from testing import test
from systems.lottery import Lottery


def load_json_file(file_location: str) -> dict:
    test.check_existed_file(file_location=file_location)
    with open(file_location) as file:
        return json.load(file)


def get_list_by_key(key: str, dictionary: dict) -> list:
    test.check_key_in_dictionary(key=key, dictionary=dictionary)
    return dictionary[key]


def main():
    data = load_json_file('data/names.json')
    names = get_list_by_key(key='names', dictionary=data)

    if not test.check_list_is_strs(list_of_values=names):
        return

    lottery = Lottery(names=names)

    selected_name = lottery.pick_random_name()
    if selected_name is not None:
        print(selected_name)

    selected_names = lottery.pick_multiple_names(num_of_names_to_be_selected=10)
    if selected_names is not None:
        print(selected_names)


if __name__ == '__main__':
    main()
