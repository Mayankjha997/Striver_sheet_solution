def subsets2(nums):
    nums.sort()
    result = [[]]
    for n in nums:
        temp = []
        for l in result:
            temp.append(l + [n])
        result.extend(temp)
    
    return [list(l) for l in set([tuple(i) for i in result])]
            
test_cases = int(input())
nums = list(map(int,input("enter the numbers ").strip().split()))
print(nums)
v = subsets2(nums)
print(v)