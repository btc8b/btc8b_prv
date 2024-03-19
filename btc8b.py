#learning python
import cmath
import numpy

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

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)

arr = np.array([1, 2, 3, 4, 5, 4, 4])
