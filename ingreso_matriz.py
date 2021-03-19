# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:54:51 2020
@author: Giancarlo
"""
import numpy as np

#INTRODUCE MATRIZ CUADRADA POR ELEMENTO 
m=int(input("Introduce m numero de filas: "))
Z=[]
fila=[]
for i in range(1,m+1):
    for j in range(1,m+1):
        #print("Introduce a{}{}: ".format(i,j))
        print(f"Introduce a{i}{j}: ")
        elem=int(input())
        fila.append(elem)
    Z.append(fila)
    fila=[]

A=np.array(Z)
print("Matriz A: ")
print(A)


#Introduce matriz fila separada por espacios unicamente 
op= list(map(int,input("ingresa: ").split()))
op = np.asarray(op)


#Introduce matriz cuadrada, ingresando fila , la fila debe tener solo espacios 
m=int(input("Introduce m numero de filas: "))
A=np.ones((m,m),np.int16)
for i in range(m):
    fila= list(map(int,input("Ingresa fila: ").split()))
    A[i]=fila


#Introduce matriz mxn ingresando fila , la fila debe tener solo espacios 
m=int(input("Introduce m numero de filas: "))
n=int(input("Introduce n numero de columnas: "))
A=np.ones((m,n),np.int16)
for i in range(m):
    fila= list(map(int,input(f"Ingresa fila{i+1}: ").split()))
    A[i]=fila



