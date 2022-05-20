#majority element where elements > n/2
def majority_elements(nums):
    dic ={}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        if dic[num] > len(nums) //2:
            return num
        else:
            dic[num] += 1
            
nums = []
n = int(input("enter number of elements "))
for i in range(n):
    v = int(input("enter elements "))
    nums.append(v)
print(nums)
print(majority_elements(nums))