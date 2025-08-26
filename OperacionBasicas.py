from tokenize import _all_string_prefixes
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

#suma y resta, deben tener elmismo tamaño
print(a+b)
print(a-b)

#suma y resta con un escalar
print(a+2)
print(b-10)

#multiplicacion y division de arreglos, se hace elemento a elemento
print(a*b)
print(a/b)

#multiplicar o dividir por un escalar
print(a*10)
print(b/10)