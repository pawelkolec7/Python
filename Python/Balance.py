n = int(input())
w = list(map(int, input().split()))

s = sum(w)

t = [0]
for i in range(n):
    t.append(t[-1] + w[i])

ans = float('inf')
for i in range(n):
    ans = min(ans, abs(s - 2 * t[i + 1]))

print(ans)