# 트리의 지름
# 골드2

import heapq
import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

graph = {i:{} for i in range(1, n+1)}
for i in range(n):
  pp = list(map(int, input().split()))
  idx = 1
  while pp[idx] != -1:
    graph[pp[0]][pp[idx]] = pp[idx+1]
    idx += 2

q = [(0, 1)]
distances = [-1 for _ in range(n+1)]
distances[1] = 0

while q:
  current_cost, current_node = heapq.heappop(q)
  if distances[current_node] > current_cost:
    continue
  for node, cost in graph[current_node].items():
    distance = cost+current_cost
    if distances[node] == -1 or distance < distances[node]:
      distances[node] = distance
      heapq.heappush(q, (distance, node))

maxDistance = max(distances)
startPoint = distances.index(maxDistance)

q = [(0, startPoint)]
distances = [-1 for _ in range(n+1)]
distances[startPoint] = 0

while q:
  current_cost, current_node = heapq.heappop(q)
  if distances[current_node] > current_cost:
    continue
  for node, cost in graph[current_node].items():
    distance = cost+current_cost
    if distances[node] == -1 or distance < distances[node]:
      distances[node] = distance
      heapq.heappush(q, (distance, node))

print(max(distances))