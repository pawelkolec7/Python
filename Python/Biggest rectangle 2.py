n = int(input())
wysokosc = [int(input()) for _ in range(n)]

max_pole = 0
stos = []
for i, h in enumerate(wysokosc + [0]):
    while stos and wysokosc[stos[-1]] >= h:
        j = stos.pop()
        k = stos[-1] if stos else -1
        max_pole = max(max_pole, (i - k - 1) * wysokosc[j])
    stos.append(i)

print(max_pole)