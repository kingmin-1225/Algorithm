# 토마토
# 골드5
from collections import deque
import sys
input=lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())

board = []
q = deque()
for i in range(m):
  pp = list(map(int, input().split()))
  for j in range(n):
    if pp[j] == 1:
      q.append([i, j])
  board.append(pp)

while q:
  x, y = q.popleft()
  for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
    if 0 <= x+dx < m and 0 <= y+dy < n:
      if board[x+dx][y+dy] == 0:
        q.append([x+dx, y+dy])
        board[x+dx][y+dy] = board[x][y]+1

clear = True
ans = 0
for x in range(m):
  for y in range(n):
    if board[x][y] == 0:
      clear = False
    elif ans < board[x][y]:
      ans = board[x][y]

print(ans-1 if clear else -1)