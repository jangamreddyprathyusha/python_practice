# import numpy as np
# arr=np.array([1,2,3,4,5])
# l=[1,"raju",True,9.67,3]
# print(l)
# print(type(l))
# arr=np.array(l)
# print(arr)
# print(np.dtype)

# l=[1,2,3,4,5]
# arr=np.array([1,2,3,4,5])
# print(arr+2)
# for i in range(len(l)):
#     l[i]=(l[i]+2)
# print(l)
# print(l*2)

# l=[1,2,3,4,5]
# arr=np.array([1,'abc',3.4])
# print(arr.dtype)

# import numpy as np
# arr=np.array([1,2,3])
# print(arr.sum())
# print(sum(arr))
# print(np.sum(arr))
# print(np.max(arr))
# print(np.min(arr))
# print(np.mean(arr))

# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(np.mean(arr))
# print(np.median(arr))
# print(np.std(arr))
# print(np.var(arr))

# import numpy as np
# arr=np.array([1,2,3])
# print(arr)
# arr1=np.array([[1],[2],[3]])
# print(arr1)
# print(np.eye(2))
# print(np.identity(3))
# arr2=np.array([[1,2,3],[4,5,6]])
# print(arr2)
# print(arr2.shape)
# print(arr2.reshape(3,2))
# print(np.sum(arr2,axis=0))
# print(np.sum(arr2,axis=1))


# import numpy as np
# arr1=np.array([[1,2],[3,4]])
# arr2=np.array([[4,3],[2,1]])
# print(np.add(arr1,arr2))
# print(arr1+arr2)
# print(np.subtract(arr1,arr2))


# import numpy as np
# arr1=np.array([[1,2],[3,4]])
# arr2=np.array([[4,3,2],[2,1,1]])
# print(np.dot(arr1,arr2))
# print(np.matmul(arr1,arr2))
# print(arr1@arr2)
# print(arr2.T)
# print(arr2.flatten())

import numpy as np
arr1=np.array([[1,2,3],[3,4,4],[1,2,3]])
print(np.linalg.det(arr1))
