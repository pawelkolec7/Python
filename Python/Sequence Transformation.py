n, m = map(int, input().split())
s = input()
max_length = n
max_string = s

for i in range(m):
    a, b, op = map(str, input().split(';'))
    part1 = s[:min(int(a), int(b))]
    part2 = s[min(int(a), int(b)):max(int(a), int(b))+1]
    part3 = s[max(int(a), int(b))+1:]
    s = part1 + op + part3
    if len(s) > max_length:
        max_length = len(s)
        max_string = s
print(s)
print(max_string)