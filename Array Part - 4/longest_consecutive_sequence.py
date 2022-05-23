def longest_consecutive_seequence(nums):
    num = set(nums)
    longest = 0
    for n in num:
        if n-1 not in num:
            length = 0
            while length+n in num:
               length+=1
            longest = max(longest,length)
    
    return longest 


nums = []
n = int(input("enter number of elements "))
for i in range(n):
    v = int(input("enter elements "))
    nums.append(v)
print(nums)
v = longest_consecutive_seequence(nums)
print(v)