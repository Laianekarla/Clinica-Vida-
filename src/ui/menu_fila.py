def menu_fila():
    while True:
        print("\n--- MENU FILA DE ATENDIMENTO ---")
        print("1 - Ver Fila")
        print("2 - Inserir Paciente na Fila")
        print("3 - Atender Próximo")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            print("Ver fila - EM DESENVOLVIMENTO")
        elif opcao == "2":
            print("Inserir paciente na fila - EM DESENVOLVIMENTO")
        elif opcao == "3":
            print("Atender próximo - EM DESENVOLVIMENTO")
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")