def the_celebrity_problem(arr):
    n = len(arr)
    stack = []
    for i in range(n):
        stack.append(i)
    
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        
        if arr[a][b] == 1:
            stack.append(b)
        else:
            stack.append(a)
            
    pc = stack.pop()
    
    for i in range(n):
        if i!= pc:
            if arr[i][pc] == 0 or arr[pc][i] == 1: #i that does not know potential or potential doesnot knows i then false
                return -1
    
    return pc

rows = int(input("enter the number of rows "))
cols = int(input("enter the number of columns "))
arr = []
for i in range(rows):
    l = []
    for j in range(cols):
        x = int(input("enter the number "))
        l.append(x)
    arr.append(l)
print(arr)
v = the_celebrity_problem(arr)
print(v)