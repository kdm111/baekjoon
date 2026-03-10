N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

dp = graph[-1][:]

for i in range(N-1, -1, -1):
    for j in range(i):
        dp[j] = graph[i-1][j] + max(dp[j], dp[j+1])

print(max(dp))
        