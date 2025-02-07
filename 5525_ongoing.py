# IOIOI
# 실버1

import sys
input=lambda:sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
S = input()

ans = 0
for i in range(m-2*n):
  key = True
  for j in range(n+1):
    if S[i+j] != S[i+2*n-j] or not ((j % 2 == 0 and S[i+j] == "I") or (j % 2 == 1 and S[i+j] == "O")):
      key = False
      break
  if key:
    ans += 1
print(ans)