import copy

rozmiar_macierzy = int(input())
macierz = []

def oblicz_srednia(x,wiersz,kolumna,rozmiar_macierzy):
    aktualna_liczba = macierz[wiersz][kolumna]
    srednia = -macierz[wiersz][kolumna]
    licznik = -1
    for k in range(rozmiar_macierzy):
        if x[wiersz][k] >= aktualna_liczba:
            srednia += macierz[wiersz][k]
            licznik+=1
    for l in range(rozmiar_macierzy):
        if x[l][kolumna] >= aktualna_liczba:
            srednia += macierz[l][kolumna]
            licznik += 1
    return srednia/licznik

for i in range(rozmiar_macierzy):
    macierz.append(list(map(int, input().split())))
nowa_macierz = copy.deepcopy(macierz)
for i in range(rozmiar_macierzy):
    for j in range(rozmiar_macierzy):
        if macierz[i][j] >= 7:
            nowa_macierz[i][j] = 1
        elif oblicz_srednia(macierz,i,j,rozmiar_macierzy) >= 7:
            nowa_macierz[i][j] = 1
        else:
            nowa_macierz[i][j] = 0
for i in range(rozmiar_macierzy):
    print(*nowa_macierz[i],sep=" ")