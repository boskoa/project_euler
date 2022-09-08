def fibo(n, i=0, j=1):
    for k in range(n):
        i, j = j, j + i
    return i

h = 1

while True:
    if len(str(fibo(h))) == 1000:
        print(fibo(h))
        print(h)
        break
    h += 1