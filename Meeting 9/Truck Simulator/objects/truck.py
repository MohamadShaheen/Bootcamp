def calculate_fuel_consumption(truck, road_type, length):
    terrain_hardness = road_type['terrain_hardness']
    fuel_consumption = length / (truck['km_per_liter'] * terrain_hardness)
    truck['fuel'] -= fuel_consumption
    return fuel_consumption


def calculate_wheel_wear(truck, road_type, length):
    wheel_damage_effect = road_type['wheel_damage_effect']
    wheel_damage = length * wheel_damage_effect
    wheel_repair_cost = wheel_damage * truck['wheel_repair_cost']
    return wheel_repair_cost


def calculate_mental_effect(truck, road_type):
    mental_effect = road_type['mental_effect']
    truck['mental_health'] += mental_effect
