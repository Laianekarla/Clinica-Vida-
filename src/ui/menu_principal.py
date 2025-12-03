from ui.menu_pacientes import menu_pacientes
from ui.menu_medicos import menu_medicos
from ui.menu_agendamentos import menu_agendamentos
from ui.menu_fila import menu_fila
from ui.menu_estatisticas import menu_estatisticas

def menu_principal():
    while True:
        print("""
===== CLÍNICA VIDA+ =====
1 - Pacientes
2 - Médicos
3 - Agendamentos
4 - Fila de atendimento
5 - Estatísticas / Regras lógicas
0 - Sair
""")
        opc = input("Escolha: ").strip()
        if opc == "1":
            menu_pacientes()
        elif opc == "2":
            menu_medicos()
        elif opc == "3":
            menu_agendamentos()
        elif opc == "4":
            menu_fila()
        elif opc == "5":
            menu_estatisticas()
        elif opc == "0":
            print("Saindo... até logo!")
            break
        else:
            print("Opção inválida.")