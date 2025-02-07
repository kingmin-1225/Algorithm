# 내리막길
# 골드3

from collections import deque
import sys
input=lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

q = deque()
q.append([0, 0])
cnt = 0
while q:
  x, y = q.popleft()
  if x == n-1 and y == m-1:
    cnt += 1
  for dx, dy in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
    if 0 <= x+dx < n and 0 <= y+dy < m and board[x+dx][y+dy] < board[x][y]:
      q.append([x+dx, y+dy])

print(cnt)