# 낚시왕
# 골드1

import sys
input=lambda:sys.stdin.readline().rstrip()

def shark_move(x, y, info):
  global R, C, new_board
  size, dx, dy = info
  if dx > 0:
    x = ((x+dx+1)+(x+dx+1)%R)%R-1
  new_board[x][y] = max(new_board[x][y], [(size, dx, dy)])


R, C, M = map(int, input().split())
move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
board = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
  r, c, s, d, z = map(int, input().split())
  board[r-1][c-1].append((z, move[d-1][0]*s, move[d-1][1]*s))

ans = 0
for Y in range(C):
  for X in range(R):
    if board[X][Y] == []:
      continue
    ans += board[X][Y].pop()[0]
    break
  new_board = [[[]*C] for _ in range(R)]
  for x in range(R):
    for y in range(C):
      if board[x][y] == []:
        continue
      shark_move(x, y, board[x][y].pop())
  board = new_board
print(ans)