delioci = {}

for i in range(2, 10000):
    for j in range(1, i//2+1):
        if i % j == 0:
            if i not in delioci:
                delioci[i] = [j]
            else:
                delioci[i].append(j)

delioci_b = {key:sum(value) for key, value in delioci.items()}

suma = 0

for key, value in delioci_b.items():
    if delioci_b[key] == 1 or delioci_b[key] > 9999 or delioci_b[key] == key:
        pass
    elif delioci_b[delioci_b[key]] == key:
        suma += key
