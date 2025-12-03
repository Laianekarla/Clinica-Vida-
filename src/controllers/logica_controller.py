from typing import List, Tuple

def consulta_normal(A: bool, B: bool, C: bool, D: bool) -> bool:
    return (A and B and C) or (B and C and D)

def emergencia(A: bool, B: bool, C: bool, D: bool) -> bool:
    return C and (B or D)

def tabela_verdade_consulta_normal() -> List[Tuple[int,int,int,int,int]]:
    linhas = []
    for A in (0,1):
        for B in (0,1):
            for C in (0,1):
                for D in (0,1):
                    res = consulta_normal(bool(A), bool(B), bool(C), bool(D))
                    linhas.append((A,B,C,D,int(res)))
    return linhas

def tabela_verdade_emergencia() -> List[Tuple[int,int,int,int,int]]:
    linhas = []
    for A in (0,1):
        for B in (0,1):
            for C in (0,1):
                for D in (0,1):
                    res = emergencia(bool(A), bool(B), bool(C), bool(D))
                    linhas.append((A,B,C,D,int(res)))
    return linhas

def contar_casos_validos_consulta_normal() -> int:
    return sum(row[4] for row in tabela_verdade_consulta_normal())

def contar_casos_validos_emergencia() -> int:
    return sum(row[4] for row in tabela_verdade_emergencia())