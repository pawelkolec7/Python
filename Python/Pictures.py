h, w, y, x = map(int, input().split())

t = []

for i in range(h):
    t.append(input().split())
    t[i] = [int(x) for x in t[i]]

for i in range(h - y + 1):
    for j in range(w - x + 1):
        p = 0
        for k in range(i, i + y):
            for l in range(j, j + x):
                if t[k][l] == 0:
                    p += 1

        if p == x * y:
            print(True)
            exit()

print(False)