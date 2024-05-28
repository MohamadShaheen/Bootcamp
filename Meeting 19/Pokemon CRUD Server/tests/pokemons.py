from fastapi.testclient import TestClient
from server import app

client = TestClient(app)


def test_get_pokemon_details_by_id():
    response = client.get('/pokemons/?pokemon_id=1')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Get pokemon details by id works successfully\n{response.text}\n')


def test_get_pokemon_details_by_name():
    response = client.get('/pokemons/by-name/?pokemon_name=bulbasaur')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Get pokemon details by name works successfully\n{response.text}\n')


def main():
    test_get_pokemon_details_by_id()
    test_get_pokemon_details_by_name()


if __name__ == '__main__':
    main()
