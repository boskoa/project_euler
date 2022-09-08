from time import time
from math import factorial, sqrt
from itertools import permutations

start = time()

count = 0
# Check primality function (faster).
def is_prime(n):
    for i in range(2, int(sqrt(n))+2):
        if n % i == 0:
            return False
    return True

# Generate prime numbers up to 1 million.
num_gen = (i for i in range(3, 1000000, 2) if is_prime(i))
       
sum_tr = 0

dict_p = {}

dict_p[2] = '2'

for i in num_gen:
    dict_p[i] = str(i)
    
for k, v in dict_p.items():
    if k > 20:
        cond = True
        vd = v
        vl = v
        for t in range(1, len(v)):
            vd = vd[0:-1]
            if int(vd) not in dict_p:
                cond = False
                break
                
        for q in range(1, len(v)):
            vl = vl[1:]
            if int(vl) not in dict_p:
                cond = False
                break
                
        if cond:
            count += 1
            sum_tr += k

end = time()

print("Finished in: ", end - start)
