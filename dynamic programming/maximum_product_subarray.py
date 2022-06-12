def maximum_product_subarray(nums):
    max_pro = nums[0]
    min_pro = nums[0]
    result = nums[0]
    
    for i in range(1,len(nums)):
        curr = nums[i]
        temp_max = max(curr,curr * max_pro,curr * min_pro)
        min_pro = min(curr,curr * max_pro,curr * min_pro)
        max_pro = temp_max
        result = max(result,max_pro)
        
    return result



nums = list(map(int,input("enter the numbers").strip().split()))
print(nums)
v = maximum_product_subarray(nums)
print(v)