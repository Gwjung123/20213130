import numpy as np

A = np.array ([[2,5]
            ,  [1,3] , 
               [4,1]])

B = np.array ([[4,-1]
              ,[2,3] , 
               [6,2]])

C = np.array ([[1,2,2] , 
              [3,4,5]])

m = np.matmul(B,C)
m2 = np.matmul(C , A)

print(A+B)

print(B-A)

print(m)

print(m2)


