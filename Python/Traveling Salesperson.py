import math

def tour_length(n, cities, order):
  result = 0
  for i in range(n):
    x1, y1 = cities[order[i]]
    x2, y2 = cities[order[(i + 1) % n]]
    result += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
  return result

n = int(input())
cities = {}
for _ in range(n):
  name, x, y = input().split()
  cities[name] = (int(x), int(y))
order = input().split()
print(tour_length(n, cities, order))