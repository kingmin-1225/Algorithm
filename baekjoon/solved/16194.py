# 카드 구매하기 2
# 실버1

import sys
input=lambda:sys.stdin.readline().rstrip()

n = int(input())
cards = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
  dp[i] = cards[i-1]
  for j in range(i):
    dp[i] = min(dp[i], dp[i-j-1]+cards[j])

print(dp[n])