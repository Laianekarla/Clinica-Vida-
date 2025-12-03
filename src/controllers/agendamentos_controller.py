from utils.storage import carregar_json, salvar_json
from models.agendamento import Agendamento

def gerar_id_agendamento():
    ag = carregar_json("agendamentos.json")
    return len(ag) + 1

def cadastrar_agendamento():
    cpf = input("CPF do Paciente: ")
    crm = input("CRM do Médico: ")
    tipo = input("Tipo (1 - Normal | 2 - Emergência): ")

    tipo = "Normal" if tipo == "1" else "Emergência"

    agendamentos = carregar_json("agendamentos.json")

    novo = Agendamento(gerar_id_agendamento(), cpf, crm, tipo)
    agendamentos.append(novo.to_dict())
    salvar_json("agendamentos.json", agendamentos)

    print("✅ Consulta agendada com sucesso!")

def listar_agendamentos():
    agendamentos = carregar_json("agendamentos.json")

    if not agendamentos:
        print("Nenhum agendamento encontrado.")
        return

    print("\n--- Lista de Agendamentos ---")
    for a in agendamentos:
        print(f"ID {a['id']} | Paciente {a['cpf_paciente']} | Médico {a['crm_medico']} | {a['tipo']} | {a['status']}")

import json
import os
from models.medico import Medico
from utils.storage import carregar_json, salvar_json

DATA_FILE = os.path.join("src", "data", "medicos.json")

def carregar_medicos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def salvar_medicos(medicos):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(medicos, file, indent=4, ensure_ascii=False)

# ✅ CADASTRAR
def cadastrar_medico():
    crm = input("CRM: ").strip()
    nome = input("Nome: ").strip()
    especialidade = input("Especialidade: ").strip()

    medicos = carregar_medicos()
    for m in medicos:
        if m["crm"] == crm:
            print("⚠️ Já existe um médico cadastrado com esse CRM!")
            return

    novo = Medico(crm, nome, especialidade)
    medicos.append(novo.to_dict())
    salvar_medicos(medicos)
    print("✅ Médico cadastrado com sucesso!")

# ✅ LISTAR
def listar_medicos():
    medicos = carregar_medicos()
    if not medicos:
        print("📭 Nenhum médico cadastrado!")
        return

    print("\n📋 Lista de Médicos:")
    for m in medicos:
        print(f"- {m['nome']} | CRM: {m['crm']} | Especialidade: {m['especialidade']}")

# ✅ BUSCAR
def buscar_medico():
    nome = input("Digite o nome do médico: ").strip().lower()
    medicos = carregar_medicos()
    encontrados = [m for m in medicos if nome in m["nome"].lower()]

    if not encontrados:
        print("❌ Nenhum médico encontrado!")
        return

    print("\n🔍 Resultados da busca:")
    for m in encontrados:
        print(f"{m['nome']} | CRM: {m['crm']} | Especialidade: {m['especialidade']}")

# ✅ EDITAR
def editar_medico():
    try:
        id_busca = int(input("Digite o ID do médico a ser editado: ").strip())
    except ValueError:
        print("❌ ID inválido!")
        return

    medicos = carregar_medicos()
    for m in medicos:
        if m.get("id") == id_busca:
            print(f"Editando: {m.get('nome')}")
            novo_nome = input("Novo nome (Enter para manter): ").strip()
            nova_esp = input("Nova especialidade (Enter para manter): ").strip()
            if novo_nome != "":
                m["nome"] = novo_nome
            if nova_esp != "":
                m["especialidade"] = nova_esp
            salvar_medicos(medicos)
            print("✅ Médico atualizado com sucesso!")
            return

    print("❌ Médico não encontrado!")

# ✅ EXCLUIR
def excluir_medico():
    try:
        id_busca = int(input("Digite o ID do médico a excluir: ").strip())
    except ValueError:
        print("❌ ID inválido!")
        return

    medicos = carregar_medicos()
    for m in medicos:
        if m.get("id") == id_busca:
            medicos.remove(m)
            salvar_medicos(medicos)
            print("🗑️ Médico excluído com sucesso!")
            return

    print("❌ Médico não encontrado!")

# ✅ CANCELAR AGENDAMENTO COMO MÉDICO (simulação)
def cancelar_agendamento_medico():
    try:
        id_medico = int(input("Digite seu ID de médico: ").strip())
    except ValueError:
        print("❌ ID inválido!")
        return

    agendamentos = carregar_json("agendamentos.json")
    meus_agendamentos = [a for a in agendamentos if a["medico_id"] == id_medico and a["status"] == "Agendado"]

    if not meus_agendamentos:
        print("❌ Nenhum agendamento ativo encontrado para este médico.")
        return

    print("\n📋 Seus agendamentos ativos:")
    for a in meus_agendamentos:
        print(f"ID Agendamento: {a['id']} | Paciente ID: {a['paciente_id']} | Início: {a['inicio']} | Fim: {a['fim']}")

    try:
        id_ag = int(input("Digite o ID do agendamento que deseja cancelar: ").strip())
    except ValueError:
        print("❌ ID inválido!")
        return

    for a in meus_agendamentos:
        if a["id"] == id_ag:
            a["status"] = "Cancelado"
            salvar_json("agendamentos.json", agendamentos)
            print("✅ Agendamento cancelado com sucesso!")
            return

    print("❌ Agendamento não encontrado.")

# ✅ GERAR RECEITA COMO MÉDICO (simulação)
def gerar_receita_medico():
    try:
        id_medico = int(input("Digite seu ID de médico: ").strip())
    except ValueError:
        print("❌ ID inválido!")
        return

    # Simulação: pedir informações do paciente e medicação
    id_paciente = input("Digite o ID do paciente: ").strip()
    medicacao = input("Digite a medicação prescrita: ").strip()
    dosagem = input("Digite a dosagem: ").strip()
    observacoes = input("Observações adicionais: ").strip()

    print("\n📝 Receita gerada com sucesso!")
    print(f"Médico ID: {id_medico}")
    print(f"Paciente ID: {id_paciente}")
    print(f"Medicação: {medicacao}")
    print(f"Dosagem: {dosagem}")
    print(f"Observações: {observacoes}")   
