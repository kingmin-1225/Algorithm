# 1로 만들기
# 실버3

import sys
input=lambda:sys.stdin.readline().rstrip()

n = int(input())
dp = [i for i in range(n+1)]

for i in range(1, n+1):
  dp[i] = min(dp[i], dp[i-1]+1)
  if i*2 < n+1:
    dp[i*2] = min(dp[i*2], dp[i]+1)
  if i*3 < n+1:
    dp[i*3] = min(dp[i*3], dp[i]+1)
print(dp[n]-1)

