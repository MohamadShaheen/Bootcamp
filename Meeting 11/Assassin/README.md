# Assassin Game Simulator

This code offers a solution to the problem of
identifying the assassin among a group of players in a
game scenario. Each player accuses another, and if their
accusation is correct, the game concludes, and the
assassin is apprehended. Conversely, if the game
concludes with only a single player and the assassin
remaining, the assassin emerges victorious.
This script serves as a basic implementation
reminiscent of the mechanics found
in the popular game `Among Us`.

<br></br>

# Directories

## data
The `data` directory houses a .JSON file containing information about places, weapons, and player names.

## games
Within the `games` directory resides a class responsible for simulating a complete game.

<br>

# Classes and Their Functions

## Game
This class contains all the necessary functions to simulate
a full game.

### Functions

`_generate_round_data`: Generates the data for a single round and returns it.
`_generate_murdered_person`: Generates the murdered person and returns it.
`_suspect_and_accuse`: Returns suspicious and accused players by a single player.
`_simulate_round`: Simulates a single round and returns True if the assassin found, False otherwise.
`simulate_game`: Simulates the entire game.

<br>

# Error Handling and Points of Failure

In certain instances, a proper accusation couldn't be determined, leading the current player to accuse a random player, albeit not the ideal action.

Given that everything was randomly generated, frequent checks for values weren't necessary. Additionally, since inputs were appropriately formatted and their types didn't require validation, these checks were omitted.