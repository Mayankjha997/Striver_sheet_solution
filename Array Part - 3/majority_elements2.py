#majority element where elements > n/3
def majority_elements2(nums):
    if nums == []:
        return [] 
    cand1, count1 = None, 0
    cand2, count2 = None, 0
    for num in nums:
        if cand1 == num:
            count1+=1
        elif cand2 == num:
            count2+=1
        elif count1 == 0:
            cand1 = num
            count1+=1
        elif count2 == 0:
            cand2 = num
            count2+=1
        else:
            count1 , count2 = count1 - 1, count2 - 1
    
    return[x for x in (cand1,cand2) if nums.count(x) > len(nums) // 3]  

nums = []
n = int(input("enter number of elements "))
for i in range(n):
    v = int(input("enter elements "))
    nums.append(v)
print(nums)
print(majority_elements2(nums))