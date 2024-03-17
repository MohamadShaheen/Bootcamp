import csv


class DataHandler:
    def __init__(self, csv_file_location: str):
        with open(csv_file_location, 'r'):
            self.csv_file = csv.reader(csv_file_location)

    def get_records(self) -> list:
        records = []
        for row in self.csv_file:
            records.append(row)

        return records

    def add_record(self, record_name: str, record_num_of_copies: int):
        new_record = [record_name, record_num_of_copies]

        csv_writer = csv.writer(self.csv_file)
        csv_writer.writerow(new_record)

    def remove_record(self, record_name: str, record_num_of_copies: int):
        record_to_remove = [record_name, record_num_of_copies]

        self.csv_file.seek(0)
        updated_records = [row for row in csv.reader(self.csv_file) if row != record_to_remove]
        self.csv_file.seek(0)
        self.csv_file.truncate()
        csv_writer = csv.writer(self.csv_file)
        csv_writer.writerows(updated_records)

    def update_record(self, old_record: list, new_record: list):

