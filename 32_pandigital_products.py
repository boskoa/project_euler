from time import time

start = time()

lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
r = {}
for i in range(1, 100):
    for j in range(100, 5000):
        lis = list(str(i)+str(j)+str(i*j))
        #print(lis)
        if len(lis) > 9:
            pass
        else:
            cond = True
            for c in lista:
                #print(lis, c, lis.count(c))
                if lis.count(c) != 1:
                    cond = False
                    break
                else:
                    cond = True
            if cond:
                r[i*j] = [i, j]

sum_pd = 0
for v in r.values():
    sum_pd += v[0] * v[1]
print(sum_pd)

end = time()

print(end - start)