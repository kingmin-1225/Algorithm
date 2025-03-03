# 패션왕 신해빈
# 실버3

import sys
input = lambda:sys.stdin.readline().rstrip()

for i in range(int(input())):
  clothes = {}
  for j in range(int(input())):
    name, kind = input().split()
    if kind in clothes:
      clothes[kind] += 1
    else:
      clothes[kind] = 1
  ans = 1
  for c in clothes:
    ans *= (clothes[c]+1)
  print(ans-1)