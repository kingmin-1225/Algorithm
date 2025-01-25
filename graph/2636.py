# 치즈
# 골드4

from collections import deque
import sys
input=lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

time = 0

ans = 0
for x in range(n):
  for y in range(m):
    if board[x][y] == 1:
      ans += 1

while ans > 0:
  time += 1
  visited = [[0 for _ in range(m)] for _ in range(n)]
  q = deque([(0, 0)])
  melted = 0
  visited[0][0] = 1
  while q:
    x, y = q.popleft()
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
      if 0 <= x+dx < n and 0 <= y+dy < m:
        if visited[x+dx][y+dy] == 1:
          continue
        visited[x+dx][y+dy] = 1
        if board[x+dx][y+dy] == 0:
          q.append((x+dx, y+dy))
          continue
        melted += 1
        board[x+dx][y+dy] = 0
  ans -= melted
print(time)
print(melted)