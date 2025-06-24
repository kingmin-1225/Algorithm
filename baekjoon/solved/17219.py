# 비밀번호 찾기
# 실버4

import sys
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
passwords = {}
for _ in range(n):
  site, password = input().split()
  passwords[site] = password

for _ in range(m):
  print(passwords[input()])