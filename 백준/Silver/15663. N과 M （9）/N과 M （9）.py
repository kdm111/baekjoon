n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

seen = set()
def solve(curr):
    if len(curr) == m:
        print(*curr)
        return
    prev = set()
    for i in range(0, n):
        if i in seen:
            continue
        if nums[i] in prev:
            continue
        seen.add(i)
        curr.append(nums[i])
        prev.add(nums[i])
        solve(curr)
        seen.remove(i)
        curr.pop()

solve([])