# prerequiste - 1) longest_common_subsequence  and 2) longest_palindromic_subsequence

def minimum_insertion_to_make_string_palindrome(s):
    text2 = s[::-1]
    n,m = len(s),len(text2)
    dp = [[0] * (m+1) for z in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            if s[i] == text2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
                
    return (n - dp[-1][-1])


s = input("enter the string ")
v = minimum_insertion_to_make_string_palindrome(s)
print(v)