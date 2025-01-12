# 파티
# 골드3

import heapq
import sys
input=lambda:sys.stdin.readline().rstrip()

n, m, x = map(int, input().split())

graph = {i:{} for i in range(1, n+1)}
for _ in range(m):
  start, end, weight = map(int, input().split())
  if end in graph[start]:
    graph[start][end] = min(graph[start][end], weight)
  else:
    graph[start][end] = weight

ans = [0 for _ in range(n+1)]

for student in range(1, n+1):
  distances = [100000 for _ in range(n+1)]
  distances[student] = 0
  q = [(0, student)]
  while q:
    current_distance, current_student = heapq.heappop(q)
    if distances[current_student] < current_distance:
      continue
    for neighbor, weight in graph[current_student].items():
      distance = current_distance+weight
      if distances[neighbor] > distance:
        distances[neighbor] = distance
        heapq.heappush(q, (distance, neighbor))
  if student == x:
    for i in range(n+1):
      ans[i] += distances[i]
  ans[student] += distances[x]
print(max(ans[1:]))