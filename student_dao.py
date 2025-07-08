from db.connection import get_cursor
from models.student import Student

def insert_student(student):
    with get_cursor() as cursor:
        cursor.execute("INSERT INTO aluno(nome,email,idade) VALUES (?,?,?)",
                       (student.name,student.email,student.age)
        )


def update_student(student):
    with get_cursor() as cursor: 
        cursor.execute("UPDATE aluno SET nome = ?, email = ?, idade = ? WHERE id = ?",
                   (student.name,student.email,student.age, student.id))


def get_all_students():
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM aluno")
        rows = cursor.fetchall()
        return [Student(id=row[0], name=row[1], email=[2], age=[3]) for row in rows]
        

        
    
def delete_students(id):
     with get_cursor() as cursor: 
        cursor.execute("DELETE FROM aluno WHERE id=?",
                   (id))



