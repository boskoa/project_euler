from time import time
from math import factorial

start = time()

suma = 0
suma_k = 0

faktorijali = {}

for k in range(10):
    faktorijali[str(k)] = factorial(k)

for i in range(3, 2000000):
    l = list(str(i))
    for d in l:
        suma += faktorijali[d]
    if i == suma:
        suma_k += i
    suma = 0
    
print(suma_k)    

end = time()

print("Finished in: ", end - start)