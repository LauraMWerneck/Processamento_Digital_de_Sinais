#Teste para verificar a linearidade de um sistema

from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np

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
