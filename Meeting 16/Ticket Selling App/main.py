import json
import os
import random


def generate_tickets(filepath):
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file:
            data = json.load(file)
        if data:
            print('File already exists')
            return

    ids = random.sample(range(10000, 100000), 2000)
    events = ['Concert', 'Sports Game', 'Theater Show', 'Movie Premiere']
    prices = [20, 100, 40, 60]

    data = {'Concert': None, 'Sports Game': None, 'Theater Show': None, 'Movie Premiere': None}

    i = 0
    for event, price in zip(events, prices):
        for _ in range(500):
            data[ids[i]] = {'event': event, 'price': price, 'sold': False}
            i += 1

    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    generate_tickets(filepath='data/tickets.json')


if __name__ == '__main__':
    main()