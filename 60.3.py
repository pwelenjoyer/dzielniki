liczby = []
with open("liczby.txt", "r") as plik:
    for i in plik.readlines():
        liczby.append(int(i))

def nwd(x, y):
    while y:
        x, y = y, x % y
    return x

def zgodnosc(i, liczby):
    for x in liczby:
        if x != i and nwd(i, x) != 1:
            return False
    return True

szukana = None
liczby.sort()
b = reversed(liczby)
for i in b:
    if zgodnosc(i, liczby):
        szukana = i
        break
print(szukana)