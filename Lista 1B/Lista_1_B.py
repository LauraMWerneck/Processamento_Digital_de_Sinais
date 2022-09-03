# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 20:22:34 2022

@author: Laura Martin Werneck
"""

""""""""""""" Exercicios Lista 1 B """""""""""""

from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np

""""""""""""" P2.11 """""""""""""

""" T1[x(n)] = x(n).u(n) """

n=np.array(range(101))
x1=np.random.rand(len(n))
x2=np.sqrt(10)*np.random.randn(len(n))

# sistema sob teste: y[n] = x[n]*u[n]

[u,n]=stepseq(0,0,100)
y1=x1*u
y2=x2*u

a=5                     # constante a
b=10                    # constante b
y=(a*x1+b*x2)*u

# verificar se é igual a a.y1 + b.y2, descontando erros numéricos 
diff = sum (abs(y - (a*y1 + b*y2)))   

if diff < 1e-5:
    print(' **** Sistema é linear ***')
else:
    print(' **** Sistema não é linear ***')
    
    
""" T2[x(n)] = x(n) + n.x(n+1) """

n = np.array(range(101))

x1 = np.random.rand(len(n))     """ Parte 2 do exercício """
[x11,n11] = sigshift(x1,n,-1)

x2 = np.sqrt(10)*np.random.randn(len(n))  """ Parte 2 do exercício """
[x21,n21] = sigshift(x2,n,-1)

[u,n] = stepseq(0,0,100)

[y11,nx] = sigmult(n,n,x11,n11)
[y12,nx] = sigadd(x1,n,y11,nx)

y1= y12 


[y21,nx] = sigmult(n,n,x21,n21)
[y22,nx] = sigadd(x2,n,y21,nx)


y2=x2 + n*x21

a=5                     # constante a
b=10                    # constante b
y=a*x1 + a*n*x11 +b*x2 + b*n*x21

# verificar se é igual a a.y1 + b.y2, descontando erros numéricos
diff = sum (abs(y - (a*y1 + b*y2)))  """ Conferir """   

if diff < 1e-5:
    print(' **** Sistema é linear ***')
else:
    print(' **** Sistema não é linear ***')
    
    
    
""" T3[x(n)] = x(n) + (1/2).x(n-2) - (1/3).x(n-3).x(2n) """




""" T4[x(n)] =  """



""" T5[x(n)] = x(2n) """




""" T6[x(n)] = round[x(n)] """
    
    
    
    
    
    
    
    
    
    
    
    
    