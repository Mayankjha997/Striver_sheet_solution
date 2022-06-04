def longest_palindromic_subsequence(s):
    text2 = s[::-1]
    n = len(s)
    m = len(text2)
    
    dp = [[0]* (m+1) for z in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            if s[i] == text2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
    
    return dp[-1][-1]


s = input("enter the string ")
v = longest_palindromic_subsequence(s)
print(v)