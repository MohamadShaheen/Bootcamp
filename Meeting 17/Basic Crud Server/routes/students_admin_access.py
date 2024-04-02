from utils.database_functions import read_data, add_data
from fastapi import APIRouter, Query, HTTPException
from classes.student import Student
from main import filepath

students = read_data(filepath=filepath)

router = APIRouter()


@router.post('/add-student')
def add_student(new_student: Student):
    for student in students:
        if student['id'] == str(new_student.id):
            raise HTTPException(status_code=404, detail='Student with that ID already exists')

    add_data(filepath=filepath, new_data=new_student.dict())
    students.append(new_student.dict())
    return {'message': 'Student was added successfully'}


@router.get('/get-students-in-class')
def get_students_in_class(class_type: str = Query(..., description='Enter class type')):
    students_in_class = []
    for student in students:
        if class_type in student['classes']:
            students_in_class.append(student)

    if len(students_in_class) > 0:
        return students_in_class
    else:
        raise HTTPException(status_code=404, detail='No students found')
