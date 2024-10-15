n = int(input())
results = []
for i in range(n):
  match = input().split()
  results.append((match[0], match[1]))
players = {}
for match in results:
  player1, player2 = match
  p1_id, p1_points = player1.split(":")
  p2_id, p2_points = player2.split(":")
  p1_points, p2_points = int(p1_points), int(p2_points)
  if p1_id not in players:
    players[p1_id] = {"wins": 0, "points": 0}
  if p2_id not in players:
    players[p2_id] = {"wins": 0, "points": 0}
  if p1_points > p2_points:
    players[p1_id]["wins"] += 1
  elif p1_points < p2_points:
    players[p2_id]["wins"] += 1
  players[p1_id]["points"] += p1_points
  players[p2_id]["points"] += p2_points
sorted_players = sorted(players.keys(), key=lambda x: (-players[x]["wins"], -players[x]["points"], x))
for player in sorted_players:
  print(player)
