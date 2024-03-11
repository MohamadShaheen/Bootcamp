import objects.truck as tr
import objects.road as rd
import json


def load_json_file(file_path):
    with open(file_path, "r") as file:
        roads = json.load(file)
    return roads


def main():
    road_types_location = 'data/road_types.json'
    trucks_location = 'data/trucks.json'

    road_types = load_json_file(road_types_location)
    trucks = load_json_file(trucks_location)

    rd.add_road(road_types_location=road_types_location, name='test', terrain_hardness=1, mental_effect=2, wheel_damage_effect=1.5)


if __name__ == "__main__":
    main()