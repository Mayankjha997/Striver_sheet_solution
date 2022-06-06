def next_greater_element_2(nums1):
    stack = []
    result = [-1] * len(nums1)
    
    for i in range(2):
        for i,num in enumerate(nums1):
            while stack and nums1[stack[-1]] < num:
                result[stack.pop()] = num 
            stack.append(i)
            
    return result 


nums1 = list(map(int,input("enter the number for first array ").strip().split()))
v = next_greater_element_2(nums1)
print(v)