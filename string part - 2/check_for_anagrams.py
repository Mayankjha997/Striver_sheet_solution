def check_for_anagrams(s,t):
    dict = {}
    dics = {}
    
    for str in s:
        if str in dics:
            dics[str] += 1
        else:
            dics[str] = 1
            
    for letter in t:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    
    for stri in dics:
        if stri not in dict:
            return False
        else:
            if dics[stri] == dict[stri]:
                continue
            else:
                return False
    return True
            
    
    
    #if len(s) != len(t):
    # return False
    # return sorted(s) == sorted(t)


s = input("enter the string1 ")
t = input("enter the string2 ")
print(check_for_anagrams(s,t))