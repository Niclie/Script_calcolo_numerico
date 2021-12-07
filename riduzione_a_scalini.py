import numpy as np

def riduzione_a_scalini(m):
    r, c = m.shape
    a = np.copy(m)
    
    y = 0
    for k in range(r-1):
        if k + y >= c:
            break
        
        if a[k][k+y] == 0:
            c_row = -1
            z = 1
            while k+z < r and a[k+z][k+y] == 0:
                z += 1
                
            if k+z < r:
                c_row = k+z
                        
            if c_row != -1:
                a[[k, c_row]] = a[[c_row, k]]
            else:
                while k+y < c and a[k][k+y] == 0:
                    y += 1
        
        for i in range(k+1, r):
            m = -(a[i][k+y]/a[k][k+y])
            for j in range(0, c):
                a[i][j] = a[i][j]+(m*a[k][j])
                
    return a


def main():
    """a = np.array([[1, -2, -3, 0, 1, 0],
                  [-2, 4, 6, 0, -1, 2], 
                  [1, 0, 1, -2, 1, 0], 
                  [0, -2, -4, 2, 2, 1]])"""
    
    a = np.array([[1, 1, -2], [1, -1, 1], [2, 0, -1]])
    #a = np.array([[2, -1], [1, 3], [1, -4], [4, -2]], float)
    print(a, "\n")
    
    print(riduzione_a_scalini(a))
    
    return

if __name__ == '__main__':
    main()