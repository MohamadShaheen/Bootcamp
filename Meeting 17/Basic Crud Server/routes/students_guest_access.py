from utils.database_functions import read_data
from fastapi import APIRouter, Query, HTTPException
from main import filepath

students = read_data(filepath=filepath)

router = APIRouter()


@router.get('/get-all-students')
def get_all_students():
    students_list = []
    for student in students:
        student_details = {
            'name': student['name'],
            'age': student['age'],
            'classes': student['classes']
        }
        students_list.append(student_details)

    return students_list


@router.get('/get-student-by-name')
def get_student_by_name(name: str = Query(..., description='Enter student name')):
    for student in students:
        if student['name'] == name:
            student_details = {
                'name': student['name'],
                'age': student['age'],
                'classes': student['classes']
            }
            return student_details

    raise HTTPException(status_code=404, detail='Student with that name does not exist')


@router.get('/get-student-by-id')
def get_student_by_id(id: str = Query(..., description='Enter student ID')):
    for student in students:
        if student['id'] == id:
            student_details = {
                'name': student['name'],
                'age': student['age'],
                'classes': student['classes']
            }
            return student_details

    raise HTTPException(status_code=404, detail='Student with that ID does not exist')

