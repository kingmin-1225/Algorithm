
from collections import deque
import sys
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
ans = 0
for x in range(n):
  for y in range(m):
    if board[x][y] == 'L' and visited[x][y] == 0:
      visited[x][y] = 1
      q = deque([(x, y)])
      while q:
        x, y = q.popleft()
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
          if 0 <= x+dx < n and 0 <= y+dy < m and board[x+dx][y+dy] == 'L' and visited[x+dx][y+dy] == 0:
            visited[x+dx][y+dy] = 1
            q.append((x+dx, y+dy))
        if len(q) == 0:
          start = deque([(x, y)])
      distance = [[0]*m for _ in range(n)]
      distance[x][y] = 1
      while start:
        x, y = start.popleft()
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
          if 0 <= x+dx < n and 0 <= y+dy < m and board[x+dx][y+dy] == 'L' and distance[x+dx][y+dy] == 0:
            distance[x+dx][y+dy] = distance[x][y]+1
            start.append((x+dx, y+dy))
      ans = max(ans, distance[x][y]-1)
print(ans)
