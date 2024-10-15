numbers = list(map(int, input().split()))
num_queries = int(input())

prefix_sum = [0] * (len(numbers) + 1)
for i in range(1, len(numbers) + 1):
    prefix_sum[i] = prefix_sum[i-1] + numbers[i-1]

for _ in range(num_queries):
    start, end = map(int, input().split())
    print(prefix_sum[end+1] - prefix_sum[start])