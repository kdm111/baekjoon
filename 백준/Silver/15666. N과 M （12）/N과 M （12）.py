n, m = map(int, input().split())
nums = sorted(set(map(int, input().split())))

curr = [-1] * m
def solve(depth, start):
    if depth == m:
        print(*curr)
        return
    for i in range(start, len(nums)):
        curr[depth] = nums[i]
        solve(depth+1, i)

solve(0, 0)