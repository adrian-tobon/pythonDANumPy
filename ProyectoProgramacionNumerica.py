import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
#df = pd.read_csv('pasajeros.csv')

#obtencion de datos y graficacion
data = np.genfromtxt(url,delimiter=',',skip_header=1,usecols=1)
print(data)



#normalizamos(linealizamos) la distribucion de los datos
log_data = np.log(data)


x = np.arange(1,len(data)+1)
X = np.column_stack((np.ones(len(x)),x))

#modelacion exponencial
X_pinv = np.linalg.pinv(X)
params = np.dot(X_pinv,log_data)

log_A = params[0]
B = params[1]
A = np.exp(log_A)


fitted_values = A * np.exp(B * x)


plt.figure(figsize=(10,6))
plt.plot(data,label="Datos originales",linestyle='--',marker='o')
plt.plot(fitted_values,label='Modelo Ajustado', color='red')
plt.title('Pasajeros de Aerolineas (1949-1960)')
plt.xlabel('Meses desde enero 1949')
plt.ylabel('Numero de pasajeros')
plt.grid(True)
plt.legend()
plt.show()