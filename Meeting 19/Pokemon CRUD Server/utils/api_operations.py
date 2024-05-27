import requests

poke_api_URL = 'https://pokeapi.co/api/v2/pokemon'


def get_pokemon_details(pokemon_name):
    response = requests.get(f'{poke_api_URL}/{pokemon_name.lower()}')
    if response.status_code == 200:
        data = response.json()
        types = [type_info['type']['name'] for type_info in data['types']]
        height = data['height']
        weight = data['weight']
        return types, height, weight
    else:
        return None, None, None
