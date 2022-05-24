def subarray_with_given_xor(nums,target):
    dict ={}
    count = 0
    xor = 0
    for i in nums:
        xor = xor ^ i
        if xor ^ target in dict:
            count += dict[xor ^ target]
        if xor == target:
            count += 1 

        if xor in dict:
            dict[xor] += 1
        else:
            dict[xor] = 1
            
    return count


nums = []
target = int(input("enter the target XOR number "))
n = int(input("enter number of elements "))
for i in range(n):
    v = int(input("enter elements "))
    nums.append(v)
print(nums)
z = subarray_with_given_xor(nums,target)
print(z)