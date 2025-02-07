# 연구소
# 골드4

import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
not_walls = []
board = []
viruses = []
for i in range(n):
  pp = list(map(int, input().split()))
  for j in range(m):
    if pp[j] == 0:
      not_walls.append([i, j])
    elif pp[j] == 2:
      viruses.append([i, j])
  board.append(pp)

cnt = 0
visited = [[0 for _ in range(m)] for _ in range(n)]
ans = 0
for i in range(len(not_walls)-2):
  for j in range(i+1, len(not_walls)-1):
    for z in range(j+1, len(not_walls)):
      cnt += 1
      temp = len(not_walls)-3
      new_walls = [not_walls[i], not_walls[j], not_walls[z]]
      q = deque(viruses)
      while q:
        x, y = q.popleft()
        for dx, dy in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
          if 0 <= x+dx < n and  0 <= y+dy < m and visited[x+dx][y+dy] < cnt:
            if board[x+dx][y+dy] == 0 and [x+dx, y+dy] not in new_walls:
              temp -= 1
              q.append([x+dx,y+dy])
              visited[x+dx][y+dy] = cnt
      ans = max(ans, temp)
print(ans)