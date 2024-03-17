import random


class Game:
    def __init__(self, players: dict, places: list, weapons: list):
        self.players = players
        self.places = places
        self.weapons = weapons

    def _generate_round_data(self, assassin: str, murder_place: str, murder_weapon: str) -> dict:
        """
        Generate a dictionary as data for a single round
        :param assassin: represents the assassin name
        :param murder_place: represents the place where the murder occurred
        :param murder_weapon: represents the weapon the murderer used
        :return: returns a dictionary with the data for the round of the game
        """
        round_data = {}
        for player in self.players.keys():
            # Randomly generate 1-3 visited places
            visited_places = random.sample(self.places, random.randint(1, 3))

            # Ensure that the assassin visited the murder place
            if player == assassin and murder_place not in visited_places:
                visited_places.pop()
                visited_places.append(murder_place)
                self.players[player][0] = visited_places

            # Ensure that the assassin has the murder weapon as one of his favorites
            if player == assassin and murder_weapon not in self.players[player][1]:
                self.players[player][1].pop()
                self.players[player][1].append(murder_weapon)

            self.players[player][0] = visited_places
            round_data[player] = [visited_places, self.players[player][1]]

        return round_data

    def _generate_murdered_person(self, assassin: str, murder_place: str, round_data: str) -> str:
        """
        Generate a murdered person
        :param assassin: represents the assassin name
        :param murder_place: represents the place where the murder occurred
        :param round_data: represents a dictionary with the data for the round of the game
        :return: returns the murdered person name
        """
        for name, values in round_data.items():
            # Ensure that the murdered person visited the murder place, and he is not the assassin himself
            if name != assassin and murder_place in values[0]:
                break

        # Remove the murdered person from the current round and from all players list
        self.players.pop(name)
        round_data.pop(name)

        return name

    def _suspect_and_accuse(self) -> tuple:
        """
        Generate a suspected and accused players
        :return: returns the suspected and accused players
        """
        suspected_players = random.sample(self.places, 2)
        favorite_weapon = random.choice(self.weapons)
        accused_player = ''
        for player_name, player_values in self.players.items():
            # Check if the suspected player visited the murder place and the murder weapon is one of his favorites
            for suspected_player in suspected_players:
                if suspected_player in player_values[0] and favorite_weapon in player_values[1]:
                    accused_player = player_name

        # Generate random accused player in case there is no match
        if accused_player == '':
            accused_player = random.choice(list(self.players.keys()))

        return suspected_players, accused_player

    def _simulate_round(self) -> bool:
        """
        Simulate a single round
        :return: returns True if the assassin has been found, False otherwise
        """
        assassin = random.choice(list(self.players.keys()))
        murder_place = random.choice(self.places)
        murder_weapon = random.choice(self.weapons)

        round_data = self._generate_round_data(assassin=assassin, murder_place=murder_place, murder_weapon=murder_weapon)
        murdered_player = self._generate_murdered_person(assassin=assassin, murder_place=murder_place, round_data=round_data)
        for player in round_data.keys():
            suspected_players, accused_player = self._suspect_and_accuse()
            if accused_player == assassin:
                print(f'Player {player} found the murderer. {assassin} killed {murdered_player} using {murder_weapon} at {murder_place}')
                return True

        return False

    def simulate_game(self):
        """
        Simulate a full game
        :return: terminates the game if the assassin has been found
        """
        # Loop until there is 2 player left in the game or the assassin has been found
        for _ in range(len(self.players) - 2):
            game_over = self._simulate_round()
            if game_over:
                print('Game over. Assassin has been found!')
                return
        print('Game over. Assassin has won!')
