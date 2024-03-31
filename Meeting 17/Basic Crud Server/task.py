from fastapi import FastAPI, Query, HTTPException
from main import read_data, add_data, filepath
from classes.student import Student

students = read_data(filepath='data/students.json')

app = FastAPI()


@app.get('/get-all-students')
def get_all_students():
    return students


@app.get('/get-student-by-name')
def get_student_by_name(name: str = Query(..., description='Enter student name')):
    for student in students:
        if student['name'] == name:
            return student

    raise HTTPException(status_code=404, detail='Student with that name does not exist')


@app.get('/get-student-by-id')
def get_student_by_id(id: str = Query(..., description='Enter student ID')):
    for student in students:
        if student['id'] == id:
            return student

    raise HTTPException(status_code=404, detail='Student with that ID does not exist')


@app.post('/add-student')
def add_student(new_student: Student):
    for student in students:
        if student['id'] == str(new_student.id):
            raise HTTPException(status_code=404, detail='Student with that ID already exists')

    add_data(filepath=filepath, new_data=new_student.dict())
    students.append(new_student.dict())
    return {'message': 'Student was added successfully'}


@app.get('/get-students-in-class')
def get_students_in_class(class_type: str = Query(..., description='Enter class type')):
    students_in_class = []
    for student in students:
        if class_type in student['classes']:
            students_in_class.append(student)

    if len(students_in_class) > 0:
        return students_in_class
    else:
        raise HTTPException(status_code=404, detail='No students found')
