from pkg_resources import safe_extra


def largest_rectangle_in_histogram(heights):
    stack = []
    maxarea = 0
    
    for i,h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index,height = stack.pop()
            maxarea = max(maxarea, height * (i - index))
            start = index
        stack.append((start,h))
        
    for i,h in stack:
        maxarea = max(maxarea, h * (len(heights) - i))
        
    return maxarea


heights = list(map(int,input("enter the heights ").strip().split()))
v = largest_rectangle_in_histogram(heights)
print(v)