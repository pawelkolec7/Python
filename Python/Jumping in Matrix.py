n = int(input())
sx, sy = map(int, input().split())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

while True:
    row_min = float('inf')
    for i in range(n):
        row_min = min(row_min, matrix[sx][i])
    if row_min == matrix[sx][sy]:
        col_min = float('inf')
        for i in range(n):
            col_min = min(col_min, matrix[i][sy])
        if col_min == matrix[sx][sy]:
            print(sx, sy)
            break
        else:
            for i in range(n):
                if matrix[i][sy] == col_min:
                    sx = i
                    break
    else:
        for i in range(n):
            if matrix[sx][i] == row_min:
                sy = i
                break