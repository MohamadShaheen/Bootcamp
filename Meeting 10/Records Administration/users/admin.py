from main import ask_user_for_numeric_input
from main import print_list_numbered
from user import User


class Admin(User):
    def __init__(self, password: str, records: list):
        super().__init__(records)
        self.password = password
        self.records = records

    def _find_records_by_name(self, record_name: str) -> list:
        found_records = []
        for name, num_of_copies in self.records:
            if record_name in name:
                found_records.append(name)

        print(f'Found {len(found_records)} records matching {record_name}: {found_records}')
        return found_records

    def _edit_existing_record(self, old_record: list, new_record: list):
        for i, sublist in enumerate(self.records):
            if sublist == old_record:
                self.records[i][1] += new_record[1]
                print(f'Record {old_record} was successfully updated to {new_record}')
                break

    def _remove_existing_record(self, record_name: str, record_num_of_copies: int):
        record_to_remove = [record_name, record_num_of_copies]
        for i, record in enumerate(self.records):
            if record == record_to_remove:
                self.records.pop(i)
                print(f'Record {record} was successfully removed')
                break

    def add_record(self, record_name: str, record_num_of_copies: int):
        found_records = self._find_records_by_name(record_name)
        if len(found_records) == 0:
            self.records.append([record_name, record_num_of_copies])
            print(f'Record [{record_name}, {record_num_of_copies}] was successfully added as new record')
        else:
            option = ask_user_for_numeric_input(input_text='Insert 1 to add as new record or 0 to edit existing record',
                                                error_text='Please choose a proper number',
                                                lower_bound=0, upper_bound=1)
            if option == 1:
                self.records.append([record_name, record_num_of_copies])
                print(f'Record [{record_name}, {record_num_of_copies}] was successfully added as new record')
            else:
                print_list_numbered(found_records)
                chosen_record = ask_user_for_numeric_input(
                    input_text=f'Please choose a record to edit (1 to {len(found_records)})',
                    error_text='Please choose a proper record number',
                    lower_bound=1, upper_bound=len(found_records))
                old_record = found_records[chosen_record - 1]
                new_record = [record_name, record_num_of_copies]
                self._edit_existing_record(old_record=old_record, new_record=new_record)

    def remove_record(self, record_name: str, record_num_of_copies: int):
        if len(self.records) == 1:
            print('There is only 1 record. You are not allowed to have no records.')
            return
        if not self.search_record_by_name(record_name=record_name):
            print('There is no record with this name and number of copies')
            return
        self._remove_existing_record(record_name, record_num_of_copies)

    def update_record_name(self, record_name: str, record_num_of_copies: int, new_record_name: str):
        self._edit_existing_record(old_record=[record_name, record_num_of_copies],
                                   new_record=[new_record_name, record_num_of_copies])

    def update_record_amount(self, record_name: str, record_num_of_copies: int, new_record_amount: int):
        self._edit_existing_record(old_record=[record_name, record_num_of_copies],
                                   new_record=[record_name, new_record_amount])