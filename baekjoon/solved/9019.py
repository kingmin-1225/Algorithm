# DSLR
# 골드4

from collections import deque
import sys
input = lambda:sys.stdin.readline().rstrip()


for _ in range(int(input())):
  origin, result = map(int, input().split())
  visited = [[] for _ in range(10000)]
  visited[origin].append("")
  q = deque([origin])
  while q:
    num = q.popleft()
    if num == result:
      print(*visited[num], sep = "")
      break
    
    for i in ['D', 'S', 'L', 'R']:
      if i == 'D':
        n = num*2
        n %= 10000
      elif i == 'S':
        n = num-1
        if n == -1:
          n = 9999
      elif i == 'L':
        n = (num%1000)*10+num//1000
      else:
        n = (num%10)*1000+num//10
      if visited[n] == []:
        visited[n] = visited[num][:]
        visited[n].append(i)
        q.append(n)