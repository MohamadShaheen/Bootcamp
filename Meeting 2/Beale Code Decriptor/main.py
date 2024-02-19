import string


class Cipher:
    def __init__(self, text, cypher):
        self.text = text
        self.cypher = cypher
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.cypher):
            raise StopIteration
        letter = self.text[self.cypher[self.index]][0]
        self.index += 1
        return letter


def key(message, text):
    current = 0
    message_index = 0
    while message_index != len(message):
        if text[current][0] == message[message_index]:
            yield current
            text[current] = '!'
            current = 0
            message_index += 1
        current += 1


def main():
    with open('declaration_of_independence.txt', 'r') as file:
        dec_of_ind = file.read()

    # Remove all new lines
    dec_of_ind = dec_of_ind.replace('\n', ' ')
    # Remove all punctuation marks
    dec_of_ind = dec_of_ind.translate(str.maketrans('', '', string.punctuation))
    # Get the words as tokens
    words = dec_of_ind.split()
    # Delete all the words after 'and our sacred honor'
    words = words[:words.index('honor') + 1]
    cypher = [4, 93, 52, 12, 41, 23, 9, 1, 34, 2, 11, 111, 6, 13, 24, 99, 100, 30, 10,
              26, 16, 29, 155, 32, 37, 61, 15, 42, 3, 633, 27, 70, 77, 45, 55, 43, 35,
              108, 103, 56, 159, 166, 7, 8, 174, 36]

    # Get the ciphered text
    ciphered_text = Cipher(words, cypher)

    # Print the ciphered text and save it in a variable
    result = ''
    for ciphered_letter in ciphered_text:
        result += ciphered_letter
        print(ciphered_letter, end='')

    print()

    # Get the keys based on the given message and text
    keys = key(result, words.copy())

    # Save the keys to a list
    keys_list = []
    for key_part in keys:
        keys_list.append(key_part)

    print(keys_list)


if __name__ == '__main__':
    main()
