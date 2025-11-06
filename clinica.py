import os
import json
from os.path import exists
import re
from datetime import datetime, timedelta

# ---------- Arquivos ----------
ARQ_PACIENTES = "pacientes.json"
ARQ_MEDICOS = "medicos.json"
ARQ_AGENDAMENTOS = "agendamentos.json"

# ---------- Utilitários JSON ----------
def inicializar_arquivos():
    """Cria os arquivos JSON vazios se não existirem."""
    for caminho in (ARQ_PACIENTES, ARQ_MEDICOS, ARQ_AGENDAMENTOS):
        if not os.path.exists(caminho):
            with open(caminho, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=2)

def carregar_json(caminho):
    """Carrega lista do JSON — retorna lista vazia em erro."""
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_json(caminho, dados):
    """Salva lista no JSON (pretty print)."""
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

# ---------- Validações e formatação ----------
def apenas_numeros(texto):
    return re.sub(r"\D", "", texto or "")

def validar_telefone(telefone):
    t = apenas_numeros(telefone)
    # aceita 10 (fixo) ou 11 (celular) dígitos
    return bool(re.fullmatch(r"\d{10}|\d{11}", t))

def validar_cpf(cpf):
    c = apenas_numeros(cpf)
    if len(c) != 11 or c == c[0] * 11:
        return False
    for i in range(9, 11):
        soma = sum(int(c[num]) * ((i + 1) - num) for num in range(0, i))
        digito = (soma * 10 % 11) % 10
        if digito != int(c[i]):
            return False
    return True

def formatar_cpf(cpf):
    c = apenas_numeros(cpf)
    if len(c) == 11:
        return f"{c[0:3]}.{c[3:6]}.{c[6:9]}-{c[9:11]}"
    return cpf

def formatar_telefone(tel):
    t = apenas_numeros(tel)
    if len(t) == 10:
        return f"({t[0:2]}) {t[2:6]}-{t[6:10]}"
    if len(t) == 11:
        return f"({t[0:2]}) {t[2:7]}-{t[7:11]}"
    return tel

def input_nao_vazio(prompt):
    v = input(prompt).strip()
    while not v:
        print("Valor obrigatório. Tente novamente.")
        v = input(prompt).strip()
    return v

def gerar_id(lista):
    if not lista:
        return 1
    return max(item["id"] for item in lista) + 1

def parse_datetime(dt_str):
    try:
        return datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    except ValueError:
        return None

# ---------- Inicialização dos dados ----------
inicializar_arquivos()
pacientes = carregar_json(ARQ_PACIENTES)
medicos = carregar_json(ARQ_MEDICOS)
agendamentos = carregar_json(ARQ_AGENDAMENTOS)



# ---------- Funções Pacientes ----------
def cadastrar_paciente():
    print("\n--- Cadastrar Paciente ---")
    nome = input_nao_vazio("Nome: ")
    idade_s = input_nao_vazio("Idade: ")
    while not (idade_s.isdigit() and int(idade_s) > 0):
        print("Idade inválida.")
        idade_s = input_nao_vazio("Idade: ")
    idade = int(idade_s)

    cpf_raw = input("CPF (somente números): ").strip()
    while not validar_cpf(cpf_raw):
        print("CPF inválido. Digite novamente (11 dígitos).")
        cpf_raw = input("CPF (somente números): ").strip()
    cpf = apenas_numeros(cpf_raw)

    telefone = input("Telefone (opcional): ").strip()
    while telefone and not validar_telefone(telefone):
        print("Telefone inválido. Informe 10 ou 11 dígitos.")
        telefone = input("Telefone (opcional): ").strip()
    telefone = apenas_numeros(telefone)

    email = input("Email (opcional): ").strip()

    novo = {
        "id": gerar_id(pacientes),
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "telefone": telefone,
        "email": email
    }
    pacientes.append(novo)
    salvar_json(ARQ_PACIENTES, pacientes)
    print(f"✅ Paciente '{nome}' cadastrado (ID {novo['id']}).")

def listar_pacientes():
    print("\n--- Lista de Pacientes ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    print(f"Total de pacientes: {len(pacientes)}")
    for p in pacientes:
        print(f"ID {p['id']}: {p['nome']} | {p['idade']} anos | CPF: {formatar_cpf(p['cpf'])} | Tel: {formatar_telefone(p['telefone']) or 'N/A'}")

def buscar_paciente():
    termo = input("Buscar por nome ou CPF parcial: ").strip().lower()
    if not termo:
        print("Busca vazia.")
        return
    t_num = apenas_numeros(termo)
    resultados = [p for p in pacientes if termo in p["nome"].lower() or (t_num and t_num in p["cpf"])]
    if not resultados:
        print("Nenhum paciente encontrado.")
        return
    for p in resultados:
        print(f"ID {p['id']}: {p['nome']} | {p['idade']} anos | CPF: {formatar_cpf(p['cpf'])}")

def editar_paciente():
    listar_pacientes()
    id_s = input("ID do paciente para editar: ").strip()
    if not id_s.isdigit():
        print("ID inválido.")
        return
    idn = int(id_s)
    p = next((x for x in pacientes if x["id"] == idn), None)
    if not p:
        print("Paciente não encontrado.")
        return
    print(f"Editando {p['nome']} (Enter mantém valor atual)")
    novo_nome = input(f"Nome [{p['nome']}]: ").strip() or p['nome']
    idade_s = input(f"Idade [{p['idade']}]: ").strip() or str(p['idade'])
    while not (idade_s.isdigit() and int(idade_s) > 0):
        print("Idade inválida.")
        idade_s = input(f"Idade [{p['idade']}]: ").strip() or str(p['idade'])
    novo_idade = int(idade_s)
    cpf_raw = input(f"CPF [{formatar_cpf(p['cpf'])}]: ").strip() or p['cpf']
    while not validar_cpf(cpf_raw):
        print("CPF inválido.")
        cpf_raw = input(f"CPF [{formatar_cpf(p['cpf'])}]: ").strip() or p['cpf']
    novo_cpf = apenas_numeros(cpf_raw)
    tel_raw = input(f"Telefone [{formatar_telefone(p['telefone']) or 'N/A'}]: ").strip() or p['telefone']
    while tel_raw and not validar_telefone(tel_raw):
        print("Telefone inválido.")
        tel_raw = input(f"Telefone [{formatar_telefone(p['telefone']) or 'N/A'}]: ").strip() or p['telefone']
    novo_tel = apenas_numeros(tel_raw)
    novo_email = input(f"Email [{p.get('email','')}]: ").strip() or p.get('email','')

    p.update({
        "nome": novo_nome,
        "idade": novo_idade,
        "cpf": novo_cpf,
        "telefone": novo_tel,
        "email": novo_email
    })
    salvar_json(ARQ_PACIENTES, pacientes)
    print("✅ Paciente atualizado.")

def excluir_paciente():
    listar_pacientes()
    id_s = input("ID do paciente para excluir: ").strip()
    if not id_s.isdigit():
        print("ID inválido.")
        return
    idn = int(id_s)
    p = next((x for x in pacientes if x["id"] == idn), None)
    if not p:
        print("Paciente não encontrado.")
        return
    confirm = input(f"Confirmar exclusão de {p['nome']}? (s/n): ").strip().lower()
    if confirm == "s":
        global agendamentos
        agendamentos = [a for a in agendamentos if a["paciente_id"] != idn]
        salvar_json(ARQ_AGENDAMENTOS, agendamentos)
        pacientes.remove(p)
        salvar_json(ARQ_PACIENTES, pacientes)
        print("✅ Paciente excluído.")
    else:
        print("Operação cancelada.")

# ---------- Funções Médicos (simples) ----------
def cadastrar_medico():
    print("\n--- Cadastrar Médico (simples) ---")
    nome = input_nao_vazio("Nome do médico: ")
    especialidade = input_nao_vazio("Especialidade: ")
    crm = input_nao_vazio("CRM: ")
    novo = {
        "id": gerar_id(medicos),
        "nome": nome,
        "especialidade": especialidade,
        "crm": crm
    }
    medicos.append(novo)
    salvar_json(ARQ_MEDICOS, medicos)
    print(f"✅ Médico '{nome}' cadastrado (ID {novo['id']}).")

def listar_medicos():
    print("\n--- Lista de Médicos ---")
    if not medicos:
        print("Nenhum médico cadastrado.")
        return
    for m in medicos:
        print(f"ID {m['id']}: {m['nome']} | {m['especialidade']} | CRM: {m['crm']}")

def buscar_medico():
    termo = input("Buscar médico por nome ou CRM: ").strip().lower()
    if not termo:
        print("Busca vazia.")
        return
    resultados = [m for m in medicos if termo in m["nome"].lower() or termo in m["crm"].lower()]
    if not resultados:
        print("Nenhum médico encontrado.")
        return
    for m in resultados:
        print(f"ID {m['id']}: {m['nome']} | {m['especialidade']} | CRM: {m['crm']}")

def editar_medico():
    listar_medicos()
    id_s = input("ID do médico para editar: ").strip()
    if not id_s.isdigit():
        print("ID inválido.")
        return
    idn = int(id_s)
    m = next((x for x in medicos if x["id"] == idn), None)
    if not m:
        print("Médico não encontrado.")
        return
    novo_nome = input(f"Nome [{m['nome']}]: ").strip() or m['nome']
    nova_esp = input(f"Especialidade [{m['especialidade']}]: ").strip() or m['especialidade']
    novo_crm = input(f"CRM [{m['crm']}]: ").strip() or m['crm']
    m.update({"nome": novo_nome, "especialidade": nova_esp, "crm": novo_crm})
    salvar_json(ARQ_MEDICOS, medicos)
    print("✅ Médico atualizado.")

def excluir_medico():
    listar_medicos()
    id_s = input("ID do médico para excluir: ").strip()
    if not id_s.isdigit():
        print("ID inválido.")
        return
    idn = int(id_s)
    m = next((x for x in medicos if x["id"] == idn), None)
    if not m:
        print("Médico não encontrado.")
        return
    confirm = input(f"Confirmar exclusão de {m['nome']}? (s/n): ").strip().lower()
    if confirm == "s":
        global agendamentos
        agendamentos = [a for a in agendamentos if a["medico_id"] != idn]
        salvar_json(ARQ_AGENDAMENTOS, agendamentos)
        medicos.remove(m)
        salvar_json(ARQ_MEDICOS, medicos)
        print("✅ Médico excluído.")
    else:
        print("Operação cancelada.")

# ---------- Agendamentos ----------
def agendar_consulta():
    print("\n--- Agendar Consulta ---")
    if not pacientes or not medicos:
        print("Cadastre pacientes e médicos antes de agendar.")
        return
    listar_pacientes()
    pid_s = input("ID do paciente: ").strip()
    if not pid_s.isdigit():
        print("ID inválido.")
        return
    pid = int(pid_s)
    paciente = next((p for p in pacientes if p["id"] == pid), None)
    if not paciente:
        print("Paciente não encontrado.")
        return

    listar_medicos()
    mid_s = input("ID do médico: ").strip()
    if not mid_s.isdigit():
        print("ID inválido.")
        return
    mid = int(mid_s)
    medico = next((m for m in medicos if m["id"] == mid), None)
    if not medico:
        print("Médico não encontrado.")
        return

    dt_in = input("Data e hora (YYYY-MM-DD HH:MM): ").strip()
    dt = parse_datetime(dt_in)
    if not dt:
        print("Formato inválido.")
        return
    if dt < datetime.now():
        print("Não é possível agendar em data/hora passada.")
        return

    dur_min = input("Duração em minutos (padrão 30): ").strip()
    dur = int(dur_min) if dur_min.isdigit() else 30
    dt_fim = dt + timedelta(minutes=dur)

    # checar conflito
    conflitos = []
    for a in agendamentos:
        if a["medico_id"] != mid or a["status"] != "agendada":
            continue
        a_inicio = parse_datetime(a["inicio"])
        a_fim = parse_datetime(a["fim"])
        if (dt < a_fim) and (dt_fim > a_inicio):
            conflitos.append(a)
    if conflitos:
        print("❌ Conflito de horário com consultas já agendadas para esse médico:")
        for c in conflitos:
            p = next((x for x in pacientes if x["id"] == c["paciente_id"]), {"nome": "?"})
            print(f"- {c['inicio']} -> {c['fim']} | Paciente: {p.get('nome')}")
        return

    novo = {
        "id": gerar_id(agendamentos),
        "paciente_id": pid,
        "medico_id": mid,
        "inicio": dt.strftime("%Y-%m-%d %H:%M"),
        "fim": dt_fim.strftime("%Y-%m-%d %H:%M"),
        "duracao_min": dur,
        "status": "agendada"
    }
    agendamentos.append(novo)
    salvar_json(ARQ_AGENDAMENTOS, agendamentos)
    print(f"✅ Consulta agendada (ID {novo['id']}) em {novo['inicio']}")

def listar_agendamentos():
    print("\n--- Agendamentos ---")
    if not agendamentos:
        print("Nenhum agendamento.")
        return
    for a in sorted(agendamentos, key=lambda x: x["inicio"]):
        p = next((x for x in pacientes if x["id"] == a["paciente_id"]), {"nome":"?"})
        m = next((x for x in medicos if x["id"] == a["medico_id"]), {"nome":"?"})
        print(f"ID {a['id']}: {a['inicio']} -> {a['fim']} | Médico: {m['nome']} | Paciente: {p['nome']} | Status: {a['status']}")

def buscar_agendamento():
    termo = input("Buscar por ID do agendamento (ou parte da data YYYY-MM-DD): ").strip()
    if not termo:
        print("Busca vazia.")
        return
    resultados = []
    if termo.isdigit():
        idn = int(termo)
        resultados = [a for a in agendamentos if a["id"] == idn]
    else:
        resultados = [a for a in agendamentos if termo in a["inicio"]]
    if not resultados:
        print("Nenhum agendamento encontrado.")
        return
    for a in resultados:
        p = next((x for x in pacientes if x["id"] == a["paciente_id"]), {"nome":"?"})
        m = next((x for x in medicos if x["id"] == a["medico_id"]), {"nome":"?"})
        print(f"ID {a['id']}: {a['inicio']} -> {a['fim']} | Médico: {m['nome']} | Paciente: {p['nome']} | Status: {a['status']}")

# ---------- Relatórios / Estatísticas ----------
def estatisticas_gerais():
    print("\n--- Estatísticas Gerais ---")
    total_p = len(pacientes)
    total_m = len(medicos)
    total_a = len([a for a in agendamentos if a["status"]=="agendada"])
    print(f"Pacientes: {total_p}")
    print(f"Médicos: {total_m}")
    print(f"Agendamentos ativos: {total_a}")

    if total_p > 0:
        idades = [p["idade"] for p in pacientes if isinstance(p.get("idade"), int)]
        media = sum(idades) / len(idades) if idades else 0
        mais_novo = min(pacientes, key=lambda x: x.get("idade", 999999))
        mais_velho = max(pacientes, key=lambda x: x.get("idade", -1))
        print(f"Idade média dos pacientes: {media:.1f} anos")
        print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
        print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")

# ---------- Menus ----------
def menu_principal():
    print("\n=== SISTEMA CLÍNICA VIDA+ ===")
    print("1. Pacientes")
    print("2. Médicos")
    print("3. Agendamentos")
    print("4. Estatísticas gerais")
    print("5. Sair")

def menu_pacientes():
    print("\n--- Menu Pacientes ---")
    print("1. Cadastrar paciente")
    print("2. Buscar paciente")
    print("3. Listar pacientes")
    print("4. Editar paciente")
    print("5. Excluir paciente")
    print("6. Voltar")

def menu_medicos():
    print("\n--- Menu Médicos ---")
    print("1. Cadastrar médico")
    print("2. Buscar médico")
    print("3. Listar médicos")
    print("4. Editar médico")
    print("5. Excluir médico")
    print("6. Voltar")

def menu_agendamentos():
    print("\n--- Menu Agendamentos ---")
    print("1. Criar agendamento")
    print("2. Buscar agendamento")
    print("3. Listar agendamentos")
    print("4. Cancelar agendamento")
    print("5. Voltar")

    

# ---------- Loop principal ----------
def main():
    global pacientes, medicos, agendamentos
    pacientes = carregar_json(ARQ_PACIENTES)
    medicos = carregar_json(ARQ_MEDICOS)
    agendamentos = carregar_json(ARQ_AGENDAMENTOS)
    while True:
        menu_principal()
        escolha = input("Escolha: ").strip()
        if escolha == "1":
            while True:
                menu_pacientes()
                op = input("Opção Pacientes: ").strip()
                if op == "1":
                    cadastrar_paciente()
                elif op == "2":
                    buscar_paciente()
                elif op == "3":
                    listar_pacientes()
                elif op == "4":
                    editar_paciente()
                elif op == "5":
                    excluir_paciente()
                elif op == "6":
                    break
                else:
                    print("Opção inválida.")
        elif escolha == "2":
            while True:
                menu_medicos()
                op = input("Opção Médicos: ").strip()
                if op == "1":
                    cadastrar_medico()
                elif op == "2":
                    buscar_medico()
                elif op == "3":
                    listar_medicos()
                elif op == "4":
                    editar_medico()
                elif op == "5":
                    excluir_medico()
                elif op == "6":
                    break
                else:
                    print("Opção inválida.")
        elif escolha == "3":
            while True:
                menu_agendamentos()
                op = input("Opção Agendamentos: ").strip()
                if op == "1":
                    agendar_consulta()
                elif op == "2":
                    buscar_agendamento()
                elif op == "3":
                    listar_agendamentos()
                elif op == "4":
                    cancelar_agendamento()
                elif op == "5":
                    break
                else:
                    print("Opção inválida.")
        elif escolha == "4":
            estatisticas_gerais()
        elif escolha == "5":
            salvar_json(ARQ_PACIENTES, pacientes)
            salvar_json(ARQ_MEDICOS, medicos)
            salvar_json(ARQ_AGENDAMENTOS, agendamentos)
            print("Saindo... dados salvos.")
            break
        else:
            print("Escolha inválida.")

if __name__ == "__main__":
    main()