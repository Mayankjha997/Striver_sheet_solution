def single_element_in_a_sorted_array(nums):
    # time complexity - o(n) and space is also o(n)
    dic = {}
    for n in nums:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
            
    for n,val in dic.items():
        if val == 1:
            return n       
               
nums = list(map(int,input("enter the list of numbers ").strip().split()))
v = single_element_in_a_sorted_array(nums)
print(v)