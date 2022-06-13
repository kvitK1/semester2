a = [1, 4, 5, 7, 1, 2, 8, 1, 5, 4, 2, 1]
tupl = set()
for el in a:
    p = a.count(el)
    tupl.add((el, p))

for k in tupl:
    print(k)