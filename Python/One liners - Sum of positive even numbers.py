s = input()
print(sum(filter(lambda x: int(x) > 0 and int(x) % 2 == 0, map(int,s.split()))))