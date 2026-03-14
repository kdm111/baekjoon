
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]
dp[0][0] = graph[0][0]
for i in range(1, N):
    dp[0][i] = graph[0][i] + dp[0][i-1]
    dp[i][0] = graph[i][0] + dp[i-1][0]

for r in range(1, N):
    for c in range(1, N):
        dp[r][c] = dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1] + graph[r][c]


for _ in range(M):
    x1, y1, x2, y2 = map(lambda x : int(x) - 1, input().split())
    ans = dp[x2][y2]
    if x1-1 >= 0:
        ans -= dp[x1-1][y2]
    if y1-1 >= 0:
        ans -= dp[x2][y1-1]
    if x1-1 >= 0 and y1-1 >= 0:
        ans += dp[x1-1][y1-1]
    print(ans)
    
    