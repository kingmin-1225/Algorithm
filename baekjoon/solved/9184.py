# 신나는 함수 실행
# 실버2

import sys
input=lambda:sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())
dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
dp[0][0][0] = 1

for d in range(20):
  for dx, dy, dz in [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]:
    x, y, z= d+dx, d+dy, d+dz
    if x <= 0 or y <= 0 or z <= 0:
      dp[x][y][z] = 1
    elif x < y < z:
      dp[x][y][z] = dp[x][y][z-1]+dp[x][y-1][z-1]-dp[x][y-1][z]
    else:
      dp[x][y][z] = dp[x-1][y][z] + dp[x-1][y-1][z] + dp[x-1][y][z-1] - dp[x-1][y-1][z-1]


while not (a==b==c==-1):
  if a <= 0 or b <= 0 or c <= 0:
    print(f'w({a}, {b}, {c}) = 1')
  elif a > 20 or b > 20 or c > 20:
    print(f'w({a}, {b}, {c}) = {dp[20][20][20]}')
  else:
    print(f'w({a}, {b}, {c}) = {dp[a][b][c]}')
  a, b, c = map(int, input().split())