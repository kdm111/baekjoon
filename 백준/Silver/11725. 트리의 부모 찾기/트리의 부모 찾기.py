from collections import defaultdict
tree = defaultdict(list)
n = int(input())
for _ in range(n-1):
    p, c = map(int, input().split())
    tree[c].append(p)
    tree[p].append(c)

ans = {}
seen = set([])
from collections import deque
stack = deque([])
stack.append((None, 1))
while stack:
    p, c = stack.pop()
    ans[c] = p
    seen.add(c)
    for g in tree[c]:
        if g not in seen:
            stack.append((c, g))

for i in range(2, n+1):
    print(ans[i])