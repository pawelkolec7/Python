n = int(input())
chessboard = []
total_attacks = 0

for i in range(n):
  chessboard.append(input())

for i in range(n):
  for j in range(n):
    if chessboard[i][j] == 's':
      attacks = 0
      if i > 1:
        if j > 0 and chessboard[i-2][j-1] == 's':
          attacks += 1
        if j < n-1 and chessboard[i-2][j+1] == 's':
          attacks += 1
      if i < n-2:
        if j > 0 and chessboard[i+2][j-1] == 's':
          attacks += 1
        if j < n-1 and chessboard[i+2][j+1] == 's':
          attacks += 1
      if j > 1:
        if i > 0 and chessboard[i-1][j-2] == 's':
          attacks += 1
        if i < n-1 and chessboard[i+1][j-2] == 's':
          attacks += 1
      if j < n-2:
        if i > 0 and chessboard[i-1][j+2] == 's':
          attacks += 1
        if i < n-1 and chessboard[i+1][j+2] == 's':
          attacks += 1
      total_attacks += attacks
    
print(total_attacks)