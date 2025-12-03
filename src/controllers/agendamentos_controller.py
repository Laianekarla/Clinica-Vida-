from typing import List, Optional
from models.agendamento import Agendamento
from utils.storage import carregar_json, salvar_json
from controllers.pacientes_controller import obter_por_id as paciente_por_id

ARQ = "agendamento.json"

def _load_all() -> List[Agendamento]:
    raw = carregar_json(ARQ)
    return [Agendamento.from_dict(x) for x in raw]

def _save_all(ags: List[Agendamento]):
    salvar_json(ARQ, [a.to_dict() for a in ags])

def _next_id(ags: List[Agendamento]) -> int:
    if not ags:
        return 1
    return max(a.id for a in ags) + 1

def listar_agendamentos() -> List[Agendamento]:
    return _load_all()

def agendar_consulta(paciente_id: int, medico_id: int, data_hora: str, tipo: str) -> Optional[Agendamento]:
    if not paciente_por_id(paciente_id):
        return None
    ags = _load_all()
    nid = _next_id(ags)
    ag = Agendamento(id=nid, paciente_id=paciente_id, medico_id=medico_id,
                     data_hora=data_hora, tipo=tipo.upper(), confirmado=False)
    ags.append(ag)
    _save_all(ags)
    return ag

def confirmar_agendamento(aid: int) -> bool:
    ags = _load_all()
    for ag in ags:
        if ag.id == aid:
            ag.confirmado = True
            _save_all(ags)
            return True
    return False

def cancelar_agendamento(aid: int) -> bool:
    ags = _load_all()
    novos = [a for a in ags if a.id != aid]
    if len(novos) == len(ags):
        return False
    _save_all(novos)
    return True

def gerar_receita_por_agendamento(aid: int) -> Optional[str]:
    """
    Função para gerar receita, chamada somente pelo menu de médicos.
    Permite o médico adicionar observações / orientações para o paciente.
    Lazy import para evitar import circular.
    """
    from controllers.medicos_controller import obter_por_id as medico_por_id
    from utils.storage import carregar_json, salvar_json

    RECEITAS_ARQ = "receitas.json"

    ags = _load_all()
    ag = next((a for a in ags if a.id == aid), None)
    if not ag:
        return None

    paciente = paciente_por_id(ag.paciente_id)
    medico = medico_por_id(ag.medico_id)

    # Solicitar observações do médico
    observacoes = input("Digite observações / orientações médicas para o paciente: ").strip()

    texto = (
        f"--- RECEITA MÉDICA ---\n"
        f"Paciente: {paciente.nome if paciente else 'N/D'}\n"
        f"CPF: {getattr(paciente,'cpf','') if paciente else ''}\n"
        f"Médico: {medico.nome if medico else 'N/D'}\n"
        f"Data/Hora: {ag.data_hora}\n"
        f"Tipo: {ag.tipo}\n"
        f"Observações / Orientações: {observacoes}\n"
        f"Assinatura: ____\n"
    )

    # Salvar no arquivo receitas.json
    receitas = carregar_json(RECEITAS_ARQ)
    receitas.append({"agendamento_id": ag.id, "texto": texto})
    salvar_json(RECEITAS_ARQ, receitas)

    # Retorna o texto da receita para impressão
    return texto