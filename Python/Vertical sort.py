wymiary_macierzy = input().split()
wiersze = int(wymiary_macierzy[1])
kolumny = int(wymiary_macierzy[0])
tablica_macierzy = []
for i in range(wiersze):
    row = list(map(int, input().split()))
    tablica_macierzy.append(row)
tablica_macierzy1 = [list(i) for i in zip(*tablica_macierzy)]
tablica_macierzy2 = []
for wiersz in tablica_macierzy1:
    sorted_row = sorted(wiersz)
    tablica_macierzy2.append(sorted_row)
tablica_macierzy3 = [list(i) for i in zip(*tablica_macierzy2)]
for wiersz in tablica_macierzy3:
    print(*wiersz)