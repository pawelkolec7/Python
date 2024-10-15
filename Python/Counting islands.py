n = int(input())
M = []
for i in range(n):
    M.append(list(input()))
    
def zwiedzaj(m, i, j):
    M[i][j] = '2'
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0 <= i+di < len(m) and 0 <= j+dj < len(m) and m[i+di][j+dj] == '1':
            zwiedzaj(m, i+di, j+dj)
            
res = 0
for i in range(n):
    for j in range(n):
        if M[i][j] == '1':
            zwiedzaj(M, i, j)
            res += 1

print(res)