def  maximum_sum_inccreasing_subsequence(nums,n):
    dp = [0] * n
    max = 0
    
    for i in range(n):
        dp[i] = nums[i]
    
    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
                dp[i] = dp[j] + nums[i]
                
    for i in range(n):
        if max < dp[i]:
            max = dp[i]
            
    return max
            
nums = list(map(int,input("enter the numbers").strip().split()))
print(nums)
n = len(nums)
v = maximum_sum_inccreasing_subsequence(nums,n)
print(v)