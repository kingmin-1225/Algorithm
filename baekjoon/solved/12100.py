# 2048
# 골드1

import sys
input=lambda:sys.stdin.readline().rstrip()

n = int(input())
board_origin = [list(map(int, input().split())) for _ in range(n)]

def move(ll):
  stack = []
  merged = False
  for i in range(len(ll)):
    if ll[i] == 0:
      continue
    if stack == []:
      stack.append(ll[i])
    else:
      if ll[i] == stack[-1] and not merged:
        stack[-1] *= 2
        merged = True
      else:
        stack.append(ll[i])
        merged = False
  for _ in range(len(ll)-len(stack)):
    stack.append(0)
  return stack

def rotate(ll):
  global n
  B = [[0]*n for _ in range(n)]
  for x in range(n):
    for y in range(n):
      B[n-y-1][x] = ll[x][y]
  return B

R = []
for a in range(4):
  for b in range(4):
    for c in range(4):
      for d in range(4):
        for e in range(4):
          R.append([a,b,c,d,e])

ans = 0
for rotate_list in R:
  board = []
  for i in range(n):
    board.append(board_origin[i][:])
  for r in rotate_list:
    for _ in range(r):
      board = rotate(board) 
    for idx in range(n):
      board[idx] = move(board[idx])
  for x in range(n):
    for y in range(n):
      ans = max(board[x][y], ans)

print(ans)