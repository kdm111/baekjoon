N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dp = [[[0]*3 for _ in range(N)] for _ in range(N)]

dp[0][1][0] = 1
for r in range(N):
    for c in range(N):
        for d in range(3):
            if graph[r][c] == 1:
                continue
            if d == 0 and c-1 > 0 and graph[r][c-1] == 0:
                dp[r][c][d] = dp[r][c-1][0] + dp[r][c-1][2]
            if d == 1 and r-1 > 0 and graph[r-1][c] == 0: 
                dp[r][c][d] = dp[r-1][c][1] + dp[r-1][c][2]
            if d == 2 and r > 0 and c > 0 and graph[r][c-1] == 0 and graph[r-1][c-1] == 0 and graph[r-1][c] == 0:
                dp[r][c][d] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]

print(sum(dp[-1][-1][i] for i in range(3)))