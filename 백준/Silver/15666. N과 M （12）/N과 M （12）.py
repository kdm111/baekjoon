n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums = sorted(set(nums))

def solve(curr):
    if len(curr) == m:
        print(*curr)
        return
    for i in range(len(nums)):
        if curr[-1] <= nums[i]:
            curr.append(nums[i])
            solve(curr)
            curr.pop()

for num in nums:
    solve([num])