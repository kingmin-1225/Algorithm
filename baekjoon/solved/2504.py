# 괄호의 값
# 골드5

import sys
input=lambda:sys.stdin.readline().rstrip()

words = input()
stack = []
answer = True
for word in words:
  if not answer:
    break
  if word in "([":
    stack.append(word)
  elif word in ")]":
    ans = 0
    for i in range(len(stack)+1):
      if stack == []:
        answer = False
        break
      key = stack.pop()
      if key.isdigit():
        ans += int(key)
      elif key == "(" and word==")":
        if ans == 0:
          ans += 1
        ans *= 2
        stack.append(str(ans))
        break
      elif key == "[" and word=="]":
        if ans == 0:
          ans += 1
        ans *= 3
        stack.append(str(ans))
        break
      else:
        answer = False
        break

if answer:
  ans = 0
  for i in stack:
    if i.isdigit():
      ans += int(i)
    else:
      ans = 0
      break
  print(ans)
else:
  print(0)