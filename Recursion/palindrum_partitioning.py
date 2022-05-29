def palindrum_partitioning(s):
    result = []
    part = []
    def backtrack(i):
        if i >= len(s):
            result.append(part.copy())
            return
        for j in range(i,len(s)):
            if ispali(s,i,j):
                part.append(s[i:j+1])
                backtrack(j+1)
                part.pop()
                
    def ispali(s,i,j):
        while i < j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True

    backtrack(0)
    return result

test_cases = int(input())
s = input("enter the string ")
print(s)
v = palindrum_partitioning(s)
print(v)
                