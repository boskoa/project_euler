from time import time

start = time()
"""
# By counting all possible combinations.

# 200p solution included
counter = 1

for a in range(3):
    for b in range(int((200-a*100)/50)+1):
        for c in range(int((200-a*100-b*50)/20)+1):
            for d in range(int((200-a*100-b*50-c*20)/10)+1):
                for e in range(int((200-a*100-b*50-c*20-d*10)/5)+1):
                    for f in range(int((200-a*100-b*50-c*20-d*10-e*5)/2)+1):
                        counter += 1

print(counter)
"""

# By making a complete 200x7 matrix and filling it with formula results based on previous results.
pen_ar = [[1, 1, 1, 1, 1, 1, 1, 1]]
p = [1, 2, 5, 10, 20, 50, 100, 200]
su = [i+1 for i in range(200)]

for i in range(1, 200):
    pen_ar.append([1])
    for j in range(1, 8):
        pen_ar[i].extend([0])

def ar(s, d):
    pov = 0
    if su[s] < p[d]:
        pov = pen_ar[s][d-1]
    elif su[s] == p[d]:
        pov = pen_ar[s][d-1] + 1
    else:
        pov = pen_ar[s][d-1] + pen_ar[su[s]-p[d]-1][d]
    return pov

for s in range(0, 200):
    for d in range(0, 8):
        if s != 0 and d != 0:
            pen_ar[s][d] = ar(s, d)
            
print(pen_ar[199][7])

end = time()

print(end - start)