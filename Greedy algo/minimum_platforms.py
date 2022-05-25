def minimum_platforms(arr,dep):
    n = len(arr)
    arr.sort()
    dep.sort()
    
    platfrom = 1
    maximum_platforms = 1
    i = 1 #for arr
    j = 0 #for dep
    
    while i < n and j < n:
        if arr[i] <= dep[j]:
            platfrom += 1
            i+=1
            if platfrom > maximum_platforms:
                maximum_platforms = platfrom
        else :
            platfrom -= 1
            j+=1
                  
    return maximum_platforms


test_cases = int(int(input("enter the number of test cases to run ")))
for i in range(test_cases):
    arr = list(map(int,input("enter the arrival time of the train ").strip().split()))
    dep = list(map(int,input("enter the departure time of the train ").strip().split()))
    
print(arr)
print(dep)
v = minimum_platforms(arr,dep)
print(v)

        
            
            
            
             
    
    