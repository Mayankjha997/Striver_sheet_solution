def missing_Number(nums):
    res = len(nums)
    for i in range(len(nums)):
        res =res - nums[i] + i
    return res

nums = []
n = int(input("enter nmber of elements"))
for i in range(n):
    v = int(input("enter elements"))
    nums.append(v)
print(nums)
print(missing_Number(nums))
