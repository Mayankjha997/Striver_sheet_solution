def subst_sums(nums):
    if sum(nums) % 2 == 1:
        return False
    
    dp = set()
    dp.add(0)
    target = sum(nums) // 2
    
    for i in range(len(nums)-1,-1,-1):
        nextdp = set()
        for t in dp:
            nextdp.add(t+nums[i])
            nextdp.add(t)
        dp = nextdp
    
    return True if target in dp else False


nums = list(map(int,input("enter the numbers ").strip().split()))
v = subst_sums(nums)
print(v)