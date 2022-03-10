import numpy as np

A = np.array([[2,3,4]
              ,[4,8,2]
               [1,2,1] ])

print(A[1])
print(A[: , 2])

print(A.T)
print(np.transpose(A))
