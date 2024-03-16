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

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[:4])
print(arr[-3:-1])
