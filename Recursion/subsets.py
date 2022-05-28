def subsets(nums):
    result = [[]]
    
    for n in nums:
        result += [i + [n]for i in result]
        
    return result

test_cases = int(input())
nums = list(map(int,input("enter the numbers ").strip().split()))
print(nums)
v = subsets(nums)
print(v)