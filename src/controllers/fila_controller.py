from typing import List, Dict
from utils.storage import carregar_json, salvar_json

ARQ = "fila.json"

def _load_fila() -> List[Dict]:
    """Carrega a fila do JSON."""
    return carregar_json(ARQ)

def _save_fila(fila: List[Dict]):
    """Salva a fila no JSON."""
    salvar_json(ARQ, fila)

def inserir_tres_pacientes(pacientes: List[Dict]):
    """
    Insere até 3 pacientes na fila.
    Cada paciente deve ser um dict com 'nome' e 'cpf'.
    """
    if len(pacientes) > 3:
        pacientes = pacientes[:3]
    fila = _load_fila()
    fila.extend(pacientes)
    _save_fila(fila)
    return True

def inserir_paciente_na_fila(nome: str, cpf: str):
    """Insere um paciente na fila."""
    fila = _load_fila()
    fila.append({"nome": nome, "cpf": cpf})
    _save_fila(fila)
    return True

def listar_fila() -> List[Dict]:
    """Retorna a lista de pacientes na fila."""
    return _load_fila()

def remover_primeiro() -> Dict:
    """Remove e retorna o primeiro paciente da fila."""
    fila = _load_fila()
    if not fila:
        return {}
    primeiro = fila.pop(0)
    _save_fila(fila)
    return primeiro