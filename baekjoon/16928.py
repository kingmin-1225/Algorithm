# 뱀과 사다리 게임
# 골드5

import sys, heapq
from collections import deque
input=lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())

board = [j for j in range(101)]
other = [j for j in range(101)]

for _ in range(n):
  x, y = map(int, input().split())
  other[x] = y
for _ in range(m):
  u, v = map(int, input().split())
  other[u] = v

# board[1] = 0
# q = [(0, 1)]

# while q:
#   cost, location = heapq.heappop(q)
#   if cost > board[location]:
#     continue
#   for i in range(1, 7):
#     dest = location+i
#     if dest > 100:
#       break
#     if board[other[dest]] > cost+1:
#       board[other[dest]] = cost+1
#       heapq.heappush(q, (cost+1, other[dest]))

# print(board[-1])

q = deque([1])
board[1] = 0
while q:
  start = q.popleft()
  for i in range(1, 7):
    if start+i > 100:
      break
    if board[other[start+i]] > board[start]+1:
      board[other[start+i]] = board[start]+1
      q.append(other[start+i])
print(board[100])