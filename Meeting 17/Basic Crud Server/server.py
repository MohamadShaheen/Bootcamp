from routes import students_admin_access, students_guest_access
from fastapi import FastAPI
from main import read_data


students = read_data(filepath='data/students.json')

app = FastAPI()

app.include_router(students_admin_access.router)
app.include_router(students_guest_access.router)


@app.get('/')
def root():
    return 'Welcome to the Crud Server!'
