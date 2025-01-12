# 케빈 베이컨의 6단계 법칙
# 실버1

import heapq
import sys
input=lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

min_of_kevin_nums = 10000
ans = 1
for i in range(1, n+1):
  distances = [10000 for _ in range(n+1)]
  distances[i] = 0
  q = [(0, i)]
  while q:
    num, person = heapq.heappop(q)
    if distances[person] < num:
      continue
    for friend in graph[person]:
      if distances[friend] > num+1:
        distances[friend] = num+1
        heapq.heappush(q, (num+1, friend))
  kevin_num = sum(distances[1:])
  if min_of_kevin_nums > kevin_num:
    min_of_kevin_nums = kevin_num
    ans = i
print(ans)