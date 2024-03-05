import requests
import json
import matplotlib.pyplot as plt


def extract_decimal(string, i):
    # For a string number, get the number with 'i' digits after the decimal point
    decimal_index = string.find('.')
    if decimal_index != -1:
        return string[:decimal_index + i]
    else:
        return None


def create_plot(first_metric, second_metric, title, xlabel, ylabel, save_as):
    plt.figure(figsize=(10, 6))
    plt.plot(first_metric, second_metric, 'o', color='red', markersize=5)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(save_as)
    plt.show()


def main():
    # Insert your API Key file
    with open('API Key.txt', 'r') as file:
        API_key = file.read().strip()

    url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-13&api_key={API_key}'

    # Request the data and save it as json file
    response = requests.get(url)
    data = response.json()

    # This where the asteroids details are found
    near_earth_objects = data['near_earth_objects']

    asteroids_data = []
    min_diameters = []
    velocities = []
    distances = []
    max_diameters = []
    names = []

    # Loop over all dates in the given range
    for date in near_earth_objects:
        # Get all detected asteroids in the respective date
        asteroids = near_earth_objects[date]
        for asteroid in asteroids:
            # Get the asteroid details
            asteroid_id = asteroid['id']
            name = asteroid['name']
            diameter_min = asteroid['estimated_diameter']['kilometers']['estimated_diameter_min']
            diameter_max = asteroid['estimated_diameter']['kilometers']['estimated_diameter_max']
            miss_distance_km = asteroid['close_approach_data'][0]['miss_distance']['kilometers']
            relative_velocity_kmh = asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']

            # Save the asteroid info as dictionary
            asteroid_info = {
                "asteroid_id": asteroid_id,
                "name": name,
                "estimated_diameter_min_km": diameter_min,
                "estimated_diameter_max_km": diameter_max,
                "miss_distance_km": miss_distance_km,
                "relative_velocity_kmh": relative_velocity_kmh
            }

            # Add the asteroid to the list of all asteroids
            asteroids_data.append(asteroid_info)
            min_diameters.append(diameter_min)
            velocities.append(extract_decimal(relative_velocity_kmh, 4))
            distances.append(extract_decimal(miss_distance_km, 4))
            max_diameters.append(diameter_max)
            names.append(name)

    # Save the asteroids list as JSON file
    with open('asteroids_data.json', 'w') as json_file:
        json.dump(asteroids_data, json_file, indent=4)

    # Keep first 30 asteroids that were detected
    min_diameters = min_diameters[:30]
    velocities = velocities[:30]
    distances = distances[:30]
    max_diameters = max_diameters[:30]
    names = names[:30]

    create_plot(min_diameters, velocities, 'Minimum Diameter vs. Relative Velocity of Asteroids',
                'Minimum Diameter (km)', 'Relative Velocity (km/h)', 'min_diameter_velocity.png')

    create_plot(max_diameters, distances, 'Maximum Diameter vs. Miss Distance of Asteroids',
                'Maximum Diameter (km)', 'Miss Distance (km)', 'miss_distance_max_diameter.png')

    # Create lists for the coefficients
    coefficients = []
    coefficients_names = ['A', 'B', 'C']

    for coefficients_name in coefficients_names:
        # Keep trying until the user enters valid input
        while True:
            try:
                string_number = input(f'Enter {coefficients_name} (empty input to make it 1): ')
                if string_number == '':
                    coefficients.append(1)
                    break
                number = float(string_number)
                coefficients.append(number)
                break
            except ValueError:
                print('Invalid input')

    # Calculate the danger for each asteroid
    average_diameter = [coefficients[0] * (a + b) / 2 for a, b in zip(min_diameters, max_diameters)]
    relative_speed = [coefficients[1] * float(a) for a in velocities]
    miss_distance = [1 / coefficients[2] * float(a) for a in distances]

    dangers = [extract_decimal(str(a + b + c), 0) for a, b, c in zip(average_diameter, relative_speed, miss_distance)]

    create_plot(dangers, names, 'Dangers vs. Names of Asteroids',
                'Danger', 'Name', 'name_danger.png')


if __name__ == '__main__':
    main()
