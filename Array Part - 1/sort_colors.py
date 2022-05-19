def sort_colors(nums):
    l = 0
    r = len(nums) - 1
    curr = 0
    
    while curr<=r:
        if nums[curr] == 0:
            nums[l],nums[curr] = nums[curr],nums[l]
            l+=1
            curr+=1
        elif nums[curr] == 2:
            nums[curr],nums[r] = nums[r],nums[curr]
            r-=1
        else:
            curr+=1
            

l = int(input("enter number of colors "))
nums = []
for i in range(l):
    v = int(input("enter a number between 0, 1, 2 "))
    nums.append(v)

print(nums)
sort_colors(nums)
print(nums)