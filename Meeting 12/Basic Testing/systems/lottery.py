import random

from testing import test


class Lottery:
    def __init__(self, names: list):
        self.names = names

    def pick_random_name(self) -> str | None:
        selected_name = random.choice(self.names)
        if not test.check_str_type(value=selected_name):
            return None
        return random.choice(self.names)

    def pick_multiple_names(self, num_of_names_to_be_selected: int) -> None | list[str]:
        if not test.check_value_bigger_than_list_len(value=num_of_names_to_be_selected, list_of_values=self.names):
            print(f'The list {self.names} is not big enough to pick {num_of_names_to_be_selected} names from')
            return None
        selected_names = []

        for _ in range(num_of_names_to_be_selected):
            selected_name = self.pick_random_name()
            if selected_name is None:
                continue
            while not test.check_value_in_list(value=selected_name, list_of_values=selected_names):
                selected_name = self.pick_random_name()
            selected_names.append(selected_name)

        return selected_names
