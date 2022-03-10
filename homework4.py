
import numpy as np

A = np.array([[3,0] 
            , [-1,2] , 
            [1,1]])

B = np.array([[-3,-1] 
            , [2,1] , 
            [4,3]])

C = np.array([[1,2,3] 
            , [2,0,1]])

D = np.array([[1] , 
              [2] , 
              [3]])

print(A + 2*B)

m = np.matmul(A,C)

print(m)

print(3 * D)




