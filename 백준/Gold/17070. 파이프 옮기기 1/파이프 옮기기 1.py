N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

ans = 0
def is_safe_diagonal(r,c):
    global N
    return (0 <= r + 1 < N and
            0 <= c + 1 < N and
            graph[r+1][c] == 0 and
            graph[r][c+1] == 0 and
            graph[r+1][c+1] == 0)

def solve(r,c,dir):
    global ans, N

    if r == N-1 and c == N-1:
        return 1
    ret = 0
    if dir == 'h' or dir == 'd':
        if 0 <= c + 1 < N and graph[r][c+1] == 0:
            ret += solve(r,c+1, 'h')
    if dir == 'v' or dir == 'd':
        if 0 <= r + 1 < N and graph[r+1][c] == 0:
            ret += solve(r+1,c,'v')
    if is_safe_diagonal(r, c):
        ret += solve(r+1,c+1,'d')
    return ret
print(solve(0,1,'h'))
