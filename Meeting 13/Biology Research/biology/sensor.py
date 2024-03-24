import random
import time
from biology import analyzer
from handler import data_handler


def create_record():
    rabbits_births = random.randint(10, 20)
    rabbits_deaths = random.randint(10, 20)
    record = {'births': rabbits_births, 'deaths': rabbits_deaths}

    print(f'Rabbits births: {rabbits_births}. Rabbits deaths: {rabbits_deaths}.')

    sleep_time = random.randint(5, 10)
    time.sleep(sleep_time)

    return record


def create_records():
    num_of_records = random.randint(10, 30) * 10
    print(f'Number of records to be generated: {num_of_records}')
    records = []

    for i in range(num_of_records):
        if (i + 1) % 10 == 0:
            analyzer.analyze_records()
            data_handler.update_json(key='records', value=records)

        record = create_record()
        records.append(record)
