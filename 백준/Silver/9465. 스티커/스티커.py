N = int(input())
for _ in range(N):
    L = int(input())

    sticker = []
    sticker.append(list(map(int, input().split())))
    sticker.append(list(map(int, input().split())))
    if L == 1:
        print(max(sticker[0][0], sticker[1][0]))
    elif L == 2:
        print(max(sticker[0][0]+sticker[1][1], sticker[1][0]+sticker[0][1]))
    else:
        dp = [[0] * L for _ in range(2)]
        dp[0][0] = sticker[0][0]; dp[1][0] = sticker[1][0]
        dp[0][1] = sticker[0][1]+sticker[1][0]; dp[1][1] = sticker[1][1]+sticker[0][0]
        for i in range(2, L):
            dp[0][i] = sticker[0][i] + max(dp[1][i-1], dp[1][i-2])
            dp[1][i] = sticker[1][i] + max(dp[0][i-1], dp[0][i-2])
        print(max(dp[0][-1], dp[1][-1]))
