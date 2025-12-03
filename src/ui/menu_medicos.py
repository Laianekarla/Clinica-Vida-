from controllers.agendamentos_controller import gerar_receita_por_agendamento
from controllers.medicos_controller import listar_medicos, cadastrar_medico

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
            # Cadastro de médico
            nome = input("Nome do médico: ").strip()
            especialidade = input("Especialidade: ").strip()
            m = cadastrar_medico(nome, especialidade)
            print(f"✅ Médico cadastrado com ID {m.id}!\n")
            
        elif opc == "2":
            # Listar médicos
            for m in listar_medicos():
                print(f"{m.id} - {m.nome} - {m.especialidade}")
            print()
            
        elif opc == "3":
            # Gerar receita
            try:
                aid = int(input("ID do agendamento para gerar receita: "))
            except ValueError:
                print("❌ ID inválido.\n")
                continue

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