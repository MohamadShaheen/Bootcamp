import json
from games.game import Game
import random


def load_json_file(file_location) -> dict:
    try:
        with open(file_location) as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f'JSON file with the provided location does not exist. Application terminated.')


def main():
    data = load_json_file(file_location='data/assassin_data.json')

    places = data['places']
    weapons = data['weapons']
    names = data['names']

    players = {}
    for name in names:
        last_visited_places = []
        favorite_weapons = random.sample(weapons, random.randint(1, 3))
        players[name] = [last_visited_places, favorite_weapons]

    game = Game(players=players, places=places, weapons=weapons)
    game.simulate_game()


if __name__ == '__main__':
    main()
