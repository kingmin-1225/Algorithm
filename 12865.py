# 평범한 배낭
# 골드5

import sys
input=lambda:sys.stdin.readline().rstrip()

n, k = map(int, input().split())

dp = [0 for _ in range(k+1)]

for _ in range(n):
  w, v = map(int, input().split())
  for i in range(k-w, -1, -1):
    dp[i+w] = max(dp[i+w], dp[i]+v)
print(max(dp))