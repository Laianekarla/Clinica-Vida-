class Paciente:
    def __init__(self, cpf, nome, idade):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade

    def to_dict(self):
        return {
            "cpf": self.cpf,
            "nome": self.nome,
            "idade": self.idade
        }