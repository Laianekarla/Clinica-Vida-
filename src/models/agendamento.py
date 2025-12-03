from dataclasses import dataclass, asdict
from typing import Dict

@dataclass
class Agendamento:
    id: int
    paciente_id: int
    medico_id: int
    data_hora: str
    tipo: str  # "NORMAL" ou "EMERGÊNCIA"
    confirmado: bool = False

    def to_dict(self) -> Dict:
        return asdict(self)

    @staticmethod
    def from_dict(d: Dict):
        return Agendamento(
            id=d.get("id"),
            paciente_id=d.get("paciente_id"),
            medico_id=d.get("medico_id"),
            data_hora=d.get("data_hora"),
            tipo=d.get("tipo"),
            confirmado=d.get("confirmado", False)
        )