graph = []
for _ in range(int(input())):
    graph.append(list(map(int, input().split())))

dp = [graph[0][:] for _ in range(len(graph))]
for i in range(1, len(graph)):
    dp[i][0] = min(graph[i][0]+dp[i-1][1], graph[i][0] + dp[i-1][2])
    dp[i][1] = min(graph[i][1]+dp[i-1][0], graph[i][1] + dp[i-1][2])
    dp[i][2] = min(graph[i][2]+dp[i-1][1], graph[i][2] + dp[i-1][0])
    
print(min(dp[-1]))