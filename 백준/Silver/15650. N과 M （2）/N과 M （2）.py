n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]

def print_arr(arr):
    for i in arr:
        print(i, end= " ")
    print()
def solve(curr, idx):
    if len(curr) == m:
        print_arr(curr)
        return 
    for i in range(idx, n):
        curr.append(nums[i])
        solve(curr, i+1)
        curr.pop()

solve([], 0)