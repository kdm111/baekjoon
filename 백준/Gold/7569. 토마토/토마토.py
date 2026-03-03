c, r, h = map(int, input().split())
tmp = 0
graph = []
for i in range(h):
    tmp_graph = []
    for _ in range(r):
        tmp_graph.append(list(map(int, input().split())))
    graph.append(tmp_graph)
            

total = r * c * h
from collections import deque
tomato = deque([])
rest = 0
for a in range(h):
    for b in range(r):
        for d in range(c):
            if graph[a][b][d] == 1:
                tomato.append((a,b,d))
            elif graph[a][b][d] == 0:
                rest += 1

ans = 0
while rest > 0 and tomato:
    temp = []
    ans += 1
    for t in tomato:
        c_h, c_r, c_c = t
        for dh, dr, dc in [[1,0,0], [0,1,0], [0,0,1], [0,0,-1],[0,-1,0],[-1,0,0]]:
            n_h = c_h + dh
            n_r = c_r + dr
            n_c = c_c + dc
            if 0 <= n_h < h and 0 <= n_r < r and 0 <= n_c < c and graph[n_h][n_r][n_c] == 0:
                rest -= 1
                temp.append((n_h, n_r, n_c))
                graph[n_h][n_r][n_c] = 1
    tomato = temp[:]

print(ans if rest == 0 else -1)
