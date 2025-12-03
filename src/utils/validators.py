def ler_int(msg, minimo=None, maximo=None):
    """
    Lê um número inteiro do usuário.
    Permite definir valores mínimos e máximos.
    """
    while True:
        try:
            valor = int(input(msg))
            if minimo is not None and valor < minimo:
                print(f"⚠️ O valor deve ser no mínimo {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"⚠️ O valor deve ser no máximo {maximo}.")
                continue
            return valor
        except ValueError:
            print("⚠️ Digite um número inteiro válido.")


def ler_texto(msg, obrigatorio=True):
    """
    Lê um texto do usuário.
    Se obrigatorio=True, não aceita vazio.
    """
    while True:
        texto = input(msg).strip()
        if obrigatorio and not texto:
            print("⚠️ Este campo é obrigatório.")
            continue
        return texto


def ler_texto(msg):
    while True:
        texto = input(msg).strip()
        if texto == "":
            print("⚠️ O campo não pode ficar vazio.")
        else:
            return texto


def ler_opcao(msg, opcoes_validas):
    """
    Lê uma opção garantindo que esteja no conjunto permitido.
    Ex: ler_opcao("Escolha [S/N]: ", ["S", "N"])
    """
    while True:
        valor = input(msg).strip().upper()
        if valor in opcoes_validas:
            return valor
        print(f"⚠️ Opção inválida! As opções válidas são: {opcoes_validas}")