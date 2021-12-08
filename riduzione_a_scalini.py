import numpy as np

def riduzione_a_scalini(m):
    r, c = m.shape
    a = np.copy(m)
    i = j = 0

    while i < r - 1 and j < c:
        if a[i][j] == 0:
            cond = True
            for k in range(i+1, r):
                if a[k][j] != 0:
                    a[[i, k]] = a[[k, i]]
                    cond = False
                    break
            
            if cond:
                while j < c and a[i][j] == 0:
                    j += 1
                
        
        row_diff_0 = np.where(a[i+1:, j] != 0)[0] + i + 1
        for row in row_diff_0:
            m = -(a[row][j]/a[i][j])
            for k in range(c):
                a[row][k] += m*a[i][k]
        i += 1
        j += 1
    
    return a

def rango(m):
    a = riduzione_a_scalini(m)
    r, c = a.shape
    i = j = 0

    rank = 0
    while i < r and j < c:
        while j < c and a[i][j] == 0:
            j += 1
        
        if j < c:
            rank += 1
        
        i += 1
        j += 1
    
    return rank
    

def main():
    """a = np.array([[1, -2, -3, 0, 1, 0],
                  [-2, 4, 6, 0, -1, 2], 
                  [1, 0, 1, -2, 1, 0], 
                  [0, -2, -4, 2, 2, 1]])"""
                  
    #a = np.array([[1, 1, -2], [1, -1, 1], [2, 0, -1]], float)
    #a = np.array([[2, -1], [1, 3], [1, -4], [4, -2]], float)
    #a = np.array([[1, 2, 0, -1], [2, 1, 1, 0]])
    a = np.array([[1, -1, 0, 1], [0, 1, 1, -1], [1, -2, -1, 2]])
    
    print(a, "\n")
    
    print(riduzione_a_scalini(a))
    print(rango(a))
    
    return

if __name__ == '__main__':
    main()