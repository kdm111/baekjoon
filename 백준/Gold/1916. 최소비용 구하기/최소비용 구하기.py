N = int(input())
M = int(input())
mp = {}
for i in range(1, N+1):
    mp.setdefault(i, [])

for _ in range(M):
    a,b,c = map(int, input().split())
    mp[a].append((b,c))
at, to = map(int, input().split())
import heapq

heap = [(at, 0)]
dist = [float('inf')] * (N + 1)
dist[at] = 0

while heap:
    curr, cost = heapq.heappop(heap)
    if cost > dist[curr]:
        continue
    for nxt,val in mp[curr]:
        n_cost = cost + val
        if n_cost < dist[nxt]:
            dist[nxt] = n_cost
            heapq.heappush(heap, (nxt, n_cost))
print(dist[to])