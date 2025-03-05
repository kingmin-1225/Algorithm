
import sys
input = lambda:sys.stdin.readline().rstrip()

ans = []
people = {}

for _ in range(int(input())):
  name, state = input().split()
  ans.append(name)
  people[name] = state
ans = list(set(ans))
ans.sort(reverse=True)
for name in ans:
  if people[name] == "enter":
    print(name)