c, r = map(int, input().split())
tmp = 0
graph = []

for _ in range(r):
    graph.append(list(map(int, input().split())))
            

total = r * c

from collections import deque
tomato = deque([])
rest = 0
for b in range(r):
    for d in range(c):
        if graph[b][d] == 1:
            tomato.append((b,d))
        elif graph[b][d] == 0:
            rest += 1

ans = 0
while tomato:
    temp = deque([])
    ans += 1
    for t in tomato:
        c_r, c_c = t
        for dr, dc in [[0,1], [1,0],[0,-1],[-1,0]]:
            n_r = c_r + dr
            n_c = c_c + dc
            if 0 <= n_r < r and 0 <= n_c < c and graph[n_r][n_c] == 0:
                rest -= 1
                temp.append((n_r, n_c))
                graph[n_r][n_c] = 1
    tomato = deque(temp)

print(ans-1 if rest == 0 else -1)