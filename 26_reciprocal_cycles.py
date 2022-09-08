def decimals(i):
    lista_decimala = []
    lista_ostataka = []
    d = 1
    o = 0
    oi = 0
    while True:
        o = (d * 10) % i
        if d == 0:
            break
        elif d in lista_ostataka:
            oi = lista_ostataka.index(d)
            return lista_decimala[oi:]
        lista_decimala.append((d*10)//i)
        lista_ostataka.append(d)
        d = o

lista = {}
for i in range(2, 1000):
    if type(decimals(i)) == type([1]):
        lista[i] = decimals(i)

lista_v = []
lista_k = []
for k, v in lista.items():
    lista_v.append(len(v))
    lista_k.append(k)
    
najduži = lista_v.index(max(lista_v))
print(lista_k[najduži])
