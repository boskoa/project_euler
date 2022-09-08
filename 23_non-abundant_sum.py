from math import sqrt

delioci = []

# Funkcija za dobijanje delilaca.
def delioci(n):
    divs = [1]
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            divs.extend([i, int(n/i)])
    return sorted(list(set(divs)))

# Funkcija za odredjivanje abundantnog broja.
def abu(n):
    if n < sum(delioci(n)):
        return n
    else:
        pass
    
list_ab = [abu(i) for i in range(1, 28123) if abu(i)]
add_ab = set()

for i in list_ab:
    for j in list_ab:
        if i + j < 28124:
            add_ab.add(i+j)

print(add_ab)
suma = 0
for i in range(1, 28123):
    if i not in add_ab:
        suma += i

"""
    for j in range(2, int(sqrt(i)+1)):
        if i % j == 0:
            if i not in delioci:
                delioci[i] = [j]
            else:
                delioci[i].append(j)

# Suma delilaca.
delioci_b = {key:sum(value) for key, value in delioci.items()}

# Rečnik: suma delilaca > broj.
delioci_v = {}

# Selekcija brojeva koji imaju veću sumu delilaca od sebe samih.
for key, value in delioci_b.items():
    if value > key:
        delioci_v[key] = value
        
# Lista brojeva.
lista_b = [key for key in delioci_v.keys()]
"""
"""
lista_bb = lista_b[:]

# Lista zbirova.
lista_zb = []

for i in lista_b:
    for t in lista_bb:
        if i + t not in lista_zb:
            lista_zb.append(i+t)
        else:
            pass
    lista_bb.remove(i)
    
lista_zb.sort()
print(lista_zb)

suma_zb = 0

for r in range(1, 10000):
    if r not in lista_zb:
        print(r)
        suma_zb += r
"""