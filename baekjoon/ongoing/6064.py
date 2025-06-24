
import sys
input = lambda:sys.stdin.readline().rstrip()

def gcd(x, y):
  if x < y:
    return gcd(y, x)
  if y == 0:
    return x
  else:
    return gcd(y, x%y)


for _ in range(int(input())):
  n, m, x, y = map(int, input().split())
  lcm = n*m//gcd(n, m)
  ans = -1
  for i in range(1, lcm+1):
    if i % n == x and i % m == y:
      ans = i
      break
  print(ans)