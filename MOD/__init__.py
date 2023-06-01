import random as r
def contacpf(a = ""):

    contador = 10
    saida = 0
    for i in a:
        troca = int(i)
        total = contador * troca
        saida += total
        contador -= 1
    conta = (saida * 10) % 11
    return conta
def contacpf2(a = ""):
    contador = 11
    saida = 0
    for i in a:
        troca = int(i)
        total = contador * troca
        saida += total
        contador -= 1
    conta = (saida * 10) % 11
    return conta

def linha(a = 0):
    print(f"\033[1;{a}m-=\033[m" * 20)
def cabeçalho(a = "TEXTO"):
    print(f"\033[1m{a.center(40)}\033[m")
def texto(a = "TEXTO"):
    linha(32)
    cabeçalho(a)
    linha(35)
