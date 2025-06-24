
import heapq
import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
if n == 1:
  print(0)
else:
  graph = {i:{} for i in range(1, n+1)}
  for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

  distances = [-1 for _ in range(n+1)]
  distances[1] = 0
  q = [(0, 1)]

  while q:
    current_cost, current_node = heapq.heappop(q)
    if current_cost > distances[current_node]:
      continue
    for node, cost in graph[current_node].items():
      distance = current_cost+cost
      if distances[node] == -1 or distance < distances[node]:
        distances[node] = distance
        heapq.heappush(q, (distance, node))

  ans = 0
  start = 0
  for i in range(1, n+1):
    if distances[i] > ans:
      start = i
      ans = distances[i]

  distances = [-1 for _ in range(n+1)]
  distances[start] = 0
  q = [(0, start)]

  while q:
    current_cost, current_node = heapq.heappop(q)
    if current_cost > distances[current_node]:
      continue
    for node, cost in graph[current_node].items():
      distance = current_cost+cost
      if distances[node] == -1 or distance < distances[node]:
        distances[node] = distance
        heapq.heappush(q, (distance, node))

  print(max(distances))