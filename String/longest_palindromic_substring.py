def longest_palindromic_substring(s):
    res = ""
    for i in range(len(s)):
        odd = helper(s,i,i)
        even = helper(s,i,i+1)
        res = max(res,odd,even,key = len)
    return res


def helper(s,l,r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l-= 1
        r+= 1
    return s[l+1:r]

s = input("enter the string ")
v = longest_palindromic_substring(s)
print(v)     
    