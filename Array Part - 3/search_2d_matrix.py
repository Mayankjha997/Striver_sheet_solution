def search_2d_matrix(matrix,target):
    rows = len(matrix)
    cols = len(matrix[0])
    top , bottom = 0 , len(matrix) - 1
    while top <= bottom:
        row = (top+bottom) // 2
        if target < matrix[row][0]:
            bottom = row - 1
        elif target > matrix[row][-1]:
            top = row + 1
        else:
            break
        
    if not(top <= bottom):
        return False
    
    row = (top+bottom) // 2
    l , r = 0 , cols-1
    while l <= r:
        m = (l+r) // 2
        if target < matrix[row][m]:
            r = m - 1
        elif target > matrix[row][m]:
            l = m + 1
        else :
            return True
    return False                   


target = int(input("enter the target number to search "))
r = int(input("enter nmber of rows "))
c = int(input("enter number of columns "))
matrix = []
for i in range(r):
    l = []
    for j in range(c):
        v = int(input("enter the element of the matrix "))
        l.append(v)
    matrix.append(l)
print(matrix)
search_2d_matrix(matrix, target)

