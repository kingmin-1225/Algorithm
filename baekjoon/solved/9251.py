# LCS
# 골드5

import sys
input = lambda:sys.stdin.readline().rstrip()

first_word = input()
second_word = input()

dp = [[0 for _ in range(len(second_word)+1)] for _ in range(len(first_word)+1)]
for x in range(1, len(first_word)+1):
  for y in range(1, len(second_word)+1):
    if first_word[x-1] == second_word[y-1]:
      dp[x][y] = dp[x-1][y-1]+1
    else:
      dp[x][y] = max(dp[x][y-1], dp[x-1][y])
print(dp[-1][-1])