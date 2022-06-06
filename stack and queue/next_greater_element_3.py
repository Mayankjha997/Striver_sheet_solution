def next_greater_element_3(n):
    nums = list(map(int,str(n)))
    
    index = len(nums) - 2
    while index >= 0 and nums[index] >= nums[index+1]:
        index -= 1
    if index == -1:
        return -1
    
    index2 = len(nums) - 1
    while nums[index2] <= nums[index]:
        index2-=1
        
    nums[index],nums[index2] = nums[index2],nums[index]
    nums[index+1:] = reversed(nums[index+1:])
    
    result = ""
    for n in nums:
        result += str(n)
        
    if int(result) < 2**31:
        return int(result)
    else:
        return -1
    

n = int(input("enter the number "))
v = next_greater_element_3(n)
print(v)
     