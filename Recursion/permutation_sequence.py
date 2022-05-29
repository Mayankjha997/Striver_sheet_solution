import math

def permutation_sequence(n,k):
    output =[]
    
    nums = [str(i) for i in range(1,n+1)]
    factorial = math.factorial(n)
    index = k-1
    
    while nums:
        factorial = factorial//len(nums)
        pos = index // factorial
        number = nums.pop(pos)
        output.append(number)
        index = index % factorial
    
    return "".join(output)

n = int(input("enter the sequence number "))
k = int(input("enter the kth permutation to find "))
v = permutation_sequence(n,k)
print(v)