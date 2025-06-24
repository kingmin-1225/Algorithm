# 영역 구하기
# 실버1

import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()

M, N, K = map(int, input().split())

board = [[0]*N for _ in range(M)]
visited = [[0]*N for _ in range(M)]
for _ in range(K):
  start_y, start_x, end_y, end_x = map(int, input().split())
  for x in range(start_x, end_x):
    for y in range(start_y, end_y):
      board[x][y] = 1
ans = []
for x in range(M):
  for y in range(N):
    if board[x][y] == 0 and visited[x][y] == 0:
      q = deque([[x, y]])
      ans.append(1)
      visited[x][y] = 1
      while q:
        x, y = q.popleft()
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
          if 0 <= x+dx < M and 0 <= y+dy < N and board[x+dx][y+dy] == 0 and visited[x+dx][y+dy] == 0:
            visited[x+dx][y+dy] = 1
            ans[-1] += 1
            q.append([x+dx, y+dy])
ans.sort()
print(len(ans))
print(*ans)
