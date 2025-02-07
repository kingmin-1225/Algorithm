# 알파벳
# 골드4

import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()

r, c = map(int, input().split())

board = [list(input()) for _ in range(r)]

q = deque([([board[0][0]], 0, 0)])

while q:
  keys, x, y = q.popleft()
  for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
    if not (0 <= x+dx < r and 0 <= y+dy < c):
      continue
    if not (board[x+dx][y+dy] in keys):
      q.append((keys+[board[x+dx][y+dy]], x+dx, y+dy))
print(len(keys))