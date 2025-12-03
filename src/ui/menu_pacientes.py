from controllers.pacientes_controller import listar_pacientes, cadastrar_paciente, buscar_por_nome, obter_por_id
from utils.storage import carregar_json
from utils.storage import BASE_PATH
from utils import storage
from utils.storage import carregar_json as _carregar
from utils.storage import salvar_json as _salvar

def menu_pacientes():
    while True:
        print("""
--- Pacientes ---
1 - Cadastrar paciente
2 - Listar pacientes
3 - Buscar paciente por nome
4 - Voltar
""")
        opc = input("Escolha: ").strip()
        if opc == "1":
            nome = input("Nome do paciente: ").strip()
            try:
                idade = int(input("Idade: ").strip())
            except ValueError:
                print("Idade inválida.")
                continue
            telefone = input("Telefone: ").strip()
            cpf = input("CPF (opcional): ").strip()
            p = cadastrar_paciente(nome=nome, idade=idade, telefone=telefone, cpf=cpf)
            print(f"Paciente cadastrado com ID {p.id}.")
        elif opc == "2":
            todos = listar_pacientes()
            if not todos:
                print("Nenhum paciente cadastrado.")
            else:
                print("Lista de pacientes:")
                for p in todos:
                    print(f"ID: {p.id} | Nome: {p.nome} | Idade: {p.idade} | Telefone: {p.telefone} | CPF: {p.cpf}")
        elif opc == "3":
            termo = input("Nome (ou parte): ").strip()
            encontrados = buscar_por_nome(termo)
            if not encontrados:
                print("Nenhum paciente encontrado.")
            else:
                for p in encontrados:
                    print(f"ID: {p.id} | Nome: {p.nome} | Idade: {p.idade} | Telefone: {p.telefone} | CPF: {p.cpf}")
        elif opc == "4":
            break
        else:
            print("Opção inválida.")