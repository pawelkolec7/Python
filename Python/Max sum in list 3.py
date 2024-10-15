def max_sum(numbers):
  result = 0
  current = 0
  for n in numbers:
    current += n
    if current < 0:
      current = 0
    result = max(result, current)
  return result

numbers = list(map(int, input().split()))
print(max_sum(numbers))