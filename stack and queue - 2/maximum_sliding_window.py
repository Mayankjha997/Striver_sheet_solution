import collections


def maximum_sliding_window(nums,k):
    output = []
    l = r = 0
    q = collections.deque()
     
    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q .append(r)
        
        
        if l > q[0]:
            q.popleft()
            
        if (r+1) >= k:
            output.append(nums[q[0]])
            l+= 1
        r += 1
        
    return output

nums = list(map(int,input("enter the numbers ").strip().split()))
k = int(input("enter the window length "))
v = maximum_sliding_window(nums,k)
print(v)
        
    
    