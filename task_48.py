arr = [5, 7, 11, 13, 15, 20, 25]
avrg = 0
count = 0
for el in arr:
    if el > 10:
        avrg += el
        count += 1
avrg = avrg/count