# Problem_Title
# Rank

import heapq
import sys
input=lambda:sys.stdin.readline().rstrip()

n = int(input())

lectures = []
for _  in range(n):
  s, t = map(int, input().split())
  lectures.append([s, t])
lectures.sort()

room = []
heapq.heappush(room, 0)

for lecture in lectures:
  r = heapq.heappop(room)
  if lecture[0] < r:
    heapq.heappush(room, r)
  heapq.heappush(room, lecture[1])
print(len(room))