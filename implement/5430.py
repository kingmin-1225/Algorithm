# AC
# 골드5

import sys
input=lambda:sys.stdin.readline().rstrip()

for _ in range(int(input())):
  p = input()
  n = int(input())
  arr = input().replace("[", "").replace("]", "")
  arr = list(map(int, arr.split(","))) if arr != "" else []
  left = 0
  right = n
  to_right = True
  for order in p:
    if order == "R":
      to_right = not to_right
    else:
      n -= 1
      if to_right:
        left += 1
      else:
        right -= 1
  if n < 0:
    print("error")
    continue
  if to_right:
    print("[", end="")
    print(*arr[left:right], sep=",", end="")
    print("]")

  else:
    print("[", end="")
    print(*list(reversed(arr[left:right])), sep=",", end="")
    print("]")