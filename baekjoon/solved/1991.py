
import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
tree = {}

for _ in range(n):
  node, left, right = input().split()
  tree[node] = [left, right]

preorderList = []
inorderList = []
postorderList = []

def preorderTraversal(node):
  if node == ".":
    return
  preorderList.append(node)
  left, right = tree[node]
  preorderTraversal(left)
  preorderTraversal(right)

def inorderTraversal(node):
  if node == ".":
    return
  left, right = tree[node]
  inorderTraversal(left)
  inorderList.append(node)
  inorderTraversal(right)

def postorderTraversal(node):
  if node == ".":
    return
  left, right = tree[node]
  postorderTraversal(left)
  postorderTraversal(right)
  postorderList.append(node)


preorderTraversal('A')
inorderTraversal('A')
postorderTraversal('A')

print(*preorderList, sep="")
print(*inorderList, sep="")
print(*postorderList, sep="")