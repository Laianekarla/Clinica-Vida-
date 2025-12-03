class Agendamento:
    def __init__(self, id, cpf_paciente, crm_medico, tipo):
        self.id = id  # número sequencial
        self.cpf_paciente = cpf_paciente
        self.crm_medico = crm_medico
        self.tipo = tipo  # "Normal" ou "Emergência"
        self.status = "Agendado"  # Pode mudar depois (Cancelado / Atendido)

    def to_dict(self):
        return {
            "id": self.id,
            "cpf_paciente": self.cpf_paciente,
            "crm_medico": self.crm_medico,
            "tipo": self.tipo,
            "status": self.status
        }