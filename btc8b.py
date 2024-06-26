#learning python
import cmath
import numpy
import matplotlib.pyplot as plt
from numpy import random


i =1
j =3
k = i + j
print("i+j=",k)
c=complex(i,j)
print(c.real)
print("the real part of c = ",c.real)
print("the imaginary part of c = ",c.imag)
absc=abs(c)
print("abs(c)=",abs(c))


arr = numpy.array([1, 2, 3, 4, 5])
print(arr)
print(arr[1:5])
print(arr[:4])
print(arr[-3:-1])

for x in arr:
  print(x)

arr = numpy.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)

import numpy as np


#Find the indexes where the value is 4:
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

#log at base 10
print(np.log10(arr))

#Natural Log
print(np.log(arr))

#sorting arrays
print(np.sort(arr))

#Add the values in arr1 to the values in arr2:
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.add(arr1, arr2)
print(newarr)

#Generate a random normal distribution of size 2x3:
x = random.normal(size=(2, 3))
print(x)

#Draw out a sample for chi squared distribution with degree of freedom 2 with size 2x3:
x = random.chisquare(df=2, size=(2, 3))
print(x)


#pip install seaborn

import seaborn as sns

sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()

#normal (Gaussian) distribution
sns.distplot(random.normal(size=1000), hist=False)
plt.show()

sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()

