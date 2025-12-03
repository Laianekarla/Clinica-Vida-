import json
import os

BASE_PATH = os.path.join(os.getcwd(), "src", "data")

def carregar_json(nome_arquivo):
    caminho = os.path.join(BASE_PATH, nome_arquivo)

    if not os.path.exists(caminho):
        return []

    with open(caminho, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def salvar_json(nome_arquivo, dados):
    caminho = os.path.join(BASE_PATH, nome_arquivo)

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)