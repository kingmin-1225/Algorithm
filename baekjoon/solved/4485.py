# 녹색 옷 입은 애가 젤다지?
# 골드4

import heapq
import sys 
input = lambda:sys.stdin.readline().rstrip()

problemNum = 1
n = int(input())
while n > 0:
  board = [list(map(int, input().split())) for _ in range(n)]
  earnedRupee = [[-1]*(n) for _ in range(n)]
  earnedRupee[0][0] = board[0][0]
  q = [(board[0][0], 0, 0)]
  while q:
    rupee, x, y = heapq.heappop(q)
    if rupee > earnedRupee[x][y]:
      continue
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
      if not(0 <= x+dx < n and 0 <= y+dy < n):
        continue

      total = board[x+dx][y+dy]+rupee
      if earnedRupee[x+dx][y+dy] == -1 or earnedRupee[x+dx][y+dy] > total:
        earnedRupee[x+dx][y+dy] = total
        heapq.heappush(q, (total, x+dx, y+dy))
  print(f"Problem {problemNum}: {earnedRupee[n-1][n-1]}")
  n = int(input())
  problemNum += 1
