from utils.database_functions import create_data, add_field_to_data

filepath = 'data/students_data.json'


def main():
    create_data(filepath=filepath)

    add_field_to_data(filepath=filepath, field_name='password', field_value=None)


if __name__ == "__main__":
    main()
