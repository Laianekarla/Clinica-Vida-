import json
import os
from models.paciente import Paciente

DATA_FILE = os.path.join("src", "data", "pacientes.json")

def carregar_pacientes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def salvar_pacientes(pacientes):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(pacientes, file, indent=4, ensure_ascii=False)

# ✅ CADASTRAR
def cadastrar_paciente():
    cpf = input("CPF: ").strip()
    nome = input("Nome: ").strip()
    idade = input("Idade: ").strip()

    pacientes = carregar_pacientes()

    for paciente in pacientes:
        if paciente["cpf"] == cpf:
            print("⚠️ Já existe um paciente cadastrado com esse CPF!")
            return

    novo = Paciente(cpf, nome, idade)
    pacientes.append(novo.to_dict())
    salvar_pacientes(pacientes)

    print("✅ Paciente cadastrado com sucesso!")

# ✅ LISTAR
def listar_pacientes():
    pacientes = carregar_pacientes()
    if not pacientes:
        print("📭 Nenhum paciente cadastrado!")
        return

    print("\n📋 Lista de Pacientes:")
    for p in pacientes:
        print(f"- {p['nome']} | CPF: {p['cpf']} | Idade: {p['idade']}")

# ✅ BUSCAR
def buscar_paciente():
    nome = input("Digite o nome do paciente: ").strip().lower()
    pacientes = carregar_pacientes()

    encontrados = [p for p in pacientes if nome in p["nome"].lower()]

    if not encontrados:
        print("❌ Nenhum paciente encontrado!")
        return

    print("\n🔍 Resultados da busca:")
    for p in encontrados:
        print(f"{p['nome']} | CPF: {p['cpf']} | Idade: {p['idade']}")

# ✅ EDITAR
def editar_paciente():
    cpf = input("Digite o CPF do paciente a ser editado: ").strip()
    pacientes = carregar_pacientes()

    for p in pacientes:
        if p["cpf"] == cpf:
            print(f"Editando: {p['nome']}")
            novo_nome = input("Novo nome (Enter para manter): ").strip()
            nova_idade = input("Nova idade (Enter para manter): ").strip()

            if novo_nome != "":
                p["nome"] = novo_nome
            if nova_idade != "":
                p["idade"] = nova_idade

            salvar_pacientes(pacientes)
            print("✅ Paciente atualizado com sucesso!")
            return

    print("❌ Paciente não encontrado!")

# ✅ EXCLUIR
def excluir_paciente():
    cpf = input("Digite o CPF do paciente a excluir: ").strip()
    pacientes = carregar_pacientes()

    for p in pacientes:
        if p["cpf"] == cpf:
            pacientes.remove(p)
            salvar_pacientes(pacientes)
            print("🗑️ Paciente excluído com sucesso!")
            return

    print("❌ Paciente não encontrado!")

# ✅ ESTATÍSTICAS
def estatisticas_pacientes():
    pacientes = carregar_pacientes()
    if not pacientes:
        print("📭 Nenhum paciente cadastrado!")
        return

    total = len(pacientes)
    idades = [int(p["idade"]) for p in pacientes]
    media = sum(idades) / total
    mais_novo = min(pacientes, key=lambda x: int(x["idade"]))
    mais_velho = max(pacientes, key=lambda x: int(x["idade"]))

    print("\n📊 Estatísticas da Clínica:")
    print(f"👥 Total de pacientes: {total}")
    print(f"📈 Idade média: {media:.1f} anos")
    print(f"🧒 Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"👴 Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")