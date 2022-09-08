set_kvadrata = set()

for a in range(2, 101):
    for b in range(2, 101):
        c = a**b
        set_kvadrata.add(c)
        
lista_kvadrata = sorted(list(set_kvadrata))
print(len(set_kvadrata))