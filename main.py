import sys
import os

PROJECT_DIR = "C:\\Projeto\\studentRegistrationSQL\\"

sys.path.append(os.path.abspath(PROJECT_DIR))

from db.connection import createTable
import services.student_services as service

def show_students():
                students = service.display_record()

                for student in students:
                    print(f"{student.id} - {student.name} - {student.email} - {student.age}")


#MENU   PRINCIPAL
def mainMenu() -> str:
    print("\n Sistema de Cadastro de Alunos")
    print("1. Cadastrar aluno")
    print("2. Listar Aluno")
    print("3. Atualizar Aluno")
    print("4. Excluir Aluno")
    print("5. Sair")

    opcao: str = input("Escolha uma opção:")
    return opcao

if __name__ == "__main__":
    createTable()
    


    while True:
        opcao = mainMenu() 

        if opcao == "1":
            name: str = input("Nome:")
            email: str = input("E-mail:")
            age = int(input("Idade:"))
            service.create_record(name,email,age)
            show_students()        
        elif opcao == "2":
            show_students()
       
        elif opcao == "3":
            id = int(input("Informe o id do aluno que vc deseja atualizar: "))
            name = input("novo nome: ")
            email = input("novo email: ")
            age = int(input("nova idade: "))
            service.edit_record(name,email,age,id) 
            show_students()
                       
      
        elif opcao == "4":
            id = input("Informe o id do aluno que vc quer excluir: ")         
            service.delete_record(id)
            print("Aluno deletado com sucesso!")
            show_students()
        
        elif opcao == "5":
            break
        else:
            print("Opção invalida")


