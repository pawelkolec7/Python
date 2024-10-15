def zadanie():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    max_sum = 0
    for i in range(n):
        for j in range(m):
            diagonal_sum = 0
            k = i
            l = j
            while k < n and l < m:
                diagonal_sum += matrix[k][l]
                k += 1
                l += 1
            max_sum = max(max_sum, diagonal_sum)
            diagonal_sum = 0
            k = i
            l = j
            while k < n and l >= 0:
                diagonal_sum += matrix[k][l]
                k += 1
                l -= 1
            max_sum = max(max_sum, diagonal_sum)
    print(max_sum)

if __name__ == "__main__":
    zadanie()