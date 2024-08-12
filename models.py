from database import Database

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def save(self):
        db = Database()
        db.execute_query("INSERT INTO pessoas (nome, idade) VALUES (%s, %s)", (self.nome, self.idade))
        db.close()

    @staticmethod
    def get_all():
        db = Database()
        results = db.fetch_all("SELECT * FROM pessoas")
        db.close()
        return results
