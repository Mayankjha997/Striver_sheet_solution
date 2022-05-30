def median_of_two_sorted_array(nums1,nums2):
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2
    
    if len(A) > len(B):  #as we want a array length should be less
        A,B = B,A
    
    l = 0
    r = len(A) - 1
    
    while True:
        i = (l+r) // 2
        j = half - i - 2  # 2 because array A and array B are starting with 0 index
        
        aleft = A[i] if i >= 0 else float("-infinity")
        aright = A[i+1] if (i+1) < len(A) else float("infinity")
        bleft = B[j] if j >= 0 else float("-infinity")
        bright = B[j+1] if (j+1) < len(B) else float("infinity")
        
        if aleft <= bright and bleft <= aright:
            #odd side
            if total % 2 == 1:
                return min(aright, bright)
            else: #even side
                return (max(aleft,bleft) + min(aright, bright)) / 2
            
        elif aleft > bright:
            r = i - 1
        else :
            l = i + 1
            

nums1 = list(map(int, input("enter the number for first arrray ").strip().split()))
nums2 = list(map(int, input("enter the number for second arrray ").strip().split()))
print(nums1)
print(nums2)
v = median_of_two_sorted_array(nums1, nums2)
print(v)

            
            
    