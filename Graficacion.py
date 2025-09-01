import matplotlib.pyplot as plt
import numpy as np

#grafico de dispersion
x = np.random.rand(50)
y = np.random.rand(50)

print(x)
print(y)

'''plt.scatter(x,y)
plt.title("prueba")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
'''

#grafico de funciones

#f(x) = x^2 -4x + 4
'''x = np.linspace(-1,5,5)
y = x**2 -4*x + 4


plt.figure(figsize=(8,4))
plt.plot(x,y,label="f(x) = x^2 -4x + 4",color=(0,0,0),linestyle=":",marker='^')
plt.title("Grafica de la funcion cuadratica")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend(loc='best')
plt.show()
'''
#multiples graficos
#subplot
x = np.linspace(0,10,100)
y_lineal = x
y_exponential = np.exp(x)

'''
plt.figure(figsize=(10,4))
plt.subplot(2,1,1)
plt.plot(x,y_lineal,'r-')
plt.title("Funcion Lineal")
plt.xlabel("x")
plt.ylabel("y)")
plt.grid(True)
plt.tight_layout(pad=5.0)
plt.subplot(2,1,2)
plt.plot(x,y_exponential,'r-')
plt.title("Funcion Cuadratica")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

plt.figure(figsize=(10,4))
plt.plot(x,y_lineal,'g-')
plt.plot(x,y_exponential)
plt.xlabel("x")
plt.ylabel("y)")
plt.ylim(0,10)
plt.xlim(0,10)
plt.grid(True)
plt.show()
'''
#subplots
fig,axs = plt.subplots(2,2,figsize=(10,10))

x =np.linspace(0,2*np.pi,100)
funcs = [np.sin(x),np.cos(x),np.tan(x),np.sqrt(x)]

titles = ['Seno','Coseno','Tangente','Raiz Cuadrada']

for ax,func,title in zip(axs.ravel(),funcs,titles):
    ax.plot(x,func)
    ax.set_title(title)
    ax.grid(True)

plt.tight_layout(pad=2)
plt.show()   