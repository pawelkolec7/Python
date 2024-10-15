wiersz, columna = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(wiersz)]
a = int(input())
for _ in range(a):
    b = input().split()
    if b[0] == "RR":
        matrix[int(b[1])] = matrix[int(b[1])][::-1]
    elif b[0] == "RC":
        matrix = [list(x) for x in zip(*matrix)]
        matrix[int(b[1])] = matrix[int(b[1])][::-1]
        matrix = [list(x) for x in zip(*matrix)]
    elif b[0] == "T":
        matrix = [list(x) for x in zip(*matrix)]

for row in matrix:
    print(" ".join(map(str, row)))