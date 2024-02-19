def general_prime_founder(n):
    main_number_list = list(range(4, n + 1))
    prime_numbers_list = [2, 3]

    # Remove all numbers divisible by 2 or 3
    main_number_list = [number for number in main_number_list if number % 2 != 0 and number % 3 != 0]

    for number in main_number_list:
        # Create a flag to represent if the current number is prime or not
        is_prime = True
        for prime in prime_numbers_list:
            if number % prime == 0:
                is_prime = False
                break

        if is_prime:
            # Add the new prime number to the prime number list
            prime_numbers_list.append(number)
            # Remove all numbers divisible by the new prime number
            main_number_list = [item for item in main_number_list if item % number != 0]

    print(f'There are {len(prime_numbers_list)} prime numbers found.')
    print(f'Primes: {prime_numbers_list}')


def main():
    # main_number_list = list(range(4, 151))
    # prime_numbers_list = [2, 3]
    #
    # # Remove all numbers divisible by 2 or 3
    # main_number_list = [number for number in main_number_list if number % 2 != 0 and number % 3 != 0]
    #
    # for number in main_number_list:
    #     # Create a flag to represent if the current number is prime or not
    #     is_prime = True
    #     for prime in prime_numbers_list:
    #         if number % prime == 0:
    #             is_prime = False
    #             break
    #
    #     if is_prime:
    #         # Add the new prime number to the prime number list
    #         prime_numbers_list.append(number)
    #         # Remove all numbers divisible by the new prime number
    #         main_number_list = [item for item in main_number_list if item % number != 0]
    #
    # print(f'There are {len(prime_numbers_list)} prime numbers found.')
    # print(f'Primes: {prime_numbers_list}')

    general_prime_founder(150)


if __name__ == '__main__':
    main()
