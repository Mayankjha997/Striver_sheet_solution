from cv2 import rotate


def rotate_image(matrix):
    n = len(matrix)
    matrix.reverse()
    for i in range(n):
        for j in range(i):
            matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
            
            
            
r = int(input("enter number of rows "))
c = int(input("enter number of columns "))
matrix = []
for i in range(r):
    l = []
    for j in range(c):
        v = int(input("enter value"))
        l.append(v)
    matrix.append(l)
print(matrix)
rotate_image(matrix)
print(matrix)

    
            