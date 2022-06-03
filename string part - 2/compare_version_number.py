def compare_version_number(version1,version2):
    version1 = version1.split('.')
    version2 = version2.split('.')
    
    len1 = len(version1)
    len2 = len(version2)
    
    for i in range(max(len1,len2)):
        l1 = int(version1[i]) if i < len1 else 0
        l2 = int(version2[i]) if i < len2 else 0
        
        if l1 < l2:
            return -1
        elif l1 > l2:
            return 1
        
    return 0


version1 = input('enter version1 ')
version2 = input('enter version2 ')
v = compare_version_number(version1, version2)
print(v)
            