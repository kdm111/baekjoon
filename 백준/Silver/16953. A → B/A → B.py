s, g = map(int, input().split())

from collections import deque
queue = deque([(s, 1)])
ans = -1
while queue:
    c,k  = queue.popleft()
    if c == g:
        ans = k
        break
    if 2 * c <= g:
        queue.append((2*c, k + 1))
    if 2*c != c*10 + 1 and c*10 + 1 <= g:
        queue.append((c*10 + 1, k + 1))
print(ans)