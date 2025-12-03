from typing import List, Optional
from models.paciente import Paciente
from utils.storage import carregar_json, salvar_json

ARQ = "pacientes.json"

def _load_all() -> List[Paciente]:
    raw = carregar_json(ARQ)
    return [Paciente.from_dict(x) for x in raw]

def _save_all(pacientes: List[Paciente]):
    salvar_json(ARQ, [p.to_dict() for p in pacientes])

def _next_id(pacientes: List[Paciente]) -> int:
    if not pacientes:
        return 1
    return max(p.id for p in pacientes) + 1

def listar_pacientes() -> List[Paciente]:
    return _load_all()

def cadastrar_paciente(nome: str, idade: int, telefone: str, cpf: str = "") -> Paciente:
    pacientes = _load_all()
    nid = _next_id(pacientes)
    p = Paciente(id=nid, nome=nome, idade=idade, telefone=telefone, cpf=cpf)
    pacientes.append(p)
    _save_all(pacientes)
    return p

def buscar_por_nome(term: str) -> List[Paciente]:
    term_low = term.strip().lower()
    return [p for p in _load_all() if term_low in p.nome.lower()]

def obter_por_id(pid: int) -> Optional[Paciente]:
    for p in _load_all():
        if p.id == pid:
            return p
    return None

def remover_por_id(pid: int) -> bool:
    pacientes = _load_all()
    novos = [p for p in pacientes if p.id != pid]
    if len(novos) == len(pacientes):
        return False
    _save_all(novos)
    return True