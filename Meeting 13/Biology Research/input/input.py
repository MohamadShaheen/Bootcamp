import random
import time

failure_probability = 0  # Initial failure probability


def raise_random_exception_with_probability():
    global failure_probability
    while True:
        try:
            if random.random() < failure_probability:
                failure_probability = 0
                # Raise a random exception
                random_exception = random.choice([
                    FileNotFoundError,
                    PermissionError,
                    IsADirectoryError,
                    FileExistsError,
                    NotADirectoryError,
                    IOError
                ])
                raise random_exception("Random exception raised")
            else:
                if failure_probability < 1.0:  # Cap the failure probability at 100%
                    failure_probability += 0.05  # Increase failure probability
            print('failure_probability after: ', failure_probability)
        except FileNotFoundError:
            print(f'File not found error')
        except PermissionError:
            print(f'Permission error')
        except IsADirectoryError:
            print(f'Is a directory error')
        except FileExistsError:
            print(f'File exists error')
        except NotADirectoryError:
            print(f'Not a directory error')
        except IOError:
            print(f'IO error')

        time.sleep(1)
