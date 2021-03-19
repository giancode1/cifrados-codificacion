# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:32:05 2020
@author: Giancarlo
"""

import numpy as np

alfabeto= 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ@'
print("Cifrado de Hill") 

while(True):    
    m=int(input("Matriz cuadrada, introduce m numero de filas: "))
    if m<2:
        print("m debe ser entero, positivo y mayor que 1")
    else:
        break


print("1 Usar matriz del programa\n2 Ingresar matriz: ")
opcion=int(input("Elige una opción 1 o 2 : "))
if opcion==1:
    if m==2:
        A=np.array([ [1,3],
                     [2,7] ])
    if m==3:
        A=np.array([ [1,1,1],
                     [2,1,1],
                     [1,2,1] ])
if opcion==2:
    while(True):
        try:
            A=np.ones((m,m),np.int16)
            for i in range(m):
                fila= list(map(int,input(f"Ingresa fila {i+1}: ").split()))
                A[i]=fila
                
            determinante=np.linalg.det(A) 
            if determinante!=1:
                print("El determinante es diferente de uno, det(A)=",determinante)
                print("Ingresa otra matriz")
            else:
                print("det(A)=",determinante)
                break # Importante romper la iteración si todo ha salido bien
        except ValueError:
            print("Ha ocurrido un error, ingresa bien los términos")
if opcion!=(1 or 2):
    raise ValueError("Error! elige bien")
    
while(True):
    try:
        mensaje = str(input("Introduce el mensaje: "))
        mensaje = mensaje.replace(' ', '@').upper()	 
        for i in mensaje:
            alfabeto.index(i)
        break
    except ValueError:
        print("Un caracter del mensaje no esta contenido en el alfabeto")
        print("Ingresa otro mensaje")
    


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
    
print("Matriz usada:")
print(A)
print("Mensaje:    ",mensaje) 
print("Cifrado:    ",cifrado_final)

Ainv=np.linalg.inv(A)
#  ,dtype=np.int16
#Av=Ainv.astype(int)    #no convierte el float bn a int 
Av = np.around(Ainv, 2)
print("Matriz Inversa de A: ")
print(Av)
