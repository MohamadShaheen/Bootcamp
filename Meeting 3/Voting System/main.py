from queue import Queue
from faker import Faker
import random
import string


def main():
    # Create a Faker instance to generate random names and addresses
    fake = Faker('en_US')
    # The candidates will be stored in a 'Dictionary'
    candidates = {
        'John Smith': ['Legislative Aide', 'Public Relations Officer'],
        'Maria Garcia': ['Policy Analyst', 'Government Affairs Specialist'],
        'Mohammed Khan': ['Budget Analyst', 'Grants Administrator'],
        'Catherine White': ['Environmental Planner', 'Urban Development Coordinator'],
        'Carlos Martinez': ['Immigration Officer', 'Community Outreach Coordinator']
    }
    # Create a 'Dictionary' to store for each candidate how many votes he got
    votes_statistics = {
        'John Smith': 0,
        'Maria Garcia': 0,
        'Mohammed Khan': 0,
        'Catherine White': 0,
        'Carlos Martinez': 0
    }

    # Create a 'Queue' to represent the current line
    q = Queue()
    # Create a 'List' to store the voters (if needed)
    voters = []
    # Create a 'List' to store the votes (if needed)
    votes = {}

    # Consider 1,000 iterations
    for i in range(1000):
        # Generate random number of voters that arrive at one-time
        for _ in range(random.randint(1, 10)):
            # Generate a random name
            voter_name = fake.name()
            # Generate a random age
            voter_age = random.randint(18, 80)
            # Generate a random address
            voter_address = fake.address().replace('\n', ' ')

            # Generate a random vote id of 9 digits
            vote_id = ''.join(random.choices(string.digits, k=9))
            # Generate a vote for a random candidate
            vote_candidate = random.choice(list(candidates.keys()))

            # Check if the specific id didn't vote before
            if not (vote_id in votes.keys()):
                voters.append([voter_name, voter_age, voter_address])
                votes[vote_id] = vote_candidate
                q.put([voters[-1], vote_id, vote_candidate])
            # Detect an imposter
            else:
                print(f'{voter_name} has already voted. He is imposter.')

        # Allow all the voters to vote following FIFO principle
        while not q.empty():
            vote_details = q.get()
            # Print voter details
            print(f'{vote_details[0][0]} arrives to vote. He is {vote_details[0][1]} years old. '
                  f'He lives in {vote_details[0][2]}.')
            # Print vote details
            print(f'Vote id is {vote_details[1]}. He voted for {vote_details[2]}.\n')
            # Increase the votes of the respective candidate by 1
            votes_statistics[vote_details[2]] += 1

    # Print the results
    for key, value in votes_statistics.items():
        print(f'{key} got {value} votes.')


if __name__ == '__main__':
    main()
