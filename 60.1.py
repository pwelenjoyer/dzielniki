liczby = []
with open("liczby.txt", "r") as plik:
    for i in plik.readlines():
        liczby.append(int(i))

lista = []
x = 0
a = 0
b = 0
for i in liczby:
    if i < 1000:
        x += 1
        b = a
        a = i

print("przedostatnia:", b, "ostatnia:", a, "ilosc:", x)