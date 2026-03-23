N, K = map(int, input().split())

dp = [float('inf')] * (100_000 + 1)

dp[N] = 0

from collections import deque
queue = deque([(N, 0)])

while queue:
    pos, curr = queue.popleft()
    if pos == K:
        print(curr)
        break
    if 0 <= 2 * pos < len(dp) and dp[2 * pos] > curr:
        dp[2 * pos] = curr
        queue.appendleft((2*pos, curr))
    if 0 <= pos + 1 < len(dp) and dp[pos+1] > curr + 1:
        dp[pos+1] = curr + 1
        queue.append((pos+1, curr+1))
    if 0 <= pos - 1 < len(dp) and dp[pos-1] > curr + 1:
        dp[pos-1] = curr + 1 
        queue.append((pos-1, curr+1))