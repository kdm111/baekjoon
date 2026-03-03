mp = [i for i in range(0, 101)]
ladder, snake = map(int, input().split())
for _ in range(ladder + snake):
    loc, to = map(int, input().split())
    mp[loc] = to

loc = {1 : 0}
from collections import deque
queue = deque([(1, 0)])
while queue:
    c, k = queue.popleft()
    if c == 100:
        break
    for i in range(1, 7):
        if c+i > 100 or mp[c+i] in loc:
            continue
        loc[mp[c+i]] = k + 1
        queue.append((mp[c+i], k+1))
#print(loc) 
print(loc.get(100, -1))