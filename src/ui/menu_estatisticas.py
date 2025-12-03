def menu_estatisticas():
    while True:
        print("\n--- MENU ESTATÍSTICAS & SITUAÇÕES ---")
        print("1 - Estatísticas Gerais")
        print("2 - Regras Lógicas e Análise")
        print("3 - Tabelas Verdade")
        print("4 - Situação Prática do Paciente")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            print("Estatísticas gerais - EM DESENVOLVIMENTO")
        elif opcao == "2":
            print("Regras lógicas - EM DESENVOLVIMENTO")
        elif opcao == "3":
            print("Tabelas verdade - EM DESENVOLVIMENTO")
        elif opcao == "4":
            print("Situação prática - EM DESENVOLVIMENTO")
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")