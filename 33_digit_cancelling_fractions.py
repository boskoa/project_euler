from time import time

start = time()

res = []
for i in range(12, 99):
    a = list(str(i))[0]
    b = list(str(i))[1]
    if b == '0':
        pass
    else:
        for j in range(int(b)*10+1, (int(b)+1)*10):
            r = list(str(j))
            c = r[1]
            r = ''.join(r)
            if i == int(r):
                pass
            elif int(a) / int(c) == i / int(r):
                res.append(int(a)/int(c))
              
sum_m = 1
for z in range(len(res)):
    sum_m *= res[z]
    
print(1/round(sum_m, 2))

end = time()

print(end - start)