# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 21:15:42 2022

@author: laura martin Werneck
"""
import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np

############## P2.4 ##################
# Dado x(n) = {2,4,-3,1,-5,4,7}. Gere e plote as amostras das sequências 
# a seguir:

# Criação de  x(n) = {2,4,-3,1,-5,4,7}
n=np.arange(-3, 4)
x=np.array([2, 4, -3, 1, -5, 4, 7])
plt.figure()
plt.stem(n,x)
plt.title("Sequência x[n]")

# Exercício 1
# x1(n) = 2x(n-3)+3x(n+4)-x(n)

[x11,n11] = sigshift(x,n,3)             # x(n-3)
[x12,n12] = sigshift(x,n,-4)            # x(n+4)
plt.figure()
plt.stem(n11,2*x11)                     # 2x(n-3)
plt.title("Sequência 2x(n-3)")
plt.axis([-8, 7, -18, 25])
plt.figure()
plt.stem(n12,3*x12)                     # 3x(n+4)
plt.title("Sequência 3x(n+4)")
plt.axis([-8, 7, -18, 25])
[x1a,n1a] = sigadd(2*x11,n11,3*x12,n12) # 2x(n-3)+3x(n+4)
[x1,n1] = sigadd(x1a,n1a,-x,n)          # 2x(n-3)+3x(n+4)-x(n)
plt.figure()
plt.stem(n1,x1)
plt.title("Sequência exercício 2.4.1")
plt.axis([-8, 7, -18, 25])

# Exercício 2
# x2(n) = 4x(n+4)+5x(n+5)+2x(n)

[x21,n21] = sigshift(x,n,-4)                # x(n+4)
[x22,n22] = sigshift(x,n,-5)                # x(n+5)
plt.figure()
plt.stem(n21,4*x21)                         # 4x(n+4) 
plt.title("Sequência 4x(4+n)")
plt.axis([-9, 4, -22, 60])
plt.figure()
plt.stem(n22,5*x22)                         # 5x(n+5)
plt.title("Sequência 5x(n+5)")
plt.axis([-9, 4, -22, 60])
[x2a,n2a] = sigadd(4*x21,n21,5*x22,n22);    # 4x(n+4)+5x(n+5)
plt.figure()
plt.stem(n,2*x)                             # 2x(n)
plt.title("Sequência 2x(n)")
plt.axis([-9, 4, -22, 60]) 
[x2,n2] = sigadd(x2a,n2a,2*x,n);            # 4x(n+4)+5x(n+5)+2x(n)
plt.figure()
plt.stem(n2,x2)
plt.title("Sequência exercício 2.4.2")
plt.axis([-9, 4, -22, 60]) 

# Exercício 3
# x3(n) = x(n+3)*x(n-2)+x(1-n)*x(n+1)

[x31,n31] = sigshift(x,n,-3)                # x(n+3)
[x32,n32] = sigshift(x,n,2)                 # x(n-2)
plt.figure()
plt.stem(n31,x31)
plt.title("Sequência x(n+3)")
plt.axis([-7, 6, -22, 54])
plt.figure()
plt.stem(n32,x32)
plt.title("Sequência x(n-2)")
plt.axis([-7, 6, -22, 54])
[x33,n33] = sigmult(x31,n31,x32,n32)        # x(n+3)*x(n-2)
plt.figure()
plt.stem(n33,x33)
plt.title("Sequência x(n+3).x(n-2)")
plt.axis([-7, 6, -22, 54]) 
[x34a,n34a] = sigfold(x,n)                  # x(-n)
plt.figure()
plt.stem(n34a,x34a)
plt.title("Sequência x(-n)")
plt.axis([-7, 6, -22, 54])  
[x34,n34] = sigshift(x34a,n34a,1)           # x(1-n)
plt.figure()
plt.stem(n34,x34)
plt.title("Sequência x(-(n-1))")
plt.axis([-7, 6, -22, 54])  
[x35,n35] = sigshift(x,n,-1)                # x(n+1)
plt.figure()
plt.stem(n35,x35)
plt.title("Sequência x(n+1)")
plt.axis([-7, 6, -22, 54])    
[x36,n36] = sigmult(x34,n34,x35,n35)        # x(1-n)*x(n+1)
plt.figure()
plt.stem(n36,x36)
plt.title("Sequência x(1-n).x(n+1)")
plt.axis([-7, 6, -22, 54])   
[x3,n3] = sigadd(x33,n33,x36,n36)           # x(n+3)*x(n-2)+x(1-n)*x(n+1)
plt.figure()
plt.stem(n3,x3)
plt.title("Sequência exercício 2.4.3")
plt.axis([-7, 6, -22, 54])

# Exercício 4
# x4(n) = 2exp^(0,5n) * x(n) + cos(0,1*pi*n)*x(n+2) 
# -10 < n < 10

n41=np.arange(-10, 11)                  # -n até n-1 entao de -10 ate 10 mas o phyton usa n+1 como limite
x41=2*np.exp(0.5*n41)                   #  2exp^(0,5n)
plt.figure()
plt.stem(n41,x41)
plt.title("Sequência 2*exp(0.5*n)")
plt.axis([-11, 11, -12, 300])
[x42,n42] = sigmult(x41,n41,x,n)        #  2exp^(0,5n) * x(n)
plt.figure()
plt.stem(n42,x42)
plt.title("Sequência 2*exp(0.5*n).x(n)")
plt.axis([-11, 11, -12, 300])
x43=np.cos(0.1*np.pi*n41)               # cos(0,1*pi*n)
plt.figure()
plt.stem(n41,x43)
plt.title("Sequência cos(0.1*pi*n)")
plt.axis([-11, 11, -1.2, 1.2]) 
[x44,n44] = sigshift(x,n,-2)            # x(n+2)
plt.figure()
plt.stem(n44,x44)
plt.title("Sequência x(n+2)")
plt.axis([-11, 11, -12, 12]) 
[x45,n45] = sigmult(x43,n41,x44,n44)    # cos(0,1*pi*n)*x(n+2)
plt.figure()
plt.stem(n45,x45)
plt.title("Sequência cos(0.1*pi*n).x(n+2)")
plt.axis([-11, 11, -12, 12]) 
[x4,n4] = sigadd(x42,n42,x45,n45)       # 2exp^(0,5n) * x(n) + cos(0,1*pi*n)*x(n+2)
plt.figure()
plt.stem(n4,x4)
plt.title("Sequência exercício 2.4.4")
plt.axis([-11, 11, -12, 70])

