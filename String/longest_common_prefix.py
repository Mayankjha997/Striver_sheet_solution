def longest_common_prefix(strs):
    if len(strs) == 0:
        return ""
    
    minlen = len(strs[0])
    for i in range(len(strs)):
        minlen = min(len(strs[i]) , minlen)
        
    i = 0
    res = ""
    while i < minlen:
        char = strs[0][i]
        for j in range(len(strs)):
            if strs[j][i] != char:
                return res
        res += char
        i += 1
    return res


strs = list(map(str,input("enter the string ").strip().split()))
print(strs)
v = longest_common_prefix(strs)
print(v)
            