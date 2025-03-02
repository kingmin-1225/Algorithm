# 특정 거리의 도시 찾기
# 실버2

import heapq
import sys
input = lambda:sys.stdin.readline().rstrip()

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

ans = []
q = [(0, x)]
distances = [1000000 for _ in range(n+1)]
distances[x] = 0

while q:
  cost, current_node = heapq.heappop(q)
  if cost > distances[current_node]:
    continue
  for node in graph[current_node]:
    if distances[node] > cost+1:
      distances[node] = cost+1
      heapq.heappush(q, (cost+1, node))

for i in range(1, n+1):
  if distances[i] == k:
    ans.append(i)
if ans == []:
  print(-1)
else:
  ans.sort()
  print(*ans, sep="\n")

