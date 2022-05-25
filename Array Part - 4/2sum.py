def two_sum(nums,target):    #here nums is an list of integers that contains negative values also , and target is the target number to find
    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            sum = nums[j] + nums[i]
        if sum == target:
            return [i,j]
        


            