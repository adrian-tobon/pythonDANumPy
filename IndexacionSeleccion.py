import numpy as np

#indice basico
a = np.array([1,2,3,4,5])
print(a)
print(a[4])

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(b[0,1])

#rebanado de arreglo
c = np.arange(10)
print(c)
print(c[:5])
print(c[5:])
print(c[3:8])
print(c[::3])

#rebanado de matrices
d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(d)
print(d[:2,:2])
print(d[:,::2])

#array de indices
e = np.array([1,2,3,4,5,6,7,8,9])
indices=np.array([1,3,5])

print(e[indices])

#indexacion booleana
f = np.array([1,-1,-2,3,-3,3])
print(f)
condition = f>0
print(condition)
print(f[condition])