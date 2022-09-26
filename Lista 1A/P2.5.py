# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:35:21 2022

@author: laura
"""

import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np

############## P2.5 ##################
# A sequência exponencial complexa exp^(jw0n) ou a sequência cossenoidal cos(w0n) 
# são periódicas se a frequência normalizada f0=w0/2pi for um número racional.
# Isto é, f0=K/N onde K e N são um inteiros.

# Exercício 1
# Prove o resultado acima
'''
e^[jw0(n+N)] = e^(jw0n).e^(jw0N) = e^(jw0n) se w0N = K.2pi
ou
2.pi.f0.N = K.2.pi
f0 = K/N
f0 = 0.1/2 = 1/20 = K/N
K é quantidade de períodos da função analógica em N pontos
N é periodicidade real do sinal digital (se repete a cada N pontos)
'''

# Exercício 2
# Gere exp^(0,1pin), -100 < n < 100. Trace suas partes reais e imaginárias usando a 
# função stem. Essa sequência é periódica? Se for qual é o seu período 
# fundamental? Da análise do gráfico, qual a interpretação que se pode dar dos 
# inteiros K e N acima?
n=np.arange(-100, 101)
alpha = 0.1*np.pi*1j
x = np.exp(alpha*n)
plt.figure()
plt.stem(n,np.real(x))
plt.title("Parte REAL")

plt.figure()
plt.stem(n,np.imag(x))
plt.title("Parte IMAGINÁRIA")

# Sim, é periódica, com período 20, f0 = K/N= 1/20 como esperado K e N sendo números
# inteiros a sequência é periódica.

# Exercicio 3
# Gere e plote cos(0,1n), -20 < n < 20. Essa sequência é  preiódica? O que você 
# conclui do gráfico?

n=np.arange(-75, 76)
x = np.cos(0.1*n)
plt.figure()
plt.stem(n,x)
plt.title("Sequência cos(0.1n)")

# O sinal não é periódico, pois as amostras não se repetem nunca (num período fixo) - pois f0 não é um número racional.

