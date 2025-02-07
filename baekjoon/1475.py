# 방 번호
# 실버5

import sys
input=lambda:sys.stdin.readline().rstrip()

n = input()

nums = [0 for _ in range(9)]

for i in n:
  key = int(i)
  if key == 9:
    nums[6] += 1
  else:
    nums[key] += 1
if nums[6]%2 == 1:
  nums[6] = nums[6]//2+1
else:
  nums[6] = nums[6]//2
print(max(nums))
