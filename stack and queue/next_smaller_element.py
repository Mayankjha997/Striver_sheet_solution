def nearestSmallerToLeft(arr):
    stack = []
    result = []

    for i in range(len(arr)):
        if len(stack) == 0:
            result.append(-1)
            stack.append(arr[i])
        elif len(stack) != 0:
            while(len(stack) > 0 and stack[-1] > arr[i]): 
                stack.pop()
            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1])
            stack.append(arr[i])
        
    return result

arr = list(map(int,input("enter the numbers ").strip().split()))
v = nearestSmallerToLeft(arr)
print(v)

