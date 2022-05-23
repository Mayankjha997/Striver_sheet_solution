def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            sum = nums[j] + nums[i]
        if sum == target:
            return [i,j]
        


            