from handler import data_handler


def analyze_records():
    num_alive_rabbits = data_handler.read_from_json(key='alive_rabbits')
    records = data_handler.read_from_json(key='records')
    records = records[-10:]

    for record in records:
        rabbits_birth = record['births']
        rabbits_deaths = record['deaths']
        if num_alive_rabbits + rabbits_birth < rabbits_deaths:
            print(f'Record {record} is not valid and shall be ignored')
            continue

        num_alive_rabbits += rabbits_birth - rabbits_deaths

    data_handler.update_json(key='alive_rabbits', value=num_alive_rabbits)
