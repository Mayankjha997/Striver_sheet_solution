def search_in_a_rotated_sorted_array(nums,target):
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid
        
        #left sorted portion of array
        if nums[mid] >= nums[l]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
                
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
                
    return -1


nums = list(map(int,input("enter the array ").strip().split()))
target = int(input("enter the target number to find "))
v = search_in_a_rotated_sorted_array(nums, target)
print(v)
            
         