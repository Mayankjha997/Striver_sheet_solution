def next_permutation(nums):
    length = len(nums)
    if length <= 2:
        return nums.reverse()
    
    pointer = length - 2
    while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
        pointer-=1
        
    if pointer == -1:
        return nums.reverse()
    
    for i in range(length-1,pointer,-1):
        if nums[pointer] < nums[i]:
            nums[pointer],nums[i] = nums[i],nums[pointer]
            break
        
    nums[pointer+1:] = reversed(nums[pointer+1:])
    
    
l = int(input("enter number of digits "))
nums = []
for i in range(l):
    v = int(input("enter a number to be permuted "))
    nums.append(v)

print(nums)
next_permutation(nums)
print(nums)
        