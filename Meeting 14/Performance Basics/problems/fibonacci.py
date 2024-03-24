def recursive_fibonacci(index: int) -> int:
    if index <= 1:
        return index
    else:
        return recursive_fibonacci(index - 1) + recursive_fibonacci(index - 2)


def list_memorization_fibonacci(index: int) -> int:
    if index == 0 or index == 1:
        return index
    fibonacci_list = [0, 1]
    for i in range(2, index + 1):
        fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])

    return fibonacci_list[index]
