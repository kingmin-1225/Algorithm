# 트리
# 골드5


from collections import deque
import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
tree = [[] for _ in range(n)]
nodes = list(map(int, input().split()))
root = 0
rmv_node = int(input())

for idx in range(len(nodes)):
  if nodes[idx] == -1:
    root = idx
    continue
  elif idx == rmv_node:
    continue
  tree[nodes[idx]].append(idx)

q = deque([root])
ans = 0
while q:
  start_node = q.popleft()
  if start_node == rmv_node:
    continue
  if len(tree[start_node]) == 0:
    ans += 1
  for node in tree[start_node]:
    q.append(node)
print(ans)