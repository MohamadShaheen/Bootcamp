from main import load_json_file
import json


def add_road(road_types_location, name, terrain_hardness, mental_effect, wheel_damage_effect):
    road_types = load_json_file(road_types_location)

    road_types[name] = {
        'terrain_hardness': terrain_hardness,
        'mental_effect': mental_effect,
        'wheel_damage_effect': wheel_damage_effect
    }

    with open(road_types_location, 'w') as file:
        json.dump(road_types, file, indent=4)
