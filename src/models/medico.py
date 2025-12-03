class Medico:
    def __init__(self, crm, nome, especialidade):
        self.crm = crm
        self.nome = nome
        self.especialidade = especialidade
        self.disponivel = True  # médico pode estar disponível ou não

    def to_dict(self):
        return {
            "crm": self.crm,
            "nome": self.nome,
            "especialidade": self.especialidade,
            "disponivel": self.disponivel
        }