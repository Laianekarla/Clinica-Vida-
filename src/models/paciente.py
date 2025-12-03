from dataclasses import dataclass, asdict
from typing import Dict

@dataclass
class Paciente:
    id: int
    nome: str
    idade: int
    telefone: str
    cpf: str = ""

    def to_dict(self) -> Dict:
        return asdict(self)

    @staticmethod
    def from_dict(d: Dict):
        return Paciente(
            id=d.get("id"),
            nome=d.get("nome"),
            idade=d.get("idade"),
            telefone=d.get("telefone"),
            cpf=d.get("cpf", "")
        )