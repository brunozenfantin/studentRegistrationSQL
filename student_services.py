import dao.student_dao as dao
from models.student import Student

def create_record(name,email,age):
    student = Student(name,email,age)

    #validacao dos dados e regra de negocio
    #usuario informou @ no email
    #informou idade > 130
    if age >= 130:
        print("Idade incorreta")
        return
    
    if age < 10:
        print("Aceitamos matriculas apenas para alunos maiores de idade")
        return

    dao.insert_student(student)




