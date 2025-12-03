from utils.validators import ler_texto
from controllers.fila_controller import inserir_tres_pacientes, inserir_paciente_na_fila, listar_fila, remover_primeiro

def menu_fila():
    while True:
        print("""
--- Fila de atendimento ---
1 - Inserir 3 pacientes na fila
2 - Inserir 1 paciente manualmente
3 - Chamar próximo da fila (remover)
4 - Mostrar fila atual
0 - Voltar
""")
        opc = input("Escolha: ").strip()
        if opc == "1":
            lista = []
            for i in range(1,4):
                nome = ler_texto(f"Nome paciente {i}: ")
                cpf = ler_texto(f"CPF paciente {i}: ")
                lista.append({"nome": nome, "cpf": cpf})
            inserir_tres_pacientes(lista)
            print("3 pacientes adicionados à fila.")
        elif opc == "2":
            nome = ler_texto("Nome: ")
            cpf = ler_texto("CPF: ")
            inserir_paciente_na_fila(nome, cpf)
            print("Paciente adicionado à fila.")
        elif opc == "3":
            p = remover_primeiro()
            if not p:
                print("Fila vazia.")
            else:
                print(f"Atendendo: {p['nome']} - CPF: {p['cpf']}")
        elif opc == "4":
            fila = listar_fila()
            if not fila:
                print("Fila vazia.")
            else:
                for idx, it in enumerate(fila, start=1):
                    print(f"{idx}. {it['nome']} - CPF: {it['cpf']}")
        elif opc == "0":
            break
        else:
            print("Opção inválida.")