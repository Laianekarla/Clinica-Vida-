from controllers.pacientes_controller import listar_pacientes
from controllers.logica_controller import (
    tabela_verdade_consulta_normal, tabela_verdade_emergencia,
    contar_casos_validos_consulta_normal, contar_casos_validos_emergencia,
    consulta_normal, emergencia
)

def menu_estatisticas():
    while True:
        print("""
--- Estatísticas / Lógica ---
1 - Mostrar estatísticas simples (total, média, mais novo/velho)
2 - Tabela verdade - Consulta Normal (16 linhas)
3 - Tabela verdade - Emergência (16 linhas)
4 - Contagens de casos válidos (ambas)
5 - Análise caso prático (A=F,B=V,C=V,D=F)
0 - Voltar
""")
        opc = input("Escolha: ").strip()
        pacientes = listar_pacientes()
        if opc == "1":
            total = len(pacientes)
            print(f"Total de pacientes: {total}")
            if total > 0:
                idades = [p.idade for p in pacientes]
                media = sum(idades)/len(idades)
                mais_novo = min(pacientes, key=lambda x: x.idade)
                mais_velho = max(pacientes, key=lambda x: x.idade)
                print(f"Idade média: {media:.2f}")
                print(f"Mais novo: {mais_novo.nome} - {mais_novo.idade} anos")
                print(f"Mais velho: {mais_velho.nome} - {mais_velho.idade} anos")
        elif opc == "2":
            linhas = tabela_verdade_consulta_normal()
            print("A B C D | ConsultaNormal")
            for r in linhas:
                print(f"{r[0]} {r[1]} {r[2]} {r[3]} | {r[4]}")
        elif opc == "3":
            linhas = tabela_verdade_emergencia()
            print("A B C D | Emergência")
            for r in linhas:
                print(f"{r[0]} {r[1]} {r[2]} {r[3]} | {r[4]}")
        elif opc == "4":
            cn = contar_casos_validos_consulta_normal()
            em = contar_casos_validos_emergencia()
            print(f"Consulta Normal: {cn} de 16")
            print(f"E mergência: {em} de 16")
        elif opc == "5":
            A,B,C,D = False, True, True, False
            print("Caso prático: A=F B=V C=V D=F")
            print("Consulta Normal?", "SIM" if consulta_normal(A,B,C,D) else "NÃO")
            print("Emergência?", "SIM" if emergencia(A,B,C,D) else "NÃO")
        elif opc == "0":
            break
        else:
            print("Opção inválida.")