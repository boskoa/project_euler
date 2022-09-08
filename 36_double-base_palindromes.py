from time import time
from math import factorial

start = time()

dec = []
for d in range(1, 1000000):
    d_o = list(str(d))
    if d_o[::-1] == d_o[:]:
        dec.append(''.join(d_o))
        
b_bin = [0 for i in range(19)]

def biny(n):
    if n == 0:
        return ''
    else:
        return biny(n//2) + str(n%2)

suma = 0
for d in dec:
    b = list(biny(int(d)))
    if b == b[::-1]:
        suma += int(d)
        print(d, suma)
        

end = time()

print("Finished in: ", end - start)
