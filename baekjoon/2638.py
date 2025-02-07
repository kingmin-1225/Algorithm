# 치즈
# 골드3

from collections import deque
import sys
input=lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

time = 0
cheeses = 0
for x in range(n):
  for y in range(m):
    if board[x][y] == 1:
      cheeses += 1

while cheeses > 0:
  time += 1
  q = deque([[0, 0]])
  visited = [[0 for _ in range(m)] for _ in range(n)]
  visited[0][0] = 1
  while q:
    x, y = q.popleft()
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
      if not(0 <= x+dx < n and 0 <= y+dy < m):
        continue
      if board[x+dx][y+dy] == 0 and visited[x+dx][y+dy] == 0:
        visited[x+dx][y+dy] = 1
        q.append([x+dx, y+dy])
      elif board[x+dx][y+dy] == 1:
        visited[x+dx][y+dy] += 1
        if visited[x+dx][y+dy] == 2:
          board[x+dx][y+dy] = 0
          cheeses -= 1
print(time)