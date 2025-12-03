from controllers.pacientes_controller import (
    cadastrar_paciente,
    buscar_paciente,
    listar_pacientes,
    editar_paciente,
    excluir_paciente,
    estatisticas_pacientes
)

def menu_pacientes():
    while True:
        print("\n--- MENU PACIENTES ---")
        print("1 - Cadastrar Paciente")
        print("2 - Buscar Paciente")
        print("3 - Listar Pacientes")
        print("4 - Editar Paciente")
        print("5 - Excluir Paciente")
        print("6 - Estatísticas dos Pacientes")
        print("0 - Voltar")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            buscar_paciente()
        elif opcao == "3":
            listar_pacientes()
        elif opcao == "4":
            editar_paciente()
        elif opcao == "5":
            excluir_paciente()
        elif opcao == "6":
            estatisticas_pacientes()
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida!")