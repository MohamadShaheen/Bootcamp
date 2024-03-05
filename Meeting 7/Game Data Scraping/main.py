import requests
from bs4 import BeautifulSoup
import json
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt


def create_soup_instance(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.text, 'html.parser')
    return soup


def count_genres(games):
    # Create a list of all genres (allow repeating)
    genres_list = []
    for genres in games.values():
        genres_list.extend(genres)
    return genres_list


def create_genres_plot(top_genres):
    # Make a pandas dataframe for plotting
    dataframe = pd.DataFrame.from_dict(top_genres, orient='index', columns=['count'])

    plt.figure(figsize=(10, 6))
    dataframe['count'].plot(kind='bar', color='skyblue')
    plt.title('Top 30 Game Genres')
    plt.xlabel('Genres')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('genres_count.png')
    plt.show()


def create_specific_genre_plot(formatted_genre, genre_count, percentage):
    plt.figure(figsize=(10, 6))
    plt.bar([formatted_genre], [genre_count], color='skyblue', label='Count')
    plt.xlabel('Genres')
    plt.ylabel('Count')
    plt.title(f'Statistics for {formatted_genre}')
    plt.xticks(rotation=45, ha='right')
    plt.legend(loc='upper right')
    plt.tight_layout()

    # Create a text stating the relevant statstic
    plt.text(formatted_genre, genre_count + 10, f'{percentage:.2f}%', ha='center')

    plt.savefig('genre_statistics.png')
    plt.show()


def main():
    # Create a BeautifulSoup instance
    soup = create_soup_instance('https://store.steampowered.com/search/?filter=globaltopsellers')
    # I can't access game genres from the given website. However, each game has its own link which
    # I can visit and get all its genres from there.
    # Get all games links
    games_links = soup.find_all('a', class_='search_result_row ds_collapse_flag')

    try:
        # If a file already created for games and there genres, get it
        with open('games.json', 'r') as file:
            games = json.load(file)
    except FileNotFoundError:
        # If no such file created, create it and save if needed in the future
        # Create a dictionary to save games names and their genres
        games = {}
        for game_link in games_links:
            # Get the current game link
            respective_game_link = game_link['href']
            # This is a special case where 'Steam Deck' isn't a game, so I add this condition to prevent errors
            if 'Steam_Deck' in respective_game_link:
                continue
            # Create a BeautifulSoup instance for the current game
            soup = create_soup_instance(respective_game_link)
            # Get the game name
            name = soup.find('div', class_='apphub_AppName')
            # Get the game tags (a list of tags)
            tags = soup.find_all('a', class_='app_tag')
            # Save the tags in a list
            tags_list = [tag.text.strip() for tag in tags]
            # Add the game along with its tags to the dictionary
            games[name.text.strip()] = tags_list

        # Save the dictionary as json file
        with open('games.json', 'w') as file:
            json.dump(games, file)

    # Count each genre and how much times it appeared
    genres_dict = Counter(count_genres(games))
    # Keep the top 30 genres (there are many genres so the plot will be deformed otherwise)
    top_n = 30
    top_genres = dict(genres_dict.most_common(top_n))

    # Plot the genres count
    create_genres_plot(top_genres)

    # Keep getting inputs until the users inserts a valid genre
    while True:
        try:
            genre = input('Enter a tag: ')
            # Uppercase the input to make the input case-independent
            uppercase_keys = [tag.upper() for tag in top_genres.keys()]
            if genre.upper() in uppercase_keys:
                break
            raise ValueError
        except ValueError:
            print('Invalid genre')

    # If the user inserted 'AcTIoN' it will be reformatted to 'Action' to prevent errors
    formatted_genre = genre.capitalize()
    # Get the number of games that has this specific genre
    genre_count = top_genres[formatted_genre]
    # Get the total count of all genres
    total_count = sum(top_genres.values())
    # Calculate the percentage
    percentage = (genre_count / total_count) * 100
    # Plot this specific genre with a statistic of its percentage according to other genres
    create_specific_genre_plot(formatted_genre, genre_count, percentage)


if __name__ == '__main__':
    main()
