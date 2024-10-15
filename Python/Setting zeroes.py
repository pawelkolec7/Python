def dodaj_rzad(macierz, rzad):
    new_matrix = [row.copy() for row in macierz]
    new_matrix[rzad] = [0] * len(new_matrix[rzad])
    return new_matrix
def dodaj_kolumne(macierz, kolumna):
    new_matrix = [row.copy() for row in macierz]
    for i in range(len(new_matrix)):
        new_matrix[i][kolumna] = 0
    return new_matrix
def robota(macierz):
    t = set()
    for i, j in enumerate(macierz):
        for k, l in enumerate(j):
            if l == 0:
                t.add((i, k))
    for i, k in t:
        macierz = dodaj_rzad(macierz, i)
        macierz = dodaj_kolumne(macierz, k)
    return macierz
def dodawanie(rzad, kolumna):
    macierz = []
    for el in range(rzad):
        macierz.append(list(map(int, input().split())))
    return macierz
def zadanie():
    rzad, kolumna = map(int, input().split())
    macierz = dodawanie(rzad, kolumna)
    macierz = robota(macierz)
    for el in macierz:
        print(" ".join(list(map(str, el))))
if __name__ == "__main__":
    zadanie()