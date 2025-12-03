from typing import List, Optional
from models.medico import Medico
from utils.storage import carregar_json, salvar_json
from controllers.agendamentos_controller import gerar_receita_por_agendamento

ARQ = "medicos.json"

def _load_all() -> List[Medico]:
    raw = carregar_json(ARQ)
    return [Medico.from_dict(x) for x in raw]

def _save_all(meds: List[Medico]):
    salvar_json(ARQ, [m.to_dict() for m in meds])

def _next_id(meds: List[Medico]) -> int:
    if not meds:
        return 1
    return max(m.id for m in meds) + 1

def listar_medicos() -> List[Medico]:
    return _load_all()

def cadastrar_medico(nome: str, especialidade: str) -> Medico:
    meds = _load_all()
    nid = _next_id(meds)
    m = Medico(id=nid, nome=nome, especialidade=especialidade)
    meds.append(m)
    _save_all(meds)
    return m

def obter_por_id(mid: int) -> Optional[Medico]:
    meds = _load_all()
    return next((m for m in meds if m.id == mid), None)

def gerar_receita(aid: int) -> Optional[str]:
    """
    Chamando a função do agendamentos_controller.
    """
    return gerar_receita_por_agendamento(aid)