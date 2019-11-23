import numpy as np

A = np.array (range(1,101))

A.resize (10,10)

x = A**2
print (x)
print ("Elements that are divisible by 3: ")

X= x[x%3==0]
print (X)

