# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 20:47:38 2022

@author: Laura Martin Werneck
"""

import matplotlib.pyplot as plt
import numpy as np

############## P2.3 ##################
# Gere as seguintes sequências periódicas e plote suas amostras a partir do
# número de períodos indicado.

# Exercicio 1 
# x1(n) = {...,-2,-1,0,1,2,...} periódico
# Plotar 5 períodos

n = np.arange(-12,13)
x = np.array([-2,-1,0,1,2])
y = np.tile(x,5)

plt.figure()
plt.stem(n,y)
plt.title("Sequência exercício P2.3.1")

# Exercicio 2
# x2(n) = exp(0.1*n)[u(n)-u(n-20)]
# Plotar 3 peíodos 

n1=np.arange(0,20)
x=np.exp(0.1*n1)
plt.figure()
plt.stem(n1,x)
plt.title("exp(0.1*n)[u(n)-u(n-20)]")

n=np.arange(0,60)
y=np.tile(x,3)

plt.figure()
plt.stem(n,y)
plt.title("Sequência exercício P2.3.2")

# Exercicio 3
# x3(n) = sin(0.1*pi*n)[u(n)-u(n-10)]
# Plote 4 períodos

n1=np.arange(0,10)
x=np.sin(0.1*np.pi*n1)
plt.figure()
plt.stem(n1,x)
plt.title("sin(0.1*pi*n)[u(n)-u(n-10)]")

n=np.arange(0,40)
y=np.tile(x,4)

plt.figure()
plt.stem(n,y)
plt.title("Sequência exercício P2.3.3")

# Exercicio 4
# x4(n) = {...,1,2,3,...} + {...,1,2,3,4,...} periódicos
# 0 < n < 24
# Descobrir qual o período de x4(n)

n=np.arange(0,36)
x=np.array([1, 2, 3])
x1=np.tile(x,12)
plt.figure()
plt.stem(n,x1)
plt.title("Sequência {1,2,3}")

x=np.array([1, 2, 3, 4])
x2=np.tile(x,9)
plt.figure()
plt.stem(n,x2)
plt.title("Sequência {1,2,3,4}")


plt.figure()
plt.stem(n,x1+x2)
plt.title("Sequência exercício P2.3.4")
