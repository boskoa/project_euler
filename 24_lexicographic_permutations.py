import itertools

lista = [i for i in range(10)]

perm = list(itertools.permutations(lista))

print(perm[999999])