import random
import time
import math
import json
import requests

counter = 0


class Spaceship:
    def __init__(self, name):
        self.name = name
        self.fuel = random.randint(100, 1000)
        self.health = random.randint(100, 1000)
        self.original_fuel = self.fuel
        self.original_health = self.health
        self.filename = f'spaceship{counter}.json'
        self.events = []

    def travel(self, distance):
        # Calculate the fuel needed according to the distance
        fuel_needed = math.ceil(distance * 0.05)
        # If the spaceship doesn't have enough fuel then end the game
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            self.events.append(f'{self.name} traveled {distance} light-years')
            print(f'{self.name} traveled {distance} light-years')
        else:
            self.events.append(f'{self.name} does not have enough fuel for this journey')
            print(f'{self.name} does not have enough fuel for this journey')

    def encounter_event(self):
        # Choose random event according to given probabilities
        event = random.choices(['Asteroid Field', 'Space Pirates', 'Alien Diplomacy', 'Black Hole'], (0.33, 0.33, 0.33, 0.01))[0]
        # Decide what to do for each encountered event
        if event == 'Asteroid Field':
            self.health -= 10
            self.events.append('Asteroid Field encountered! Health reduced')
            print('Asteroid Field encountered! Health reduced')
        elif event == 'Space Pirates':
            self.health -= 15
            self.fuel -= 10
            self.events.append('Space Pirates attacked! Health and fuel reduced')
            print('Space Pirates attacked! Health and fuel reduced')
        elif event == 'Alien Diplomacy':
            self.fuel += 20
            self.events.append('Met friendly aliens. Fuel replenished')
            print('Met friendly aliens. Fuel replenished')
        elif event == 'Black Hole':
            self.health = 0
            self.fuel = 0
            self.events.append('Fell into a Black Hole. Game Over')
            print('Fell into a Black Hole. Game Over')
            
        self.events.append(f'{self.name} - Health: {self.health}, Fuel: {self.fuel}')

    def save_to_json(self):
        data = {
            'name': self.name,
            'health': self.original_health,
            'fuel': self.original_fuel,
            'events': self.events
        }

        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_json_file(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)

        return data

    def __str__(self):
        return f'{self.name} - Health: {self.health}, Fuel: {self.fuel}\n'


def main():
    # Create spaceship names. I just took random names from the internet.
    spaceship = Spaceship(random.choice(['Voyager', 'Explorer', 'Starship', 'Cosmos', 'Odyssey', 'Infinity', 'Pioneer', 'Eclipse', 'Phoenix', 'Astral']))

    print('########################################################################################\n')
    print('\t\t\t\t\t\t\t\tSpaceship Details\n')
    print('########################################################################################\n')

    print(spaceship)

    print('########################################################################################\n')
    print('\t\t\t\t\t\t\t\t\tGame Started\n')
    print('########################################################################################\n')

    # Continue as long as the ship has health and fuel
    while spaceship.health > 0 and spaceship.fuel > 0:
        spaceship.travel(random.randint(5, 20))
        spaceship.encounter_event()
        print(spaceship)
        # Uncomment to add times between each event
        # time.sleep(1)

    # Save th spaceship details to JSON file
    spaceship.save_to_json()
    print('Game Over. Thanks for playing!\n')

    print('########################################################################################\n')
    print('\t\t\t\t\t\t\t\tLoad JSON File\n')
    print('########################################################################################\n')

    # Load the JSON file
    file = spaceship.load_json_file()
    print(f'{file['name']} - Health: {file['health']}, Fuel: {file['fuel']}\n')

    for i, event in enumerate(file['events']):
        if i % 3 == 0:
            print()
            print(event)
        else:
            print(event)


if __name__ == '__main__':
    main()
