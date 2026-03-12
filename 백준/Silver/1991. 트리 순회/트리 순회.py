def preorder(c):
    print(c,end="")
    if tree[c][0] and tree[c][0] != '.':
        preorder(tree[c][0])
    if tree[c][1] and tree[c][1] != '.':
        preorder(tree[c][1])

def inorder(c):
    if tree[c][0] and tree[c][0] != '.':
        inorder(tree[c][0])
    print(c,end="")
    if tree[c][1] and tree[c][1] != '.':
        inorder(tree[c][1])
def postorder(c):
    if tree[c][0] and tree[c][0] != '.':
        postorder(tree[c][0])
    if tree[c][1] and tree[c][1] != '.':
        postorder(tree[c][1])
    print(c,end="")
tree = {}
N = int(input())
for _ in range(N):
    val, left, right = input().split()
    tree[val] = (left, right)
ans = []
preorder('A')
print()
ans = []
inorder('A')
print()
ans = []
postorder('A')
print()
