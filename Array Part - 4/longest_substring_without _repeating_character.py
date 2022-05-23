def longest_substring_without_repeating_character(string1):
    string1_set = set()
    l = 0
    result = 0
    for r in range(len(string1)):
        while string1[r] in string1_set:
            string1_set.remove(string1[l])
            l += 1
        string1_set.add(string1[r])
        result = max(result, r-l+1)
    return result


string1 = input("enter the string")
print(string1)
v = longest_substring_without_repeating_character(string1)
print(v) 
            
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
        