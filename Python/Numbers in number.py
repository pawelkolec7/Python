def find(length: int, string: str) -> None:
    sub = []
    f = []
    for i in range(len(string) - length + 1):
        sub.append(string[i:i + length])
    sub.sort()
    for i in range(len(sub)):
        count = sub.count(sub[i])
        if i == 0:
            f.append([sub[i], count])
        elif sub[i] != sub[i-1]:
            f.append([sub[i], count])
    f.sort(reverse=True, key = lambda x: x[1])
    print(f[0][0])

string = input()
for i in range(1, len(string) + 1):
    find(i, string)