def implement_strstr(haystack, needle):
    if needle == "":
        return 0
    
    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                break
            if j == len(needle) - 1:
                return i
            
    return -1


haystack = input("enter the text ")
needle = input("enter the pattern to search ")
v = implement_strstr(haystack,needle)
print(v)