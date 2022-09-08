lista = []
suma = 1
counter = 0
r = 2

for i in range(2001):
    lista.append(suma)
    suma += r
    counter += 1
    if counter == 4:
        r += 2
        counter = 0
    
print(sum(lista))