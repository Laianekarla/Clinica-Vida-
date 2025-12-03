from dataclasses import dataclass, asdict
from typing import Dict

@dataclass
class Medico:
    id: int
    nome: str
    especialidade: str

    def to_dict(self) -> Dict:
        return asdict(self)

    @staticmethod
    def from_dict(d: Dict):
        return Medico(
            id=d.get("id"),
            nome=d.get("nome"),
            especialidade=d.get("especialidade", "")
        )