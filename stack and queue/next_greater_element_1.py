def next_greater_element_1(nums1,nums2):
    dic = {}
    stack = []
    
    for n in nums2:
        while stack and stack[-1] < n:
            k = stack.pop()
            dic[k] = n
        stack.append(n)
        
    return [dic.get(n,-1) for n in nums1]

nums1 = list(map(int,input("enter the number for first array ").strip().split()))
nums2 = list(map(int,input("enter the number for second array ").strip().split()))
v = next_greater_element_1(nums1,nums2)
print(v)