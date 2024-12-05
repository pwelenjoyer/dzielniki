liczby = []
with open("liczby.txt", "r") as plik:
    for i in plik.readlines():
        liczby.append(int(i))

lista = {}
for i in liczby:
    x = 0
    a = []
    for j in range(1, int((i + 1)**0.5)):
        if i % j == 0:
            a.append(j)
            a.append(i // j)
            x += 2
    if x == 18:
        a.sort()
        lista[i] = a
print(lista)