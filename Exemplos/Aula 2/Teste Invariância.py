# Teste para verificar a invariancia ao tempo de um sistema

from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np

nx=np.array(range(101))
x=np.sqrt(10)*np.random.randn(len(nx))

# sistema sob teste: y[n] = x[n]*u[n]
delay = 1                       # atraso               
[u,nu] = stepseq(0,0,100)
y = x*u
[y1,ny1] = sigshift(y,nx,delay) #y[n-delay]

[x1,nx1] = sigshift(x,nx,delay) #x[n-delay]
[y2,ny2] = sigmult(x1,nx1,u,nu) #T{x[n-delay]}

[diff,ndiff]=sigadd(y1,ny1,-y2,ny2)
vdiff=sum(abs(diff))

if vdiff < 1e-5:
    print(' **** Sistema é Invariante no Tempo ***')
else:
    print(' **** Sistema não é Invariante no Tempo ***')
