# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 21:49:51 2020

@author: Giancarlo
"""
import numpy as np

alfabeto= 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ@'
print("Cifrado de Hill")
#m = int(input("Introduce # de agrupaciones: "))
m=3
mensaje = str(input("Introduce el mensaje: "))
mensaje = mensaje.replace(' ', '@').upper()	 

"""
A=np.array([ [1,1,1],
             [2,1,1],
             [1,2,1] ])
"""
A=np.array([ [3,4,8],
             [2,0,1],
             [-3,1,0] ])

determinante=np.linalg.det(A)

#print("deteminante: ",determinante)

for i in range(0,m):
    if len(mensaje)%m!=0:
        mensaje=mensaje+'@'
    else:
        break

lista=[]
for i in mensaje:
    lista.append(   alfabeto.index(i)   ) 

#funcion para partir en m grupos la lista
def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs

listas=split(lista, m) 
#QUEDA asi por ejm:
#listas=[[1,2,3],[4,5,6],[7,8,9]]
#listas[0]=[1.2.3]

cifrado=[]
#multiplica A por cada grupo m
for i in range(0,len(listas)):
    B=np.array( listas[i] )   #array horizontal o matriz fila
    B=B.transpose()             #array vertical o matriz columna
    C=np.dot(A,B) 
    cifrado.append( C.tolist() )

l=len(alfabeto)


def lista_aplanada(lst):
    #esta funcion solo sirve para un nivel de aplanamiento
    #para mas niveles:
    #https://joedicastro.com/aplanar-listas-en-python.html
    return sum(lst, [])

cifrado_total=lista_aplanada(cifrado)


#creo una lista cir que tiene todos los elementos de cifrado_total y le aplica el mod(n)
cir=list( map(lambda x: x%l, cifrado_total) )
    

cifrado_final=''

for i in cir:
    cifrado_final+=alfabeto[ i ]
    
print("matriz usada:")
print(A)
print("mensaje:    ",mensaje) 
print("cifrado:    ",cifrado_final)
print("")
print("Descifrado")

Ainv=np.linalg.inv(A)

print("Matriz Inversa de A: ")
print(Ainv)

