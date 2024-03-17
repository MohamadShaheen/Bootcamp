from main import print_list_numbered


class User:
    def __init__(self, records: list):
        self.records = records

    def search_record_by_name(self, record_name: str) -> bool:
        for record in self.records:
            if record[0] == record_name:
                print(f'Record found: {record}')
                return True
        print(f'Record not found: {record_name}')
        return False

    def print_record_amount(self, record_name: str) -> bool:
        for record in self.records:
            if record[0] == record_name:
                print(f'Record amount: {record[1]}')
                return True
        print(f'Record not found: {record_name}')
        return False

    def print_all_records(self):
        print_list_numbered(self.records)
