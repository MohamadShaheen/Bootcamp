from faker import Faker
import random
import json
import os

filepath = 'data/students.json'


def create_student():
    list_of_classes = ['Mathematics', 'Science', 'Engineering', 'Chemistry', 'Biology']
    fake = Faker('en_US')

    name = fake.name()
    id = str(fake.random_number(digits=9))
    age = random.randint(15, 17)
    classes = random.sample(list_of_classes, random.randint(1, len(list_of_classes)))

    student = {'name': name, 'id': id, 'age': age, 'classes': classes}
    return student


def create_data(filepath):
    if os.path.exists(filepath):
        print("File already exists")
        return

    students = []
    num_of_students = 100

    for _ in range(num_of_students):
        student = create_student()
        students.append(student)

    with open(filepath, 'w') as file:
        json.dump(students, file, indent=4)


def read_data(filepath):
    if not os.path.exists(filepath):
        print('File does not exist')
        return None

    with open(filepath, 'r') as file:
        data = json.load(file)

    return data


def add_data(filepath, new_data):
    with open(filepath, 'r') as file:
        data = json.load(file)

    data.append(new_data)

    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    create_data(filepath=filepath)


if __name__ == "__main__":
    main()
