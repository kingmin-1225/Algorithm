# 헌내기는 친구가 필요해
# 실버2


from collections import deque
import sys
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
board = []
visited = [[0]*m for _ in range(n)] 
q = deque() 
for i in range(n):
  board.append(list(input()))
  if len(q) == 0:
    for j in range(m):
      if board[i][j] == 'I':
        q.append((i, j))

ans = 0
while q:
  x, y = q.popleft()
  for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
    if 0 <= x+dx < n and 0 <= y+dy < m and visited[x+dx][y+dy] == 0 and board[x+dx][y+dy] != 'X':
      q.append((x+dx, y+dy))
      visited[x+dx][y+dy] = 1
      if board[x+dx][y+dy] == 'P':
        ans += 1
        board[x+dx][y+dy] = 'O'
print(ans if ans > 0 else "TT")