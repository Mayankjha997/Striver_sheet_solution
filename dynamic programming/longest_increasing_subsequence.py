def longest_increasing_subsequence(nums):
    Lis = [1] * len(nums)
    
    for i in range(len(nums)-1,-1,-1):
        for j in range(i+1,len(nums)):
            if nums[i] < nums[j]:
                Lis[i] = max(Lis[i], 1+Lis[j])
                
    return max(Lis)

nums = list(map(int,input("enter the numbers").strip().split()))
print(nums)
v = longest_increasing_subsequence(nums)
print(v)