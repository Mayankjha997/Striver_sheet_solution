def maximum_subbarray(nums):
    total_sum = max_sum = nums[0]
        
    for i in nums[1:]:
        total_sum = max(i,total_sum+i)
        max_sum = max(max_sum,total_sum)
        
    return max_sum



l = int(input("enter number of digits "))
nums = []
for i in range(l):
    v = int(input("enter numbers "))
    nums.append(v)

print(nums)
print(maximum_subbarray(nums))
