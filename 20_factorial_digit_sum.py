def fak(n, pr=1):
    for i in range(1, n+1):
        pr *= i
        yield pr

lista = [i for i in fak(100)]
lista_fak = list(str(lista[-1]))
suma = 0
for i in lista_fak:
    suma += int(i)
    