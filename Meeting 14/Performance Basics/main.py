import random
from typing import Any
import matplotlib.pyplot as plt
from problems import fibonacci
from problems import search
from problems import words
import numpy as np


def measure_time(function, *values: Any) -> Any | float:
    import time
    start_time = time.perf_counter()
    result = function(*values)
    end_time = time.perf_counter()
    total_time = end_time - start_time

    return result, total_time


def test_fibonacci():
    values = list(range(5, 32, 3))
    times_recursive_fibonacci = []
    times_list_memorization_fibonacci = []

    with open('results/fibonacci/fibonacci.txt', 'w') as file:
        file.write('The fibonacci series results using recursion\n\n')
        for i in values:
            result, time_taken = measure_time(fibonacci.recursive_fibonacci, i)
            file.write(f'Number at place [{i}] is {result}. Time taken to find it is {time_taken}.\n')
            times_recursive_fibonacci.append(time_taken)

        file.write('\nThe fibonacci series results using list for memorization\n\n')
        for i in values:
            result, time_taken = measure_time(fibonacci.list_memorization_fibonacci, i)
            file.write(f'Number at place [{i}] is {result}. Time taken to find it is {time_taken}.\n')
            times_list_memorization_fibonacci.append(time_taken)

        plt.plot(values, times_recursive_fibonacci, label='Recursive Fibonacci', marker='o')
        plt.plot(values, times_list_memorization_fibonacci, label='Memorization Fibonacci', marker='o')
        plt.xlabel('Input Value')
        plt.ylabel('Time (seconds)')
        plt.title('Time taken by Fibonacci functions')
        plt.legend()
        plt.savefig('results/fibonacci/fibonacci.png')
        plt.show()


def test_search():
    list_of_numbers = [i for i in range(10000)]
    values = [list_of_numbers[i] for i in range(0, len(list_of_numbers), 1000)]
    times_linear_search = []
    times_binary_search = []

    with open('results/search/search.txt', 'w') as file:
        file.write('The search results using linear search\n\n')
        for value in values:
            result, time_taken = measure_time(search.linear_search, list_of_numbers, value)
            file.write(f'Number {value} found at [{result}]. Time taken to find it is {time_taken}.\n')
            times_linear_search.append(time_taken)

        file.write('\nThe search results using binary search\n\n')
        for value in values:
            result, time_taken = measure_time(search.binary_search, list_of_numbers, value)
            file.write(f'Number {value} found at [{result}]. Time taken to find it is {time_taken}.\n')
            times_binary_search.append(time_taken)

        plt.plot(values, times_linear_search, label='Linear Search', marker='o')
        plt.plot(values, times_binary_search, label='Binary Search', marker='o')
        plt.xlabel('Numbers')
        plt.ylabel('Time (seconds)')
        plt.title('Time taken by search functions')
        plt.legend()
        plt.savefig('results/search/search.png')
        plt.show()


def test_words():
    with open('data/text.txt', 'r') as file:
        text = file.read()

    text = text.split()
    values = random.sample(text, 10)
    times_naive_search = []
    times_dict_search = []

    with open('results/words/words.txt', 'w') as file:
        file.write('The search results using naive search\n\n')
        for value in values:
            result, time_taken = measure_time(words.naive_search, text, value)
            file.write(f'Word [{value}] appeared {result} times in the text. Time taken to find it is {time_taken}.\n')
            times_naive_search.append(time_taken)

        file.write('\nThe search results using dictionary search\n\n')
        for value in values:
            result, time_taken = measure_time(words.dict_search, text, value)
            file.write(f'Word [{value}] appeared {result} times in the text. Time taken to find it is {time_taken}.\n')
            times_dict_search.append(time_taken)

        plt.plot(values, times_naive_search, label='Naive Approach', marker='o')
        plt.plot(values, times_dict_search, label='Dictionary Approach', marker='o')
        plt.xlabel('Words')
        plt.ylabel('Time (seconds)')
        plt.title('Time taken by word search functions')
        plt.xticks(range(len(values)), values, rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.savefig('results/words/words.png')
        plt.show()


def main():
    test_fibonacci()
    test_search()
    test_words()


if __name__ == "__main__":
    main()
