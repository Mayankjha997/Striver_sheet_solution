def valid_parenthesis():
    stack = []
    dic ={")" : "(", "}" :"{" , "]" : "["}
    
    for c in s:
        if c in dic:
            if stack and stack[-1] == dic[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
            
    return True if not stack else False


s = input("enter the brckets ")
v = valid_parenthesis(s)
print(v)