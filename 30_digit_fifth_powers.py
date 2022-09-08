suma_k = 0
for i in range(2, 300000):
    suma = 0
    for j in str(i):
        suma += int(j)**5
    if i == suma:
        suma_k += i