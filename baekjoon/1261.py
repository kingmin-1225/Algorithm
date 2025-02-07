# 알고스팟
# 골드4

import heapq
import sys
input=lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(m)]
costs = [[200]*n for _ in range(m)]
costs[0][0] = 0

q = [(0, 0, 0)] # num_of_crumbling_walls, x, y
while q:
  num_walls, x, y = heapq.heappop(q)
  if costs[x][y] < num_walls:
    continue
  for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
    if not (0 <= x+dx < m and 0 <= y+dy < n):
      continue
    cost = num_walls
    if board[x+dx][y+dy] == 1:
      cost += 1
    if costs[x+dx][y+dy] > cost:
      costs[x+dx][y+dy] = cost
      heapq.heappush(q, (cost, x+dx, y+dy))
print(costs[m-1][n-1])