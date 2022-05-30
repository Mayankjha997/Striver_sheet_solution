def nth_root_of_m(n,m):
    for i in range(m+1):
        data = i ** n
        if data == m:
            return i
        elif data > m:
            return -1
        else:
            continue
        
        

n = int(input("enter the number "))
m = int(input("enter the number to find the square root "))
v = nth_root_of_m(n,m)
print(v)