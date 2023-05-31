from MOD import *
import random as r

lista = []
for i in range(1):
    c = ""
    for i in range(9):
        a = r.randint(0, 9)
        b = str(a)
        c += b
    e = contacpf(c)
    if int(e) > 9:
        e = 0
    d = c + str(e)
    g = contacpf2(d)
    if int(g) > 9:
        g = 0
    f = d + str(g)
    contador = 1
    for i in f:
        lista.append(i)
        if contador == 3 or contador == 6:
            lista.append(".")
        if contador == 9:
            lista.append("-")
        contador += 1
fim = ""
for i in lista:
    fim += i
print(fim)