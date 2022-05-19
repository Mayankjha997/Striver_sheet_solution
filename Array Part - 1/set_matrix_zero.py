def set_matrix_zero(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    row0_0 = 0
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    row0_0 = True
                    
    for r in range(1,rows):
        for c in range(1,cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    
    
    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0
            
    if row0_0:
        for c in range(cols):
            matrix[0][c] = 0
            
            
            
            
                       
r = int(input("enter rows"))
c = int(input("enter columns"))
matrix = []
for rows in range(r):
    l = []
    for cols in range(c):
        v = int(input())
        l.append(v)  
    matrix.append(l)
print(matrix)
set_matrix_zero(matrix)
print(matrix)
    
    