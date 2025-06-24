# 곱셈
# 실버1

import sys
input = lambda:sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())

toBinary = []
while b > 0:
  toBinary.append(b%2)
  b //= 2

mod = [a for _ in range(len(toBinary))]
ans = 1
for i in range(len(mod)):
  if i > 0:
    mod[i] = (mod[i-1]**2)%c
  if toBinary[i] == 1:
    ans *= mod[i]%c
print(ans%c)