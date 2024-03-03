from assertpy import assert_that


def bigger(tested_value, value_to_compare_to):
    assert_that(tested_value).is_greater_than(value_to_compare_to)

    return True


def smaller(tested_value, value_to_compare_to):
    assert_that(tested_value).is_less_than(value_to_compare_to)

    return True


def equals(tested_value, value_to_compare_to):
    assert_that(tested_value).is_equal_to(value_to_compare_to)

    return True


def value_in_list(tested_value, value_to_compare_to):
    assert tested_value in value_to_compare_to, "tested_value must be in the list"

    return True


def value_in_list_of_lists(tested_value, value_to_compare_to):
    for list in value_to_compare_to:
        if tested_value in list:
            return True

    assert 0 > 1, "tested_value is not in the list"


def key_in_dict_keys(tested_value, value_to_compare_to):
    assert tested_value in value_to_compare_to.keys(), "key must be in dictionary"

    return True


def key_in_dict_keys_of_lists(tested_value, value_to_compare_to):
    for keys in value_to_compare_to.keys():
        if tested_value in keys:
            return True

    assert 0 > 1, "tested_value is not in the dictionary"


def key_in_dict_of_dicts(tested_value, value_to_compare_to):
    for dict in value_to_compare_to:
        if tested_value in dict.keys():
            return True

    assert 0 > 1, "tested_value is not in the dictionary"


def value_in_dict_values(tested_value, value_to_compare_to):
    assert tested_value in value_to_compare_to.values(), "value must be in dictionary"

    return True


def value_in_dict_values_of_lists(tested_value, value_to_compare_to):
    for values in value_to_compare_to.values():
        if tested_value in values:
            return True

    return False


def value_in_dict_of_dicts(tested_value, value_to_compare_to):
    for dict in value_to_compare_to:
        if tested_value in dict.values():
            return True

    return False