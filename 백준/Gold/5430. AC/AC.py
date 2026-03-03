for _ in range(int(input())):
    cmd = input()
    l = input()
    inp = input()
    if inp == "[]":
        nums = []
    else:
        nums = list(map(int, inp[1:-1].split(",")))
    l, r, flag, error = 0, len(nums)-1, True, False
    for c in cmd:
        if c == "R":
            flag = not flag
        if c == "D":
            if l > r:
                print("error")
                error = True
                break
            elif flag:
                l += 1
            else:
                r -= 1
    if not error:
        nums = nums[l:r+1]
        if not flag:
            nums.reverse()
        print("[", end="")
        for i in range(len(nums)):
            print(f"{nums[i]}{',' if i != len(nums) -1 else ''}",end="")
        print("]")