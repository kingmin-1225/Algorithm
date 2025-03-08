

import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
words = input()
ans = 0
key = 0
idx = 0

while idx < m:
  if words[idx] == "I" and idx+2 < m and words[idx:idx+3] == "IOI":
    key += 1
    idx += 2
  else:
    if key-n+1 > 0:
      ans += key-n+1
    key = 0
    idx += 1

if key-n+1 > 0:
  ans += key-n+1

print(ans)