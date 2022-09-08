counter = 0
month = 1
months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
day_n = 1
year = 1900

leap = [i for i in range(1904, 2001, 4)]

while year < 2001:
    if year in leap and month == 2:
        day_n = (day_n + (29 % 7)) % 7
    else:
        day_n = (day_n + (months[month] % 7)) % 7

    if year > 1900 and day_n == 0:
        counter += 1

    month += 1

    if month == 13:
        year += 1
        month = 1

print(counter)