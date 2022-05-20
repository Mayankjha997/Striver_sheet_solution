def pow_x_n(x,n):
    if n == 0:
        return 1
    elif n < 0:
        return pow_x_n(1/x , -n)
    elif n % 2 == 0:
        temp = pow_x_n(x,n/2)
        return temp * temp
    else:
        return x * pow_x_n(x,n-1) 
    
    
x =float(input("enter the number"))
n = int(input("enter the power"))
print(pow_x_n(x,n))