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
num_gen = (i for i in range(1, 1000000, 2) if is_prime(i))
"""
# Check if generated number's permutations are also primes.
for i in num_gen:
    cond = True
    i_str = str(i)
    i_list = list(permutations(i_str))
    for l in i_list:
        perm_str = ''
        for k in l:
            perm_str += k
        perm_num = int(perm_str)
        if is_prime(perm_num):
            cond = True
            continue
        else:
            cond = False
            break
    if cond:
        count += 1
"""        
# Check for primes in circular numbers.
for i in num_gen:
    cond = True
    i_str = str(i)
    for d in range(1, len(i_str)):
        i_str = i_str[1:]+i_str[0]
        cond = is_prime(int(i_str))
        if cond == False:
            break

    if cond:
        count += 1

end = time()

print("Finished in: ", end - start)
