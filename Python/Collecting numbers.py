n = int(input())
m = [[int(x) for x in input().split()] for _ in range(n)]

dp = [[0]*n for i in range(n)]
dp[0][0] = m[0][0]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + m[i][0]
    dp[0][i] = dp[0][i-1] + m[0][i]
    
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = m[i][j] + max(dp[i-1][j], dp[i][j-1])
        
print(dp[n-1][n-1])