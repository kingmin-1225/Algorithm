# 이중 우선순위 큐
# 골드4

import heapq
import sys
input = lambda:sys.stdin.readline().rstrip()

for i in range(int(input())):
  Max = []
  Min = []
  added = {}
  total = 0
  for j in range(int(input())):
    order, num = input().split()
    num = int(num)
    if order == 'I':
      if num in added:
        added[num] += 1
      else:
        added[num] = 1
      total += 1
      heapq.heappush(Max, -num)
      heapq.heappush(Min, num)
    elif order == 'D' and total > 0:
      total -= 1
      if num == -1:
        key = heapq.heappop(Min)
        while added[key] == 0:
          key = heapq.heappop(Min)
      else:
        key = -heapq.heappop(Max)
        while added[key] == 0:
          key = -heapq.heappop(Max)
      added[key] -= 1
  if total == 0:
    print("EMPTY")
  else:
    answer = [0, 0]
    first = -heapq.heappop(Max)
    while added[first] == 0:
      first = -heapq.heappop(Max)
    second = heapq.heappop(Min)
    while added[second] == 0:
      second = heapq.heappop(Min)
    print(first, second)