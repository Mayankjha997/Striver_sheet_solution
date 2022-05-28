def combination_sum(nums,target):
    nums.sort()
    result = []
    
    def helper(index, target, sublist):
        if target == 0:
            result.append(sublist)
        if target < 0:
            return
        for i in range(index,len(nums)):
            helper(i, target - nums[i],sublist + [nums[i]])
            
    helper(0,target,[])
    return result

test_cases = int(input())
target = int(input("enter the target number to find "))
nums = list(map(int,input("enter the numbers ").strip().split()))
print(nums)
v = combination_sum(nums,target)
print(v)
            
    