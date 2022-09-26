"""
Created on Fri Aug 26 19:42:11 2022

@author: Laura Martin Werneck
"""

import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np

# Lista de Exercicio 1


############ P2.1 ############

# Gere as seguintes sequencias usando as funções básicas de sinais e as 
# operações de sinais presentes no arquivo fDSP. Plotar amostrar de sinais 
# usando a função stem.


#Exercicio 1 

# x1(n)=3£(n+2)+2£(n)-£(n-3)+5£(n-7) , -5 < n < 15

[x11,n] = impseq(-2,-5,15) 
[x12,n] = impseq(0,-5,15)
[x13,n] = impseq(3,-5,15) 
[x14,n] = impseq(7,-5,15)

x1 = 3*x11 + 2*x12- x13 + 5*x14

plt.figure()
plt.stem(n,x1)
plt.title("Sequência x1[n]")


# Exercicio 2  

x2 = 0
# Ou x2 = np.zeros(21)

for i in range(-5, 6):
#Ou for k in range(-5,6):
    
    [x21,n] = impseq(2*i,-10,10) 
    x21 = x21*np.exp(- np.abs(i))
    x2=x2+x21
    
plt.figure()
plt.stem(n,x2)    
plt.title("Sequência x2[n]")


# Exercicio 3

[x31,n] = stepseq(0,0,20)    
[x32,n] = stepseq(5,0,20)
[x33,n] = stepseq(10,0,20)
[x34,n] = stepseq(15,0,20)

x3 = 10*x31 - 5*x32 - 10*x33 + 5*x34

plt.figure()
plt.stem(n,x3)
plt.title("Sequência x3[n]")


# Exercicio 4

[x41,n] = stepseq(-20,-30,20)    
[x42,n] = stepseq(10,-30,20)

x4 = np.exp(0.1*n)*(x41 - x42)

plt.figure()
plt.stem(n,x4)
plt.title("Sequência x4[n]")


# Exericio 5

n = np.array(range(-200, 201))

x51 = np.cos(0.49*np.pi*n)
x52 = np.cos(0.51*np.pi*n)

x5 = 5*(x51 + x52)
# Ou x5 = 5*(np.cos(0.49*np.pi*n) + np.cos(0.51*np.pi*n))

plt.figure()
plt.stem(n,x5)
plt.title("Sequência x5[n]")

# Gráfico: modulação em amplitude

# Exercicio 6

n = np.array(range(-200, 201))

x61 = np.sin(0.01*np.pi*n)
x62 = np.cos(0.5*np.pi*n)

x6 = 2*x61*x62
# Ou x6 = 2*np.sin(0.01*np.pi*n)*np.cos(0.5*np.pi*n)

plt.figure()
plt.stem(n,x6)
plt.title("Sequência x6[n]")

# Gráfico: modulação em amplitude

# Exercicio 7

n = np.array(range(101))

x71 = np.sin(0.1*np.pi*n + np.pi/3)

x7 = np.exp(-0.05*n)*x71
# Ou x7 = np.exp(-0.05*n)*np.sin(0.1*np.pi*n +np.pi/3)

plt.figure()
plt.stem(n,x7)
plt.title("Sequência x7[n]")

# Gráfico: oscilação amortecida

# Exercicio 8 

n = np.array(range(101))

x81 = np.sin(0.1*np.pi*n)

x8 = np.exp(0.01*n)*x81

plt.figure()
plt.stem(n,x8)
plt.title("Sequência x8[n]")

# Gráfico: oscilação com ressonância

plt.show()

