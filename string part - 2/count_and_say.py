def count_and_say(n):
    if n == 1:
        return "1"
    
    prev = count_and_say(n-1)
    count = 1
    res = ""
    p = len(prev)
    
    for i in range(p):
        if i == len(prev) - 1 or prev[i] != prev[i+1]:
            res+= str(count) + prev[i]
            count = 1
        else:
            count+=1
            
    return res


n = int(input("enter the number "))
v = count_and_say(n)
print(v)