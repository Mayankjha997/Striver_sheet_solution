def first_and_last_occurance(nums,target):
    left_part = search(nums,target,True)
    right_part = search(nums,target,False)
    return [left_part, right_part]
    
def search(nums,target,leftbias):
    l = 0
    r = len(nums) - 1
    ans = -1
    while l <= r:
        mid = (l+r) // 2
        if target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        else:
            ans = mid
            if leftbias:
                r = mid - 1
            else:
                l = mid + 1
    
    return ans 
                
                
nums = list(map(int,input("enter the numbers ").strip().split()))
target = int(input("enter the target "))
v = first_and_last_occurance(nums,target)
print(v)