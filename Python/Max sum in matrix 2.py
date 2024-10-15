n = int(input())
matrix = []
for i in range(n):
    x = list(map(int, input().split()))
    matrix.append(x)

p_sum = [[0 for _ in range(n)] for _ in range(n)]
p_sum[0][0] = matrix[0][0]

for i in range(1, n):
    p_sum[0][i] = p_sum[0][i-1] + matrix[0][i]
    p_sum[i][0] = p_sum[i-1][0] + matrix[i][0]

for i in range(1, n):
    for j in range(1, n):
        p_sum[i][j] = p_sum[i-1][j] + p_sum[i][j-1] - p_sum[i-1][j-1] + matrix[i][j]


max_sum = float('-inf')
for t in range(n):
    for l in range(n):
        for b in range(t, n):
            for r in range(l, n):
                sum_ = p_sum[b][r]
                if t > 0:
                    sum_ -= p_sum[t-1][r]
                if l > 0:
                    sum_ -= p_sum[b][l-1]
                if t > 0 and l > 0:
                    sum_ += p_sum[t-1][l-1]
                max_sum = max(max_sum, sum_)

print(max_sum)
