def linear_search(list_of_numbers: list, number: int) -> int:
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] == number:
            return i

    return -1


def binary_search(list_of_numbers: list, number: int) -> int:
    left = 0
    right = len(list_of_numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if list_of_numbers[mid] == number:
            return mid
        elif list_of_numbers[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1
