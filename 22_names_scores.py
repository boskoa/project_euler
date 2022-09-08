import re, string

letter_dict = {}
counter = 1

names_st = []
names_dict = {}

with open('names.txt', 'r') as n:
    names = re.sub('"', '', n.readlines()[0])
    names_st = names.split(',')
    names_st.sort()

for i in string.ascii_uppercase:
    letter_dict[i] = counter
    counter += 1
    
for g in names_st:
    sum_l = 0
    for h in g:
        sum_l += letter_dict[h]
    names_dict[g] = sum_l * (names_st.index(g) + 1)
    
sum_all = 0

for i in names_dict.values():
    sum_all += i
    
print(sum_all)