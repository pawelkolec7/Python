s = input()
print(sum(s.count(c) % 2 for c in set(s)) <= 1)