from ui.menu_pacientes import menu_pacientes
from ui.menu_medicos import menu_medicos
from ui.menu_agendamentos import menu_agendamentos
from ui.menu_estatisticas import menu_estatisticas
from ui.menu_fila import menu_fila

def menu_principal():
    while True:
        print("\n=== Clínica Vida+ ===")
        print("1. Pacientes")
        print("2. Médicos")
        print("3. Agendamentos")
        print("4. Estatísticas e Situações")
        print("5. Fila de Atendimento")
        print("0. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            menu_pacientes()
        elif opcao == "2":
            menu_medicos()
        elif opcao == "3":
            menu_agendamentos()
        elif opcao == "4":
            menu_estatisticas()
        elif opcao == "5":
            menu_fila()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")