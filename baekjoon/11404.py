# 플로이드
# 골드4

import heapq
import sys
input=lambda:sys.stdin.readline().rstrip()

n = int(input())
graph = {i:{} for i in range(1, n+1)}

for _ in range(int(input())):
  a, b, c = map(int, input().split())
  if b in graph[a]:
    graph[a][b] = min(graph[a][b], c)
  else:
    graph[a][b] = c
  
for root in range(1, n+1):
  distances = [100000000 for _ in range(n+1)]
  distances[root] = 0
  q = [(0, root)]
  while q:
    current_distance, current_node = heapq.heappop(q)
    if current_distance > distances[current_node]:
      continue
    for neighbor, weight in graph[current_node].items():
      distance = current_distance+weight
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(q, (distance, neighbor))
  for i in range(1, n+1):
    if distances[i] == 100000000:
      distances[i] = 0
  print(*distances[1:])