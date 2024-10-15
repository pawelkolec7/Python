def kadane(arr):
    max_so_far = max_ending_here = arr[0]
    start = end = 0
    for i in range(1, len(arr)):
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            start = end = i
        else:
            max_ending_here += arr[i]
            end = i
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return (max_so_far, start, end)

def max_sum_submatrix(matrix):
    n = len(matrix)
    max_sum = float('-inf')
    left = top = 0
    right = bottom = 0
    for left_col in range(n):
        temp = [0] * n
        for right_col in range(left_col, n):
            for i in range(n):
                temp[i] += matrix[i][right_col]
            kadane_res = kadane(temp)
            if kadane_res[0] > max_sum:
                max_sum = kadane_res[0]
                left = left_col
                right = right_col
                top = kadane_res[1]
                bottom = kadane_res[2]
    return (max_sum, left, top, right, bottom)

n = int(input())
matrix = []
for i in range(n):
    x = list(map(int, input().split()))
    matrix.append(x)

res = max_sum_submatrix(matrix)
print(res[0])