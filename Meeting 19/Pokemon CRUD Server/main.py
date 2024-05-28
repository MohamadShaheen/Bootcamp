import json
from utils.api_operations import get_pokemon_details
from database_connection import create_database


def main():
    # with open('data/pokemons_data.json', 'r') as file:
    #     pokemon_data = json.load(file)
    #
    # for pokemon in pokemon_data:
    #     correct_types = get_pokemon_details(pokemon['name'])
    #     if correct_types:
    #         pokemon['types'] = correct_types
    #         if 'type' in pokemon:
    #             del pokemon['type']
    #
    # with open('data/pokemons_data.json', 'w') as file:
    #     json.dump(pokemon_data, file, indent=4)

    create_database.create_database()


if __name__ == '__main__':
    main()
