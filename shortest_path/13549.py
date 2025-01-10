# 숨바꼭질3
# 골드5

import heapq
import sys
input=lambda:sys.stdin.readline().rstrip()

n, k = map(int, input().split())

distances = [100000 for _ in range(200001)]
distances[n] = 0
q = [(0, n)]
while q:
  distance, current_node = heapq.heappop(q)
  if current_node > 0 and distances[current_node-1] > distance+1:
    distances[current_node-1] = distance+1
    heapq.heappush(q, (distance+1, current_node-1))
  if current_node < 200000 and distances[current_node+1] > distance+1:
    distances[current_node+1] = distance+1
    heapq.heappush(q, (distance+1, current_node+1))
  if current_node < 100000 and distances[current_node*2] > distance:
    distances[current_node*2] = distance
    heapq.heappush(q, (distance, current_node*2))
print(distances[k])