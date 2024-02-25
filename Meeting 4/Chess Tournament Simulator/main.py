from faker import Faker
import random


def single_round(player_1, player_2):
    # Get the ranking for each player
    ranking_1 = player_1.ranking
    ranking_2 = player_2.ranking

    # Calculate the ratio and the reversed ratio
    ratio = ranking_1 / ranking_2
    reversed_ratio = 1 - ratio

    # Calculate each of players winning chances
    player_1_winning = 0.4 - reversed_ratio
    player_2_winning = 0.4 + reversed_ratio

    # Define the results
    results = [0, 1, 2]
    # Define the density function
    probabilities = [0.2, player_1_winning, player_2_winning]

    # Choose the winner according to the density function
    winner = random.choices(results, probabilities)[0]

    # Player 1 won
    if winner == 1:
        player_1.total_points += 1
        winner = player_1.name
    # Player 2 won
    elif winner == 2:
        player_2.total_points += 1
        winner = player_2.name
    # Draw
    else:
        player_1.total_points += 0.5
        player_2.total_points += 0.5
        winner = 'Draw'

    return winner


def main():
    # Create Faker instance to generate random names
    fake = Faker('en_US')

    # Create a class for the players
    class Player:
        def __init__(self):
            self.ranking = random.randint(1500, 2000)
            self.name = fake.name()
            self.total_points = 0

    # Create a list of the players
    players = [Player(), Player(), Player(), Player()]

    # Choose two players randomly
    chosen_players = random.sample(players, 2)

    print()

    # Print the chosen players
    for player in chosen_players:
        print(f'Name: {player.name}. Total points: {player.total_points}, Rank: {player.ranking}')

    winner = single_round(chosen_players[0], chosen_players[1])

    print(f'\nWinner: {winner}\n')

    # Generate all possible pairs of players
    players_pairs = [(player_1, player_2) for i, player_1 in enumerate(players) for player_2 in players[i + 1:]]

    # for player in players_pairs:
    #     print(f'Name: {player[0].name}. Total points: {player[0].total_points}, Rank: {player[0].ranking}')
    #     print(f'Name: {player[1].name}. Total points: {player[1].total_points}, Rank: {player[1].ranking}\n')

    print('------------------------------------------------------------------------------------------\n')

    for i, pair in enumerate(players_pairs):
        winner = single_round(pair[0], pair[1])
        print(f'Round {i + 1}: {pair[0].name} VS. {pair[1].name}')
        print(f'Winner: {winner}\n')

    print()
    winner_name = ''
    winner_points = 0
    winner_rank = 0
    for player in players:
        print(f'Name: {player.name}. Total points: {player.total_points}, Rank: {player.ranking}')
        if player.total_points > winner_points:
            winner_points = player.total_points
            winner_name = player.name
            winner_rank = player.ranking
        elif player.total_points == winner_points:
            if player.ranking < winner_rank:
                winner_points = player.ranking
                winner_name = player
                winner_rank = player.ranking

    print(f'\nWinner: {winner_name}.')


if __name__ == "__main__":
    main()
