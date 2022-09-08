# equation
def form(n, a, b):
    return n**2 + a * n + b

# check for prime function
def is_prime(p):
    for i in range(2, abs(p)):
        if abs(p) % i == 0:
            return False
    return True

# list of primes from -1000 up to 1000 for factor b (it must be a prime)
pr_list = [i for i in range(-1000, 1000) if is_prime(i)]

# dictionary of factor combinations and number of their consecutive primes initiated
list_dik = {}

# loop
for j in range(-1000, 1000):
    for k in pr_list:
        prk = str(j)+', '+str(k)
        counter = 0
        for i in range(100):
            if is_prime(form(i, j, k)):
                #print(i, j, k, form(i, j, k))
                counter += 1
                list_dik[prk] = counter
            else:
                break

# lists of keys and values
list_dik_k = list(list_dik.keys())
list_dik_v = list(list_dik.values())

# getting the maximum of prime list and printing coresponding key (factor combinations)
maks = max(list_dik_v)
print(maks, list_dik_k[list_dik_v.index(maks)])