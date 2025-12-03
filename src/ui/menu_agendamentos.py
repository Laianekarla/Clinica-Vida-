from utils.validators import ler_int, ler_texto
from controllers.agendamentos_controller import (
    agendar_consulta, listar_agendamentos,
    confirmar_agendamento, cancelar_agendamento
)
from controllers.pacientes_controller import listar_pacientes
from controllers.medicos_controller import listar_medicos

def menu_agendamentos():
    while True:
        print("""
--- Agendamentos ---
1 - Cadastrar agendamento
2 - Listar agendamentos
3 - Confirmar agendamento
4 - Cancelar agendamento
0 - Voltar
""")
        opc = input("Escolha: ").strip()
        if opc == "1":
            print("Pacientes:")
            for p in listar_pacientes():
                print(f"{p.id} - {p.nome}")
            pid = ler_int("ID do paciente: ", minimo=1)
            print("Médicos:")
            for m in listar_medicos():
                print(f"{m.id} - {m.nome} - {m.especialidade}")
            mid = ler_int("ID do médico: ", minimo=1)
            data_hora = ler_texto("Data e hora (ex: 2025-12-10 14:00): ")
            tipo = ""
            while tipo not in ("NORMAL", "EMERGÊNCIA"):
                tipo = ler_texto("Tipo (NORMAL/EMERGÊNCIA): ").upper()
            ag = agendar_consulta(paciente_id=pid, medico_id=mid, data_hora=data_hora, tipo=tipo)
            if ag:
                print(f"✔ Agendamento criado com ID {ag.id}.\n")
        elif opc == "2":
            ags = listar_agendamentos()
            if not ags:
                print("Nenhum agendamento.\n")
            else:
                for a in ags:
                    print(f"{a.id} - Pac:{a.paciente_id} Med:{a.medico_id} {a.data_hora} Tipo:{a.tipo} Confirmado:{a.confirmado}")
        elif opc == "3":
            aid = ler_int("ID do agendamento para confirmar: ", minimo=1)
            ok = confirmar_agendamento(aid)
            print("✔ Agendamento confirmado.\n" if ok else "❌ Agendamento não encontrado.\n")
        elif opc == "4":
            aid = ler_int("ID do agendamento para cancelar: ", minimo=1)
            ok = cancelar_agendamento(aid)
            print("✔ Agendamento cancelado.\n" if ok else "❌ Agendamento não encontrado.\n")
        elif opc == "0":
            break
        else:
            print("❌ Opção inválida.\n")