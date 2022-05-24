def largest_subarray_with_zero_sum(nums):
    maxi = 0
    sum1 = 0
    dict = {}
    for i in range(len(nums)):
        sum1 += nums[i]
        if sum1 == 0:
            maxi = i + 1
        else:
            if sum1 in dict:
                maxi = max(maxi, i - dict.get(sum1))
            else:
                dict[sum1] = i             
    return maxi


nums = []
n = int(input("enter number of elements "))
for i in range(n):
    v = int(input("enter elements "))
    nums.append(v)
print(nums)
v = largest_subarray_with_zero_sum(nums)
print(v)
                
                