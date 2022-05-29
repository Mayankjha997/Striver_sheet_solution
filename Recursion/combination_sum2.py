def combination_sum2(nums,target):
    result = []
    def dfs(sub_list,index):
        sum_of_list = sum(sub_list)
        if sum_of_list == target:
            if sorted(sub_list) not in result:
                result.append(sorted(sub_list))
            return
        if sum_of_list > target:
            return
        for i in range(index,len(nums)):
            sub_list.append(nums[i])
            dfs(sub_list,i+1)
            sub_list.pop()
        
    dfs([],0)
    return result


test_cases = int(input())
target = int(input("enter the target number to find "))
nums = list(map(int,input("enter the numbers ").strip().split()))
print(nums)
v = combination_sum2(nums,target)
print(v)