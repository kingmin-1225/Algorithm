# 경사로
# 골드3

import sys
input=lambda:sys.stdin.readline().rstrip()

n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
  top_ramp = [0 for _ in range(n)]
  top_ans = True
  for j in range(1, n):
    key = board[j][i]-board[j-1][i]
    if abs(key) > 1:
      top_ans = False
      break
    elif key == -1:
      if j+l-1 < n and [board[j][i]]*l == [board[j+x][i] for x in range(l)] and sum(top_ramp[j:j+l]) == 0:
        
        for idx in range(l):
          top_ramp[j+idx] = 1
      else:
        top_ans = False
        break
    elif key == 1:
      if j >= l and [board[j-1][i]]*l == [board[j-x-1][i] for x in range(l)] and sum(top_ramp[j-l:j]) == 0:
        for idx in range(l):
          top_ramp[j-idx-1] = 1
      else:
        top_ans = False
        break
  if top_ans:
    ans += 1

  left_ramp = [0 for _ in range(n)]
  left_ans = True
  for j in range(1, n):
    key = board[i][j]-board[i][j-1]
    if abs(key) > 1:
      left_ans = False
      break
    elif key == -1:
      if j+l-1 < n and [board[i][j]]*l == [board[i][j+x] for x in range(l)] and sum(left_ramp[j:j+l]) == 0:
        for idx in range(l):
          left_ramp[j+idx] = 1
      else:
        left_ans = False
        break
    elif key == 1:
      if j >= l and [board[i][j-1]]*l == [board[i][j-x-1] for x in range(l)] and sum(left_ramp[j-l:j]) == 0:
        for idx in range(l):
          left_ramp[j-idx-1] = 1
      else:
        left_ans = False
        break
  if left_ans:
    ans += 1

print(ans)