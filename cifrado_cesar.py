# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 23:42:05 2020

@author: Giancarlo
"""


#Cifrado Cesar
alfabeto= 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
print("Cifrado César")
mensaje = str(input("Introduce el mensaje: "))
mensaje = mensaje.replace(' ', '').upper()	 
d = int(input("Introduce el desplazamiento: "))

l=len(alfabeto)

if d>l or d<0:
    d=d%l

cifrado = '' 
descifrado = ''


for i in mensaje:
    x=alfabeto.find(i)+d
    cifrado+=alfabeto[x%l]
    
print("mensaje: ",mensaje)
print("desplazamiento: ",d)
print("cifrado: ",cifrado)

#descifrado 
for i in cifrado:
    x=alfabeto.find(i)-d
    descifrado+=alfabeto[x%l]

print("descifrado: ",descifrado)

print("")
print("descifrado sin saber desplazamiento:")

opciones=[]
elemento=''

for n in range(l):
    for i in cifrado:
        x=alfabeto.find(i)+n
        elemento+=alfabeto[x%l]
    opciones.append(elemento)
    elemento=''

for z in opciones:
    print(z)
