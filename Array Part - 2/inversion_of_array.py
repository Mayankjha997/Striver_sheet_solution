def count_inversion(nums):
    inversion_count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                inversion_count += 1
                
    return inversion_count

nums = []
n = int(input("enter number of elements "))
for i in range(n):
    v = int(input("enter elements "))
    nums.append(v)
print(nums)
print(count_inversion(nums))