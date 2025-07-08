import dao.student_dao as dao
from models.student import Student

def validate_data(student):
    if student.age >= 130:
        print("Idade incorreta")
        return False
    
    if student.age <= 18:
        print("Aceitamos matriculas apenas para alunos maiores de idade")
        return False

    return True


def create_record(name: str,email: str,age: int):
    student = Student(name,email,age)

    if validate_data(student):
        dao.insert_student(student)


def edit_record( name: str,email: str,age: int, id: int):
    student = Student(name,email,age,id)
    
    if validate_data(student):
        dao.update_student(student)



def display_record():
    return dao.get_all_students()   


def delete_record(id) :
    dao.delete_students(id)