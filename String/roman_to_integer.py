def roman_to_integer(s):
    dic = {"I":1,
           "V":5,
           "X":10,
           "L":50,
           "C":100,
           "D":500,
           "M":1000,  }
    
    total  = 0
    curr = 0
    prev = 0
    
    for i in range(len(s)):
        curr = dic[s[i]]
        if curr > prev:
            total = total + curr - 2*prev
        else:
            total = total + curr
        
        prev = curr
        
    return total

s = input("enter the string ")
v = roman_to_integer(s)
print(v)