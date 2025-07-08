import sqlite3
from contextlib import contextmanager


#constante que indica o caminho para o diretorio do banco de dados
DB_NAME = "C:/Projeto/studentRegistrationSQL/databases/students.db"

def undo(msg:str, e , conexao):
    conexao.rollback()
    print(f"{msg}{e}")
    raise


@contextmanager
def get_cursor():
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    try:
        yield cursor
        conexao.commit()
    except sqlite3.IntegrityError as e:
        undo(f"ocorreu um erro de integridade no banco de dados: {e}")       
    except sqlite3.ProgrammingError as e:
        undo(f"ocorreu um erro de programação: {e}")        
    except sqlite3.OperationalError as e:
        undo(f"ocorreuum erro do sistema operacional: {e}")        
    except sqlite3.DatabaseError as e:
        undo(f"ocorreu um erro de banco de dados: {e}")
    except Exception as e:
        undo(f"erro inesperado: {e}")
    finally:
        conexao.close()

def createTable():
    with get_cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS aluno(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        idade INTEGER
                    )                                             
            """)
    


