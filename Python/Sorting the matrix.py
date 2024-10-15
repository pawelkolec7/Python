macierz = input().split()
wiersze = int(macierz[0])
kolumny = int(macierz[1])
tablica_macierzy = []

for i in range(wiersze):
    tablica_macierzy.append(list(map(int, input().split())))
macierz_robocza = []

for wiersz in tablica_macierzy:
    for i in range(len(wiersz)):
        macierz_robocza.append(wiersz[i])
#sortowanie_macierzy
macierz_robocza.sort()
#wynikowa_macierz
macierz_wynikowa = [[0] * kolumny for i in range(wiersze)]
k = 0
for i in range(kolumny):
    for j in range(wiersze):
        macierz_wynikowa[j][i] = macierz_robocza[k]
        k += 1
for wiersz in macierz_wynikowa:
    print(*wiersz)