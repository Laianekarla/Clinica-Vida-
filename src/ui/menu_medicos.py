from controllers.agendamentos_controller import gerar_receita_por_agendamento
from controllers.medicos_controller import listar_medicos

def menu_medicos():
    while True:
        print("""
--- Médicos ---
1 - Cadastrar médico
2 - Listar médicos
3 - Gerar receita para agendamento
0 - Voltar
""")
        opc = input("Escolha: ").strip()
        if opc == "1":
            # código de cadastro de médico
            pass
        elif opc == "2":
            for m in listar_medicos():
                print(f"{m.id} - {m.nome} - {m.especialidade}")
        elif opc == "3":
            aid = int(input("ID do agendamento para gerar receita: "))
            texto = gerar_receita_por_agendamento(aid)
            if texto:
                print(texto)
                print("[Receita salva em data/receitas.json]\n")
            else:
                print("❌ Agendamento não encontrado.\n")
        elif opc == "0":
            break
        else:
            print("❌ Opção inválida.\n")