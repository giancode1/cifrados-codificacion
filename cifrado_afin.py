# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 21:28:24 2020

@author: Giancarlo
"""


#CIFRADO AFIN
#C(x)=(ax+b)mod(n)

alfabeto= 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
print("Cifrado Afín")
mensaje = str(input("Introduce el mensaje: "))
mensaje = mensaje.replace(' ', '').upper()	 
a = int(input("Introduce a: "))
b = int(input("Introduce b: "))

l=len(alfabeto)
 
if b>l or b<0:
    b=b%l

cifrado = '' 
descifrado = ''

 
for i in mensaje:
    x=a*alfabeto.find(i)+b
    cifrado+=alfabeto[x%l]
    
print("mensaje:    ",mensaje)
print("cifrado:    ",cifrado)


#descifrado 
#a1 es el a^(-1)
for a1 in range(0,l):
    if (a1*a)%l==1:
        break

for i in cifrado: 
    x=a1*(alfabeto.find(i)-b)
    descifrado+=alfabeto[x%l]

print("descifrado: ",descifrado)

