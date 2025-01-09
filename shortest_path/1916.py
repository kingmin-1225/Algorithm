# 최소비용 구하기
# 골드5

import sys
import heapq
input=lambda:sys.stdin.readline().rstrip()

n = int(input())

graph = {i: {} for i in range(1, n+1)}
distances = [1000000000 for _ in range(n+1)]

for _ in  range(int(input())):
  start, end, cost = map(int, input().split())
  if end in graph[start]:
    graph[start][end] = min(graph[start][end], cost)
  else:
    graph[start][end] = cost

start, end = map(int, input().split())

distances[start] = 0
q = [(0, start)]
while q:
  current_distance, current_node = heapq.heappop(q)
  if current_distance > distances[current_node]:
    continue
  for neighbor, weight in graph[current_node].items():
    distance = current_distance + weight
    if distance < distances[neighbor]:
      distances[neighbor] = distance
      heapq.heappush(q, (distance, neighbor))

print(distances[end])