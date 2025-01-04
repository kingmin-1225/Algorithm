# 설탕 배달
# 실버4

import sys
input=lambda:sys.stdin.readline().rstrip()

n = int(input())
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
  if i == 3 or i == 5:
    dp[i] = 1
    continue
  if dp[i-3] != 0:
    dp[i] = dp[i-3]+1
  if dp[i-5] != 0:
    dp[i] = dp[i-5]+1 if dp[i] == 0 else min(dp[i], dp[i-5]+1)
print(dp[n] if dp[n] != 0 else -1)