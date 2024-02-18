import random


def main():
    class Pokemon:
        def __init__(self, name, level, strength, speed, type, life):
            self.name = name
            self.level = level
            self.strength = strength
            self.speed = speed
            self.type = type
            self.life = life

    class Player:
        def __init__(self, pokemons):
            self.pokemons = pokemons

    # Create pokemons for the first player
    pokemons_1 = [
        Pokemon('Blazeleon', 28, 7, 3, 'Fire', 120),
        Pokemon('Torrenturtle', 35, 6, 4, 'Water', 120),
        Pokemon('Terrafang', 40, 8, 2, 'Earth', 120),
        Pokemon('Gustavian', 45, 5, 5, 'Wind', 120),
        Pokemon('Flamewyrm', 25, 8, 4, 'Fire', 120)
    ]

    # Create pokemons for the second player
    pokemons_2 = [
        Pokemon('Infernozard', 32, 9, 2, 'Fire', 120),
        Pokemon('Aquablastoise', 38, 7, 3, 'Water', 120),
        Pokemon('Georock', 42, 8, 1, 'Earth', 120),
        Pokemon('Zephyraptor', 50, 6, 5, 'Wind', 120),
        Pokemon('Hydrodrake', 34, 6, 5, 'Water', 120)
    ]

    # Save the players in the list
    players = [
        Player(pokemons_1),
        Player(pokemons_2)
    ]

    # Create table that indicates which styles each style beats
    types_table = {
        'Fire': ['Water', 'Wind'],
        'Water': ['Earth'],
        'Earth': ['Fire', 'Wind'],
        'Wind': ['Water']
    }

    player_1 = players[0]
    player_2 = players[1]

    # Add random speeds to player_1 pokemons
    for pokemon in player_1.pokemons:
        random_num = random.randint(1, 20)
        pokemon.speed += random_num

    # Add random speeds to player_2 pokemons
    for pokemon in player_2.pokemons:
        random_num = random.randint(1, 20)
        pokemon.speed += random_num

    # Create a function to determine the best pokemon for each player
    def best_pokemon(player):
        player_pokemon = player.pokemons[0]

        for pokemon in player.pokemons:
            if pokemon is player_pokemon:
                continue

            if pokemon.speed > player_pokemon.speed:
                player_pokemon = pokemon

        return player_pokemon

    # Continue until one player has no pokemons left
    while len(player_1.pokemons) != 0 and len(player_2.pokemons) != 0:
        # Get the best pokemon for each player
        player_1_pokemon = best_pokemon(player_1)
        player_2_pokemon = best_pokemon(player_2)

        # State which pokemons enters the fight
        print(f'Player 1: Pokemon {player_1_pokemon.name} has joined the fight')
        print(f'Player 2: Pokemon {player_2_pokemon.name} has joined the fight')

        # Continue until a pokemon has lost
        while True:
            # Both pokemons have the same type
            if player_1_pokemon.type == player_2_pokemon.type:
                damage_1 = random.randint(1, 20) + player_1_pokemon.strength
                damage_2 = random.randint(1, 20) + player_2_pokemon.strength

            # player_1 pokemon is stronger
            elif player_2_pokemon.type in types_table[player_1_pokemon.type]:
                damage_1 = 2 * (random.randint(1, 20) + player_1_pokemon.strength)
                damage_2 = random.randint(1, 20) + player_2_pokemon.strength

            # player_2 pokemon is stronger
            else:
                damage_1 = random.randint(1, 20) + player_1_pokemon.strength
                damage_2 = 2 * (random.randint(1, 20) + player_2_pokemon.strength)

            player_2_pokemon.life -= damage_1

            print(f'{player_1_pokemon.name} attack {player_2_pokemon.name}. deals {damage_1} damage. '
                  f'{player_2_pokemon.name} now has {player_2_pokemon.life} amount of life after the attack.')

            # If player_2's pokemon has died
            if player_2_pokemon.life <= 0:
                player_2.pokemons.remove(player_2_pokemon)
                print(f'\nPokemon {player_2_pokemon.name} has died\n')
                print(f'Pokemon {player_1_pokemon.name} has won')
                print(f'Pokemon {player_2_pokemon.name} has lost\n')
                break

            player_1_pokemon.life -= damage_2

            print(f'{player_2_pokemon.name} attack {player_1_pokemon.name}. deals {damage_2} damage. '
                  f'{player_1_pokemon.name} now has {player_1_pokemon.life} amount of life after the attack.')

            # If player_1's pokemon has died
            if player_1_pokemon.life <= 0:
                player_1.pokemons.remove(player_1_pokemon)
                print(f'\nPokemon {player_1_pokemon.name} has died\n')
                print(f'Pokemon {player_2_pokemon.name} has won')
                print(f'Pokemon {player_1_pokemon.name} has lost\n')
                break


if __name__ == '__main__':
    main()
