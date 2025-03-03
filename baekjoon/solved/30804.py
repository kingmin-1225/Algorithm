# 과일 탕후루
# 실버2

import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
fruits = list(map(int, input().split()))

pnt = [[fruits[0], 1, 0]]
for i in range(1, n):
  if fruits[i] == pnt[-1][0]:
    pnt[-1][1] += 1
  else:
    pnt.append([fruits[i], 1, 0])

ans = pnt[0][1]
temp = pnt[0][1]

for i in range(1, len(pnt)):
  if pnt[i-1][2] == 0 or pnt[i-1][2] == pnt[i][0]:
    pnt[i][2] = pnt[i-1][0]
    temp += pnt[i][1]
  else:
    temp = pnt[i-1][1]+pnt[i][1]
    pnt[i][2] = pnt[i-1][0]
  ans = max(ans, temp)

print(ans)