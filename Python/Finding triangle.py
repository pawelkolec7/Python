n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]

min_pole = float('inf')
max_pole = float('-inf')

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x1, y1 = p[i]
            x2, y2 = p[j]
            x3, y3 = p[k]
            if (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2):
                continue
            pole = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)
            min_pole = min(min_pole, pole)
            max_pole = max(max_pole, pole)
            
print(min_pole, max_pole)