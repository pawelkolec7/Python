n, x, y = input().split()
n = int(n)
x = int(x)
y = int(y)
values = {}

for i in range(0, n+1):
    for j in range(0, n+1):
        value = x*i**2+y*j**2
        if value not in values:
            values[value] = 0
        values[value] += 1

value1 = 0

for k in range(0, n+1):
    for l in range(0, n+1):
        if x*k**2+y*l**2 in values:
            value1 += values[x*k**2+y*l**2]

print(value1)