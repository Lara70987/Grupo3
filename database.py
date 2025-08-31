import sqlite3
from dataclasses import dataclass

@dataclass
class Candidato:
    id: int = None
    name: str = ""
    email: str = ""
    phone: str = ""
    matricula: str = ""
    course: str = ""
    semester: int = 0

class Database:
    def __init__(self, name_database: str):
        self.conn = sqlite3.connect(name_database + ".db", check_same_thread=False)
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS candidatos (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                matricula TEXT NOT NULL,
                course TEXT NOT NULL,
                semester INTEGER NOT NULL
                );"""
        )
    
    def add(self, candidato: Candidato) -> None:
        command = """
        INSERT INTO candidatos (name, email, phone, matricula, course, semester) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')
        """.format(candidato.name, candidato.email, candidato.phone, candidato.matricula, candidato.course, candidato.semester)
        
        self.conn.execute(command)
        self.conn.commit()
    
    def get_all(self) -> list[Candidato]:
        cursor = self.conn.execute("SELECT name, email, phone, matricula, course, semester FROM candidatos")
        data = []
        for linha in cursor:
            _id = linha[0]
            name = linha[1]
            email = linha[2]
            phone = linha[3]
            matricula = linha[4]
            course = linha[5]
            semester = linha[6]
            data.append(Candidato(
                id = _id,
                name=name,
                email=email,
                phone=phone,
                matricula=matricula,
                course=course,
                semester=semester
            ))
        
        return data
    
    def delete(self, candidato_id: int):
        self.conn.execute(f"DELETE FROM candidatos WHERE id = {candidato_id}")
        self.conn.commit()