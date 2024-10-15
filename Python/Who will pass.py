
N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if matrix[i][j] >= 3:
            print(1, end=' ')
        else:
            neighbors = []
            if i > 0:
                neighbors.append(matrix[i-1][j])
            if i < N-1:
                neighbors.append(matrix[i+1][j])
            if j > 0:
                neighbors.append(matrix[i][j-1])
            if j < N-1:
                neighbors.append(matrix[i][j+1])
            if i > 0 and j > 0:
                neighbors.append(matrix[i-1][j-1])
            if i > 0 and j < N-1:
                neighbors.append(matrix[i-1][j+1])
            if i < N-1 and j > 0:
                neighbors.append(matrix[i+1][j-1])
            if i < N-1 and j < N-1:
                neighbors.append(matrix[i+1][j+1])
            if sum(neighbors) / len(neighbors) >= 3:
                print(1, end=' ')
            else:
                print(0, end=' ')
    print()