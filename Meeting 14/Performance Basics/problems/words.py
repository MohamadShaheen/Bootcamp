dictionary = {}


def naive_search(text: list, word: str) -> int:
    counter = 0

    for token in text:
        if token == word:
            counter += 1

    return counter


def dict_search(text: list, word: str) -> int:
    if not dictionary:
        for token in text:
            if token not in dictionary:
                dictionary[token] = 1
            else:
                dictionary[token] += 1

    return dictionary[word]
