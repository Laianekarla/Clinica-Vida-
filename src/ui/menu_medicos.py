from controllers.medicos_controller import (
    cadastrar_medico,
    buscar_medico,
    listar_medicos,
    editar_medico,
    excluir_medico,
    cancelar_agendamento_medico,
    gerar_receita_medico
)

def menu_medicos():
    while True:
        print("\n--- MENU MÉDICOS ---")
        print("1 - Cadastrar Médico")
        print("2 - Buscar Médico")
        print("3 - Listar Médicos")
        print("4 - Editar Médico")
        print("5 - Excluir Médico")
        print("6 - Cancelar Agendamento como Médico")
        print("7 - Gerar Receita como Médico")
        print("0 - Voltar")

        escolha = input("Escolha: ").strip()

        if escolha == "1":
            cadastrar_medico()
        elif escolha == "2":
            buscar_medico()
        elif escolha == "3":
            listar_medicos()
        elif escolha == "4":
            editar_medico()
        elif escolha == "5":
            excluir_medico()
        elif escolha == "6":
            cancelar_agendamento_medico()
        elif escolha == "7":
            gerar_receita_medico()
        elif escolha == "0":
            break
        else:
            print("❌ Opção inválida! Tente novamente.")