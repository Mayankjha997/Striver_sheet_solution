def word_break(s,worddict):
    dp = [True] + [False] * len(s)
    for i in range(1,len(s)+1):
        for word in worddict:
            if dp[i - len(word)] and s[:i].endswith(word):
                dp[i] = True
    return dp[-1]    
    
s = input("enter the string to match with the worddict ")
worddict = list(map(str,input("enter the wordbreak ").strip().split()))
print(s)
print(worddict)
v = word_break(s,worddict)
print(v)