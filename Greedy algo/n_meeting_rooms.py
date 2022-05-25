def n_meeting_rooms(s,f):
    l = []
    for i in range(len(s)):
        l.append([s[i],f[i],i+1])
    
    l.sort(key = lambda x : x[1])
    
    ans = [l[0][2]]
    end_time = l[0][1]
    
    for i in range(1,len(s)):
        if l[i][0] > end_time:
            ans.append(l[i][2])
            end_time = l[i][1]
            
    return len(ans)

test_cases = int(input("test cases "))
for i in range(test_cases):
    s = list(map(int, input("enter the initial time ").strip().split()))
    f = list(map(int, input("enter the final time ").strip().split()))
print(s)
print(f)
v = n_meeting_rooms(s,f)
print(v)
            